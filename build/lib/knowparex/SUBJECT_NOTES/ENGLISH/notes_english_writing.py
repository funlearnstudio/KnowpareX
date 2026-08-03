from knowparex.PROGRAMMING_NOTES import compare_system
class english_writing:
    @staticmethod
    def paragraph_structure():
        compare_system.definition("topic sentence", "段落", "主題句指出段落中心思想", "中文解釋")
        compare_system.definition("supporting sentence", "段落", "支持句提供理由、例子、證據或解釋", "中文解釋")
        compare_system.definition("concluding sentence", "段落", "結尾句總結段落或連接下一段", "中文解釋")
        compare_system.exampleof("Regular exercise improves both physical and mental health.", "英文例句", "可作健康主題段落的主題句", "中文解釋")
        compare_system.exampleof("For example, exercise can reduce stress and improve sleep quality.", "英文例句", "提供具體支持", "中文解釋")

    @staticmethod
    def introduction():
        compare_system.definition("hook", "作文開頭", "吸引讀者注意的第一句", "中文解釋")
        compare_system.definition("background information", "作文開頭", "提供理解主題所需的背景", "中文解釋")
        compare_system.definition("thesis statement", "作文開頭", "清楚表達全文主要立場或方向", "中文解釋")
        compare_system.exampleof("Technology has changed not only how we communicate but also how we learn.", "英文例句", "可作科技主題的開場句", "中文解釋")

    @staticmethod
    def body_paragraph():
        compare_system.definition("body paragraph", "作文主體", "每一段集中發展一個主要理由或觀點", "中文解釋")
        compare_system.requires("body paragraph", "作文主體", "topic sentence", "必要元素")
        compare_system.requires("body paragraph", "作文主體", "evidence or example", "必要元素")
        compare_system.requires("body paragraph", "作文主體", "explanation", "必要元素")
        compare_system.exampleof("One major benefit of public transportation is that it reduces traffic congestion.", "英文例句", "主體段主題句", "中文解釋")

    @staticmethod
    def conclusion():
        compare_system.definition("conclusion", "作文結尾", "重述主旨、整理重點並留下完整收束", "中文解釋")
        compare_system.exampleof("In conclusion, public transportation benefits both individuals and the environment.", "英文例句", "重述整體立場", "中文解釋")

    @staticmethod
    def opinion_essay():
        compare_system.definition("opinion essay", "作文類型", "清楚表達立場並用理由與證據支持", "中文解釋")
        compare_system.exampleof("I believe students should have more opportunities to choose their own projects.", "英文例句", "直接表達立場", "中文解釋")

    @staticmethod
    def narrative_essay():
        compare_system.definition("narrative essay", "作文類型", "以人物、事件、時間順序與細節敘述經驗或故事", "中文解釋")
        compare_system.exampleof("As I stepped onto the stage, my hands began to shake.", "英文例句", "以具體動作與感受開場", "中文解釋")

    @staticmethod
    def descriptive_essay():
        compare_system.definition("descriptive essay", "作文類型", "使用感官細節與精確詞語描寫人、地、物或經驗", "中文解釋")
        compare_system.exampleof("The narrow street smelled of fresh bread and echoed with bicycle bells.", "英文例句", "同時使用嗅覺與聽覺細節", "中文解釋")

    @staticmethod
    def compare_contrast_essay():
        compare_system.definition("compare-and-contrast essay", "作文類型", "分析兩個主題的相同與不同之處", "中文解釋")
        compare_system.exampleof("Both online and classroom learning can be effective, but they require different kinds of self-discipline.", "英文例句", "同時指出相同與差異", "中文解釋")

    @staticmethod
    def problem_solution_essay():
        compare_system.definition("problem-solution essay", "作文類型", "說明問題、分析原因或影響，並提出可行解決方法", "中文解釋")
        compare_system.exampleof("Food waste is a serious problem in many schools.", "英文例句", "提出問題", "中文解釋")
        compare_system.exampleof("Schools can reduce waste by offering smaller portions and allowing students to request more.", "英文例句", "提出具體解法", "中文解釋")

    @staticmethod
    def revision_checklist():
        compare_system.definition("revision", "寫作流程", "檢查內容、結構、邏輯與表達，而不只改拼字", "中文解釋")
        compare_system.requires("revision", "寫作流程", "clear thesis", "檢查項目")
        compare_system.requires("revision", "寫作流程", "logical organization", "檢查項目")
        compare_system.requires("revision", "寫作流程", "specific evidence", "檢查項目")
        compare_system.requires("revision", "寫作流程", "grammar and punctuation", "檢查項目")
