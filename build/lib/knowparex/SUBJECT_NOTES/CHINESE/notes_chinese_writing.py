from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_writing:
    @staticmethod
    def writing_process():
        compare_system.definition('寫作流程', '國文作文', '審題、立意、選材、組織、起草、修改與校對', '中文解釋')
        compare_system.requires('完成作文', '流程', '構思、書寫與修訂', '條件')

    @staticmethod
    def analyze_prompt():
        compare_system.definition('審題', '作文步驟', '辨認題目限制、關鍵詞、文體與寫作對象', '中文解釋')
        compare_system.requires('正確審題', '方法', '圈出關鍵詞、確認範圍、判斷題型', '條件')

    @staticmethod
    def determine_purpose():
        compare_system.definition('立意', '作文步驟', '確定文章中心思想與價值方向', '中文解釋')
        compare_system.requires('好的立意', '寫作', '明確、真誠、集中且具有思考深度', '條件')

    @staticmethod
    def select_material():
        compare_system.definition('選材', '作文步驟', '挑選最能支持主旨的事件、細節、例子與資料', '中文解釋')
        compare_system.requires('有效選材', '寫作', '真實、典型、具體並符合題意', '條件')

    @staticmethod
    def outline():
        compare_system.definition('大綱', '寫作工具', '安排文章段落、順序與重點的架構', '中文解釋')
        compare_system.partof('開頭', '大綱', '文章', '結構')
        compare_system.partof('主體', '大綱', '文章', '結構')
        compare_system.partof('結尾', '大綱', '文章', '結構')

    @staticmethod
    def paragraphing():
        compare_system.definition('分段', '篇章組織', '依意義、事件、時間或論點劃分段落', '中文解釋')
        compare_system.requires('良好分段', '寫作', '每段中心清楚並前後連貫', '條件')

    @staticmethod
    def topic_sentence():
        compare_system.definition('主題句', '段落寫作', '指出段落中心內容的句子', '中文解釋')
        compare_system.related('支持句', '段落寫作', '用細節、例子與說明支持主題句', '功能')

    @staticmethod
    def coherence():
        compare_system.definition('連貫', '篇章品質', '句子與段落在語意和邏輯上順暢銜接', '中文解釋')
        compare_system.requires('文章連貫', '方法', '代詞指涉清楚、轉承自然、順序合理', '條件')

    @staticmethod
    def transition():
        compare_system.definition('過渡', '篇章技巧', '連接段落、事件、時間或論點，使文章轉換自然', '中文解釋')
        compare_system.exampleof('然而、因此、另一方面、接著、最後', '詞語', '過渡語', '例子')

    @staticmethod
    def opening():
        compare_system.definition('開頭', '作文結構', '引入主題並建立閱讀期待', '中文解釋')
        compare_system.requires('有效開頭', '寫作', '簡潔、扣題、具有方向', '條件')

    @staticmethod
    def direct_opening():
        compare_system.definition('開門見山', '開頭方式', '直接點出主題或立場', '中文解釋')

    @staticmethod
    def scene_opening():
        compare_system.definition('情境開頭', '開頭方式', '以場景、動作或對話帶入主題', '中文解釋')

    @staticmethod
    def question_opening():
        compare_system.definition('設問開頭', '開頭方式', '以問題引起讀者思考', '中文解釋')

    @staticmethod
    def quotation_opening():
        compare_system.definition('引用開頭', '開頭方式', '引用名言、詩句或資料引出主題', '中文解釋')
        compare_system.requires('引用開頭', '寫作', '來源適切且能服務主旨', '條件')

    @staticmethod
    def ending():
        compare_system.definition('結尾', '作文結構', '收束全文、回扣主旨並留下完整印象', '中文解釋')

    @staticmethod
    def summary_ending():
        compare_system.definition('總結式結尾', '結尾方式', '整理主要內容並重申中心', '中文解釋')

    @staticmethod
    def echo_ending():
        compare_system.definition('呼應式結尾', '結尾方式', '回應題目、開頭或前文重要意象', '中文解釋')

    @staticmethod
    def open_ending():
        compare_system.definition('餘韻式結尾', '結尾方式', '不完全說盡，留下思考與想像空間', '中文解釋')

    @staticmethod
    def narrative():
        compare_system.definition('記敘文', '作文文體', '以人物與事件為核心，呈現經過、情感與意義', '中文解釋')
        compare_system.requires('記敘文', '要素', '人物、時間、地點、事件與因果', '內容')

    @staticmethod
    def narrative_order():
        compare_system.definition('順敘', '敘事方式', '依事件發生先後敘述', '中文解釋')
        compare_system.definition('倒敘', '敘事方式', '先寫結果或後來事件，再回述經過', '中文解釋')
        compare_system.definition('插敘', '敘事方式', '在主要敘事中插入背景或相關事件', '中文解釋')

    @staticmethod
    def character_writing():
        compare_system.definition('人物描寫', '記敘文技巧', '透過外貌、語言、動作、心理與側面描寫刻畫人物', '中文解釋')
        compare_system.partof('外貌描寫', '人物描寫', '人物描寫', '類型')
        compare_system.partof('語言描寫', '人物描寫', '人物描寫', '類型')
        compare_system.partof('動作描寫', '人物描寫', '人物描寫', '類型')
        compare_system.partof('心理描寫', '人物描寫', '人物描寫', '類型')

    @staticmethod
    def scene_writing():
        compare_system.definition('景物描寫', '寫作技巧', '運用感官、空間順序與變化呈現環境', '中文解釋')
        compare_system.requires('有效景物描寫', '寫作', '選擇性、具體性與情感功能', '條件')

    @staticmethod
    def event_writing():
        compare_system.definition('事件描寫', '記敘文技巧', '聚焦關鍵衝突、轉折與細節', '中文解釋')
        compare_system.requires('事件有張力', '寫作', '目標、阻礙、選擇與結果', '條件')

    @staticmethod
    def detail():
        compare_system.definition('細節描寫', '寫作技巧', '用具體微小的動作、語言、物件或感受呈現真實感', '中文解釋')
        compare_system.resultsin('具體細節', '寫作效果', '人物與場景更鮮明', '結果')

    @staticmethod
    def lyrical():
        compare_system.definition('抒情文', '作文文體', '以情感為中心，重視真誠與感染力', '中文解釋')
        compare_system.typeof('直接抒情', '抒情文', '直接表達情感', '類型')
        compare_system.typeof('間接抒情', '抒情文', '藉景物、事件或象徵寄託情感', '類型')

    @staticmethod
    def expository():
        compare_system.definition('說明文', '作文文體', '清楚解說事物、知識、方法或原理', '中文解釋')
        compare_system.requires('說明文', '品質', '內容正確、條理清楚、語言精確', '條件')

    @staticmethod
    def expository_methods():
        compare_system.partof('下定義', '說明方法', '說明文', '方法')
        compare_system.partof('分類', '說明方法', '說明文', '方法')
        compare_system.partof('舉例', '說明方法', '說明文', '方法')
        compare_system.partof('比較', '說明方法', '說明文', '方法')
        compare_system.partof('列數據', '說明方法', '說明文', '方法')
        compare_system.partof('因果說明', '說明方法', '說明文', '方法')

    @staticmethod
    def argumentative():
        compare_system.definition('議論文', '作文文體', '提出論點並以理由與證據加以證明', '中文解釋')
        compare_system.partof('論點', '議論文要素', '議論文', '內容')
        compare_system.partof('論據', '議論文要素', '議論文', '內容')
        compare_system.partof('論證', '議論文要素', '議論文', '內容')

    @staticmethod
    def claim():
        compare_system.definition('論點', '議論文', '作者主張或欲證明的核心觀點', '中文解釋')
        compare_system.requires('好論點', '議論寫作', '明確、可辯論、符合題意', '條件')

    @staticmethod
    def evidence():
        compare_system.definition('論據', '議論文', '支持論點的事實、例子、數據、名言或原理', '中文解釋')
        compare_system.requires('可靠論據', '議論寫作', '真實、相關、充分且具代表性', '條件')

    @staticmethod
    def reasoning():
        compare_system.definition('論證', '議論文', '說明論據如何支持論點的推理過程', '中文解釋')
        compare_system.requires('有效論證', '議論寫作', '邏輯清楚並回應可能反例', '條件')

    @staticmethod
    def example_argument():
        compare_system.definition('舉例論證', '論證方法', '用具體事例證明論點', '中文解釋')

    @staticmethod
    def comparison_argument():
        compare_system.definition('對比論證', '論證方法', '比較正反或異同以凸顯觀點', '中文解釋')

    @staticmethod
    def cause_argument():
        compare_system.definition('因果論證', '論證方法', '分析原因與結果建立論點', '中文解釋')

    @staticmethod
    def quotation_argument():
        compare_system.definition('引用論證', '論證方法', '引用權威言論、經典或研究支持論點', '中文解釋')
        compare_system.requires('引用論證', '寫作', '來源可信且解釋與論點關係', '條件')

    @staticmethod
    def counterargument():
        compare_system.definition('反方觀點', '議論寫作', '可能反對自身論點的意見', '中文解釋')
        compare_system.requires('回應反方', '議論寫作', '公平陳述、分析限制並提出反駁', '方法')

    @staticmethod
    def compare_contrast():
        compare_system.definition('比較型作文', '作文題型', '分析兩個以上對象的相同、不同與意義', '中文解釋')
        compare_system.requires('比較型作文', '結構', '明確比較標準與一致分析層次', '條件')

    @staticmethod
    def problem_solution():
        compare_system.definition('問題解決型作文', '作文題型', '界定問題、分析原因並提出可行方案', '中文解釋')
        compare_system.requires('解決方案', '寫作', '具體、可行並回應問題原因', '條件')

    @staticmethod
    def reflection():
        compare_system.definition('感想文', '作文題型', '由事件、文本或經驗出發，提出個人理解與反思', '中文解釋')
        compare_system.requires('有深度的感想', '寫作', '不只重述內容，還要連結觀點與經驗', '條件')

    @staticmethod
    def reading_response():
        compare_system.definition('閱讀心得', '作文題型', '摘要文本重點並提出回應、評價與延伸思考', '中文解釋')
        compare_system.requires('閱讀心得', '結構', '文本理解、個人回應與具體依據', '條件')

    @staticmethod
    def picture_writing():
        compare_system.definition('圖表或圖像寫作', '素養寫作', '根據圖片、漫畫、圖表或多模態材料寫作', '中文解釋')
        compare_system.requires('圖像寫作', '方法', '觀察細節、解讀關係、形成主旨', '條件')

    @staticmethod
    def prompt_material_writing():
        compare_system.definition('材料作文', '作文題型', '根據提供的文字或資料提煉主題並完成文章', '中文解釋')
        compare_system.requires('材料作文', '方法', '概括材料、抓核心、避免只抄材料', '條件')

    @staticmethod
    def title_writing():
        compare_system.definition('命題作文', '作文題型', '依既定題目與範圍完成文章', '中文解釋')
        compare_system.requires('命題作文', '方法', '精確理解題目中的核心概念與限制', '條件')

    @staticmethod
    def free_topic_writing():
        compare_system.definition('自訂題目作文', '作文題型', '在指定主題或材料下自行命題', '中文解釋')
        compare_system.requires('自訂題目', '寫作', '簡潔、具體、能統攝內容', '條件')

    @staticmethod
    def description():
        compare_system.definition('描寫', '寫作方式', '以具體語言呈現人物、景物、動作與感受', '中文解釋')

    @staticmethod
    def sensory_detail():
        compare_system.definition('感官描寫', '寫作技巧', '運用視覺、聽覺、嗅覺、味覺與觸覺', '中文解釋')

    @staticmethod
    def show_not_tell():
        compare_system.definition('以描寫代替直說', '寫作技巧', '透過動作、對話與細節讓讀者自行感受', '中文解釋')

    @staticmethod
    def dialogue():
        compare_system.definition('對話', '記敘文技巧', '透過人物說話推進情節、塑造性格', '中文解釋')
        compare_system.requires('有效對話', '寫作', '符合人物身分並具有功能', '條件')

    @staticmethod
    def voice():
        compare_system.definition('文章語調', '寫作品質', '作者在文字中呈現的態度、節奏與個人風格', '中文解釋')

    @staticmethod
    def word_choice():
        compare_system.definition('遣詞用字', '寫作技巧', '選擇準確、具體且符合語境的詞語', '中文解釋')
        compare_system.requires('精確用詞', '寫作', '避免空泛、重複與不合搭配', '條件')

    @staticmethod
    def sentence_variety():
        compare_system.definition('句式變化', '寫作技巧', '交替使用長短句、整散句與不同句型', '中文解釋')
        compare_system.resultsin('句式變化', '寫作效果', '節奏更自然並避免單調', '結果')

    @staticmethod
    def rhetoric_in_writing():
        compare_system.related('譬喻、排比、映襯、設問', '作文修辭', '可增強形象與節奏', '功能')
        compare_system.requires('使用修辭', '寫作', '自然、適量並服務內容', '條件')

    @staticmethod
    def revision():
        compare_system.definition('修改', '寫作流程', '重新檢查內容、結構、邏輯與語言', '中文解釋')
        compare_system.requires('作文修改', '方法', '檢查扣題、段落、證據、連貫與用字', '條件')

    @staticmethod
    def proofreading():
        compare_system.definition('校對', '寫作流程', '檢查錯別字、標點、語病與格式', '中文解釋')

    @staticmethod
    def common_errors():
        compare_system.related('離題', '作文問題', '內容未回應題目核心', '中文解釋')
        compare_system.related('流水帳', '作文問題', '只按順序羅列事件，缺乏重點與意義', '中文解釋')
        compare_system.related('空泛', '作文問題', '缺少具體材料與細節', '中文解釋')
        compare_system.related('堆砌修辭', '作文問題', '修辭過多且未服務內容', '中文解釋')

    @staticmethod
    def time_management():
        compare_system.definition('作文時間分配', '考試策略', '預留審題構思、書寫與檢查時間', '中文解釋')
        compare_system.requires('考場作文', '策略', '先規畫再書寫，最後檢查', '條件')

    @staticmethod
    def handwriting_layout():
        compare_system.definition('卷面與格式', '考試寫作', '字跡清楚、分段明確、標點正確', '中文解釋')
        compare_system.resultsin('清楚卷面', '閱卷效果', '提升可讀性並減少誤判', '結果')
