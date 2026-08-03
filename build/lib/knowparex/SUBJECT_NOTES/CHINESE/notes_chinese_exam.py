from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_exam:
    @staticmethod
    def exam_overview():
        compare_system.definition('國文考試準備', '評量策略', '結合語文知識、閱讀理解、文言文、寫作與時間管理', '中文解釋')
        compare_system.requires('有效準備國文考試', '方法', '理解概念、練習題型、分析錯誤並定期複習', '條件')

    @staticmethod
    def junior_high_exam():
        compare_system.definition('國中教育會考國文', '國中評量', '重視語文知識、閱讀理解、文言文與生活情境運用', '中文解釋')
        compare_system.requires('準備會考國文', '方法', '累積字詞成語、熟悉閱讀題型並練習長文', '條件')

    @staticmethod
    def high_school_exam():
        compare_system.definition('高中國文評量', '高中評量', '重視文言閱讀、現代文本、多文本整合、文學文化與表達', '中文解釋')
        compare_system.requires('準備高中國文', '方法', '建立知識架構並練習深層分析與證據作答', '條件')

    @staticmethod
    def gsat_chinese():
        compare_system.definition('學測國文', '升學評量', '測驗語文理解、文學文化知識、閱讀統整與表達能力', '中文解釋')
        compare_system.requires('準備學測國文', '方法', '練習長文、多文本、文言文、圖表與混合題', '條件')

    @staticmethod
    def chinese_writing_test():
        compare_system.definition('國語文寫作能力測驗', '國寫', '以引導材料評量理解、分析、感受與文字表達能力', '中文解釋')
        compare_system.requires('完成國寫', '能力', '審題、取材、組織、論述、抒情與修訂', '條件')

    @staticmethod
    def knowledge_questions():
        compare_system.definition('語文知識題', '國文題型', '測驗字音字形、詞義、成語、修辭、文法與文化常識', '中文解釋')
        compare_system.requires('作答語文知識題', '方法', '結合規則、語境與排除法', '條件')

    @staticmethod
    def character_pronunciation():
        compare_system.definition('字音題', '國文題型', '判斷漢字在詞語中的正確讀音', '中文解釋')
        compare_system.requires('準備字音題', '方法', '整理破音字、形近字與常見誤讀', '條件')

    @staticmethod
    def character_form():
        compare_system.definition('字形題', '國文題型', '判斷詞語中的正確漢字', '中文解釋')
        compare_system.requires('準備字形題', '方法', '比較部件、字義與固定搭配', '條件')

    @staticmethod
    def word_meaning():
        compare_system.definition('詞義題', '國文題型', '判斷字詞在特定語境中的意義', '中文解釋')
        compare_system.requires('作答詞義題', '方法', '先看上下文，再比較選項差異', '條件')

    @staticmethod
    def idiom_question():
        compare_system.definition('成語題', '國文題型', '判斷成語意義、感情色彩與使用對象', '中文解釋')
        compare_system.requires('作答成語題', '方法', '檢查主詞、情境、褒貶與固定用法', '條件')

    @staticmethod
    def rhetoric_question():
        compare_system.definition('修辭題', '國文題型', '辨認修辭並分析表達效果', '中文解釋')
        compare_system.requires('作答修辭題', '方法', '先判斷語句關係，再說明形象、情感或語氣效果', '條件')

    @staticmethod
    def grammar_question():
        compare_system.definition('語法題', '國文題型', '測驗詞類、句型、複句與語病', '中文解釋')
        compare_system.requires('作答語法題', '方法', '找句子主幹並分析詞語功能', '條件')

    @staticmethod
    def culture_question():
        compare_system.definition('文化常識題', '國文題型', '測驗文體、經典、稱謂、節日、年齡與應用文', '中文解釋')
        compare_system.requires('準備文化常識', '方法', '建立分類表並以例題反覆辨認', '條件')

    @staticmethod
    def classical_question():
        compare_system.definition('文言文題', '國文題型', '測驗實詞、虛詞、句式、翻譯、主旨與人物思想', '中文解釋')
        compare_system.requires('作答文言文題', '方法', '逐句理解並回到全文判斷', '條件')

    @staticmethod
    def modern_text_question():
        compare_system.definition('現代文閱讀題', '國文題型', '測驗主旨、結構、推論、觀點與表現手法', '中文解釋')
        compare_system.requires('作答現代文閱讀題', '方法', '用題幹定位，再以文本證據判斷', '條件')

    @staticmethod
    def poetry_question():
        compare_system.definition('詩歌閱讀題', '國文題型', '測驗意象、情感、章法、語氣與修辭', '中文解釋')
        compare_system.requires('作答詩歌題', '方法', '先還原畫面，再分析情感與手法', '條件')

    @staticmethod
    def multiple_text_question():
        compare_system.definition('多文本題', '國文題型', '整合兩篇以上文本、圖表或不同觀點', '中文解釋')
        compare_system.requires('作答多文本題', '方法', '先分別理解，再比較共同問題', '條件')

    @staticmethod
    def mixed_question():
        compare_system.definition('混合題', '國文題型', '結合選擇、簡答、填表與文本分析', '中文解釋')
        compare_system.requires('作答混合題', '方法', '依每小題要求分別定位證據', '條件')

    @staticmethod
    def image_chart_question():
        compare_system.definition('圖表閱讀題', '國文題型', '整合文字、數據、圖像與表格資訊', '中文解釋')
        compare_system.requires('作答圖表題', '方法', '看標題、圖例、單位、趨勢與文字關聯', '條件')

    @staticmethod
    def question_stem():
        compare_system.definition('題幹判讀', '考試策略', '辨認題目要求、範圍、人物與作答動詞', '中文解釋')
        compare_system.requires('讀題', '方法', '圈出最適當、不正確、主要、根據本文等關鍵詞', '條件')

    @staticmethod
    def negative_question():
        compare_system.definition('反向題', '考試題型', '要求選出不正確、不符合或無法推論的選項', '中文解釋')
        compare_system.requires('作答反向題', '方法', '先明確標記否定詞，避免看懂內容卻選反', '條件')

    @staticmethod
    def best_answer():
        compare_system.definition('最佳答案題', '選擇題', '多個選項似乎合理，但需選最完整符合文本者', '中文解釋')
        compare_system.requires('選最佳答案', '方法', '比較範圍、精確度與文本支持程度', '條件')

    @staticmethod
    def elimination():
        compare_system.definition('排除法', '選擇題策略', '先刪除明顯錯誤，再比較剩餘選項', '中文解釋')
        compare_system.requires('排除選項', '方法', '找無中生有、張冠李戴、過度推論與因果顛倒', '條件')

    @staticmethod
    def return_to_text():
        compare_system.definition('回文定位', '閱讀策略', '依題幹回到原文尋找相關句段', '中文解釋')
        compare_system.resultsin('回文定位', '考試效果', '降低只憑記憶與印象作答的錯誤', '結果')

    @staticmethod
    def evidence_answer():
        compare_system.definition('證據作答', '閱讀策略', '答案同時包含判斷與支持它的文本根據', '中文解釋')
        compare_system.requires('證據作答', '結構', '答案、證據、證據與答案的關聯', '條件')

    @staticmethod
    def short_answer():
        compare_system.definition('簡答題', '國文題型', '以精確文字回答指定內容或分析任務', '中文解釋')
        compare_system.requires('完成簡答題', '方法', '回答全部要求並避免抄寫無關原文', '條件')

    @staticmethod
    def comparison_answer():
        compare_system.definition('比較題作答', '閱讀策略', '使用共同標準分析兩個對象', '中文解釋')
        compare_system.requires('比較答案', '結構', '相同點、不同點與各自證據', '條件')

    @staticmethod
    def cause_answer():
        compare_system.definition('原因題作答', '閱讀策略', '說明事件發生或人物行動的原因', '中文解釋')
        compare_system.requires('原因答案', '方法', '分辨直接原因、深層原因與背景', '條件')

    @staticmethod
    def effect_answer():
        compare_system.definition('作用題作答', '閱讀策略', '分析詞句、段落或手法對內容與結構的效果', '中文解釋')
        compare_system.requires('作用答案', '結構', '寫了什麼、如何表達、產生什麼效果', '條件')

    @staticmethod
    def main_idea_answer():
        compare_system.definition('主旨題作答', '閱讀策略', '概括文本核心思想或情感', '中文解釋')
        compare_system.requires('主旨答案', '方法', '包含主要對象、核心事件與作者態度', '條件')

    @staticmethod
    def title_answer():
        compare_system.definition('標題題作答', '閱讀策略', '分析標題與內容、主旨、結構及讀者效果', '中文解釋')

    @staticmethod
    def translation_answer():
        compare_system.definition('文言翻譯題', '文言題型', '將文言句準確轉為通順現代漢語', '中文解釋')
        compare_system.requires('文言翻譯', '方法', '逐詞落實、補省略、調語序、不漏關鍵詞', '條件')

    @staticmethod
    def classical_comparison():
        compare_system.definition('文言比較題', '文言題型', '比較不同文本的思想、人物、語氣或寫法', '中文解釋')
        compare_system.requires('文言比較', '方法', '先分篇理解，再使用共同標準', '條件')

    @staticmethod
    def exam_time_management():
        compare_system.definition('國文考試時間管理', '考試策略', '依題型與難度分配閱讀、作答與檢查時間', '中文解釋')
        compare_system.requires('時間管理', '方法', '先穩定得分、卡題暫跳、最後回查', '條件')

    @staticmethod
    def first_pass():
        compare_system.definition('第一輪作答', '考試策略', '先完成能快速確定的題目', '中文解釋')
        compare_system.resultsin('第一輪作答', '考試效果', '建立基本分數並避免前段耗時過多', '結果')

    @staticmethod
    def mark_difficult():
        compare_system.definition('標記難題', '考試策略', '暫時保留需要更多時間的題目', '中文解釋')
        compare_system.requires('標記難題', '方法', '留下初步判斷與疑點，第二輪再處理', '條件')

    @staticmethod
    def final_check():
        compare_system.definition('最後檢查', '考試策略', '檢查漏題、題號、否定詞與答案卡', '中文解釋')

    @staticmethod
    def error_log():
        compare_system.definition('錯題紀錄', '學習方法', '記錄題目、錯誤答案、正解與錯因', '中文解釋')
        compare_system.requires('有效錯題本', '內容', '題型、知識點、錯誤原因與下次策略', '條件')

    @staticmethod
    def error_types():
        compare_system.definition('錯誤分類', '學習方法', '把錯誤分為知識不足、讀題錯誤、推論過度、粗心與時間問題', '中文解釋')

    @staticmethod
    def knowledge_error():
        compare_system.definition('知識型錯誤', '錯題類型', '因不熟字詞、文化常識或文言用法而答錯', '中文解釋')
        compare_system.requires('修正知識型錯誤', '方法', '回到概念整理並安排間隔複習', '條件')

    @staticmethod
    def reading_error():
        compare_system.definition('理解型錯誤', '錯題類型', '誤解文本主旨、指涉、因果或人物動機', '中文解釋')
        compare_system.requires('修正理解型錯誤', '方法', '重做文本結構與證據定位', '條件')

    @staticmethod
    def question_error():
        compare_system.definition('讀題型錯誤', '錯題類型', '忽略否定詞、比較範圍或作答要求', '中文解釋')
        compare_system.requires('修正讀題型錯誤', '方法', '圈題幹關鍵詞並完成後反向核對', '條件')

    @staticmethod
    def careless_error():
        compare_system.definition('粗心型錯誤', '錯題類型', '已理解但因抄錯、漏看或選錯題號失分', '中文解釋')
        compare_system.requires('降低粗心', '方法', '固定檢查順序並避免只告訴自己要小心', '條件')

    @staticmethod
    def spaced_review():
        compare_system.definition('間隔複習', '學習方法', '在逐漸拉長的時間間隔重複回想', '中文解釋')
        compare_system.resultsin('間隔複習', '學習效果', '提升長期記憶與提取能力', '結果')

    @staticmethod
    def active_recall():
        compare_system.definition('主動回想', '學習方法', '不看答案，先從記憶中提取內容', '中文解釋')
        compare_system.resultsin('主動回想', '學習效果', '比單純重讀更能檢查真正掌握程度', '結果')

    @staticmethod
    def mock_exam():
        compare_system.definition('模擬測驗', '備考方法', '在接近正式考試的時間與規則下作答', '中文解釋')
        compare_system.requires('模擬測驗後', '檢討', '分析錯誤、時間與作答順序', '條件')

    @staticmethod
    def writing_overview():
        compare_system.definition('國寫準備', '寫作評量', '培養理解材料、組織觀點、描述經驗與文字表達能力', '中文解釋')
        compare_system.requires('國寫進步', '方法', '閱讀、觀察、練筆、回饋與重寫', '條件')

    @staticmethod
    def writing_prompt_analysis():
        compare_system.definition('國寫審題', '寫作步驟', '分析引導文字、核心概念、限制與寫作任務', '中文解釋')
        compare_system.requires('國寫審題', '方法', '圈關鍵詞、確認要回答幾個層次', '條件')

    @staticmethod
    def material_interpretation():
        compare_system.definition('材料解讀', '國寫能力', '理解文字、圖表、情境或案例所提供的訊息', '中文解釋')
        compare_system.requires('材料解讀', '方法', '摘要共同核心，區分材料觀點與自己觀點', '條件')

    @staticmethod
    def writing_thesis():
        compare_system.definition('中心立意', '國寫', '全文欲傳達的核心觀點或感受', '中文解釋')
        compare_system.requires('有效立意', '條件', '回應題目、集中、具體並有思考深度', '條件')

    @staticmethod
    def writing_outline():
        compare_system.definition('國寫大綱', '寫作工具', '在動筆前安排開頭、段落重點、例證與結尾', '中文解釋')
        compare_system.resultsin('先列大綱', '寫作效果', '降低離題、重複與結構混亂', '結果')

    @staticmethod
    def rational_writing():
        compare_system.definition('知性題寫作', '國寫類型', '分析概念、材料、原因、影響或解決方案', '中文解釋')
        compare_system.requires('知性題', '寫作', '觀點明確、邏輯完整、證據具體', '條件')

    @staticmethod
    def emotional_writing():
        compare_system.definition('情意題寫作', '國寫類型', '由經驗、感受與觀察呈現生命理解', '中文解釋')
        compare_system.requires('情意題', '寫作', '真實情境、具體細節、情感轉折與反思', '條件')

    @staticmethod
    def argument_structure():
        compare_system.definition('議論結構', '國寫', '提出論點、給予理由、使用證據並回應限制', '中文解釋')
        compare_system.partof('論點', '議論結構', '議論文', '內容')
        compare_system.partof('論據', '議論結構', '議論文', '內容')
        compare_system.partof('論證', '議論結構', '議論文', '內容')

    @staticmethod
    def narrative_structure():
        compare_system.definition('敘事結構', '國寫', '以事件、衝突、轉折與反思組織經驗', '中文解釋')
        compare_system.requires('有效敘事', '方法', '選擇關鍵時刻，不寫成流水帳', '條件')

    @staticmethod
    def opening_strategy():
        compare_system.definition('國寫開頭', '寫作技巧', '快速建立情境、問題或立場', '中文解釋')
        compare_system.requires('國寫開頭', '條件', '簡潔、扣題並能引向全文', '條件')

    @staticmethod
    def ending_strategy():
        compare_system.definition('國寫結尾', '寫作技巧', '收束內容並深化主旨', '中文解釋')
        compare_system.requires('國寫結尾', '條件', '避免突然停止或只重複題目', '條件')

    @staticmethod
    def example_selection():
        compare_system.definition('例證選擇', '議論寫作', '選擇能直接支持論點的事例或資料', '中文解釋')
        compare_system.requires('好例證', '條件', '真實、具體、相關且不過度老套', '條件')

    @staticmethod
    def personal_experience():
        compare_system.definition('個人經驗材料', '情意寫作', '從自身生活中選擇可呈現主題的事件', '中文解釋')
        compare_system.requires('使用個人經驗', '方法', '寫具體場景與變化，而非只下結論', '條件')

    @staticmethod
    def public_issue():
        compare_system.definition('公共議題材料', '議論寫作', '從社會、科技、環境、教育等議題建立觀點', '中文解釋')
        compare_system.requires('討論公共議題', '方法', '辨認不同立場並使用可信資料', '條件')

    @staticmethod
    def counterargument_writing():
        compare_system.definition('回應反方', '議論技巧', '承認另一觀點的合理部分，再說明限制', '中文解釋')
        compare_system.resultsin('回應反方', '寫作效果', '使論證更完整且不流於單方面宣告', '結果')

    @staticmethod
    def paragraph_unity():
        compare_system.definition('段落統一性', '寫作品質', '一個段落集中處理一個主要重點', '中文解釋')
        compare_system.requires('段落統一', '方法', '刪除與主題句無關的內容', '條件')

    @staticmethod
    def paragraph_development():
        compare_system.definition('段落發展', '寫作品質', '用解釋、細節、例子與分析展開主題句', '中文解釋')

    @staticmethod
    def transition_writing():
        compare_system.definition('作文轉承', '寫作技巧', '連結段落、時間、觀點與情緒轉折', '中文解釋')
        compare_system.requires('自然轉承', '方法', '依實際邏輯使用轉折、因果、補充與總結', '條件')

    @staticmethod
    def concrete_detail():
        compare_system.definition('具體細節', '寫作技巧', '以動作、對話、感官與物件呈現經驗', '中文解釋')
        compare_system.resultsin('具體細節', '寫作效果', '增加畫面、可信度與感染力', '結果')

    @staticmethod
    def show_not_tell():
        compare_system.definition('以描寫呈現', '寫作技巧', '讓人物行動與細節表現情感，而非只直接宣告', '中文解釋')

    @staticmethod
    def language_accuracy():
        compare_system.definition('語言準確', '寫作評量', '用詞、句法、標點與指涉正確清楚', '中文解釋')

    @staticmethod
    def language_fluency():
        compare_system.definition('語言流暢', '寫作評量', '句子自然、段落連貫且節奏適當', '中文解釋')

    @staticmethod
    def language_depth():
        compare_system.definition('表達深度', '寫作評量', '能由事件或材料提出進一步理解與反思', '中文解釋')

    @staticmethod
    def avoid_cliches():
        compare_system.definition('避免套語', '寫作技巧', '避免大量使用與內容無直接關係的固定名言或模板', '中文解釋')
        compare_system.requires('使用名言', '方法', '確定來源、語意與文章論點真正相關', '條件')

    @staticmethod
    def avoid_empty_language():
        compare_system.definition('避免空泛', '寫作技巧', '不要只寫重要、努力、感動等抽象結論', '中文解釋')
        compare_system.requires('改善空泛', '方法', '補充誰、何時、做什麼、如何改變', '條件')

    @staticmethod
    def avoid_stream_of_events():
        compare_system.definition('避免流水帳', '寫作技巧', '不要平均記錄每個步驟而缺乏重點', '中文解釋')
        compare_system.requires('改善流水帳', '方法', '聚焦衝突、轉折與最有意義的片段', '條件')

    @staticmethod
    def avoid_off_topic():
        compare_system.definition('避免離題', '寫作技巧', '每段都應回應題目核心概念', '中文解釋')
        compare_system.requires('檢查離題', '方法', '寫完每段後問它如何支持主旨', '條件')

    @staticmethod
    def writing_revision():
        compare_system.definition('國寫修改', '寫作流程', '檢查內容、結構、語言與格式', '中文解釋')
        compare_system.requires('修改順序', '方法', '先處理立意結構，再處理句子字詞', '條件')

    @staticmethod
    def writing_proofreading():
        compare_system.definition('國寫校對', '寫作流程', '檢查錯別字、漏字、標點與段落格式', '中文解釋')

    @staticmethod
    def writing_time_management():
        compare_system.definition('國寫時間管理', '考試策略', '合理分配審題、構思、書寫與檢查時間', '中文解釋')
        compare_system.requires('國寫時間分配', '方法', '預留最後數分鐘檢查，不邊想邊無限重寫開頭', '條件')

    @staticmethod
    def writing_score_content():
        compare_system.definition('內容評量', '作文評分', '檢查是否切題、材料充實且具有深度', '中文解釋')

    @staticmethod
    def writing_score_structure():
        compare_system.definition('組織評量', '作文評分', '檢查段落安排、前後連貫與整體結構', '中文解釋')

    @staticmethod
    def writing_score_language():
        compare_system.definition('語言評量', '作文評分', '檢查用詞、句式、流暢度與錯誤', '中文解釋')

    @staticmethod
    def writing_score_format():
        compare_system.definition('卷面格式', '作文評分', '字跡、分段、標點與整潔度影響可讀性', '中文解釋')

    @staticmethod
    def writing_self_check():
        compare_system.definition('作文自我檢查', '寫作策略', '依題意、立意、材料、結構、語言逐項檢查', '中文解釋')
        compare_system.requires('作文完成前', '檢查', '是否扣題、是否有具體材料、結尾是否收束', '條件')

    @staticmethod
    def study_plan():
        compare_system.definition('國文讀書計畫', '備考方法', '依弱點安排知識、閱讀、文言與作文練習', '中文解釋')
        compare_system.requires('讀書計畫', '條件', '具體、可執行、可檢查並保留調整空間', '條件')

    @staticmethod
    def daily_reading():
        compare_system.definition('每日閱讀', '備考方法', '固定閱讀不同文體並做簡短摘要與分析', '中文解釋')
        compare_system.resultsin('每日閱讀', '學習效果', '提升速度、語感、背景知識與理解能力', '結果')

    @staticmethod
    def weekly_writing():
        compare_system.definition('定期寫作', '備考方法', '每週完成短文、段落或完整作文並重寫', '中文解釋')
        compare_system.resultsin('定期寫作', '學習效果', '累積材料並改善組織與表達', '結果')

    @staticmethod
    def vocabulary_review():
        compare_system.definition('字詞複習', '備考方法', '整理字音、字形、成語、文言字義與錯題', '中文解釋')

    @staticmethod
    def classical_review():
        compare_system.definition('文言複習', '備考方法', '按實詞、虛詞、句式、翻譯與篇章理解分類', '中文解釋')

    @staticmethod
    def reading_review():
        compare_system.definition('閱讀複習', '備考方法', '不只重看答案，而要重建題幹、證據與推理', '中文解釋')

    @staticmethod
    def exam_day():
        compare_system.definition('考試當日策略', '考試準備', '保持正常作息、確認工具並依固定流程作答', '中文解釋')
        compare_system.requires('考試當日', '方法', '先讀清題幹、穩定節奏、遇難題不慌張', '條件')
