from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from knowparex.cli import search_main
from knowparex.curriculum_adapter import (
    default_curriculum_path,
    find_curriculum_topic,
    get_curriculum_lesson_article,
    load_curriculum_js,
)
from knowparex.curriculum_quality import semantic_issues


class Release170Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_curriculum_js(default_curriculum_path())

    def test_cli_curriculum_first_results(self):
        expected = {
            "牛頓第二定律": "力與牛頓定律",
            "細胞呼吸": "光合作用與呼吸作用",
            "歐姆定律": "電流電壓與電阻",
            "電功率": "電功率與生活用電",
            "氧化數": "氧化還原",
            "ATP": "酵素與能量代謝",
            "遺傳漂變": "演化與分類",
            "拋物線": "二次函數",
            "限制試劑": "莫耳與化學計量",
            "板塊": "板塊構造",
        }
        for query, wanted in expected.items():
            with self.subTest(query=query):
                output = io.StringIO()
                with patch("builtins.input", return_value="1"), redirect_stdout(output):
                    search_main(query, open_topic=True, source="curriculum")
                first = next(
                    line.strip()
                    for line in output.getvalue().splitlines()
                    if line.strip().startswith("1. ")
                )
                self.assertIn(wanted, first)
                self.assertIn("【重點知識】", output.getvalue())

    def test_targeted_204_units_pass_semantic_audit(self):
        checked = 0
        targeted_ids = []
        for subject, books in self.data.items():
            for book in books:
                stage = book.get("stage")
                targeted = (
                    (subject == "physics" and stage == "high_school")
                    or (subject == "science" and stage == "junior_high")
                    or (subject == "chemistry" and stage == "high_school")
                    or (subject == "math" and stage in {"junior_high", "high_school"})
                    or (subject == "biology" and stage in {"junior_high", "high_school"})
                    or (subject == "earth" and stage in {"junior_high", "high_school"})
                )
                if not targeted:
                    continue
                for unit in book.get("units", []):
                    targeted_ids.append((subject, stage, book["book"], unit["name"]))
                    semantic_subject = subject
                    if subject == "science":
                        semantic_subject = "chemistry" if unit["name"] in {
                            "認識物質", "物質的變化", "原子分子與反應式",
                            "化學反應與質量守恆", "氧化還原", "酸鹼鹽",
                            "反應速率", "有機物與材料",
                        } else "physics"
                    elif subject in {"biology", "earth"}:
                        semantic_subject = f"{subject}_{stage}"
                    self.assertEqual(
                        [],
                        semantic_issues(semantic_subject, unit["name"], unit["lessonDetails"]),
                        f"{subject}/{stage}/{unit['name']}",
                    )
                    checked += 1
        self.assertEqual(204, checked)
        self.assertEqual(204, len(set(targeted_ids)))

    def test_catalog_has_816_unique_units(self):
        unit_ids = [
            (subject, book["stage"], book["book"], unit["name"])
            for subject, books in self.data.items()
            for book in books
            for unit in book.get("units", [])
        ]
        self.assertEqual(816, len(unit_ids))
        self.assertEqual(816, len(set(unit_ids)))

    def test_release_content_samples_are_complete_and_clean(self):
        samples = [
            ("physics", "高一物理", "光學入門"),
            ("physics", "高一物理", "力與牛頓定律"),
            ("science", "國三下", "電功率與生活用電"),
            ("science", "國三上", "電流電壓與電阻"),
            ("chemistry", "高二化學", "氧化還原"),
            ("chemistry", "高一化學", "莫耳與化學計量"),
            ("math", "國三上", "二次函數"),
            ("biology", "高一生物", "光合作用與呼吸作用"),
            ("biology", "國一下", "演化"),
            ("earth", "高一地科", "板塊構造"),
        ]
        forbidden = {
            "電功率與生活用電": ("ρ=m/V", "同名磁極"),
            "光學入門": ("牛頓第二定律", "ΣF=ma"),
            "光合作用與呼吸作用": ("V=IR", "莫耳質量", "二次函數"),
            "演化": ("V=IR", "莫耳質量", "二次函數"),
            "二次函數": ("ΣF=ma", "莫耳", "化學反應式"),
        }
        for subject, book, title in samples:
            with self.subTest(title=title):
                category, item = find_curriculum_topic(subject, book, title)
                article = get_curriculum_lesson_article(category, item)
                self.assertGreaterEqual(len(article["paragraphs"]), 2)
                self.assertGreaterEqual(len(article["key_points"]), 3)
                self.assertGreaterEqual(len(article["examples"]), 3)
                text = str(article)
                for term in forbidden.get(title, ()):
                    self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
