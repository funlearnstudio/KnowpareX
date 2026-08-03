from knowparex.PROGRAMMING_NOTES import compare_system
class code_return:
    @staticmethod
    def ex_return():
        compare_system.exactsame("return true","go","return true","c++")
        compare_system.codesamebutsyntaxsimilar("return x;", "c++", "return x", "Python")
        compare_system.codesamebutsyntaxsimilar("return x;", "c++", "return x", "go")
        compare_system.codesamebutsyntaxsimilar("return x;", "c++", "return x;", "JavaScript")

