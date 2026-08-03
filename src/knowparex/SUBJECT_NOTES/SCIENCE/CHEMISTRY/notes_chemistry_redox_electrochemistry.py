# ===========================================
# notes_chemistry_redox_electrochemistry.py
# 化學：氧化還原與電化學
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_redox_electrochemistry:

    @staticmethod
    def oxidation_reduction():
        compare_system.equivalentto("氧化", "氧化還原", "物質失去電子或氧化數上升的過程", "定義")
        compare_system.equivalentto("還原", "氧化還原", "物質得到電子或氧化數下降的過程", "定義")
        compare_system.equal("失去電子", "反應分類", "氧化", "答案")
        compare_system.equal("得到電子", "反應分類", "還原", "答案")
        compare_system.equal("氧化與還原", "關係", "必須同時發生", "答案")
        compare_system.equal("電子", "氧化還原中", "由還原劑轉移給氧化劑", "答案")
        compare_system.notequal("氧化反應", "敘述", "一定要直接與氧氣反應", "錯誤觀念")

    @staticmethod
    def oxidizing_reducing_agent():
        compare_system.equivalentto("氧化劑", "反應物", "使其他物質氧化而自己被還原的物質", "定義")
        compare_system.equivalentto("還原劑", "反應物", "使其他物質還原而自己被氧化的物質", "定義")
        compare_system.equal("氧化劑", "電子變化", "得到電子", "答案")
        compare_system.equal("還原劑", "電子變化", "失去電子", "答案")
        compare_system.equal("氧化劑的氧化數", "反應後", "降低", "答案")
        compare_system.equal("還原劑的氧化數", "反應後", "升高", "答案")
        compare_system.notequal("氧化劑", "敘述", "自己發生氧化", "錯誤觀念")

    @staticmethod
    def oxidation_number():
        compare_system.equivalentto("氧化數", "形式電荷", "用於追蹤氧化還原電子變化的假想電荷", "定義")
        compare_system.equal("單質中的元素", "氧化數", "0", "答案")
        compare_system.equal("單原子離子", "氧化數", "等於離子電荷", "答案")
        compare_system.equal("氧在多數化合物", "氧化數", "-2", "答案")
        compare_system.equal("氫在多數非金屬化合物", "氧化數", "+1", "答案")
        compare_system.equal("中性化合物各元素氧化數總和", "關係", "0", "答案")
        compare_system.equal("多原子離子各元素氧化數總和", "關係", "等於離子總電荷", "答案")
        compare_system.equal("H₂O 中氧", "氧化數", "-2", "答案")
        compare_system.equal("CO₂ 中碳", "氧化數", "+4", "答案")

    @staticmethod
    def balancing_redox():
        compare_system.equal("氧化還原方程式平衡", "需守恆", "原子數與總電荷", "答案")
        compare_system.equal("半反應法", "步驟", "分別寫出氧化與還原半反應", "答案")
        compare_system.equal("半反應中電子", "作用", "表示電子失去或得到", "答案")
        compare_system.equal("合併半反應前", "要求", "使失去電子數與得到電子數相等", "答案")
        compare_system.equal("酸性條件平衡氧", "常用方法", "加入 H₂O", "答案")
        compare_system.equal("酸性條件平衡氫", "常用方法", "加入 H⁺", "答案")
        compare_system.notequal("平衡氧化還原反應", "敘述", "只需要平衡原子數而不用平衡電荷", "錯誤觀念")

    @staticmethod
    def activity_series():
        compare_system.equivalentto("金屬活動性", "性質", "金屬失去電子並發生氧化的相對傾向", "定義")
        compare_system.equal("活動性較高的金屬", "傾向", "較容易失去電子", "答案")
        compare_system.equal("Zn + Cu²⁺", "反應可能性", "Zn 可置換出 Cu", "答案")
        compare_system.equal("Cu + Zn²⁺", "反應可能性", "通常不自發置換出 Zn", "答案")
        compare_system.equal("活性金屬與酸", "可能生成", "氫氣", "答案")
        compare_system.equal("金、鉑", "金屬活動性", "相對較低", "答案")
        compare_system.notequal("金屬活動性高", "敘述", "表示金屬離子很容易得到電子", "錯誤觀念")

    @staticmethod
    def corrosion():
        compare_system.equivalentto("腐蝕", "化學現象", "材料與環境反應而逐漸劣化的過程", "定義")
        compare_system.equal("鐵生鏽", "反應類型", "氧化還原反應", "答案")
        compare_system.equal("鐵鏽形成", "通常需要", "氧氣與水", "答案")
        compare_system.equal("鹽水環境", "對鐵腐蝕", "通常會加速", "答案")
        compare_system.equal("塗油漆", "防鏽原理", "隔絕水與氧氣", "答案")
        compare_system.equal("鍍鋅", "防鏽原理", "鋅提供保護並可作為犧牲金屬", "答案")
        compare_system.equal("不鏽鋼", "抗腐蝕原因之一", "形成保護性氧化膜", "答案")
        compare_system.notequal("鐵鏽", "敘述", "會形成緻密保護膜完全阻止後續腐蝕", "錯誤觀念")

    @staticmethod
    def galvanic_cell():
        compare_system.equivalentto("原電池", "電化學裝置", "利用自發氧化還原反應產生電能的裝置", "定義")
        compare_system.equal("原電池陽極", "反應", "氧化", "答案")
        compare_system.equal("原電池陰極", "反應", "還原", "答案")
        compare_system.equal("原電池電子流向", "外電路", "由陽極流向陰極", "答案")
        compare_system.equal("原電池陽極", "常見極性", "負極", "答案")
        compare_system.equal("原電池陰極", "常見極性", "正極", "答案")
        compare_system.equal("鹽橋", "作用", "維持兩半電池電中性並完成內部電路", "答案")
        compare_system.notequal("電子", "敘述", "主要經鹽橋由陽極移至陰極", "錯誤觀念")

    @staticmethod
    def daniell_cell():
        compare_system.equal("鋅—銅丹尼爾電池陽極", "題目", "鋅電極", "答案")
        compare_system.equal("鋅—銅丹尼爾電池陰極", "題目", "銅電極", "答案")
        compare_system.equal("鋅電極半反應", "反應", "Zn → Zn²⁺ + 2e⁻", "答案")
        compare_system.equal("銅電極半反應", "反應", "Cu²⁺ + 2e⁻ → Cu", "答案")
        compare_system.equal("鋅電極質量", "反應進行", "減少", "答案")
        compare_system.equal("銅電極質量", "反應進行", "增加", "答案")
        compare_system.equal("電子流向", "題目", "由鋅電極流向銅電極", "答案")

    @staticmethod
    def electrolysis():
        compare_system.equivalentto("電解", "電化學", "利用外加電能驅動非自發氧化還原反應", "定義")
        compare_system.equal("電解池陽極", "反應", "氧化", "答案")
        compare_system.equal("電解池陰極", "反應", "還原", "答案")
        compare_system.equal("電解池陽極", "常見極性", "正極", "答案")
        compare_system.equal("電解池陰極", "常見極性", "負極", "答案")
        compare_system.equal("陽離子", "電場移動方向", "移向陰極", "答案")
        compare_system.equal("陰離子", "電場移動方向", "移向陽極", "答案")
        compare_system.notequal("原電池與電解池", "敘述", "陽極反應不同", "錯誤觀念")
        compare_system.equal("陽極", "永遠發生", "氧化", "答案")

    @staticmethod
    def electroplating():
        compare_system.equivalentto("電鍍", "電解應用", "利用電解在物體表面沉積金屬薄層", "定義")
        compare_system.equal("待鍍物", "電鍍接法", "陰極", "答案")
        compare_system.equal("鍍層金屬離子", "反應", "在陰極得到電子而沉積", "答案")
        compare_system.equal("金屬鍍層", "用途", "防腐蝕、裝飾或改善表面性質", "答案")
        compare_system.equal("鍍銅時 Cu²⁺", "陰極反應", "Cu²⁺ + 2e⁻ → Cu", "答案")
        compare_system.notequal("待鍍物", "敘述", "應接在陽極使金屬沉積", "錯誤觀念")

    @staticmethod
    def faraday_law():
        compare_system.equal("電解生成物質量", "一般關係", "與通過的總電量成正比", "答案")
        compare_system.calculatedby("電量", "公式", "Q = It", "答案")
        compare_system.equal("電流增加", "相同時間", "通過電量增加", "結果")
        compare_system.equal("電解時間增加", "相同電流", "生成或消耗物質量增加", "結果")
        compare_system.equal("1 mol 電子所帶電量", "名稱", "法拉第常數", "答案")
        compare_system.approximatelyequal("法拉第常數", "數值", "96485 C/mol e⁻", "答案")
        compare_system.notequal("電流較大", "敘述", "電解生成物種類一定改變", "錯誤觀念")

    @staticmethod
    def battery():
        compare_system.equivalentto("一次電池", "電池", "通常設計為使用後不再充電的電池", "定義")
        compare_system.equivalentto("二次電池", "電池", "可藉外加電能使反應逆轉並重複充電的電池", "定義")
        compare_system.equal("鋰離子電池", "分類", "二次電池", "答案")
        compare_system.equal("乾電池", "一般分類", "一次電池", "答案")
        compare_system.equal("電池放電", "能量轉換", "化學能轉換為電能", "答案")
        compare_system.equal("二次電池充電", "能量轉換", "電能轉換並儲存為化學能", "答案")
        compare_system.notequal("電池", "敘述", "能永久提供能量而不消耗反應物", "錯誤觀念")