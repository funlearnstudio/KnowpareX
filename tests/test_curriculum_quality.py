from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from knowparex.cli import (
    _recommendation_terms,
    get_curriculum_search_recommendations,
    print_curriculum_lesson_article,
)
from knowparex.curriculum_adapter import (
    curriculum_stats,
    default_curriculum_path,
    find_curriculum_topic,
    get_curriculum_lesson_article,
    get_curriculum_topic_data,
    load_curriculum_js,
)
from knowparex.curriculum_quality import (
    BROAD_CONCEPT_TERMS,
    RECOMMENDATION_STOPWORDS,
    TEMPLATE_FRAGMENTS,
    normalize_for_compare,
    organize_lesson,
    quality_issues,
    split_sentences,
)


class CurriculumQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = load_curriculum_js(default_curriculum_path())

    def iter_units(self):
        for subject, books in self.data.items():
            for book in books:
                for unit in book.get("units", []):
                    yield subject, book, unit

    def article(self, subject: str, book: str, unit: str):
        category, item = find_curriculum_topic(subject, book, unit)
        return category, item, get_curriculum_lesson_article(category, item)

    def test_all_units_pass_quality_gate(self) -> None:
        checked = 0
        for _subject, _book, unit in self.iter_units():
            title = unit["name"]
            organized = organize_lesson(unit["lessonDetails"], title)
            self.assertEqual([], quality_issues(title, organized), title)
            for formula in organized["formulas"]:
                self.assertLessEqual(len(formula), 220, title)
                self.assertLessEqual(len(split_sentences(formula)), 3, title)
                if sum(formula.count(symbol) for symbol in "=＝→⇌") >= 2:
                    for marker in ("例題", "實例", "取兩點", "再代入", "與原點資料一致"):
                        self.assertNotIn(marker, formula, title)
            for paragraph in organized["paragraphs"]:
                for fragment in TEMPLATE_FRAGMENTS:
                    self.assertNotIn(fragment, paragraph, title)
            checked += 1
        self.assertEqual(816, checked)

    def test_polynomial_function_is_topic_specific(self) -> None:
        _category, _item, article = self.article("math", "高一上", "多項式函數")
        self.assertEqual(3, len(article["paragraphs"]))
        body = "".join(article["paragraphs"])
        for expected in ("一般寫成", "次數", "係數", "零點", "因式定理", "圖形"):
            self.assertIn(expected, body)
        names = [point["topic"] for point in article["key_points"]]
        self.assertEqual(
            ["一般形式與次數", "係數與常數項", "零點", "因式定理", "圖形基本特徵"],
            names,
        )
        self.assertEqual(3, len(article["formulas"]))
        self.assertEqual(5, len(article["examples"]))
        self.assertNotIn("兩點(1,3)", body)

    def test_photosynthesis_and_respiration_is_topic_specific(self) -> None:
        _category, _item, article = self.article(
            "biology", "高一生物", "光合作用與呼吸作用"
        )
        body = "".join(article["paragraphs"])
        for expected in ("葉綠體", "類囊體膜", "卡爾文循環", "線粒體", "ATP", "物質上彼此關聯"):
            self.assertIn(expected, body)
        names = [point["topic"] for point in article["key_points"]]
        self.assertEqual(
            ["光合作用", "細胞呼吸", "能量轉換", "物質關係", "植物的氣體交換"],
            names,
        )
        self.assertEqual(2, len(article["formulas"]))
        self.assertEqual(5, len(article["examples"]))
        self.assertNotIn("同一母群", body)
        self.assertNotIn("統計判斷", body)

    def test_recommendations_ignore_generic_words_and_same_topic(self) -> None:
        category, item, article = self.article("math", "高一上", "多項式函數")
        terms = _recommendation_terms(article)
        for term, _weight, _origin in terms:
            normalized = normalize_for_compare(term)
            self.assertNotIn(normalized, RECOMMENDATION_STOPWORDS)
            self.assertNotIn(normalized, BROAD_CONCEPT_TERMS)

        recommendations = get_curriculum_search_recommendations(
            category, item, article, limit=10
        )
        names = [value["display_name"] for value in recommendations]
        self.assertNotIn("多項式函數", names)
        for recommendation in recommendations:
            for term in recommendation["matched_terms"]:
                self.assertNotIn(normalize_for_compare(term), RECOMMENDATION_STOPWORDS)

    def test_adapter_and_rendering_compatibility(self) -> None:
        category, item, article = self.article("math", "高一上", "多項式函數")
        records = get_curriculum_topic_data(category, item)
        self.assertTrue(records)
        self.assertTrue(all("relation" in record for record in records))
        output = io.StringIO()
        with redirect_stdout(output):
            print_curriculum_lesson_article(article, [])
        rendered = output.getvalue()
        for heading in ("多項式函數", "【重點知識】", "【公式與規則】", "【例子】"):
            self.assertIn(heading, rendered)

    def test_curriculum_counts_remain_compatible(self) -> None:
        stats = curriculum_stats()
        self.assertEqual(25, stats["categories"])
        self.assertEqual(816, stats["topics"])


if __name__ == "__main__":
    unittest.main()
