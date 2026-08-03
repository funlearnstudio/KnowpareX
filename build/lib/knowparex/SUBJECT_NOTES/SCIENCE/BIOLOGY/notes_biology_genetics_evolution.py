# ===========================================
# notes_biology_genetics_evolution.py
# 生物：細胞分裂、遺傳、DNA、演化與分類
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class biology_genetics_evolution:

    @staticmethod
    def chromosome():
        compare_system.equivalentto("染色體", "遺傳構造", "由 DNA 與蛋白質組成並攜帶遺傳資訊的構造", "定義")
        compare_system.equal("染色體主要成分", "題目", "DNA 與組蛋白", "答案")
        compare_system.equal("同源染色體", "關係", "大小形狀相似並具有相同基因座", "答案")
        compare_system.equal("一對同源染色體", "來源", "一條來自父方、一條來自母方", "答案")
        compare_system.equal("姐妹染色分體", "形成", "同一染色體複製後的兩份相同結構", "答案")
        compare_system.notequal("同源染色體", "敘述", "基因型必定完全相同", "錯誤觀念")

    @staticmethod
    def cell_cycle():
        compare_system.equivalentto("細胞週期", "生物過程", "細胞由一次分裂完成至下一次分裂完成的過程", "定義")
        compare_system.equal("細胞週期主要階段", "題目", "間期與分裂期", "答案")
        compare_system.equal("DNA 複製", "主要時期", "間期的 S 期", "答案")
        compare_system.equal("G₁ 期", "主要活動", "細胞生長與製造蛋白質", "答案")
        compare_system.equal("G₂ 期", "主要活動", "分裂前準備", "答案")
        compare_system.equal("細胞週期檢查點", "功能", "監控 DNA 與分裂條件", "答案")
        compare_system.notequal("間期", "敘述", "細胞完全沒有活動", "錯誤觀念")

    @staticmethod
    def mitosis():
        compare_system.equivalentto("有絲分裂", "細胞分裂", "產生遺傳資訊通常相同之兩個子細胞的核分裂", "定義")
        compare_system.equal("有絲分裂主要功能", "多細胞生物", "生長、修補與無性生殖", "答案")
        compare_system.equal("有絲分裂後染色體套數", "關係", "通常與母細胞相同", "答案")
        compare_system.equal("前期", "主要事件", "染色體凝縮、紡錘體形成", "答案")
        compare_system.equal("中期", "主要事件", "染色體排列於赤道面", "答案")
        compare_system.equal("後期", "主要事件", "姐妹染色分體分離", "答案")
        compare_system.equal("末期", "主要事件", "兩組染色體形成新細胞核", "答案")
        compare_system.notequal("有絲分裂", "敘述", "會使染色體套數減半", "錯誤觀念")

    @staticmethod
    def meiosis():
        compare_system.equivalentto("減數分裂", "細胞分裂", "產生染色體套數減半之生殖細胞的分裂", "定義")
        compare_system.equal("減數分裂", "分裂次數", "連續兩次核分裂", "答案")
        compare_system.equal("DNA 複製", "減數分裂", "只在第一次分裂前進行一次", "答案")
        compare_system.equal("減數分裂第一分裂", "主要分離", "同源染色體", "答案")
        compare_system.equal("減數分裂第二分裂", "主要分離", "姐妹染色分體", "答案")
        compare_system.equal("減數分裂後", "子細胞數", "通常為 4 個", "答案")
        compare_system.equal("減數分裂後染色體套數", "結果", "減半", "答案")
        compare_system.notequal("減數分裂產生的四個細胞", "敘述", "遺傳組成完全相同", "錯誤觀念")

    @staticmethod
    def crossing_over():
        compare_system.equivalentto("互換", "遺傳現象", "同源染色體非姐妹染色分體交換對應片段", "定義")
        compare_system.equal("互換主要時期", "減數分裂", "第一分裂前期", "答案")
        compare_system.equal("互換", "結果", "產生新的等位基因組合", "答案")
        compare_system.equal("獨立分配", "結果", "增加配子遺傳組合多樣性", "答案")
        compare_system.equal("隨機受精", "結果", "增加子代遺傳多樣性", "答案")
        compare_system.notequal("互換", "敘述", "發生於姐妹染色分體的完全相同位置並毫無影響", "錯誤觀念")

    @staticmethod
    def dna():
        compare_system.equivalentto("DNA", "遺傳物質", "儲存生物遺傳資訊的去氧核糖核酸", "定義")
        compare_system.equal("DNA 基本單位", "題目", "核苷酸", "答案")
        compare_system.equal("DNA 核苷酸組成", "題目", "磷酸、去氧核糖與含氮鹼基", "答案")
        compare_system.equal("DNA 鹼基", "題目", "A、T、C、G", "答案")
        compare_system.equal("DNA 結構", "典型形態", "雙股螺旋", "答案")
        compare_system.equal("A", "互補鹼基", "T", "答案")
        compare_system.equal("C", "互補鹼基", "G", "答案")
        compare_system.notequal("DNA", "敘述", "只存在細胞核而不可能出現在其他細胞器", "錯誤觀念")

    @staticmethod
    def dna_replication():
        compare_system.equivalentto("DNA 複製", "遺傳過程", "以原有 DNA 為模板合成新 DNA 的過程", "定義")
        compare_system.equivalentto("半保留複製", "DNA 複製", "每個新 DNA 含一股舊鏈與一股新鏈", "定義")
        compare_system.equal("解旋酶", "功能", "分開 DNA 雙股", "答案")
        compare_system.equal("DNA 聚合酶", "功能", "依模板加入互補核苷酸", "答案")
        compare_system.equal("DNA 複製方向", "新鏈延伸", "5' 端向 3' 端", "答案")
        compare_system.equal("DNA 複製", "發生時機", "細胞分裂前", "答案")
        compare_system.notequal("DNA 複製", "敘述", "通常完全沒有任何錯誤或校對機制", "錯誤觀念")

    @staticmethod
    def gene():
        compare_system.equivalentto("基因", "遺傳單位", "DNA 上能產生功能性 RNA 或影響性狀的片段", "定義")
        compare_system.equivalentto("基因座", "位置", "基因在染色體上的位置", "定義")
        compare_system.equivalentto("等位基因", "基因形式", "同一基因座上不同版本的基因", "定義")
        compare_system.equal("基因", "功能", "可影響蛋白質、RNA 與性狀", "答案")
        compare_system.equal("同源染色體", "基因座", "通常具有相同種類基因", "答案")
        compare_system.notequal("一個基因", "敘述", "永遠只控制一個完全獨立且簡單的性狀", "錯誤觀念")

    @staticmethod
    def rna():
        compare_system.equivalentto("RNA", "核酸", "由核糖核苷酸組成並參與基因表現的核酸", "定義")
        compare_system.equal("RNA 糖", "題目", "核糖", "答案")
        compare_system.equal("RNA 鹼基", "題目", "A、U、C、G", "答案")
        compare_system.equal("RNA", "典型股數", "通常為單股", "答案")
        compare_system.equal("mRNA", "功能", "攜帶蛋白質合成資訊", "答案")
        compare_system.equal("tRNA", "功能", "攜帶胺基酸至核糖體", "答案")
        compare_system.equal("rRNA", "功能", "構成核糖體並參與催化", "答案")
        compare_system.notequal("RNA", "敘述", "一定只存在細胞核", "錯誤觀念")

    @staticmethod
    def transcription():
        compare_system.equivalentto("轉錄", "基因表現", "以 DNA 為模板合成 RNA 的過程", "定義")
        compare_system.equal("轉錄主要酵素", "題目", "RNA 聚合酶", "答案")
        compare_system.equal("真核細胞轉錄", "主要位置", "細胞核", "答案")
        compare_system.equal("轉錄產物", "可能種類", "mRNA、tRNA 或 rRNA", "答案")
        compare_system.equal("RNA 與 DNA 配對", "A 對應", "U", "答案")
        compare_system.equal("RNA 與 DNA 配對", "C 對應", "G", "答案")
        compare_system.notequal("轉錄", "概念", "DNA 直接變成蛋白質", "錯誤觀念")

    @staticmethod
    def translation():
        compare_system.equivalentto("轉譯", "基因表現", "核糖體依 mRNA 密碼子序列合成蛋白質的過程", "定義")
        compare_system.equal("轉譯場所", "題目", "核糖體", "答案")
        compare_system.equivalentto("密碼子", "遺傳密碼", "mRNA 上連續三個鹼基", "定義")
        compare_system.equivalentto("反密碼子", "tRNA", "與 mRNA 密碼子互補的三個鹼基", "定義")
        compare_system.equal("起始密碼子", "常見", "AUG", "答案")
        compare_system.equal("AUG", "編碼胺基酸", "甲硫胺酸", "答案")
        compare_system.equal("終止密碼子", "功能", "停止轉譯", "答案")
        compare_system.notequal("一個密碼子", "敘述", "由兩個鹼基組成", "錯誤觀念")

    @staticmethod
    def central_dogma():
        compare_system.equivalentto("中心法則", "遺傳資訊流", "DNA 經轉錄形成 RNA，再經轉譯形成蛋白質", "定義")
        compare_system.equal("DNA → DNA", "過程", "複製", "答案")
        compare_system.equal("DNA → RNA", "過程", "轉錄", "答案")
        compare_system.equal("RNA → 蛋白質", "過程", "轉譯", "答案")
        compare_system.equal("蛋白質", "功能", "可參與構造、運輸、催化與調節", "答案")
        compare_system.notequal("中心法則", "敘述", "蛋白質資訊通常可直接反向轉成 DNA 序列", "錯誤觀念")

    @staticmethod
    def mendel_law():
        compare_system.equivalentto("分離律", "孟德爾定律", "一對等位基因在配子形成時彼此分離", "定義")
        compare_system.equivalentto("獨立分配律", "孟德爾定律", "不同基因對在特定條件下彼此獨立分配", "定義")
        compare_system.equal("孟德爾研究生物", "題目", "豌豆", "答案")
        compare_system.equal("純品系", "特徵", "自交後特定性狀穩定出現", "答案")
        compare_system.equal("單因子雜交 F₂ 表現型比例", "完全顯性理想情況", "3：1", "答案")
        compare_system.equal("單因子雜交 F₂ 基因型比例", "理想情況", "1：2：1", "答案")
        compare_system.notequal("獨立分配律", "敘述", "所有位於同一染色體的基因都完全獨立", "錯誤觀念")

    @staticmethod
    def genotype_phenotype():
        compare_system.equivalentto("基因型", "遺傳概念", "個體具有的等位基因組合", "定義")
        compare_system.equivalentto("表現型", "遺傳概念", "可觀察或測量的性狀表現", "定義")
        compare_system.equivalentto("同型合子", "基因型", "同一基因座具有兩個相同等位基因", "定義")
        compare_system.equivalentto("異型合子", "基因型", "同一基因座具有兩個不同等位基因", "定義")
        compare_system.equal("AA", "基因型", "顯性同型合子", "答案")
        compare_system.equal("Aa", "基因型", "異型合子", "答案")
        compare_system.equal("aa", "基因型", "隱性同型合子", "答案")
        compare_system.notequal("相同表現型", "敘述", "基因型必定完全相同", "錯誤觀念")

    @staticmethod
    def dominance():
        compare_system.equivalentto("完全顯性", "遺傳模式", "異型合子表現與顯性同型合子相同", "定義")
        compare_system.equivalentto("不完全顯性", "遺傳模式", "異型合子表現介於兩種同型合子之間", "定義")
        compare_system.equivalentto("共顯性", "遺傳模式", "異型合子中兩個等位基因皆明顯表現", "定義")
        compare_system.equal("紅花與白花產生粉紅花", "遺傳模式", "不完全顯性", "答案")
        compare_system.equal("AB 血型", "遺傳模式", "IA 與 IB 共顯性", "答案")
        compare_system.notequal("顯性等位基因", "敘述", "在人群中一定比較常見或比較有利", "錯誤觀念")

    @staticmethod
    def blood_type():
        compare_system.equal("ABO 血型等位基因", "題目", "IA、IB、i", "答案")
        compare_system.equal("A 型血可能基因型", "題目", "IAIA 或 IAi", "答案")
        compare_system.equal("B 型血可能基因型", "題目", "IBIB 或 IBi", "答案")
        compare_system.equal("AB 型血基因型", "題目", "IAIB", "答案")
        compare_system.equal("O 型血基因型", "題目", "ii", "答案")
        compare_system.equal("IA 與 IB", "關係", "共顯性", "答案")
        compare_system.equal("IA 與 i", "關係", "IA 對 i 顯性", "答案")

    @staticmethod
    def sex_linked():
        compare_system.equivalentto("性聯遺傳", "遺傳模式", "基因位於性染色體上的遺傳", "定義")
        compare_system.equal("人類女性性染色體", "一般情況", "XX", "答案")
        compare_system.equal("人類男性性染色體", "一般情況", "XY", "答案")
        compare_system.equal("X 聯隱性性狀", "男性", "一個致病等位基因即可表現", "答案")
        compare_system.equal("紅綠色盲", "常見遺傳", "X 聯隱性", "答案")
        compare_system.equal("血友病部分類型", "常見遺傳", "X 聯隱性", "答案")
        compare_system.notequal("所有性別差異性狀", "敘述", "都由性染色體基因直接控制", "錯誤觀念")

    @staticmethod
    def mutation():
        compare_system.equivalentto("突變", "遺傳變化", "DNA 序列或染色體結構、數目發生改變", "定義")
        compare_system.equal("突變", "來源", "可自然發生或由誘變因子造成", "答案")
        compare_system.equal("體細胞突變", "遺傳給下一代", "通常不會經有性生殖直接遺傳", "答案")
        compare_system.equal("生殖細胞突變", "遺傳", "可能傳給下一代", "答案")
        compare_system.equal("突變", "演化意義", "提供新的遺傳變異", "答案")
        compare_system.notequal("突變", "敘述", "一定對生物有害", "錯誤觀念")
        compare_system.notequal("突變", "敘述", "一定會造成明顯表現型改變", "錯誤觀念")

    @staticmethod
    def biotechnology():
        compare_system.equivalentto("生物技術", "應用領域", "利用生物體、細胞或生物分子製造產品與解決問題", "定義")
        compare_system.equivalentto("基因工程", "技術", "直接操作或重組 DNA 的技術", "定義")
        compare_system.equal("限制酶", "功能", "辨識特定 DNA 序列並切割", "答案")
        compare_system.equal("DNA 連接酶", "功能", "連接 DNA 片段", "答案")
        compare_system.equal("質體", "用途", "常作為細菌基因轉殖載體", "答案")
        compare_system.equal("重組胰島素", "製造方式", "可利用基因工程微生物生產", "答案")
        compare_system.notequal("基因改造生物", "敘述", "所有風險與效益都完全相同", "錯誤觀念")

    @staticmethod
    def pcr():
        compare_system.equivalentto("PCR", "分子技術", "聚合酶連鎖反應，可大量擴增特定 DNA 片段", "定義")
        compare_system.equal("PCR 第一階段", "名稱", "變性", "答案")
        compare_system.equal("PCR 第二階段", "名稱", "引子黏合", "答案")
        compare_system.equal("PCR 第三階段", "名稱", "延伸", "答案")
        compare_system.equal("PCR", "必要材料", "模板 DNA、引子、核苷酸與耐熱 DNA 聚合酶", "答案")
        compare_system.equal("PCR 循環增加", "結果", "目標 DNA 片段近似指數增加", "答案")
        compare_system.notequal("PCR", "敘述", "直接將 DNA 轉譯成蛋白質", "錯誤觀念")

    @staticmethod
    def evolution():
        compare_system.equivalentto("演化", "生物概念", "族群遺傳特徵隨世代改變的過程", "定義")
        compare_system.equal("演化的單位", "題目", "族群而非單一個體", "答案")
        compare_system.equal("演化所需基礎", "題目", "可遺傳變異", "答案")
        compare_system.equal("突變與基因重組", "作用", "提供遺傳變異", "答案")
        compare_system.equal("自然選擇", "作用", "改變族群中等位基因與性狀比例", "答案")
        compare_system.notequal("個體適應環境", "敘述", "會因需要主動產生並遺傳有利突變", "錯誤觀念")

    @staticmethod
    def natural_selection():
        compare_system.equivalentto("自然選擇", "演化機制", "具有較適合環境性狀的個體留下較多可育後代", "定義")
        compare_system.equal("自然選擇作用對象", "直接", "個體的表現型", "答案")
        compare_system.equal("自然選擇演化結果", "族群", "等位基因頻率改變", "答案")
        compare_system.equal("適應度", "定義", "個體對下一代基因庫的相對貢獻", "答案")
        compare_system.equal("抗生素抗藥性", "演化", "抗藥菌在選擇壓力下比例上升", "答案")
        compare_system.notequal("自然選擇", "敘述", "為族群未來需要而預先設計性狀", "錯誤觀念")
        compare_system.notequal("最強壯個體", "敘述", "在所有環境中適應度一定最高", "錯誤觀念")

    @staticmethod
    def evidence_evolution():
        compare_system.equal("化石", "演化證據", "記錄過去生物與形態變化", "答案")
        compare_system.equal("同源構造", "意義", "可能顯示共同祖先", "答案")
        compare_system.equal("痕跡構造", "意義", "可能是祖先功能構造退化後的遺留", "答案")
        compare_system.equal("胚胎發育相似性", "意義", "可提供親緣關係線索", "答案")
        compare_system.equal("DNA 與蛋白質序列", "用途", "比較生物親緣關係", "答案")
        compare_system.equal("地理分布", "用途", "支持物種演化與隔離歷史", "答案")
        compare_system.notequal("任何兩種相似構造", "敘述", "都必定是同源構造", "錯誤觀念")

    @staticmethod
    def speciation():
        compare_system.equivalentto("物種形成", "演化過程", "族群逐漸產生生殖隔離並形成不同物種", "定義")
        compare_system.equal("地理隔離", "可能作用", "減少族群間基因交流", "答案")
        compare_system.equal("生殖隔離", "結果", "不同族群無法產生可育後代", "答案")
        compare_system.equal("突變、選擇與漂變", "作用", "使隔離族群逐漸分化", "答案")
        compare_system.equal("異域物種形成", "特徵", "由地理隔離促成", "答案")
        compare_system.notequal("物種形成", "敘述", "必須在單一世代瞬間完成", "錯誤觀念")

    @staticmethod
    def classification():
        compare_system.equivalentto("生物分類", "科學方法", "依共同特徵與演化關係整理生物", "定義")
        compare_system.equal("分類階層由大到小", "傳統順序", "界、門、綱、目、科、屬、種", "答案")
        compare_system.equal("種", "分類階層", "傳統分類基本單位", "答案")
        compare_system.equal("學名", "命名方式", "雙名法", "答案")
        compare_system.equal("雙名法第一字", "代表", "屬名", "答案")
        compare_system.equal("雙名法第二字", "代表", "種小名", "答案")
        compare_system.equal("屬名", "書寫", "第一個字母大寫", "答案")
        compare_system.notequal("外形相似", "敘述", "即可完全確定親緣關係最近", "錯誤觀念")

    @staticmethod
    def domains():
        compare_system.equal("三域系統", "分類", "細菌域、古菌域、真核生物域", "答案")
        compare_system.equal("細菌域", "細胞種類", "原核細胞", "答案")
        compare_system.equal("古菌域", "細胞種類", "原核細胞", "答案")
        compare_system.equal("真核生物域", "細胞種類", "真核細胞", "答案")
        compare_system.equal("古菌與細菌", "關係", "皆為原核生物但分屬不同域", "答案")
        compare_system.notequal("原核生物", "敘述", "全部屬於同一個域", "錯誤觀念")

    @staticmethod
    def virus():
        compare_system.equivalentto("病毒", "非細胞型感染因子", "由遺傳物質與蛋白質外殼等構成並依賴宿主複製", "定義")
        compare_system.equal("病毒遺傳物質", "種類", "DNA 或 RNA", "答案")
        compare_system.equal("病毒", "細胞構造", "沒有完整細胞構造", "答案")
        compare_system.equal("病毒複製", "條件", "必須利用宿主細胞系統", "答案")
        compare_system.equal("抗生素", "對病毒感染", "通常無效", "答案")
        compare_system.equal("疫苗", "作用", "訓練免疫系統辨識特定病原", "答案")
        compare_system.notequal("病毒", "敘述", "可在一般營養液中自行生長繁殖", "錯誤觀念")