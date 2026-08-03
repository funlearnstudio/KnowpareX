from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_rhetoric:
    @staticmethod
    def rhetoric_overview():
        compare_system.definition('修辭', '語文表達', '為增強表達效果而安排語言的方法', '中文解釋')
        compare_system.related('語境', '修辭判斷', '同一語句須放回上下文判斷', '重要原則')

    @staticmethod
    def simile():
        compare_system.definition('明喻', '譬喻', '本體、喻體與喻詞都明確出現', '中文解釋')
        compare_system.exampleof('她的笑容像春天的陽光。', '例句', '明喻', '修辭')

    @staticmethod
    def metaphor():
        compare_system.definition('暗喻', '譬喻', '不用像、如等喻詞，直接以喻體說明本體', '中文解釋')
        compare_system.exampleof('時間是一條不停流動的河。', '例句', '暗喻', '修辭')

    @staticmethod
    def metonymic_metaphor():
        compare_system.definition('略喻', '譬喻', '省略本體，只留下喻體', '中文解釋')
        compare_system.exampleof('黑夜裡亮起了一盞明燈。', '例句', '略喻', '修辭')

    @staticmethod
    def metonymy():
        compare_system.definition('借代', '修辭', '不直接說本體，借與其密切相關的事物代替', '中文解釋')
        compare_system.exampleof('紅顏易老。', '例句', '以紅顏借代美麗女子', '中文解釋')

    @staticmethod
    def personification():
        compare_system.definition('擬人', '轉化', '把非人事物寫成人的動作、情感或性格', '中文解釋')
        compare_system.exampleof('風在窗外低聲歌唱。', '例句', '擬人', '修辭')

    @staticmethod
    def objectification():
        compare_system.definition('擬物', '轉化', '把人寫成物或把一物寫成另一物', '中文解釋')
        compare_system.exampleof('他在壓力下縮成一粒沉默的石頭。', '例句', '擬物', '修辭')

    @staticmethod
    def hyperbole():
        compare_system.definition('誇飾', '修辭', '故意誇大或縮小事物以加深印象', '中文解釋')
        compare_system.exampleof('我等你等了一萬年。', '例句', '誇飾', '修辭')

    @staticmethod
    def parallelism():
        compare_system.definition('排比', '修辭', '連續使用三個以上結構相似、語意相關的語句', '中文解釋')
        compare_system.exampleof('我們要學會思考，學會判斷，學會行動。', '例句', '排比', '修辭')

    @staticmethod
    def antithesis():
        compare_system.definition('對偶', '修辭', '上下兩句字數相等、結構相似、詞性相對', '中文解釋')
        compare_system.exampleof('海內存知己，天涯若比鄰。', '例句', '對偶', '修辭')

    @staticmethod
    def contrast():
        compare_system.definition('映襯', '修辭', '把相反或相對事物放在一起互相凸顯', '中文解釋')
        compare_system.exampleof('四周越安靜，心中的聲音越清楚。', '例句', '映襯', '修辭')

    @staticmethod
    def positive_contrast():
        compare_system.definition('正襯', '映襯', '以相近事物互相陪襯、加強效果', '中文解釋')

    @staticmethod
    def negative_contrast():
        compare_system.definition('反襯', '映襯', '以相反事物襯托主體', '中文解釋')
        compare_system.exampleof('以樂景寫哀情。', '寫作手法', '反襯', '修辭')

    @staticmethod
    def question():
        compare_system.definition('設問', '修辭', '先提出問題，再由作者回答或引導思考', '中文解釋')
        compare_system.exampleof('成功靠的是運氣嗎？不是，而是長期努力。', '例句', '設問', '修辭')

    @staticmethod
    def rhetorical_question():
        compare_system.definition('反問', '修辭', '用疑問形式表達肯定或否定，不期待回答', '中文解釋')
        compare_system.exampleof('難道我們不該珍惜時間嗎？', '例句', '反問', '修辭')

    @staticmethod
    def repetition():
        compare_system.definition('反復', '修辭', '重複相同詞句以強調情感或節奏', '中文解釋')
        compare_system.exampleof('走吧，走吧，別再回頭。', '例句', '反復', '修辭')

    @staticmethod
    def anadiplosis():
        compare_system.definition('頂真', '修辭', '前一句末尾詞語接續成為後一句開頭', '中文解釋')
        compare_system.exampleof('知識帶來力量，力量帶來改變。', '例句', '頂真', '修辭')

    @staticmethod
    def palindrome():
        compare_system.definition('回文', '修辭', '語句順讀倒讀皆可形成意義或結構呼應', '中文解釋')

    @staticmethod
    def gradation():
        compare_system.definition('層遞', '修辭', '依程度、範圍、時間或邏輯逐層推進', '中文解釋')
        compare_system.exampleof('先理解，再練習，最後熟練。', '例句', '層遞', '修辭')

    @staticmethod
    def climax():
        compare_system.definition('遞升', '層遞', '語意由輕到重、由小到大逐步上升', '中文解釋')

    @staticmethod
    def anticlimax():
        compare_system.definition('遞降', '層遞', '語意由重到輕、由大到小逐步下降', '中文解釋')

    @staticmethod
    def quotation():
        compare_system.definition('引用', '修辭', '引用他人言語、典籍、詩文或俗語加強表達', '中文解釋')
        compare_system.typeof('明引', '引用', '標明出處或作者', '類型')
        compare_system.typeof('暗引', '引用', '不明示出處', '類型')

    @staticmethod
    def allusion():
        compare_system.definition('用典', '修辭', '運用歷史故事、典籍或人物事蹟表達深層意義', '中文解釋')
        compare_system.requires('理解用典', '閱讀', '掌握典故來源與語境功能', '條件')

    @staticmethod
    def symbolism():
        compare_system.definition('象徵', '修辭與寫作', '以具體事物寄託抽象觀念或情感', '中文解釋')
        compare_system.exampleof('梅花象徵堅毅。', '例句', '象徵', '修辭')

    @staticmethod
    def pun():
        compare_system.definition('雙關', '修辭', '利用語音或語義使語句同時具有兩層意思', '中文解釋')
        compare_system.typeof('諧音雙關', '雙關', '利用讀音相同或相近', '類型')
        compare_system.typeof('語義雙關', '雙關', '利用同詞多義', '類型')

    @staticmethod
    def euphemism():
        compare_system.definition('婉曲', '修辭', '以委婉含蓄方式表達不便直說的內容', '中文解釋')
        compare_system.exampleof('他已長眠。', '例句', '以長眠婉指死亡', '中文解釋')

    @staticmethod
    def irony():
        compare_system.definition('倒反', '修辭', '表面說法與真正意思相反，多用於諷刺', '中文解釋')
        compare_system.exampleof('你可真準時，會議都結束了。', '例句', '倒反', '修辭')

    @staticmethod
    def synesthesia():
        compare_system.definition('移覺', '修辭', '把一種感官感受轉移到另一種感官描述', '中文解釋')
        compare_system.exampleof('她的聲音很甜。', '例句', '以味覺形容聽覺', '中文解釋')

    @staticmethod
    def sensory_description():
        compare_system.definition('摹寫', '修辭', '具體描寫視覺、聽覺、嗅覺、味覺、觸覺或動作', '中文解釋')
        compare_system.partof('視覺摹寫', '摹寫', '摹寫', '類型')
        compare_system.partof('聽覺摹寫', '摹寫', '摹寫', '類型')
        compare_system.partof('嗅覺、味覺、觸覺摹寫', '摹寫', '摹寫', '類型')

    @staticmethod
    def dynamic_description():
        compare_system.definition('動態描寫', '描寫手法', '呈現人物或事物的動作與變化', '中文解釋')

    @staticmethod
    def static_description():
        compare_system.definition('靜態描寫', '描寫手法', '呈現人物或景物在某一時刻的狀態', '中文解釋')

    @staticmethod
    def foreshadowing():
        compare_system.definition('伏筆', '寫作手法', '先在前文埋下線索，後文再回應', '中文解釋')
        compare_system.related('照應', '篇章結構', '使前後內容互相聯繫', '功能')

    @staticmethod
    def suspense():
        compare_system.definition('懸念', '寫作手法', '暫時隱藏關鍵資訊，引起讀者期待', '中文解釋')

    @staticmethod
    def flashback():
        compare_system.definition('倒敘', '敘事手法', '先寫後來發生的事，再回到先前經過', '中文解釋')

    @staticmethod
    def interpolation():
        compare_system.definition('插敘', '敘事手法', '在主要敘事中插入相關事件或背景', '中文解釋')

    @staticmethod
    def direct_statement():
        compare_system.definition('直抒胸臆', '抒情手法', '直接說出情感與思想', '中文解釋')

    @staticmethod
    def indirect_lyricism():
        compare_system.definition('間接抒情', '抒情手法', '藉景、物、事或人物寄託情感', '中文解釋')

    @staticmethod
    def scene_emotion():
        compare_system.definition('借景抒情', '抒情手法', '透過景物描寫表達情感', '中文解釋')

    @staticmethod
    def object_emotion():
        compare_system.definition('託物言志', '抒情手法', '借物的特性表達志向與品格', '中文解釋')

    @staticmethod
    def scene_blending():
        compare_system.definition('情景交融', '抒情手法', '情感與景物互相滲透、難以分割', '中文解釋')

    @staticmethod
    def opening_closing_echo():
        compare_system.definition('首尾呼應', '篇章結構', '開頭與結尾在內容或語句上互相照應', '中文解釋')

    @staticmethod
    def comparison():
        compare_system.definition('比較', '說明與議論方法', '把兩者以上放在一起辨明異同', '中文解釋')

    @staticmethod
    def classification():
        compare_system.definition('分類', '說明方法', '依共同標準將事物分成不同類別', '中文解釋')

    @staticmethod
    def definition_method():
        compare_system.definition('下定義', '說明方法', '用準確簡潔語句揭示概念本質', '中文解釋')

    @staticmethod
    def example_method():
        compare_system.definition('舉例', '說明與論證方法', '用具體事例說明抽象道理', '中文解釋')

    @staticmethod
    def data_method():
        compare_system.definition('列數據', '說明與論證方法', '用數字資料增加精確性與說服力', '中文解釋')
