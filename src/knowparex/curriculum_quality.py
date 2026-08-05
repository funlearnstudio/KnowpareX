"""Curriculum content normalization and quality checks.

The source curriculum is intentionally kept compatible with the historical
JavaScript schema.  This module is the single normalization layer shared by
the adapter, importer, CLI rendering and quality tests.
"""

from __future__ import annotations

import re
import unicodedata
from difflib import SequenceMatcher
from typing import Any, Dict, Iterable, List, Sequence, Set, Tuple


RECOMMENDATION_STOPWORDS: Set[str] = {
    "其中", "例如", "以及", "並且", "因此", "所以", "包含", "使用",
    "要求", "學習", "方法", "答案", "題目", "內容", "單元", "課程",
    "重點", "知識", "概念", "公式", "規則", "說明", "結果", "條件",
    "關係", "資料", "實際", "理解", "處理", "建立", "完整", "推理",
    "檢查", "教材", "練習", "計算", "合理性", "表示", "輸入", "輸出",
    "進行", "需要", "可以", "必須", "問題", "情境", "定義", "應用",
}

# These words are meaningful inside a compound term, but too broad to create a
# recommendation on their own.
BROAD_CONCEPT_TERMS: Set[str] = {
    "函數", "作用", "系統", "方法", "模型", "變化", "運動", "生活",
    "閱讀", "寫作", "文化", "社會", "自然", "科學", "物質", "能量",
    "資料", "分析", "總複習", "整合", "入門", "進階", "概論",
}

TEMPLATE_FRAGMENTS: Tuple[str, ...] = (
    "要先建立概念邊界",
    "核心不是記住名稱",
    "可以從現象出發",
    "逐層處理基本概念",
    "每一項都要寫出已知條件",
    "逐步推理、結果與限制",
    "用單位、原始資料、反例或另一種方法檢查",
    "先列出已知條件與未知目標",
    "不能只憑關鍵字作答",
    "答案能否回應",
    "必須從定義、構成要素",
    "整合實作包含",
    "先畫出研究系統與正方向",
    "要以數學定義、符號與關係式精確表達",
    "公式、規則與完整計算",
    "推理與判讀規則",
)

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[。！？!?])|(?<=\.)\s+")
_LABEL_RE = re.compile(r"【[^】]{1,40}】")
_FORMULA_RE = re.compile(
    r"(?:[A-Za-zΑ-ωα-ω][A-Za-z0-9_₀-₉]*\s*[=＝→⇌]|"
    r"[=＝→⇌∫Σ√²³]|\b(?:sin|cos|tan|log|lim|gcd|lcm)\b)",
    re.IGNORECASE,
)
_RULE_WORD_RE = re.compile(
    r"定律|定理|守恆|內角和|外角和|同乘|同除|不等號|先.+再.+最後|"
    r"取共同質因數|取所有質因數|酸性|中性|鹼性"
)
_WORKED_EXAMPLE_RE = re.compile(
    r"(?:例如|例題|實例|取兩點|代入.+(?:所以|得到)|再代入|與原.+一致)"
)
_PUNCT_OR_SPACE_RE = re.compile(r"[\W_]+", re.UNICODE)
_CHINESE_TERM_RE = re.compile(r"[\u4e00-\u9fff]{2,12}")


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def normalize_for_compare(value: Any) -> str:
    """Normalize spacing, punctuation, width and case for de-duplication."""
    text = unicodedata.normalize("NFKC", clean_text(value)).casefold()
    return _PUNCT_OR_SPACE_RE.sub("", text)


def text_similarity(left: str, right: str) -> float:
    """Return a conservative similarity score for curriculum prose."""
    a = normalize_for_compare(left)
    b = normalize_for_compare(right)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    if min(len(a), len(b)) >= 24 and (a in b or b in a):
        return min(len(a), len(b)) / max(len(a), len(b))
    sequence = SequenceMatcher(None, a, b).ratio()
    if min(len(a), len(b)) < 8:
        return sequence
    a_pairs = {a[index:index + 2] for index in range(len(a) - 1)}
    b_pairs = {b[index:index + 2] for index in range(len(b) - 1)}
    union = a_pairs | b_pairs
    jaccard = len(a_pairs & b_pairs) / len(union) if union else 0.0
    return max(sequence, jaccard)


def is_duplicate(text: str, accepted: Sequence[str], threshold: float = 0.88) -> bool:
    return any(text_similarity(text, previous) >= threshold for previous in accepted)


def dedupe_texts(values: Iterable[Any], threshold: float = 0.88) -> List[str]:
    result: List[str] = []
    for value in values:
        text = clean_text(value)
        if not text or is_duplicate(text, result, threshold):
            continue
        result.append(text)
    return result


