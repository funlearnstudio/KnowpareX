# ===========================================
# notes_physics_thermodynamics.py
# 物理：溫度、熱與熱力學
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_thermodynamics:

    @staticmethod
    def temperature():
        compare_system.equivalentto("溫度", "物理量", "描述物體冷熱程度並決定熱傳方向的狀態量", "定義")
        compare_system.equal("熱自然傳遞方向", "條件", "由高溫物體傳向低溫物體", "答案")
        compare_system.equal("兩物體達到熱平衡", "結果", "溫度相同且沒有淨熱傳", "答案")
        compare_system.equal("攝氏溫標", "常用單位", "攝氏度（°C）", "答案")
        compare_system.equal("熱力學溫標", "SI 單位", "克耳文（K）", "答案")
        compare_system.calculatedby("攝氏轉克耳文", "近似公式", "T(K) = t(°C) + 273.15", "答案")
        compare_system.equal("0 K", "名稱", "絕對零度", "答案")
        compare_system.approximatelyequal("0 K", "溫度", "-273.15 °C", "溫度")
        compare_system.notequal("溫度", "物理量", "熱量", "物理量")

    @staticmethod
    def thermometer():
        compare_system.equivalentto("溫度計", "儀器", "利用物理性質隨溫度改變來測量溫度", "定義")
        compare_system.equal("液體溫度計", "原理", "液體熱脹冷縮", "答案")
        compare_system.equal("溫度計測量物體溫度", "條件", "需等待溫度計與物體接近熱平衡", "答案")
        compare_system.equal("量測範圍", "限制", "受溫度計材料與刻度範圍限制", "答案")
        compare_system.equal("紅外線溫度計", "原理", "偵測物體放出的紅外線輻射", "答案")
        compare_system.notequal("溫度計讀數", "敘述", "接觸物體瞬間立即等於物體真實溫度", "錯誤觀念")
        compare_system.equal("溫度計感測部分", "使用方式", "應與待測物充分接觸", "答案")

    @staticmethod
    def heat():
        compare_system.equivalentto("熱", "能量傳遞", "因溫度差而在物體之間傳遞的能量", "定義")
        compare_system.equal("熱量的 SI 單位", "題目", "焦耳（J）", "答案")
        compare_system.equal("高溫物體接觸低溫物體", "結果", "熱由高溫物體傳向低溫物體", "答案")
        compare_system.equal("達到熱平衡", "結果", "兩物體間沒有淨熱量傳遞", "答案")
        compare_system.notequal("物體內含有熱", "嚴格說法", "熱是傳遞中的能量，不是物體儲存的物質", "答案")
        compare_system.equal("物體吸熱", "一般情況", "內能增加", "答案")
        compare_system.equal("物體放熱", "一般情況", "內能減少", "答案")
        compare_system.notequal("吸收相同熱量", "敘述", "所有物體溫度上升都相同", "錯誤觀念")

    @staticmethod
    def specific_heat():
        compare_system.equivalentto("比熱", "物理量", "單位質量物質升高單位溫度所需的熱量", "定義")
        compare_system.calculatedby("顯熱", "公式", "Q = mcΔT", "答案")
        compare_system.calculatedby("溫度變化", "公式", "ΔT = Q ÷ mc", "答案")
        compare_system.equal("比熱的常用 SI 單位", "題目", "J/(kg·K)", "答案")
        compare_system.equal("比熱較大", "相同質量與吸熱量", "溫度變化較小", "結果")
        compare_system.equal("水的比熱", "特性", "相對較大", "答案")
        compare_system.equal("海洋調節沿海氣候", "原因之一", "水的比熱較大", "答案")
        compare_system.equal("質量 2 kg、比熱 500 J/(kg·°C)、升溫 3°C", "題目", "吸熱 3000 J", "答案")

    @staticmethod
    def calorimetry():
        compare_system.equivalentto("熱量測定", "方法", "利用能量守恆分析物體間的熱交換", "定義")
        compare_system.equal("理想隔熱系統", "熱平衡", "高溫物體放熱量等於低溫物體吸熱量", "答案")
        compare_system.calculatedby("熱平衡關係", "公式", "Q放 + Q吸 = 0", "答案")
        compare_system.equal("混合相同物質、相同質量、無熱損失", "結果", "平衡溫度為兩初溫平均", "答案")
        compare_system.equal("平衡溫度", "一般範圍", "介於兩物體初溫之間", "答案")
        compare_system.notequal("實際量熱實驗", "敘述", "完全沒有熱量散失", "錯誤觀念")
        compare_system.equal("量熱器", "作用", "盡量減少系統與外界的熱交換", "答案")

    @staticmethod
    def phase_change():
        compare_system.equivalentto("相變", "物理變化", "物質在固態、液態與氣態之間改變狀態", "定義")
        compare_system.equal("熔化", "相變", "固態變液態", "答案")
        compare_system.equal("凝固", "相變", "液態變固態", "答案")
        compare_system.equal("汽化", "相變", "液態變氣態", "答案")
        compare_system.equal("凝結", "相變", "氣態變液態", "答案")
        compare_system.equal("昇華", "相變", "固態直接變氣態", "答案")
        compare_system.equal("凝華", "相變", "氣態直接變固態", "答案")
        compare_system.equal("純物質在固定壓力下相變", "理想情況", "溫度可保持不變", "答案")
        compare_system.notequal("相變時溫度不變", "敘述", "物質沒有吸收或放出能量", "錯誤觀念")

    @staticmethod
    def latent_heat():
        compare_system.equivalentto("潛熱", "物理量", "物質相變時每單位質量吸收或放出的熱量", "定義")
        compare_system.calculatedby("相變熱量", "公式", "Q = mL", "答案")
        compare_system.equal("熔化", "能量變化", "吸收熔化潛熱", "答案")
        compare_system.equal("凝固", "能量變化", "放出凝固潛熱", "答案")
        compare_system.equal("汽化", "能量變化", "吸收汽化潛熱", "答案")
        compare_system.equal("凝結", "能量變化", "放出凝結潛熱", "答案")
        compare_system.equal("流汗可降低體溫", "原因", "汗水蒸發時吸收汽化潛熱", "答案")
        compare_system.equal("水蒸氣燙傷可能嚴重", "原因之一", "凝結時會放出潛熱", "答案")

    @staticmethod
    def conduction():
        compare_system.equivalentto("熱傳導", "熱傳方式", "能量藉粒子碰撞或自由電子移動在物質內傳遞", "定義")
        compare_system.equal("熱傳導", "是否需要介質", "需要物質介質", "答案")
        compare_system.equal("金屬", "熱傳導性", "通常較佳", "答案")
        compare_system.equal("木材、塑膠、空氣", "熱傳導性", "通常較差", "答案")
        compare_system.equal("鍋具使用金屬", "原因", "金屬導熱較快", "答案")
        compare_system.equal("鍋柄使用塑膠或木材", "原因", "降低熱傳導以避免燙傷", "答案")
        compare_system.equal("雙層玻璃中夾空氣", "作用", "減少熱傳導與對流", "答案")
        compare_system.equal("真空保溫瓶", "作用", "大幅減少傳導與對流", "答案")

    @staticmethod
    def convection():
        compare_system.equivalentto("熱對流", "熱傳方式", "流體因密度差與整體流動而傳遞熱量", "定義")
        compare_system.equal("熱對流主要發生於", "題目", "液體與氣體", "答案")
        compare_system.equal("流體受熱", "一般結果", "膨脹、密度減小並上升", "答案")
        compare_system.equal("流體冷卻", "一般結果", "密度增加並下降", "答案")
        compare_system.equal("煮水時水循環流動", "現象", "熱對流", "答案")
        compare_system.equal("海風", "形成原因之一", "陸地與海洋受熱差異造成空氣對流", "答案")
        compare_system.equal("冷氣裝在較高處", "原因之一", "冷空氣下沉有助室內對流", "答案")
        compare_system.notequal("固體內部", "敘述", "通常以物質整體流動形成熱對流", "錯誤觀念")

    @staticmethod
    def radiation():
        compare_system.equivalentto("熱輻射", "熱傳方式", "以電磁波傳遞能量", "定義")
        compare_system.equal("熱輻射", "是否需要介質", "不需要物質介質", "答案")
        compare_system.equal("太陽能量到達地球", "主要方式", "輻射", "答案")
        compare_system.equal("所有高於絕對零度的物體", "現象", "都會放出熱輻射", "答案")
        compare_system.equal("溫度愈高", "一般結果", "輻射功率通常愈大", "答案")
        compare_system.equal("黑色粗糙表面", "一般特性", "吸收與放射熱輻射能力較強", "答案")
        compare_system.equal("銀亮表面", "一般特性", "反射熱輻射能力較強", "答案")
        compare_system.equal("保溫瓶內壁鍍銀", "作用", "減少熱輻射", "答案")

    @staticmethod
    def thermal_expansion():
        compare_system.equivalentto("熱膨脹", "現象", "物質受熱後尺寸通常增大", "定義")
        compare_system.equal("物質冷卻", "一般結果", "尺寸通常縮小", "答案")
        compare_system.equal("鐵軌留縫", "原因", "避免熱膨脹造成彎曲", "答案")
        compare_system.equal("橋梁設置伸縮縫", "原因", "容納溫度改變造成的伸縮", "答案")
        compare_system.equal("金屬瓶蓋加熱", "效果", "瓶蓋膨脹後較容易打開", "答案")
        compare_system.equal("雙金屬片受熱彎曲", "原因", "兩種金屬熱膨脹程度不同", "答案")
        compare_system.notequal("所有物質受熱", "敘述", "體積一定以完全相同比例增加", "錯誤觀念")
        compare_system.equal("水在 0°C 到 4°C 間", "特殊現象", "具有反常膨脹性質", "答案")

    @staticmethod
    def gas_law():
        compare_system.equal("氣體壓力", "微觀來源", "氣體分子撞擊容器壁", "答案")
        compare_system.equal("定容氣體升溫", "一般結果", "壓力增加", "答案")
        compare_system.equal("定壓氣體升溫", "一般結果", "體積增加", "答案")
        compare_system.equal("定溫氣體體積減小", "一般結果", "壓力增加", "答案")
        compare_system.calculatedby("波以耳定律", "定溫公式", "P₁V₁ = P₂V₂", "答案")
        compare_system.calculatedby("查理定律", "定壓公式", "V₁/T₁ = V₂/T₂", "答案")
        compare_system.calculatedby("理想氣體方程式", "公式", "PV = nRT", "答案")
        compare_system.equal("氣體定律溫度", "公式使用", "應使用絕對溫度 K", "答案")
        compare_system.notequal("查理定律公式", "敘述", "可直接代入攝氏溫度而永遠正確", "錯誤觀念")

    @staticmethod
    def internal_energy():
        compare_system.equivalentto("內能", "能量", "系統內微觀粒子的動能與交互作用位能總和", "定義")
        compare_system.equal("物體溫度升高", "一般情況", "內能增加", "結果")
        compare_system.equal("物體相變", "情況", "溫度可能不變但內能仍改變", "答案")
        compare_system.equal("熱傳", "作用", "可改變系統內能", "答案")
        compare_system.equal("外界對系統做功", "作用", "可改變系統內能", "答案")
        compare_system.notequal("內能", "敘述", "只等於物體整體平移動能", "錯誤觀念")
        compare_system.notequal("兩物體溫度相同", "敘述", "內能必定相同", "錯誤觀念")

    @staticmethod
    def first_law():
        compare_system.equivalentto("熱力學第一定律", "定律", "能量守恆在熱力學系統中的表現", "定義")
        compare_system.calculatedby("熱力學第一定律", "一種符號約定", "ΔU = Q - W", "答案")
        compare_system.equal("Q > 0", "此符號約定", "系統吸收熱量", "答案")
        compare_system.equal("W > 0", "此符號約定", "系統對外做功", "答案")
        compare_system.equal("系統吸熱且不做功", "結果", "內能增加", "答案")
        compare_system.equal("絕熱過程", "定義", "系統與外界沒有熱量交換", "答案")
        compare_system.notequal("絕熱過程", "敘述", "溫度一定保持不變", "錯誤觀念")
        compare_system.equal("壓縮氣體", "可能結果", "外界對氣體做功使內能與溫度增加", "答案")