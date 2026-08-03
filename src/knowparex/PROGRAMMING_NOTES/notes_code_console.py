from knowparex.PROGRAMMING_NOTES import compare_system
class code_console:
    @staticmethod
    def print():
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "print(\"hello\")", "Python")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "fmt.Println(\"hello\")", "Go")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "console.log(\"hello\")", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "console.log(\"hello\")", "TypeScript")
