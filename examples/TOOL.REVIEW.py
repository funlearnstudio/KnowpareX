# ===========================================
# *********************
# TOOL.REVIEW.py
# python3 PROGRAMMING_TOOLS/TOOL.COMPARE.py
# python3 PROGRAMMING_TOOLS/TOOL.PRACTICE.py
# python3 PROGRAMMING_TOOLS/TOOL.REVIEW.py
# *********************
# ===========================================

import json
import os


file_name = "PROGRAMMING_TOOLS/wrong_questions.json"


# ===========================================
# 檢查錯題檔案
# ===========================================
if not os.path.exists(file_name):
    print("No wrong question file found.")
    exit()


# ===========================================
# 讀取錯題
# ===========================================
try:
    with open(file_name, "r", encoding="utf-8") as file:
        wrong_questions = json.load(file)

except json.JSONDecodeError:
    print("Wrong question file is broken or empty.")
    exit()


if len(wrong_questions) == 0:
    print("No wrong questions to review.")
    exit()


# ===========================================
# 整理科目
# ===========================================
subjects = []

for wrong in wrong_questions:
    # 支援以前沒有 subject 的舊錯題
    subject = wrong.get("subject", "未分類")

    if subject not in subjects:
        subjects.append(subject)


# ===========================================
# 選擇科目
# ===========================================
print("=======================================================")
print("===================== 錯題科目 ========================")
print("=======================================================")

for subject in subjects:
    subject_question_count = 0

    for wrong in wrong_questions:
        if wrong.get("subject", "未分類") == subject:
            subject_question_count += 1

    print(f"{subject} ({subject_question_count} 題)")

print("=======================================================")

selected_subject = input(
    "請輸入要複習的科目（輸入 0 結束）："
).strip()

if selected_subject == "0":
    print("Finished!")
    exit()

if selected_subject not in subjects:
    print(f'找不到科目：「{selected_subject}」')
    exit()


# ===========================================
# 整理該科目的單元
# ===========================================
units = []

for wrong in wrong_questions:
    subject = wrong.get("subject", "未分類")

    if subject == selected_subject:
        unit = wrong.get("unit", "未分類")

        if unit not in units:
            units.append(unit)


# ===========================================
# 選擇單元
# ===========================================
print()
print("=======================================================")
print(f"================== {selected_subject} ==================")
print("=======================================================")

for unit in units:
    unit_question_count = 0

    for wrong in wrong_questions:
        subject = wrong.get("subject", "未分類")
        wrong_unit = wrong.get("unit", "未分類")

        if subject == selected_subject and wrong_unit == unit:
            unit_question_count += 1

    print(f"{unit} ({unit_question_count} 題)")

print("全部")
print("=======================================================")

selected_unit = input(
    "請輸入要複習的單元（輸入 全部 複習本科全部錯題）："
).strip()

if selected_unit != "全部" and selected_unit not in units:
    print(f'在「{selected_subject}」中找不到單元：「{selected_unit}」')
    exit()


# ===========================================
# 將錯題分成：
# 1. 這次要複習的
# 2. 這次不複習的
# ===========================================
review_questions = []
untouched_questions = []

for wrong in wrong_questions:
    subject = wrong.get("subject", "未分類")
    unit = wrong.get("unit", "未分類")

    subject_matches = subject == selected_subject

    unit_matches = (
        selected_unit == "全部"
        or unit == selected_unit
    )

    if subject_matches and unit_matches:
        review_questions.append(wrong)
    else:
        untouched_questions.append(wrong)


if len(review_questions) == 0:
    print("This subject or unit has no wrong questions.")
    exit()


# ===========================================
# 開始複習
# ===========================================
print()
print("=======================================================")
print("================== WRONG QUESTION REVIEW ==============")
print("=======================================================")
print(f"科目：{selected_subject}")
print(f"單元：{selected_unit}")
print(f"題數：{len(review_questions)}")
print("=======================================================")

still_wrong_questions = []
correct_count = 0


for question_number, wrong in enumerate(review_questions, start=1):
    question = wrong["question"]

    print()
    print(f"Question {question_number}/{len(review_questions)}")

    print(
        f'{question["code_a"]} ({question["language_a"]}) '
        f'=> {question["relation"]} <= '
        f'{{enter your answer}} ({question["language_b"]})'
    )

    answer = input("> ").strip()
    correct_answer = question["code_b"]

    if answer == correct_answer:
        print("Correct!")
        correct_count += 1

    else:
        print("Wrong!")
        print(f"Correct answer: {correct_answer}")

        # 這次仍然答錯，所以繼續保留
        still_wrong_questions.append(wrong)


# ===========================================
# 合併錯題
#
# untouched_questions：
# 這次沒有選到的科目與單元，全部保留
#
# still_wrong_questions：
# 這次複習後仍然答錯的題目
# ===========================================
remaining_questions = (
    untouched_questions
    + still_wrong_questions
)


# ===========================================
# 寫回 JSON
# ===========================================
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(
        remaining_questions,
        file,
        ensure_ascii=False,
        indent=4
    )


# ===========================================
# 顯示結果
# ===========================================
print()
print("=======================================================")
print(f"REVIEW SUBJECT: {selected_subject}")
print(f"REVIEW UNIT: {selected_unit}")
print(f"REVIEW SCORE: {correct_count}/{len(review_questions)}")
print(
    "REMAINING WRONG QUESTIONS IN THIS REVIEW: "
    f"{len(still_wrong_questions)}"
)
print(
    "TOTAL REMAINING WRONG QUESTIONS: "
    f"{len(remaining_questions)}"
)
print("=======================================================")


# invented by Steve lin 林炫銓