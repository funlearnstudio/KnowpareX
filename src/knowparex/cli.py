from __future__ import annotations

import argparse
import json
import re
from .knowledge_service import get_categories, get_items, get_topic_data
from collections import defaultdict
import random
from datetime import date
from pathlib import Path

def print_topic_text(category: str, item: str) -> None:
    """以適合人閱讀的格式顯示主題資料。"""
    data = get_topic_data(category, item)

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
    
    all_categories = get_categories()

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

        for item in get_items(category):
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
                records = get_topic_data(category, item)
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

    sorted_topics = sorted(
        matched_topics,
        key=lambda topic: (
            topic not in direct_topic_matches,
            topic[0],
            topic[1],
        ),
    )

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
            # 不只是符合搜尋字詞的資料
            print_topic_text(category, item)
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
        if args.command is None or args.command == "compare":
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
            )
    except KeyError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()