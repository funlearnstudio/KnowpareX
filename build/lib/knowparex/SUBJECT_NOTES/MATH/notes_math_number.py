from knowparex.PROGRAMMING_NOTES import compare_system
class math_number:
    @staticmethod
    def integer():
        compare_system.bigger("5", '整數', "-2", '整數')
        compare_system.smaller("-8", '整數', "3", '整數')
        compare_system.equal("-(-7)", '算式', "7", '答案')
        compare_system.equal("0", '整數', "-0", '整數')
        compare_system.notequal("-4", '整數', "4", '整數')

    @staticmethod
    def absolute_value():
        compare_system.equal("|5|", '絕對值', "5", '答案')
        compare_system.equal("|-5|", '絕對值', "5", '答案')
        compare_system.equal("|0|", '絕對值', "0", '答案')
        compare_system.equal("|x|", '當 x >= 0', "x", '答案')
        compare_system.equal("|x|", '當 x < 0', "-x", '答案')

    @staticmethod
    def fraction():
        compare_system.equivalentto("1/2", '分數', "2/4", '分數')
        compare_system.equivalentto("3/5", '分數', "0.6", '小數')
        compare_system.simplifiedto("8/12", '原分數', "2/3", '最簡分數')
        compare_system.equal("1/3 + 1/6", '算式', "1/2", '答案')
        compare_system.equal("3/4 × 2/3", '算式', "1/2", '答案')

    @staticmethod
    def percentage():
        compare_system.equivalentto("50%", '百分比', "0.5", '小數')
        compare_system.equivalentto("25%", '百分比', "1/4", '分數')
        compare_system.equal('300 的 20%', '題目', "60", '答案')
        compare_system.equal('100 增加 10%', '題目', "110", '答案')
        compare_system.equal('100 減少 10%', '題目', "90", '答案')

    @staticmethod
    def exponent():
        compare_system.equal("2^3", '指數', "8", '答案')
        compare_system.equivalentto("a^m × a^n", '指數律', "a^(m+n)", '結果')
        compare_system.equivalentto("a^m ÷ a^n", '指數律', "a^(m-n)", '結果')
        compare_system.equivalentto("(a^m)^n", '指數律', "a^(mn)", '結果')
        compare_system.equal("a^0", '當 a != 0', "1", '答案')

    @staticmethod
    def radical():
        compare_system.equal("sqrt(25)", '根式', "5", '答案')
        compare_system.simplifiedto("sqrt(12)", '原根式', "2sqrt(3)", '化簡後根式')
        compare_system.equivalentto("sqrt(a × b)", '根式運算規則', "sqrt(a) × sqrt(b)", '結果')
        compare_system.equal("sqrt(2)^2", '算式', "2", '答案')
        compare_system.approximatelyequal("sqrt(2)", '根式', "1.414", '小數')