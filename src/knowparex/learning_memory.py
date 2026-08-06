from __future__ import annotations

import json
import re
import uuid
from dataclasses import asdict, dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Iterable

from .storage import get_learning_records_path


REVIEW_INTERVALS = (1, 3, 7, 14, 30, 60, 120)
IMPORT_SUFFIXES = {".md", ".txt", ".py"}


@dataclass
class LearningRecord:
    """One project or topic that a learner wants to remember."""

    id: str
    title: str
    summary: str = ""
    subject: str = "Uncategorized"
    source_path: str | None = None
    content: str = ""
    tags: list[str] = field(default_factory=list)
    created_on: str = field(default_factory=lambda: date.today().isoformat())
    last_reviewed_on: str | None = None
    next_review_on: str = field(default_factory=lambda: date.today().isoformat())
    review_step: int = 0
    review_count: int = 0

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "LearningRecord":
        allowed = cls.__dataclass_fields__.keys()
        return cls(**{key: value[key] for key in allowed if key in value})


def load_learning_records(path: Path | None = None) -> list[LearningRecord]:
    """Load records. Invalid or missing files behave like an empty store."""
    target = path or get_learning_records_path()
    if not target.exists():
        return []
    try:
        raw = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(raw, list):
        return []
    records: list[LearningRecord] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        try:
            records.append(LearningRecord.from_dict(item))
        except (TypeError, ValueError):
            continue
    return records


def save_learning_records(
    records: Iterable[LearningRecord],
    path: Path | None = None,
) -> Path:
    """Atomically save learning-memory records and return the file path."""
    target = path or get_learning_records_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(
        json.dumps([asdict(record) for record in records], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary.replace(target)
    return target


def add_learning_record(
    title: str,
    *,
    summary: str = "",
    subject: str = "Uncategorized",
    content: str = "",
    source_path: str | None = None,
    tags: Iterable[str] = (),
    store_path: Path | None = None,
) -> LearningRecord:
    """Create and persist one learning record."""
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("title cannot be empty")
    records = load_learning_records(store_path)
    record = LearningRecord(
        id=uuid.uuid4().hex[:12],
        title=clean_title,
        summary=summary.strip(),
        subject=subject.strip() or "Uncategorized",
        content=content.strip(),
        source_path=source_path,
        tags=sorted({tag.strip() for tag in tags if tag.strip()}),
    )
    records.append(record)
    save_learning_records(records, store_path)
    return record


def find_learning_record(query: str, *, store_path: Path | None = None) -> LearningRecord:
    """Find one record by exact ID, ID prefix, or unique title match."""
    needle = query.strip().casefold()
    records = load_learning_records(store_path)
    matches = [
        record
        for record in records
        if record.id.casefold().startswith(needle) or record.title.casefold() == needle
    ]
    if not matches:
        raise KeyError(f"learning record not found: {query}")
    if len(matches) > 1:
        raise ValueError(f"learning record is ambiguous: {query}")
    return matches[0]


def review_learning_record(
    query: str,
    rating: int,
    *,
    reviewed_on: date | None = None,
    store_path: Path | None = None,
) -> LearningRecord:
    """Record a review. Rating 0 resets; 1 holds; 2 advances; 3 skips a step."""
    if rating not in {0, 1, 2, 3}:
        raise ValueError("rating must be 0, 1, 2, or 3")
    records = load_learning_records(store_path)
    record = find_learning_record(query, store_path=store_path)
    if rating == 0:
        record.review_step = 0
    elif rating == 2:
        record.review_step = min(record.review_step + 1, len(REVIEW_INTERVALS) - 1)
    elif rating == 3:
        record.review_step = min(record.review_step + 2, len(REVIEW_INTERVALS) - 1)
    day = reviewed_on or date.today()
    record.last_reviewed_on = day.isoformat()
    record.review_count += 1
    interval = REVIEW_INTERVALS[record.review_step]
    record.next_review_on = (day + timedelta(days=interval)).isoformat()
    for index, existing in enumerate(records):
        if existing.id == record.id:
            records[index] = record
            break
    save_learning_records(records, store_path)
    return record


def due_learning_records(
    *,
    on_date: date | None = None,
    store_path: Path | None = None,
) -> list[LearningRecord]:
    """Return records due on or before the selected day."""
    day = (on_date or date.today()).isoformat()
    return sorted(
        (record for record in load_learning_records(store_path) if record.next_review_on <= day),
        key=lambda record: (record.next_review_on, record.subject.casefold(), record.title.casefold()),
    )


def _title_from_file(path: Path) -> str:
    if path.suffix.casefold() == ".md":
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            match = re.match(r"^#\s+(.+?)\s*$", line)
            if match:
                return match.group(1)
    return path.stem.replace("_", " ").replace("-", " ").strip()


def import_learning_file(
    path: str | Path,
    *,
    subject: str = "Imported",
    tags: Iterable[str] = (),
    store_path: Path | None = None,
) -> LearningRecord:
    """Import one Markdown, text, or Python file as a learning record."""
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    if source.suffix.casefold() not in IMPORT_SUFFIXES:
        raise ValueError(f"unsupported file type: {source.suffix or '(none)'}")
    content = source.read_text(encoding="utf-8", errors="replace")
    summary = next((line.strip("# ") for line in content.splitlines() if line.strip()), "")
    return add_learning_record(
        _title_from_file(source),
        summary=summary[:300],
        subject=subject,
        content=content,
        source_path=str(source),
        tags=tags,
        store_path=store_path,
    )


def import_learning_directory(
    path: str | Path,
    *,
    subject: str = "Imported",
    tags: Iterable[str] = (),
    recursive: bool = False,
    store_path: Path | None = None,
) -> list[LearningRecord]:
    """Import supported files from a directory, skipping known source paths."""
    directory = Path(path).expanduser().resolve()
    if not directory.is_dir():
        raise NotADirectoryError(directory)
    existing_sources = {
        record.source_path for record in load_learning_records(store_path) if record.source_path
    }
    pattern = "**/*" if recursive else "*"
    imported: list[LearningRecord] = []
    for source in sorted(directory.glob(pattern)):
        if not source.is_file() or source.suffix.casefold() not in IMPORT_SUFFIXES:
            continue
        if str(source.resolve()) in existing_sources:
            continue
        imported.append(
            import_learning_file(
                source,
                subject=subject,
                tags=tags,
                store_path=store_path,
            )
        )
    return imported


def _safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff._-]+", "-", value.strip()).strip("-.")
    return cleaned or "learning-record"


def export_learning_record(
    query: str,
    output_directory: str | Path,
    *,
    store_path: Path | None = None,
) -> Path:
    """Export one record as a readable Markdown learning page."""
    record = find_learning_record(query, store_path=store_path)
    directory = Path(output_directory).expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"{_safe_filename(record.title)}.md"
    tags = ", ".join(record.tags) if record.tags else "None"
    body = record.content or record.summary or "No learning notes have been added yet."
    target.write_text(
        f"# {record.title}\n\n"
        f"> Subject: {record.subject}  \n"
        f"> Tags: {tags}  \n"
        f"> Last reviewed: {record.last_reviewed_on or 'Not yet'}\n\n"
        f"## Summary\n\n{record.summary or 'No summary yet.'}\n\n"
        f"## Learning Notes\n\n{body}\n",
        encoding="utf-8",
    )
    return target
