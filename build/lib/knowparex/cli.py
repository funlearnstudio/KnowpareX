from __future__ import annotations

import argparse
import json

from .knowledge_service import get_categories, get_items, get_topic_data


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

    except KeyError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()