def split_sentences(text: str) -> List[str]:
    text = _LABEL_RE.sub("", clean_text(text))
    return [part.strip() for part in _SENTENCE_SPLIT_RE.split(text) if part.strip()]


def is_template_sentence(text: str) -> bool:
    normalized = clean_text(text)
    return any(fragment in normalized for fragment in TEMPLATE_FRAGMENTS)


def looks_like_formula(text: str) -> bool:
    return bool(_FORMULA_RE.search(text) or _RULE_WORD_RE.search(text))


def is_formula_only_sentence(text: str) -> bool:
    """Distinguish a compact rule from prose that merely mentions a formula."""
    compact = clean_text(text)
    chinese_count = len(re.findall(r"[\u4e00-\u9fff]", compact))
    equation_count = len(re.findall(r"[=＝→⇌]", compact))
    return (
        compact.startswith(("公式補全", "公式與規則", "公式、規則"))
        or chinese_count < 10
        or equation_count >= 3
    )


def _clean_sentence_sequence(text: str, *, exclude_formulas: bool) -> List[str]:
    result: List[str] = []
    for sentence in split_sentences(text):
        if is_template_sentence(sentence):
            continue
        if (
            exclude_formulas
            and looks_like_formula(sentence)
            and is_formula_only_sentence(sentence)
        ):
            continue
        if not is_duplicate(sentence, result, 0.90):
            result.append(sentence)
    return result


def clean_paragraphs(values: Any, *, maximum: int = 4) -> List[str]:
    """Build two to four readable paragraphs without formula dumps."""
    raw_values = [values] if isinstance(values, str) else list(values or [])
    paragraphs: List[str] = []

    for value in raw_values:
        sentences = _clean_sentence_sequence(clean_text(value), exclude_formulas=True)
        if not sentences:
            continue
        paragraph = "".join(sentences)
        if not is_duplicate(paragraph, paragraphs, 0.86):
            paragraphs.append(paragraph)
        if len(paragraphs) >= maximum:
            break

    # A single source paragraph is split only at sentence boundaries.  No
    # filler sentence is invented merely to reach the preferred count.
    if len(paragraphs) == 1:
        sentences = split_sentences(paragraphs[0])
        if len(sentences) >= 4:
            midpoint = (len(sentences) + 1) // 2
            paragraphs = ["".join(sentences[:midpoint]), "".join(sentences[midpoint:])]

    return paragraphs


def clean_formulas(explicit_values: Any, paragraph_values: Any = None) -> List[str]:
    """Keep compact formulas/rules and discard prose or worked examples."""
    explicit = (
        [explicit_values]
        if isinstance(explicit_values, str)
        else list(explicit_values or [])
    )
    paragraphs = (
        [paragraph_values]
        if isinstance(paragraph_values, str)
        else list(paragraph_values or [])
    )
    candidates: List[str] = []

    for value in explicit:
        matching = [
            sentence
            for sentence in split_sentences(clean_text(value))
            if looks_like_formula(sentence)
            and not is_template_sentence(sentence)
            and not (
                _WORKED_EXAMPLE_RE.search(sentence)
                and len(re.findall(r"[=＝→⇌]", sentence)) >= 2
            )
            and len(sentence) <= 220
        ]
        # One stored formula item may have accumulated an article.  Retain at
        # most three compact formula/rule sentences from that item.
        candidates.extend(matching[:3])

    # Paragraphs are not a general formula source.  Only explicitly labelled
    # formula supplements are recovered for legacy units whose formula array
    # was empty.
    for value in paragraphs:
        matching = [
            sentence
            for sentence in split_sentences(clean_text(value))
            if "公式補全" in sentence
            and looks_like_formula(sentence)
            and len(sentence) <= 220
        ]
        candidates.extend(matching[:3])

    return dedupe_texts(candidates, 0.90)


def concept_terms(text: str) -> Set[str]:
    """Extract conservative concept tokens for relevance checks."""
    terms: Set[str] = set()
    normalized = unicodedata.normalize("NFKC", clean_text(text)).casefold()
    for term in _CHINESE_TERM_RE.findall(normalized):
        if term not in RECOMMENDATION_STOPWORDS:
            terms.add(term)
        if len(term) >= 4:
            for size in (2, 3, 4):
                for index in range(len(term) - size + 1):
                    piece = term[index:index + size]
                    if (
                        piece not in RECOMMENDATION_STOPWORDS
                        and piece not in BROAD_CONCEPT_TERMS
                    ):
                        terms.add(piece)
    terms.update(
        token
        for token in re.findall(r"[a-z][a-z0-9_-]{1,20}", normalized)
        if token not in RECOMMENDATION_STOPWORDS
    )
    return terms


