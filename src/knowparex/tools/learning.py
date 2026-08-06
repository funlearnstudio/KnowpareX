from __future__ import annotations

import argparse
from pathlib import Path

from ..learning_memory import (
    add_learning_record,
    due_learning_records,
    export_learning_record,
    import_learning_directory,
    import_learning_file,
    load_learning_records,
    review_learning_record,
)


def _tags(value: str | None) -> list[str]:
    return [] if not value else [tag.strip() for tag in value.split(",") if tag.strip()]


def _print_record(record) -> None:
    print(f"{record.id} | {record.title} | {record.subject} | next: {record.next_review_on}")


def configure_parser(parser: argparse.ArgumentParser) -> None:
    commands = parser.add_subparsers(dest="learning_command", required=True)
    add = commands.add_parser("add", help="Add a project or learning record")
    add.add_argument("title")
    add.add_argument("--summary", default="")
    add.add_argument("--subject", default="Uncategorized")
    add.add_argument("--tags", help="Comma-separated tags")

    commands.add_parser("list", help="List all learning records")
    commands.add_parser("due", help="List records due for review")

    review = commands.add_parser("review", help="Record a completed review")
    review.add_argument("record", help="Record ID, ID prefix, or exact title")
    review.add_argument("rating", type=int, choices=(0, 1, 2, 3))

    importer = commands.add_parser("import", help="Import a learning file or directory")
    importer.add_argument("path")
    importer.add_argument("--subject", default="Imported")
    importer.add_argument("--tags", help="Comma-separated tags")
    importer.add_argument("--recursive", action="store_true")

    exporter = commands.add_parser("export", help="Export one record as Markdown")
    exporter.add_argument("record", help="Record ID, ID prefix, or exact title")
    exporter.add_argument("--output", default="knowparex-learning-pages")


def run(args: argparse.Namespace) -> None:
    command = args.learning_command
    if command == "add":
        record = add_learning_record(
            args.title,
            summary=args.summary,
            subject=args.subject,
            tags=_tags(args.tags),
        )
        print("Added:")
        _print_record(record)
    elif command == "list":
        records = load_learning_records()
        if not records:
            print("No learning records yet.")
        for record in records:
            _print_record(record)
    elif command == "due":
        records = due_learning_records()
        if not records:
            print("Nothing is due for review.")
        for record in records:
            _print_record(record)
    elif command == "review":
        record = review_learning_record(args.record, args.rating)
        print("Review saved:")
        _print_record(record)
    elif command == "import":
        source = Path(args.path).expanduser()
        if source.is_dir():
            records = import_learning_directory(
                source,
                subject=args.subject,
                tags=_tags(args.tags),
                recursive=args.recursive,
            )
        else:
            records = [
                import_learning_file(source, subject=args.subject, tags=_tags(args.tags))
            ]
        print(f"Imported {len(records)} learning file(s).")
        for record in records:
            _print_record(record)
    elif command == "export":
        path = export_learning_record(args.record, args.output)
        print(f"Exported: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="knowparex-learning")
    configure_parser(parser)
    run(parser.parse_args())


if __name__ == "__main__":
    main()

