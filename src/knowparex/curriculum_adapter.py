#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindLeapX curriculum adapter for KnowpareX
Python 3.9+

把 curriculum_integrated.js 虛擬成 KnowpareX 原生資料來源。
不用先匯出，也不用把 816 個單元改寫成 Python 函式。

只要 knowledge_service.py 合併這個 adapter，原本的：
- categories
- items
- topic
- search
- search --tree
- search --open
- scan
- stats
- today
- related（如果它透過 get_* API）
都會自動看到課程資料。
"""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple


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
    pass


def _extract_balanced_json_object(text: str, start: int) -> str:
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
    text = path.read_text(encoding="utf-8")
    marker_index = text.find("const fullData")
    if marker_index < 0:
        raise CurriculumFormatError("找不到 `const fullData`。")

    equals_index = text.find("=", marker_index)
    if equals_index < 0:
        raise CurriculumFormatError("找不到 `const fullData =`。")

    raw_json = _extract_balanced_json_object(text, equals_index + 1)

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise CurriculumFormatError(
            "fullData 不是標準 JSON：第 %d 行第 %d 欄"
            % (exc.lineno, exc.colno)
        ) from exc

    if not isinstance(data, dict):
        raise CurriculumFormatError("fullData 最外層必須是物件。")

    return data


def default_curriculum_path() -> Path:
    """
    尋找套件內的 data/curriculum_integrated.js。

    開發模式與 pip 安裝後都能使用。
    """
    try:
        resource = (
            resources.files("knowparex")
            .joinpath("data")
            .joinpath("curriculum_integrated.js")
        )
        return Path(str(resource))
    except (AttributeError, ModuleNotFoundError):
        # Python 3.9 / 一般原始碼執行備援
        return Path(__file__).resolve().parent / "data" / "curriculum_integrated.js"


@lru_cache(maxsize=1)
def get_curriculum_data() -> Dict[str, List[Dict[str, Any]]]:
    path = default_curriculum_path()
    if not path.exists():
        raise FileNotFoundError(
            "找不到課程資料：%s。請把 curriculum_integrated.js "
            "放到 src/knowparex/data/。" % path
        )
    return load_curriculum_js(path)


def clear_curriculum_cache() -> None:
    get_curriculum_data.cache_clear()


def _iter_units() -> Iterator[Dict[str, Any]]:
    data = get_curriculum_data()

    for subject_key, books in data.items():
        subject_name = SUBJECT_NAMES.get(subject_key, subject_key)
        if not isinstance(books, list):
            continue

        for book in books:
            stage_key = str(book.get("stage", ""))
            stage_name = STAGE_NAMES.get(stage_key, stage_key)
            book_name = str(book.get("book") or book.get("name") or "")

            for unit in book.get("units", []):
                yield {
                    "subject_key": subject_key,
                    "subject": subject_name,
                    "stage_key": stage_key,
                    "stage": stage_name,
                    "book": book_name,
                    "book_id": book.get("id"),
                    "publisher": book.get("publisher"),
                    "coverage_note": book.get("coverageNote"),
                    "unit": str(unit.get("name", "")),
                    "tags": unit.get("tags", []),
                    "topics": unit.get("topics", []),
                    "lesson_details": unit.get("lessonDetails", {}) or {},
                }


def category_name(unit: Dict[str, Any]) -> str:
    # 用「課程」前綴避免撞到原本的「數學、國文」分類。
    return "課程 / %s / %s" % (unit["stage"], unit["subject"])


def item_name(unit: Dict[str, Any]) -> str:
    return "%s / %s" % (unit["book"], unit["unit"])


@lru_cache(maxsize=1)
def _index() -> Tuple[
    Dict[str, List[str]],
    Dict[Tuple[str, str], Dict[str, Any]],
]:
    category_items: Dict[str, List[str]] = {}
    topics: Dict[Tuple[str, str], Dict[str, Any]] = {}

    for unit in _iter_units():
        category = category_name(unit)
        item = item_name(unit)

        category_items.setdefault(category, [])
        if item not in category_items[category]:
            category_items[category].append(item)

        topics[(category, item)] = unit

    for items in category_items.values():
        items.sort()

    return category_items, topics


def get_curriculum_categories() -> List[str]:
    category_items, _ = _index()
    return sorted(category_items)


def get_curriculum_items(category: str) -> List[str]:
    category_items, _ = _index()
    if category not in category_items:
        raise KeyError("Unknown curriculum category: %s" % category)
    return list(category_items[category])


def curriculum_topic_exists(category: str, item: str) -> bool:
    _, topics = _index()
    return (category, item) in topics


def _record(
    relation: str,
    code_a: Any,
    language_a: str,
    code_b: Any,
    language_b: str,
) -> Optional[Dict[str, str]]:
    if code_a is None or code_b is None:
        return None

    left = str(code_a).strip()
    right = str(code_b).strip()
    if not left or not right:
        return None

    return {
        "relation": relation,
        "code_a": left,
        "language_a": language_a,
        "code_b": right,
        "language_b": language_b,
    }


def get_curriculum_topic_data(category: str, item: str) -> List[Dict[str, str]]:
    _, topics = _index()

    try:
        unit = topics[(category, item)]
    except KeyError as exc:
        raise KeyError(
            "Unknown curriculum topic: %s / %s" % (category, item)
        ) from exc

    details = unit["lesson_details"]
    records: List[Dict[str, str]] = []

    def add(
        relation: str,
        code_a: Any,
        language_a: str,
        code_b: Any,
        language_b: str,
    ) -> None:
        value = _record(relation, code_a, language_a, code_b, language_b)
        if value is not None:
            records.append(value)

    # 三層課程架構
    add("屬於冊別", unit["unit"], "單元", unit["book"], "冊別")
    add("屬於科目", unit["book"], "冊別", unit["subject"], "科目")
    add("屬於學制", unit["subject"], "科目", unit["stage"], "學制")

    for value in unit.get("topics", []):
        add("是……的一部分", value, "單元主題", unit["unit"], "單元")

    for value in details.get("bigIdeas", []):
        add("核心概念", unit["unit"], "單元", value, "大概念")

    for value in details.get("smallFocus", []):
        add("學習重點", unit["unit"], "單元", value, "小重點")

    for value in details.get("formulas", []):
        add("計算方式", unit["unit"], "單元", value, "公式或規則")

    for value in details.get("learningObjectives", []):
        add("學習目標", unit["unit"], "單元", value, "目標")

    for value in details.get("mustKnow", []):
        add("需要", unit["unit"], "單元", value, "必會內容")

    for point in details.get("keyPoints", []):
        topic = point.get("topic") or unit["unit"]
        add("定義為", topic, "知識重點", point.get("explanation"), "解釋")
        add("是……的例子", point.get("example"), "例子", topic, "知識重點")
        add("常見錯誤", topic, "知識重點", point.get("commonTrap"), "易錯點")

    for value in details.get("examFocus", []):
        add("考試重點", unit["unit"], "單元", value, "考法")

    for value in details.get("commonMistakes", []):
        add("常見錯誤", unit["unit"], "單元", value, "易錯點")

    for value in details.get("practiceDesign", []):
        add("練習方式", unit["unit"], "單元", value, "練習")

    for value in details.get("outputSkills", []):
        add("學完後能做到", unit["unit"], "單元", value, "能力")

    lesson = details.get("readableLesson") or details.get("lessonText") or []
    for paragraph in lesson:
        add("教材內容", unit["unit"], "單元", paragraph, "課文")

    # 保留授權／範圍資訊，但不讓空值進來。
    add(
        "內容來源限制",
        unit["unit"],
        "單元",
        details.get("sourceBoundary"),
        "來源說明",
    )
    add(
        "授權說明",
        unit["unit"],
        "單元",
        details.get("copyrightPolicy"),
        "授權",
    )
    add(
        "出題範圍限制",
        unit["unit"],
        "單元",
        details.get("antiOverreachRule"),
        "限制",
    )

    # 去重
    unique: List[Dict[str, str]] = []
    seen = set()
    for value in records:
        key = (
            value["relation"],
            value["code_a"],
            value["language_a"],
            value["code_b"],
            value["language_b"],
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(value)

    return unique


def curriculum_stats() -> Dict[str, int]:
    categories = get_curriculum_categories()
    topic_count = sum(len(get_curriculum_items(c)) for c in categories)
    record_count = sum(
        len(get_curriculum_topic_data(c, i))
        for c in categories
        for i in get_curriculum_items(c)
    )
    return {
        "categories": len(categories),
        "topics": topic_count,
        "records": record_count,
    }


def _matches_subject(unit: Dict[str, Any], subject: str) -> bool:
    query = subject.casefold()
    return (
        query in unit["subject_key"].casefold()
        or query in unit["subject"].casefold()
    )


def _matches_stage(unit: Dict[str, Any], stage: Optional[str]) -> bool:
    if not stage:
        return True
    query = stage.casefold()
    return (
        query in unit["stage_key"].casefold()
        or query in unit["stage"].casefold()
    )


def get_subjects() -> List[Dict[str, str]]:
    values = []
    seen = set()
    for unit in _iter_units():
        key = unit["subject_key"]
        if key in seen:
            continue
        seen.add(key)
        values.append({"key": key, "name": unit["subject"]})
    return sorted(values, key=lambda value: value["key"])


def get_books(
    subject: str,
    *,
    stage: Optional[str] = None,
) -> List[Dict[str, str]]:
    values = []
    seen = set()

    for unit in _iter_units():
        if not _matches_subject(unit, subject):
            continue
        if not _matches_stage(unit, stage):
            continue

        key = (unit["stage"], unit["subject"], unit["book"])
        if key in seen:
            continue
        seen.add(key)
        values.append({
            "stage": unit["stage"],
            "subject": unit["subject"],
            "book": unit["book"],
        })

    return sorted(
        values,
        key=lambda value: (
            value["stage"],
            value["subject"],
            value["book"],
        ),
    )


def get_units(
    subject: str,
    book: str,
    *,
    stage: Optional[str] = None,
) -> List[Dict[str, str]]:
    values = []

    for unit in _iter_units():
        if not _matches_subject(unit, subject):
            continue
        if not _matches_stage(unit, stage):
            continue
        if book.casefold() not in unit["book"].casefold():
            continue

        values.append({
            "stage": unit["stage"],
            "subject": unit["subject"],
            "book": unit["book"],
            "unit": unit["unit"],
        })

    return sorted(values, key=lambda value: value["unit"])


def find_curriculum_topic(
    subject: str,
    book: str,
    unit: str,
    *,
    stage: Optional[str] = None,
) -> Tuple[str, str]:
    matches = []

    for value in _iter_units():
        if not _matches_subject(value, subject):
            continue
        if not _matches_stage(value, stage):
            continue
        if book.casefold() not in value["book"].casefold():
            continue
        if unit.casefold() not in value["unit"].casefold():
            continue

        matches.append((category_name(value), item_name(value)))

    if not matches:
        raise KeyError(
            "找不到課程：%s / %s / %s" % (subject, book, unit)
        )

    if len(matches) > 1:
        preview = "、".join(
            "%s / %s" % match
            for match in matches[:5]
        )
        raise KeyError(
            "找到多個課程，請加上 --stage 或輸入更完整名稱：%s"
            % preview
        )

    return matches[0]
