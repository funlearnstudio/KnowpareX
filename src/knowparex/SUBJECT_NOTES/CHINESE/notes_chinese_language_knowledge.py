from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_language_knowledge:
    @staticmethod
    def six_principles():
        compare_system.definition('六書', '文字學', '傳統分析漢字構形與運用的六種原則', '中文解釋')
        compare_system.partof('象形、指事、會意、形聲', '六書', '造字法', '類型')
        compare_system.partof('轉注、假借', '六書', '用字法', '類型')

    @staticmethod
    def pictograph():
        compare_system.definition('象形', '六書', '依物體外形描繪而造字', '中文解釋')
        compare_system.exampleof('日、月、山、木', '漢字', '象形字', '例子')

    @staticmethod
    def indicative():
        compare_system.definition('指事', '六書', '用抽象符號或在象形字上加符號表示概念', '中文解釋')
        compare_system.exampleof('上、下、本、末', '漢字', '指事字', '例子')

    @staticmethod
    def ideogram():
        compare_system.definition('會意', '六書', '組合兩個以上意符表達新意義', '中文解釋')
        compare_system.exampleof('休、明、林', '漢字', '會意字', '例子')

    @staticmethod
    def phonetic_compound():
        compare_system.definition('形聲', '六書', '由形符表示意義類別、聲符提示讀音', '中文解釋')
        compare_system.related('形符', '形聲字', '提示字義範圍', '功能')
        compare_system.related('聲符', '形聲字', '提示讀音', '功能')

    @staticmethod
    def mutual_explanation():
        compare_system.definition('轉注', '六書', '同源字之間互相解釋或轉化使用', '中文解釋')

    @staticmethod
    def phonetic_loan():
        compare_system.definition('假借', '六書', '借用已有同音或近音字表示另一詞義', '中文解釋')
        compare_system.exampleof('來', '漢字', '原義與借義分化的假借例', '例子')

    @staticmethod
    def radicals_components():
        compare_system.definition('部首', '文字工具', '字典中用來分類檢字的主要偏旁', '中文解釋')
        compare_system.definition('偏旁', '文字學', '漢字中可分析出的構字部件', '中文解釋')
        compare_system.related('部件位置', '識字', '可分左、右、上、下、內、外等', '關係')

    @staticmethod
    def character_form_sound_meaning():
        compare_system.definition('字形', '語文常識', '漢字的書寫形式', '中文解釋')
        compare_system.definition('字音', '語文常識', '漢字的讀音', '中文解釋')
        compare_system.definition('字義', '語文常識', '漢字在語境中的意義', '中文解釋')
        compare_system.requires('理解漢字', '閱讀能力', '結合字形、字音、字義與語境', '條件')

    @staticmethod
    def homophones():
        compare_system.definition('同音字', '語文常識', '讀音相同或相近但字形、字義不同的字', '中文解釋')
        compare_system.requires('辨別同音字', '寫作', '依上下文判斷正確字義與字形', '方法')

    @staticmethod
    def similar_characters():
        compare_system.definition('形近字', '語文常識', '字形相似但讀音或意義不同的字', '中文解釋')
        compare_system.requires('辨別形近字', '寫作', '比較部件、讀音與語境', '方法')

    @staticmethod
    def polyphonic_characters():
        compare_system.definition('破音字', '語文常識', '同一漢字因意義或用法不同而有不同讀音', '中文解釋')
        compare_system.requires('判斷破音字', '閱讀', '依詞義與語境選擇讀音', '方法')

    @staticmethod
    def traditional_characters():
        compare_system.definition('正體字', '文字系統', '臺灣教育與正式書寫主要使用的漢字字體', '中文解釋')
        compare_system.related('筆順', '書寫規範', '影響書寫正確與查字效率', '功能')

    @staticmethod
    def word():
        compare_system.definition('詞', '語法', '能獨立運用、具有意義的最小語言單位之一', '中文解釋')
        compare_system.typeof('單音詞', '詞', '由一個音節構成', '類型')
        compare_system.typeof('複音詞', '詞', '由兩個以上音節構成', '類型')

    @staticmethod
    def compound_words():
        compare_system.definition('複合詞', '構詞法', '由兩個以上語素組合而成的詞', '中文解釋')
        compare_system.typeof('聯合式', '複合詞', '語素意義並列', '類型')
        compare_system.typeof('偏正式', '複合詞', '前語素修飾後語素', '類型')
        compare_system.typeof('動賓式', '複合詞', '動作加受詞', '類型')
        compare_system.typeof('主謂式', '複合詞', '主體加陳述', '類型')

    @staticmethod
    def parts_of_speech():
        compare_system.definition('詞類', '語法', '依詞在句中的功能與意義分類', '中文解釋')
        compare_system.partof('名詞、動詞、形容詞', '實詞', '詞類', '內容')
        compare_system.partof('副詞、介詞、連詞、助詞、嘆詞', '虛詞與功能詞', '詞類', '內容')

    @staticmethod
    def noun():
        compare_system.definition('名詞', '詞類', '表示人、事、物、地點、時間或抽象概念', '中文解釋')
        compare_system.exampleof('學生、臺北、友誼', '詞語', '名詞', '例子')

    @staticmethod
    def verb():
        compare_system.definition('動詞', '詞類', '表示動作、變化、存在或判斷', '中文解釋')
        compare_system.exampleof('跑、成長、存在、是', '詞語', '動詞', '例子')

    @staticmethod
    def adjective():
        compare_system.definition('形容詞', '詞類', '表示性質、狀態或特徵', '中文解釋')
        compare_system.exampleof('美麗、安靜、清楚', '詞語', '形容詞', '例子')

    @staticmethod
    def adverb():
        compare_system.definition('副詞', '詞類', '修飾動詞、形容詞或整句，表示程度、時間、範圍、否定等', '中文解釋')
        compare_system.exampleof('很、已經、都、不', '詞語', '副詞', '例子')

    @staticmethod
    def pronoun():
        compare_system.definition('代詞', '詞類', '代替人、事、物、處所、數量或情況', '中文解釋')
        compare_system.exampleof('我、你、他、這、那、誰', '詞語', '代詞', '例子')

    @staticmethod
    def preposition():
        compare_system.definition('介詞', '詞類', '引介時間、處所、對象、方式等關係', '中文解釋')
        compare_system.exampleof('在、從、對、把、被', '詞語', '介詞', '例子')

    @staticmethod
    def conjunction():
        compare_system.definition('連詞', '詞類', '連接詞、短語、分句或句子', '中文解釋')
        compare_system.exampleof('和、但是、因為、所以', '詞語', '連詞', '例子')

    @staticmethod
    def particle():
        compare_system.definition('助詞', '詞類', '附著於詞語或句子，表示結構、語氣或時態等功能', '中文解釋')
        compare_system.exampleof('的、地、得、了、著、過', '詞語', '助詞', '例子')

    @staticmethod
    def interjection():
        compare_system.definition('嘆詞', '詞類', '表示感嘆、呼喚或應答', '中文解釋')
        compare_system.exampleof('啊、唉、喂', '詞語', '嘆詞', '例子')

    @staticmethod
    def sentence_components():
        compare_system.definition('句子成分', '語法', '句中各部分所擔任的功能', '中文解釋')
        compare_system.partof('主語', '句子成分', '句子', '內容')
        compare_system.partof('謂語', '句子成分', '句子', '內容')
        compare_system.partof('賓語', '句子成分', '句子', '內容')
        compare_system.partof('定語、狀語、補語', '句子成分', '句子', '內容')

    @staticmethod
    def subject_predicate():
        compare_system.definition('主語', '句子成分', '被陳述的人或事物', '中文解釋')
        compare_system.definition('謂語', '句子成分', '對主語加以說明或陳述', '中文解釋')

    @staticmethod
    def object():
        compare_system.definition('賓語', '句子成分', '動詞所支配或涉及的對象', '中文解釋')

    @staticmethod
    def modifier():
        compare_system.definition('定語', '句子成分', '修飾名詞性中心語', '中文解釋')
        compare_system.definition('狀語', '句子成分', '修飾動詞、形容詞或整個謂語', '中文解釋')
        compare_system.definition('補語', '句子成分', '補充說明動作或狀態的結果、程度、方向等', '中文解釋')

    @staticmethod
    def basic_sentence_patterns():
        compare_system.definition('基本句型', '語法', '依主要句子成分與謂語性質分類的句型', '中文解釋')
        compare_system.typeof('敘事句', '基本句型', '主語加動詞性謂語', '類型')
        compare_system.typeof('有無句', '基本句型', '表示存在或領有', '類型')
        compare_system.typeof('表態句', '基本句型', '主語加形容詞性謂語', '類型')
        compare_system.typeof('判斷句', '基本句型', '用判斷詞連接主語與賓語', '類型')

    @staticmethod
    def compound_sentence():
        compare_system.definition('複句', '語法', '由兩個以上意義相關的分句構成', '中文解釋')
        compare_system.typeof('並列複句', '複句', '分句關係並列', '類型')
        compare_system.typeof('因果複句', '複句', '分句具有原因與結果', '類型')
        compare_system.typeof('轉折複句', '複句', '後句意思與前句預期相反', '類型')
        compare_system.typeof('條件複句', '複句', '表示條件與結果', '類型')

    @staticmethod
    def punctuation():
        compare_system.definition('標點符號', '書面語', '表示停頓、語氣、層次與句法關係的符號', '中文解釋')
        compare_system.related('句號、問號、驚嘆號', '標點符號', '句末標點', '類型')
        compare_system.related('逗號、頓號、分號', '標點符號', '句中停頓', '類型')
        compare_system.related('冒號、引號、括號、破折號', '標點符號', '說明與標示', '類型')

    @staticmethod
    def comma():
        compare_system.definition('逗號', '標點符號', '表示句中一般停頓', '中文解釋')

    @staticmethod
    def enumeration_comma():
        compare_system.definition('頓號', '標點符號', '表示並列詞語間較短停頓', '中文解釋')

    @staticmethod
    def semicolon():
        compare_system.definition('分號', '標點符號', '表示並列分句間較大停頓', '中文解釋')

    @staticmethod
    def colon():
        compare_system.definition('冒號', '標點符號', '提示下文、說明或引語', '中文解釋')

    @staticmethod
    def quotation_marks():
        compare_system.definition('引號', '標點符號', '標示直接引語、特殊用語或需要強調的詞語', '中文解釋')

    @staticmethod
    def dash():
        compare_system.definition('破折號', '標點符號', '表示解釋、轉折、延長或語意中斷', '中文解釋')

    @staticmethod
    def ellipsis():
        compare_system.definition('刪節號', '標點符號', '表示語句省略、聲音延長或意思未盡', '中文解釋')

    @staticmethod
    def book_title_marks():
        compare_system.definition('書名號', '標點符號', '標示書籍、篇章、報刊、影劇等作品名稱', '中文解釋')

    @staticmethod
    def idiom():
        compare_system.definition('成語', '語文常識', '形式固定、意義完整且常有典故的熟語', '中文解釋')
        compare_system.requires('正確使用成語', '寫作', '理解字面、典故、感情色彩與適用對象', '條件')

    @staticmethod
    def proverb():
        compare_system.definition('諺語', '民間語言', '群眾長期流傳、表達生活經驗或道理的固定語句', '中文解釋')

    @staticmethod
    def common_saying():
        compare_system.definition('俗語', '民間語言', '通俗且廣泛使用的固定說法', '中文解釋')

    @staticmethod
    def xiehouyu():
        compare_system.definition('歇後語', '民間語言', '前半像謎面、後半說明含義的俏皮語句', '中文解釋')

    @staticmethod
    def couplet():
        compare_system.definition('對聯', '應用語文', '上下聯字數相等、詞性相對、意義相關的文體', '中文解釋')
        compare_system.requires('對聯', '形式', '字數相等、平仄協調、對仗工整', '條件')

    @staticmethod
    def letter_format():
        compare_system.definition('書信', '應用文', '個人或團體傳遞訊息、情感與意見的文體', '中文解釋')
        compare_system.partof('稱謂', '書信格式', '書信', '內容')
        compare_system.partof('正文', '書信格式', '書信', '內容')
        compare_system.partof('祝頌語', '書信格式', '書信', '內容')
        compare_system.partof('署名與日期', '書信格式', '書信', '內容')

    @staticmethod
    def notice():
        compare_system.definition('啟事', '應用文', '向公眾說明事項或請求協助的文字', '中文解釋')
        compare_system.requires('啟事', '寫作', '目的清楚、資訊完整、格式適當', '條件')

    @staticmethod
    def invitation():
        compare_system.definition('柬帖', '應用文', '邀請他人參與活動的正式文字', '中文解釋')
        compare_system.related('時間、地點、事由', '柬帖', '必要資訊', '內容')

    @staticmethod
    def title_honorifics():
        compare_system.definition('稱謂', '語文常識', '依身分、關係與場合使用的稱呼', '中文解釋')
        compare_system.related('謙稱', '稱謂', '對自己或己方表示謙遜', '類型')
        compare_system.related('敬稱', '稱謂', '對他人或對方表示尊敬', '類型')

    @staticmethod
    def age_terms():
        compare_system.definition('年齡代稱', '文化常識', '以特定詞語指稱不同年齡階段', '中文解釋')
        compare_system.related('總角', '年齡代稱', '童年', '意義')
        compare_system.related('弱冠', '年齡代稱', '男子二十歲左右', '意義')
        compare_system.related('而立、不惑、知命', '年齡代稱', '三十、四十、五十歲', '意義')

    @staticmethod
    def seasons_months():
        compare_system.definition('季節與月份代稱', '文化常識', '古典作品中常以節氣、花木或干支表示時間', '中文解釋')
        compare_system.requires('判讀時間代稱', '閱讀', '結合節氣、物候與文化背景', '方法')

    @staticmethod
    def heavenly_stems_earthly_branches():
        compare_system.definition('天干地支', '傳統文化', '十天干與十二地支組合紀年、紀月、紀日、紀時', '中文解釋')
        compare_system.partof('甲乙丙丁戊己庚辛壬癸', '天干', '天干地支', '內容')
        compare_system.partof('子丑寅卯辰巳午未申酉戌亥', '地支', '天干地支', '內容')
