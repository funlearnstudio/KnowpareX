from knowparex.PROGRAMMING_NOTES import compare_system
class math_probability:
    @staticmethod
    def basic_probability():
        compare_system.calculatedby('機率', '目標', '有利結果數 / 所有可能結果數', '公式')
        compare_system.equal('公平硬幣出現正面的機率', '題目', "1/2", '答案')
        compare_system.equal('擲出 6 點的機率', '公平骰子', "1/6", '答案')
        compare_system.equal('不可能事件的機率', '事件', "0", '答案')
        compare_system.equal('必然事件的機率', '事件', "1", '答案')

    @staticmethod
    def complement():
        compare_system.equivalentto('P（非 A）', '餘事件', "1 - P(A)", '公式')
        compare_system.equal("P(A) = 0.3", '已知', "P(not A) = 0.7", '答案')
        compare_system.equal('P（下雨）= 20%', '已知', 'P（不下雨）= 80%', '答案')
        compare_system.equal('P（成功）= 3/5', '已知', 'P（失敗）= 2/5', '答案')
        compare_system.equal('P（非不可能事件）', '題目', "1", '答案')