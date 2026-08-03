# ===========================================
# => DIFFERENT <= means:
# 「概念與語法都不同」
# (概念不相似，語法不相似)

# => CODE DIFFERENT, SYNTAX SIMILAR <= means:
# 「概念不同，但語法相似」
# (概念不相似，語法相似)

# => CODE DIFFERENT, SYNTAX SAME <= means:
# 「概念不同，但語法完全相同」
# (概念不相似，語法完全相同)

# => CODE SIMILAR, SYNTAX DIFFERENT <= means:
# 「概念相似，但語法不同」
# (概念相似，語法不相似)

# => SIMILAR <= means:
# 「概念與語法都相似」
# (概念相似，語法也相似)

# => CODE SIMILAR, SYNTAX SAME <= means:
# 「概念相似，而且語法完全相同」
# (概念相似，語法完全相同)

# => CODE SAME, SYNTAX DIFFERENT <= means:
# 「概念完全相同，但語法不同」
# (概念完全相同，語法不相似)

# => CODE SAME, SYNTAX SIMILAR <= means:
# 「概念完全相同，而且語法相似」
# (概念完全相同，語法相似)

# => EXACT SAME <= means:
# 「概念與語法都完全相同」
# (概念完全相同，語法完全相同)

# causes:
# A 是原因，B 是結果
#
# resultsin:
# A 這個事件或過程，導致 B
# ===========================================


# 所有函式

#============================================================================================================
#============================================================================================================
#============================================================================================================


show_output = True
collected_data = []


def set_show(value):
    global show_output
    show_output = value


def clear_data():
    collected_data.clear()


def get_data():
    return collected_data.copy()


def save_data(relation, code_a, language_a, code_b, language_b):
    data = {
        "relation": relation,
        "code_a": code_a,
        "language_a": language_a,
        "code_b": code_b,
        "language_b": language_b,
    }

    collected_data.append(data)

    if show_output:
        print(
            f"{code_a} ({language_a}) "
            f"=> {relation} <= "
            f"{code_b} ({language_b})"
        )

    return data


