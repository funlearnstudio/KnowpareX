from knowparex.PROGRAMMING_NOTES import compare_system
class english_grammar:
    @staticmethod
    def parts_of_speech():
        compare_system.definition("noun", "詞性", "名詞：人、事、物、地點或概念的名稱", "中文解釋")
        compare_system.definition("verb", "詞性", "動詞：表示動作、狀態或存在", "中文解釋")
        compare_system.definition("adjective", "詞性", "形容詞：修飾名詞或代名詞", "中文解釋")
        compare_system.definition("adverb", "詞性", "副詞：修飾動詞、形容詞、副詞或整句", "中文解釋")
        compare_system.exampleof("The careful student answered quickly.", "英文例句", "careful 是形容詞，quickly 是副詞", "中文解釋")

    @staticmethod
    def subject_verb_agreement():
        compare_system.definition("Subject-verb agreement", "文法", "主詞與動詞在人稱和單複數上要一致", "中文解釋")
        compare_system.exampleof("She likes music.", "英文例句", "第三人稱單數主詞搭配 likes", "中文解釋")
        compare_system.exampleof("They like music.", "英文例句", "複數主詞搭配 like", "中文解釋")
        compare_system.exampleof("The list of names is on the desk.", "英文例句", "真正主詞是 list，因此使用 is", "中文解釋")

    @staticmethod
    def articles():
        compare_system.definition("a / an", "冠詞", "用於不特定的單數可數名詞", "中文解釋")
        compare_system.definition("the", "冠詞", "用於特定、已知或唯一的人事物", "中文解釋")
        compare_system.exampleof("I saw a dog in the park.", "英文例句", "第一次提到且不特定", "中文解釋")
        compare_system.exampleof("The dog followed me home.", "英文例句", "再次提到同一隻狗，因此使用 the", "中文解釋")

    @staticmethod
    def countable_uncountable():
        compare_system.definition("countable noun", "名詞", "可數名詞，可以直接計數並有單複數", "中文解釋")
        compare_system.definition("uncountable noun", "名詞", "不可數名詞，通常不能直接加數字或複數 s", "中文解釋")
        compare_system.exampleof("There are three books on the table.", "英文例句", "book 是可數名詞", "中文解釋")
        compare_system.exampleof("We need more information.", "英文例句", "information 是不可數名詞", "中文解釋")

    @staticmethod
    def pronouns():
        compare_system.definition("subject pronoun", "代名詞", "主格代名詞放在主詞位置", "中文解釋")
        compare_system.definition("object pronoun", "代名詞", "受格代名詞放在動詞或介系詞後", "中文解釋")
        compare_system.definition("possessive adjective", "代名詞", "所有格形容詞放在名詞前", "中文解釋")
        compare_system.exampleof("She gave me her notebook.", "英文例句", "She 是主格，me 是受格，her 是所有格形容詞", "中文解釋")

    @staticmethod
    def comparatives_superlatives():
        compare_system.definition("comparative", "文法", "比較級用來比較兩者", "中文解釋")
        compare_system.definition("superlative", "文法", "最高級用來比較三者以上", "中文解釋")
        compare_system.exampleof("This book is more useful than that one.", "英文例句", "more useful 是比較級", "中文解釋")
        compare_system.exampleof("She is the most careful student in the class.", "英文例句", "the most careful 是最高級", "中文解釋")

    @staticmethod
    def gerund_infinitive():
        compare_system.definition("gerund", "文法", "動名詞：V-ing 具有名詞功能", "中文解釋")
        compare_system.definition("infinitive", "文法", "不定詞：to + 原形動詞，可作名詞、形容詞或副詞", "中文解釋")
        compare_system.exampleof("Swimming is good exercise.", "英文例句", "Swimming 作主詞", "中文解釋")
        compare_system.exampleof("I hope to study abroad.", "英文例句", "to study 作 hope 的受詞", "中文解釋")

    @staticmethod
    def modals():
        compare_system.definition("modal verb", "文法", "情態動詞表示能力、可能、義務、建議或推測", "中文解釋")
        compare_system.exampleof("You should review your notes.", "英文例句", "should 表示建議", "中文解釋")
        compare_system.exampleof("He may be at home.", "英文例句", "may 表示可能性", "中文解釋")
        compare_system.exampleof("Students must follow the rules.", "英文例句", "must 表示強烈義務", "中文解釋")

    @staticmethod
    def prepositions():
        compare_system.definition("preposition", "文法", "介系詞表示時間、地點、方向、方式或關係", "中文解釋")
        compare_system.exampleof("The meeting starts at seven.", "英文例句", "at 用於明確時間點", "中文解釋")
        compare_system.exampleof("She lives in Taipei.", "英文例句", "in 用於城市或較大範圍", "中文解釋")
        compare_system.exampleof("The picture is on the wall.", "英文例句", "on 表示接觸表面", "中文解釋")
