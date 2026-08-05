#!/usr/bin/env python3
"""
KnowpareX 全課程自動重寫器
==========================

用途：
1. 從 src/knowparex/data/curriculum_integrated.js 讀出全部課程單元。
2. 逐單元呼叫 OpenAI Responses API，重新撰寫主題專屬教材。
3. 自動檢查常見跨主題污染、模板文字、內容不足與 JSON 結構。
4. 支援中斷續跑、失敗重試、分批執行、預覽與備份。
5. 全部通過後，才將結果寫回 curriculum_integrated.js。

重要：
- 這是「自動重寫＋自動稽核」工具，不等於各科教師逐篇審定。
- 預設不直接覆寫資料；必須最後明確執行 `apply`。
- API 會產生費用。816 個單元可能需要不少時間與額度。

安裝：
    python3 -m pip install --upgrade openai

設定 API key：
    export OPENAI_API_KEY="你的 API key"

典型流程：
    python3 knowparex_rewrite_all.py scan
    python3 knowparex_rewrite_all.py rewrite --workers 3
    python3 knowparex_rewrite_all.py audit
    python3 knowparex_rewrite_all.py apply --require-all

先測 10 個：
    python3 knowparex_rewrite_all.py rewrite --limit 10 --workers 2

重新處理失敗項目：
    python3 knowparex_rewrite_all.py rewrite --only-failed --workers 2

查看進度：
    python3 knowparex_rewrite_all.py status
"""

from __future__ import annotations

import argparse
import concurrent.futures
import copy
import hashlib
import json
import os
import re
import shutil
import sys
import threading
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

ROOT = Path.cwd()
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

try:
    from knowparex.curriculum_adapter import load_curriculum_js
    from knowparex.curriculum_rebuild import write_curriculum_js
except ImportError as exc:
    raise SystemExit(
        "找不到 KnowPareX 原始碼。請把本檔案放到 KnowPareX 專案根目錄再執行。"
    ) from exc

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # type: ignore[assignment]

CURRICULUM_PATH = ROOT / "src/knowparex/data/curriculum_integrated.js"
WORK_DIR = ROOT / ".knowparex_rewrite"
UNITS_FILE = WORK_DIR / "units.json"
RESULTS_DIR = WORK_DIR / "results"
FAILURES_FILE = WORK_DIR / "failures.json"
AUDIT_FILE = WORK_DIR / "audit.json"
RUN_LOG = WORK_DIR / "run.log"

DEFAULT_MODEL = os.environ.get("KNOWPAREX_REWRITE_MODEL", "gpt-5")
PRINT_LOCK = threading.Lock()

GENERIC_FRAGMENTS = (
    "能精確定義",
    "列出成立條件、相關概念與限制",
    "逐步論證",
    "先提出可測量問題",
    "設定一個自變因與一個應變因",
    "用表格和圖形判斷資料是否支持假設",
)

SUSPICIOUS_PHRASES_BY_SUBJECT: dict[str, tuple[str, ...]] = {
    "math": (
        "葉綠體", "卡爾文循環", "粒線體", "同名磁極相斥",
        "氧化數上升", "莫耳質量", "DNA複製",
    ),
    "physics": (
        "卡爾文循環", "等位基因", "氧化數上升", "莫耳質量",
        "酸鹼指示劑", "細胞膜",
    ),
    "chemistry": (
        "牛頓第二定律ΣF=ma", "卡爾文循環", "遺傳漂變",
        "拋物線的對稱軸", "同名磁極相斥",
    ),
    "biology": (
        "密度ρ=質量m÷體積V", "串聯電流相同",
        "牛頓第二定律ΣF=ma", "二次函數頂點", "莫耳質量",
    ),
    "earth_science": (
        "卡爾文循環", "串聯電流相同", "氧化數上升",
        "二次函數頂點", "莫耳質量",
    ),
    "language": (
        "牛頓第二定律ΣF=ma", "密度ρ=質量m÷體積V",
        "卡爾文循環", "氧化數上升",
    ),
}

