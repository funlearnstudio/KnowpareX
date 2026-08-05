#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindLeapX curriculum JS -> KnowpareX importer
Python 3.9+

特色：
1. 不執行 JavaScript，安全擷取 `const fullData = {...}`。
2. 支援「科目 -> 冊別 -> 單元」三層篩選。
3. 可查看統計、列出課程、顯示教材、匯出 JSONL。
4. 提供 register_subparser()，可掛進現有 argparse CLI。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, TextIO


SUBJECT_NAMES = {
    "chinese": "國文",
    "math": "數學",
    "english": "英文",
    "science": "自然",
    
    "biology": "生物",
    "physics": "物理",
    "chemistry": "化學",
    "earth": "地科",
    "social": "社會",
    "history": "歷史",
    "geography": "地理",
    "civics": "公民",
}

STAGE_NAMES = {
    "elementary": "國小",
    "junior_high": "國中",
    "high_school": "高中",
}


class CurriculumFormatError(ValueError):
    """課程檔案格式不符合預期。"""


def _extract_balanced_json_object(text: str, start: int) -> str:
    """從 start 起找第一個 JSON 物件，並以括號平衡方式擷取。"""
    object_start = text.find("{", start)
    if object_start < 0:
        raise CurriculumFormatError("找不到 fullData 的起始大括號。")

    depth = 0
    in_string = False
    escaped = False

    for index in range(object_start, len(text)):
        char = text[index]

        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[object_start:index + 1]

    raise CurriculumFormatError("fullData 物件沒有正常結束。")


