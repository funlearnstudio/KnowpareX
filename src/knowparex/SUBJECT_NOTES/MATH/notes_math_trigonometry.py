from knowparex.PROGRAMMING_NOTES import compare_system
class math_trigonometry:
    @staticmethod
    def basic_ratio():
        compare_system.equivalentto("sin(theta)", '三角比', '對邊 / 斜邊', '定義')
        compare_system.equivalentto("cos(theta)", '三角比', '鄰邊 / 斜邊', '定義')
        compare_system.equivalentto("tan(theta)", '三角比', '對邊 / 鄰邊', '定義')
        compare_system.equivalentto("tan(theta)", '乘法公式', "sin(theta) / cos(theta)", '結果')
        compare_system.equivalentto("sin^2(theta) + cos^2(theta)", '乘法公式', "1", '結果')

    @staticmethod
    def special_angles():
        compare_system.equal('sin(0 度)', '三角函數', "0", '答案')
        compare_system.equal('cos(0 度)', '三角函數', "1", '答案')
        compare_system.equal('sin(30 度)', '三角函數', "1/2", '答案')
        compare_system.equal('cos(60 度)', '三角函數', "1/2", '答案')
        compare_system.equal('tan(45 度)', '三角函數', "1", '答案')

    @staticmethod
    def degree_radian():
        compare_system.equivalentto('180 度', '角度', 'π 弧度', '弧度')
        compare_system.equivalentto('90 度', '角度', 'π/2 弧度', '弧度')
        compare_system.equivalentto('360 度', '角度', '2π 弧度', '弧度')
        compare_system.equivalentto('45 度', '角度', 'π/4 弧度', '弧度')
        compare_system.equivalentto('60 度', '角度', 'π/3 弧度', '弧度')