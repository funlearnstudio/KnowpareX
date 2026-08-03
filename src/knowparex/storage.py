from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


def get_data_directory() -> Path:
    """Return a writable per-user directory for KnowpareX data."""
    if sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    elif os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))

    directory = base / "KnowpareX"
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def get_wrong_questions_path() -> Path:
    """Return the persistent wrong-question JSON path."""
    return get_data_directory() / "wrong_questions.json"


def load_wrong_questions() -> list[dict[str, Any]]:
    """Load saved wrong questions, returning an empty list when unavailable."""
    path = get_wrong_questions_path()
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

    return data if isinstance(data, list) else []


def save_wrong_questions(questions: list[dict[str, Any]]) -> Path:
    """Save wrong questions and return the file path."""
    path = get_wrong_questions_path()
    path.write_text(
        json.dumps(questions, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )
    return path
