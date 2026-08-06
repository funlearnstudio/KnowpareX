"""KnowpareX knowledge relationship and learning database."""

from .system_library import library
from .knowledge_service import (
    get_categories,
    get_items,
    get_topic_data,
    topic_exists,
)
from .PROGRAMMING_NOTES import compare_system
from .learning_memory import (
    LearningRecord,
    add_learning_record,
    due_learning_records,
    export_learning_record,
    import_learning_directory,
    import_learning_file,
    load_learning_records,
    review_learning_record,
)

__all__ = [
    "library",
    "compare_system",
    "get_categories",
    "get_items",
    "get_topic_data",
    "topic_exists",
    "LearningRecord",
    "add_learning_record",
    "due_learning_records",
    "export_learning_record",
    "import_learning_directory",
    "import_learning_file",
    "load_learning_records",
    "review_learning_record",
]

__version__ = "1.7.0"