def example_is_relevant(topic: str, example: str) -> bool:
    """Reject examples with no lexical connection to their knowledge point."""
    topic_normalized = normalize_for_compare(topic)
    example_normalized = normalize_for_compare(example)
    if not topic_normalized or not example_normalized:
        return False
    if topic_normalized in example_normalized:
        return True
    topic_terms = concept_terms(topic)
    example_terms = concept_terms(example)
    return bool(topic_terms & example_terms)


def clean_key_points(points: Any, *, maximum: int = 6) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []
    names: List[str] = []
    explanations: List[str] = []

    for point in points or []:
        if not isinstance(point, dict):
            continue
        topic = clean_text(point.get("topic"))
        explanation_sentences = _clean_sentence_sequence(
            clean_text(point.get("explanation")),
            exclude_formulas=True,
        )
        explanation = "".join(explanation_sentences[:3])
        example = clean_text(point.get("example"))

        if not topic or is_duplicate(topic, names, 0.92):
            continue
        if not explanation or is_duplicate(explanation, explanations, 0.88):
            continue
        if example and (
            is_template_sentence(example)
            or not example_is_relevant(topic, example)
        ):
            example = ""

        result.append({
            "topic": topic,
            "explanation": explanation,
            "example": example,
        })
        names.append(topic)
        explanations.append(explanation)
        if len(result) >= maximum:
            break

    return result


def _remove_cross_section_duplicates(
    paragraphs: List[str],
    points: List[Dict[str, str]],
    formulas: List[str],
) -> List[str]:
    protected = formulas + [
        value
        for point in points
        for value in (point["explanation"], point["example"])
        if value
    ]
    result: List[str] = []
    for paragraph in paragraphs:
        sentences = [
            sentence
            for sentence in split_sentences(paragraph)
            if not is_duplicate(sentence, protected, 0.92)
        ]
        cleaned = "".join(sentences)
        if cleaned and not is_duplicate(cleaned, result, 0.88):
            result.append(cleaned)
    return result


def _condense_point_explanation(
    point: Dict[str, str],
    paragraphs: List[str],
    formulas: List[str],
) -> str:
    """Keep a short factual summary when a point copied an article paragraph."""
    explanation = point["explanation"]
    if is_duplicate(explanation, formulas, 0.92):
        return ""
    if not is_duplicate(explanation, paragraphs, 0.92):
        return explanation

    sentences = split_sentences(explanation)
    if len(sentences) > 1:
        candidates = sentences
    else:
        candidates = [
            clean_text(part)
            for part in re.split(r"[，；：]", explanation)
            if len(normalize_for_compare(part)) >= 8
        ]
    for candidate in candidates:
        if candidate and not is_duplicate(candidate, paragraphs, 0.92):
            return candidate
    return ""


def organize_lesson(details: Dict[str, Any], title: str = "") -> Dict[str, Any]:
    """Return a compatible, de-duplicated textbook presentation."""
    lesson_values = details.get("readableLesson") or details.get("lessonText") or []
    points = clean_key_points(details.get("keyPoints", []))
    formulas = clean_formulas(details.get("formulas", []), lesson_values)
    paragraphs = clean_paragraphs(lesson_values)
    paragraphs = _remove_cross_section_duplicates(paragraphs, points, formulas)

    # Prefer prose for broad explanation and keep key points only when they add
    # a distinct concise statement.  This prevents the same sentence from
    # appearing under both the article and knowledge headings.
    distinct_points: List[Dict[str, str]] = []
    distinct_explanations: List[str] = []
    for point in points:
        explanation = _condense_point_explanation(point, paragraphs, formulas)
        if not explanation or is_duplicate(explanation, distinct_explanations, 0.88):
            continue
        example = point.get("example", "")
        if is_duplicate(example, paragraphs + formulas, 0.92):
            example = ""
        distinct_points.append({
            **point,
            "explanation": explanation,
            "example": example,
        })
        distinct_explanations.append(explanation)
    points = distinct_points

    examples = dedupe_texts(
        point["example"] for point in points if point.get("example")
    )

    return {
        "paragraphs": paragraphs,
        "formulas": formulas,
        "key_points": points,
        "examples": examples,
    }


