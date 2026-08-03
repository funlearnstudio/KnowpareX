from __future__ import annotations

import argparse
import json
from pathlib import Path

from .knowledge_service import get_categories, get_items, get_topic_data


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
            data = get_topic_data(category, item)
        except KeyError as error:
            print(error)
            continue
        print()
        for record in data:
            print(
                f'{record["code_a"]} ({record["language_a"]}) '
                f'=> {record["relation"]} <= '
                f'{record["code_b"]} ({record["language_b"]})'
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="KnowpareX")
    parser.add_argument("--categories", action="store_true", help="List all categories")
    parser.add_argument("--items", metavar="CATEGORY", help="List items in a category")
    parser.add_argument("--topic", nargs=2, metavar=("CATEGORY", "ITEM"), help="Print one topic as JSON")
    args = parser.parse_args()

    if args.categories:
        print("\n".join(get_categories()))
    elif args.items:
        print("\n".join(get_items(args.items)))
    elif args.topic:
        print(json.dumps(get_topic_data(*args.topic), ensure_ascii=False, indent=2))
    else:
        compare_main()


if __name__ == "__main__":
    main()