def load_curriculum_js(path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """
    讀取 MindLeapX 課程 JS。

    預期格式：
        const fullData = { ... };
        global.CurriculumLibrary.data = fullData;
    """
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise CurriculumFormatError("檔案不是 UTF-8。") from exc

    marker = "const fullData"
    marker_index = text.find(marker)
    if marker_index < 0:
        raise CurriculumFormatError("找不到 `const fullData`。")

    equals_index = text.find("=", marker_index + len(marker))
    if equals_index < 0:
        raise CurriculumFormatError("找不到 `const fullData =`。")

    raw_json = _extract_balanced_json_object(text, equals_index + 1)

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise CurriculumFormatError(
            "fullData 看起來不是標準 JSON；錯誤位置：第 %d 行第 %d 欄。"
            % (exc.lineno, exc.colno)
        ) from exc

    if not isinstance(data, dict):
        raise CurriculumFormatError("fullData 最外層必須是物件。")

    return data


def _contains(text: Optional[str], query: Optional[str]) -> bool:
    if not query:
        return True
    return query.casefold() in (text or "").casefold()


def iter_units(
    data: Dict[str, List[Dict[str, Any]]],
    subject: Optional[str] = None,
    stage: Optional[str] = None,
    book: Optional[str] = None,
    unit: Optional[str] = None,
) -> Iterator[Dict[str, Any]]:
    """依科目、學制、冊別、單元篩選，逐一回傳標準化單元。"""
    for subject_key, books in data.items():
        subject_label = SUBJECT_NAMES.get(subject_key, subject_key)

        if subject and not (
            _contains(subject_key, subject) or _contains(subject_label, subject)
        ):
            continue

        if not isinstance(books, list):
            continue

        for book_obj in books:
            stage_key = str(book_obj.get("stage", ""))
            stage_label = STAGE_NAMES.get(stage_key, stage_key)
            book_name = str(book_obj.get("book") or book_obj.get("name") or "")

            if stage and not (
                _contains(stage_key, stage) or _contains(stage_label, stage)
            ):
                continue
            if book and not _contains(book_name, book):
                continue

            for unit_obj in book_obj.get("units", []):
                unit_name = str(unit_obj.get("name", ""))
                if unit and not _contains(unit_name, unit):
                    continue

                yield {
                    "subject_key": subject_key,
                    "subject": subject_label,
                    "stage_key": stage_key,
                    "stage": stage_label,
                    "book_id": book_obj.get("id"),
                    "book": book_name,
                    "book_name": book_obj.get("name"),
                    "publisher": book_obj.get("publisher"),
                    "coverage_note": book_obj.get("coverageNote"),
                    "unit": unit_name,
                    "tags": unit_obj.get("tags", []),
                    "topics": unit_obj.get("topics", []),
                    "lesson_details": unit_obj.get("lessonDetails", {}),
                }


def curriculum_stats(data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    subjects: Dict[str, Dict[str, int]] = {}
    stage_books: Dict[str, int] = {}
    total_books = 0
    total_units = 0
    total_key_points = 0

    for subject_key, books in data.items():
        book_count = len(books) if isinstance(books, list) else 0
        unit_count = 0
        key_point_count = 0

        for book in books if isinstance(books, list) else []:
            stage = str(book.get("stage", "unknown"))
            stage_books[stage] = stage_books.get(stage, 0) + 1
            units = book.get("units", [])
            unit_count += len(units)
            for unit in units:
                details = unit.get("lessonDetails", {})
                key_point_count += len(details.get("keyPoints", []))

        subjects[subject_key] = {
            "books": book_count,
            "units": unit_count,
            "key_points": key_point_count,
        }
        total_books += book_count
        total_units += unit_count
        total_key_points += key_point_count

    return {
        "subject_count": len(subjects),
        "book_count": total_books,
        "unit_count": total_units,
        "key_point_count": total_key_points,
        "stage_books": stage_books,
        "subjects": subjects,
    }


def _append_record(
    records: List[Dict[str, Any]],
    item: Any,
    relation: str,
    value: Any,
    kind: str,
) -> None:
    """忽略空值，並加入一筆 KnowpareX 中介紀錄。"""
    if item is None or value is None:
        return

    item_text = str(item).strip()
    value_text = str(value).strip()
    if not item_text or not value_text:
        return

    records.append({
        "item": item_text,
        "relation": relation,
        "value": value_text,
        "kind": kind,
    })


def unit_to_knowparex(unit: Dict[str, Any]) -> Dict[str, Any]:
    """
    將一個課程單元轉成 KnowpareX 可再匯入的中介格式。

    輸出保留：
    category -> topic -> records
    """
    details = unit.get("lesson_details", {}) or {}
    category = "%s / %s" % (unit["stage"], unit["subject"])
    topic = "%s / %s" % (unit["book"], unit["unit"])
    records: List[Dict[str, Any]] = []

    _append_record(records, unit["unit"], "屬於冊別", unit["book"], "hierarchy")
    _append_record(records, unit["book"], "屬於科目", unit["subject"], "hierarchy")
    _append_record(records, unit["subject"], "屬於學制", unit["stage"], "hierarchy")

    for value in unit.get("topics", []):
        _append_record(records, value, "是本單元的主題", unit["unit"], "topic")

    for value in details.get("bigIdeas", []):
        _append_record(records, unit["unit"], "核心概念", value, "big_idea")

    for value in details.get("smallFocus", []):
        _append_record(records, unit["unit"], "學習重點", value, "small_focus")

    for value in details.get("formulas", []):
        _append_record(records, unit["unit"], "公式或規則", value, "formula")

    for value in details.get("learningObjectives", []):
        _append_record(records, unit["unit"], "學習目標", value, "objective")

    for value in details.get("mustKnow", []):
        _append_record(records, value, "是本單元必會內容", unit["unit"], "must_know")

    for point in details.get("keyPoints", []):
        point_topic = point.get("topic") or unit["unit"]
        _append_record(
            records, point_topic, "定義為", point.get("explanation"), "explanation"
        )
        _append_record(
            records, point_topic, "是……的例子", point.get("example"), "example"
        )
        _append_record(
            records, point_topic, "常見錯誤", point.get("commonTrap"), "common_trap"
        )

    for value in details.get("examFocus", []):
        _append_record(records, unit["unit"], "考試重點", value, "exam_focus")

    for value in details.get("commonMistakes", []):
        _append_record(records, unit["unit"], "常見錯誤", value, "common_mistake")

    for value in details.get("practiceDesign", []):
        _append_record(records, unit["unit"], "練習方式", value, "practice")

    for value in details.get("outputSkills", []):
        _append_record(records, unit["unit"], "學完後能做到", value, "output_skill")

    for paragraph in (
        details.get("readableLesson")
        or details.get("lessonText")
        or []
    ):
        _append_record(records, unit["unit"], "教材內容", paragraph, "lesson_text")

    # 在單元內去重，保留原順序。
    seen = set()
    unique_records = []
    for record in records:
        key = (
            record["item"],
            record["relation"],
            record["value"],
            record["kind"],
        )
        if key in seen:
            continue
        seen.add(key)
        unique_records.append(record)

    return {
        "category": category,
        "topic": topic,
        "metadata": {
            "subject_key": unit["subject_key"],
            "subject": unit["subject"],
            "stage_key": unit["stage_key"],
            "stage": unit["stage"],
            "book_id": unit["book_id"],
            "book": unit["book"],
            "unit": unit["unit"],
            "publisher": unit["publisher"],
            "tags": unit.get("tags", []),
            "topics": unit.get("topics", []),
            "source_boundary": details.get("sourceBoundary"),
            "copyright_policy": details.get("copyrightPolicy"),
            "anti_overreach_rule": details.get("antiOverreachRule"),
        },
        "records": unique_records,
    }


def export_jsonl(
    units: Iterable[Dict[str, Any]],
    output: TextIO,
) -> int:
    count = 0
    for unit in units:
        output.write(
            json.dumps(unit_to_knowparex(unit), ensure_ascii=False) + "\n"
        )
        count += 1
    return count


def print_lesson(unit: Dict[str, Any]) -> None:
    details = unit.get("lesson_details", {}) or {}

    print("=" * 60)
    print("%s / %s / %s" % (unit["subject"], unit["book"], unit["unit"]))
    print("=" * 60)

    lesson = details.get("readableLesson") or details.get("lessonText") or []
    for paragraph in lesson:
        print(paragraph)
        print()

    key_points = details.get("keyPoints", [])
    if key_points:
        print("【重點】")
        for index, point in enumerate(key_points, 1):
            print("%d. %s" % (index, point.get("topic", "未命名重點")))
            if point.get("explanation"):
                print("   解釋：%s" % point["explanation"])
            if point.get("example"):
                print("   例子：%s" % point["example"])
            if point.get("commonTrap"):
                print("   易錯：%s" % point["commonTrap"])

    if details.get("examFocus"):
        print("\n【考試重點】")
        for value in details["examFocus"]:
            print("- %s" % value)


def _build_curriculum_parser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(
        "curriculum",
        help="讀取 MindLeapX 課程資料",
    )
    parser.add_argument(
        "--file",
        required=True,
        type=Path,
        help="curriculum_integrated.js 的路徑",
    )

    actions = parser.add_subparsers(dest="curriculum_action", required=True)

    actions.add_parser("inspect", help="查看課程資料統計")

    list_parser = actions.add_parser("list", help="列出冊別與單元")
    _add_filters(list_parser)
    list_parser.add_argument("--limit", type=int, default=50)

    lesson_parser = actions.add_parser("lesson", help="顯示一個單元教材")
    _add_filters(lesson_parser)
    lesson_parser.add_argument("--index", type=int, default=1)

    export_parser = actions.add_parser("export", help="匯出 KnowpareX JSONL")
    _add_filters(export_parser)
    export_parser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
        help="輸出的 .jsonl 路徑",
    )

    parser.set_defaults(func=curriculum_main)
    return parser


def _add_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--subject", help="科目，例如 math、數學")
    parser.add_argument("--stage", help="學制，例如 high_school、高中")
    parser.add_argument("--book", help="冊別關鍵字，例如 高一上")
    parser.add_argument("--unit", help="單元關鍵字，例如 實數")


def register_subparser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    """
    掛進 KnowpareX 既有 argparse：

        from curriculum_importer import register_subparser
        register_subparser(subparsers)
    """
    return _build_curriculum_parser(subparsers)


def curriculum_main(args: argparse.Namespace) -> int:
    try:
        data = load_curriculum_js(args.file)
    except (OSError, CurriculumFormatError) as exc:
        print("課程資料讀取失敗：%s" % exc)
        return 2

    action = args.curriculum_action

    if action == "inspect":
        stats = curriculum_stats(data)
        print("=" * 60)
        print("MindLeapX 課程資料統計")
        print("=" * 60)
        print("科目數：%d" % stats["subject_count"])
        print("冊別數：%d" % stats["book_count"])
        print("單元數：%d" % stats["unit_count"])
        print("重點紀錄數：%d" % stats["key_point_count"])
        print("\n【各科】")
        for key, value in stats["subjects"].items():
            print(
                "- %s：%d 冊、%d 單元、%d 個 keyPoints"
                % (
                    SUBJECT_NAMES.get(key, key),
                    value["books"],
                    value["units"],
                    value["key_points"],
                )
            )
        return 0

    units = list(
        iter_units(
            data,
            subject=getattr(args, "subject", None),
            stage=getattr(args, "stage", None),
            book=getattr(args, "book", None),
            unit=getattr(args, "unit", None),
        )
    )

    if action == "list":
        if not units:
            print("找不到符合條件的單元。")
            return 1
        for index, item in enumerate(units[: args.limit], 1):
            print(
                "%d. %s / %s / %s"
                % (index, item["subject"], item["book"], item["unit"])
            )
        if len(units) > args.limit:
            print("……另有 %d 個結果" % (len(units) - args.limit))
        return 0

    if action == "lesson":
        if not units:
            print("找不到符合條件的單元。")
            return 1
        if args.index < 1 or args.index > len(units):
            print("--index 超出範圍；目前共有 %d 個結果。" % len(units))
            return 1
        print_lesson(units[args.index - 1])
        return 0

    if action == "export":
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as output:
            count = export_jsonl(units, output)
        print("已匯出 %d 個單元到 %s" % (count, args.output))
        return 0

    print("未知動作：%s" % action)
    return 2


def build_standalone_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="curriculum-importer",
        description="MindLeapX 課程資料匯入工具",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    _build_curriculum_parser(subparsers)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_standalone_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
