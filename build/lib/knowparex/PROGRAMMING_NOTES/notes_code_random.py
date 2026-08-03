from knowparex.PROGRAMMING_NOTES import compare_system
class code_random:
    @staticmethod
    def random():
        compare_system.codesamebutsyntaxdifferent("distribution(generator)", "c++", "random.randint(minimum, maximum)", "Python")
        compare_system.different("uniform_int_distribution<int> distribution(minimum, maximum);", "c++", "Math.random()", "JavaScript")