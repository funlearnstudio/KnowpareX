from __future__ import annotations

import argparse
import json
import re
from .knowledge_service import get_categories, get_items, get_topic_data
from collections import defaultdict

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
            )
    except KeyError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()