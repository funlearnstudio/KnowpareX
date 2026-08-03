from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_reading:
    @staticmethod
    def reading_overview():
        compare_system.definition('閱讀理解', '國文能力', '從文字、圖表與語境中建構意義的能力', '中文解釋')
        compare_system.requires('閱讀理解', '核心能力', '字詞理解、句意整合、篇章分析、推論與評鑑', '條件')
        compare_system.related('閱讀目的', '閱讀策略', '會影響閱讀速度、注意重點與理解方法', '關係')

    @staticmethod
    def previewing():
        compare_system.definition('預覽', '閱讀策略', '正式閱讀前先看標題、作者、段落、圖表與關鍵詞', '中文解釋')
        compare_system.resultsin('預覽', '閱讀效果', '建立文章主題與結構的初步預期', '結果')

    @staticmethod
    def prediction():
        compare_system.definition('預測', '閱讀策略', '根據標題、前文與線索推測後續內容', '中文解釋')
        compare_system.requires('有效預測', '閱讀', '以文本線索為依據並隨閱讀修正', '條件')

    @staticmethod
    def questioning():
        compare_system.definition('提問', '閱讀策略', '在閱讀前、中、後提出問題以維持理解', '中文解釋')
        compare_system.exampleof('作者為什麼先寫這件事？', '問題', '閱讀提問', '例子')
        compare_system.exampleof('這段如何支持全文主旨？', '問題', '閱讀提問', '例子')

    @staticmethod
    def monitoring_comprehension():
        compare_system.definition('理解監控', '後設認知', '讀者檢查自己是否真正理解文本', '中文解釋')
        compare_system.requires('理解中斷', '修正策略', '重讀、放慢、查詞、摘要或尋找上下文', '方法')

    @staticmethod
    def rereading():
        compare_system.definition('重讀', '閱讀策略', '再次閱讀重要、困難或前後矛盾的段落', '中文解釋')
        compare_system.resultsin('重讀', '閱讀效果', '釐清指涉、因果與深層意義', '結果')

    @staticmethod
    def annotation():
        compare_system.definition('閱讀標記', '閱讀策略', '以畫線、圈詞與旁註記錄重點與疑問', '中文解釋')
        compare_system.requires('有效標記', '閱讀', '只標關鍵內容並說明標記原因', '條件')

    @staticmethod
    def keyword_identification():
        compare_system.definition('關鍵詞', '閱讀理解', '反覆出現或承擔主要概念的詞語', '中文解釋')
        compare_system.requires('找關鍵詞', '方法', '注意標題、重複詞、轉折詞與概念詞', '條件')

    @staticmethod
    def main_idea():
        compare_system.definition('主旨', '閱讀理解', '全文最核心的思想、情感或觀點', '中文解釋')
        compare_system.requires('判斷主旨', '方法', '統整各段重點、標題、開頭、結尾與作者態度', '條件')
        compare_system.opposite('主旨', '閱讀概念', '局部細節', '概念對照')

    @staticmethod
    def topic():
        compare_system.definition('主題', '閱讀理解', '文章主要談論的對象或範圍', '中文解釋')
        compare_system.related('主題', '閱讀理解', '文章談什麼', '判斷重點')
        compare_system.related('主旨', '閱讀理解', '作者想表達什麼', '判斷重點')

    @staticmethod
    def paragraph_main_idea():
        compare_system.definition('段落大意', '閱讀理解', '一個段落的核心內容', '中文解釋')
        compare_system.requires('概括段意', '方法', '刪除例子與重複內容，保留人物、事件與核心關係', '條件')

    @staticmethod
    def topic_sentence():
        compare_system.definition('主題句', '段落結構', '直接表達段落中心的句子', '中文解釋')
        compare_system.related('主題句', '段落位置', '可能出現在段首、段中或段末', '關係')

    @staticmethod
    def supporting_details():
        compare_system.definition('支持細節', '段落結構', '用例子、理由、數據、描寫或說明支持中心', '中文解釋')
        compare_system.requires('判斷支持細節', '閱讀', '說明它如何支援段落或全文中心', '條件')

    @staticmethod
    def summary():
        compare_system.definition('摘要', '閱讀策略', '以精簡文字重述文本主要內容', '中文解釋')
        compare_system.requires('有效摘要', '方法', '保留主旨、重要人物、事件、原因與結果', '條件')
        compare_system.requires('摘要', '寫作', '避免加入個人評論與無關細節', '條件')

    @staticmethod
    def paraphrase():
        compare_system.definition('改寫', '閱讀策略', '用自己的話重新表達原文意思', '中文解釋')
        compare_system.requires('正確改寫', '方法', '不改變原意、不照抄句型並保留重要訊息', '條件')

    @staticmethod
    def literal_meaning():
        compare_system.definition('字面義', '語意理解', '詞句直接表達的表層意思', '中文解釋')

    @staticmethod
    def contextual_meaning():
        compare_system.definition('語境義', '語意理解', '字詞在特定上下文中的實際意思', '中文解釋')
        compare_system.requires('判斷語境義', '方法', '結合前後句、搭配、語氣與文體', '條件')

    @staticmethod
    def context_clues():
        compare_system.definition('上下文線索', '閱讀策略', '利用周圍文字推測生詞或句意', '中文解釋')
        compare_system.typeof('定義線索', '上下文線索', '文中直接解釋', '類型')
        compare_system.typeof('例子線索', '上下文線索', '以例子提示意思', '類型')
        compare_system.typeof('對比線索', '上下文線索', '以相反內容提示', '類型')
        compare_system.typeof('因果線索', '上下文線索', '由原因或結果推測', '類型')

    @staticmethod
    def reference_words():
        compare_system.definition('指涉', '篇章理解', '代詞或省略成分指向前後文對象', '中文解釋')
        compare_system.requires('判斷指涉', '方法', '尋找語意、單複數與邏輯相符的對象', '條件')

    @staticmethod
    def cohesion():
        compare_system.definition('銜接', '篇章結構', '詞句透過代詞、重複、連接詞與省略彼此連結', '中文解釋')
        compare_system.related('連接詞', '篇章銜接', '標示因果、轉折、並列與順序', '功能')

    @staticmethod
    def coherence():
        compare_system.definition('連貫', '篇章結構', '文章整體在主題、順序與邏輯上保持一致', '中文解釋')
        compare_system.requires('判斷連貫', '閱讀', '檢查段落是否共同服務主旨', '條件')

    @staticmethod
    def sequence():
        compare_system.definition('順序關係', '篇章結構', '內容依時間、空間、步驟或邏輯排列', '中文解釋')
        compare_system.typeof('時間順序', '順序關係', '依事件先後排列', '類型')
        compare_system.typeof('空間順序', '順序關係', '依位置與視線移動排列', '類型')
        compare_system.typeof('邏輯順序', '順序關係', '依概念關係排列', '類型')

    @staticmethod
    def chronological_order():
        compare_system.definition('時間順序', '篇章結構', '依事件發生或發展先後排列', '中文解釋')
        compare_system.related('起初、接著、後來、最後', '時間順序', '常見提示詞', '例子')

    @staticmethod
    def spatial_order():
        compare_system.definition('空間順序', '篇章結構', '依遠近、上下、內外或移動路線描寫', '中文解釋')
        compare_system.related('由遠而近', '空間順序', '常見安排', '例子')

    @staticmethod
    def cause_effect():
        compare_system.definition('因果關係', '篇章邏輯', '說明事件發生的原因與造成的結果', '中文解釋')
        compare_system.related('因為、由於', '因果關係', '原因提示詞', '例子')
        compare_system.related('所以、因此、導致', '因果關係', '結果提示詞', '例子')

    @staticmethod
    def comparison_contrast():
        compare_system.definition('比較與對照', '篇章結構', '分析兩個以上對象的相同與不同', '中文解釋')
        compare_system.requires('判讀比較', '方法', '找出比較對象、標準與結論', '條件')

    @staticmethod
    def problem_solution():
        compare_system.definition('問題解決結構', '篇章結構', '先提出問題，再分析原因或提出解法', '中文解釋')
        compare_system.requires('判讀問題解決結構', '方法', '分辨問題、原因、方案與評估', '條件')

    @staticmethod
    def classification_structure():
        compare_system.definition('分類結構', '說明文結構', '依共同標準將事物分成數類', '中文解釋')
        compare_system.requires('判讀分類', '方法', '找分類標準與各類特徵', '條件')

    @staticmethod
    def general_specific():
        compare_system.definition('總分結構', '篇章結構', '先總說再分述，或先分述再總結', '中文解釋')
        compare_system.typeof('總分', '總分結構', '先總後分', '類型')
        compare_system.typeof('分總', '總分結構', '先分後總', '類型')
        compare_system.typeof('總分總', '總分結構', '總說、分述、總結', '類型')

    @staticmethod
    def transition_words():
        compare_system.definition('轉承詞', '篇章訊號', '標示內容關係與段落方向的詞語', '中文解釋')
        compare_system.related('然而、但是', '轉承詞', '轉折', '功能')
        compare_system.related('因此、所以', '轉承詞', '因果', '功能')
        compare_system.related('此外、而且', '轉承詞', '補充', '功能')

    @staticmethod
    def author_purpose():
        compare_system.definition('寫作目的', '閱讀理解', '作者創作文本想達成的功能', '中文解釋')
        compare_system.typeof('說明', '寫作目的', '傳遞知識', '類型')
        compare_system.typeof('說服', '寫作目的', '改變讀者觀點或行動', '類型')
        compare_system.typeof('抒情', '寫作目的', '表達感受', '類型')
        compare_system.typeof('娛樂', '寫作目的', '提供故事與趣味', '類型')

    @staticmethod
    def author_viewpoint():
        compare_system.definition('作者觀點', '閱讀理解', '作者對人物、事件或議題的看法', '中文解釋')
        compare_system.requires('判斷作者觀點', '方法', '分析評價詞、例證選擇、語氣與結論', '條件')

    @staticmethod
    def author_attitude():
        compare_system.definition('作者態度', '閱讀理解', '作者面對對象時的情感與立場', '中文解釋')
        compare_system.exampleof('肯定、批判、同情、諷刺、懷疑', '詞語', '作者態度', '例子')

    @staticmethod
    def tone():
        compare_system.definition('語氣', '閱讀理解', '文字呈現的情緒與說話方式', '中文解釋')
        compare_system.exampleof('平靜、沉重、幽默、激昂、諷刺', '詞語', '語氣', '例子')

    @staticmethod
    def objective_subjective():
        compare_system.definition('客觀敘述', '表達方式', '以可驗證事實為主，較少個人評價', '中文解釋')
        compare_system.definition('主觀敘述', '表達方式', '包含個人感受、判斷與價值立場', '中文解釋')

    @staticmethod
    def fact_opinion():
        compare_system.definition('事實', '閱讀判斷', '可透過證據查證真假的陳述', '中文解釋')
        compare_system.definition('意見', '閱讀判斷', '包含評價、偏好或主張的陳述', '中文解釋')
        compare_system.requires('區分事實與意見', '方法', '判斷能否查證及是否含價值詞', '條件')

    @staticmethod
    def explicit_information():
        compare_system.definition('明示訊息', '閱讀理解', '文本直接寫出的資訊', '中文解釋')

    @staticmethod
    def implicit_information():
        compare_system.definition('隱含訊息', '閱讀理解', '未直接寫出但可由線索推得的意思', '中文解釋')

    @staticmethod
    def inference():
        compare_system.definition('推論', '閱讀理解', '依文本證據與常識推得未明說的結論', '中文解釋')
        compare_system.requires('有效推論', '方法', '有文本證據且不超出合理範圍', '條件')

    @staticmethod
    def evidence_based_inference():
        compare_system.definition('證據推論', '閱讀策略', '先找線索，再說明線索如何支持推論', '中文解釋')
        compare_system.requires('推論答案', '作答', '同時指出結論與根據', '條件')

    @staticmethod
    def character_inference():
        compare_system.definition('人物推論', '敘事閱讀', '由言語、行動、心理與他人反應判斷人物特質', '中文解釋')
        compare_system.requires('判斷人物性格', '方法', '引用具體行為而非只寫形容詞', '條件')

    @staticmethod
    def motivation():
        compare_system.definition('人物動機', '敘事閱讀', '人物採取行動的原因、需求或目的', '中文解釋')
        compare_system.requires('推測動機', '方法', '結合處境、前文、內心與選擇', '條件')

    @staticmethod
    def character_change():
        compare_system.definition('人物轉變', '敘事閱讀', '人物在事件前後的態度、價值或行動改變', '中文解釋')
        compare_system.requires('分析人物轉變', '方法', '比較前後差異並找出觸發事件', '條件')

    @staticmethod
    def conflict():
        compare_system.definition('衝突', '敘事要素', '人物目標受到內在或外在阻礙', '中文解釋')
        compare_system.typeof('人與自我', '衝突', '內在衝突', '類型')
        compare_system.typeof('人與人', '衝突', '人際衝突', '類型')
        compare_system.typeof('人與社會或自然', '衝突', '外在衝突', '類型')

    @staticmethod
    def plot():
        compare_system.definition('情節', '敘事要素', '事件依因果與衝突組成的發展過程', '中文解釋')
        compare_system.partof('開端', '情節', '情節', '結構')
        compare_system.partof('發展', '情節', '情節', '結構')
        compare_system.partof('高潮', '情節', '情節', '結構')
        compare_system.partof('結局', '情節', '情節', '結構')

    @staticmethod
    def setting():
        compare_system.definition('環境', '敘事要素', '故事發生的時間、地點、社會與自然背景', '中文解釋')
        compare_system.resultsin('環境設定', '敘事效果', '影響人物行動、氣氛與主題', '結果')

    @staticmethod
    def narrator():
        compare_system.definition('敘述者', '敘事閱讀', '負責講述故事的聲音或角色', '中文解釋')
        compare_system.related('作者', '敘事概念', '不一定等同敘述者', '重要區別')

    @staticmethod
    def first_person():
        compare_system.definition('第一人稱敘事', '敘事觀點', '以我或我們敘述', '中文解釋')
        compare_system.resultsin('第一人稱敘事', '閱讀效果', '親切直接但視野受限', '結果')

    @staticmethod
    def third_person():
        compare_system.definition('第三人稱敘事', '敘事觀點', '以他、她或人物姓名敘述', '中文解釋')
        compare_system.typeof('全知觀點', '第三人稱', '可了解多個人物內心', '類型')
        compare_system.typeof('限知觀點', '第三人稱', '集中於特定人物所知', '類型')

    @staticmethod
    def unreliable_narrator():
        compare_system.definition('不可靠敘述者', '敘事觀點', '其理解、記憶或說法可能不完全可信', '中文解釋')
        compare_system.requires('判斷敘述可靠性', '方法', '比較前後矛盾與其他人物、事件證據', '條件')

    @staticmethod
    def foreshadowing():
        compare_system.definition('伏筆', '敘事技巧', '先提供線索，為後文事件作準備', '中文解釋')
        compare_system.requires('辨認伏筆', '方法', '找後文與前文細節的呼應', '條件')

    @staticmethod
    def suspense():
        compare_system.definition('懸念', '敘事技巧', '暫時隱藏資訊，讓讀者期待後續', '中文解釋')

    @staticmethod
    def flashback():
        compare_system.definition('倒敘', '敘事順序', '先寫後發生的事件，再回到先前經過', '中文解釋')

    @staticmethod
    def interpolation():
        compare_system.definition('插敘', '敘事順序', '在主要敘事中加入背景或相關事件', '中文解釋')

    @staticmethod
    def symbol():
        compare_system.definition('象徵', '閱讀理解', '具體事物在文本中代表更抽象的觀念', '中文解釋')
        compare_system.requires('判斷象徵', '方法', '觀察反覆出現、情節位置與文化意義', '條件')

    @staticmethod
    def imagery():
        compare_system.definition('意象', '文學閱讀', '融合感官形象與情感意義的語言單位', '中文解釋')
        compare_system.requires('分析意象', '方法', '說明它呈現的畫面、情緒與主題功能', '條件')

    @staticmethod
    def atmosphere():
        compare_system.definition('氛圍', '文學閱讀', '文本營造的整體情緒環境', '中文解釋')
        compare_system.resultsin('景物、用詞與節奏', '表現手法', '形成特定氛圍', '結果')

    @staticmethod
    def irony():
        compare_system.definition('反諷', '文學閱讀', '表面意義與實際意義形成落差', '中文解釋')
        compare_system.requires('判斷反諷', '方法', '比較言語、情境與結果間的矛盾', '條件')

    @staticmethod
    def humor():
        compare_system.definition('幽默', '文學效果', '以語言、情境或反差產生趣味與思考', '中文解釋')

    @staticmethod
    def satire():
        compare_system.definition('諷刺', '文學手法', '以誇張、反語或對比批評人物與社會現象', '中文解釋')

    @staticmethod
    def narrative_reading():
        compare_system.definition('記敘文閱讀', '文體閱讀', '掌握人物、事件、情節、環境與主旨', '中文解釋')
        compare_system.requires('閱讀記敘文', '方法', '找事件轉折、人物改變與細節作用', '條件')

    @staticmethod
    def lyrical_reading():
        compare_system.definition('抒情文閱讀', '文體閱讀', '理解情感來源、抒情方式、意象與語調', '中文解釋')
        compare_system.requires('閱讀抒情文', '方法', '辨認直接抒情與借景、託物等間接抒情', '條件')

    @staticmethod
    def expository_reading():
        compare_system.definition('說明文閱讀', '文體閱讀', '理解說明對象、特徵、方法與結構', '中文解釋')
        compare_system.requires('閱讀說明文', '方法', '找定義、分類、例子、數據與因果', '條件')

    @staticmethod
    def argumentative_reading():
        compare_system.definition('議論文閱讀', '文體閱讀', '分析論點、論據、論證與反方回應', '中文解釋')
        compare_system.requires('閱讀議論文', '方法', '檢查理由與證據是否足以支持主張', '條件')

    @staticmethod
    def claim():
        compare_system.definition('論點', '議論閱讀', '作者希望讀者接受的核心主張', '中文解釋')

    @staticmethod
    def evidence():
        compare_system.definition('論據', '議論閱讀', '支持論點的事例、數據、引言、原理或經驗', '中文解釋')
        compare_system.requires('評估論據', '方法', '檢查真實性、相關性、充分性與代表性', '條件')

    @staticmethod
    def reasoning():
        compare_system.definition('論證', '議論閱讀', '說明論據如何支持論點的推理', '中文解釋')

    @staticmethod
    def counterargument():
        compare_system.definition('反方觀點', '議論閱讀', '與作者主要立場不同或相反的看法', '中文解釋')
        compare_system.requires('分析反方回應', '方法', '判斷作者是否公平呈現並有效反駁', '條件')

    @staticmethod
    def logical_fallacy():
        compare_system.definition('邏輯謬誤', '議論閱讀', '推理形式或證據使用出現錯誤', '中文解釋')
        compare_system.requires('辨認謬誤', '方法', '檢查因果、樣本、概念與人身攻擊', '條件')

    @staticmethod
    def hasty_generalization():
        compare_system.definition('以偏概全', '邏輯謬誤', '以少量或不具代表性的例子推論整體', '中文解釋')

    @staticmethod
    def false_cause():
        compare_system.definition('錯誤因果', '邏輯謬誤', '把相關或先後誤認為因果', '中文解釋')

    @staticmethod
    def false_dilemma():
        compare_system.definition('非黑即白', '邏輯謬誤', '把多種可能簡化成只有兩種選擇', '中文解釋')

    @staticmethod
    def appeal_to_authority():
        compare_system.definition('不當訴諸權威', '邏輯謬誤', '引用不具相關專業或不可驗證的權威代替證據', '中文解釋')

    @staticmethod
    def ad_hominem():
        compare_system.definition('人身攻擊', '邏輯謬誤', '攻擊提出主張的人，而非回應主張內容', '中文解釋')

    @staticmethod
    def data_reading():
        compare_system.definition('數據閱讀', '資訊閱讀', '理解數字、比例、單位、趨勢與比較基準', '中文解釋')
        compare_system.requires('判讀數據', '方法', '確認資料來源、樣本、時間與單位', '條件')

    @staticmethod
    def chart_reading():
        compare_system.definition('圖表閱讀', '多模態閱讀', '將圖、表、文字與數據整合解讀', '中文解釋')
        compare_system.requires('圖表閱讀', '步驟', '看標題、軸線、圖例、單位、趨勢與例外', '條件')

    @staticmethod
    def table_reading():
        compare_system.definition('表格閱讀', '多模態閱讀', '依欄列標題比較資料', '中文解釋')
        compare_system.requires('表格判讀', '方法', '確認比較項目與同一欄列的關係', '條件')

    @staticmethod
    def infographic():
        compare_system.definition('資訊圖表', '多模態文本', '結合文字、圖像、圖示與數據傳達資訊', '中文解釋')
        compare_system.requires('判讀資訊圖表', '方法', '區分視覺裝飾與核心證據', '條件')

    @staticmethod
    def image_text_relation():
        compare_system.definition('圖文關係', '多模態閱讀', '圖像與文字可能互補、重複、對照或衝突', '中文解釋')
        compare_system.requires('分析圖文關係', '方法', '說明圖像增加或改變了哪些訊息', '條件')

    @staticmethod
    def multiple_texts():
        compare_system.definition('多文本閱讀', '閱讀素養', '整合兩篇以上不同來源、觀點或形式的文本', '中文解釋')
        compare_system.requires('多文本整合', '方法', '比較主題、立場、證據與可靠性', '條件')

    @staticmethod
    def cross_text_comparison():
        compare_system.definition('跨文本比較', '閱讀策略', '比較不同文本的相同、差異與互補', '中文解釋')
        compare_system.requires('跨文本比較', '作答', '使用共同標準並引用各文本證據', '條件')

    @staticmethod
    def source_evaluation():
        compare_system.definition('來源評估', '資訊素養', '判斷作者、出版者、目的、時間與證據品質', '中文解釋')
        compare_system.requires('評估來源可信度', '方法', '確認專業性、透明度、可查證性與利益關係', '條件')

    @staticmethod
    def bias():
        compare_system.definition('偏見或偏向', '資訊閱讀', '因立場、利益或選材使呈現不完全中立', '中文解釋')
        compare_system.requires('辨認偏向', '方法', '分析用詞、遺漏、選例與資訊來源', '條件')

    @staticmethod
    def misinformation():
        compare_system.definition('錯誤資訊', '媒體閱讀', '內容不正確但未必故意欺騙', '中文解釋')
        compare_system.definition('假訊息', '媒體閱讀', '刻意製造或散播以誤導的資訊', '中文解釋')

    @staticmethod
    def fact_checking():
        compare_system.definition('事實查核', '資訊素養', '透過可靠來源驗證可查證的主張', '中文解釋')
        compare_system.requires('事實查核', '方法', '追原始來源、交叉比對、查日期與完整脈絡', '條件')

    @staticmethod
    def advertisement_reading():
        compare_system.definition('廣告閱讀', '媒體閱讀', '分析廣告目標、受眾、訴求與證據', '中文解釋')
        compare_system.requires('判讀廣告', '方法', '區分事實、暗示、情緒訴求與誇大', '條件')

    @staticmethod
    def news_reading():
        compare_system.definition('新聞閱讀', '媒體閱讀', '分辨事件事實、消息來源、評論與報導框架', '中文解釋')
        compare_system.requires('閱讀新聞', '方法', '比較多家來源並注意標題與內文差異', '條件')

    @staticmethod
    def classical_text_reading():
        compare_system.definition('文言文閱讀', '文體閱讀', '理解實詞、虛詞、句式、語境與文化背景', '中文解釋')
        compare_system.requires('閱讀文言文', '步驟', '逐句理解、辨句法、串聯段意、統整主旨', '條件')

    @staticmethod
    def classical_word_meaning():
        compare_system.requires('判斷文言字義', '方法', '看詞性、搭配、上下文與古今異義', '條件')

    @staticmethod
    def classical_sentence_pattern():
        compare_system.requires('判斷文言句式', '方法', '辨認判斷、被動、倒裝與省略', '條件')

    @staticmethod
    def classical_translation():
        compare_system.requires('翻譯文言句', '方法', '保留原意、補省略、調語序並使語句通順', '條件')

    @staticmethod
    def classical_theme():
        compare_system.requires('判斷古文主旨', '方法', '結合事件、議論、作者處境與結尾', '條件')

    @staticmethod
    def classical_poetry_reading():
        compare_system.definition('古典詩歌閱讀', '詩歌閱讀', '理解意象、情感、聲律、用典與章法', '中文解釋')
        compare_system.requires('閱讀古典詩', '方法', '先還原畫面，再分析情感與表現手法', '條件')

    @staticmethod
    def poetry_speaker():
        compare_system.definition('詩中說話者', '詩歌閱讀', '詩中發出聲音的角色，不必等同作者本人', '中文解釋')

    @staticmethod
    def poetry_imagery():
        compare_system.requires('分析詩歌意象', '方法', '說明景物特徵、文化聯想與情感功能', '條件')

    @staticmethod
    def poetry_emotion():
        compare_system.requires('判斷詩歌情感', '方法', '結合意象、動詞、語氣、時間與處境', '條件')

    @staticmethod
    def poetry_structure():
        compare_system.requires('分析詩歌結構', '方法', '觀察起承轉合、時空變化與結尾收束', '條件')

    @staticmethod
    def modern_poetry_reading():
        compare_system.definition('現代詩閱讀', '詩歌閱讀', '理解分行、節奏、意象、語言跳躍與象徵', '中文解釋')
        compare_system.requires('閱讀現代詩', '方法', '不要只逐字解釋，要統整畫面與情緒', '條件')

    @staticmethod
    def rhetoric_effect():
        compare_system.definition('修辭效果', '閱讀理解', '修辭對形象、節奏、情感、語氣與說服力的作用', '中文解釋')
        compare_system.requires('回答修辭效果', '方法', '指出修辭名稱、描寫內容與表達作用', '條件')

    @staticmethod
    def word_effect():
        compare_system.definition('用詞效果', '閱讀理解', '特定字詞在準確度、情感與畫面上的作用', '中文解釋')
        compare_system.requires('分析用詞', '方法', '比較替換前後的語氣與意義差異', '條件')

    @staticmethod
    def sentence_effect():
        compare_system.definition('句式效果', '閱讀理解', '長短句、整散句、問句與感嘆句造成的節奏與語氣', '中文解釋')

    @staticmethod
    def title_function():
        compare_system.definition('標題作用', '篇章閱讀', '概括內容、點明主旨、設置懸念或形成象徵', '中文解釋')
        compare_system.requires('分析標題', '方法', '連結內容、結構、主旨與讀者效果', '條件')

    @staticmethod
    def opening_function():
        compare_system.definition('開頭作用', '篇章閱讀', '引入主題、交代背景、營造氛圍或設置懸念', '中文解釋')

    @staticmethod
    def ending_function():
        compare_system.definition('結尾作用', '篇章閱讀', '總結、點題、呼應、轉折或留下餘韻', '中文解釋')

    @staticmethod
    def paragraph_function():
        compare_system.definition('段落作用', '篇章閱讀', '段落在內容與結構上的功能', '中文解釋')
        compare_system.requires('分析段落作用', '方法', '分別說明內容功能與結構功能', '條件')

    @staticmethod
    def transition_paragraph():
        compare_system.definition('過渡段', '篇章結構', '承接上文並引出下文的段落', '中文解釋')

    @staticmethod
    def detail_function():
        compare_system.definition('細節作用', '文學閱讀', '細節可塑造人物、推進情節、營造氛圍或深化主題', '中文解釋')

    @staticmethod
    def quotation_function():
        compare_system.definition('引用作用', '閱讀理解', '增加權威、文化厚度、真實感或論證力量', '中文解釋')

    @staticmethod
    def example_function():
        compare_system.definition('舉例作用', '閱讀理解', '使抽象概念具體並支持說明或論證', '中文解釋')

    @staticmethod
    def data_function():
        compare_system.definition('數據作用', '閱讀理解', '使說明更精確並增強可信度', '中文解釋')

    @staticmethod
    def contrast_function():
        compare_system.definition('對比作用', '閱讀理解', '凸顯差異、人物特質或作者立場', '中文解釋')

    @staticmethod
    def description_function():
        compare_system.definition('描寫作用', '閱讀理解', '呈現形象、氛圍、性格與情感', '中文解釋')

    @staticmethod
    def reading_question_stems():
        compare_system.definition('題幹', '考試閱讀', '題目提出的任務與限制', '中文解釋')
        compare_system.requires('讀懂題幹', '作答', '圈出人物、範圍、比較標準與作答動詞', '條件')

    @staticmethod
    def locate_information():
        compare_system.definition('檢索訊息題', '閱讀題型', '從文本中找出明確資訊', '中文解釋')
        compare_system.requires('作答檢索題', '方法', '精確回到指定段落並核對條件', '條件')

    @staticmethod
    def integrate_information():
        compare_system.definition('統整訊息題', '閱讀題型', '結合不同句段形成完整答案', '中文解釋')
        compare_system.requires('作答統整題', '方法', '避免只抄單一句，需建立關係', '條件')

    @staticmethod
    def interpretation_question():
        compare_system.definition('解釋題', '閱讀題型', '說明詞句、行為、結構或表現手法的意義', '中文解釋')
        compare_system.requires('作答解釋題', '方法', '用自己的話說明並引用文本依據', '條件')

    @staticmethod
    def inference_question():
        compare_system.definition('推論題', '閱讀題型', '根據文本線索推得未直接說出的答案', '中文解釋')
        compare_system.requires('作答推論題', '方法', '答案不可超出文本可支持範圍', '條件')

    @staticmethod
    def evaluation_question():
        compare_system.definition('評鑑題', '閱讀題型', '判斷觀點、證據、寫法或來源的有效性', '中文解釋')
        compare_system.requires('作答評鑑題', '方法', '提出標準、判斷與理由', '條件')

    @staticmethod
    def comparison_question():
        compare_system.definition('比較題', '閱讀題型', '比較兩個人物、段落、文本或觀點', '中文解釋')
        compare_system.requires('作答比較題', '方法', '使用同一標準並同時處理兩方', '條件')

    @staticmethod
    def open_response():
        compare_system.definition('開放式閱讀題', '閱讀題型', '允許多種合理答案，但必須有文本依據', '中文解釋')
        compare_system.requires('開放式作答', '方法', '觀點明確、引用證據並解釋關聯', '條件')

    @staticmethod
    def multiple_choice_strategy():
        compare_system.definition('選擇題策略', '考試閱讀', '先判斷題幹要求，再逐項核對文本', '中文解釋')
        compare_system.requires('排除選項', '方法', '找偷換概念、範圍擴大、因果顛倒與無中生有', '條件')

    @staticmethod
    def distractor_types():
        compare_system.definition('干擾選項', '考試閱讀', '看似合理但與文本不符的選項', '中文解釋')
        compare_system.typeof('過度推論', '干擾選項', '超出文本', '類型')
        compare_system.typeof('張冠李戴', '干擾選項', '人物或事件對錯', '類型')
        compare_system.typeof('部分正確', '干擾選項', '一半正確但整體錯誤', '類型')

    @staticmethod
    def short_answer_strategy():
        compare_system.definition('簡答題策略', '考試閱讀', '依題目動詞組織完整、精確且有依據的答案', '中文解釋')
        compare_system.requires('簡答題', '作答', '回答問題、引用證據、說明關係', '條件')

    @staticmethod
    def evidence_citation():
        compare_system.definition('文本證據', '閱讀作答', '支持答案的具體字句、事件或資料', '中文解釋')
        compare_system.requires('引用文本證據', '方法', '引用必要部分並解釋其支持作用', '條件')

    @staticmethod
    def answer_completeness():
        compare_system.definition('答案完整性', '閱讀作答', '涵蓋題目要求的所有部分', '中文解釋')
        compare_system.requires('檢查答案', '方法', '核對題幹中的幾點、比較與原因', '條件')

    @staticmethod
    def reading_speed():
        compare_system.definition('閱讀速度', '考試策略', '依文本難度與題目目的調整速度', '中文解釋')
        compare_system.requires('有效閱讀速度', '方法', '簡單處快讀、關鍵處慢讀、難處重讀', '條件')

    @staticmethod
    def time_management():
        compare_system.definition('閱讀時間分配', '考試策略', '依題數、篇幅與難度安排作答時間', '中文解釋')
        compare_system.requires('時間管理', '方法', '先完成有把握題目並保留檢查時間', '條件')

    @staticmethod
    def exam_review():
        compare_system.definition('閱讀題檢查', '考試策略', '重新核對題幹、選項與文本證據', '中文解釋')
        compare_system.requires('檢查選擇題', '方法', '確認不是憑印象而是依文本', '條件')

    @staticmethod
    def junior_exam_reading():
        compare_system.definition('國中會考閱讀', '考試閱讀', '重視語文基礎、篇章理解、推論與生活情境應用', '中文解釋')
        compare_system.requires('準備會考閱讀', '方法', '練習短文、長文、圖表與跨文本題', '條件')

    @staticmethod
    def high_school_reading():
        compare_system.definition('高中國文閱讀', '考試閱讀', '重視文本分析、文言理解、多文本整合與評鑑', '中文解釋')
        compare_system.requires('準備高中閱讀', '方法', '累積文學常識並練習深層推論與證據判斷', '條件')

    @staticmethod
    def literacy_based_reading():
        compare_system.definition('素養導向閱讀', '課程與評量', '將知識運用於真實或新情境的閱讀', '中文解釋')
        compare_system.requires('素養閱讀', '能力', '整合資訊、判斷來源、解決問題與表達理由', '條件')

    @staticmethod
    def interdisciplinary_reading():
        compare_system.definition('跨領域閱讀', '閱讀素養', '結合國文與歷史、科學、社會、藝術等知識', '中文解釋')
        compare_system.requires('跨領域閱讀', '方法', '先理解文本，再辨認所需背景知識', '條件')

    @staticmethod
    def long_text_strategy():
        compare_system.definition('長文閱讀', '閱讀策略', '處理篇幅較長、資訊較多的文本', '中文解釋')
        compare_system.requires('閱讀長文', '方法', '分段摘要、標記轉折、建立結構圖', '條件')

    @staticmethod
    def difficult_text_strategy():
        compare_system.definition('難文閱讀', '閱讀策略', '面對生詞、抽象概念與複雜句式的處理方法', '中文解釋')
        compare_system.requires('理解難文', '方法', '拆句、找主幹、重讀、改寫與連結上下文', '條件')

    @staticmethod
    def reading_notes():
        compare_system.definition('閱讀筆記', '學習方法', '整理文本結構、主旨、關鍵詞與個人疑問', '中文解釋')
        compare_system.requires('有效閱讀筆記', '方法', '以自己的話統整，而非整段抄錄', '條件')

    @staticmethod
    def concept_map():
        compare_system.definition('概念圖', '閱讀工具', '用節點與連線呈現概念關係', '中文解釋')
        compare_system.resultsin('概念圖', '學習效果', '看清分類、因果與上下位關係', '結果')

    @staticmethod
    def timeline():
        compare_system.definition('時間軸', '閱讀工具', '依時間順序整理人物、事件與變化', '中文解釋')
        compare_system.resultsin('時間軸', '學習效果', '釐清事件先後與因果', '結果')

    @staticmethod
    def compare_chart():
        compare_system.definition('比較表', '閱讀工具', '以共同標準整理不同對象的異同', '中文解釋')

    @staticmethod
    def question_answer_relationship():
        compare_system.definition('問題與答案關係', '閱讀策略', '辨認答案在文本直接出現、需整合、需推論或需結合個人觀點', '中文解釋')

    @staticmethod
    def reading_reflection():
        compare_system.definition('閱讀反思', '閱讀後活動', '思考文本如何改變、挑戰或深化自己的理解', '中文解釋')
        compare_system.requires('閱讀反思', '方法', '連結文本證據、個人經驗與公共議題', '條件')

    @staticmethod
    def reading_transfer():
        compare_system.definition('閱讀遷移', '學習能力', '把在一篇文本學到的策略運用到新文本', '中文解釋')
        compare_system.resultsin('閱讀遷移', '學習效果', '提升面對陌生文本的獨立理解能力', '結果')