def quality_issues(title: str, organized: Dict[str, Any]) -> List[str]:
    """Return machine-readable reasons a unit should be regenerated."""
    issues: List[str] = []
    paragraphs = organized.get("paragraphs", []) or []
    points = organized.get("key_points", []) or []
    formulas = organized.get("formulas", []) or []
    examples = organized.get("examples", []) or []

    if len(dedupe_texts(paragraphs)) != len(paragraphs):
        issues.append("duplicate_paragraph")
    names = [point.get("topic", "") for point in points]
    if len(dedupe_texts(names, 0.92)) != len(names):
        issues.append("duplicate_key_point_name")
    explanations = [point.get("explanation", "") for point in points]
    if len(dedupe_texts(explanations, 0.88)) != len(explanations):
        issues.append("duplicate_key_point_explanation")
    if any(len(formula) > 220 or len(split_sentences(formula)) > 3 for formula in formulas):
        issues.append("formula_too_long")
    if any(is_template_sentence(paragraph) for paragraph in paragraphs):
        issues.append("template_sentence")
    if any(is_template_sentence(example) for example in examples):
        issues.append("template_example")
    if any(term in RECOMMENDATION_STOPWORDS for term in concept_terms(title)):
        issues.append("title_stopword")
    if examples and not all(
        any(example_is_relevant(point.get("topic", ""), example) for point in points)
        for example in examples
    ):
        issues.append("irrelevant_example")
    section_values = formulas + explanations + examples
    if any(
        is_duplicate(paragraph, section_values, 0.92)
        for paragraph in paragraphs
    ):
        issues.append("cross_section_duplicate")
    if any(
        is_duplicate(formula, explanations + examples, 0.92)
        for formula in formulas
    ):
        issues.append("cross_section_duplicate")
    if title and paragraphs:
        title_terms = concept_terms(title)
        body_terms = concept_terms("".join(paragraphs))
        if title_terms and not title_terms.intersection(body_terms):
            issues.append("title_not_explained")
    return issues


# Semantic checks are deliberately conservative: they catch known impossible
# subject combinations and missing topic evidence, but do not claim to replace
# review by a qualified teacher.
SUBJECT_FORBIDDEN_TERMS: Dict[str, Tuple[str, ...]] = {
    "physics": ("卡爾文循環", "葉綠體", "等位基因", "遺傳漂變", "氧化數", "限制試劑"),
    "chemistry": ("牛頓第二定律", "向心加速度", "卡爾文循環", "遺傳漂變", "拋物線的焦點"),
    "biology": ("歐姆定律", "串聯電阻", "向心力", "二次函數頂點", "莫耳質量"),
    "math": ("葉綠體", "細胞呼吸", "氧化數", "電磁感應", "板塊邊界"),
    "earth": ("歐姆定律", "卡爾文循環", "限制試劑", "二次函數頂點"),
}

TITLE_REQUIRED_TERMS: Dict[str, Tuple[str, ...]] = {
    "牛頓第二定律": ("合力", "加速度", "質量"),
    "細胞呼吸": ("ATP", "糖解", "粒線體"),
    "歐姆定律": ("電壓", "電流", "電阻"),
    "電功率": ("功率", "電壓", "電流"),
    "氧化數": ("氧化", "還原", "電子"),
    "ATP": ("磷酸", "能量", "細胞"),
    "遺傳漂變": ("隨機", "族群", "等位基因"),
    "拋物線": ("焦點", "準線", "對稱軸"),
    "限制試劑": ("反應物", "化學計量", "產物"),
    "板塊": ("板塊", "邊界", "地震"),
}


def semantic_issues(subject: str, title: str, details: Dict[str, Any]) -> List[str]:
    """Audit topic/subject consistency as well as lesson completeness.

    The check operates on the stored schema (including ``commonTrap``), not on
    the adapter's presentation-only normalization.
    """
    issues: List[str] = []
    paragraphs = details.get("readableLesson") or details.get("lessonText") or []
    points = details.get("keyPoints") or []
    formulas = details.get("formulas") or []
    if not isinstance(paragraphs, list) or not 2 <= len(paragraphs) <= 5:
        issues.append("paragraph_count")
    if not isinstance(points, list) or len(points) < 3:
        issues.append("key_point_count")
    for index, point in enumerate(points if isinstance(points, list) else [], start=1):
        if not isinstance(point, dict):
            issues.append("key_point_%d_not_object" % index)
            continue
        for field in ("topic", "explanation", "example", "commonTrap"):
            if len(clean_text(point.get(field))) < (2 if field == "topic" else 12):
                issues.append("key_point_%d_missing_%s" % (index, field))

    text = "\n".join(
        [clean_text(title)]
        + [clean_text(value) for value in paragraphs]
        + [clean_text(value) for value in formulas]
        + [clean_text(point.get(field)) for point in points if isinstance(point, dict)
           for field in ("topic", "explanation", "example", "commonTrap")]
    )
    for term in SUBJECT_FORBIDDEN_TERMS.get(subject, ()):
        if term in text:
            issues.append("cross_subject_term:%s" % term)

    for trigger, required in TITLE_REQUIRED_TERMS.items():
        if trigger in title and any(term not in text for term in required):
            issues.append("missing_semantic_evidence:%s" % trigger)

    organized = organize_lesson(details, title)
    issues.extend("format:%s" % issue for issue in quality_issues(title, organized))
    return sorted(set(issues))
