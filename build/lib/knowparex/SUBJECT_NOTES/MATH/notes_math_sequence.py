from knowparex.PROGRAMMING_NOTES import compare_system
class math_sequence:
    @staticmethod
    def arithmetic_sequence():
        compare_system.calculatedby('等差數列第 n 項', '目標', "a_n = a_1 + (n - 1)d", '公式')
        compare_system.equal("2, 5, 8, 11", '數列', '公差 = 3', '性質')
        compare_system.equal("a1 = 4, d = 2, a5", '題目', "12", '答案')
        compare_system.calculatedby('等差級數和', '目標', "S_n = n(a_1 + a_n)/2", '公式')
        compare_system.equal("1 + 2 + 3 + 4 + 5", '等差級數和', "15", '答案')

    @staticmethod
    def geometric_sequence():
        compare_system.calculatedby('等比數列第 n 項', '目標', "a_n = a_1 × r^(n - 1)", '公式')
        compare_system.equal("2, 6, 18, 54", '數列', '公比 = 3', '性質')
        compare_system.equal("a1 = 2, r = 3, a4", '題目', "54", '答案')
        compare_system.calculatedby('有限等比級數和', '目標', "S_n = a_1(1 - r^n)/(1 - r)", '公式')
        compare_system.equal("1 + 2 + 4 + 8", '等比級數和', "15", '答案')