from knowparex.PROGRAMMING_NOTES import compare_system
class code_function:
    @staticmethod
    def void():
        compare_system.codesamebutsyntaxsimilar("void hello()", "c++", "func hello()", "go")
        compare_system.codesamebutsyntaxdifferent("void hello()", "c++", "def hello():", "Python")
        compare_system.codesamebutsyntaxdifferent("void hello()", "c++", "function hello() {}", "JavaScript")
        compare_system.codesamebutsyntaxdifferent("void hello()", "c++", "function hello(): void {}", "TypeScript")

    @staticmethod
    def int():
        compare_system.codesamebutsyntaxsimilar("int add(int a, int b) { return a + b; }", "c++", "func add(a int, b int) int { return a + b }", "go")
        compare_system.codesamebutsyntaxdifferent("int add(int a, int b) { return a + b; }", "c++", "def add(a, b): return a + b", "Python")
        compare_system.codesamebutsyntaxsimilar("int add(int a, int b) { return a + b; }", "c++", "function add(a: number, b: number): number { return a + b; }", "TypeScript")

    @staticmethod
    def bool():
        compare_system.codesamebutsyntaxsimilar("bool isAdult(int age) { return age >= 18; }", "c++", "func isAdult(age int) bool { return age >= 18 }", "go")
        compare_system.codesamebutsyntaxdifferent("bool isAdult(int age) { return age >= 18; }", "c++", "def is_adult(age): return age >= 18", "Python")
        compare_system.codesamebutsyntaxsimilar("bool isAdult(int age) { return age >= 18; }", "c++", "function isAdult(age: number): boolean { return age >= 18; }", "TypeScript")

    @staticmethod
    def auto():
        compare_system.codesamebutsyntaxsimilar("auto add(int a, int b) { return a + b; }", "c++", "function add(a, b) { return a + b; }", "JavaScript")
        compare_system.codesamebutsyntaxdifferent("auto add(int a, int b) { return a + b; }", "c++", "def add(a, b): return a + b", "Python")

    @staticmethod
    def string():
        compare_system.codesamebutsyntaxsimilar("string greet(string name) { return \"Hello, \" + name; }", "c++", "function greet(name: string): string { return \"Hello, \" + name; }", "TypeScript")
        compare_system.codesamebutsyntaxdifferent("string greet(string name) { return \"Hello, \" + name; }", "c++", "def greet(name): return \"Hello, \" + name", "Python")
        compare_system.codesamebutsyntaxsimilar("string greet(string name) { return \"Hello, \" + name; }", "c++", "func greet(name string) string { return \"Hello, \" + name }", "go")

    @staticmethod
    def double():
        compare_system.codesamebutsyntaxsimilar("double divide(double a, double b) { return a / b; }", "c++", "function divide(a: number, b: number): number { return a / b; }", "TypeScript")
        compare_system.codesamebutsyntaxdifferent("double divide(double a, double b) { return a / b; }", "c++", "def divide(a, b): return a / b", "Python")

    @staticmethod
    def float():
        compare_system.codesamebutsyntaxsimilar("float half(float x) { return x / 2.0f; }", "c++", "func half(x float32) float32 { return x / 2 }", "go")
        compare_system.codesamebutsyntaxdifferent("float half(float x) { return x / 2.0f; }", "c++", "def half(x): return x / 2", "Python")

    @staticmethod
    def char():
        compare_system.codesamebutsyntaxsimilar("char getGrade() { return 'A'; }", "c++", "function getGrade(): string { return 'A'; }", "TypeScript")
        compare_system.codesamebutsyntaxdifferent("char getGrade() { return 'A'; }", "c++", "def get_grade(): return 'A'", "Python")
        compare_system.codesamebutsyntaxsimilar("char getGrade() { return 'A'; }", "c++", "func getGrade() rune { return 'A' }", "go")
    #| 回傳型別   | 用途                     | 函式範例                                  |
    #| -------- | ------------------------ | ----------------------------------------- |
    #| `void`   | 不回傳任何值               | `void hello() { cout << "Hello"; }`       |
    #| `int`    | 回傳整數                   | `int getAge() { return 15; }`              |
    #| `double` | 回傳較高精度小數            | `double getPi() { return 3.14159; }`       |
    #| `float`  | 回傳較低精度小數            | `float getHalf() { return 0.5f; }`         |
    #| `char`   | 回傳單一字元                | `char getGrade() { return 'A'; }`          |
    #| `bool`   | 回傳 true 或 false         | `bool isAdult() { return false; }`         |
    #| `string` | 回傳一整串文字              | `string getName() { return "Steve"; }`     |
    #| `auto`   | 讓編譯器推斷回傳型別         | `auto add(int a, int b) { return a + b; }` |
