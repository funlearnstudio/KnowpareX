from knowparex.PROGRAMMING_NOTES import compare_system
class code_if:
    @staticmethod
    def ex_if():
        compare_system.codesimilarbutsyntaxsame("switch {case x >= y: fmt.Println()}","go","if (x >= y) { cout << \"...\" << endl; }","c++")
