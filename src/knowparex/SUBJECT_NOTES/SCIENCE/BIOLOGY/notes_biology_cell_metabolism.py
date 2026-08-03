# ===========================================
# notes_biology_cell_metabolism.py
# 生物：細胞、物質運輸、代謝與酵素
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class biology_cell_metabolism:

    @staticmethod
    def cell_theory():
        compare_system.equivalentto("細胞學說", "生物概念", "生物體由一個或多個細胞組成", "定義")
        compare_system.equal("細胞", "生物體", "構造與功能的基本單位", "答案")
        compare_system.equal("新細胞", "來源", "由原有細胞分裂產生", "答案")
        compare_system.equal("單細胞生物", "特徵", "一個細胞即可完成生命活動", "答案")
        compare_system.equal("多細胞生物", "特徵", "由許多分化細胞共同組成", "答案")
        compare_system.equal("細胞學說", "適用範圍", "所有已知生物", "答案")
        compare_system.notequal("病毒", "敘述", "由完整細胞構成", "錯誤觀念")

    @staticmethod
    def prokaryote_eukaryote():
        compare_system.equivalentto("原核細胞", "細胞種類", "沒有被核膜包圍之細胞核的細胞", "定義")
        compare_system.equivalentto("真核細胞", "細胞種類", "具有被核膜包圍之細胞核的細胞", "定義")
        compare_system.equal("細菌", "細胞種類", "原核細胞", "答案")
        compare_system.equal("動物細胞", "細胞種類", "真核細胞", "答案")
        compare_system.equal("植物細胞", "細胞種類", "真核細胞", "答案")
        compare_system.equal("真菌細胞", "細胞種類", "真核細胞", "答案")
        compare_system.equal("原核細胞 DNA", "主要位置", "細胞質中的核區", "答案")
        compare_system.equal("真核細胞 DNA", "主要位置", "細胞核", "答案")
        compare_system.notequal("原核細胞", "敘述", "完全沒有 DNA", "錯誤觀念")

    @staticmethod
    def cell_membrane():
        compare_system.equivalentto("細胞膜", "細胞構造", "包圍細胞並控制物質進出的選擇性屏障", "定義")
        compare_system.equal("細胞膜主要結構", "題目", "磷脂雙層與蛋白質", "答案")
        compare_system.equal("磷脂親水端", "方向", "朝向水溶液", "答案")
        compare_system.equal("磷脂疏水端", "方向", "朝向膜的內部", "答案")
        compare_system.equal("細胞膜", "通透性", "選擇性通透", "答案")
        compare_system.equal("膜蛋白", "可能功能", "運輸、受體、酵素與細胞辨識", "答案")
        compare_system.notequal("細胞膜", "敘述", "所有物質都能自由通過", "錯誤觀念")

    @staticmethod
    def cytoplasm():
        compare_system.equivalentto("細胞質", "細胞構造", "細胞膜內、細胞核外的物質與構造", "定義")
        compare_system.equal("細胞質基質", "特徵", "含水、離子、蛋白質與多種溶質", "答案")
        compare_system.equal("許多代謝反應", "位置", "細胞質中進行", "答案")
        compare_system.equal("核糖體", "位置", "可游離於細胞質或附著於粗糙內質網", "答案")
        compare_system.equal("細胞器", "真核細胞", "多數位於細胞質中", "答案")
        compare_system.notequal("細胞質", "概念", "只有完全透明的水", "錯誤觀念")

    @staticmethod
    def nucleus():
        compare_system.equivalentto("細胞核", "細胞器", "儲存大部分遺傳物質並控制細胞活動的構造", "定義")
        compare_system.equal("核膜", "構造", "雙層膜", "答案")
        compare_system.equal("核孔", "功能", "調節細胞核與細胞質間物質交換", "答案")
        compare_system.equal("染色質", "組成", "DNA 與蛋白質", "答案")
        compare_system.equal("核仁", "主要功能", "製造核糖體 RNA 並組裝核糖體次單元", "答案")
        compare_system.equal("細胞分裂前", "染色質", "凝縮形成染色體", "答案")
        compare_system.notequal("成熟哺乳類紅血球", "敘述", "具有完整細胞核", "錯誤觀念")

    @staticmethod
    def mitochondrion():
        compare_system.equivalentto("粒線體", "細胞器", "進行有氧呼吸並產生大量 ATP 的場所", "定義")
        compare_system.equal("粒線體", "膜數", "具有雙層膜", "答案")
        compare_system.equal("粒線體內膜褶皺", "名稱", "嵴", "答案")
        compare_system.equal("嵴", "作用", "增加進行電子傳遞反應的表面積", "答案")
        compare_system.equal("粒線體", "遺傳物質", "具有少量自身 DNA", "答案")
        compare_system.equal("耗能較多的細胞", "一般特徵", "通常含較多粒線體", "答案")
        compare_system.notequal("粒線體", "敘述", "只存在植物細胞中", "錯誤觀念")

    @staticmethod
    def chloroplast():
        compare_system.equivalentto("葉綠體", "細胞器", "植物與部分藻類進行光合作用的場所", "定義")
        compare_system.equal("葉綠體", "膜數", "具有雙層膜", "答案")
        compare_system.equal("葉綠素", "主要位置", "類囊體膜", "答案")
        compare_system.equal("光反應", "主要位置", "類囊體膜", "答案")
        compare_system.equal("卡爾文循環", "主要位置", "葉綠體基質", "答案")
        compare_system.equal("葉綠體", "遺傳物質", "具有少量自身 DNA", "答案")
        compare_system.notequal("植物所有細胞", "敘述", "都具有大量葉綠體", "錯誤觀念")

    @staticmethod
    def ribosome():
        compare_system.equivalentto("核糖體", "細胞構造", "依 mRNA 資訊合成蛋白質的場所", "定義")
        compare_system.equal("核糖體", "主要組成", "rRNA 與蛋白質", "答案")
        compare_system.equal("游離核糖體", "主要製造", "細胞質內使用的蛋白質", "答案")
        compare_system.equal("粗糙內質網上的核糖體", "主要製造", "分泌或膜系統相關蛋白質", "答案")
        compare_system.equal("原核與真核細胞", "共同構造", "皆具有核糖體", "答案")
        compare_system.notequal("核糖體", "敘述", "由膜包圍形成", "錯誤觀念")

    @staticmethod
    def endoplasmic_reticulum():
        compare_system.equivalentto("內質網", "細胞器", "由膜構成並參與蛋白質與脂質製造及運輸的系統", "定義")
        compare_system.equal("粗糙內質網", "表面", "附有核糖體", "答案")
        compare_system.equal("粗糙內質網", "主要功能", "合成與初步加工蛋白質", "答案")
        compare_system.equal("平滑內質網", "表面", "沒有附著核糖體", "答案")
        compare_system.equal("平滑內質網", "主要功能", "合成脂質、解毒與儲存鈣離子", "答案")
        compare_system.equal("肝細胞", "一般特徵", "具有較發達的平滑內質網", "答案")
        compare_system.notequal("粗糙內質網", "敘述", "表面粗糙是因為覆蓋細胞壁", "錯誤觀念")

    @staticmethod
    def golgi_apparatus():
        compare_system.equivalentto("高基氏體", "細胞器", "修飾、分類、包裝並運送蛋白質與脂質", "定義")
        compare_system.equal("高基氏體接收物質", "主要來源", "內質網運輸囊泡", "答案")
        compare_system.equal("高基氏體", "可能產物", "分泌囊泡與溶體", "答案")
        compare_system.equal("分泌旺盛細胞", "一般特徵", "高基氏體較發達", "答案")
        compare_system.equal("高基氏體", "構造", "多層扁平膜囊堆疊", "答案")
        compare_system.notequal("高基氏體", "敘述", "直接負責複製 DNA", "錯誤觀念")

    @staticmethod
    def lysosome_vacuole():
        compare_system.equivalentto("溶體", "細胞器", "含消化酵素並分解物質的膜狀構造", "定義")
        compare_system.equal("溶體", "功能", "分解老舊細胞器與吞入物質", "答案")
        compare_system.equivalentto("液胞", "細胞器", "儲存水、離子、色素或其他物質的膜囊", "定義")
        compare_system.equal("成熟植物細胞", "液胞", "通常具有大型中央液胞", "答案")
        compare_system.equal("中央液胞", "功能之一", "維持細胞膨壓", "答案")
        compare_system.equal("動物細胞液胞", "一般特徵", "較小且不一定明顯", "答案")
        compare_system.notequal("溶體", "敘述", "作用是製造葡萄糖", "錯誤觀念")

    @staticmethod
    def cell_wall():
        compare_system.equivalentto("細胞壁", "細胞構造", "位於細胞膜外並提供支持與保護的構造", "定義")
        compare_system.equal("植物細胞壁主要成分", "題目", "纖維素", "答案")
        compare_system.equal("真菌細胞壁主要成分之一", "題目", "幾丁質", "答案")
        compare_system.equal("細菌細胞壁主要成分之一", "題目", "肽聚醣", "答案")
        compare_system.equal("動物細胞", "細胞壁", "沒有", "答案")
        compare_system.equal("細胞壁", "通透性", "通常不像細胞膜具有高度選擇性", "答案")
        compare_system.notequal("植物細胞壁", "敘述", "取代了細胞膜", "錯誤觀念")

    @staticmethod
    def diffusion():
        compare_system.equivalentto("擴散", "被動運輸", "粒子由高濃度區域向低濃度區域淨移動", "定義")
        compare_system.equal("擴散", "能量需求", "不需細胞額外提供 ATP", "答案")
        compare_system.equal("濃度差增加", "一般結果", "擴散速率增加", "答案")
        compare_system.equal("溫度升高", "一般結果", "粒子擴散通常加快", "答案")
        compare_system.equal("分子較小", "一般結果", "通常較容易擴散", "答案")
        compare_system.equal("達到動態平衡", "擴散", "粒子仍移動但沒有淨移動", "答案")
        compare_system.notequal("擴散平衡", "敘述", "所有粒子完全停止運動", "錯誤觀念")

    @staticmethod
    def osmosis():
        compare_system.equivalentto("滲透作用", "被動運輸", "水經選擇性通透膜由水勢較高處向水勢較低處淨移動", "定義")
        compare_system.equal("低溶質濃度溶液", "相對水勢", "較高", "答案")
        compare_system.equal("高溶質濃度溶液", "相對水勢", "較低", "答案")
        compare_system.equal("動物細胞置於低張溶液", "結果", "吸水膨脹甚至破裂", "答案")
        compare_system.equal("動物細胞置於高張溶液", "結果", "失水皺縮", "答案")
        compare_system.equal("植物細胞置於低張溶液", "結果", "吸水並產生膨壓", "答案")
        compare_system.equal("植物細胞置於高張溶液", "結果", "可能發生質壁分離", "答案")
        compare_system.notequal("滲透作用", "敘述", "溶質一定穿過膜移動", "錯誤觀念")

    @staticmethod
    def active_transport():
        compare_system.equivalentto("主動運輸", "膜運輸", "利用能量使物質逆濃度梯度移動", "定義")
        compare_system.equal("主動運輸", "能量需求", "通常需要 ATP", "答案")
        compare_system.equal("主動運輸", "蛋白質需求", "通常需要膜運輸蛋白", "答案")
        compare_system.equal("物質移動方向", "主動運輸", "可由低濃度移向高濃度", "答案")
        compare_system.equal("鈉鉀幫浦", "運輸類型", "主動運輸", "答案")
        compare_system.equal("植物根毛吸收部分礦物離子", "運輸類型", "主動運輸", "答案")
        compare_system.notequal("主動運輸", "敘述", "只要有濃度差就不需能量", "錯誤觀念")

    @staticmethod
    def endocytosis_exocytosis():
        compare_system.equivalentto("胞吞作用", "膜運輸", "細胞膜內陷形成囊泡將物質帶入細胞", "定義")
        compare_system.equivalentto("胞吐作用", "膜運輸", "囊泡與細胞膜融合將物質排出細胞", "定義")
        compare_system.equal("白血球吞噬細菌", "運輸", "胞吞作用", "答案")
        compare_system.equal("神經傳遞物質釋放", "運輸", "胞吐作用", "答案")
        compare_system.equal("胞吞與胞吐", "能量需求", "通常需要能量", "答案")
        compare_system.equal("大型顆粒進出細胞", "方式", "可利用胞吞或胞吐", "答案")
        compare_system.notequal("胞吐作用", "敘述", "只運送水分子", "錯誤觀念")

    @staticmethod
    def enzyme():
        compare_system.equivalentto("酵素", "生物催化劑", "降低活化能並加速生化反應的物質", "定義")
        compare_system.equal("大多數酵素", "化學本質", "蛋白質", "答案")
        compare_system.equal("部分 RNA", "功能", "也能具有催化作用", "答案")
        compare_system.equal("酵素", "反應前後", "通常不被永久消耗", "答案")
        compare_system.equal("酵素", "作用", "降低活化能", "答案")
        compare_system.equal("酵素", "對反應平衡", "不改變平衡位置", "答案")
        compare_system.notequal("酵素", "敘述", "提供反應所需的全部能量", "錯誤觀念")

    @staticmethod
    def enzyme_specificity():
        compare_system.equivalentto("酵素專一性", "特性", "酵素通常只催化特定受質或特定類型反應", "定義")
        compare_system.equal("酵素作用位置", "名稱", "活性部位", "答案")
        compare_system.equal("受質", "定義", "與酵素結合並被催化的反應物", "答案")
        compare_system.equal("酵素與受質結合", "形成", "酵素—受質複合體", "答案")
        compare_system.equal("活性部位形狀改變", "結果", "可能降低酵素活性", "答案")
        compare_system.notequal("一種酵素", "敘述", "可以催化所有生化反應", "錯誤觀念")

    @staticmethod
    def enzyme_factors():
        compare_system.equal("溫度升高至適溫前", "一般結果", "酵素反應速率增加", "答案")
        compare_system.equal("溫度過高", "可能結果", "酵素變性並失去活性", "答案")
        compare_system.equal("pH 偏離最適值", "可能結果", "酵素活性降低", "答案")
        compare_system.equal("受質濃度增加", "酵素未飽和時", "反應速率增加", "答案")
        compare_system.equal("酵素達飽和", "結果", "再增加受質時速率增加有限", "答案")
        compare_system.equal("增加酵素濃度", "受質充足時", "反應速率增加", "答案")
        compare_system.notequal("所有酵素", "敘述", "最適溫度與最適 pH 完全相同", "錯誤觀念")

    @staticmethod
    def atp():
        compare_system.equivalentto("ATP", "能量分子", "細胞短期儲存與傳遞能量的重要分子", "定義")
        compare_system.equal("ATP 中文名稱", "題目", "腺苷三磷酸", "答案")
        compare_system.equal("ATP 水解", "生成", "ADP、無機磷酸與可利用能量", "答案")
        compare_system.equal("ATP", "用途", "主動運輸、合成作用與肌肉收縮", "答案")
        compare_system.equal("ATP", "細胞內", "持續被合成與消耗", "答案")
        compare_system.notequal("ATP", "敘述", "是人體長期儲存能量的主要大型倉庫", "錯誤觀念")

    @staticmethod
    def photosynthesis():
        compare_system.equivalentto("光合作用", "代謝作用", "利用光能將二氧化碳與水合成有機物並釋放氧氣", "定義")
        compare_system.calculatedby("光合作用總反應", "簡式", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", "答案")
        compare_system.equal("光合作用能量來源", "題目", "光能", "答案")
        compare_system.equal("光合作用主要場所", "真核植物", "葉綠體", "答案")
        compare_system.equal("光反應", "主要產物", "ATP、NADPH 與 O₂", "答案")
        compare_system.equal("卡爾文循環", "主要作用", "固定 CO₂ 並合成醣類", "答案")
        compare_system.equal("光合作用釋放的氧", "主要來源", "水分子", "答案")
        compare_system.notequal("植物", "敘述", "只進行光合作用而不進行呼吸作用", "錯誤觀念")

    @staticmethod
    def cellular_respiration():
        compare_system.equivalentto("細胞呼吸", "代謝作用", "分解有機物並將能量轉移至 ATP 的過程", "定義")
        compare_system.calculatedby("有氧呼吸總反應", "簡式", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 能量", "答案")
        compare_system.equal("糖解作用", "主要位置", "細胞質", "答案")
        compare_system.equal("檸檬酸循環", "主要位置", "粒線體基質", "答案")
        compare_system.equal("電子傳遞鏈", "主要位置", "粒線體內膜", "答案")
        compare_system.equal("有氧呼吸", "ATP 產量", "通常高於發酵", "答案")
        compare_system.equal("氧氣", "有氧呼吸", "最終電子接受者", "答案")
        compare_system.notequal("呼吸作用", "概念", "只是肺部吸入與呼出空氣", "錯誤觀念")

    @staticmethod
    def fermentation():
        compare_system.equivalentto("發酵", "代謝作用", "缺氧或無氧條件下使糖解作用得以持續的能量代謝方式", "定義")
        compare_system.equal("乳酸發酵", "產物", "乳酸", "答案")
        compare_system.equal("酒精發酵", "產物", "乙醇與 CO₂", "答案")
        compare_system.equal("酵母菌", "常見代謝", "酒精發酵", "答案")
        compare_system.equal("乳酸菌", "常見代謝", "乳酸發酵", "答案")
        compare_system.equal("發酵 ATP", "主要來源", "糖解作用", "答案")
        compare_system.equal("發酵 ATP 產量", "比較", "低於有氧呼吸", "答案")
        compare_system.notequal("發酵", "敘述", "完全不產生 ATP", "錯誤觀念")