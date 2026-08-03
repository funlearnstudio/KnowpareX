from __future__ import annotations

from typing import Any

from .system_library import library
from .PROGRAMMING_NOTES import compare_system


def get_categories() -> list[str]:
    """Return all category names."""
    return list(library.keys())


def get_items(category: str) -> list[str]:
    """Return all item names in one category."""
    if category not in library:
        raise KeyError(f"找不到分類：{category}")
    return list(library[category].keys())


def get_topic_data(category: str, item: str) -> list[dict[str, Any]]:
    """Run one topic function and return its collected relationship records."""
    if category not in library:
        raise KeyError(f"找不到分類：{category}")
    if item not in library[category]:
        raise KeyError(f"在「{category}」中找不到項目：{item}")

    compare_system.clear_data()
    compare_system.set_show(False)
    try:
        library[category][item]()
        return compare_system.get_data()
    finally:
        compare_system.set_show(True)


def topic_exists(category: str, item: str) -> bool:
    """Return True when the category and item are registered."""
    return category in library and item in library[category]
