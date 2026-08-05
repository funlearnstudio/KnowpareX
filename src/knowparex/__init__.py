"""KnowpareX knowledge relationship and learning database."""

from .system_library import library
from .knowledge_service import (
    get_categories,
    get_items,
    get_topic_data,
    topic_exists,
)
from .PROGRAMMING_NOTES import compare_system

__all__ = [
    "library",
    "compare_system",
    "get_categories",
    "get_items",
    "get_topic_data",
    "topic_exists",
]

__version__ = "1.7.0"
