#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KnowpareX data service with separated sources.

預設只讀原本的 KnowpareX 知識資料。
課程資料必須明確指定 source="curriculum"。
只有明確指定 source="all" 時才會合併。
"""

from __future__ import annotations

from typing import Dict, List, Literal

from .system_library import library
from .PROGRAMMING_NOTES import compare_system
from .curriculum_adapter import (
    curriculum_topic_exists,
    get_curriculum_categories,
    get_curriculum_items,
    get_curriculum_topic_data,
)

DataSource = Literal["knowledge", "curriculum", "all"]


def _validate_source(source: str) -> None:
    if source not in {"knowledge", "curriculum", "all"}:
        raise ValueError(
            "source 必須是 knowledge、curriculum 或 all。"
        )


def get_categories(source: DataSource = "knowledge") -> List[str]:
    _validate_source(source)

    if source == "knowledge":
        return list(library.keys())

    if source == "curriculum":
        return get_curriculum_categories()

    knowledge_categories = list(library.keys())
    return knowledge_categories + [
        category
        for category in get_curriculum_categories()
        if category not in library
    ]


def get_items(
    category: str,
    source: DataSource = "knowledge",
) -> List[str]:
    _validate_source(source)

    if source == "knowledge":
        if category not in library:
            raise KeyError("Unknown knowledge category: %s" % category)
        return list(library[category].keys())

    if source == "curriculum":
        return get_curriculum_items(category)

    if category in library:
        return list(library[category].keys())

    return get_curriculum_items(category)


def topic_exists(
    category: str,
    item: str,
    source: DataSource = "knowledge",
) -> bool:
    _validate_source(source)

    if source == "knowledge":
        return category in library and item in library[category]

    if source == "curriculum":
        return curriculum_topic_exists(category, item)

    if category in library and item in library[category]:
        return True

    return curriculum_topic_exists(category, item)


def get_topic_data(
    category: str,
    item: str,
    source: DataSource = "knowledge",
) -> List[Dict[str, object]]:
    _validate_source(source)

    if source in {"knowledge", "all"} and category in library:
        if item not in library[category]:
            raise KeyError("Unknown knowledge item: %s" % item)

        compare_system.clear_data()
        compare_system.set_show(False)

        try:
            library[category][item]()
            return compare_system.get_data()
        finally:
            compare_system.set_show(True)

    if source in {"curriculum", "all"}:
        return get_curriculum_topic_data(category, item)

    raise KeyError("Unknown topic: %s / %s" % (category, item))
