from knowparex.PROGRAMMING_NOTES import compare_system
class code_type:
    @staticmethod
    def bool():
        compare_system.exactsame("bool","go","bool","c++")
        compare_system.codesamebutsyntaxsimilar("bool", "c++", "bool", "go")
        compare_system.codesamebutsyntaxsimilar("bool", "c++", "boolean", "TypeScript")
    @staticmethod
    def int():
        compare_system.codesimilarbutsyntaxsame("isAdult(age)","go","isAdult(int age)","c++")
        compare_system.codesimilarbutsyntaxsame("numbers []int","go","int numbers","c++")
        compare_system.codesimilarbutsyntaxsame("numbers []int","go","numbers","py")
    @staticmethod
    def auto():
        compare_system.codesimilarbutsyntaxsame("biggest := numbers[0]","go","auto biggest = numbers[0];","c++")
        compare_system.codesimilarbutsyntaxsame("biggest := numbers[0]","go","biggest = numbers[0]","Python")
    @staticmethod
    def string():
        compare_system.codesamebutsyntaxsimilar("string", "c++", "str", "Python")
        compare_system.codesamebutsyntaxsimilar("string", "c++", "string", "TypeScript")
    @staticmethod
    def double():
        compare_system.codesamebutsyntaxsimilar("double", "c++", "float", "Python")
        compare_system.codesamebutsyntaxsimilar("double", "c++", "number", "TypeScript")
    @staticmethod
    def float():
        compare_system.codesamebutsyntaxsimilar("float", "c++", "float", "Python")
    @staticmethod
    def char():
        compare_system.codesamebutsyntaxsimilar("char", "c++", "str", "Python")
        compare_system.codesamebutsyntaxsimilar("char", "c++", "string", "TypeScript")
    #| 名稱       | 用途           | 範例                       |
    #| -------- | ------------ | ------------------------ |
    #| `int`    | 整數           | `int age = 15;`          |
    #| `double` | 小數           | `double pi = 3.14;`      |
    #| `float`  | 小數（精度較低）     | `float x = 1.5f;`        |
    #| `char`   | 一個字元         | `char c = 'A';`          |
    #| `bool`   | true / false | `bool pass = true;`      |
    #| `string` | 一整串文字        | `string name = "Steve";` |
