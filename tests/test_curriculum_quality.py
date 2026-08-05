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
    semantic_issues,
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

    def test_high_school_physics_units_are_fully_rewritten(self) -> None:
        checked = 0
        for subject, book, unit in self.iter_units():
            if subject != "physics" or book.get("stage") != "high_school":
                continue
            details = unit["lessonDetails"]
            self.assertEqual([], semantic_issues(subject, unit["name"], details), unit["name"])
            self.assertGreaterEqual(len(details["readableLesson"]), 2)
            self.assertGreaterEqual(len(details["keyPoints"]), 3)
            self.assertTrue(all(point.get("commonTrap") for point in details["keyPoints"]))
            checked += 1
        self.assertEqual(24, checked)

    def test_semantic_regressions_for_required_topics(self) -> None:
        cases = {
            "牛頓第二定律": ("physics", "合力、質量與加速度彼此相連。"),
            "細胞呼吸": ("biology", "糖解後在粒線體合成ATP。"),
            "歐姆定律": ("physics", "電壓、電流與電阻必須同時判讀。"),
            "電功率": ("physics", "功率等於電壓乘電流。"),
            "氧化數": ("chemistry", "追蹤電子可判斷氧化與還原。"),
            "ATP": ("biology", "ATP的磷酸基轉移為細胞提供可用能量。"),
            "遺傳漂變": ("biology", "小族群的等位基因頻率會因隨機抽樣改變。"),
            "拋物線": ("math", "拋物線由焦點、準線與對稱軸描述。"),
            "限制試劑": ("chemistry", "依化學計量比較反應物，限制試劑決定產物上限。"),
            "板塊": ("earth", "板塊邊界的運動與地震分布密切相關。"),
        }
        for title, (subject, evidence) in cases.items():
            with self.subTest(title=title):
                details = {
                    "readableLesson": [f"{title}的核心如下。{evidence}", f"實際判讀時仍須核對{title}的條件與證據。"],
                    "lessonText": [f"{title}的核心如下。{evidence}", f"實際判讀時仍須核對{title}的條件與證據。"],
                    "formulas": [],
                    "keyPoints": [
                        {"topic": f"{title}概念{i}", "explanation": f"這是與{title}直接相關且可驗證的第{i}項解釋。", "example": f"以具體情境{i}示範{title}的正確判斷。", "commonTrap": f"不可把不相關學科內容混入{title}的第{i}項判斷。"}
                        for i in range(1, 4)
                    ],
                }
                self.assertEqual([], semantic_issues(subject, title, details))

    def test_semantic_audit_rejects_cross_subject_pollution(self) -> None:
        details = {
            "readableLesson": ["電功率說明電能轉換速率。", "葉綠體的卡爾文循環固定二氧化碳。"],
            "lessonText": ["電功率說明電能轉換速率。", "葉綠體的卡爾文循環固定二氧化碳。"],
            "formulas": ["P=VI。"],
            "keyPoints": [
                {"topic": "功率", "explanation": "電功率是單位時間轉換的電能。", "example": "12 V、2 A時功率為24 W。", "commonTrap": "不可混淆功率與電能。"},
                {"topic": "電壓", "explanation": "電壓是單位電荷的能量差。", "example": "電池兩端可維持電位差。", "commonTrap": "不可把電壓當作電流。"},
                {"topic": "電流", "explanation": "電流是單位時間通過的電量。", "example": "每秒2 C代表2 A。", "commonTrap": "不可把安培當作能量單位。"},
            ],
        }
        issues = semantic_issues("physics", "電功率", details)
        self.assertIn("cross_subject_term:卡爾文循環", issues)
        self.assertIn("cross_subject_term:葉綠體", issues)

    def test_junior_high_physical_science_units_are_fully_rewritten(self) -> None:
        expected = {
            "基本測量與密度", "認識物質", "波動與聲音", "光與成像", "溫度與熱", "物質的變化",
            "原子分子與反應式", "化學反應與質量守恆", "氧化還原", "酸鹼鹽", "反應速率", "有機物與材料",
            "力與運動", "功與能", "電流電壓與電阻", "電功率與生活用電", "磁場與電磁感應", "科技與能源",
        }
        seen = set()
        for subject, book, unit in self.iter_units():
            if subject != "science" or book.get("stage") != "junior_high":
                continue
            self.assertIn(unit["name"], expected)
            semantic_subject = "chemistry" if unit["name"] in {
                "認識物質", "物質的變化", "原子分子與反應式", "化學反應與質量守恆",
                "氧化還原", "酸鹼鹽", "反應速率", "有機物與材料",
            } else "physics"
            details = unit["lessonDetails"]
            self.assertEqual([], semantic_issues(semantic_subject, unit["name"], details), unit["name"])
            self.assertEqual(2, len(details["readableLesson"]))
            self.assertGreaterEqual(len(details["keyPoints"]), 3)
            self.assertTrue(all(point.get("example") and point.get("commonTrap") for point in details["keyPoints"]))
            seen.add(unit["name"])
        self.assertEqual(expected, seen)

    def test_junior_high_known_pollution_regressions(self) -> None:
        checks = {
            "基本測量與密度": (("密度", "質量", "體積", "ρ=m/V"), ("磁極", "電磁感應")),
            "電流電壓與電阻": (("歐姆定律", "電流", "電壓", "電阻"), ("磁通量", "法拉第")),
            "電功率與生活用電": (("電功率", "P=VI", "kWh", "用電安全"), ("ρ=m/V", "同名磁極")),
            "磁場與電磁感應": (("磁場", "線圈", "感應電流"), ("密度", "酸鹼")),
            "氧化還原": (("氧化數", "電子", "氧化劑", "還原劑"), ("pH", "聚合物")),
            "酸鹼鹽": (("酸", "鹼", "pH", "中和"), ("反應速率", "氧化劑")),
            "反應速率": (("速率", "碰撞", "催化劑", "時間"), ("酸鹼", "聚合物")),
            "原子分子與反應式": (("原子", "分子", "化學式", "配平"), ("反應速率", "酸鹼")),
        }
        by_title = {
            unit["name"]: unit["lessonDetails"]
            for subject, book, unit in self.iter_units()
            if subject == "science" and book.get("stage") == "junior_high"
        }
        for title, (required, forbidden) in checks.items():
            with self.subTest(title=title):
                details = by_title[title]
                text = str(details)
                for term in required:
                    self.assertIn(term, text)
                for term in forbidden:
                    self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
