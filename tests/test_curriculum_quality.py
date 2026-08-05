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
        self.assertGreaterEqual(len(article["paragraphs"]), 2)
        body = "".join(article["paragraphs"])
        for expected in ("多項式", "餘式", "二次函數", "定義域"):
            self.assertIn(expected, body)
        names = [point["topic"] for point in article["key_points"]]
        self.assertEqual(["多項式與餘式", "二次函數", "代數式運算"], names)
        self.assertGreaterEqual(len(article["formulas"]), 3)
        self.assertEqual(3, len(article["examples"]))
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

    def test_high_school_chemistry_units_are_fully_rewritten(self) -> None:
        expected = {
            "物質組成與分類", "原子結構", "週期表與元素性質", "化學鍵", "莫耳與化學計量", "溶液與濃度", "化學反應式", "生活中的化學",
            "氣體與溶液", "反應熱", "反應速率", "化學平衡", "酸鹼平衡", "氧化還原", "電化學", "實驗與誤差",
            "有機化學入門", "烴與官能基", "醇醛酸酯", "高分子材料", "環境化學", "材料化學", "化學素養題", "分科化學總複習",
        }
        seen = set()
        for subject, book, unit in self.iter_units():
            if subject != "chemistry" or book.get("stage") != "high_school":
                continue
            details = unit["lessonDetails"]
            self.assertEqual([], semantic_issues("chemistry", unit["name"], details), unit["name"])
            self.assertEqual(2, len(details["readableLesson"]))
            self.assertGreaterEqual(len(details["keyPoints"]), 3)
            self.assertTrue(all(
                all(point.get(field) for field in ("topic", "explanation", "example", "commonTrap"))
                for point in details["keyPoints"]
            ))
            seen.add(unit["name"])
        self.assertEqual(expected, seen)

    def test_high_school_chemistry_concept_regressions(self) -> None:
        checks = {
            "莫耳與化學計量": (("莫耳", "6.022×10²³", "限制試劑", "3 mol H₂O"), ("半導體", "污染物")),
            "氧化還原": (("氧化數", "氧化劑", "還原劑", "電子"), ("pH", "緩衝液")),
            "電化學": (("原電池", "電解池", "陽極", "陰極", "電子", "1.10 V"), ("歐姆定律", "磁場")),
            "化學平衡": (("動態平衡", "平衡常數", "反應商", "Q<K"), ("速率方程", "緩衝公式")),
            "酸鹼平衡": (("共軛酸鹼", "Ka", "pH", "緩衝", "pH=3.00"), ("電池電位", "催化劑降低活化能")),
            "反應速率": (("反應速率", "碰撞", "活化能", "速率方程", "0.10 M/s"), ("平衡產率", "pH=-log")),
            "烴與官能基": (("有機官能基", "羥基", "羰基", "羧基", "酯基"), ("半導體摻雜", "酸雨")),
        }
        by_title = {
            unit["name"]: unit["lessonDetails"]
            for subject, book, unit in self.iter_units()
            if subject == "chemistry" and book.get("stage") == "high_school"
        }
        for title, (required, forbidden) in checks.items():
            with self.subTest(title=title):
                text = str(by_title[title])
                for term in required:
                    self.assertIn(term, text)
                for term in forbidden:
                    self.assertNotIn(term, text)

    def test_high_school_math_units_are_fully_rewritten(self) -> None:
        checked = 0
        for subject, book, unit in self.iter_units():
            if subject != "math" or book.get("stage") != "high_school":
                continue
            details = unit["lessonDetails"]
            self.assertEqual([], semantic_issues("math", unit["name"], details), unit["name"])
            self.assertEqual(2, len(details["readableLesson"]))
            self.assertGreaterEqual(len(details["keyPoints"]), 3)
            self.assertTrue(all(all(point.get(k) for k in ("topic", "explanation", "example", "commonTrap")) for point in details["keyPoints"]))
            checked += 1
        self.assertEqual(36, checked)

    def test_high_school_math_concept_regressions(self) -> None:
        required = {
            "多項式函數": ("餘式定理", "二次函數"), "指數與對數": ("a>0", "a≠1", "真數", "x>0"),
            "三角函數": ("弧度", "tan", "x≠π/2+kπ"), "平面向量": ("內積", "u·v"),
            "空間向量": ("叉積", "v×u"), "直線方程式": ("斜率", "x₂-x₁"),
            "圓方程式": ("圓心", "r>0"), "圓錐曲線": ("橢圓", "雙曲線", "拋物線"),
            "數列級數": ("等差", "等比", "|r|<1"), "排列組合": ("排列", "組合", "P(n,r)"),
            "機率": ("0≤P(A)≤1", "樣本"), "數據分析": ("平均", "標準差"),
            "極限概念": ("0/0", "x≠2"), "微分與導數": ("瞬時變化率", "平均變化率", "f′(3)"),
            "積分概念": ("反導函數", "+C", "=4"), "二次函數": ("a≠0", "拋物線"),
        }
        by_title={u["name"]:u["lessonDetails"] for s,b,u in self.iter_units() if s=="math" and b.get("stage")=="high_school"}
        # The curriculum title is 「多項式函數」; its quadratic point supplies
        # the required high-school quadratic-function regression.
        for title, terms in required.items():
            target = "多項式函數" if title == "二次函數" else title
            with self.subTest(title=title):
                text=str(by_title[target])
                for term in terms: self.assertIn(term,text)

    def test_math_semantic_audit_detects_known_failure_modes(self) -> None:
        base={"readableLesson":["主題正文包含足夠定義與條件。","第二段提供直接相關的推理與限制。"],"lessonText":["主題正文包含足夠定義與條件。","第二段提供直接相關的推理與限制。"],"formulas":[],"keyPoints":[{"topic":f"重點{i}","explanation":"這是一段完整而可檢驗的數學解釋。","example":"具體例子含有正確步驟與答案。","commonTrap":"不可忽略定義條件與符號限制。"} for i in range(3)]}
        import copy
        cases=[("二次函數","二次函數兩點斜率主例", "math:quadratic_linear_slope_pollution"),("圓方程式","牛頓第二定律", "math:geometry_cross_subject:牛頓第二定律"),("機率","排列數直接等於機率", "math:count_is_probability"),("對數函數","只有log運算但沒有條件", "math:log_domain_missing"),("微分與導數","平均變化率就是導數", "math:average_rate_as_derivative")]
        for title,bad,expected in cases:
            with self.subTest(title=title):
                details=copy.deepcopy(base); details["readableLesson"][0]+=bad; details["lessonText"]=list(details["readableLesson"])
                self.assertIn(expected,semantic_issues("math",title,details))

    def test_junior_high_math_units_are_fully_rewritten(self) -> None:
        checked=0
        for subject,book,unit in self.iter_units():
            if subject!="math" or book.get("stage")!="junior_high": continue
            d=unit["lessonDetails"]
            self.assertEqual([],semantic_issues("math",unit["name"],d),unit["name"])
            self.assertEqual(2,len(d["readableLesson"]));self.assertGreaterEqual(len(d["keyPoints"]),3)
            self.assertTrue(all(all(p.get(k) for k in ("topic","explanation","example","commonTrap")) for p in d["keyPoints"]));checked+=1
        self.assertEqual(36,checked)

    def test_junior_high_math_concept_regressions(self) -> None:
        checks={"整數與數線":("正負數","|-7|=7"),"因數倍數與分數運算":("整數指數律","2⁷=128"),"一元一次方程式":("x=5",),"二元一次聯立方程式":("(4,3)",),"比與比例式":("正比例","反比例","x≠0"),"線型函數":("斜率",),"平方根與畢氏定理":("實數","非負","直角三角形","=10"),"因式分解":("(x-2)(x-3)",),"一元二次方程式":("a≠0","解2、3"),"二次函數":("拋物線","a≠0"),"相似形入門":("對應角相等","對應邊","全等"),"圓周角與切線":("圓周角","切線","60°"),"統計與盒狀圖":("中位數3","IQR"),"機率初步":("0≤P(A)≤1","理論機率"),}
        data={u["name"]:str(u["lessonDetails"]) for s,b,u in self.iter_units() if s=="math" and b.get("stage")=="junior_high"}
        for title,terms in checks.items():
            with self.subTest(title=title):
                for term in terms:self.assertIn(term,data[title])


if __name__ == "__main__":
    unittest.main()
