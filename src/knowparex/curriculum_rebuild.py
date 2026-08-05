#!/usr/bin/env python3
"""Rebuild and audit curriculum content without changing the JS schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple

try:
    from .curriculum_adapter import load_curriculum_js
    from .curriculum_quality import (
        TEMPLATE_FRAGMENTS,
        clean_text,
        organize_lesson,
        quality_issues,
        text_similarity,
    )
except ImportError:  # Support direct script execution.
    from curriculum_adapter import load_curriculum_js
    from curriculum_quality import (
        TEMPLATE_FRAGMENTS,
        clean_text,
        organize_lesson,
        quality_issues,
        text_similarity,
    )


CURATED_UNITS: Dict[Tuple[str, str], Dict[str, Any]] = {
    ("math", "多項式函數"): {
        "paragraphs": [
            "多項式函數是由有限個非負整數次冪項相加而成的函數，一般寫成f(x)=aₙxⁿ+aₙ₋₁xⁿ⁻¹+⋯+a₁x+a₀，其中n是非負整數，最高次項係數aₙ不為0。n稱為多項式的次數，各項前的數稱為係數，a₀是常數項。一次函數與二次函數分別是一次、二次多項式函數。",
            "使f(c)=0的數c稱為零點，也就是函數圖形與x軸交點的橫坐標。因式定理指出，f(c)=0若且唯若x-c是f(x)的因式；因此找零點、因式分解與解多項式方程式是彼此相連的工作。",
            "多項式函數的圖形連續而平滑，不會突然中斷。最高次項決定|x|很大時圖形兩端的大致方向；實係數多項式在實零點處可能穿越或接觸x軸，行為與該零點的重根次數有關。局部轉折仍須配合後續的函數分析工具判斷。",
        ],
        "key_points": [
            {
                "topic": "一般形式與次數",
                "explanation": "多項式函數由有限個非負整數次冪項組成；最高非零項的指數就是次數。",
                "example": "一般形式與次數：f(x)=2x³-5x+1是三次多項式函數，最高次項係數為2，常數項為1。",
            },
            {
                "topic": "係數與常數項",
                "explanation": "係數決定各次冪項的權重；沒有寫出的次冪項，其係數視為0。",
                "example": "係數與常數項：f(x)=x³-4的x²項與x項係數都是0，常數項是-4。",
            },
            {
                "topic": "零點",
                "explanation": "零點c滿足f(c)=0，圖形上的對應點(c,0)位於x軸。",
                "example": "零點：f(x)=x²-9時，f(3)=0且f(-3)=0，所以零點為3與-3。",
            },
            {
                "topic": "因式定理",
                "explanation": "f(c)=0與x-c是f(x)的因式互為充要條件，可用來檢查候選零點並進行因式分解。",
                "example": "因式定理：f(2)=2²-3×2+2=4-6+2=0，因此x-2是x²-3x+2的因式。",
            },
            {
                "topic": "圖形基本特徵",
                "explanation": "多項式函數圖形連續；最高次項控制兩端趨勢，實零點及其重數影響圖形與x軸的交會方式。",
                "example": "圖形基本特徵：y=(x-1)²在x=1接觸x軸後折回，而y=(x-1)³在x=1穿越x軸。",
            },
        ],
        "formulas": [
            "一般形式：f(x)=aₙxⁿ+aₙ₋₁xⁿ⁻¹+⋯+a₁x+a₀，n為非負整數且aₙ≠0。",
            "零點：f(c)=0。",
            "因式定理：f(c)=0 ⇔ x-c是f(x)的因式。",
        ],
    },
    ("biology", "光合作用與呼吸作用"): {
        "paragraphs": [
            "光合作用把光能轉換成有機物中的化學能。植物主要在葉綠體進行光合作用：光反應在類囊體膜吸收光能，產生ATP與NADPH並釋放氧；卡爾文循環在基質利用二氧化碳合成醣類。",
            "細胞呼吸把有機物中的化學能轉移到ATP，供細胞進行主動運輸、合成與運動。糖解作用發生在細胞質；有氧條件下，後續反應主要在線粒體進行，氧在電子傳遞鏈末端接受電子，最終形成水。",
            "光合作用與呼吸作用在物質上彼此關聯：光合作用產生的有機物與氧可供有氧呼吸使用，呼吸作用產生的二氧化碳與水又可成為光合作用的原料。能量不在兩者之間循環；能量由光進入生態系，經化學能轉換後逐漸以熱散失。植物白天與夜晚都會呼吸，但只有在有光且條件適合時進行光合作用。",
        ],
        "key_points": [
            {
                "topic": "光合作用",
                "explanation": "光合作用在葉綠體將光能轉成化學能，利用二氧化碳和水合成有機物並釋放氧。",
                "example": "光合作用：比較同一株植物白天受光葉片與遮光葉片的澱粉形成，可觀察光對光合作用產物的影響。",
            },
            {
                "topic": "細胞呼吸",
                "explanation": "細胞呼吸分解有機物並將能量轉移到ATP；有氧呼吸的主要後續步驟在線粒體進行。",
                "example": "細胞呼吸：萌發種子的呼吸速率較高，會消耗較多氧並釋放較多二氧化碳與熱。",
            },
            {
                "topic": "能量轉換",
                "explanation": "光合作用儲存由光而來的能量，細胞呼吸釋放有機物中的能量並供ATP合成。",
                "example": "能量轉換：葉片製造的葡萄糖可運送到根部，根細胞再藉呼吸作用取得可用能量。",
            },
            {
                "topic": "物質關係",
                "explanation": "光合作用與有氧呼吸的總反應在反應物和產物上大致相反，但兩者包含不同場所與多個反應步驟。",
                "example": "物質關係：形成2 mol葡萄糖需要12 mol二氧化碳，並可依總反應式產生12 mol氧。",
            },
            {
                "topic": "植物的氣體交換",
                "explanation": "植物隨時進行呼吸；淨氣體交換取決於光合作用速率與呼吸速率的相對大小。",
                "example": "植物的氣體交換：光照充足時葉片可能淨吸收二氧化碳，黑暗中停止光合作用後則淨釋放二氧化碳。",
            },
        ],
        "formulas": [
            "光合作用總反應：6CO₂+6H₂O+光能→C₆H₁₂O₆+6O₂。",
            "有氧呼吸總反應：C₆H₁₂O₆+6O₂→6CO₂+6H₂O+能量。",
        ],
    },
}


RELIABLE_PARAGRAPH_REPLACEMENTS: Dict[Tuple[str, str], List[str]] = {
    ("math", "兩步驟四則問題"): [
        "兩步驟四則問題需要把一個情境拆成前後相依的兩次運算。先確認第二步需要使用哪個中間量，再決定第一步要先求什麼；若兩步關係容易混淆，可用括號把先算的部分標出來。",
        "列式後依先括號、再乘除、後加減的順序計算。答案必須回到原情境確認單位與數量意義，例如先求每組數量再求總數，不能把兩個互不相干的數直接相加。",
    ],
    ("math", "機率統計整合"): [
        "機率描述隨機事件發生的可能程度，統計則由觀察資料整理分布、中心與變異。兩者結合時，可用機率模型預測長期比例，再以實際樣本檢查模型是否合理。",
        "樣本比例不一定等於理論機率，樣本數愈大時通常較穩定。解題要分清母體、樣本、事件與樣本空間，並依資料型態選擇平均數、中位數、標準差或機率規則。",
    ],
    ("math", "數據分析"): [
        "數據分析先確認研究問題、母體、樣本、變數型態與資料來源，再選擇合適的表格、圖形和統計量。類別資料適合次數與比例，數值資料還可比較中心、分散與分布形狀。",
        "平均數容易受極端值影響，中位數對偏斜資料較穩健；標準差描述資料相對平均數的分散程度。相關性可呈現共同變動，但不能單獨證明因果，還須檢查混淆變因、抽樣方式與資料品質。",
    ],
    ("english", "Phonics: CVC Words"): [
        "A CVC word has a consonant-vowel-consonant pattern, as in cat, bed, sit, hot, and sun. The vowel in a closed CVC syllable usually has its short sound, although English still has exceptions that must be learned by word.",
        "Readers blend the three phonemes from left to right without inserting an extra vowel: /m/ /a/ /p/ becomes map. Changing one sound builds word families and contrast: map, cap, tap; sit, sat, set.",
    ],
    ("english", "Daily Routines"): [
        "Daily routines are repeated activities such as getting up, eating breakfast, going to school, and doing homework. English normally uses the present simple for these habits, with time phrases such as every day, on weekdays, and at seven o'clock.",
        "The verb agrees with the subject: I walk to school, but Mia walks to school. Frequency adverbs usually come before an ordinary verb and after be: We often read after dinner; He is usually early.",
    ],
    ("english", "Phonics: Consonant Blends"): [
        "A consonant blend contains two or more consonants whose sounds remain audible, as in black, stop, frog, and desk. This differs from a consonant digraph such as sh or ch, where the letters work together to represent one main sound.",
        "Learners should segment and blend each sound in order: /s/ /t/ /ŏ/ /p/ becomes stop. Initial blends include bl, cr, and st; final blends include nd, st, and mp.",
    ],
    ("science", "功與能"): [
        "功與能用來描述力如何改變物體狀態並轉移能量。物體受到力但沒有位移，或力與位移垂直時，該力不作功；功的大小同時取決於力、位移與兩者夾角。",
        "動能與運動狀態有關，位能與物體在力場中的位置或形變有關。只有保守力作功時，動能與位能總和保持不變；摩擦出現時，部分機械能轉成內能，但總能量仍守恆。",
    ],
    ("science", "酸鹼鹽"): [
        "酸鹼鹽的性質要從水溶液中的離子理解。酸在水中增加氫離子濃度，鹼在水中增加氫氧根離子濃度；酸鹼強弱與濃度是不同概念。常溫水溶液可用pH判斷酸鹼性，pH低於7為酸性、高於7為鹼性。",
        "酸與鹼反應可生成鹽和水，稱為中和反應。鹽是由陽離子與陰離子組成的離子化合物，溶於水後的酸鹼性仍取決於離子是否與水反應，不能一律視為中性。",
    ],
    ("biology", "生態系與保育"): [
        "生態系由生物群集與非生物環境組成。能量由生產者進入食物網並在營養階層間逐步散失，水、碳與氮等物質則在生物與環境之間循環。",
        "保育不只保護單一物種，也要維持棲地、族群遺傳多樣性與生態過程。主要威脅包括棲地破壞、過度利用、污染、外來種與氣候變遷，策略需配合威脅來源與長期監測。",
    ],
    ("biology", "生態模型"): [
        "生態模型用簡化的文字、圖形或方程式描述族群與環境的關係。模型會選取重要變因並忽略部分細節，因此預測必須限定在假設與資料範圍內。",
        "指數成長適合資源近乎不受限制的短期情境；邏輯斯成長加入環境負荷量，描述成長率隨族群接近上限而下降。實際族群還會受到年齡結構、遷移、天候與物種交互作用影響。",
    ],
    ("english", "Conjunctions"): [
        "Conjunctions connect words, phrases, or clauses and show how ideas are related. Coordinating conjunctions join elements of equal grammatical status, while subordinating conjunctions introduce dependent clauses of time, reason, condition, contrast, or purpose.",
        "The connector must match the intended logic. Because gives a reason, although marks contrast, if states a condition, and so introduces a result; punctuation changes according to clause order and sentence structure.",
    ],
    ("english", "Junior High Bridge Course"): [
        "The junior high bridge course reviews the sentence system needed before longer reading and writing: subject-verb agreement, be and ordinary verbs, questions, negatives, pronouns, articles, prepositions, and basic tense contrasts.",
        "Students apply these forms in short messages and paragraphs rather than isolated drills. A complete answer should communicate time, participants, action, and place clearly enough for another reader to follow.",
    ],
    ("english", "Grammar Review"): [
        "Grammar review organizes forms by sentence function instead of treating every rule as separate. It checks clause structure, verb tense and aspect, agreement, noun phrases, pronoun reference, modifiers, connectors, and punctuation.",
        "Revision begins with the sentence core: identify the subject and finite verb, then inspect complements and modifiers. A correction is valid only when it preserves the writer's intended meaning and fits the surrounding discourse.",
    ],
    ("english", "Translation Skills"): [
        "Translation conveys meaning, purpose, tone, and information structure rather than replacing each word mechanically. The translator first identifies the sentence core, reference, tense, logical links, and context-specific meaning.",
        "Natural target-language order may differ from the source. After drafting, compare names, numbers, negation, modality, cause and effect, and register to ensure that no information was added, omitted, or reversed.",
    ],
    ("english", "Exam Final Review"): [
        "Final exam review combines vocabulary, grammar, cloze, reading, listening, and writing around recurring weaknesses. Learners classify each error by cause and practise the same concept in a new context instead of memorizing an answer.",
        "During the exam, read the task and units of information first, eliminate choices that violate grammar or passage logic, and reserve time to check unanswered items, pronoun reference, tense consistency, and writing requirements.",
    ],
    ("english", "Mixed Text Analysis"): [
        "Mixed text analysis integrates prose, tables, charts, notices, images, or multiple viewpoints. Each source has its own purpose and evidence, so readers identify the author, audience, date, labels, units, and central claim before combining information.",
        "A conclusion must be supported across sources. Agreement strengthens a claim, while disagreement may come from different definitions, samples, time periods, or perspectives and should not be hidden.",
    ],
    ("english", "Opinion Essay"): [
        "An opinion essay states a clear, arguable position and supports it with relevant reasons and evidence. The introduction frames the issue and thesis; body paragraphs develop one reason at a time; the conclusion explains the significance without merely repeating sentences.",
        "Strong essays address a reasonable counterargument and use transitions to show logic. Examples must support the stated reason, and claims should be limited when the available evidence does not justify a universal conclusion.",
    ],
    ("english", "Presentation English"): [
        "Presentation English helps an audience follow spoken information. An effective talk previews its structure, defines unfamiliar terms, signals transitions, explains visuals, and ends by restating the main finding or request.",
        "Delivery requires intelligible pronunciation, purposeful stress, suitable pace, eye contact, and concise slides. Speakers should cite sources, distinguish evidence from opinion, and answer questions by confirming what was asked before responding.",
    ],
    ("english", "Discourse Markers"): [
        "Discourse markers signal how one sentence or section relates to another. For example introduces evidence, however marks contrast, therefore gives a result, meanwhile shifts time, and in conclusion closes an argument.",
        "Markers do not create logic by themselves. Writers must first establish a real causal, comparative, sequential, or argumentative relation and then choose a marker with the correct meaning and punctuation.",
    ],
    ("english", "Translation Review"): [
        "Translation review checks accuracy and naturalness at sentence and paragraph levels. It verifies participants, tense, modality, negation, quantities, terminology, reference, and logical connections against the source.",
        "A revised translation should read naturally without changing the message. Back-checking difficult phrases and comparing alternative word orders help reveal omissions, additions, ambiguity, and source-language interference.",
    ],
    ("english", "Exam Strategy"): [
        "Exam strategy begins with task recognition: determine whether an item tests grammar, vocabulary, detail, inference, organization, or integrated evidence. Allocate time by section value and difficulty, and mark uncertain answers for a controlled second pass.",
        "Use elimination with explicit reasons. In reading, return to the relevant lines; in cloze, test grammar and discourse; in writing, reserve time for structure, agreement, tense, spelling, and required content.",
    ],
    ("english", "Essay Final Practice"): [
        "Final essay practice rehearses the complete writing process under realistic time limits. Writers analyse the prompt, choose a controlling idea, outline paragraph roles, draft evidence, and revise for coherence and language accuracy.",
        "The final check confirms that every paragraph supports the thesis, examples are specific, transitions express genuine logic, and sentences maintain consistent tense, reference, agreement, punctuation, and register.",
    ],
}


def iter_units(data: Dict[str, Any]) -> Iterator[Tuple[str, Dict[str, Any]]]:
    for subject, books in data.items():
        for book in books if isinstance(books, list) else []:
            for unit in book.get("units", []):
                yield subject, unit


def restore_key_point_candidates(
    data: Dict[str, Any],
    baseline: Dict[str, Any],
) -> int:
    """Restore only key-point candidates from a schema-compatible baseline."""
    restored = 0
    for subject, books in data.items():
        baseline_books = baseline.get(subject, [])
        for book_index, book in enumerate(books):
            if book_index >= len(baseline_books):
                continue
            baseline_units = baseline_books[book_index].get("units", [])
            for unit_index, unit in enumerate(book.get("units", [])):
                if unit_index >= len(baseline_units):
                    continue
                baseline_unit = baseline_units[unit_index]
                if baseline_unit.get("name") != unit.get("name"):
                    continue
                points = (
                    baseline_unit.get("lessonDetails", {}).get("keyPoints", [])
                    or []
                )
                if points:
                    unit.setdefault("lessonDetails", {})["keyPoints"] = points
                    restored += 1
    return restored


def _clean_common_trap(value: Any) -> str:
    text = clean_text(value)
    if any(fragment in text for fragment in TEMPLATE_FRAGMENTS):
        return ""
    return text


def _apply_organized(details: Dict[str, Any], organized: Dict[str, Any]) -> None:
    original_points = {
        clean_text(point.get("topic")): point
        for point in details.get("keyPoints", []) or []
        if isinstance(point, dict)
    }
    paragraphs = organized["paragraphs"]
    details["lessonText"] = list(paragraphs)
    details["readableLesson"] = list(paragraphs)
    details["formulas"] = list(organized["formulas"])
    details["keyPoints"] = [
        {
            "topic": point["topic"],
            "explanation": point["explanation"],
            "example": point["example"],
            "commonTrap": _clean_common_trap(
                original_points.get(point["topic"], {}).get("commonTrap")
            ),
        }
        for point in organized["key_points"]
    ]


def _repair_title_explanation(title: str, organized: Dict[str, Any]) -> None:
    """Move one matching point into prose when legacy prose misses the title."""
    if "title_not_explained" not in quality_issues(title, organized):
        return
    points = organized.get("key_points", [])
    if not points:
        return
    best_index = max(
        range(len(points)),
        key=lambda index: text_similarity(title, points[index].get("topic", "")),
    )
    point = points.pop(best_index)
    organized["paragraphs"] = [
        "%s：%s" % (title, point["explanation"])
    ] + list(organized.get("paragraphs", []))
    organized["paragraphs"] = organized["paragraphs"][:4]
    organized["examples"] = [
        value
        for value in organized.get("examples", [])
        if value != point.get("example")
    ]


def rebuild_data(data: Dict[str, Any]) -> Dict[str, int]:
    counts = {"units": 0, "curated": 0, "reduced": 0}
    for subject, unit in iter_units(data):
        counts["units"] += 1
        details = unit.get("lessonDetails", {}) or {}
        curated = CURATED_UNITS.get((subject, unit.get("name", "")))
        if curated:
            _apply_organized(details, {
                "paragraphs": curated["paragraphs"],
                "formulas": curated["formulas"],
                "key_points": curated["key_points"],
                "examples": [
                    point["example"] for point in curated["key_points"]
                ],
            })
            counts["curated"] += 1
            continue

        before = (
            len(details.get("lessonText", []) or []),
            len(details.get("formulas", []) or []),
            len(details.get("keyPoints", []) or []),
        )
        organized = organize_lesson(details, str(unit.get("name", "")))
        replacement = RELIABLE_PARAGRAPH_REPLACEMENTS.get(
            (subject, str(unit.get("name", "")))
        )
        if replacement:
            organized["paragraphs"] = list(replacement)
        _repair_title_explanation(str(unit.get("name", "")), organized)
        _apply_organized(details, organized)
        after = (
            len(details.get("lessonText", []) or []),
            len(details.get("formulas", []) or []),
            len(details.get("keyPoints", []) or []),
        )
        if after != before:
            counts["reduced"] += 1
    return counts


def audit_data(data: Dict[str, Any]) -> Dict[str, Any]:
    issue_counts: Dict[str, int] = {}
    failed_units: List[str] = []
    for subject, unit in iter_units(data):
        title = str(unit.get("name", ""))
        organized = organize_lesson(unit.get("lessonDetails", {}) or {}, title)
        issues = quality_issues(title, organized)
        if issues:
            failed_units.append("%s/%s" % (subject, title))
        for issue in issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
    return {
        "failed_unit_count": len(failed_units),
        "issue_counts": issue_counts,
        "failed_units": failed_units,
    }


def write_curriculum_js(path: Path, data: Dict[str, Any]) -> None:
    raw = path.read_text(encoding="utf-8")
    start_marker = "  const fullData = "
    end_marker = "\n\n  global.CurriculumLibrary.data = fullData;"
    start = raw.find(start_marker)
    end = raw.find(end_marker)
    if start < 0 or end < 0:
        raise ValueError("找不到 curriculum_integrated.js 的 fullData 邊界。")
    value_start = start + len(start_marker)
    encoded = json.dumps(data, ensure_ascii=False, indent=2) + ";"
    path.write_text(raw[:value_start] + encoded + raw[end:], encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument(
        "--baseline",
        type=Path,
        help="只從相容基準檔恢復 keyPoints 候選，再套用新規則",
    )
    args = parser.parse_args()

    data = load_curriculum_js(args.file)
    restored = 0
    if args.baseline:
        restored = restore_key_point_candidates(
            data,
            load_curriculum_js(args.baseline),
        )
    rebuild_counts = rebuild_data(data)
    report = {
        "restored_key_point_units": restored,
        "rebuild": rebuild_counts,
        "audit": audit_data(data),
    }
    if args.write:
        write_curriculum_js(args.file, data)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
