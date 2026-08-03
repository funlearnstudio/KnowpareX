from knowparex.PROGRAMMING_NOTES import compare_system
class math_algebra:
    @staticmethod
    def like_terms():
        compare_system.simplifiedto("2x + 3x", '原式', "5x", '化簡結果')
        compare_system.simplifiedto("7a - 2a", '原式', "5a", '化簡結果')
        compare_system.simplifiedto("3x + 4 + 2x - 1", '原式', "5x + 3", '化簡結果')
        compare_system.simplifiedto("5y - y", '原式', "4y", '化簡結果')
        compare_system.notequal("2x + 3", '算式', "5x", '算式')

    @staticmethod
    def distributive_property():
        compare_system.equivalentto("a(b + c)", '原式', "ab + ac", '展開結果')
        compare_system.equivalentto("3(x + 2)", '原式', "3x + 6", '展開結果')
        compare_system.equivalentto("-2(x - 4)", '原式', "-2x + 8", '展開結果')
        compare_system.equivalentto("(x + 2)(x + 3)", '原式', "x^2 + 5x + 6", '展開結果')
        compare_system.equivalentto("(a - b)(a + b)", '原式', "a^2 - b^2", '展開結果')

    @staticmethod
    def factoring():
        compare_system.factorizedto("x^2 + 5x + 6", '多項式', "(x + 2)(x + 3)", '因式分解結果')
        compare_system.factorizedto("x^2 - 9", '平方差', "(x - 3)(x + 3)", '因式分解結果')
        compare_system.factorizedto("2x + 6", '多項式', "2(x + 3)", '因式分解結果')
        compare_system.factorizedto("x^2 - 6x + 9", '完全平方式', "(x - 3)^2", '因式分解結果')
        compare_system.factorizedto("3x^2 + 6x", '多項式', "3x(x + 2)", '因式分解結果')

    @staticmethod
    def identities():
        compare_system.equivalentto("(a + b)^2", '乘法公式', "a^2 + 2ab + b^2", '展開結果')
        compare_system.equivalentto("(a - b)^2", '乘法公式', "a^2 - 2ab + b^2", '展開結果')
        compare_system.equivalentto("(a + b)(a - b)", '乘法公式', "a^2 - b^2", '展開結果')
        compare_system.equivalentto("(x + 1)^2", '乘法公式', "x^2 + 2x + 1", '展開結果')
        compare_system.equivalentto("(2x - 3)^2", '乘法公式', "4x^2 - 12x + 9", '展開結果')