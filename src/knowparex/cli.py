from __future__ import annotations

import argparse
import json
import re
from .knowledge_service import get_categories, get_items, get_topic_data
from .curriculum_quality import (
    BROAD_CONCEPT_TERMS,
    RECOMMENDATION_STOPWORDS,
    concept_terms,
    normalize_for_compare,
)
from collections import defaultdict
import random
from datetime import date
from pathlib import Path

def print_topic_text(
    category: str,
    item: str,
    *,
    source: str = "knowledge",
) -> None:
    """以適合人閱讀的格式顯示主題資料。"""
    data = get_topic_data(category, item, source=source)

    print()
    print("=" * 55)
    print(f"{category} / {item}")
    print("=" * 55)

    for record in data:
        print(
            f'{record["code_a"]} ({record["language_a"]}) '
            f'=> {record["relation"]} <= '
            f'{record["code_b"]} ({record["language_b"]})'
        )

    print("=" * 55)




def format_record(record: dict) -> str:
    """將一筆知識紀錄轉為適合人閱讀的文字。"""
    return (
        f'{record.get("code_a", "")} '
        f'({record.get("language_a", "")}) '
        f'=> {record.get("relation", "")} <= '
        f'{record.get("code_b", "")} '
        f'({record.get("language_b", "")})'
    )

def get_all_topics() -> list[tuple[str, str]]:
    """取得全部分類與主題。"""
    return [
        (category, item)
        for category in get_categories()
        for item in get_items(category)
    ]
def text_matches(
    keyword: str,
    value: object,
    *,
    exact: bool = False,
) -> bool:
    """判斷文字是否符合搜尋關鍵字。"""
    normalized_value = str(value).casefold()
    normalized_keyword = keyword.casefold()

    if exact:
        # 避免「醇」匹配到「乙醇」或「醇厚」
        pattern = rf"(?<!\w){re.escape(normalized_keyword)}(?!\w)"
        return re.search(pattern, normalized_value) is not None

    return normalized_keyword in normalized_value

