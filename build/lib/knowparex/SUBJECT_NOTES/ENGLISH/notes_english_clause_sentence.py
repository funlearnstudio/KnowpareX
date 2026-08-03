from knowparex.PROGRAMMING_NOTES import compare_system
class english_clause_sentence:
    @staticmethod
    def simple_compound_complex():
        compare_system.definition("simple sentence", "句型", "簡單句：只有一個主要子句", "中文解釋")
        compare_system.definition("compound sentence", "句型", "合句：兩個獨立子句以連接詞或分號連接", "中文解釋")
        compare_system.definition("complex sentence", "句型", "複句：一個主要子句加至少一個從屬子句", "中文解釋")
        compare_system.exampleof("I finished my homework.", "英文例句", "簡單句", "中文解釋")
        compare_system.exampleof("I finished my homework, and I watched a movie.", "英文例句", "合句", "中文解釋")
        compare_system.exampleof("After I finished my homework, I watched a movie.", "英文例句", "複句", "中文解釋")

    @staticmethod
    def relative_clause():
        compare_system.definition("relative clause", "子句", "關係子句修飾前面的名詞", "中文解釋")
        compare_system.exampleof("The student who won the contest is my friend.", "英文例句", "who won the contest 修飾 student", "中文解釋")

    @staticmethod
    def noun_clause():
        compare_system.definition("noun clause", "子句", "名詞子句在句中作主詞、受詞或補語", "中文解釋")
        compare_system.exampleof("What he said surprised everyone.", "英文例句", "What he said 作主詞", "中文解釋")
        compare_system.exampleof("I believe that she is honest.", "英文例句", "that she is honest 作受詞", "中文解釋")

    @staticmethod
    def adverb_clause():
        compare_system.definition("adverb clause", "子句", "副詞子句修飾主要子句，表時間、原因、條件、讓步等", "中文解釋")
        compare_system.exampleof("Because it was raining, we stayed home.", "英文例句", "表示原因", "中文解釋")
        compare_system.exampleof("If you practice, you will improve.", "英文例句", "表示條件", "中文解釋")

    @staticmethod
    def conditionals():
        compare_system.definition("zero conditional", "條件句", "表示普遍事實或必然結果", "中文解釋")
        compare_system.definition("first conditional", "條件句", "表示未來可能發生的條件與結果", "中文解釋")
        compare_system.definition("second conditional", "條件句", "表示現在或未來不太可能、假設性的情況", "中文解釋")
        compare_system.definition("third conditional", "條件句", "表示與過去事實相反的假設", "中文解釋")
        compare_system.exampleof("If you heat ice, it melts.", "英文例句", "零條件句", "中文解釋")
        compare_system.exampleof("If it rains, we will stay home.", "英文例句", "第一條件句", "中文解釋")
        compare_system.exampleof("If I had more time, I would learn another language.", "英文例句", "第二條件句", "中文解釋")
        compare_system.exampleof("If I had studied harder, I would have passed.", "英文例句", "第三條件句", "中文解釋")

    @staticmethod
    def reported_speech():
        compare_system.definition("reported speech", "文法", "間接引語用自己的話轉述別人的話", "中文解釋")
        compare_system.exampleof("She said that she was tired.", "英文例句", "轉述他人的話", "中文解釋")

    @staticmethod
    def inversion():
        compare_system.definition("inversion", "句型", "倒裝句將助動詞或動詞移到主詞前以強調或配合特定結構", "中文解釋")
        compare_system.exampleof("Never have I seen such a beautiful view.", "英文例句", "否定副詞置首造成倒裝", "中文解釋")
