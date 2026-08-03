from knowparex.PROGRAMMING_NOTES import compare_system
class code_math:
    @staticmethod
    def sqrt():
        compare_system.codesimilarbutsyntaxsame("math.Sqrt(x)","go","sqrt(x)","c++")
        compare_system.codesamebutsyntaxsimilar("sqrt(x)", "c++", "math.sqrt(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("sqrt(x)", "c++", "Math.sqrt(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("sqrt(x)", "c++", "math.Sqrt(x)", "go")
    @staticmethod
    def pow():
        compare_system.codesimilarbutsyntaxsame("math.Pow(x, y)","go","pow(x, y)","Python")
        compare_system.codesamebutsyntaxsimilar("pow(x, y)", "c++", "math.pow(x, y)", "Python")
        compare_system.codesamebutsyntaxsimilar("pow(x, y)", "c++", "Math.pow(x, y)", "TypeScript")
        compare_system.codesamebutsyntaxsimilar("pow(x, y)", "c++", "math.Pow(x, y)", "go")
    @staticmethod
    def random():
        compare_system.codesamebutsyntaxdifferent("distribution(generator)", "c++", "random.randint(minimum, maximum)", "Python")
        compare_system.different("uniform_int_distribution<int> distribution(minimum, maximum);", "c++", "Math.random()", "JavaScript")
    @staticmethod
    def abs():
        compare_system.exactsame("abs(x)", "c++", "abs(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("abs(x)", "c++", "Math.abs(x)", "JavaScript")
    @staticmethod
    def round():
        compare_system.codesamebutsyntaxsimilar("round(x)", "c++", "math.Round(x)", "go")

        compare_system.codesamebutsyntaxsimilar("round(x)", "c++", "round(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("round(x)", "c++", "Math.round(x)", "JavaScript")
    @staticmethod
    def floor():
        compare_system.codesamebutsyntaxsimilar("floor(x)", "c++", "math.floor(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("floor(x)", "c++", "Math.floor(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("floor(x)", "c++", "math.Floor(x)", "go")
    @staticmethod
    def ceil():
        compare_system.codesamebutsyntaxsimilar("ceil(x)", "c++", "Math.ceil(x)", "TypeScript")
        compare_system.codesamebutsyntaxsimilar("ceil(x)", "c++", "math.ceil(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("ceil(x)", "c++", "math.Ceil(x)", "go")
    @staticmethod
    def fmod():
        compare_system.codesamebutsyntaxsimilar("fmod(x, y)", "c++", "math.fmod(x, y)", "Python")
        compare_system.codesamebutsyntaxdifferent("fmod(x, y)", "c++", "x % y", "JavaScript")
    @staticmethod
    def max():
        compare_system.codesamebutsyntaxsimilar("max(a, b)", "c++", "max(a, b)", "Python")
        compare_system.codesamebutsyntaxsimilar("max(a, b)", "c++", "Math.max(a, b)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("max(a, b)", "c++", "math.Max(a, b)", "go")
    @staticmethod
    def min():
        compare_system.codesamebutsyntaxsimilar("min(a, b)", "c++", "min(a, b)", "Python")
        compare_system.codesamebutsyntaxsimilar("min(a, b)", "c++", "Math.min(a, b)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("min(a, b)", "c++", "math.Min(a, b)", "go")
    @staticmethod
    def sin():
        compare_system.codesamebutsyntaxsimilar("sin(x)", "c++", "math.sin(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("sin(x)", "c++", "Math.sin(x)", "JavaScript")
    @staticmethod
    def cos():
        compare_system.codesamebutsyntaxsimilar("cos(x)", "c++", "math.cos(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("cos(x)", "c++", "Math.cos(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("cos(x)", "c++", "math.Cos(x)", "go")
    @staticmethod
    def tan():
        compare_system.codesamebutsyntaxsimilar("tan(x)", "c++", "math.tan(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("tan(x)", "c++", "Math.tan(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("tan(x)", "c++", "math.Tan(x)", "go")
    @staticmethod
    def log():
        compare_system.codesamebutsyntaxsimilar("log(x)", "c++", "math.log(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("log(x)", "c++", "Math.log(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("log(x)", "c++", "math.Log(x)", "go")
    @staticmethod
    def log10():
        compare_system.codesamebutsyntaxsimilar("log10(x)", "c++", "Math.log10(x)", "JavaScript")

        compare_system.codesamebutsyntaxsimilar("log10(x)", "c++", "math.log10(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("log10(x)", "c++", "math.Log10(x)", "go")
    @staticmethod
    def exp():
        compare_system.codesamebutsyntaxsimilar("exp(x)", "c++", "math.exp(x)", "Python")
        compare_system.codesamebutsyntaxsimilar("exp(x)", "c++", "Math.exp(x)", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("exp(x)", "c++", "math.Exp(x)", "go")

    #| 功能    | C++ `<cmath>` | Python `math`               | JavaScript／TypeScript `Math` | Go `math`        |
    #| ----- | ------------- | --------------------------- | ---------------------------- | ---------------- |
    #| 平方根   | `sqrt(x)`     | `math.sqrt(x)`              | `Math.sqrt(x)`               | `math.Sqrt(x)`   |
    #| 次方    | `pow(x, y)`   | `math.pow(x, y)` 或 `x ** y` | `Math.pow(x, y)` 或 `x ** y`  | `math.Pow(x, y)` |
    #| 絕對值   | `abs(x)`      | `abs(x)`                    | `Math.abs(x)`                | `math.Abs(x)`    |
    #| 四捨五入  | `round(x)`    | `round(x)`                  | `Math.round(x)`              | `math.Round(x)`  |
    #| 向下取整  | `floor(x)`    | `math.floor(x)`             | `Math.floor(x)`              | `math.Floor(x)`  |
    #| 向上取整  | `ceil(x)`     | `math.ceil(x)`              | `Math.ceil(x)`               | `math.Ceil(x)`   |
    #| 浮點數餘數 | `fmod(x, y)`  | `math.fmod(x, y)`           | `x % y`                      | `math.Mod(x, y)` |
    #| 最大值   | `max(a, b)`   | `max(a, b)`                 | `Math.max(a, b)`             | `math.Max(a, b)` |
    #| 最小值   | `min(a, b)`   | `min(a, b)`                 | `Math.min(a, b)`             | `math.Min(a, b)` |
    #| 正弦    | `sin(x)`      | `math.sin(x)`               | `Math.sin(x)`                | `math.Sin(x)`    |
    #| 餘弦    | `cos(x)`      | `math.cos(x)`               | `Math.cos(x)`                | `math.Cos(x)`    |
    #| 正切    | `tan(x)`      | `math.tan(x)`               | `Math.tan(x)`                | `math.Tan(x)`    |
    #| 自然對數  | `log(x)`      | `math.log(x)`               | `Math.log(x)`                | `math.Log(x)`    |
    #| 常用對數  | `log10(x)`    | `math.log10(x)`             | `Math.log10(x)`              | `math.Log10(x)`  |
    #| 指數函式  | `exp(x)`      | `math.exp(x)`               | `Math.exp(x)`                | `math.Exp(x)`    |
