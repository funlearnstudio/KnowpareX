from knowparex.PROGRAMMING_NOTES import compare_system
class code_class:
    @staticmethod
    def ex_class():
        # 最基本的空 class
        compare_system.codesamebutsyntaxdifferent("class Student {};", "c++", "class Student: pass", "Python")
        compare_system.codesamebutsyntaxsimilar("class Student {};", "c++", "class Student {}", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("class Student {};", "c++", "class Student {}", "TypeScript")

        # class 裡面放資料
        compare_system.codesamebutsyntaxdifferent("class Student { public: string name = \"Steve\"; };", "c++", "class Student:\n    name = \"Steve\"", "Python")
        compare_system.codesamebutsyntaxsimilar("class Student { public: string name = \"Steve\"; };", "c++", "class Student { name = \"Steve\"; }", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("class Student { public: string name = \"Steve\"; };", "c++", "class Student { name: string = \"Steve\"; }", "TypeScript")

        # Go 沒有 class 關鍵字，通常使用 struct 組織資料
        compare_system.codesimilarbutsyntaxdifferent("class Student { public: string name; };", "c++", "type Student struct { name string }", "Go")

    # ==================================================
    # class 的基本作用：
    # 把有關聯的資料與功能整理在同一個自訂型別裡。
    #
    # 這個檔案只記錄：
    # 1. class 的基本宣告
    # 2. class 裡面放資料
    #
    # 其他概念分開放：
    # constructor
    # destructor
    # static
    # object
    # inheritance
    # polymorphism
    # encapsulation
    # access modifier
    # ==================================================