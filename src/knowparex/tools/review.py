from __future__ import annotations

from collections import Counter
from typing import Any

from ..storage import get_wrong_questions_path, load_wrong_questions, save_wrong_questions


def _choose(prompt: str, options: list[str], *, allow_all: bool = False) -> str | None:
    while True:
        value = input(prompt).strip()
        if value == "0":
            return None
        if allow_all and value == "全部":
            return value
        if value in options:
            return value
        print(f"找不到選項：{value}")


def main() -> None:
    wrong_questions = load_wrong_questions()
    if not wrong_questions:
        print("No wrong questions to review.")
        print(f"Wrong-question file: {get_wrong_questions_path()}")
        return

    subjects = list(dict.fromkeys(q.get("subject", "未分類") for q in wrong_questions))
    subject_counts = Counter(q.get("subject", "未分類") for q in wrong_questions)

    print("=" * 55)
    print("錯題科目")
    print("=" * 55)
    for subject in subjects:
        print(f"{subject} ({subject_counts[subject]} 題)")

    selected_subject = _choose("請輸入要複習的科目（輸入 0 結束）：", subjects)
    if selected_subject is None:
        print("Finished!")
        return

    units = list(
        dict.fromkeys(
            q.get("unit", "未分類")
            for q in wrong_questions
            if q.get("subject", "未分類") == selected_subject
        )
    )
    unit_counts = Counter(
        q.get("unit", "未分類")
        for q in wrong_questions
        if q.get("subject", "未分類") == selected_subject
    )

    print("\n" + "=" * 55)
    print(selected_subject)
    print("=" * 55)
    for unit in units:
        print(f"{unit} ({unit_counts[unit]} 題)")
    print("全部")

    selected_unit = _choose(
        "請輸入要複習的單元（輸入 全部 複習本科全部錯題）：",
        units,
        allow_all=True,
    )
    if selected_unit is None:
        print("Finished!")
        return

    review_questions: list[dict[str, Any]] = []
    untouched_questions: list[dict[str, Any]] = []

    for wrong in wrong_questions:
        subject_matches = wrong.get("subject", "未分類") == selected_subject
        unit_matches = selected_unit == "全部" or wrong.get("unit", "未分類") == selected_unit
        (review_questions if subject_matches and unit_matches else untouched_questions).append(wrong)

    correct_count = 0
    still_wrong: list[dict[str, Any]] = []

    print("\n" + "=" * 55)
    print("WRONG QUESTION REVIEW")
    print(f"科目：{selected_subject}")
    print(f"單元：{selected_unit}")
    print(f"題數：{len(review_questions)}")
    print("=" * 55)

    for number, wrong in enumerate(review_questions, start=1):
        question = wrong.get("question", {})
        print(f"\nQuestion {number}/{len(review_questions)}")
        print(
            f'{question.get("code_a", "")} ({question.get("language_a", "")}) '
            f'=> {question.get("relation", "")} <= '
            f'{{enter your answer}} ({question.get("language_b", "")})'
        )
        answer = input("> ").strip()
        correct_answer = str(question.get("code_b", ""))

        if answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print("Wrong!")
            print(f"Correct answer: {correct_answer}")
            still_wrong.append(wrong)

    remaining = untouched_questions + still_wrong
    path = save_wrong_questions(remaining)

    print("\n" + "=" * 55)
    print(f"REVIEW SCORE: {correct_count}/{len(review_questions)}")
    print(f"REMAINING WRONG QUESTIONS IN THIS REVIEW: {len(still_wrong)}")
    print(f"TOTAL REMAINING WRONG QUESTIONS: {len(remaining)}")
    print(f"Saved to: {path}")
    print("=" * 55)
