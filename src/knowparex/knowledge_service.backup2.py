#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Drop-in replacement for knowparex/knowledge_service.py

把原本 Python 函式資料庫與 MindLeapX 課程資料合併成同一組 API。
因為 CLI 的 search、scan、tree、stats 都是呼叫這三個函式，
所以不必各自重寫。
"""

from __future__ import annotations

from typing import Dict, List

from .system_library import library
from .PROGRAMMING_NOTES import compare_system
from .curriculum_adapter import (
    curriculum_topic_exists,
    get_curriculum_categories,
    get_curriculum_items,
    get_curriculum_topic_data,
)


def get_categories() -> List[str]:
    static_categories = list(library.keys())
    curriculum_categories = get_curriculum_categories()

    # 保留靜態資料原順序，課程資料放後面。
    return static_categories + [
        category
        for category in curriculum_categories
        if category not in library
    ]


def get_items(category: str) -> List[str]:
    if category in library:
        return list(library[category].keys())

    return get_curriculum_items(category)


def topic_exists(category: str, item: str) -> bool:
    if category in library:
        return item in library[category]

    return curriculum_topic_exists(category, item)


def get_topic_data(category: str, item: str) -> List[Dict[str, object]]:
    if category in library:
        if item not in library[category]:
            raise KeyError("Unknown item: %s" % item)

        compare_system.clear_data()
        compare_system.set_show(False)

        try:
            library[category][item]()
            return compare_system.get_data()
        finally:
            compare_system.set_show(True)

    return get_curriculum_topic_data(category, item)
