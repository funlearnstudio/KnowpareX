# ===========================================
# notes_chemistry_bond_formula.py
# 化學：化學鍵、分子與化學式
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_bond_formula:

    @staticmethod
    def chemical_bond():
        compare_system.equivalentto("化學鍵", "化學概念", "使原子或離子結合在一起的作用", "定義")
        compare_system.equal("形成化學鍵", "一般原因", "系統可達到較低且較穩定的能量狀態", "答案")
        compare_system.equal("常見主要化學鍵", "題目", "離子鍵、共價鍵與金屬鍵", "答案")
        compare_system.equal("化學鍵形成或斷裂", "關係", "伴隨能量變化", "答案")
        compare_system.notequal("化學鍵", "敘述", "是把原子黏住的實體繩子", "錯誤觀念")
        compare_system.equal("價電子", "重要性", "直接參與許多化學鍵形成", "答案")

    @staticmethod
    def ionic_bond():
        compare_system.equivalentto("離子鍵", "化學鍵", "陽離子與陰離子之間的靜電吸引作用", "定義")
        compare_system.equal("離子化合物常見組成", "題目", "金屬陽離子與非金屬陰離子", "答案")
        compare_system.equal("氯化鈉", "鍵結種類", "主要為離子鍵", "答案")
        compare_system.equal("鈉形成 Na⁺", "過程", "失去 1 個電子", "答案")
        compare_system.equal("氯形成 Cl⁻", "過程", "得到 1 個電子", "答案")
        compare_system.equal("離子化合物固態", "導電性", "通常不易導電", "答案")
        compare_system.equal("離子化合物熔融或溶於水", "導電性", "常可導電", "答案")
        compare_system.equal("離子化合物", "結構", "通常形成離子晶格而非單獨分子", "答案")

    @staticmethod
    def covalent_bond():
        compare_system.equivalentto("共價鍵", "化學鍵", "原子間共享一對或多對電子形成的鍵", "定義")
        compare_system.equal("共價鍵常見於", "題目", "非金屬原子之間", "答案")
        compare_system.equal("單鍵", "共享電子對數", "1 對", "答案")
        compare_system.equal("雙鍵", "共享電子對數", "2 對", "答案")
        compare_system.equal("三鍵", "共享電子對數", "3 對", "答案")
        compare_system.equal("H₂", "鍵結", "單一共價鍵", "答案")
        compare_system.equal("O₂", "鍵結", "雙鍵", "答案")
        compare_system.equal("N₂", "鍵結", "三鍵", "答案")

    @staticmethod
    def metallic_bond():
        compare_system.equivalentto("金屬鍵", "化學鍵", "金屬陽離子骨架與離域電子間的吸引作用", "定義")
        compare_system.equal("金屬良好導電性", "原因", "具有可移動的離域電子", "答案")
        compare_system.equal("金屬延展性", "原因之一", "金屬鍵不具強烈固定方向性", "答案")
        compare_system.equal("金屬光澤", "原因之一", "自由電子與光交互作用", "答案")
        compare_system.equal("金屬鍵", "常見物質", "金屬單質與合金", "答案")
        compare_system.notequal("金屬鍵", "敘述", "由一個金屬原子把電子完全交給另一金屬原子", "錯誤觀念")

    @staticmethod
    def lewis_structure():
        compare_system.equivalentto("路易斯結構", "表示法", "用元素符號與價電子點或鍵線表示分子結構", "定義")
        compare_system.equal("路易斯結構中的線", "意義", "一對共享電子", "答案")
        compare_system.equal("孤電子對", "定義", "未參與鍵結的一對價電子", "答案")
        compare_system.equal("畫路易斯結構第一步之一", "題目", "計算總價電子數", "答案")
        compare_system.equal("帶負電離子", "價電子計算", "需加入相應電子數", "答案")
        compare_system.equal("帶正電離子", "價電子計算", "需減去相應電子數", "答案")
        compare_system.notequal("路易斯結構", "敘述", "能完全精確呈現所有分子三維形狀", "錯誤觀念")

    @staticmethod
    def octet_rule():
        compare_system.equivalentto("八隅體規則", "經驗規則", "許多主族原子傾向形成 8 個價電子的穩定排列", "定義")
        compare_system.equal("氫的穩定電子數", "常見規則", "2", "答案")
        compare_system.equal("鈉失去 1 電子", "結果", "形成類似氖的穩定排列", "答案")
        compare_system.equal("氯得到 1 電子", "結果", "形成類似氬的穩定排列", "答案")
        compare_system.notequal("八隅體規則", "敘述", "所有分子毫無例外都必須遵守", "錯誤觀念")
        compare_system.equal("硼、磷、硫等元素", "情況", "可能出現不完整或擴展八隅體", "答案")

    @staticmethod
    def electronegativity():
        compare_system.equivalentto("電負度", "化學性質", "鍵結原子吸引共享電子的相對能力", "定義")
        compare_system.equal("電負度差增大", "一般結果", "鍵的極性增強", "答案")
        compare_system.equal("相同原子形成的鍵", "極性", "非極性共價鍵", "答案")
        compare_system.equal("H-Cl 鍵", "極性", "極性共價鍵", "答案")
        compare_system.equal("Na-Cl 鍵", "主要性質", "高度離子性", "答案")
        compare_system.equal("氟", "電負度", "最高", "答案")
        compare_system.notequal("極性共價鍵", "敘述", "電子完全轉移給其中一個原子", "錯誤觀念")

    @staticmethod
    def molecular_polarity():
        compare_system.equivalentto("分子極性", "分子性質", "分子內電荷分布不均所形成的整體偶極", "定義")
        compare_system.equal("判斷分子極性", "主要考量", "鍵極性與分子形狀", "答案")
        compare_system.equal("H₂O", "分子極性", "極性分子", "答案")
        compare_system.equal("CO₂", "分子極性", "非極性分子", "答案")
        compare_system.equal("CH₄", "分子極性", "非極性分子", "答案")
        compare_system.equal("NH₃", "分子極性", "極性分子", "答案")
        compare_system.notequal("含有極性鍵的分子", "敘述", "整個分子一定是極性分子", "錯誤觀念")

    @staticmethod
    def intermolecular_force():
        compare_system.equivalentto("分子間作用力", "作用力", "分子彼此之間的吸引或排斥作用", "定義")
        compare_system.equal("凡得瓦力", "範圍", "分子間作用力的統稱之一", "答案")
        compare_system.equal("偶極—偶極作用力", "主要存在於", "極性分子之間", "答案")
        compare_system.equal("倫敦分散力", "存在範圍", "所有原子與分子之間", "答案")
        compare_system.equal("粒子可極化性增加", "一般結果", "分散力增強", "答案")
        compare_system.equal("分子間作用力較強", "一般結果", "沸點通常較高", "答案")
        compare_system.notequal("分子間作用力", "概念", "分子內共價鍵", "錯誤觀念")

    @staticmethod
    def hydrogen_bond():
        compare_system.equivalentto("氫鍵", "分子間作用力", "氫連接高電負度原子後與另一高電負度原子間的較強吸引", "定義")
        compare_system.equal("常形成氫鍵的元素", "題目", "N、O、F", "答案")
        compare_system.equal("水分子之間", "作用力", "氫鍵", "答案")
        compare_system.equal("水沸點較高", "原因之一", "水分子間具有氫鍵", "答案")
        compare_system.equal("DNA 鹼基配對", "穩定作用之一", "氫鍵", "答案")
        compare_system.notequal("任何含氫分子", "敘述", "都能形成強烈氫鍵", "錯誤觀念")

    @staticmethod
    def molecular_shape():
        compare_system.equivalentto("VSEPR 理論", "模型", "電子對彼此排斥並盡量遠離以決定分子形狀", "定義")
        compare_system.equal("CO₂", "分子形狀", "直線形", "答案")
        compare_system.equal("CH₄", "分子形狀", "正四面體", "答案")
        compare_system.equal("NH₃", "分子形狀", "三角錐形", "答案")
        compare_system.equal("H₂O", "分子形狀", "彎曲形", "答案")
        compare_system.equal("孤電子對", "排斥力", "通常比鍵結電子對排斥更強", "答案")
        compare_system.notequal("路易斯結構畫成平面", "敘述", "分子實際一定是平面形", "錯誤觀念")

    @staticmethod
    def chemical_formula():
        compare_system.equivalentto("化學式", "表示法", "用元素符號與下標表示物質組成", "定義")
        compare_system.equal("化學式右下角數字", "意義", "該元素原子數或比例", "答案")
        compare_system.equal("H₂O", "組成", "每個水分子含 2 個氫原子與 1 個氧原子", "答案")
        compare_system.equal("CO₂", "組成", "每個分子含 1 個碳原子與 2 個氧原子", "答案")
        compare_system.equal("化學式前係數", "意義", "分子數、化學式單位數或莫耳數比例", "答案")
        compare_system.notequal("下標與係數", "敘述", "在化學方程式中可以任意互換", "錯誤觀念")

    @staticmethod
    def ionic_formula():
        compare_system.equal("離子化合物化學式", "原則", "總正電荷與總負電荷相等", "答案")
        compare_system.equal("Na⁺ 與 Cl⁻", "形成化學式", "NaCl", "答案")
        compare_system.equal("Mg²⁺ 與 Cl⁻", "形成化學式", "MgCl₂", "答案")
        compare_system.equal("Al³⁺ 與 O²⁻", "形成化學式", "Al₂O₃", "答案")
        compare_system.equal("Ca²⁺ 與 OH⁻", "形成化學式", "Ca(OH)₂", "答案")
        compare_system.equal("NH₄⁺ 與 SO₄²⁻", "形成化學式", "(NH₄)₂SO₄", "答案")
        compare_system.notequal("離子化合物下標", "敘述", "可以留下共同倍數而不化簡", "錯誤觀念")

    @staticmethod
    def common_ions():
        compare_system.equal("鈉離子", "符號", "Na⁺", "答案")
        compare_system.equal("鈣離子", "符號", "Ca²⁺", "答案")
        compare_system.equal("鋁離子", "符號", "Al³⁺", "答案")
        compare_system.equal("氯離子", "符號", "Cl⁻", "答案")
        compare_system.equal("氧化物離子", "符號", "O²⁻", "答案")
        compare_system.equal("氫氧根離子", "符號", "OH⁻", "答案")
        compare_system.equal("硝酸根離子", "符號", "NO₃⁻", "答案")
        compare_system.equal("硫酸根離子", "符號", "SO₄²⁻", "答案")
        compare_system.equal("碳酸根離子", "符號", "CO₃²⁻", "答案")
        compare_system.equal("銨根離子", "符號", "NH₄⁺", "答案")

    @staticmethod
    def naming():
        compare_system.equal("NaCl", "中文名稱", "氯化鈉", "答案")
        compare_system.equal("MgO", "中文名稱", "氧化鎂", "答案")
        compare_system.equal("CaCO₃", "中文名稱", "碳酸鈣", "答案")
        compare_system.equal("NaOH", "中文名稱", "氫氧化鈉", "答案")
        compare_system.equal("HCl 水溶液", "中文名稱", "鹽酸", "答案")
        compare_system.equal("H₂SO₄", "中文名稱", "硫酸", "答案")
        compare_system.equal("HNO₃", "中文名稱", "硝酸", "答案")
        compare_system.equal("NH₃", "中文名稱", "氨", "答案")