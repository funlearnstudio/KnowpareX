from knowparex.PROGRAMMING_NOTES import compare_system
class math_function:
    @staticmethod
    def function_value():
        compare_system.equal("f(x) = 2x + 1, f(3)", '題目', "7", '答案')
        compare_system.equal("f(x) = x^2, f(-2)", '題目', "4", '答案')
        compare_system.equal("f(x) = 5 - x, f(1)", '題目', "4", '答案')
        compare_system.equal("f(x) = 3x, f(0)", '題目', "0", '答案')
        compare_system.equal("f(x) = x^2 + 2x, f(2)", '題目', "8", '答案')

    @staticmethod
    def linear_function():
        compare_system.calculatedby('斜率', '目標', "(y2 - y1) / (x2 - x1)", '公式')
        compare_system.equivalentto('一次函數', '名稱', "y = mx + b", '形式')
        compare_system.equal("y = 2x + 3", '函數', '斜率 = 2', '性質')
        compare_system.equal("y = -x + 4", '函數', 'y 截距 = 4', '性質')
        compare_system.equal("y = 5", '函數', '斜率 = 0', '性質')

    @staticmethod
    def quadratic_function():
        compare_system.equivalentto('二次函數', '名稱', "y = ax^2 + bx + c", '形式')
        compare_system.equal("y = x^2", '函數', '頂點 = (0, 0)', '性質')
        compare_system.equal("y = (x - 2)^2 + 3", '函數', '頂點 = (2, 3)', '性質')
        compare_system.equal("a > 0", '二次項係數', '開口向上', '圖形')
        compare_system.equal("a < 0", '二次項係數', '開口向下', '圖形')

    @staticmethod
    def domain():
        compare_system.equal("f(x) = 1/x", '函數', "x != 0", '定義域限制')
        compare_system.equal("f(x) = sqrt(x)", '函數', "x >= 0", '實數定義域')
        compare_system.equal("f(x) = x^2", '函數', '所有實數', '定義域')
        compare_system.equal("f(x) = sqrt(x - 3)", '函數', "x >= 3", '定義域')
        compare_system.equal("f(x) = 1/(x - 5)", '函數', "x != 5", '定義域限制')