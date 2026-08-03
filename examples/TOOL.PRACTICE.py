# ===========================================
# *********************
# TOOL.PRACTICE.py
# python3 PROGRAMMING_TOOLS/TOOL.COMPARE.py
# python3 PROGRAMMING_TOOLS/TOOL.PRACTICE.py
# python3 PROGRAMMING_TOOLS/TOOL.REVIEW.py
# *********************
# ===========================================


# ===========================================
# import
# ===========================================
import PROGRAMMING_NOTES.compare_system as compare_system 
from system_library import library
import json
import os
# run code
# code_(name).something()

print("=======================================================")
print("=====================All functions=====================")
print("=======================================================")

for category in library:
    print(category)

print("=======================================================")
print()
mode = input("CHOOSE MODE (practice / test): ").strip().lower()

while mode not in ["practice", "test"]:
    print('Please enter "practice" or "test".')
    mode = input("CHOOSE MODE (practice / test): ").strip().lower()

while True:
    print()
    print("=======================================================")
    print("====================== 大標題 =========================")
    print("=======================================================")

    for category_name in library:
        print(category_name)

    print("=======================================================")

    category = input(
        "請輸入大標題（輸入 0 結束）："
    ).strip()

    if category == "0":
        print("Finished!")
        break

    if category not in library:
        print(f'找不到大標題：「{category}」')
        continue

    print()
    print("=======================================================")
    print(f"==================== {category} ====================")
    print("=======================================================")

    for item_name in library[category]:
        print(item_name)

    print("=======================================================")

    item = input(
        "請輸入小標題（輸入 back 返回上一層）："
    ).strip()

    if item.lower() == "back":
        continue

    if item not in library[category]:
        print(f'在「{category}」中找不到小標題：「{item}」')
        continue

    # 從這裡開始接回原本的題目收集與作答程式

    # 清除上一次取得的資料
    compare_system.clear_data()

    # 不顯示完整答案
    compare_system.set_show(False)

    # 執行 library 裡的筆記函式，
    # 資料會被 compare_system 自動收集
    library[category][item]()

    # 取得該主題的全部題目
    questions = compare_system.get_data()

    # 恢復正常顯示模式
    compare_system.set_show(True)

    if len(questions) == 0:
        print("This topic has no practice data.")
        continue

    correct_count = 0
    wrong_questions = []

    print("=======================================================")
    print(f"TOPIC: {category} {item}")
    print(f"QUESTIONS: {len(questions)}")
    print("=======================================================")


    for question_number, question in enumerate(questions, start=1):
        print()
        print(f"Question {question_number}/{len(questions)}")

        # 一次只顯示一行題目
        print(
            f'{question["code_a"]} ({question["language_a"]}) '
            f'=> {question["relation"]} <= '
            f'{{enter your answer}} ({question["language_b"]})'
        )

        answer = input("> ").strip()
        correct_answer = question["code_b"]

        if answer == correct_answer:
            correct_count += 1

            if mode == "practice":
                print("Correct!")
        else:
            wrong_questions.append({
                "subject": category,
                "unit": item,
                "question": question,
                "your_answer": answer,
            })

            if mode == "practice":
                print("Wrong!")
                print(f"Correct answer: {correct_answer}")

    print()
    print("=======================================================")
    print(f"SCORE: {correct_count}/{len(questions)}")
    print("=======================================================")
    file_name = "PROGRAMMING_TOOLS/wrong_questions.json"

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            old_wrong_questions = json.load(file)
    else:
        old_wrong_questions = []

    old_wrong_questions.extend(wrong_questions)

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(old_wrong_questions, file, ensure_ascii=False, indent=4)

    if mode == "test" and len(wrong_questions) > 0:
        print("WRONG ANSWERS:")

        for wrong_number, wrong in enumerate(wrong_questions, start=1):
            print(
                f'Wrong question {wrong_number}: '
                f'your answer = {wrong["your_answer"]}, '
                f'correct answer = {wrong["question"]["code_b"]}'
            )
    
#============================================================================


# how to use: 

# ---------------------------------
# both

# different("","","","")
# similar("","","","")
# exactsame("","","","")
# ---------------------------------


# ---------------------------------
# half

# code(x)butsyntax(y)("","","","")
# code(x)butsyntax(y)("","","","")
# different < similar < same
# ---------------------------------


# ===============================================


# ---------------------------------
# 1

# codedifferentbutsyntaxsame("","","","")
# codesamebutsyntaxdifferent("","","","")
# ---------------------------------


# ---------------------------------
# 2


# ---------------------------------
# codedifferentbutsyntaxsimilar("","","","")
# codesimilarbutsyntaxdifferent("","","","")
# ---------------------------------


# ---------------------------------
# 3

# codesimilarbutsyntaxsame("","","","")
# codesamebutsyntaxsimilar("","","","")

# ---------------------------------

# invented by Steve lin 林炫銓

#| 概念＼語法  | Different                       | Similar                         | Same                         |
#| --------- | ------------------------------- | ------------------------------- | ---------------------------- |
#| Different | `different`                     | `codedifferentbutsyntaxsimilar` | `codedifferentbutsyntaxsame` |
#| Similar   | `codesimilarbutsyntaxdifferent` | `similar`                       | `codesimilarbutsyntaxsame`   |
#| Same      | `codesamebutsyntaxdifferent`    | `codesamebutsyntaxsimilar`      | `exactsame`                  |
#============================================================================
