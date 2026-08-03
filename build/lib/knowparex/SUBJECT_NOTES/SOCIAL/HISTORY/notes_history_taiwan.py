from knowparex.PROGRAMMING_NOTES import compare_system
class history_taiwan:
    @staticmethod
    def historical_sources():
        compare_system.definition('史料', '歷史學', '研究過去人類活動所使用的文字、器物、影像與口述等材料', '中文解釋')
        compare_system.related('史料判讀', '歷史能力', '來源、年代、作者立場與可信度', '重點')

    @staticmethod
    def prehistoric_taiwan():
        compare_system.definition('史前時代', '臺灣史', '尚未留下可解讀文字記錄的時代', '中文解釋')
        compare_system.related('長濱文化', '臺灣史前文化', '舊石器時代', '時期')
        compare_system.related('大坌坑文化', '臺灣史前文化', '新石器時代早期', '時期')
        compare_system.related('十三行文化', '臺灣史前文化', '金屬器時代', '時期')

    @staticmethod
    def austronesian_peoples():
        compare_system.definition('南島語族', '族群與語言', '分布於臺灣、東南亞島嶼與太平洋廣大區域的語族', '中文解釋')
        compare_system.related('臺灣原住民族', '臺灣歷史', '南島語族', '語言文化關係')

    @staticmethod
    def dutch_spanish_rule():
        compare_system.definition('荷蘭統治臺灣', '臺灣史', '1624年至1662年間荷蘭東印度公司在臺灣南部建立統治', '中文解釋')
        compare_system.definition('西班牙統治臺灣北部', '臺灣史', '1626年至1642年間西班牙在臺灣北部建立據點', '中文解釋')
        compare_system.resultsin('荷蘭擊敗西班牙', '歷史事件', '西班牙退出臺灣北部', '結果')

    @staticmethod
    def zheng_rule():
        compare_system.definition('鄭氏政權', '臺灣史', '1662年至1683年間以臺灣為基地的漢人政權', '中文解釋')
        compare_system.related('鄭成功', '人物', '驅逐荷蘭並建立鄭氏政權', '事蹟')
        compare_system.resultsin('屯墾政策', '鄭氏治理', '農地開發與漢人移入增加', '結果')

    @staticmethod
    def qing_rule():
        compare_system.definition('清治臺灣', '臺灣史', '1683年至1895年間臺灣受清帝國統治', '中文解釋')
        compare_system.related('渡臺禁令', '政策', '限制部分漢人渡臺與攜眷', '目的')
        compare_system.related('分類械鬥', '社會衝突', '不同祖籍或群體之間的衝突', '中文解釋')

    @staticmethod
    def qing_late_reforms():
        compare_system.related('沈葆楨', '人物', '清末來臺推動防務與行政改革', '事蹟')
        compare_system.related('劉銘傳', '人物', '推動臺灣建省與近代化建設', '事蹟')
        compare_system.resultsin('臺灣建省', '行政改革', '臺灣行政地位提高', '結果')

    @staticmethod
    def treaty_of_shimonoseki():
        compare_system.definition('馬關條約', '條約', '1895年清日戰爭後簽訂的條約', '中文解釋')
        compare_system.resultsin('馬關條約', '歷史結果', '臺灣與澎湖割讓給日本', '結果')

    @staticmethod
    def japanese_rule():
        compare_system.definition('日本統治臺灣', '臺灣史', '1895年至1945年間臺灣受日本帝國統治', '中文解釋')
        compare_system.related('臺灣總督府', '統治機構', '日本統治臺灣的最高行政機關', '功能')
        compare_system.related('保甲制度', '地方控制', '協助行政、治安與戶口管理', '功能')

    @staticmethod
    def japanese_economy_society():
        compare_system.related('糖業與蓬萊米', '殖民經濟', '日本時代重要農業與出口項目', '關係')
        compare_system.related('嘉南大圳', '水利建設', '改善嘉南平原灌溉', '功能')
        compare_system.related('公共衛生與學校教育', '殖民治理', '現代制度建設但存在差別待遇', '特徵')

    @staticmethod
    def political_movements():
        compare_system.definition('臺灣議會設置請願運動', '政治運動', '1920年代起要求設置臺灣議會的運動', '中文解釋')
        compare_system.related('臺灣文化協會', '社會運動', '推動文化啟蒙與民族意識', '功能')
        compare_system.related('蔣渭水與林獻堂', '人物', '臺灣政治社會運動的重要參與者', '關係')

    @staticmethod
    def kominka():
        compare_system.definition('皇民化運動', '日本統治後期', '強化日本國民認同與戰爭動員的政策', '中文解釋')
        compare_system.related('國語運動與改姓名', '皇民化措施', '推廣日語與日本式姓名', '內容')

    @staticmethod
    def postwar_takeover():
        compare_system.definition('戰後接收臺灣', '臺灣史', '1945年第二次世界大戰結束後中華民國政府接管臺灣', '中文解釋')
        compare_system.related('臺灣省行政長官公署', '接收機構', '戰後初期治理臺灣的機關', '功能')

    @staticmethod
    def february_28():
        compare_system.definition('二二八事件', '臺灣史', '1947年因查緝私菸衝突引發並擴大的政治與社會事件', '中文解釋')
        compare_system.causes('行政失序、經濟困難與社會矛盾', '背景', '二二八事件', '結果')
        compare_system.resultsin('二二八事件', '歷史影響', '大量傷亡與長期政治創傷', '結果')

    @staticmethod
    def martial_law_white_terror():
        compare_system.definition('戒嚴時期', '臺灣史', '1949年至1987年間臺灣長期實施戒嚴的時期', '中文解釋')
        compare_system.definition('白色恐怖', '政治史', '國家以逮捕、審判與監控壓制異議的歷史現象', '中文解釋')

    @staticmethod
    def economic_development():
        compare_system.related('土地改革', '戰後經濟', '三七五減租、公地放領與耕者有其田', '內容')
        compare_system.related('進口替代與出口導向', '經濟政策', '推動工業化與外銷成長', '功能')
        compare_system.related('十大建設', '公共建設', '改善交通、能源與工業基礎', '功能')

    @staticmethod
    def democratization():
        compare_system.definition('民主化', '臺灣政治史', '政治權力逐步開放、競爭與受人民監督的過程', '中文解釋')
        compare_system.related('解除戒嚴', '民主化', '1987年臺灣結束戒嚴', '關係')
        compare_system.related('總統直選', '民主改革', '人民直接選舉總統', '結果')
        compare_system.related('政黨輪替', '民主政治', '透過選舉和平轉移執政權', '中文解釋')

    @staticmethod
    def transitional_justice():
        compare_system.definition('轉型正義', '民主政治', '處理威權統治遺留的不義、真相與制度問題', '中文解釋')
        compare_system.related('政治檔案、平反與賠償', '轉型正義', '釐清真相與修復社會', '功能')