RESPONSE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "title",
        "paragraphs",
        "key_points",
        "formulas",
        "quality_notes",
    ],
    "properties": {
        "title": {"type": "string"},
        "paragraphs": {
            "type": "array",
            "minItems": 2,
            "maxItems": 5,
            "items": {"type": "string"},
        },
        "key_points": {
            "type": "array",
            "minItems": 3,
            "maxItems": 8,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "topic",
                    "explanation",
                    "example",
                    "common_trap",
                ],
                "properties": {
                    "topic": {"type": "string"},
                    "explanation": {"type": "string"},
                    "example": {"type": "string"},
                    "common_trap": {"type": "string"},
                },
            },
        },
        "formulas": {
            "type": "array",
            "maxItems": 10,
            "items": {"type": "string"},
        },
        "quality_notes": {
            "type": "array",
            "maxItems": 8,
            "items": {"type": "string"},
        },
    },
}


def log(message: str) -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().isoformat(timespec="seconds")
    with PRINT_LOCK:
        print(message, flush=True)
        with RUN_LOG.open("a", encoding="utf-8") as handle:
            handle.write(f"[{stamp}] {message}\n")


def walk_units(
    node: Any,
    path: tuple[str, ...] = (),
) -> Iterable[tuple[tuple[str, ...], dict[str, Any]]]:
    if isinstance(node, dict):
        if isinstance(node.get("name"), str) and isinstance(
            node.get("lessonDetails"), dict
        ):
            yield path, node
        for key, value in node.items():
            yield from walk_units(value, path + (str(key),))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_units(value, path + (str(index),))


def subject_from_path(path: tuple[str, ...]) -> str:
    joined = " ".join(path).casefold()
    if "數學" in joined or "math" in joined:
        return "math"
    if "物理" in joined or "physics" in joined:
        return "physics"
    if "化學" in joined or "chemistry" in joined:
        return "chemistry"
    if "生物" in joined or "biology" in joined:
        return "biology"
    if any(x in joined for x in ("地科", "地球科學", "earth")):
        return "earth_science"
    if any(x in joined for x in ("國文", "英文", "英語", "chinese", "english")):
        return "language"
    if "自然" in joined or "science" in joined:
        return "science"
    return "other"


def stable_id(path: tuple[str, ...], title: str) -> str:
    raw = "/".join(path + (title,))
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    return digest


def flatten_existing(unit: dict[str, Any]) -> dict[str, Any]:
    details = unit.get("lessonDetails", {}) or {}
    paragraphs = details.get("readableLesson") or details.get("lessonText") or []
    points = details.get("keyPoints") or []
    return {
        "paragraphs": [str(x) for x in paragraphs if str(x).strip()],
        "key_points": [
            {
                "topic": str(p.get("topic", "")),
                "explanation": str(p.get("explanation", "")),
                "example": str(p.get("example", "")),
                "common_trap": str(p.get("commonTrap", "")),
            }
            for p in points
            if isinstance(p, dict)
        ],
        "formulas": [
            str(x)
            for x in (details.get("formulas") or [])
            if str(x).strip()
        ],
    }


