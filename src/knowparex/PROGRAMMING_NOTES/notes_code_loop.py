from knowparex.PROGRAMMING_NOTES import compare_system
class code_loop:

    @staticmethod
    def loop_for():
        compare_system.codesimilarbutsyntaxdifferent("for i := 0; i < len(numbers); i++ {","go","for (int i = 0; i < numbers.size(); i++) {","c++")
        compare_system.codesimilarbutsyntaxdifferent("for i := 0; i < len(numbers); i++ {","go","for i in range(len(numbers)):", "Python")
    @staticmethod
    def loop_while():
        compare_system.nothing()
    @staticmethod
    def loop_do():
        compare_system.nothing()
    # for(...){
    # }

    # while(...){
    # }

    # do{
    # }
    # while(...);