from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_classical:
    @staticmethod
    def classical_overview():
        compare_system.definition('文言文', '古典語文', '以古代漢語書面語寫成的文章', '中文解釋')
        compare_system.requires('閱讀文言文', '閱讀能力', '字詞理解、句法判斷、語境推論與文化背景', '條件')

    @staticmethod
    def content_words():
        compare_system.definition('實詞', '文言語法', '具有實際詞彙意義的名詞、動詞、形容詞等', '中文解釋')
        compare_system.related('一詞多義', '文言實詞', '同一字在不同語境有不同意義', '現象')

    @staticmethod
    def function_words():
        compare_system.definition('虛詞', '文言語法', '主要表示語法關係或語氣的詞', '中文解釋')
        compare_system.exampleof('之、其、而、以、於、乃、則、者、也、焉', '詞語', '常見文言虛詞', '例子')

    @staticmethod
    def polysemy():
        compare_system.definition('一詞多義', '文言閱讀', '同一字詞因語境不同具有多種意義', '中文解釋')
        compare_system.requires('判斷一詞多義', '閱讀', '依句法位置、搭配與上下文', '方法')

    @staticmethod
    def ancient_modern_meaning():
        compare_system.definition('古今異義', '文言閱讀', '同一詞古代意義與現代意義不同', '中文解釋')
        compare_system.requires('辨別古今異義', '翻譯', '避免直接套用現代詞義', '方法')

    @staticmethod
    def tongjia():
        compare_system.definition('通假字', '文言閱讀', '古書中借用同音或近音字代替本字', '中文解釋')
        compare_system.requires('判斷通假字', '閱讀', '結合語意、古注與固定用法', '方法')

    @staticmethod
    def word_class_conversion():
        compare_system.definition('詞類活用', '文言語法', '詞在特定語境中臨時改變原有詞性或功能', '中文解釋')
        compare_system.typeof('名詞作動詞', '詞類活用', '名詞具有動作意義', '類型')
        compare_system.typeof('名詞作狀語', '詞類活用', '名詞修飾動詞', '類型')
        compare_system.typeof('使動用法', '詞類活用', '使賓語產生某動作或狀態', '類型')
        compare_system.typeof('意動用法', '詞類活用', '主觀認為賓語具有某性質', '類型')

    @staticmethod
    def noun_as_verb():
        compare_system.definition('名詞作動詞', '詞類活用', '名詞在句中具有動詞功能', '中文解釋')

    @staticmethod
    def noun_as_adverbial():
        compare_system.definition('名詞作狀語', '詞類活用', '名詞直接修飾動詞，表示方式、工具、方向或處所', '中文解釋')

    @staticmethod
    def causative_usage():
        compare_system.definition('使動用法', '詞類活用', '使賓語發生某動作或成為某狀態', '中文解釋')

    @staticmethod
    def intentional_usage():
        compare_system.definition('意動用法', '詞類活用', '主語主觀認為賓語具有某性質', '中文解釋')

    @staticmethod
    def judgment_sentence():
        compare_system.definition('判斷句', '文言句式', '表示主語與賓語之間判斷關係', '中文解釋')
        compare_system.related('者……也', '判斷句', '常見格式', '形式')

    @staticmethod
    def passive_sentence():
        compare_system.definition('被動句', '文言句式', '主語是動作承受者', '中文解釋')
        compare_system.related('為……所……', '被動句', '常見格式', '形式')
        compare_system.related('見、被、於', '被動句', '常見標誌', '形式')

    @staticmethod
    def inversion_sentence():
        compare_system.definition('倒裝句', '文言句式', '句子成分順序與現代漢語常態不同', '中文解釋')
        compare_system.typeof('賓語前置', '倒裝句', '賓語移到動詞前', '類型')
        compare_system.typeof('介賓後置', '倒裝句', '介詞結構置於謂語後', '類型')
        compare_system.typeof('定語後置', '倒裝句', '修飾語置於中心詞後', '類型')

    @staticmethod
    def ellipsis_sentence():
        compare_system.definition('省略句', '文言句式', '省略可由語境推知的主語、賓語、介詞等', '中文解釋')
        compare_system.requires('翻譯省略句', '翻譯', '依語境補出必要成分', '方法')

    @staticmethod
    def fixed_structures():
        compare_system.definition('固定句式', '文言語法', '具有固定形式與穩定意義的語法結構', '中文解釋')
        compare_system.exampleof('何……之有', '固定句式', '有什麼……呢', '意義')
        compare_system.exampleof('不亦……乎', '固定句式', '不是也……嗎', '意義')
        compare_system.exampleof('孰與', '固定句式', '與……相比誰更……', '意義')

    @staticmethod
    def zhi():
        compare_system.definition('之', '文言虛詞', '可作代詞、助詞或動詞', '中文解釋')
        compare_system.related('代詞', '之', '代替人事物', '用法')
        compare_system.related('結構助詞', '之', '相當於現代漢語的『的』', '用法')
        compare_system.related('取消句子獨立性', '之', '用於主謂之間', '用法')
        compare_system.related('往、到', '之', '作動詞', '用法')

    @staticmethod
    def qi():
        compare_system.definition('其', '文言虛詞', '可作代詞、副詞或語氣詞', '中文解釋')
        compare_system.related('他的、它的', '其', '代詞用法', '意義')
        compare_system.related('大概、恐怕', '其', '推測語氣', '意義')
        compare_system.related('難道', '其', '反問語氣', '意義')

    @staticmethod
    def er():
        compare_system.definition('而', '文言虛詞', '常作連詞，表示並列、承接、轉折、修飾等關係', '中文解釋')
        compare_system.related('並列', '而', '又、並且', '意義')
        compare_system.related('轉折', '而', '但是、卻', '意義')
        compare_system.related('修飾', '而', '連接狀語與中心語', '用法')

    @staticmethod
    def yi():
        compare_system.definition('以', '文言虛詞', '可作介詞、連詞或動詞', '中文解釋')
        compare_system.related('用、拿', '以', '介詞用法', '意義')
        compare_system.related('因為', '以', '介詞或連詞用法', '意義')
        compare_system.related('來、用來', '以', '目的關係', '意義')
        compare_system.related('認為', '以', '動詞用法', '意義')

    @staticmethod
    def yu():
        compare_system.definition('於', '文言虛詞', '介詞，可表示處所、時間、對象、比較、被動等', '中文解釋')
        compare_system.related('在、從、到', '於', '處所或時間', '意義')
        compare_system.related('比', '於', '比較', '意義')
        compare_system.related('被', '於', '被動', '意義')

    @staticmethod
    def nai():
        compare_system.definition('乃', '文言虛詞', '可作副詞或代詞，表示才、竟然、就是等', '中文解釋')

    @staticmethod
    def ze():
        compare_system.definition('則', '文言虛詞', '可表示承接、判斷、轉折或條件結果', '中文解釋')

    @staticmethod
    def zhe_ye():
        compare_system.definition('者', '文言虛詞', '可表人事物、停頓或判斷結構', '中文解釋')
        compare_system.definition('也', '文言虛詞', '常表判斷、陳述、疑問或感嘆語氣', '中文解釋')

    @staticmethod
    def yan():
        compare_system.definition('焉', '文言虛詞', '可兼有代詞、介詞與語氣詞功能', '中文解釋')
        compare_system.related('於之', '焉', '常見合音意義', '意義')

    @staticmethod
    def he():
        compare_system.definition('何', '文言疑問詞', '可表示什麼、為什麼、怎麼', '中文解釋')

    @staticmethod
    def hu():
        compare_system.definition('乎', '文言虛詞', '可作語氣詞或介詞', '中文解釋')
        compare_system.related('嗎、呢', '乎', '疑問語氣', '意義')
        compare_system.related('於', '乎', '介詞用法', '意義')

    @staticmethod
    def translation_principles():
        compare_system.definition('信達雅', '翻譯原則', '忠實、通順並兼顧文字品質', '中文解釋')
        compare_system.requires('文言翻譯', '方法', '直譯為主、意譯為輔，補省略、調語序', '條件')

    @staticmethod
    def literal_translation():
        compare_system.definition('直譯', '翻譯方法', '盡量依原文字詞與句法翻譯', '中文解釋')

    @staticmethod
    def free_translation():
        compare_system.definition('意譯', '翻譯方法', '在忠於原意下調整表達，使現代語句自然', '中文解釋')

    @staticmethod
    def translation_steps():
        compare_system.requires('文言翻譯', '步驟', '辨字義、判句式、補省略、調語序、順語意', '方法')

    @staticmethod
    def classical_reading_context():
        compare_system.requires('文言閱讀', '背景', '理解作者、時代、文體與篇章脈絡', '條件')

    @staticmethod
    def classical_argument():
        compare_system.definition('文言議論', '古文閱讀', '以論點、理由、例證與反駁說理', '中文解釋')
        compare_system.requires('分析文言議論', '閱讀', '找論點、論據與論證方式', '方法')

    @staticmethod
    def classical_narrative():
        compare_system.definition('文言敘事', '古文閱讀', '以人物、事件與因果組織故事', '中文解釋')
        compare_system.requires('分析文言敘事', '閱讀', '掌握人物動機、事件順序與轉折', '方法')

    @staticmethod
    def classical_lyric():
        compare_system.definition('文言抒情', '古文閱讀', '透過景物、事件或議論寄託情感', '中文解釋')

    @staticmethod
    def classical_poetry_image():
        compare_system.definition('古典詩歌意象', '詩歌閱讀', '反覆出現並承載文化情感的景物或事物', '中文解釋')
        compare_system.exampleof('月', '意象', '思鄉、團圓或孤寂', '常見意義')
        compare_system.exampleof('柳', '意象', '送別與留戀', '常見意義')
        compare_system.exampleof('雁', '意象', '思鄉、書信與漂泊', '常見意義')

    @staticmethod
    def poetry_scene_emotion():
        compare_system.requires('古典詩歌閱讀', '方法', '理解景物、情感、意象、聲律與用典', '條件')

    @staticmethod
    def poetry_structure():
        compare_system.related('起承轉合', '古典詩歌', '常見章法', '關係')
        compare_system.related('情景交融', '古典詩歌', '常見表現方式', '關係')

    @staticmethod
    def classical_culture():
        compare_system.definition('文化語境', '文言閱讀', '典章制度、禮俗、官職、地名與思想背景', '中文解釋')
        compare_system.requires('理解文化語境', '閱讀', '避免以現代觀念直接套用古代文本', '條件')

    @staticmethod
    def official_titles():
        compare_system.definition('官職名', '文化常識', '古代行政、軍事與禮制職位名稱', '中文解釋')
        compare_system.requires('判讀官職', '文言閱讀', '結合朝代制度與上下文', '方法')

    @staticmethod
    def classical_names():
        compare_system.definition('名、字、號', '文化常識', '古人可能同時具有本名、表字與別號', '中文解釋')
        compare_system.related('表字', '古代稱謂', '成年後用於社交', '功能')
        compare_system.related('別號', '古代稱謂', '個人自取或他人所稱', '功能')
