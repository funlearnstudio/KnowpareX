from knowparex.PROGRAMMING_NOTES import compare_system
class math_statistics:
    @staticmethod
    def mean():
        compare_system.calculatedby('平均數', '目標', '資料總和 / 資料個數', '公式')
        compare_system.equal('2、4、6 的平均數', '題目', "4", '答案')
        compare_system.equal('5、5、5 的平均數', '題目', "5", '答案')
        compare_system.equal('1、2、3、4 的平均數', '題目', "2.5", '答案')
        compare_system.equal('總和 = 40，個數 = 8', '題目', '平均數 = 5', '答案')

    @staticmethod
    def median():
        compare_system.equal('1、3、5 的中位數', '題目', "3", '答案')
        compare_system.equal('1、2、3、4 的中位數', '題目', "2.5", '答案')
        compare_system.equal('7、2、5 的中位數', '題目', "5", '答案')
        compare_system.equal('9 筆資料的中位數位置', '題目', '第 5 個數值', '答案')
        compare_system.equal('中位數', '定義', '排序後位於中間的數值', '意義')

    @staticmethod
    def mode():
        compare_system.equal('1、2、2、3 的眾數', '題目', "2", '答案')
        compare_system.equal('5、5、5、7 的眾數', '題目', "5", '答案')
        compare_system.equal('眾數', '定義', '出現次數最多的數值', '意義')
        compare_system.equal('1、1、2、2', '資料', '有兩個眾數', '性質')
        compare_system.equal('1、2、3', '資料', '沒有眾數', '性質')

    @staticmethod
    def range():
        compare_system.calculatedby('全距', '目標', '最大值 - 最小值', '公式')
        compare_system.equal('2、5、9 的全距', '題目', "7", '答案')
        compare_system.equal('4、4、4 的全距', '題目', "0", '答案')
        compare_system.equal('最大值 = 20，最小值 = 3', '題目', '全距 = 17', '答案')
        compare_system.equal('較大的全距', '統計', '資料分布較分散', '意義')