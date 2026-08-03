from __future__ import annotations

from typing import Any

from ..knowledge_service import get_categories, get_items, get_topic_data
from ..storage import load_wrong_questions, save_wrong_questions


def _ask_mode() -> str:
    while True:
        mode = input("CHOOSE MODE (practice / test): ").strip().lower()
        if mode in {"practice", "test"}:
            return mode
        print('Please enter "practice" or "test".')


def _select_topic() -> tuple[str, str] | None:
    while True:
        print("\n" + "=" * 55)
        print("所有分類")
        print("=" * 55)
        for category in get_categories():
            print(category)

        category = input("請輸入分類（輸入 0 結束）：").strip()
        if category == "0":
            return None

        try:
            items = get_items(category)
        except KeyError as error:
            print(error)
            continue

        print(f"\n{category}：")
        for item in items:
            print(item)

        item = input("請輸入項目（輸入 back 返回上一層）：").strip()
        if item.lower() == "back":
            continue
        if item not in items:
            print(f'在「{category}」中找不到項目：「{item}」')
            continue
        return category, item


def _run_questions(category: str, item: str, mode: str) -> None:
    questions = get_topic_data(category, item)
    if not questions:
        print("This topic has no practice data.")
        return

    correct_count = 0
    wrong_questions: list[dict[str, Any]] = []

    print("=" * 55)
    print(f"TOPIC: {category} / {item}")
    print(f"QUESTIONS: {len(questions)}")
    print("=" * 55)

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}/{len(questions)}")
        print(
            f'{question["code_a"]} ({question["language_a"]}) '
            f'=> {question["relation"]} <= '
            f'{{enter your answer}} ({question["language_b"]})'
        )

        answer = input("> ").strip()
        correct_answer = str(question["code_b"])

        if answer == correct_answer:
            correct_count += 1
            if mode == "practice":
                print("Correct!")
        else:
            wrong_questions.append(
                {
                    "subject": category,
                    "unit": item,
                    "question": question,
                    "your_answer": answer,
                }
            )
            if mode == "practice":
                print("Wrong!")
                print(f"Correct answer: {correct_answer}")

    print("\n" + "=" * 55)
    print(f"SCORE: {correct_count}/{len(questions)}")
    print("=" * 55)

    if wrong_questions:
        all_wrong = load_wrong_questions()
        all_wrong.extend(wrong_questions)
        path = save_wrong_questions(all_wrong)
        print(f"Saved {len(wrong_questions)} wrong question(s) to: {path}")

    if mode == "test" and wrong_questions:
        print("WRONG ANSWERS:")
        for number, wrong in enumerate(wrong_questions, start=1):
            print(
                f'Wrong question {number}: '
                f'your answer = {wrong["your_answer"]}, '
                f'correct answer = {wrong["question"]["code_b"]}'
            )


def main() -> None:
    print("=" * 55)
    print("KnowpareX Practice / Test")
    print("=" * 55)
    mode = _ask_mode()

    while True:
        selected = _select_topic()
        if selected is None:
            print("Finished!")
            return
        category, item = selected
        _run_questions(category, item, mode)
