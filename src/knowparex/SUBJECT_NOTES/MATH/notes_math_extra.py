from knowparex.PROGRAMMING_NOTES import compare_system


class math_extra:
    # =====================================================
    # 數與數系
    # =====================================================

    @staticmethod
    def decimal():
        compare_system.equivalentto("0.5", "有限小數", "1/2", "分數")
        compare_system.equivalentto("0.125", "有限小數", "1/8", "分數")
        compare_system.equivalentto("0.333……", "循環小數", "1/3", "分數")
        compare_system.notequal("無限小數", "敘述", "一定是無理數", "錯誤觀念")

    @staticmethod
    def scientific_notation():
        compare_system.equivalentto("3.2 × 10^5", "科學記號", "320000", "一般表示")
        compare_system.equivalentto("4.5 × 10^-3", "科學記號", "0.0045", "一般表示")
        compare_system.equal("科學記號的前導數", "條件", "大於等於 1 且小於 10", "答案")
        compare_system.notequal("25 × 10^3", "敘述", "標準科學記號", "錯誤觀念")

    @staticmethod
    def approximation():
        compare_system.approximatelyequal("π", "圓周率", "3.14", "近似值")
        compare_system.approximatelyequal("sqrt(2)", "無理數", "1.414", "近似值")
        compare_system.equal("四捨五入到整數", "3.6", "4", "答案")
        compare_system.equal("四捨五入到小數第一位", "2.46", "2.5", "答案")

    @staticmethod
    def significant_figures():
        compare_system.equal("0.00450", "有效數字個數", "3", "答案")
        compare_system.equal("1200", "有效數字", "需依題目標示判斷末尾零是否有效", "使用說明")
        compare_system.equal("1.2345 取三位有效數字", "題目", "1.23", "答案")
        compare_system.notequal("小數點前的零", "敘述", "一定是有效數字", "錯誤觀念")

    @staticmethod
    def interval():
        compare_system.equivalentto("[2, 5]", "閉區間", "2 <= x <= 5", "不等式")
        compare_system.equivalentto("(2, 5)", "開區間", "2 < x < 5", "不等式")
        compare_system.equivalentto("[2, 5)", "半開區間", "2 <= x < 5", "不等式")
        compare_system.equivalentto("(-∞, 3]", "區間", "x <= 3", "不等式")
        compare_system.notequal("∞", "敘述", "可以作為區間中的實數端點", "錯誤觀念")

    # =====================================================
    # 代數
    # =====================================================

    @staticmethod
    def expression():
        compare_system.equivalentto("3x + 2", "代數式", "由數字、字母與運算符號組成的式子", "定義")
        compare_system.equal("3x + 2", "x = 4 時的值", "14", "答案")
        compare_system.notequal("代數式", "敘述", "一定含有等號", "錯誤觀念")

    @staticmethod
    def monomial():
        compare_system.equivalentto("3x^2y", "單項式", "由數與字母乘積組成且字母指數為非負整數的式子", "定義")
        compare_system.equal("3x^2y", "次數", "3", "答案")
        compare_system.equal("-5", "分類", "常數單項式", "答案")
        compare_system.notequal("1/x", "分類", "多項式中的單項式", "錯誤分類")

    @staticmethod
    def polynomial():
        compare_system.equivalentto("2x^3 - x + 5", "多項式", "有限個單項式相加減形成的代數式", "定義")
        compare_system.equal("2x^3 - x + 5", "最高次數", "3", "答案")
        compare_system.equal("2x^3 - x + 5", "常數項", "5", "答案")
        compare_system.notequal("x^-1 + 2", "分類", "多項式", "錯誤分類")

    @staticmethod
    def coefficient():
        compare_system.equal("7x^2", "x^2 的係數", "7", "答案")
        compare_system.equal("-x", "x 的係數", "-1", "答案")
        compare_system.equal("5", "常數項係數", "5", "答案")

    @staticmethod
    def constant_term():
        compare_system.equal("3x^2 - 4x + 7", "常數項", "7", "答案")
        compare_system.equal("x^3 + 2x", "常數項", "0", "答案")
        compare_system.notequal("常數項", "敘述", "一定不是 0", "錯誤觀念")

    @staticmethod
    def special_products():
        compare_system.equivalentto("(a + b)^2", "乘法公式", "a^2 + 2ab + b^2", "展開結果")
        compare_system.equivalentto("(a - b)^2", "乘法公式", "a^2 - 2ab + b^2", "展開結果")
        compare_system.equivalentto("(a + b)(a - b)", "乘法公式", "a^2 - b^2", "展開結果")
        compare_system.notequal("(a + b)^2", "敘述", "a^2 + b^2", "錯誤觀念")

    @staticmethod
    def perfect_square():
        compare_system.equivalentto("x^2 + 6x + 9", "完全平方", "(x + 3)^2", "因式分解")
        compare_system.equivalentto("x^2 - 10x + 25", "完全平方", "(x - 5)^2", "因式分解")
        compare_system.equal("a^2 + 2ab + b^2", "結構", "(a + b)^2", "答案")

    @staticmethod
    def difference_of_squares():
        compare_system.equivalentto("a^2 - b^2", "平方差", "(a - b)(a + b)", "因式分解")
        compare_system.equivalentto("x^2 - 16", "平方差", "(x - 4)(x + 4)", "因式分解")
        compare_system.notequal("a^2 + b^2", "敘述", "可用平方差公式直接分解", "錯誤觀念")

    @staticmethod
    def common_factor():
        compare_system.simplifiedto("6x + 9", "原式", "3(2x + 3)", "提出公因式")
        compare_system.simplifiedto("4x^2 - 8x", "原式", "4x(x - 2)", "提出公因式")
        compare_system.equal("提公因式", "目的", "把共同因數提出括號外", "答案")

    @staticmethod
    def cross_method():
        compare_system.equivalentto("x^2 + 5x + 6", "二次式", "(x + 2)(x + 3)", "十字交乘")
        compare_system.equivalentto("2x^2 + 7x + 3", "二次式", "(2x + 1)(x + 3)", "十字交乘")
        compare_system.notequal("十字交乘", "敘述", "所有多項式都一定能用整數係數分解", "錯誤觀念")

    @staticmethod
    def factor_theorem():
        compare_system.equivalentto("f(a) = 0", "因式定理條件", "x - a 是 f(x) 的因式", "結論")
        compare_system.equal("f(x) = x^2 - 5x + 6", "f(2)", "0", "答案")
        compare_system.equal("x - 2", "與 x^2 - 5x + 6 的關係", "因式", "答案")

    @staticmethod
    def remainder_theorem():
        compare_system.equivalentto("f(x) 除以 x - a 的餘數", "餘式定理", "f(a)", "答案")
        compare_system.equal("f(x) = x^2 + 1 除以 x - 2", "餘數", "5", "答案")
        compare_system.notequal("f(a) = 0", "敘述", "餘數一定不為 0", "錯誤觀念")

    # =====================================================
    # 方程式與不等式
    # =====================================================

    @staticmethod
    def cubic_equation():
        compare_system.equivalentto("ax^3 + bx^2 + cx + d = 0，a != 0", "三次方程式", "最高次為 3 的一元多項式方程式", "定義")
        compare_system.equal("x^3 - 8 = 0", "實數解", "x = 2", "答案")
        compare_system.equal("x^3 - 6x^2 + 11x - 6 = 0", "解", "x = 1、2、3", "答案")
        compare_system.notequal("三次方程式", "敘述", "一定只有一個實數解", "錯誤觀念")

    @staticmethod
    def polynomial_equation():
        compare_system.equivalentto("P(x) = 0", "多項式方程式", "由多項式形成的方程式", "定義")
        compare_system.equal("多項式方程式的次數", "判斷方式", "最高次非零項的次數", "答案")
        compare_system.notequal("n 次方程式", "敘述", "一定有 n 個互異實數解", "錯誤觀念")

    @staticmethod
    def rational_equation():
        compare_system.equivalentto("含未知數分母的方程式", "分式方程式", "需先限制分母不為 0", "定義")
        compare_system.equal("1/x = 2", "解", "x = 1/2", "答案")
        compare_system.notequal("x = 0", "對 1/x = 2", "合法解", "錯誤解")
        compare_system.equal("分式方程式", "解題後必要步驟", "檢查增根與分母限制", "答案")

    @staticmethod
    def exponential_equation():
        compare_system.equivalentto("2^x = 8", "指數方程式", "x = 3", "答案")
        compare_system.equivalentto("a^x = a^y，a > 0 且 a != 1", "同底指數關係", "x = y", "答案")
        compare_system.notequal("指數方程式", "敘述", "只能用試數求解", "錯誤觀念")

    @staticmethod
    def logarithmic_equation():
        compare_system.equivalentto("log_a(x) = b", "對數方程式", "x = a^b", "指數形式")
        compare_system.equal("log_2(x) = 3", "解", "x = 8", "答案")
        compare_system.equal("對數真數", "限制", "必須大於 0", "答案")
        compare_system.notequal("log(x - 2)", "定義域", "x <= 2", "錯誤觀念")

    @staticmethod
    def absolute_equation():
        compare_system.equal("|x| = 5", "解", "x = 5 或 x = -5", "答案")
        compare_system.equal("|x - 2| = 3", "解", "x = 5 或 x = -1", "答案")
        compare_system.notequal("|x| = -2", "敘述", "有實數解", "錯誤觀念")

    @staticmethod
    def absolute_inequality():
        compare_system.equivalentto("|x| < a，a > 0", "絕對值不等式", "-a < x < a", "解")
        compare_system.equivalentto("|x| > a，a > 0", "絕對值不等式", "x < -a 或 x > a", "解")
        compare_system.equal("|x| <= 3", "解", "-3 <= x <= 3", "答案")

    @staticmethod
    def discriminant():
        compare_system.equivalentto("Δ", "二次方程式判別式", "b^2 - 4ac", "公式")
        compare_system.equal("Δ > 0", "根的情況", "有兩個相異實根", "答案")
        compare_system.equal("Δ = 0", "根的情況", "有兩個相同實根", "答案")
        compare_system.equal("Δ < 0", "根的情況", "沒有實根", "答案")

    @staticmethod
    def roots_and_coefficients():
        compare_system.equal("ax^2 + bx + c = 0 的兩根 α、β", "根和", "α + β = -b/a", "公式")
        compare_system.equal("ax^2 + bx + c = 0 的兩根 α、β", "根積", "αβ = c/a", "公式")
        compare_system.notequal("根與係數關係", "敘述", "不需確認 a != 0", "錯誤觀念")

    # =====================================================
    # 函數
    # =====================================================

    @staticmethod
    def function_definition():
        compare_system.equivalentto("函數", "數學關係", "每個定義域元素都對應唯一函數值的關係", "定義")
        compare_system.equal("同一個輸入", "函數條件", "不能對應兩個不同輸出", "答案")
        compare_system.notequal("不同輸入", "敘述", "一定不能對應相同輸出", "錯誤觀念")

    @staticmethod
    def function_range():
        compare_system.equivalentto("值域", "函數概念", "函數所有可能輸出值形成的集合", "定義")
        compare_system.equal("f(x) = x^2，x 為實數", "值域", "y >= 0", "答案")
        compare_system.equal("f(x) = 2x + 1，x 為實數", "值域", "所有實數", "答案")

    @staticmethod
    def cubic_function():
        compare_system.equivalentto("f(x) = ax^3 + bx^2 + cx + d，a != 0", "三次函數", "最高次為 3 的多項式函數", "定義")
        compare_system.equal("f(x) = x^3", "函數性質", "奇函數", "答案")
        compare_system.equal("f(x) = x^3", "圖形經過", "原點", "答案")
        compare_system.notequal("所有三次函數", "敘述", "圖形都關於原點對稱", "錯誤觀念")

    @staticmethod
    def polynomial_function():
        compare_system.equivalentto("多項式函數", "函數類型", "以多項式作為對應規則的函數", "定義")
        compare_system.equal("f(x) = 2x^4 - x + 3", "次數", "4", "答案")
        compare_system.equal("多項式函數", "定義域", "所有實數", "答案")

    @staticmethod
    def absolute_function():
        compare_system.equivalentto("f(x) = |x|", "絕對值函數", "圖形呈 V 字形", "圖形特徵")
        compare_system.equal("f(x) = |x|", "最小值", "0", "答案")
        compare_system.equal("f(x) = |x|", "對稱軸", "y 軸", "答案")

    @staticmethod
    def piecewise_function():
        compare_system.equivalentto("分段函數", "函數類型", "在不同輸入區間使用不同規則定義的函數", "定義")
        compare_system.equal("分段函數求值", "方法", "先判斷輸入落在哪個條件範圍", "答案")
        compare_system.notequal("分段函數", "敘述", "一定不連續", "錯誤觀念")

    @staticmethod
    def inverse_function():
        compare_system.equivalentto("反函數", "函數關係", "交換原函數輸入與輸出的函數", "定義")
        compare_system.equal("f(x) = 2x + 3", "反函數", "f^-1(x) = (x - 3)/2", "答案")
        compare_system.equal("f(f^-1(x))", "結果", "x", "答案")
        compare_system.notequal("所有函數", "敘述", "都有反函數", "錯誤觀念")

    @staticmethod
    def odd_function():
        compare_system.equivalentto("f(-x) = -f(x)", "奇函數條件", "圖形關於原點對稱", "答案")
        compare_system.equal("f(x) = x^3", "分類", "奇函數", "答案")
        compare_system.notequal("奇函數", "敘述", "圖形關於 y 軸對稱", "錯誤觀念")

    @staticmethod
    def even_function():
        compare_system.equivalentto("f(-x) = f(x)", "偶函數條件", "圖形關於 y 軸對稱", "答案")
        compare_system.equal("f(x) = x^2", "分類", "偶函數", "答案")
        compare_system.notequal("偶函數", "敘述", "圖形一定通過原點", "錯誤觀念")

    @staticmethod
    def exponential_function():
        compare_system.equivalentto("f(x) = a^x，a > 0 且 a != 1", "指數函數", "自變數位於指數位置的函數", "定義")
        compare_system.equal("a > 1", "指數函數趨勢", "遞增", "答案")
        compare_system.equal("0 < a < 1", "指數函數趨勢", "遞減", "答案")
        compare_system.equal("指數函數", "值域", "y > 0", "答案")

    @staticmethod
    def logarithmic_function():
        compare_system.equivalentto("f(x) = log_a(x)", "對數函數", "指數函數的反函數", "定義")
        compare_system.equal("對數函數", "定義域", "x > 0", "答案")
        compare_system.equal("對數函數", "值域", "所有實數", "答案")
        compare_system.equal("log_a(1)", "答案", "0", "結果")

    @staticmethod
    def monotonicity():
        compare_system.equivalentto("遞增函數", "函數性質", "輸入增大時函數值不減少或增大", "概念")
        compare_system.equivalentto("遞減函數", "函數性質", "輸入增大時函數值不增加或減小", "概念")
        compare_system.notequal("函數", "敘述", "在整個定義域一定遞增或遞減", "錯誤觀念")

    @staticmethod
    def transformation():
        compare_system.equal("y = f(x) + k", "圖形變換", "向上平移 k 單位", "答案")
        compare_system.equal("y = f(x - h)", "圖形變換", "向右平移 h 單位", "答案")
        compare_system.equal("y = -f(x)", "圖形變換", "關於 x 軸對稱", "答案")
        compare_system.equal("y = f(-x)", "圖形變換", "關於 y 軸對稱", "答案")

    # =====================================================
    # 幾何
    # =====================================================

    @staticmethod
    def angle():
        compare_system.equal("直角", "角度", "90°", "答案")
        compare_system.equal("平角", "角度", "180°", "答案")
        compare_system.equal("周角", "角度", "360°", "答案")
        compare_system.equal("互補角", "角度和", "90°", "答案")
        compare_system.equal("互餘角", "角度和", "180°", "答案")

    @staticmethod
    def parallel_lines():
        compare_system.equal("兩平行線被截線所截", "同位角", "相等", "答案")
        compare_system.equal("兩平行線被截線所截", "內錯角", "相等", "答案")
        compare_system.equal("兩平行線被截線所截", "同側內角和", "180°", "答案")

    @staticmethod
    def congruence():
        compare_system.equivalentto("全等圖形", "幾何關係", "形狀與大小完全相同的圖形", "定義")
        compare_system.equal("SSS", "三角形全等判定", "三邊分別相等", "答案")
        compare_system.equal("SAS", "三角形全等判定", "兩邊及夾角分別相等", "答案")
        compare_system.equal("ASA", "三角形全等判定", "兩角及夾邊分別相等", "答案")

    @staticmethod
    def similarity():
        compare_system.equivalentto("相似圖形", "幾何關係", "形狀相同且對應邊成比例的圖形", "定義")
        compare_system.equal("相似三角形", "對應角", "相等", "答案")
        compare_system.equal("相似三角形", "對應邊", "成比例", "答案")
        compare_system.equal("相似比為 k", "面積比", "k^2", "答案")

    @staticmethod
    def central_angle():
        compare_system.equal("圓心角", "頂點位置", "圓心", "答案")
        compare_system.equal("圓心角度數", "與所對弧度數關係", "相等", "答案")

    @staticmethod
    def inscribed_angle():
        compare_system.equal("圓周角", "頂點位置", "圓周上", "答案")
        compare_system.equal("同弧所對圓周角", "關係", "相等", "答案")
        compare_system.equal("圓周角", "與同弧圓心角關係", "等於圓心角的一半", "答案")

    @staticmethod
    def chord():
        compare_system.equivalentto("弦", "圓的線段", "兩端都在圓上的線段", "定義")
        compare_system.equal("直徑", "與弦關係", "通過圓心的最長弦", "答案")

    @staticmethod
    def tangent():
        compare_system.equivalentto("圓的切線", "幾何概念", "與圓只有一個公共點的直線", "定義")
        compare_system.equal("切線", "與切點半徑關係", "互相垂直", "答案")
        compare_system.equal("同一圓外一點引出的兩條切線段", "長度關係", "相等", "答案")

    @staticmethod
    def sector():
        compare_system.equivalentto("扇形", "圓形區域", "由兩條半徑與其所夾弧圍成的區域", "定義")
        compare_system.equal("扇形弧長", "公式", "圓心角/360° × 2πr", "答案")
        compare_system.equal("扇形面積", "公式", "圓心角/360° × πr^2", "答案")

    @staticmethod
    def area_volume():
        compare_system.equal("三角形面積", "公式", "底 × 高 ÷ 2", "答案")
        compare_system.equal("平行四邊形面積", "公式", "底 × 高", "答案")
        compare_system.equal("圓面積", "公式", "πr^2", "答案")
        compare_system.equal("圓柱體積", "公式", "πr^2h", "答案")
        compare_system.equal("圓錐體積", "公式", "πr^2h/3", "答案")
        compare_system.equal("球體積", "公式", "4πr^3/3", "答案")

    # =====================================================
    # 三角函數
    # =====================================================

    @staticmethod
    def sine_law():
        compare_system.equal("正弦定理", "公式", "a/sin(A) = b/sin(B) = c/sin(C)", "答案")
        compare_system.equal("正弦定理", "常見用途", "已知兩角一邊或兩邊一非夾角求三角形", "答案")

    @staticmethod
    def cosine_law():
        compare_system.equal("餘弦定理", "公式", "c^2 = a^2 + b^2 - 2ab cos(C)", "答案")
        compare_system.equal("C = 90°", "餘弦定理結果", "退化為畢氏定理", "答案")

    @staticmethod
    def trig_graph():
        compare_system.equal("y = sin(x)", "週期", "2π", "答案")
        compare_system.equal("y = cos(x)", "週期", "2π", "答案")
        compare_system.equal("y = tan(x)", "週期", "π", "答案")
        compare_system.equal("sin 與 cos", "值域", "[-1, 1]", "答案")

    @staticmethod
    def trig_identity():
        compare_system.equal("sin^2(x) + cos^2(x)", "三角恆等式", "1", "答案")
        compare_system.equal("tan(x)", "與 sin、cos 關係", "sin(x)/cos(x)", "答案")
        compare_system.notequal("tan(x)", "定義條件", "cos(x) = 0 時仍有定義", "錯誤觀念")

    # =====================================================
    # 數列與級數
    # =====================================================

    @staticmethod
    def sequence():
        compare_system.equivalentto("數列", "數學概念", "依一定順序排列的一串數", "定義")
        compare_system.equal("a_n", "符號意義", "數列第 n 項", "答案")

    @staticmethod
    def arithmetic_series():
        compare_system.equal("等差級數前 n 項和", "公式", "S_n = n(a_1 + a_n)/2", "答案")
        compare_system.equal("1 + 2 + ... + n", "和", "n(n + 1)/2", "答案")

    @staticmethod
    def geometric_series():
        compare_system.equal("等比級數前 n 項和，r != 1", "公式", "S_n = a_1(1-r^n)/(1-r)", "答案")
        compare_system.equal("無窮等比級數收斂條件", "條件", "|r| < 1", "答案")
        compare_system.equal("無窮等比級數和", "公式", "S = a_1/(1-r)", "答案")

    @staticmethod
    def recurrence():
        compare_system.equivalentto("遞迴數列", "數列類型", "利用前面項目定義後面項目的數列", "定義")
        compare_system.equal("a_1 = 1，a_n = a_(n-1) + 2", "數列類型", "等差數列", "答案")

    @staticmethod
    def sigma():
        compare_system.equivalentto("Σ", "數學符號", "連續加總的簡寫符號", "定義")
        compare_system.equal("Σ(k)，k=1 到 n", "結果", "n(n+1)/2", "答案")
        compare_system.equal("Σc，共 n 項", "結果", "nc", "答案")

    # =====================================================
    # 排列組合
    # =====================================================

    @staticmethod
    def addition_rule():
        compare_system.equivalentto("加法原理", "計數原理", "互斥方法的總數等於各方法數相加", "定義")
        compare_system.equal("有 3 種公車或 2 種火車可選", "選一種交通方式的方法數", "5", "答案")

    @staticmethod
    def multiplication_rule():
        compare_system.equivalentto("乘法原理", "計數原理", "連續步驟總方法數等於各步驟方法數相乘", "定義")
        compare_system.equal("3 件上衣與 4 件褲子", "搭配數", "12", "答案")

    @staticmethod
    def permutation():
        compare_system.equal("n 個不同物取 r 個排列", "公式", "P(n,r) = n!/(n-r)!", "答案")
        compare_system.equal("5 個人排成一列", "排列數", "5! = 120", "答案")
        compare_system.equal("排列", "特徵", "順序不同視為不同結果", "答案")

    @staticmethod
    def combination():
        compare_system.equal("n 個不同物取 r 個組合", "公式", "C(n,r) = n!/[r!(n-r)!]", "答案")
        compare_system.equal("5 人中選 2 人", "組合數", "10", "答案")
        compare_system.equal("組合", "特徵", "不考慮選取順序", "答案")

    # =====================================================
    # 機率
    # =====================================================

    @staticmethod
    def sample_space():
        compare_system.equivalentto("樣本空間", "機率概念", "隨機試驗所有可能結果形成的集合", "定義")
        compare_system.equal("擲一枚骰子的樣本空間", "結果", "{1,2,3,4,5,6}", "答案")

    @staticmethod
    def event():
        compare_system.equivalentto("事件", "機率概念", "樣本空間的一個子集合", "定義")
        compare_system.equal("擲骰子得到偶數", "事件", "{2,4,6}", "答案")

    @staticmethod
    def conditional_probability():
        compare_system.equal("條件機率", "公式", "P(A|B) = P(A∩B)/P(B)", "答案")
        compare_system.equal("P(B)", "條件機率分母限制", "必須大於 0", "答案")

    @staticmethod
    def independent_event():
        compare_system.equal("A 與 B 獨立", "條件", "P(A∩B) = P(A)P(B)", "答案")
        compare_system.notequal("互斥事件", "敘述", "通常也是獨立事件", "錯誤觀念")

    # =====================================================
    # 統計
    # =====================================================

    @staticmethod
    def mean():
        compare_system.equal("平均數", "公式", "所有資料總和 ÷ 資料個數", "答案")
        compare_system.equal("2、4、6", "平均數", "4", "答案")

    @staticmethod
    def median():
        compare_system.equivalentto("中位數", "統計量", "資料排序後位於中央位置的數值", "定義")
        compare_system.equal("1、3、8", "中位數", "3", "答案")
        compare_system.equal("1、3、8、10", "中位數", "5.5", "答案")

    @staticmethod
    def mode():
        compare_system.equivalentto("眾數", "統計量", "出現次數最多的資料值", "定義")
        compare_system.equal("1、2、2、3", "眾數", "2", "答案")
        compare_system.notequal("一組資料", "敘述", "一定只有一個眾數", "錯誤觀念")

    @staticmethod
    def data_range():
        compare_system.equal("全距", "公式", "最大值 - 最小值", "答案")
        compare_system.equal("2、5、9", "全距", "7", "答案")

    @staticmethod
    def quartile():
        compare_system.equivalentto("四分位數", "統計概念", "將排序資料約分成四等份的分界值", "定義")
        compare_system.equal("第二四分位數 Q2", "關係", "中位數", "答案")

    @staticmethod
    def iqr():
        compare_system.equal("四分位距", "公式", "Q3 - Q1", "答案")
        compare_system.equal("四分位距", "用途", "描述中間 50% 資料的分散程度", "答案")

    @staticmethod
    def box_plot():
        compare_system.equal("盒狀圖", "主要資訊", "最小值、Q1、中位數、Q3、最大值", "答案")
        compare_system.equal("盒子的長度", "代表", "四分位距", "答案")

    @staticmethod
    def variance():
        compare_system.equivalentto("變異數", "統計量", "各資料與平均數差的平方之平均", "定義")
        compare_system.equal("所有資料相同", "變異數", "0", "答案")

    @staticmethod
    def standard_deviation():
        compare_system.equal("標準差", "與變異數關係", "變異數的平方根", "答案")
        compare_system.equal("標準差較大", "意義", "資料通常較分散", "答案")
        compare_system.notequal("標準差", "敘述", "可能是負數", "錯誤觀念")

    # =====================================================
    # 向量
    # =====================================================

    @staticmethod
    def vector():
        compare_system.equivalentto("向量", "數學量", "同時具有大小與方向的量", "定義")
        compare_system.equal("(3,4)", "向量長度", "5", "答案")
        compare_system.notequal("向量", "敘述", "只有大小沒有方向", "錯誤觀念")

    @staticmethod
    def vector_addition():
        compare_system.equal("(a,b) + (c,d)", "向量加法", "(a+c,b+d)", "答案")
        compare_system.equal("(1,2) + (3,4)", "結果", "(4,6)", "答案")

    @staticmethod
    def vector_subtraction():
        compare_system.equal("(a,b) - (c,d)", "向量減法", "(a-c,b-d)", "答案")
        compare_system.equal("(5,4) - (2,1)", "結果", "(3,3)", "答案")

    @staticmethod
    def dot_product():
        compare_system.equal("(a,b) · (c,d)", "向量內積", "ac + bd", "答案")
        compare_system.equal("兩向量垂直", "內積", "0", "答案")
        compare_system.equal("u · v", "另一公式", "|u||v|cosθ", "答案")

    @staticmethod
    def cross_product():
        compare_system.equivalentto("向量外積", "向量運算", "結果垂直於兩個原向量的向量", "定義")
        compare_system.equal("|u × v|", "大小", "|u||v|sinθ", "答案")
        compare_system.equal("平行向量", "外積大小", "0", "答案")

    @staticmethod
    def unit_vector():
        compare_system.equivalentto("單位向量", "向量類型", "長度為 1 的向量", "定義")
        compare_system.equal("向量 v 的單位向量", "公式", "v/|v|", "答案")

    # =====================================================
    # 矩陣
    # =====================================================

    @staticmethod
    def matrix():
        compare_system.equivalentto("矩陣", "數學物件", "依列與行排列的數或符號陣列", "定義")
        compare_system.equal("2 × 3 矩陣", "意義", "2 列 3 行", "答案")

    @staticmethod
    def matrix_addition():
        compare_system.equal("矩陣加法", "條件", "兩矩陣階數相同", "答案")
        compare_system.equal("[[1,2],[3,4]] + [[1,1],[1,1]]", "結果", "[[2,3],[4,5]]", "答案")

    @staticmethod
    def matrix_multiplication():
        compare_system.equal("A(m×n)B(n×p)", "乘積矩陣階數", "m×p", "答案")
        compare_system.equal("矩陣乘法", "一般性質", "通常 AB != BA", "答案")

    @staticmethod
    def transpose():
        compare_system.equivalentto("轉置矩陣", "矩陣運算", "交換矩陣的列與行", "定義")
        compare_system.equal("(A^T)^T", "結果", "A", "答案")

    @staticmethod
    def inverse_matrix():
        compare_system.equal("反矩陣 A^-1", "條件", "AA^-1 = I", "答案")
        compare_system.equal("可逆矩陣", "行列式條件", "det(A) != 0", "答案")
        compare_system.notequal("所有方陣", "敘述", "都有反矩陣", "錯誤觀念")

    @staticmethod
    def determinant():
        compare_system.equal("[[a,b],[c,d]]", "二階行列式", "ad - bc", "答案")
        compare_system.equal("det(A) = 0", "矩陣性質", "A 不可逆", "答案")

    # =====================================================
    # 複數
    # =====================================================

    @staticmethod
    def imaginary_number():
        compare_system.equal("i", "虛數單位", "sqrt(-1)", "定義")
        compare_system.equal("i^2", "結果", "-1", "答案")
        compare_system.equal("i^4", "結果", "1", "答案")

    @staticmethod
    def complex_number():
        compare_system.equivalentto("a + bi", "複數", "a、b 為實數且 i^2 = -1", "定義")
        compare_system.equal("a", "複數 a+bi 的部分", "實部", "答案")
        compare_system.equal("b", "複數 a+bi 的係數", "虛部係數", "答案")

    @staticmethod
    def conjugate():
        compare_system.equal("a + bi", "共軛複數", "a - bi", "答案")
        compare_system.equal("(a+bi)(a-bi)", "結果", "a^2 + b^2", "答案")

    @staticmethod
    def complex_plane():
        compare_system.equivalentto("複數平面", "幾何表示", "以橫軸表示實部、縱軸表示虛部的平面", "定義")
        compare_system.equal("複數 a+bi", "平面對應點", "(a,b)", "答案")
        compare_system.equal("|a+bi|", "複數絕對值", "sqrt(a^2+b^2)", "答案")

    # =====================================================
    # 微積分基礎
    # =====================================================

    @staticmethod
    def limit():
        compare_system.equivalentto("極限", "微積分概念", "變數接近某值時函數值所趨近的數", "定義")
        compare_system.equal("lim x→2 (x+3)", "結果", "5", "答案")
        compare_system.notequal("極限存在", "敘述", "函數在該點一定有定義", "錯誤觀念")

    @staticmethod
    def continuity():
        compare_system.equal("函數在 x=a 連續", "條件", "極限存在、函數值存在且兩者相等", "答案")
        compare_system.notequal("函數有斷點", "敘述", "在該點仍連續", "錯誤觀念")

    @staticmethod
    def derivative():
        compare_system.equivalentto("導數", "微積分概念", "函數瞬時變化率或切線斜率", "定義")
        compare_system.equal("d/dx(x^n)", "公式", "nx^(n-1)", "答案")
        compare_system.equal("d/dx(c)", "常數微分", "0", "答案")
        compare_system.equal("d/dx(x^2)", "結果", "2x", "答案")

    @staticmethod
    def differentiation():
        compare_system.equal("和的微分", "公式", "(f+g)' = f' + g'", "答案")
        compare_system.equal("乘積微分", "公式", "(fg)' = f'g + fg'", "答案")
        compare_system.equal("鏈鎖律", "公式", "d/dx f(g(x)) = f'(g(x))g'(x)", "答案")

    @staticmethod
    def integration():
        compare_system.equivalentto("積分", "微積分概念", "可用於求累積量、面積與反導函數", "定義")
        compare_system.equal("∫x^n dx，n != -1", "公式", "x^(n+1)/(n+1) + C", "答案")
        compare_system.equal("∫1 dx", "結果", "x + C", "答案")
        compare_system.equal("定積分", "幾何意義之一", "函數圖形與 x 軸間的帶符號面積", "答案")