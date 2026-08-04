from knowparex.PROGRAMMING_NOTES import compare_system


class math_number:
    @staticmethod
    def integer():
        compare_system.bigger("5", "整數", "-2", "整數")
        compare_system.smaller("-8", "整數", "3", "整數")
        compare_system.equal("-(-7)", "算式", "7", "答案")
        compare_system.equal("0", "整數", "-0", "整數")
        compare_system.notequal("-4", "整數", "4", "整數")

    @staticmethod
    def absolute_value():
        compare_system.equal("|5|", "絕對值", "5", "答案")
        compare_system.equal("|-5|", "絕對值", "5", "答案")
        compare_system.equal("|0|", "絕對值", "0", "答案")
        compare_system.equal("|x|", "當 x >= 0", "x", "答案")
        compare_system.equal("|x|", "當 x < 0", "-x", "答案")

    @staticmethod
    def fraction():
        compare_system.equivalentto("1/2", "分數", "2/4", "分數")
        compare_system.equivalentto("3/5", "分數", "0.6", "小數")
        compare_system.simplifiedto("8/12", "原分數", "2/3", "最簡分數")
        compare_system.equal("1/3 + 1/6", "算式", "1/2", "答案")
        compare_system.equal("3/4 × 2/3", "算式", "1/2", "答案")

    @staticmethod
    def percentage():
        compare_system.equivalentto("50%", "百分比", "0.5", "小數")
        compare_system.equivalentto("25%", "百分比", "1/4", "分數")
        compare_system.equal("300 的 20%", "題目", "60", "答案")
        compare_system.equal("100 增加 10%", "題目", "110", "答案")
        compare_system.equal("100 減少 10%", "題目", "90", "答案")

    @staticmethod
    def exponent():
        compare_system.equal("2^3", "指數", "8", "答案")
        compare_system.equivalentto("a^m × a^n", "指數律", "a^(m+n)", "結果")
        compare_system.equivalentto("a^m ÷ a^n", "指數律", "a^(m-n)", "結果")
        compare_system.equivalentto("(a^m)^n", "指數律", "a^(mn)", "結果")
        compare_system.equal("a^0", "當 a != 0", "1", "答案")

    @staticmethod
    def radical():
        compare_system.equal("sqrt(25)", "根式", "5", "答案")
        compare_system.simplifiedto("sqrt(12)", "原根式", "2sqrt(3)", "化簡後根式")
        compare_system.equivalentto("sqrt(a × b)", "根式運算規則", "sqrt(a) × sqrt(b)", "結果")
        compare_system.equal("sqrt(2)^2", "算式", "2", "答案")
        compare_system.approximatelyequal("sqrt(2)", "根式", "1.414", "小數")

    @staticmethod
    def natural_numbers():
        compare_system.definition("自然數", "數的集合", "用於計數的數，例如 1、2、3、4……；部分教材也包含 0", "定義")
        compare_system.equal("1、2、3、4……", "常見例子", "自然數", "分類")
        compare_system.equal("0 是否屬於自然數", "使用說明", "依教材或採用的定義而定", "答案")
        compare_system.notequal("-1", "數", "自然數", "錯誤分類")
        compare_system.notequal("1/2", "數", "自然數", "錯誤分類")

    @staticmethod
    def rational_numbers():
        compare_system.definition("有理數", "數的集合", "可以表示成兩個整數之比 a/b，且 b 不等於 0 的數", "定義")
        compare_system.equal("整數", "數的集合", "有理數", "分類")
        compare_system.equal("有限小數", "小數類型", "有理數", "分類")
        compare_system.equal("循環小數", "小數類型", "有理數", "分類")
        compare_system.equal("0.75", "有限小數", "3/4", "分數表示")
        compare_system.equal("0.333……", "循環小數", "1/3", "分數表示")
        compare_system.notequal("π", "數", "有理數", "錯誤分類")
        compare_system.notequal("√2", "數", "有理數", "錯誤分類")

    @staticmethod
    def irrational_numbers():
        compare_system.definition("無理數", "數的集合", "不能表示成兩個整數之比的實數", "定義")
        compare_system.equal("無理數的小數表示", "特徵", "無限且不循環", "答案")
        compare_system.equal("√2", "例子", "無理數", "分類")
        compare_system.equal("π", "例子", "無理數", "分類")
        compare_system.equal("√3", "例子", "無理數", "分類")
        compare_system.notequal("無限小數", "敘述", "一定都是無理數", "錯誤觀念")
        compare_system.notequal("0.333……", "循環小數", "無理數", "錯誤分類")

    @staticmethod
    def real_numbers():
        compare_system.definition("實數", "數的集合", "有理數與無理數的總稱", "定義")
        compare_system.equal("實數", "組成", "有理數與無理數", "答案")
        compare_system.equal("有理數", "數的集合", "實數的一部分", "分類")
        compare_system.equal("無理數", "數的集合", "實數的一部分", "分類")
        compare_system.equal("實數", "幾何表示", "可對應到數線上的點", "答案")
        compare_system.notequal("實數", "敘述", "只包含整數", "錯誤觀念")
        compare_system.notequal("有理數與無理數", "集合關係", "具有共同元素", "錯誤觀念")

    @staticmethod
    def number_line():
        compare_system.definition("數線", "數學表示", "以直線上的點表示實數大小與位置的工具", "定義")
        compare_system.equal("數線向右", "方向", "數值增大", "答案")
        compare_system.equal("數線向左", "方向", "數值減小", "答案")
        compare_system.equal("0", "數線位置", "原點", "答案")
        compare_system.equal("相反數", "數線關係", "位於原點兩側且到原點距離相等", "定義")
        compare_system.equal("絕對值", "數線意義", "一個數所對應的點與原點之間的距離", "定義")
        compare_system.notequal("數線上較右側的數", "大小關係", "比較小", "錯誤觀念")

    @staticmethod
    def number_set_relationships():
        compare_system.equal("自然數", "集合關係", "整數的一部分", "答案")
        compare_system.equal("整數", "集合關係", "有理數的一部分", "答案")
        compare_system.equal("有理數", "集合關係", "實數的一部分", "答案")
        compare_system.equal("無理數", "集合關係", "實數的一部分", "答案")
        compare_system.notequal("無理數", "集合關係", "有理數的一部分", "錯誤觀念")