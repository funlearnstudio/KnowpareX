# ===========================================
# notes_chemistry_solution_acid_base.py
# 化學：溶液、濃度、酸與鹼
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_solution_acid_base:

    @staticmethod
    def solution():
        compare_system.equivalentto("溶液", "混合物", "溶質均勻分散於溶劑形成的均勻混合物", "定義")
        compare_system.equivalentto("溶質", "溶液成分", "被溶解且通常含量較少的物質", "定義")
        compare_system.equivalentto("溶劑", "溶液成分", "溶解溶質且通常含量較多的物質", "定義")
        compare_system.equal("食鹽水中的食鹽", "角色", "溶質", "答案")
        compare_system.equal("食鹽水中的水", "角色", "溶劑", "答案")
        compare_system.equal("水為溶劑的溶液", "名稱", "水溶液", "答案")
        compare_system.notequal("溶液", "敘述", "一定是液態", "錯誤觀念")

    @staticmethod
    def solubility():
        compare_system.equivalentto("溶解度", "物理性質", "特定溫度下定量溶劑可溶解溶質的最大量", "定義")
        compare_system.equal("大多數固體在水中的溶解度", "溫度升高", "通常增加", "答案")
        compare_system.equal("氣體在液體中的溶解度", "溫度升高", "通常降低", "答案")
        compare_system.equal("氣體溶解度", "壓力升高", "通常增加", "答案")
        compare_system.equal("攪拌", "效果", "加快溶解速率但通常不改變平衡溶解度", "答案")
        compare_system.equal("粉碎溶質", "效果", "加快溶解速率但通常不改變平衡溶解度", "答案")
        compare_system.notequal("溶解速度較快", "敘述", "表示溶解度一定較大", "錯誤觀念")

    @staticmethod
    def saturated_solution():
        compare_system.equivalentto("未飽和溶液", "溶液", "在該條件下仍可再溶解更多溶質的溶液", "定義")
        compare_system.equivalentto("飽和溶液", "溶液", "在該條件下已達溶解平衡的溶液", "定義")
        compare_system.equivalentto("過飽和溶液", "溶液", "含有超過平衡溶解度溶質的不穩定溶液", "定義")
        compare_system.equal("飽和溶液中", "微觀狀態", "溶解與結晶速率相等", "答案")
        compare_system.equal("加入晶種至過飽和溶液", "可能結果", "快速結晶", "答案")
        compare_system.notequal("飽和溶液", "敘述", "一定是非常濃的溶液", "錯誤觀念")
        compare_system.notequal("未飽和溶液", "敘述", "一定是非常稀的溶液", "錯誤觀念")

    @staticmethod
    def mass_percent():
        compare_system.calculatedby("質量百分濃度", "公式", "溶質質量 ÷ 溶液質量 × 100%", "答案")
        compare_system.equal("溶液質量", "關係", "溶質質量 + 溶劑質量", "答案")
        compare_system.equal("10 g 食鹽加入 90 g 水", "題目", "質量百分濃度為 10%", "答案")
        compare_system.equal("20% 食鹽水 100 g", "食鹽質量", "20 g", "答案")
        compare_system.equal("加入溶劑", "其他條件不變", "質量百分濃度降低", "答案")
        compare_system.equal("蒸發部分溶劑", "未析出前", "質量百分濃度提高", "答案")
        compare_system.notequal("10 g 溶質加入 100 g 水", "敘述", "濃度一定是 10%", "錯誤觀念")

    @staticmethod
    def molarity():
        compare_system.equivalentto("體積莫耳濃度", "濃度", "每公升溶液所含溶質的莫耳數", "定義")
        compare_system.calculatedby("莫耳濃度", "公式", "M = n ÷ V", "答案")
        compare_system.equal("莫耳濃度單位", "題目", "mol/L 或 M", "答案")
        compare_system.equal("1 mol 溶質配成 2 L 溶液", "題目", "濃度為 0.5 M", "答案")
        compare_system.equal("0.2 mol 溶質配成 500 mL 溶液", "題目", "濃度為 0.4 M", "答案")
        compare_system.equal("計算莫耳濃度的體積", "注意", "應使用溶液總體積", "答案")
        compare_system.notequal("莫耳濃度", "敘述", "不會隨溫度造成的體積變化而改變", "錯誤觀念")

    @staticmethod
    def dilution():
        compare_system.equivalentto("稀釋", "操作", "加入溶劑使溶液濃度降低的過程", "定義")
        compare_system.calculatedby("稀釋公式", "公式", "M₁V₁ = M₂V₂", "答案")
        compare_system.equal("稀釋前後溶質莫耳數", "理想關係", "不變", "答案")
        compare_system.equal("加入水稀釋", "結果", "溶液體積增加、濃度降低", "答案")
        compare_system.equal("2 M 溶液 100 mL 稀釋至 200 mL", "題目", "新濃度為 1 M", "答案")
        compare_system.notequal("稀釋", "敘述", "會使溶質莫耳數自動減少", "錯誤觀念")
        compare_system.equal("濃酸加水", "安全原則", "通常將酸慢慢加入水中並攪拌", "答案")

    @staticmethod
    def electrolyte():
        compare_system.equivalentto("電解質", "物質", "溶於水或熔融時可產生可移動離子而導電的物質", "定義")
        compare_system.equivalentto("非電解質", "物質", "溶於水後不產生足量可移動離子的物質", "定義")
        compare_system.equal("NaCl 水溶液", "分類", "電解質溶液", "答案")
        compare_system.equal("HCl 水溶液", "分類", "電解質溶液", "答案")
        compare_system.equal("糖水", "分類", "非電解質溶液", "答案")
        compare_system.equal("固態 NaCl", "導電性", "通常不導電", "答案")
        compare_system.equal("熔融 NaCl", "導電性", "可導電", "答案")
        compare_system.notequal("水溶液能導電", "敘述", "一定含有自由電子作為主要載流子", "錯誤觀念")

    @staticmethod
    def acid():
        compare_system.equivalentto("阿瑞尼士酸", "酸鹼定義", "在水中增加 H⁺ 或 H₃O⁺ 濃度的物質", "定義")
        compare_system.equivalentto("布朗斯特酸", "酸鹼定義", "可提供質子的物質", "定義")
        compare_system.equal("鹽酸", "化學式", "HCl(aq)", "答案")
        compare_system.equal("硫酸", "化學式", "H₂SO₄", "答案")
        compare_system.equal("硝酸", "化學式", "HNO₃", "答案")
        compare_system.equal("酸與活性金屬反應", "可能生成物", "鹽與氫氣", "答案")
        compare_system.equal("酸性水溶液", "石蕊試紙", "使藍色石蕊變紅", "答案")
        compare_system.notequal("含有 H 的化合物", "敘述", "一定是酸", "錯誤觀念")

    @staticmethod
    def base():
        compare_system.equivalentto("阿瑞尼士鹼", "酸鹼定義", "在水中增加 OH⁻ 濃度的物質", "定義")
        compare_system.equivalentto("布朗斯特鹼", "酸鹼定義", "可接受質子的物質", "定義")
        compare_system.equal("氫氧化鈉", "化學式", "NaOH", "答案")
        compare_system.equal("氫氧化鈣", "化學式", "Ca(OH)₂", "答案")
        compare_system.equal("氨", "化學式", "NH₃", "答案")
        compare_system.equal("鹼性水溶液", "石蕊試紙", "使紅色石蕊變藍", "答案")
        compare_system.equal("鹼性溶液觸感", "常見現象", "可能有滑膩感", "答案")
        compare_system.notequal("具有 OH 基團的化合物", "敘述", "一定是阿瑞尼士鹼", "錯誤觀念")

    @staticmethod
    def strong_weak():
        compare_system.equivalentto("強酸", "酸", "在水中近乎完全解離的酸", "定義")
        compare_system.equivalentto("弱酸", "酸", "在水中只部分解離的酸", "定義")
        compare_system.equivalentto("強鹼", "鹼", "在水中近乎完全解離的鹼", "定義")
        compare_system.equivalentto("弱鹼", "鹼", "在水中只部分反應或解離的鹼", "定義")
        compare_system.equal("HCl", "強弱分類", "強酸", "答案")
        compare_system.equal("醋酸", "強弱分類", "弱酸", "答案")
        compare_system.equal("NaOH", "強弱分類", "強鹼", "答案")
        compare_system.equal("NH₃", "強弱分類", "弱鹼", "答案")
        compare_system.notequal("強酸", "概念", "高濃度的酸", "錯誤觀念")

    @staticmethod
    def ph():
        compare_system.equivalentto("pH", "物理量", "描述水溶液酸鹼程度的對數尺度", "定義")
        compare_system.calculatedby("pH", "公式", "pH = -log[H⁺]", "答案")
        compare_system.equal("25°C 中性水溶液", "pH", "約 7", "答案")
        compare_system.smaller("酸性水溶液 pH", "25°C 常見關係", "7", "答案")
        compare_system.bigger("鹼性水溶液 pH", "25°C 常見關係", "7", "答案")
        compare_system.equal("[H⁺] 增加 10 倍", "結果", "pH 降低 1", "答案")
        compare_system.notequal("pH 2 與 pH 4", "酸度比較", "只相差 2 倍", "錯誤觀念")
        compare_system.equal("pH 2 與 pH 4", "氫離子濃度比較", "pH 2 約為 pH 4 的 100 倍", "答案")

    @staticmethod
    def poh():
        compare_system.calculatedby("pOH", "公式", "pOH = -log[OH⁻]", "答案")
        compare_system.equal("25°C 水溶液", "常用關係", "pH + pOH = 14", "答案")
        compare_system.equal("pH = 3", "25°C", "pOH = 11", "答案")
        compare_system.equal("pOH = 2", "25°C", "pH = 12", "答案")
        compare_system.equal("[OH⁻] 增加", "結果", "pOH 降低", "答案")
        compare_system.notequal("pH + pOH = 14", "敘述", "在所有溫度與所有溶劑中永遠完全成立", "錯誤觀念")

    @staticmethod
    def neutralization():
        compare_system.equivalentto("中和反應", "酸鹼反應", "酸與鹼反應形成鹽與水的反應", "定義")
        compare_system.equal("強酸與強鹼淨離子反應", "方程式", "H⁺ + OH⁻ → H₂O", "答案")
        compare_system.equal("HCl + NaOH", "生成物", "NaCl + H₂O", "答案")
        compare_system.equal("中和反應", "熱量變化", "通常放熱", "答案")
        compare_system.equal("恰好完全中和", "條件", "酸鹼反應當量相等", "答案")
        compare_system.notequal("中和後的溶液", "敘述", "pH 一定恰好為 7", "錯誤觀念")
        compare_system.equal("弱酸與強鹼恰好中和", "常見結果", "溶液可能呈鹼性", "答案")

    @staticmethod
    def indicator():
        compare_system.equivalentto("酸鹼指示劑", "物質", "會隨酸鹼環境改變顏色的物質", "定義")
        compare_system.equal("藍色石蕊遇酸", "顏色", "紅色", "答案")
        compare_system.equal("紅色石蕊遇鹼", "顏色", "藍色", "答案")
        compare_system.equal("酚酞在酸性或中性溶液", "顏色", "無色", "答案")
        compare_system.equal("酚酞在鹼性溶液", "顏色", "粉紅色", "答案")
        compare_system.equal("廣用指示劑", "用途", "依顏色粗略判斷 pH 範圍", "答案")
        compare_system.notequal("單一指示劑", "敘述", "能給出所有溶液非常精確的 pH", "錯誤觀念")

    @staticmethod
    def titration():
        compare_system.equivalentto("酸鹼滴定", "分析方法", "利用已知濃度溶液測定未知酸或鹼濃度", "定義")
        compare_system.equal("滴定管", "用途", "精確加入並量測滴定液體積", "答案")
        compare_system.equivalentto("當量點", "滴定", "酸鹼依反應計量恰好完全反應的點", "定義")
        compare_system.equivalentto("終點", "滴定", "指示劑產生可觀察顏色變化的點", "定義")
        compare_system.equal("理想滴定", "關係", "終點應盡量接近當量點", "答案")
        compare_system.equal("一元強酸與一元強鹼", "當量點關係", "n酸 = n鹼", "答案")
        compare_system.notequal("所有滴定的當量點", "敘述", "pH 一定為 7", "錯誤觀念")

    @staticmethod
    def buffer():
        compare_system.equivalentto("緩衝溶液", "溶液", "加入少量酸或鹼時能減小 pH 變化的溶液", "定義")
        compare_system.equal("常見酸性緩衝系統", "組成", "弱酸與其共軛鹼", "答案")
        compare_system.equal("常見鹼性緩衝系統", "組成", "弱鹼與其共軛酸", "答案")
        compare_system.equal("緩衝溶液", "功能", "抵抗而非完全阻止 pH 改變", "答案")
        compare_system.equal("血液", "酸鹼控制", "含有重要緩衝系統", "答案")
        compare_system.notequal("緩衝溶液", "敘述", "加入任何大量強酸後 pH 都完全不變", "錯誤觀念")