def scan_units() -> list[dict[str, Any]]:
    data = load_curriculum_js(CURRICULUM_PATH)
    units: list[dict[str, Any]] = []
    for path, unit in walk_units(data):
        title = str(unit.get("name", "")).strip()
        unit_id = stable_id(path, title)
        subject_key = path[0] if path else subject_from_path(path)
        book = {}
        if len(path) >= 2 and subject_key in data:
            try:
                book = data[subject_key][int(path[1])]
            except (IndexError, TypeError, ValueError):
                book = {}
        units.append({
            "id": unit_id,
            "path": list(path),
            "title": title,
            "subject": subject_key,
            "stage": str(book.get("stage", "")),
            "book": str(book.get("book", "")),
            "existing": flatten_existing(unit),
        })
    units.sort(key=lambda item: (item["subject"], item["path"], item["title"]))
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    UNITS_FILE.write_text(
        json.dumps(
            {"unit_count": len(units), "units": units},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    log(f"已掃描 {len(units)} 個單元：{UNITS_FILE}")
    return units


def load_units() -> list[dict[str, Any]]:
    if not UNITS_FILE.exists():
        return scan_units()
    payload = json.loads(UNITS_FILE.read_text(encoding="utf-8"))
    return payload["units"]


def result_path(unit_id: str) -> Path:
    return RESULTS_DIR / f"{unit_id}.json"


def build_prompt(unit: dict[str, Any]) -> str:
    path_text = " / ".join(unit["path"])
    existing = json.dumps(unit["existing"], ensure_ascii=False, indent=2)
    return f"""
你正在重寫臺灣學校課程的單一教材單元。

課程位置：{path_text}
學科分類：{unit['subject']}
唯一且不可更改的單元名稱：{unit['title']}

目前舊內容如下。舊內容可能包含嚴重跨主題污染，只能當作問題線索，
不能假設它是正確資料：
{existing}

請從零重寫這個單元，遵守下列規則：

1. 內容必須只服務「{unit['title']}」。
2. 使用繁體中文，適合該課程階段的學生。
3. 正文 2 到 5 段，每段都要提供實質知識，禁止空泛模板。
4. 重點知識至少 3 點；每點必須有不同的概念、解釋、具體例子和常見誤區。
5. 公式只能加入這個單元真正需要而且正確的公式。沒有必要就回傳空陣列。
6. 禁止把別的單元常見公式硬塞進來。
7. 例子必須直接示範該重點，不能使用通用「設計實驗」模板。
8. 若有數值例題，請自行核算。
9. 不要提及你是 AI、舊資料、重寫流程或審核。
10. title 必須完全等於「{unit['title']}」。
11. quality_notes 只記錄你在寫作時主動檢查過的事項，例如：
    「已確認公式與單位一致」；它不會顯示給學生。
12. 輸出只能符合指定 JSON schema。
""".strip()


def extract_json_text(response: Any) -> str:
    text = getattr(response, "output_text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()

    output = getattr(response, "output", None)
    if output:
        chunks: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                part_text = getattr(part, "text", None)
                if part_text:
                    chunks.append(str(part_text))
        if chunks:
            return "\n".join(chunks).strip()

    raise ValueError("API 回應沒有可解析的文字輸出。")


def call_model(
    client: Any,
    unit: dict[str, Any],
    model: str,
    use_web_search: bool,
) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "model": model,
        "instructions": (
            "你是嚴謹的臺灣課程教材編輯。"
            "不要沿用明顯錯置的舊內容。"
            "遇到不確定的專有事實時採保守、教科書式寫法。"
        ),
        "input": build_prompt(unit),
        "text": {
            "format": {
                "type": "json_schema",
                "name": "knowparex_lesson",
                "strict": True,
                "schema": RESPONSE_SCHEMA,
            }
        },
        "store": False,
    }
    if use_web_search:
        kwargs["tools"] = [{"type": "web_search"}]

    response = client.responses.create(**kwargs)
    payload = json.loads(extract_json_text(response))
    return payload


def lesson_text(lesson: dict[str, Any]) -> str:
    parts: list[str] = [str(lesson.get("title", ""))]
    parts.extend(str(x) for x in lesson.get("paragraphs", []))
    parts.extend(str(x) for x in lesson.get("formulas", []))
    for point in lesson.get("key_points", []):
        if isinstance(point, dict):
            parts.extend(
                str(point.get(key, ""))
                for key in ("topic", "explanation", "example", "common_trap")
            )
    return "\n".join(parts)


def audit_lesson(unit: dict[str, Any], lesson: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    expected_title = unit["title"]
    if lesson.get("title") != expected_title:
        issues.append("title_mismatch")

    paragraphs = lesson.get("paragraphs")
    points = lesson.get("key_points")
    formulas = lesson.get("formulas")

    if not isinstance(paragraphs, list) or len(paragraphs) < 2:
        issues.append("too_few_paragraphs")
    if not isinstance(points, list) or len(points) < 3:
        issues.append("too_few_key_points")
    if not isinstance(formulas, list):
        issues.append("formulas_not_list")

    text = lesson_text(lesson)
    compact = re.sub(r"\s+", "", text)

    if expected_title not in text:
        issues.append("title_not_discussed")
    if len(compact) < 260:
        issues.append("content_too_short")

    for fragment in GENERIC_FRAGMENTS:
        if fragment in text:
            issues.append(f"generic_template:{fragment}")

    subject = unit["subject"]
    for phrase in SUSPICIOUS_PHRASES_BY_SUBJECT.get(subject, ()):
        if phrase in text:
            issues.append(f"suspicious_cross_subject:{phrase}")

    normalized_lines = [
        re.sub(r"\s+", "", line).strip("。；，、:：")
        for line in text.splitlines()
    ]
    counts = Counter(line for line in normalized_lines if len(line) >= 28)
    if any(count > 1 for count in counts.values()):
        issues.append("duplicate_long_sentence")

    topics: list[str] = []
    if isinstance(points, list):
        for index, point in enumerate(points, start=1):
            if not isinstance(point, dict):
                issues.append(f"key_point_{index}:not_object")
                continue
            topic = str(point.get("topic", "")).strip()
            explanation = str(point.get("explanation", "")).strip()
            example = str(point.get("example", "")).strip()
            if not topic:
                issues.append(f"key_point_{index}:missing_topic")
            else:
                topics.append(topic)
            if len(explanation) < 20:
                issues.append(f"key_point_{index}:weak_explanation")
            if len(example) < 12:
                issues.append(f"key_point_{index}:weak_example")

    if len(set(topics)) != len(topics):
        issues.append("duplicate_key_point_topics")

    return sorted(set(issues))


def rewrite_one(
    client: Any,
    unit: dict[str, Any],
    model: str,
    use_web_search: bool,
    retries: int,
) -> tuple[str, bool, str]:
    path = result_path(unit["id"])
    last_error = ""

    for attempt in range(1, retries + 1):
        try:
            lesson = call_model(client, unit, model, use_web_search)
            issues = audit_lesson(unit, lesson)
            record = {
                "id": unit["id"],
                "path": unit["path"],
                "title": unit["title"],
                "subject": unit["subject"],
                "model": model,
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "audit_passed": not issues,
                "audit_issues": issues,
                "lesson": lesson,
            }
            path.write_text(
                json.dumps(record, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            if not issues:
                return unit["id"], True, "通過"
            last_error = "；".join(issues)
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"

        if attempt < retries:
            time.sleep(min(2 ** attempt, 12))

    return unit["id"], False, last_error


def select_units(
    units: list[dict[str, Any]],
    limit: int | None,
    start: int,
    only_failed: bool,
    force: bool,
    subject: str | None = None,
    stage: str | None = None,
) -> list[dict[str, Any]]:
    failures: set[str] = set()
    if only_failed and FAILURES_FILE.exists():
        payload = json.loads(FAILURES_FILE.read_text(encoding="utf-8"))
        failures = set(payload.get("failed_ids", []))

    selected: list[dict[str, Any]] = []
    for unit in units[start:]:
        if subject and unit.get("subject") != subject:
            continue
        if stage and unit.get("stage") != stage:
            continue
        path = result_path(unit["id"])
        if only_failed and unit["id"] not in failures:
            continue
        if path.exists() and not force and not only_failed:
            try:
                existing = json.loads(path.read_text(encoding="utf-8"))
                if existing.get("audit_passed"):
                    continue
            except Exception:
                pass
        selected.append(unit)
        if limit is not None and len(selected) >= limit:
            break
    return selected


def rewrite_all(args: argparse.Namespace) -> None:
    if OpenAI is None:
        raise SystemExit(
            "尚未安裝 openai。請執行：python3 -m pip install --upgrade openai"
        )
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("找不到 OPENAI_API_KEY 環境變數。")

    units = load_units()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    selected = select_units(
        units,
        args.limit,
        args.start,
        args.only_failed,
        args.force,
        args.subject,
        args.stage,
    )
    if not selected:
        log("沒有需要處理的單元。")
        return

    client = OpenAI()
    log(
        f"準備重寫 {len(selected)} 個單元；model={args.model}；"
        f"workers={args.workers}；web_search={args.web_search}"
    )

    failures: dict[str, str] = {}
    completed = 0

    def worker(unit: dict[str, Any]) -> tuple[str, bool, str]:
        return rewrite_one(
            client,
            unit,
            args.model,
            args.web_search,
            args.retries,
        )

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max(1, args.workers)
    ) as executor:
        future_map = {
            executor.submit(worker, unit): unit
            for unit in selected
        }
        for future in concurrent.futures.as_completed(future_map):
            unit = future_map[future]
            completed += 1
            try:
                _, passed, message = future.result()
            except Exception as exc:
                passed = False
                message = f"{type(exc).__name__}: {exc}"
            if passed:
                log(f"[{completed}/{len(selected)}] ✓ {unit['title']}")
            else:
                failures[unit["id"]] = message
                log(
                    f"[{completed}/{len(selected)}] ✗ "
                    f"{unit['title']}：{message}"
                )

    FAILURES_FILE.write_text(
        json.dumps(
            {
                "failed_count": len(failures),
                "failed_ids": sorted(failures),
                "errors": failures,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    log(
        f"本輪完成：成功 {len(selected) - len(failures)}，"
        f"失敗 {len(failures)}。"
    )


def audit_all() -> dict[str, Any]:
    units = load_units()
    passed = 0
    missing: list[dict[str, str]] = []
    failed: list[dict[str, Any]] = []

    for unit in units:
        path = result_path(unit["id"])
        if not path.exists():
            missing.append({"id": unit["id"], "title": unit["title"]})
            continue
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            lesson = record["lesson"]
            issues = audit_lesson(unit, lesson)
        except Exception as exc:
            issues = [f"invalid_result:{type(exc).__name__}:{exc}"]

        if issues:
            failed.append({
                "id": unit["id"],
                "title": unit["title"],
                "issues": issues,
            })
        else:
            passed += 1

    report = {
        "total": len(units),
        "passed": passed,
        "failed": len(failed),
        "missing": len(missing),
        "failed_units": failed,
        "missing_units": missing,
    }
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_FILE.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    FAILURES_FILE.write_text(
        json.dumps(
            {
                "failed_count": len(failed) + len(missing),
                "failed_ids": [
                    x["id"] for x in failed
                ] + [
                    x["id"] for x in missing
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def find_units_by_id(data: Any) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for path, unit in walk_units(data):
        title = str(unit.get("name", "")).strip()
        mapping[stable_id(path, title)] = unit
    return mapping


def apply_results(require_all: bool) -> None:
    report = audit_all()
    if require_all and (
        report["failed"] > 0 or report["missing"] > 0
    ):
        raise SystemExit(
            "尚未全量通過，拒絕寫回。"
            f" failed={report['failed']} missing={report['missing']}"
        )

    units = load_units()
    data = load_curriculum_js(CURRICULUM_PATH)
    targets = find_units_by_id(data)
    applied = 0

    for unit in units:
        path = result_path(unit["id"])
        if not path.exists():
            continue
        record = json.loads(path.read_text(encoding="utf-8"))
        lesson = record.get("lesson")
        if not isinstance(lesson, dict):
            continue
        issues = audit_lesson(unit, lesson)
        if issues:
            continue

        target = targets.get(unit["id"])
        if target is None:
            continue

        details = target.setdefault("lessonDetails", {})
        paragraphs = [str(x).strip() for x in lesson["paragraphs"]]
        details["lessonText"] = paragraphs
        details["readableLesson"] = paragraphs
        details["formulas"] = [
            str(x).strip() for x in lesson["formulas"]
        ]
        details["keyPoints"] = [
            {
                "topic": str(point["topic"]).strip(),
                "explanation": str(point["explanation"]).strip(),
                "example": str(point["example"]).strip(),
                "commonTrap": str(point["common_trap"]).strip(),
            }
            for point in lesson["key_points"]
        ]
        applied += 1

    if applied == 0:
        raise SystemExit("沒有通過稽核的結果可寫回。")

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = CURRICULUM_PATH.with_name(
        CURRICULUM_PATH.name + f".before_ai_rewrite_{stamp}"
    )
    shutil.copy2(CURRICULUM_PATH, backup)
    write_curriculum_js(CURRICULUM_PATH, data)

    print(json.dumps({
        "applied": applied,
        "total": len(units),
        "backup": str(backup),
        "written": str(CURRICULUM_PATH),
        "require_all": require_all,
    }, ensure_ascii=False, indent=2))


def show_status() -> None:
    units = load_units()
    passed = 0
    failed = 0
    missing = 0
    for unit in units:
        path = result_path(unit["id"])
        if not path.exists():
            missing += 1
            continue
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            if not audit_lesson(unit, record["lesson"]):
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1

    print(json.dumps({
        "total": len(units),
        "passed": passed,
        "failed": failed,
        "remaining": missing,
        "progress_percent": round(
            (passed / len(units) * 100) if units else 0,
            2,
        ),
        "work_directory": str(WORK_DIR),
    }, ensure_ascii=False, indent=2))


def reset_results(confirm: str) -> None:
    if confirm != "DELETE":
        raise SystemExit(
            "這會刪除全部重寫結果。請加上：--confirm DELETE"
        )
    if WORK_DIR.exists():
        shutil.rmtree(WORK_DIR)
    print(f"已刪除：{WORK_DIR}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="KnowPareX 全課程自動重寫器"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("scan")
    sub.add_parser("status")
    sub.add_parser("audit")

    rewrite = sub.add_parser("rewrite")
    rewrite.add_argument("--model", default=DEFAULT_MODEL)
    rewrite.add_argument("--workers", type=int, default=2)
    rewrite.add_argument("--limit", type=int)
    rewrite.add_argument("--start", type=int, default=0)
    rewrite.add_argument("--retries", type=int, default=3)
    rewrite.add_argument("--only-failed", action="store_true")
    rewrite.add_argument("--force", action="store_true")
    rewrite.add_argument(
        "--subject",
        help="只處理指定學科鍵，例如 physics、chemistry、biology。",
    )
    rewrite.add_argument(
        "--stage",
        choices=("elementary", "junior_high", "high_school"),
        help="只處理指定年級階段。",
    )
    rewrite.add_argument(
        "--web-search",
        action="store_true",
        help="允許模型使用網路搜尋核對內容；成本與時間會增加。",
    )

    apply = sub.add_parser("apply")
    apply.add_argument("--require-all", action="store_true")

    reset = sub.add_parser("reset")
    reset.add_argument("--confirm", default="")

    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "scan":
        scan_units()
    elif args.command == "rewrite":
        rewrite_all(args)
    elif args.command == "status":
        show_status()
    elif args.command == "audit":
        report = audit_all()
        return 0 if report["failed"] == 0 and report["missing"] == 0 else 2
    elif args.command == "apply":
        apply_results(args.require_all)
    elif args.command == "reset":
        reset_results(args.confirm)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
