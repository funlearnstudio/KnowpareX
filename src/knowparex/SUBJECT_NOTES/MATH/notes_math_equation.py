from knowparex.PROGRAMMING_NOTES import compare_system
class math_equation:
    @staticmethod
    def linear_equation():
        compare_system.equal("x + 5 = 12", '方程式', "x = 7", '解')
        compare_system.equal("2x = 10", '方程式', "x = 5", '解')
        compare_system.equal("3x - 4 = 11", '方程式', "x = 5", '解')
        compare_system.equal("5(x - 2) = 15", '方程式', "x = 5", '解')
        compare_system.equal("2x + 3 = x + 8", '方程式', "x = 5", '解')

    @staticmethod
    def simultaneous_equations():
        compare_system.equal("x + y = 7, x - y = 1", '聯立方程式', "x = 4, y = 3", '解')
        compare_system.equal("2x + y = 5, x - y = 1", '聯立方程式', "x = 2, y = 1", '解')
        compare_system.equal("x + 2y = 8, x = 2", '聯立方程式', "x = 2, y = 3", '解')
        compare_system.equal("3x + y = 10, y = 1", '聯立方程式', "x = 3, y = 1", '解')
        compare_system.equal("x + y = 10, x = y", '聯立方程式', "x = 5, y = 5", '解')

    @staticmethod
    def quadratic_equation():
        compare_system.equal("x^2 - 9 = 0", '二次方程式', 'x = 3 或 x = -3', '解')
        compare_system.equal("x^2 - 5x + 6 = 0", '二次方程式', 'x = 2 或 x = 3', '解')
        compare_system.equal("x^2 = 16", '二次方程式', 'x = 4 或 x = -4', '解')
        compare_system.equal("(x - 2)^2 = 0", '二次方程式', "x = 2", '解')
        compare_system.calculatedby('二次方程式的根', '目標', "x = (-b ± sqrt(b^2 - 4ac)) / 2a", '公式')

    @staticmethod
    def inequality():
        compare_system.equal("x + 3 > 7", '不等式', "x > 4", '解')
        compare_system.equal("2x <= 10", '不等式', "x <= 5", '解')
        compare_system.equal("-2x > 6", '不等式', "x < -3", '解')
        compare_system.equal("3x - 1 >= 8", '不等式', "x >= 3", '解')
        compare_system.equal("|x| < 5", '絕對值不等式', "-5 < x < 5", '解')