def search_main(
    keyword: str,
    *,
    summary_only: bool = False,
    exact: bool = False,
    topic_only: bool = False,
    record_only: bool = False,
    category_filter: str | None = None,
    limit: int | None = None,
    json_output: bool = False,
    count_only: bool = False,
    random_result: bool = False,
    tree_view: bool = False,
    open_topic: bool = False,
    source: str = "knowledge",
) -> None:
    """搜尋分類、主題與知識內容。"""
    original_keyword = keyword.strip()
    normalized_keyword = original_keyword.casefold()

    if not normalized_keyword:
        print("搜尋關鍵字不可為空。")
        return

    if topic_only and record_only:
        print("不能同時使用 --topic-only 與 --record-only。")
        return

    if limit is not None and limit < 1:
        print("--limit 必須大於 0。")
        return
    
    display_modes = [
        count_only,
        random_result,
        tree_view,
        open_topic,
        json_output,
    ]

    if sum(display_modes) > 1:
        print(
            "--count、--random、--tree、--open "
            "與 --json 一次只能使用其中一個。"
        )
        return
    
    all_categories = get_categories(source=source)

    if category_filter is not None:
        matching_categories = [
            category
            for category in all_categories
            if category.casefold() == category_filter.casefold()
        ]

        if not matching_categories:
            print(f'找不到分類：「{category_filter}」')
            return

        categories_to_search = matching_categories
    else:
        categories_to_search = all_categories

    direct_topic_matches: set[tuple[str, str]] = set()
    matched_topics: set[tuple[str, str]] = set()

    grouped_records: dict[
        tuple[str, str],
        list[dict],
    ] = defaultdict(list)

    seen_records: set[tuple] = set()

    for category in categories_to_search:
        category_matches = text_matches(
            original_keyword,
            category,
            exact=exact,
        )

        for item in get_items(category, source=source):
            topic_key = (category, item)

            item_matches = text_matches(
                original_keyword,
                item,
                exact=exact,
            )

            if not record_only and (
                category_matches or item_matches
            ):
                direct_topic_matches.add(topic_key)
                matched_topics.add(topic_key)

            if topic_only:
                continue

            try:
                records = get_topic_data(category, item, source=source)
            except KeyError:
                continue

            for record in records:
                searchable_fields = {
                    "relation": record.get("relation", ""),
                    "code_a": record.get("code_a", ""),
                    "language_a": record.get("language_a", ""),
                    "code_b": record.get("code_b", ""),
                    "language_b": record.get("language_b", ""),
                }

                matched_fields = [
                    field_name
                    for field_name, value in searchable_fields.items()
                    if text_matches(
                        original_keyword,
                        value,
                        exact=exact,
                    )
                ]

                if not matched_fields:
                    continue

                record_key = (
                    category,
                    item,
                    record.get("relation"),
                    record.get("code_a"),
                    record.get("language_a"),
                    record.get("code_b"),
                    record.get("language_b"),
                )

                if record_key in seen_records:
                    continue

                seen_records.add(record_key)
                matched_topics.add(topic_key)

                result_record = dict(record)
                result_record["matched_fields"] = matched_fields

                grouped_records[topic_key].append(result_record)

    if not matched_topics:
        print(f'找不到與「{original_keyword}」相關的內容。')
        return

    def _search_bigrams(value: object) -> set[str]:
        normalized = re.sub(
            r"[^0-9a-z\u4e00-\u9fff]+",
            "",
            str(value).casefold(),
        )
        if len(normalized) < 2:
            return {normalized} if normalized else set()
        return {
            normalized[index:index + 2]
            for index in range(len(normalized) - 1)
        }

    query_bigrams = _search_bigrams(original_keyword)

    def _topic_relevance(topic: tuple[str, str]) -> tuple:
        category, item = topic
        normalized_item = item.casefold().strip()
        item_bigrams = _search_bigrams(item)
        overlap = len(query_bigrams & item_bigrams)
        union = len(query_bigrams | item_bigrams) or 1
        title_similarity = overlap / union
        record_count = len(grouped_records.get(topic, []))

        if normalized_item == normalized_keyword:
            title_score = 1000
        elif normalized_keyword in normalized_item:
            title_score = 850
        elif normalized_item in normalized_keyword:
            title_score = 700
        else:
            title_score = int(title_similarity * 600)

        return (
            -(title_score + min(record_count, 10) * 5),
            topic not in direct_topic_matches,
            category,
            item,
        )

    sorted_topics = sorted(matched_topics, key=_topic_relevance)

    # ``--open`` is for choosing the intended topic, not browsing every unit
    # whose long article happens to contain the query.  When a title-related
    # result exists, hide zero-title-similarity record-only noise.
    if open_topic:
        title_related = []
        for topic in sorted_topics:
            item_bigrams = _search_bigrams(topic[1])
            overlap = len(query_bigrams & item_bigrams)
            union = len(query_bigrams | item_bigrams) or 1
            similarity = overlap / union
            if (
                topic in direct_topic_matches
                or normalized_keyword in topic[1].casefold()
                or similarity >= 0.20
            ):
                title_related.append(topic)
        if title_related:
            sorted_topics = title_related[:20]

    category_topics: dict[str, set[str]] = defaultdict(set)
    category_record_counts: dict[str, int] = defaultdict(int)

    for category, item in sorted_topics:
        category_topics[category].add(item)
        category_record_counts[category] += len(
            grouped_records.get((category, item), [])
        )

    total_records = sum(
        len(records)
        for records in grouped_records.values()
    )
    if count_only:
        print()
        print("=" * 55)
        print(f'搜尋統計：「{original_keyword}」')
        print("=" * 55)
        print(f"涉及分類：{len(category_topics)}")
        print(f"涉及主題：{len(matched_topics)}")
        print(
            "主題名稱直接命中："
            f"{len(direct_topic_matches)}"
        )
        print(f"知識紀錄：{total_records}")

        if category_filter:
            print(f"限制分類：{category_filter}")

        print("=" * 55)
        return
    if random_result:
        available_records = [
            (category, item, record)
            for (category, item), records
            in grouped_records.items()
            for record in records
        ]

        print()
        print("=" * 55)
        print(f'隨機搜尋結果：「{original_keyword}」')
        print("=" * 55)

        if available_records:
            category, item, record = random.choice(
                available_records
            )

            print(f"{category} / {item}")
            print("-" * 55)
            print(format_record(record))

            matched_fields = record.get(
                "matched_fields",
                [],
            )

            if matched_fields:
                print(
                    "匹配欄位："
                    + ", ".join(matched_fields)
                )

        else:
            # 可能只有主題名稱命中，沒有紀錄命中
            category, item = random.choice(
                sorted_topics
            )

            print(f"{category} / {item}")
            print("此結果為主題名稱命中。")

        print("=" * 55)
        return
    if tree_view:
        print()
        print("=" * 55)
        print(f'搜尋樹狀結果：「{original_keyword}」')
        print("=" * 55)

        topics_by_category: dict[
            str,
            list[tuple[str, int, bool]],
        ] = defaultdict(list)

        for category, item in sorted_topics:
            record_count = len(
                grouped_records.get(
                    (category, item),
                    [],
                )
            )

            topics_by_category[category].append(
                (
                    item,
                    record_count,
                    (category, item)
                    in direct_topic_matches,
                )
            )

        categories = sorted(topics_by_category)

        for category_index, category in enumerate(
            categories
        ):
            is_last_category = (
                category_index
                == len(categories) - 1
            )

            category_branch = (
                "└──"
                if is_last_category
                else "├──"
            )

            print(f"{category_branch} {category}")

            topics = topics_by_category[category]

            for topic_index, (
                item,
                record_count,
                direct_match,
            ) in enumerate(topics):
                is_last_topic = (
                    topic_index
                    == len(topics) - 1
                )

                topic_branch = (
                    "    └──"
                    if is_last_topic
                    else "    ├──"
                )

                mark = (
                    " ★"
                    if direct_match
                    else ""
                )

                print(
                    f"{topic_branch} {item}"
                    f"（{record_count} 筆）"
                    f"{mark}"
                )

        print()
        print(
            f"分類：{len(category_topics)}，"
            f"主題：{len(matched_topics)}，"
            f"知識紀錄：{total_records}"
        )
        print("=" * 55)
        return
    if open_topic:
        print()
        print("=" * 55)
        print(f'選擇搜尋主題：「{original_keyword}」')
        print("=" * 55)

        for index, (category, item) in enumerate(
            sorted_topics,
            start=1,
        ):
            record_count = len(
                grouped_records.get(
                    (category, item),
                    [],
                )
            )

            mark = (
                " ★"
                if (category, item)
                in direct_topic_matches
                else ""
            )

            print(
                f"{index}. {category} / {item}"
                f"（{record_count} 筆符合紀錄）"
                f"{mark}"
            )

        print("0. 取消")

        while True:
            choice = input(
                "\n請輸入要開啟的主題編號："
            ).strip()

            if choice == "0":
                print("已取消。")
                return

            try:
                selected_index = int(choice)
            except ValueError:
                print("請輸入有效的數字。")
                continue

            if not (
                1
                <= selected_index
                <= len(sorted_topics)
            ):
                print("編號超出範圍。")
                continue

            category, item = sorted_topics[
                selected_index - 1
            ]

            # 顯示這個主題的全部資料，
            # 不只是符合搜尋字詞的資料。
            #
            # 課程資料必須使用課程文章顯示器，不能把完整顯示路徑
            # 當成一般知識庫主題重新查詢。
            selected_source = (
                "curriculum"
                if (
                    source == "curriculum"
                    or (
                        source == "all"
                        and category.startswith("課程 /")
                    )
                )
                else "knowledge"
            )

            if selected_source == "curriculum":
                from .curriculum_adapter import (
                    get_curriculum_lesson_article,
                )

                article = get_curriculum_lesson_article(
                    category,
                    item,
                )
                recommendations = (
                    get_curriculum_search_recommendations(
                        category,
                        item,
                        article,
                        limit=5,
                    )
                )
                print_curriculum_lesson_article(
                    article,
                    recommendations,
                )
            else:
                print_topic_text(
                    category,
                    item,
                    source="knowledge",
                )

            return
    if json_output:
        output = {
            "keyword": original_keyword,
            "options": {
                "exact": exact,
                "topic_only": topic_only,
                "record_only": record_only,
                "category": category_filter,
                "limit": limit,
            },
            "summary": {
                "category_count": len(category_topics),
                "topic_count": len(matched_topics),
                "direct_topic_match_count": len(
                    direct_topic_matches
                ),
                "record_count": total_records,
            },
            "topics": [],
        }

        shown_count = 0

        for category, item in sorted_topics:
            records = grouped_records.get(
                (category, item),
                [],
            )

            if limit is not None:
                remaining = max(limit - shown_count, 0)
                records = records[:remaining]

            output["topics"].append(
                {
                    "category": category,
                    "item": item,
                    "direct_topic_match": (
                        (category, item)
                        in direct_topic_matches
                    ),
                    "records": records,
                }
            )

            shown_count += len(records)

            if limit is not None and shown_count >= limit:
                break

        print(
            json.dumps(
                output,
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    print()
    print("=" * 55)
    print(f'搜尋結果：「{original_keyword}」')
    print("=" * 55)

    print()
    print("【搜尋摘要】")
    print(f"涉及分類：{len(category_topics)}")
    print(f"涉及主題：{len(matched_topics)}")
    print(
        "主題名稱直接命中："
        f"{len(direct_topic_matches)}"
    )
    print(f"知識紀錄：{total_records}")

    if category_filter:
        print(f"限制分類：{category_filter}")

    if exact:
        print("搜尋模式：完全符合")

    print()
    print("【分類統計】")

    for category in sorted(category_topics):
        print(
            f"- {category}："
            f"{len(category_topics[category])} 個主題，"
            f"{category_record_counts[category]} 筆紀錄"
        )

    print()
    print("【所有符合的主題】")

    for category, item in sorted_topics:
        record_count = len(
            grouped_records.get((category, item), [])
        )

        mark = (
            " ★ 主題名稱命中"
            if (category, item) in direct_topic_matches
            else ""
        )

        print(
            f"- {category} / {item}"
            f"（{record_count} 筆）"
            f"{mark}"
        )

    if summary_only or topic_only:
        print()
        print("=" * 55)
        return

    print()
    print("【詳細知識內容】")

    shown_records = 0
    limit_reached = False

    for category, item in sorted_topics:
        records = grouped_records.get(
            (category, item),
            [],
        )

        if not records:
            continue

        if limit is not None:
            remaining = limit - shown_records

            if remaining <= 0:
                limit_reached = True
                break

            records = records[:remaining]

        print()
        print("=" * 55)
        print(
            f"{category} / {item}"
            f"（{len(records)} 筆顯示）"
        )
        print("=" * 55)

        for record in records:
            print(format_record(record))

            matched_fields = record.get(
                "matched_fields",
                [],
            )

            if matched_fields:
                print(
                    "  匹配欄位："
                    + ", ".join(matched_fields)
                )

            shown_records += 1

        if limit is not None and shown_records >= limit:
            limit_reached = (
                shown_records < total_records
            )
            break

    if limit_reached:
        print()
        print(
            f"只顯示前 {limit} 筆，"
            f"其餘 {total_records - shown_records} 筆已省略。"
        )

    print()
    print("=" * 55)
    print(
        f"分類：{len(category_topics)}，"
        f"主題：{len(matched_topics)}，"
        f"主題名稱命中：{len(direct_topic_matches)}，"
        f"知識紀錄：{total_records}"
    )

def stats_main() -> None:
    """顯示整個 KnowpareX 資料庫統計。"""
    categories = get_categories()

    topic_count = 0
    record_count = 0
    relation_counts: dict[str, int] = defaultdict(int)
    category_counts: list[tuple[str, int, int]] = []

    largest_topic: tuple[str, str, int] | None = None

    for category in categories:
        items = get_items(category)
        category_record_count = 0
        topic_count += len(items)

        for item in items:
            try:
                records = get_topic_data(category, item)
            except KeyError:
                continue

            current_count = len(records)
            record_count += current_count
            category_record_count += current_count

            if largest_topic is None or current_count > largest_topic[2]:
                largest_topic = (
                    category,
                    item,
                    current_count,
                )

            for record in records:
                relation = str(
                    record.get("relation", "未知關係")
                )
                relation_counts[relation] += 1

        category_counts.append(
            (
                category,
                len(items),
                category_record_count,
            )
        )

    average = (
        record_count / topic_count
        if topic_count
        else 0
    )

    print()
    print("=" * 55)
    print("KnowpareX 資料庫統計")
    print("=" * 55)
    print(f"分類數：{len(categories)}")
    print(f"主題數：{topic_count}")
    print(f"知識紀錄數：{record_count}")
    print(f"平均每個主題：{average:.2f} 筆")

    if largest_topic is not None:
        category, item, count = largest_topic
        print(
            f"最大主題：{category} / {item}"
            f"（{count} 筆）"
        )

    print()
    print("【各分類統計】")

    for category, items, records in sorted(
        category_counts,
        key=lambda value: value[2],
        reverse=True,
    ):
        print(
            f"- {category}："
            f"{items} 個主題，"
            f"{records} 筆紀錄"
        )

    print()
    print("【常見關係】")

    for relation, count in sorted(
        relation_counts.items(),
        key=lambda value: value[1],
        reverse=True,
    )[:15]:
        print(f"- {relation}：{count}")

    print("=" * 55)

def today_main() -> None:
    """顯示今日推薦知識。"""
    topics = get_all_topics()

    if not topics:
        print("目前沒有可推薦的主題。")
        return

    today = date.today()

    # 使用日期數字作為種子，同一天結果固定
    generator = random.Random(today.toordinal())
    category, item = generator.choice(topics)

    print()
    print("=" * 55)
    print(f"今日知識推薦：{today.isoformat()}")
    print("=" * 55)
    print_topic_text(category, item)
from typing import Iterable

def collect_all_records() -> list[dict]:
    """收集資料庫中的所有知識紀錄，並補上分類與主題名稱。"""
    all_records: list[dict] = []

    for category in get_categories():
        for item in get_items(category):
            try:
                records = get_topic_data(category, item)
            except KeyError:
                continue

            for record in records:
                scan_record = dict(record)
                scan_record["category"] = category
                scan_record["topic"] = item
                all_records.append(scan_record)

    return all_records
def _normalize_scan_text(value: object) -> str:
    """將值轉成適合比對的文字。"""
    if value is None:
        return ""

    return str(value).strip()

SCAN_IGNORED_CONCEPTS = {
    "已知", "未知", "判斷", "說明", "敘述", "問題", "結果",
    "答案", "原因", "表示", "比較", "之後", "之前", "產生",
    "形成", "進行", "發生", "活動", "環境", "影響", "增加",
    "減少", "降低", "提高", "主要", "一般", "通常", "可能",
    "容易", "可以", "利用", "使用", "根據", "依照", "下列",
    "上述", "其中", "因此", "所以", "因為", "以及", "並且",
    "同時", "另外", "正確", "錯誤", "是否", "屬於", "請問",
    "求出", "合理", "較高", "較低", "沒有", "不是", "不一定",
    "不代表", "介紹",
}


SCAN_PREFIXES = (
    "進行",
    "利用",
    "透過",
    "藉由",
    "經由",
    "使用",
    "採用",
    "具有",
    "屬於",
    "可",
    "可以",
    "可能",
    "容易",
    "主要",
)

SCAN_SUFFIXES = (
    "增加",
    "減少",
    "降低",
    "提高",
    "形成",
    "產生",
    "發生",
    "改變",
    "作用",
    "現象",
    "功能",
    "用途",
    "原因",
    "方法",
    "過程",
)

def _normalize_scan_concept(concept: str) -> str:
    """將候選概念做正規化，避免把整句當概念。"""

    concept = concept.strip()

    changed = True
    while changed:
        changed = False

        for prefix in SCAN_PREFIXES:
            if concept.startswith(prefix) and len(concept) > len(prefix) + 1:
                concept = concept[len(prefix):].strip()
                changed = True

        for suffix in SCAN_SUFFIXES:
            if concept.endswith(suffix) and len(concept) > len(suffix) + 1:
                concept = concept[:-len(suffix)].strip()
                changed = True

    return concept
def collect_scan_topics(
    *,
    source: str = "knowledge",
) -> list[dict]:
    """整理所有主題及其可供掃描比對的關鍵詞。"""
    scan_topics: list[dict] = []

    for category in get_categories(source=source):
        for item in get_items(category, source=source):
            try:
                records = get_topic_data(category, item, source=source)
            except KeyError:
                continue

            terms: set[str] = set()

            normalized_item = _normalize_scan_concept(
                _normalize_scan_text(item)
            )

            if normalized_item:
                terms.add(normalized_item)

            for record in records:
                for field in ("code_a", "code_b"):
                    term = _normalize_scan_text(
                        record.get(field)
                    )
                    term = _normalize_scan_concept(term)

                    if not term:
                        continue

                    terms.add(term)

            scan_topics.append(
                {
                    "category": category,
                    "item": item,
                    "terms": terms,
                }
            )

    return scan_topics
def scan_text_for_topics(
    text: str,
    scan_topics: list[dict],
    *,
    minimum_length: int = 2,
) -> list[dict]:
    """掃描文字並回傳命中的知識主題。"""
    original_text = text.strip()
    normalized_text = original_text.casefold()

    if not normalized_text:
        return []

    matched_topics: list[dict] = []

    for topic in scan_topics:
        matched_terms: list[str] = []

        for raw_term in topic["terms"]:
            term = _normalize_scan_concept(
                _normalize_scan_text(raw_term)
            )

            if len(term) < minimum_length:
                continue

            if term in SCAN_IGNORED_CONCEPTS:
                continue

            if term.casefold() in normalized_text:
                matched_terms.append(term)

        if not matched_terms:
            continue

        unique_terms = sorted(
            set(matched_terms),
            key=lambda value: (
                -len(value),
                value,
            ),
        )

        matched_topics.append(
            {
                "category": topic["category"],
                "item": topic["item"],
                "matched_terms": unique_terms,
                "score": sum(
                    len(term)
                    for term in unique_terms
                ),
            }
        )

    matched_topics.sort(
        key=lambda topic: (
            -topic["score"],
            -len(topic["matched_terms"]),
            topic["category"],
            topic["item"],
        )
    )

    return matched_topics

def print_scan_topic_result(
    text: str,
    matched_topics: list[dict],
    *,
    as_json: bool = False,
) -> None:
    """顯示文字掃描命中的主題。"""
    if as_json:
        print(
            json.dumps(
                {
                    "text": text,
                    "topic_count": len(matched_topics),
                    "topics": [
                        {
                            "category": topic["category"],
                            "item": topic["item"],
                            "matched_terms": (
                                topic["matched_terms"]
                            ),
                        }
                        for topic in matched_topics
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    print()
    print("=" * 55)
    print("文字主題掃描")
    print("=" * 55)
    print(f"輸入文字：{text}")
    print()

    if not matched_topics:
        print("找不到與這段文字相關的知識主題。")
        print("=" * 55)
        return

    print("【命中的主題】")

    for index, topic in enumerate(
        matched_topics,
        start=1,
    ):
        matched_preview = "、".join(
            topic["matched_terms"][:4]
        )

        print(
            f"{index}. "
            f'{topic["category"]} / {topic["item"]}'
        )

        if matched_preview:
            print(f"   命中內容：{matched_preview}")

    print()
    print(f"主題數量：{len(matched_topics)}")
    print("=" * 55)

def interactive_scan_main(
    *,
    minimum_length: int = 2,
    source: str = "knowledge",
) -> None:
    """重複掃描文字，並允許直接開啟命中的主題。"""
    scan_topics = collect_scan_topics(source=source)

    exit_commands = {
        "0",
        "q",
        "quit",
        "exit",
        "結束",
        "離開",
        "不要查了",
    }

    print()
    print("=" * 55)
    print("KnowpareX 互動式主題掃描")
    print("=" * 55)
    print("輸入一段文字，系統會找出相關知識主題。")
    print("輸入 0、q、quit、exit、結束或離開即可停止。")
    print("=" * 55)

    while True:
        try:
            text = input(
                "\n請輸入要掃描的文字（輸入 0 結束）："
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已結束主題掃描。")
            return

        if text.casefold() in exit_commands:
            print("已結束主題掃描。")
            return

        if not text:
            print("請輸入文字，不可以空白。")
            continue

        matched_topics = scan_text_for_topics(
            text,
            scan_topics,
            minimum_length=minimum_length,
        )

        print_scan_topic_result(
            text,
            matched_topics,
            as_json=False,
        )

        if not matched_topics:
            continue

        while True:
            choice = input(
                "\n要開啟其中的主題嗎？\n"
                "輸入編號，或按 Enter 繼續掃描："
            ).strip()

            if choice == "":
                break

            if choice.casefold() in exit_commands:
                print("已結束主題掃描。")
                return

            try:
                selected_index = int(choice)
            except ValueError:
                print("請輸入有效編號，或直接按 Enter。")
                continue

            if not 1 <= selected_index <= len(
                matched_topics
            ):
                print("編號超出範圍。")
                continue

            selected_topic = matched_topics[
                selected_index - 1
            ]

            print_topic_text(
                selected_topic["category"],
                selected_topic["item"],
                source=source,
            )

            again = input(
                "\n還要開啟其他命中的主題嗎？\n"
                "輸入 y 繼續，其他內容返回掃描："
            ).strip().casefold()

            if again in {"y", "yes", "是", "要"}:
                print("\n【命中的主題】")

                for index, topic in enumerate(
                    matched_topics,
                    start=1,
                ):
                    print(
                        f"{index}. "
                        f'{topic["category"]} / '
                        f'{topic["item"]}'
                    )

                continue

            break

def scan_main(
    text: str | None,
    *,
    minimum_length: int = 2,
    json_output: bool = False,
    source: str = "knowledge",
) -> None:
    """執行單次主題掃描，或進入互動模式。"""
    if minimum_length < 1:
        print("--min-length 必須大於 0。")
        return

    if text is None:
        if json_output:
            print("--json 必須搭配一段要掃描的文字。")
            return

        interactive_scan_main(
            minimum_length=minimum_length,
            source=source,
        )
        return

    scan_topics = collect_scan_topics(source=source)

    matched_topics = scan_text_for_topics(
        text,
        scan_topics,
        minimum_length=minimum_length,
    )

    print_scan_topic_result(
        text,
        matched_topics,
        as_json=json_output,
    )


def record_to_sentence(record: dict) -> str:
    """將一筆關係資料轉成自然語句。"""
    relation = str(record.get("relation", "")).strip()
    code_a = str(record.get("code_a", "")).strip()
    language_a = str(
        record.get("language_a", "")
    ).strip()
    code_b = str(record.get("code_b", "")).strip()
    language_b = str(
        record.get("language_b", "")
    ).strip()

    left = (
        f"{code_a}（{language_a}）"
        if language_a
        else code_a
    )

    right = (
        f"{code_b}（{language_b}）"
        if language_b
        else code_b
    )

    relation_sentences = {
        "=": f"{left}是{right}。",
        "!=": f"{left}並不是{right}。",
        "等價於": f"{left}可理解為{right}。",
        "定義為": f"{left}定義為{right}。",
        "造成": f"{left}會造成{right}。",
        "導致": f"{left}會導致{right}。",
        "需要": f"{left}需要{right}。",
        "與……相關": f"{left}與{right}相關。",
        "翻譯為": f"{left}可翻譯為{right}。",
        "計算方式": f"{left}的計算方式是{right}。",
        ">": f"{left}大於{right}。",
        "<": f"{left}小於{right}。",
        ">=": f"{left}大於或等於{right}。",
        "<=": f"{left}小於或等於{right}。",
        "≈": f"{left}約等於{right}。",
    }

    return relation_sentences.get(
        relation,
        f"{left}與{right}的關係是「{relation}」。",
    )


def explain_main(category: str, item: str) -> None:
    """以較自然的文字解釋一個主題。"""
    records = get_topic_data(category, item)

    print()
    print("=" * 55)
    print(f"{category} / {item}－文字解釋")
    print("=" * 55)

    for record in records:
        print(record_to_sentence(record))

    print("=" * 55)

def topic_to_markdown(
    category: str,
    item: str,
    records: list[dict],
) -> str:
    """將主題轉成 Markdown。"""
    lines = [
        f"# {category} / {item}",
        "",
    ]

    for record in records:
        lines.append(
            f"- {format_record(record)}"
        )

    lines.append("")
    return "\n".join(lines)


def topic_to_text(
    category: str,
    item: str,
    records: list[dict],
) -> str:
    """將主題轉成純文字。"""
    lines = [
        "=" * 55,
        f"{category} / {item}",
        "=" * 55,
    ]

    lines.extend(
        format_record(record)
        for record in records
    )

    lines.append("=" * 55)
    return "\n".join(lines) + "\n"


def export_main(
    category: str,
    item: str,
    *,
    export_format: str,
    output: str | None,
) -> None:
    """匯出指定主題。"""
    records = get_topic_data(category, item)

    extensions = {
        "txt": ".txt",
        "md": ".md",
        "json": ".json",
    }

    if output:
        output_path = Path(output)
    else:
        safe_category = category.replace("/", "_")
        safe_item = item.replace("/", "_")

        output_path = Path(
            f"{safe_category}_{safe_item}"
            f"{extensions[export_format]}"
        )

    if export_format == "json":
        content = json.dumps(
            {
                "category": category,
                "item": item,
                "records": records,
            },
            ensure_ascii=False,
            indent=2,
        )
    elif export_format == "md":
        content = topic_to_markdown(
            category,
            item,
            records,
        )
    else:
        content = topic_to_text(
            category,
            item,
            records,
        )

    output_path.write_text(
        content,
        encoding="utf-8",
    )

    print(
        "匯出完成："
        f"{output_path.resolve()}"
    )

def collect_topic_terms(
    item: str,
    records: list[dict],
) -> set[str]:
    """取得適合拿來尋找相關主題的詞。"""
    terms = {item.strip()}

    for record in records:
        for field in (
            "code_a",
            "code_b",
        ):
            value = str(
                record.get(field, "")
            ).strip()

            if 2 <= len(value) <= 20:
                terms.add(value)

    return {
        term
        for term in terms
        if term
    }


def related_main(
    category: str,
    item: str,
    *,
    limit: int = 10,
) -> None:
    """尋找與指定主題相關的其他主題。"""
    source_records = get_topic_data(
        category,
        item,
    )
    terms = collect_topic_terms(
        item,
        source_records,
    )

    candidates: list[
        tuple[int, bool, str, str, list[str]]
    ] = []

    for other_category in get_categories():
        for other_item in get_items(other_category):
            if (
                other_category == category
                and other_item == item
            ):
                continue

            try:
                records = get_topic_data(
                    other_category,
                    other_item,
                )
            except KeyError:
                continue

            searchable_text = " ".join(
                str(record.get(field, ""))
                for record in records
                for field in (
                    "relation",
                    "code_a",
                    "language_a",
                    "code_b",
                    "language_b",
                )
            ).casefold()

            matched_terms = sorted(
                term
                for term in terms
                if term.casefold()
                in searchable_text
            )

            if not matched_terms:
                continue

            same_category = (
                other_category == category
            )

            score = len(matched_terms)

            # 同分類稍微優先
            if same_category:
                score += 2

            candidates.append(
                (
                    score,
                    same_category,
                    other_category,
                    other_item,
                    matched_terms,
                )
            )

    candidates.sort(
        key=lambda value: (
            -value[0],
            not value[1],
            value[2],
            value[3],
        )
    )

    print()
    print("=" * 55)
    print(f"相關主題：{category} / {item}")
    print("=" * 55)

    if not candidates:
        print("目前找不到相關主題。")
        print("=" * 55)
        return

    for (
        score,
        same_category,
        other_category,
        other_item,
        matched_terms,
    ) in candidates[:limit]:
        category_mark = (
            "同分類"
            if same_category
            else "跨分類"
        )

        preview_terms = "、".join(
            matched_terms[:3]
        )

        print(
            f"- {other_category} / {other_item}"
            f"｜{category_mark}"
            f"｜關聯分數：{score}"
        )
        print(f"  共同內容：{preview_terms}")

    print("=" * 55)

def curriculum_subjects_main() -> None:
    """列出課程資料中的科目。"""
    from .curriculum_adapter import get_subjects

    for subject in get_subjects():
        print(f'{subject["key"]}\t{subject["name"]}')


def curriculum_books_main(
    subject: str,
    *,
    stage: str | None = None,
) -> None:
    """列出指定科目的冊別。"""
    from .curriculum_adapter import get_books

    books = get_books(subject, stage=stage)

    if not books:
        print("找不到符合條件的冊別。")
        return

    for book in books:
        print(
            f'{book["stage"]}\t'
            f'{book["subject"]}\t'
            f'{book["book"]}'
        )


def curriculum_units_main(
    subject: str,
    book: str,
    *,
    stage: str | None = None,
) -> None:
    """列出指定冊別中的單元。"""
    from .curriculum_adapter import get_units

    units = get_units(subject, book, stage=stage)

    if not units:
        print("找不到符合條件的單元。")
        return

    for unit in units:
        print(unit["unit"])




CURRICULUM_RECOMMENDATION_IGNORED_TERMS = RECOMMENDATION_STOPWORDS


def _recommendation_terms(article: dict) -> list[tuple[str, int, str]]:
    """Return (term, weight, origin) without generic prose words."""
    values: list[tuple[str, int, str]] = []

    title = str(article.get("title", "")).strip()
    if title:
        values.append((title, 16, "title"))

    for point in article.get("key_points", []) or []:
        topic = str(point.get("topic", "")).strip()
        if topic:
            values.append((topic, 12, "key_point"))

    for formula in article.get("formulas", []) or []:
        formula_text = str(formula).strip()
        if not formula_text:
            continue

        # A formula label before the colon is intentional metadata.  Words
        # occurring later may only be connective prose and are not candidates.
        label = re.split(r"[：:]", formula_text, maxsplit=1)[0].strip()
        if 2 <= len(label) <= 16 and re.search(r"[\u4e00-\u9fff]", label):
            values.append((label, 7, "formula"))

    terms: list[tuple[str, int, str]] = []
    seen: set[str] = set()

    for value, weight, origin in values:
        normalized = value.casefold().strip()

        if (
            len(normalized) < 2
            or normalized in CURRICULUM_RECOMMENDATION_IGNORED_TERMS
            or normalized in BROAD_CONCEPT_TERMS
            or normalized in seen
        ):
            continue

        seen.add(normalized)
        terms.append((value.strip(), weight, origin))

    return terms


def _topic_search_concepts(
    category: str,
    item: str,
    records: list[dict],
) -> set[str]:
    """Build concepts from names and compact records, never full lesson prose."""
    values = [category, item, item.rsplit("/", 1)[-1].strip()]

    for record in records:
        language_a = str(record.get("language_a", ""))
        language_b = str(record.get("language_b", ""))
        for field, language in (
            ("code_a", language_a),
            ("code_b", language_b),
        ):
            value = str(record.get(field, "")).strip()
            if not value or language in {"課文", "解釋", "例子"}:
                continue
            if len(value) <= 48:
                values.append(value)
            elif language == "公式或規則":
                values.extend(re.findall(r"[\u4e00-\u9fff]{2,12}", value))

    concepts: set[str] = set()
    for value in values:
        normalized = normalize_for_compare(value)
        if (
            len(normalized) >= 2
            and normalized not in RECOMMENDATION_STOPWORDS
            and normalized not in BROAD_CONCEPT_TERMS
        ):
            concepts.add(normalized)
        concepts.update(
            normalize_for_compare(term)
            for term in concept_terms(value)
            if term not in RECOMMENDATION_STOPWORDS
            and term not in BROAD_CONCEPT_TERMS
        )
    return {value for value in concepts if len(value) >= 2}


def get_curriculum_search_recommendations(
    current_category: str,
    current_item: str,
    article: dict,
    *,
    limit: int = 5,
) -> list[dict]:
    """
    根據課程名稱、重點知識與公式概念，推薦其他可搜尋主題。

    同時搜尋原本知識庫與課程資料，排除目前課程及重複結果。
    """
    terms = _recommendation_terms(article)
    if not terms:
        return []

    candidates: list[dict] = []
    seen_topics: set[tuple[str, str, str]] = set()

    current_subject = current_category.rsplit("/", 1)[-1].strip().casefold()
    current_book = current_item.rsplit("/", 1)[0].strip().casefold()
    current_basename = normalize_for_compare(
        current_item.rsplit("/", 1)[-1].strip()
    )

    for source in ("knowledge", "curriculum"):
        try:
            categories = get_categories(source=source)
        except (KeyError, ValueError):
            continue

        for category in categories:
            try:
                items = get_items(category, source=source)
            except KeyError:
                continue

            for item in items:
                if (
                    source == "curriculum"
                    and category == current_category
                    and item == current_item
                ):
                    continue

                unique_key = (source, category, item)
                if unique_key in seen_topics:
                    continue
                seen_topics.add(unique_key)

                try:
                    records = get_topic_data(
                        category,
                        item,
                        source=source,
                    )
                except (KeyError, ValueError):
                    continue

                candidate_concepts = _topic_search_concepts(
                    category,
                    item,
                    records,
                )
                item_text = normalize_for_compare(item)
                basename = normalize_for_compare(
                    item.rsplit("/", 1)[-1].strip()
                )
                if basename == current_basename:
                    continue
                candidate_subject = category.rsplit(
                    "/", 1
                )[-1].strip().casefold()
                candidate_book = item.rsplit(
                    "/", 1
                )[0].strip().casefold()

                matched_terms: list[str] = []
                score = 0

                for term, weight, origin in terms:
                    normalized = normalize_for_compare(term)

                    if basename == normalized:
                        score += weight + 4
                        matched_terms.append(term)
                    elif len(normalized) >= 3 and normalized in basename:
                        score += weight
                        matched_terms.append(term)
                    elif len(basename) >= 3 and basename in normalized:
                        score += max(4, weight - 4)
                        matched_terms.append(term)
                    elif normalized in candidate_concepts:
                        score += weight
                        matched_terms.append(term)
                    elif origin != "formula" and normalized in item_text:
                        score += max(4, weight - 5)
                        matched_terms.append(term)

                if not matched_terms:
                    continue

                if (
                    source == "curriculum"
                    and category == current_category
                ):
                    score += 4
                    if candidate_book == current_book:
                        score += 3

                if candidate_subject != current_subject:
                    score -= 6

                # A candidate must have a strong concept match after penalties;
                # one accidental broad word is never enough.
                if score < 7:
                    continue

                candidates.append({
                    "score": score,
                    "source": source,
                    "category": category,
                    "item": item,
                    "matched_terms": list(dict.fromkeys(matched_terms)),
                })

    candidates.sort(
        key=lambda value: (
            -value["score"],
            0 if value["source"] == "knowledge" else 1,
            value["category"],
            value["item"],
        )
    )

    results: list[dict] = []
    used_display_names: set[str] = set()

    for candidate in candidates:
        display_name = candidate["item"].rsplit("/", 1)[-1].strip()

        # 同名結果只保留分數最高的一筆，避免推薦清單重複。
        normalized_name = display_name.casefold()
        if normalized_name in used_display_names:
            continue

        used_display_names.add(normalized_name)
        candidate["display_name"] = display_name
        results.append(candidate)

        if len(results) >= limit:
            break

    return results


def print_curriculum_search_recommendations(
    recommendations: list[dict],
) -> None:
    """顯示課程文章後的推薦搜尋。"""
    if not recommendations:
        return

    print("【推薦搜尋】")
    print()

    for index, recommendation in enumerate(
        recommendations,
        start=1,
    ):
        display_name = recommendation["display_name"]
        source = recommendation["source"]
        category = recommendation["category"]
        item = recommendation["item"]
        matched_terms = "、".join(
            recommendation["matched_terms"][:3]
        )

        source_name = (
            "知識庫"
            if source == "knowledge"
            else "課程"
        )

        print(f"{index}. {display_name}")
        print(f"   來源：{source_name}")
        print(f"   位置：{category} / {item}")

        if matched_terms:
            print(f"   相關概念：{matched_terms}")

        print(
            f'   搜尋：knowparex search "{display_name}" '
            f'--source {source}'
        )
        print()


def print_curriculum_lesson_article(
    article: dict,
    recommendations: list[dict] | None = None,
) -> None:
    """以接近課本文章的格式顯示課程內容。"""
    title = str(article.get("title", "")).strip()
    stage = str(article.get("stage", "")).strip()
    subject = str(article.get("subject", "")).strip()
    book = str(article.get("book", "")).strip()

    print()
    print("=" * 55)
    print(title)
    print("=" * 55)

    location = " / ".join(
        value
        for value in (stage, subject, book)
        if value
    )
    if location:
        print(location)
        print()

    paragraphs = article.get("paragraphs", []) or []
    formulas = article.get("formulas", []) or []
    key_points = article.get("key_points", []) or []
    examples = article.get("examples", []) or []

    for paragraph in paragraphs:
        text = str(paragraph).strip()
        if text:
            print(text)
            print()

    if key_points:
        print("【重點知識】")
        print()

        for index, point in enumerate(key_points, start=1):
            topic = str(point.get("topic", "")).strip()
            explanation = str(
                point.get("explanation", "")
            ).strip()
            heading = topic or f"重點 {index}"
            print(f"{index}. {heading}")

            if explanation:
                print(explanation)

            print()

    if formulas:
        print("【公式與規則】")
        print()

        for formula in formulas:
            text = str(formula).strip()
            if text:
                print(f"- {text}")

        print()

    if examples:
        print("【例子】")
        print()

        for example in examples:
            text = str(example).strip()
            if text:
                print(f"- {text}")

        print()

    if not paragraphs and not key_points and not formulas and not examples:
        print("這個單元目前沒有可顯示的教材內容。")
        print()

    print_curriculum_search_recommendations(
        recommendations or [],
    )

    print("=" * 55)


def curriculum_lesson_main(
    subject: str,
    book: str,
    unit: str,
    *,
    stage: str | None = None,
) -> None:
    """以課本文章格式顯示一個課程單元。"""
    from .curriculum_adapter import (
        find_curriculum_topic,
        get_curriculum_lesson_article,
    )

    category, item = find_curriculum_topic(
        subject,
        book,
        unit,
        stage=stage,
    )

    article = get_curriculum_lesson_article(
        category,
        item,
    )
    recommendations = get_curriculum_search_recommendations(
        category,
        item,
        article,
        limit=5,
    )
    print_curriculum_lesson_article(
        article,
        recommendations,
    )


def compare_main() -> None:
    print("=" * 55)
    print("KnowpareX / Steve 知識資料庫")
    print("=" * 55)

    while True:
        print("\n所有分類：")
        for category in get_categories():
            print(category)

        category = input("請輸入分類（0 結束）：").strip()
        if category == "0":
            return

        try:
            items = get_items(category)
        except KeyError as error:
            print(error)
            continue

        print(f"\n{category}：")
        for item in items:
            print(item)

        item = input("請輸入項目（back 返回）：").strip()
        if item.lower() == "back":
            continue

        try:
            print_topic_text(category, item)
        except KeyError as error:
            print(error)


def practice_main() -> None:
    from .tools.practice import main

    main()


def review_main() -> None:
    from .tools.review import main

    main()


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="knowparex",
        description="KnowpareX command-line tools",
    )

    subparsers = parser.add_subparsers(dest="command")

    curriculum_parser = subparsers.add_parser(
        "curriculum",
        help="瀏覽 MindLeapX 課程資料",
    )
    curriculum_subparsers = curriculum_parser.add_subparsers(
        dest="curriculum_command",
        required=True,
    )

    curriculum_subparsers.add_parser(
        "subjects",
        help="列出全部課程科目",
    )

    books_parser = curriculum_subparsers.add_parser(
        "books",
        help="列出指定科目的冊別",
    )
    books_parser.add_argument("subject", help="科目，例如 math、數學")
    books_parser.add_argument(
        "--stage",
        "--category",
        dest="stage",
        help="可選學制：國小、國中、高中",
    )

    units_parser = curriculum_subparsers.add_parser(
        "units",
        help="列出指定冊別的單元",
    )
    units_parser.add_argument("subject", help="科目，例如 math、數學")
    units_parser.add_argument("book", help="冊別，例如 高一上")
    units_parser.add_argument(
        "--stage",
        "--category",
        dest="stage",
        help="可選學制：國小、國中、高中",
    )

    lesson_parser = curriculum_subparsers.add_parser(
        "lesson",
        help="顯示指定單元教材",
    )
    lesson_parser.add_argument("subject", help="科目，例如 math、數學")
    lesson_parser.add_argument("book", help="冊別，例如 高一上")
    lesson_parser.add_argument("unit", help="單元，例如 函數")
    lesson_parser.add_argument(
        "--stage",
        "--category",
        dest="stage",
        help="可選學制：國小、國中、高中",
    )


    subparsers.add_parser(
        "compare",
        help="互動式查詢與比較",
    )

    subparsers.add_parser(
        "practice",
        help="開始練習或測驗",
    )

    subparsers.add_parser(
        "review",
        help="複習已儲存的錯題",
    )

    subparsers.add_parser(
        "categories",
        help="顯示全部分類",
    )

    items_parser = subparsers.add_parser(
        "items",
        help="顯示指定分類中的項目",
    )
    items_parser.add_argument(
        "category",
        help="分類名稱",
    )

    topic_parser = subparsers.add_parser(
        "topic",
        help="顯示一個主題",
    )
    search_parser = subparsers.add_parser(
        "search",
        help="搜尋分類、主題與知識內容",
    )

    search_parser.add_argument(
        "keyword",
        help="搜尋關鍵字",
    )
    search_parser.add_argument(
        "--source",
        choices=("knowledge", "curriculum", "all"),
        default="knowledge",
        help="資料來源；預設只搜尋原本知識庫",
    )

    search_parser.add_argument(
        "--summary",
        action="store_true",
        help="只顯示摘要與符合主題",
    )

    search_parser.add_argument(
        "--exact",
        action="store_true",
        help="只匹配完整欄位內容",
    )

    search_parser.add_argument(
        "--topic-only",
        action="store_true",
        help="只搜尋分類與主題名稱",
    )

    search_parser.add_argument(
        "--record-only",
        action="store_true",
        help="只搜尋知識紀錄",
    )

    search_parser.add_argument(
        "--category",
        help="只搜尋指定分類",
    )
    subparsers.add_parser(
        "stats",
        help="顯示資料庫統計",
    )

    subparsers.add_parser(
        "today",
        help="顯示今日推薦知識",
    )

    explain_parser = subparsers.add_parser(
        "explain",
        help="以自然文字解釋一個主題",
    )
    explain_parser.add_argument(
        "category",
        help="分類名稱",
    )
    explain_parser.add_argument(
        "item",
        help="主題名稱",
    )

    export_parser = subparsers.add_parser(
        "export",
        help="將一個主題匯出成檔案",
    )
    export_parser.add_argument(
        "category",
        help="分類名稱",
    )
    export_parser.add_argument(
        "item",
        help="主題名稱",
    )
    export_parser.add_argument(
        "--format",
        choices=("txt", "md", "json"),
        default="md",
        dest="export_format",
        help="匯出格式，預設為 md",
    )
    export_parser.add_argument(
        "--output",
        help="自訂輸出檔案名稱",
    )

    related_parser = subparsers.add_parser(
        "related",
        help="顯示與指定主題相關的其他主題",
    )
    related_parser.add_argument(
        "category",
        help="分類名稱",
    )
    related_parser.add_argument(
        "item",
        help="主題名稱",
    )
    related_parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="限制相關主題數量，預設為 10",
    )
    search_parser.add_argument(
        "--limit",
        type=int,
        help="限制詳細紀錄顯示數量",
    )
    
    search_parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式輸出搜尋結果",
    )
    topic_parser.add_argument(
        "category",
        help="分類名稱",
    )
    topic_parser.add_argument(
        "item",
        help="項目名稱",
    )
    topic_parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式顯示",
    )
    search_parser.add_argument(
        "--count",
        action="store_true",
        help="只顯示搜尋結果統計",
    )

    search_parser.add_argument(
        "--random",
        action="store_true",
        dest="random_result",
        help="隨機顯示一筆符合的知識紀錄",
    )
    scan_parser = subparsers.add_parser(
        "scan",
        help="掃描一段文字並列出其中命中的知識概念",
    )

    scan_parser.add_argument(
        "text",
        nargs="?",
        help="要掃描的文字；省略時進入互動模式",
    )
    scan_parser.add_argument(
        "--source",
        choices=("knowledge", "curriculum", "all"),
        default="knowledge",
        help="資料來源；預設只掃描原本知識庫",
    )

    scan_parser.add_argument(
        "--min-length",
        type=int,
        default=2,
        help="概念最少字元數，預設為 2",
    )

    scan_parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式輸出",
    )
    search_parser.add_argument(
        "--tree",
        action="store_true",
        help="以分類與主題樹狀結構顯示結果",
    )

    search_parser.add_argument(
        "--open",
        action="store_true",
        dest="open_topic",
        help="從搜尋結果中選擇並開啟完整主題",
    )
    args = parser.parse_args()

    try:
        if args.command == "curriculum":
            if args.curriculum_command == "subjects":
                curriculum_subjects_main()
            elif args.curriculum_command == "books":
                curriculum_books_main(
                    args.subject,
                    stage=args.stage,
                )
            elif args.curriculum_command == "units":
                curriculum_units_main(
                    args.subject,
                    args.book,
                    stage=args.stage,
                )
            elif args.curriculum_command == "lesson":
                curriculum_lesson_main(
                    args.subject,
                    args.book,
                    args.unit,
                    stage=args.stage,
                )

        elif args.command is None or args.command == "compare":
            compare_main()

        elif args.command == "practice":
            practice_main()

        elif args.command == "review":
            review_main()

        elif args.command == "categories":
            print("\n".join(get_categories()))

        elif args.command == "items":
            print("\n".join(get_items(args.category)))
        elif args.command == "stats":
            stats_main()

        elif args.command == "today":
            today_main()

        elif args.command == "explain":
            explain_main(
                args.category,
                args.item,
            )

        elif args.command == "export":
            export_main(
                args.category,
                args.item,
                export_format=args.export_format,
                output=args.output,
            )

        elif args.command == "related":
            if args.limit < 1:
                parser.error("--limit 必須大於 0。")

            related_main(
                args.category,
                args.item,
                limit=args.limit,
            )
        elif args.command == "topic":
            if args.json:
                data = get_topic_data(args.category, args.item)

                print(
                    json.dumps(
                        data,
                        ensure_ascii=False,
                        indent=2,
                    )
                )
            
            else:
                print_topic_text(args.category, args.item)
        elif args.command == "scan":
            scan_main(
                args.text,
                minimum_length=args.min_length,
                json_output=args.json,
                source=args.source,
            )
        elif args.command == "search":
            search_main(
                args.keyword,
                summary_only=args.summary,
                exact=args.exact,
                topic_only=args.topic_only,
                record_only=args.record_only,
                category_filter=args.category,
                limit=args.limit,
                json_output=args.json,
                count_only=args.count,
                random_result=args.random_result,
                tree_view=args.tree,
                open_topic=args.open_topic,
                source=args.source,
            )
    except KeyError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
