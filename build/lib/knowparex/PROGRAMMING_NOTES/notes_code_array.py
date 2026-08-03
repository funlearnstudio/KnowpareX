from knowparex.PROGRAMMING_NOTES import compare_system
class code_array:
    @staticmethod
    def normal_array():
        compare_system.codesimilarbutsyntaxsame("numbers := []int{3, 8, 2, 10, 5}","go","int numbers[] = {3, 8, 2, 10, 5};","c++")
        compare_system.codesimilarbutsyntaxsame("numbers := []int{3, 8, 2, 10, 5}", "go", "numbers = [3, 8, 2, 10, 5]","Python")
        compare_system.exactsame("len(numbers)","go","len(numbers)","Python")
    @staticmethod
    def vector():
        # 建立 vector
        compare_system.codesamebutsyntaxdifferent("vector<int> numbers;", "c++", "numbers = []", "Python")
        compare_system.codesamebutsyntaxdifferent("vector<int> numbers;", "c++", "numbers := []int{}", "go")

        # 初始化
        compare_system.codesimilarbutsyntaxsame("vector<int> numbers = {3, 8, 2, 10, 5};", "c++", "numbers := []int{3, 8, 2, 10, 5}", "go")
        compare_system.codesimilarbutsyntaxsame("vector<int> numbers = {3, 8, 2, 10, 5};", "c++", "numbers = [3, 8, 2, 10, 5]", "Python")

        # 長度
        compare_system.codesamebutsyntaxdifferent("numbers.size()", "c++", "len(numbers)", "Python")
        compare_system.codesamebutsyntaxdifferent("numbers.size()", "c++", "len(numbers)", "go")
        compare_system.codesamebutsyntaxdifferent("numbers.size()", "c++", "numbers.length", "JavaScript")

        # 新增元素
        compare_system.codesamebutsyntaxdifferent("numbers.push_back(x);", "c++", "numbers.append(x)", "Python")
        compare_system.codesamebutsyntaxdifferent("numbers.push_back(x);", "c++", "numbers = append(numbers, x)", "go")
        compare_system.codesamebutsyntaxdifferent("numbers.push_back(x);", "c++", "numbers.push(x)", "JavaScript")

        # 刪除最後一個
        compare_system.codesamebutsyntaxdifferent("numbers.pop_back();", "c++", "numbers.pop()", "Python")
        compare_system.codesamebutsyntaxdifferent("numbers.pop_back();", "c++", "numbers.pop()", "JavaScript")

        # 清空
        compare_system.codesamebutsyntaxdifferent("numbers.clear();", "c++", "numbers.clear()", "Python")
        compare_system.codesamebutsyntaxdifferent("numbers.clear();", "c++", "numbers = []", "Python")

        # 排序
        compare_system.codesamebutsyntaxdifferent("sort(numbers.begin(), numbers.end());", "c++", "numbers.sort()", "Python")
        compare_system.codesamebutsyntaxdifferent("sort(numbers.begin(), numbers.end());", "c++", "sort.Ints(numbers)", "go")
