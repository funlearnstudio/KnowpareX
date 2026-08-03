from knowparex.PROGRAMMING_NOTES import compare_system
class math_geometry:
    @staticmethod
    def triangle():
        compare_system.equal('角 A + 角 B + 角 C', '三角形', '180 度', '答案')
        compare_system.calculatedby('三角形面積', '目標', '底 × 高 ÷ 2', '公式')
        compare_system.equal('正三角形', '三角形種類', '三邊相等', '性質')
        compare_system.equal('等腰三角形', '三角形種類', '至少兩邊相等', '性質')
        compare_system.equal('直角三角形', '三角形種類', '有一個 90 度角', '性質')

    @staticmethod
    def pythagorean_theorem():
        compare_system.equivalentto('直角三角形', '條件', "a^2 + b^2 = c^2", '公式')
        compare_system.equal("a = 3, b = 4", '直角三角形', "c = 5", '答案')
        compare_system.equal("a = 5, b = 12", '直角三角形', "c = 13", '答案')
        compare_system.equal("c = 10, a = 6", '直角三角形', "b = 8", '答案')
        compare_system.equal("3^2 + 4^2", '算式', "5^2", '結果')

    @staticmethod
    def circle():
        compare_system.calculatedby('圓周長', '目標', "2πr", '公式')
        compare_system.calculatedby('圓面積', '目標', "πr^2", '公式')
        compare_system.equal("diameter", '圓的性質', "2 × radius", '公式')
        compare_system.equal('周角', '圓', '360 度', '答案')
        compare_system.equal('平角', '圓', '180 度', '答案')

    @staticmethod
    def polygon():
        compare_system.calculatedby('內角和', 'n 邊形', "(n - 2) × 180 degrees", '公式')
        compare_system.equal('三角形內角和', '多邊形', '180 度', '答案')
        compare_system.equal('四邊形內角和', '多邊形', '360 度', '答案')
        compare_system.equal('五邊形內角和', '多邊形', "540 degrees", '答案')
        compare_system.equal('六邊形內角和', '多邊形', "720 degrees", '答案')

    @staticmethod
    def coordinate_geometry():
        compare_system.calculatedby('中點', '目標', "((x1 + x2)/2, (y1 + y2)/2)", '公式')
        compare_system.calculatedby('距離', '目標', "sqrt((x2 - x1)^2 + (y2 - y1)^2)", '公式')
        compare_system.calculatedby('斜率', '目標', "(y2 - y1)/(x2 - x1)", '公式')
        compare_system.equal('點 (0, 0) 與 (4, 0)', '距離題目', "4", '答案')
        compare_system.equal('點 (0, 0) 與 (2, 2)', '中點題目', "(1, 1)", '答案')