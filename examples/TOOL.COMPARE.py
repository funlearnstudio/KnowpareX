# ===========================================
# *********************
# TOOL.COMPARE.py
# python3 PROGRAMMING_TOOLS/TOOL.COMPARE.py
# python3 PROGRAMMING_TOOLS/TOOL.PRACTICE.py
# python3 PROGRAMMING_TOOLS/TOOL.REVIEW.py
# *********************

# ===========================================


# ===========================================
# import
# ===========================================
from system_library import library
# run code

print("=======================================================")
print("===================高中學科＋程式資料庫===================")
print("======================= 所有分類 =======================")
print("=====================All functions=====================")
print("=======================================================")

# 目錄只在程式啟動時顯示一次
print()
print("=======================================================")
print("All Categories")
print("所有分類")
print("=======================================================")

for category_name in library:
    print(category_name)

print("=======================================================")


while True:
    category = input(
        "請輸入分類（輸入 0 結束，輸入「目錄」查看所有分類）: "
    ).strip()
    if category == "目錄":

        print("=======================================================")
        print("===================高中學科＋程式資料庫===================")
        print("======================= 所有分類 =======================")
        print("=====================All functions=====================")
        print("=======================================================")

        # 目錄只在程式啟動時顯示一次
        print()
        print("=======================================================")
        print("All Categories")
        print("所有分類")
        print("=======================================================")

        for category_name in library:
            print(category_name)

        print("=======================================================")
        continue


    if category == "0":
        print("Finished!")
        print("程式已結束！")
        break

    if category not in library:
        print(f'Cannot find category: "{category}"')
        print(f'找不到分類：「{category}」')
        continue

    print()
    print("=======================================================")
    print(f"{category}")
    print("=======================================================")

    for item_name in library[category]:
        print(item_name)

    print("=======================================================")

    item = input(
        "請輸入項目（輸入 「返回」 返回上一層）: "
    ).strip()

    if item.lower() == "返回":
        continue

    if item not in library[category]:
        print(f'Cannot find item: "{item}"')
        print(f'找不到項目：「{item}」')
        continue

    print()
    library[category][item]()
    print()
    print("=======================================================")
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
