from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from knowparex.learning_memory import (
    add_learning_record,
    due_learning_records,
    export_learning_record,
    import_learning_directory,
    load_learning_records,
    review_learning_record,
)


class LearningMemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = self.root / "records.json"

    def tearDown(self):
        self.temp.cleanup()

    def test_add_review_and_due_flow(self):
        record = add_learning_record(
            "Binary search",
            summary="Search sorted data by repeatedly halving the range.",
            subject="APCS",
            tags=["algorithm", "search"],
            store_path=self.store,
        )
        self.assertEqual(1, len(load_learning_records(self.store)))
        reviewed = review_learning_record(
            record.id,
            2,
            reviewed_on=date(2026, 8, 6),
            store_path=self.store,
        )
        self.assertEqual("2026-08-09", reviewed.next_review_on)
        self.assertEqual([], due_learning_records(on_date=date(2026, 8, 8), store_path=self.store))
        self.assertEqual(1, len(due_learning_records(on_date=date(2026, 8, 9), store_path=self.store)))

    def test_import_directory_skips_duplicates_and_exports_markdown(self):
        notes = self.root / "notes"
        notes.mkdir()
        (notes / "binary_search.md").write_text(
            "# Binary Search\n\nRequires a monotonic condition.", encoding="utf-8"
        )
        (notes / "ignored.csv").write_text("not,supported", encoding="utf-8")
        imported = import_learning_directory(notes, subject="APCS", store_path=self.store)
        self.assertEqual(1, len(imported))
        self.assertEqual([], import_learning_directory(notes, subject="APCS", store_path=self.store))
        exported = export_learning_record(imported[0].id, self.root / "public", store_path=self.store)
        text = exported.read_text(encoding="utf-8")
        self.assertIn("# Binary Search", text)
        self.assertIn("Requires a monotonic condition", text)


if __name__ == "__main__":
    unittest.main()

