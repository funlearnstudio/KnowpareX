# ===========================================
# notes_physics_energy.py
# 物理：功、能量、功率、動量
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_energy:

    @staticmethod
    def work():
        compare_system.equivalentto("功", "物理量", "力使物體沿力的方向產生位移時的能量轉移", "定義")
        compare_system.calculatedby("功", "一般公式", "W = Fs cosθ", "答案")
        compare_system.calculatedby("力與位移同方向時的功", "公式", "W = Fs", "答案")
        compare_system.equal("功的 SI 單位", "題目", "焦耳（J）", "答案")
        compare_system.equal("1 焦耳", "定義", "1 牛頓的力使物體沿力方向移動 1 公尺所做的功", "內容")
        compare_system.equal("施力 10 N，使物體沿力方向移動 3 m", "題目", "做功 30 J", "答案")
        compare_system.equal("力與位移垂直", "條件", "該力所做的功為 0", "結果")
        compare_system.equal("手水平提著書包等速前進", "情況", "手的向上支持力對書包不做功", "答案")
        compare_system.equal("力與位移方向相反", "條件", "該力做負功", "結果")

    @staticmethod
    def kinetic_energy():
        compare_system.equivalentto("動能", "能量", "物體因運動而具有的能量", "定義")
        compare_system.calculatedby("動能", "公式", "Eₖ = 1/2 mv²", "答案")
        compare_system.equal("動能的 SI 單位", "題目", "焦耳（J）", "答案")
        compare_system.equal("質量增加為原來 2 倍，速度不變", "條件", "動能增加為原來 2 倍", "結果")
        compare_system.equal("速度增加為原來 2 倍，質量不變", "條件", "動能增加為原來 4 倍", "結果")
        compare_system.equal("質量 2 kg、速度 3 m/s", "題目", "動能為 9 J", "答案")
        compare_system.equal("物體靜止", "條件", "動能為 0", "結果")
        compare_system.equal("動能", "物理量種類", "純量", "答案")

    @staticmethod
    def gravitational_potential_energy():
        compare_system.equivalentto("重力位能", "能量", "物體因所在高度而具有的能量", "定義")
        compare_system.calculatedby("地表附近的重力位能", "公式", "Eₚ = mgh", "答案")
        compare_system.equal("重力位能的 SI 單位", "題目", "焦耳（J）", "答案")
        compare_system.equal("質量增加，高度不變", "條件", "重力位能增加", "結果")
        compare_system.equal("高度增加，質量不變", "條件", "重力位能增加", "結果")
        compare_system.equal("質量 2 kg、高度 5 m，取 g = 10 m/s²", "題目", "重力位能為 100 J", "答案")
        compare_system.equal("重力位能的零點", "特性", "可以依問題方便自行選定", "答案")
        compare_system.notequal("重力位能", "敘述", "永遠只能是正值", "錯誤觀念")

    @staticmethod
    def elastic_potential_energy():
        compare_system.equivalentto("彈性位能", "能量", "彈性物體因形變而儲存的能量", "定義")
        compare_system.calculatedby("理想彈簧的彈性位能", "公式", "Eₛ = 1/2 kx²", "答案")
        compare_system.equal("彈簧形變量增加為原來 2 倍", "條件", "彈性位能增加為原來 4 倍", "結果")
        compare_system.equal("彈簧完全沒有形變", "條件", "彈性位能為 0", "結果")
        compare_system.equal("彈簧常數 k 愈大", "意義", "彈簧通常愈難拉伸或壓縮", "答案")
        compare_system.calculatedby("胡克定律", "公式", "F = -kx", "答案")
        compare_system.equal("胡克定律中的負號", "意義", "彈力方向與形變方向相反", "答案")
        compare_system.equal("橡皮筋、彈簧、弓", "例子", "可以儲存彈性位能", "答案")

    @staticmethod
    def mechanical_energy():
        compare_system.equivalentto("力學能", "能量", "動能與位能的總和", "定義")
        compare_system.calculatedby("力學能", "公式", "E = Eₖ + Eₚ", "答案")
        compare_system.equal("只有重力做功且忽略阻力", "條件", "力學能守恆", "結果")
        compare_system.equal("物體自由下落時", "能量變化", "重力位能減少、動能增加", "答案")
        compare_system.equal("物體向上拋時", "能量變化", "動能減少、重力位能增加", "答案")
        compare_system.equal("最高點瞬間", "鉛直上拋", "速度為 0，動能為 0", "答案")
        compare_system.equal("有摩擦力作用", "情況", "力學能通常不守恆", "結果")
        compare_system.notequal("力學能不守恆", "敘述", "總能量不守恆", "錯誤觀念")

    @staticmethod
    def conservation_of_energy():
        compare_system.equivalentto("能量守恆定律", "定律", "能量不會憑空產生或消失，只會轉換或轉移", "定義")
        compare_system.equal("封閉系統的總能量", "條件", "保持不變", "結果")
        compare_system.equal("燈泡發光", "能量轉換", "電能轉換為光能與熱能", "答案")
        compare_system.equal("電風扇運轉", "能量轉換", "電能轉換為動能、聲能與熱能", "答案")
        compare_system.equal("水力發電", "能量轉換", "水的位能轉換為動能，再轉換為電能", "答案")
        compare_system.equal("汽車煞車", "能量轉換", "動能主要轉換為熱能", "答案")
        compare_system.equal("植物行光合作用", "能量轉換", "光能轉換為化學能", "答案")
        compare_system.equal("食物供人體活動", "能量轉換", "化學能轉換為動能與熱能", "答案")

    @staticmethod
    def power():
        compare_system.equivalentto("功率", "物理量", "單位時間內做功或轉換能量的速率", "定義")
        compare_system.calculatedby("平均功率", "公式", "P = W ÷ t", "答案")
        compare_system.calculatedby("平均功率", "能量公式", "P = ΔE ÷ t", "答案")
        compare_system.equal("功率的 SI 單位", "題目", "瓦特（W）", "答案")
        compare_system.equal("1 瓦特", "定義", "每秒做功 1 焦耳", "內容")
        compare_system.equal("100 J 的功用時 5 秒", "題目", "功率為 20 W", "答案")
        compare_system.equal("完成相同的功所需時間較短", "條件", "功率較大", "結果")
        compare_system.notequal("功率較大的機器", "敘述", "一定做了較多的功", "錯誤觀念")
        compare_system.equal("千瓦（kW）", "單位換算", "1000 瓦特", "答案")

    @staticmethod
    def efficiency():
        compare_system.equivalentto("效率", "物理量", "有效輸出能量占輸入能量的比例", "定義")
        compare_system.calculatedby("效率", "公式", "有效輸出能量 ÷ 輸入能量 × 100%", "答案")
        compare_system.calculatedby("效率", "功率公式", "有效輸出功率 ÷ 輸入功率 × 100%", "答案")
        compare_system.equal("輸入能量 100 J，有效輸出能量 80 J", "題目", "效率為 80%", "答案")
        compare_system.equalorsmaller("實際機械效率", "一般情況", "100%", "關係")
        compare_system.notequal("效率為 80%", "敘述", "有 20% 的能量消失了", "錯誤觀念")
        compare_system.equal("未成為有效輸出的能量", "情況", "通常轉換為熱能、聲能等形式", "答案")
        compare_system.equal("減少摩擦", "方法", "通常能提高機械效率", "答案")

    @staticmethod
    def momentum():
        compare_system.equivalentto("動量", "物理量", "質量與速度的乘積", "定義")
        compare_system.calculatedby("動量", "公式", "p = mv", "答案")
        compare_system.equal("動量的 SI 單位", "題目", "kg·m/s", "答案")
        compare_system.equal("動量", "物理量種類", "向量", "答案")
        compare_system.equal("質量 2 kg、速度向東 3 m/s", "題目", "動量為向東 6 kg·m/s", "答案")
        compare_system.equal("物體靜止", "條件", "動量為 0", "結果")
        compare_system.equal("速度反向", "條件", "動量方向也反向", "結果")
        compare_system.equal("速度相同時，質量較大", "條件", "動量大小較大", "結果")

    @staticmethod
    def impulse():
        compare_system.equivalentto("衝量", "物理量", "力在一段時間內造成的作用效果", "定義")
        compare_system.calculatedby("衝量", "公式", "J = FΔt", "答案")
        compare_system.equivalentto("衝量", "動量關係", "動量變化量 Δp", "答案")
        compare_system.calculatedby("衝量—動量定理", "公式", "FΔt = Δp", "答案")
        compare_system.equal("衝量的 SI 單位", "題目", "N·s", "答案")
        compare_system.equal("10 N 的力作用 3 秒", "題目", "衝量為 30 N·s", "答案")
        compare_system.equal("安全氣囊延長碰撞時間", "效果", "在相同動量變化下減小平均作用力", "答案")
        compare_system.equal("接球時手向後縮", "效果", "延長停止時間並減小平均作用力", "答案")

    @staticmethod
    def collision():
        compare_system.equivalentto("動量守恆", "碰撞定律", "封閉系統碰撞前後的總動量相同", "定義")
        compare_system.equal("動量守恆的條件", "題目", "系統所受外力合衝量可忽略", "答案")
        compare_system.calculatedby("一維碰撞動量守恆", "公式", "m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'", "答案")
        compare_system.equivalentto("彈性碰撞", "碰撞種類", "動量與總動能皆守恆", "定義")
        compare_system.equivalentto("非彈性碰撞", "碰撞種類", "動量守恆，但總動能不一定守恆", "定義")
        compare_system.equivalentto("完全非彈性碰撞", "碰撞種類", "碰撞後兩物體黏在一起運動", "定義")
        compare_system.notequal("碰撞過程中動能減少", "敘述", "能量消失", "錯誤觀念")
        compare_system.equal("碰撞中減少的動能", "轉換", "可能轉換為熱能、聲能與形變能", "答案")