def different(code_a, language_a, code_b, language_b):
    return save_data(
        "DIFFERENT",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codesimilarbutsyntaxsame(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE SIMILAR, SYNTAX SAME",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codesamebutsyntaxsimilar(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE SAME, SYNTAX SIMILAR",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codedifferentbutsyntaxsimilar(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE DIFFERENT, SYNTAX SIMILAR",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codesimilarbutsyntaxdifferent(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE SIMILAR, SYNTAX DIFFERENT",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codedifferentbutsyntaxsame(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE DIFFERENT, SYNTAX SAME",
        code_a,
        language_a,
        code_b,
        language_b
    )


def codesamebutsyntaxdifferent(code_a, language_a, code_b, language_b):
    return save_data(
        "CODE SAME, SYNTAX DIFFERENT",
        code_a,
        language_a,
        code_b,
        language_b
    )


def similar(code_a, language_a, code_b, language_b):
    return save_data(
        "SIMILAR",
        code_a,
        language_a,
        code_b,
        language_b
    )


def exactsame(code_a, language_a, code_b, language_b):
    return save_data(
        "EXACT SAME",
        code_a,
        language_a,
        code_b,
        language_b
    )

def nodirectequivalent(code_a, language_a, code_b, language_b):
    return save_data(
        "NO DIRECT EQUIVALENT",
        code_a,
        language_a,
        code_b,
        language_b
    )


#==========數學關係============
def inverselyproportionalto(code_a, language_a, code_b, language_b):
    return save_data(
        "反比於",
        code_a,
        language_a,
        code_b,
        language_b
    )


def approximately(code_a, language_a, code_b, language_b):
    return save_data(
        "約為",
        code_a,
        language_a,
        code_b,
        language_b
    )

def equal(code_a, language_a, code_b, language_b):
    return save_data(
        "=",
        code_a,
        language_a,
        code_b,
        language_b
    )

def bigger(code_a, language_a, code_b, language_b):
    return save_data(
        ">",
        code_a,
        language_a,
        code_b,
        language_b
    )
def smaller(code_a, language_a, code_b, language_b):
    return save_data(
        "<",
        code_a,
        language_a,
        code_b,
        language_b
    )
def equalorbigger(code_a, language_a, code_b, language_b):
    return save_data(
        ">=",
        code_a,
        language_a,
        code_b,
        language_b
    )
def equalorsmaller(code_a, language_a, code_b, language_b):
    return save_data(
        "<=",
        code_a,
        language_a,
        code_b,
        language_b
    )


def notequal(code_a, language_a, code_b, language_b):
    return save_data("!=", code_a, language_a, code_b, language_b)


def approximatelyequal(code_a, language_a, code_b, language_b):
    return save_data("≈", code_a, language_a, code_b, language_b)


def proportionalto(code_a, language_a, code_b, language_b):
    return save_data("正比於", code_a, language_a, code_b, language_b)


def equivalentto(code_a, language_a, code_b, language_b):
    return save_data("等價於", code_a, language_a, code_b, language_b)


def calculatedby(code_a, language_a, code_b, language_b):
    return save_data("計算方式", code_a, language_a, code_b, language_b)


def simplifiedto(code_a, language_a, code_b, language_b):
    return save_data("化簡為", code_a, language_a, code_b, language_b)


def factorizedto(code_a, language_a, code_b, language_b):
    return save_data("因式分解為", code_a, language_a, code_b, language_b)
# ========== 一般知識關係 ==========

def definition(content_a, label_a, content_b, label_b):
    return save_data("定義為", content_a, label_a, content_b, label_b)


def exampleof(content_a, label_a, content_b, label_b):
    return save_data("是……的例子", content_a, label_a, content_b, label_b)


def partof(content_a, label_a, content_b, label_b):
    return save_data("是……的一部分", content_a, label_a, content_b, label_b)


def typeof(content_a, label_a, content_b, label_b):
    return save_data("是……的一種類型", content_a, label_a, content_b, label_b)


def causes(content_a, label_a, content_b, label_b):
    return save_data("造成", content_a, label_a, content_b, label_b)


def resultsin(content_a, label_a, content_b, label_b):
    return save_data("導致", content_a, label_a, content_b, label_b)


def requires(content_a, label_a, content_b, label_b):
    return save_data("需要", content_a, label_a, content_b, label_b)


def before(content_a, label_a, content_b, label_b):
    return save_data("在……之前", content_a, label_a, content_b, label_b)


def after(content_a, label_a, content_b, label_b):
    return save_data("在……之後", content_a, label_a, content_b, label_b)


def opposite(content_a, label_a, content_b, label_b):
    return save_data("與……相反", content_a, label_a, content_b, label_b)


def related(content_a, label_a, content_b, label_b):
    return save_data("與……相關", content_a, label_a, content_b, label_b)


def translates(content_a, label_a, content_b, label_b):
    return save_data("翻譯為", content_a, label_a, content_b, label_b)
def composedof(content_a, label_a, content_b, label_b):
    return save_data(
        "由……組成",
        content_a,
        label_a,
        content_b,
        label_b
    )


def functionof(content_a, label_a, content_b, label_b):
    return save_data(
        "功能是",
        content_a,
        label_a,
        content_b,
        label_b
    )


def locatedin(content_a, label_a, content_b, label_b):
    return save_data(
        "位於",
        content_a,
        label_a,
        content_b,
        label_b
    )


def characterizedby(content_a, label_a, content_b, label_b):
    return save_data(
        "特徵是",
        content_a,
        label_a,
        content_b,
        label_b
    )

# ========== 程式套件與生態系關係 ==========

def samepurpose(content_a, label_a, content_b, label_b):
    return save_data(
        "用途相近",
        content_a,
        label_a,
        content_b,
        label_b
    )


def alternativeof(content_a, label_a, content_b, label_b):
    return save_data(
        "可作為……的替代方案",
        content_a,
        label_a,
        content_b,
        label_b
    )


def equivalentrole(content_a, label_a, content_b, label_b):
    return save_data(
        "在生態系中的角色相近",
        content_a,
        label_a,
        content_b,
        label_b
    )


def wrapperof(content_a, label_a, content_b, label_b):
    return save_data(
        "是……的語言綁定或包裝",
        content_a,
        label_a,
        content_b,
        label_b
    )


def depends_on(content_a, label_a, content_b, label_b):
    return save_data(
        "依賴",
        content_a,
        label_a,
        content_b,
        label_b
    )


def builtwith(content_a, label_a, content_b, label_b):
    return save_data(
        "以……建構",
        content_a,
        label_a,
        content_b,
        label_b
    )


def provides(content_a, label_a, content_b, label_b):
    return save_data(
        "提供",
        content_a,
        label_a,
        content_b,
        label_b
    )


def usedfor(content_a, label_a, content_b, label_b):
    return save_data(
        "用於",
        content_a,
        label_a,
        content_b,
        label_b
    )

def customrelation(relation, content_a, label_a, content_b, label_b):
    return save_data(
        relation,
        content_a,
        label_a,
        content_b,
        label_b
    )


def nothing():
    data = {
        "relation": None,
        "code_a": None,
        "language_a": None,
        "code_b": None,
        "language_b": None,
    }

    if show_output:
        print("這裡沒有資料！")

    return data


#============================================================================================================
#============================================================================================================
#============================================================================================================


# 使用方法：

# ---------------------------------
# 一般搜尋模式

# set_show(True)
# exactsame("abs(x)", "c++", "abs(x)", "Python")

# ---------------------------------


# ---------------------------------
# 收集資料但不顯示答案

# clear_data()
# set_show(False)

# exactsame("abs(x)", "c++", "abs(x)", "Python")
# codesamebutsyntaxsimilar("abs(x)", "c++", "Math.abs(x)", "JavaScript")

# questions = get_data()

# set_show(True)

# ---------------------------------


# ---------------------------------
# 概念與語法一起比較

# different("","","","")
# similar("","","","")
# exactsame("","","","")

# ---------------------------------


# ---------------------------------
# 分別比較概念與語法

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

# codedifferentbutsyntaxsimilar("","","","")
# codesimilarbutsyntaxdifferent("","","","")

# ---------------------------------


# ---------------------------------
# 3

# codesimilarbutsyntaxsame("","","","")
# codesamebutsyntaxsimilar("","","","")

# ---------------------------------


# 由 Steve Lin 設計


#| 概念＼語法 | 不同                            | 相似                            | 相同                         |
#| ---------- | ------------------------------- | ------------------------------- | ---------------------------- |
#| 不同       | `different`                     | `codedifferentbutsyntaxsimilar` | `codedifferentbutsyntaxsame` |
#| 相似       | `codesimilarbutsyntaxdifferent` | `similar`                       | `codesimilarbutsyntaxsame`   |
#| 相同       | `codesamebutsyntaxdifferent`    | `codesamebutsyntaxsimilar`      | `exactsame`                  |