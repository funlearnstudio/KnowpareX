# ===========================================
# notes_physics_fluid_machine.py
# 物理：壓力、流體與簡單機械
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_fluid_machine:

    @staticmethod
    def pressure():
        compare_system.equivalentto("壓力", "物理量", "單位面積上所受的垂直作用力", "定義")
        compare_system.calculatedby("壓力", "公式", "P = F ÷ A", "答案")
        compare_system.equal("壓力的 SI 單位", "題目", "帕斯卡（Pa）", "答案")
        compare_system.equal("1 帕斯卡", "定義", "每平方公尺受到 1 牛頓垂直力", "內容")
        compare_system.equal("作用力增加、面積不變", "條件", "壓力增加", "結果")
        compare_system.equal("接觸面積增加、作用力不變", "條件", "壓力減小", "結果")
        compare_system.equal("刀刃做得很薄", "原因", "減小面積以增大壓力", "答案")
        compare_system.equal("雪鞋面積較大", "原因", "增加面積以減小壓力", "答案")

    @staticmethod
    def liquid_pressure():
        compare_system.equal("液體壓力", "來源", "液體重量與粒子作用", "答案")
        compare_system.calculatedby("靜止液體壓力差", "公式", "P = ρgh", "答案")
        compare_system.equal("液體深度增加", "條件", "液體壓力增加", "結果")
        compare_system.equal("液體密度增加", "條件", "同深度壓力增加", "結果")
        compare_system.equal("同一靜止液體同一深度", "關係", "壓力相同", "答案")
        compare_system.equal("液體壓力方向", "特性", "對各方向皆存在並垂直作用面", "答案")
        compare_system.equal("水壩下方較厚", "原因", "水深較大處壓力較大", "答案")
        compare_system.notequal("容器形狀不同", "同液體同深度", "壓力一定不同", "錯誤觀念")

    @staticmethod
    def atmospheric_pressure():
        compare_system.equivalentto("大氣壓力", "物理量", "大氣因重量與分子運動對物體施加的壓力", "定義")
        compare_system.equal("海平面標準大氣壓", "近似值", "1.01 × 10⁵ Pa", "答案")
        compare_system.equal("海拔升高", "一般結果", "大氣壓力降低", "答案")
        compare_system.equal("吸管喝飲料", "原理", "降低管內壓力後由外界大氣壓推動液體上升", "答案")
        compare_system.equal("吸盤貼住牆面", "原理", "內外壓力差", "答案")
        compare_system.equal("水銀氣壓計", "用途", "測量大氣壓力", "答案")
        compare_system.notequal("吸管吸水", "敘述", "嘴巴直接把水拉上來", "錯誤觀念")
        compare_system.equal("高山上水的沸點較低", "原因之一", "外界大氣壓較低", "答案")

    @staticmethod
    def pascal_law():
        compare_system.equivalentto("帕斯卡原理", "定律", "密閉液體受到的壓力變化會完整傳到各處", "定義")
        compare_system.calculatedby("液壓機壓力關係", "公式", "F₁/A₁ = F₂/A₂", "答案")
        compare_system.equal("輸出活塞面積較大", "結果", "可得到較大的輸出力", "答案")
        compare_system.equal("液壓機省力", "代價", "施力端需要移動較長距離", "答案")
        compare_system.equal("液壓千斤頂", "原理", "帕斯卡原理", "答案")
        compare_system.equal("汽車液壓煞車", "原理", "帕斯卡原理", "答案")
        compare_system.notequal("液壓機", "敘述", "能無限制放大能量", "錯誤觀念")
        compare_system.equal("理想液壓機", "能量關係", "輸入功等於輸出功", "答案")

    @staticmethod
    def buoyancy():
        compare_system.equivalentto("浮力", "物理量", "流體對浸入其中物體產生的向上合力", "定義")
        compare_system.equivalentto("阿基米德原理", "定律", "浮力等於物體排開流體的重量", "定義")
        compare_system.calculatedby("浮力", "公式", "F浮 = ρ流體 g V排開", "答案")
        compare_system.equal("物體完全浸入同一液體", "若體積不變", "浮力通常不隨深度改變", "答案")
        compare_system.equal("排開液體體積增加", "條件", "浮力增加", "結果")
        compare_system.equal("液體密度增加", "條件", "相同排開體積的浮力增加", "結果")
        compare_system.equal("物體漂浮靜止", "受力關係", "浮力等於重量", "答案")
        compare_system.equal("物體懸浮靜止", "受力關係", "浮力等於重量", "答案")
        compare_system.equal("物體下沉加速", "常見關係", "重量大於浮力", "答案")

    @staticmethod
    def floating_and_sinking():
        compare_system.equal("物體平均密度小於液體密度", "一般結果", "物體傾向漂浮", "答案")
        compare_system.equal("物體平均密度等於液體密度", "一般結果", "物體可能懸浮", "答案")
        compare_system.equal("物體平均密度大於液體密度", "一般結果", "物體傾向下沉", "答案")
        compare_system.equal("鋼製大船可漂浮", "原因", "包含空氣後整體平均密度小於水", "答案")
        compare_system.equal("潛水艇下潛", "方法", "增加壓載艙內的水以提高平均密度", "答案")
        compare_system.equal("潛水艇上浮", "方法", "排出壓載艙的水以降低平均密度", "答案")
        compare_system.notequal("會浮的物體", "敘述", "材料本身密度一定小於水", "錯誤觀念")

    @staticmethod
    def continuity():
        compare_system.equivalentto("連續方程式", "流體關係", "穩定不可壓縮流體的體積流率保持不變", "定義")
        compare_system.calculatedby("連續方程式", "公式", "A₁v₁ = A₂v₂", "答案")
        compare_system.equal("管道截面積減小", "穩定不可壓縮流", "流速增加", "結果")
        compare_system.equal("管道截面積增加", "穩定不可壓縮流", "流速減小", "結果")
        compare_system.equal("水管出口用手壓窄", "結果", "水流速度通常增加", "答案")
        compare_system.equal("體積流率", "定義", "單位時間內通過截面的流體體積", "答案")
        compare_system.calculatedby("體積流率", "公式", "Q = Av", "答案")

    @staticmethod
    def bernoulli():
        compare_system.equivalentto("白努力原理", "流體定律", "理想流體沿流線的壓力能、動能與位能總和保持不變", "定義")
        compare_system.calculatedby("白努力方程式", "公式", "P + 1/2ρv² + ρgh = 常數", "答案")
        compare_system.equal("同高度流體速度增加", "理想條件", "靜壓通常減小", "結果")
        compare_system.equal("飛機機翼升力", "簡化說明之一", "上下方流速與壓力差造成合力", "答案")
        compare_system.equal("噴霧器", "原理之一", "高速氣流造成低壓並吸起液體", "答案")
        compare_system.equal("強風吹過屋頂", "可能結果", "屋頂上方壓力降低而產生向上作用", "答案")
        compare_system.notequal("白努力原理", "敘述", "所有黏滯、紊流情況都能直接精確套用", "錯誤觀念")

    @staticmethod
    def torque():
        compare_system.equivalentto("力矩", "物理量", "力使物體繞支點轉動的效果", "定義")
        compare_system.calculatedby("力矩", "公式", "τ = rF sinθ", "答案")
        compare_system.equal("力矩的 SI 單位", "題目", "N·m", "答案")
        compare_system.equal("作用力增加", "其他條件相同", "力矩增加", "結果")
        compare_system.equal("力臂增加", "其他條件相同", "力矩增加", "結果")
        compare_system.equal("力的作用線通過支點", "條件", "力矩為 0", "結果")
        compare_system.equal("開門時推門把", "原因", "門把離轉軸較遠可產生較大力矩", "答案")
        compare_system.equal("使用長扳手", "原因", "增加力臂以較省力地轉動螺帽", "答案")

    @staticmethod
    def rotational_equilibrium():
        compare_system.equivalentto("轉動平衡", "條件", "順時針力矩總和等於逆時針力矩總和", "定義")
        compare_system.equal("物體完全靜力平衡", "條件", "合力為 0 且合力矩為 0", "答案")
        compare_system.calculatedby("槓桿平衡", "公式", "F₁d₁ = F₂d₂", "答案")
        compare_system.equal("較小的力", "要平衡較大的力", "需要較大的力臂", "答案")
        compare_system.equal("蹺蹺板平衡", "條件", "兩側相反方向力矩大小相等", "答案")
        compare_system.notequal("合力為 0", "敘述", "一定代表合力矩為 0", "錯誤觀念")
        compare_system.notequal("合力矩為 0", "敘述", "一定代表合力為 0", "錯誤觀念")

    @staticmethod
    def lever():
        compare_system.equivalentto("槓桿", "簡單機械", "可繞支點轉動的剛體", "定義")
        compare_system.equal("槓桿三要素", "題目", "支點、施力點、抗力點", "答案")
        compare_system.equal("第一類槓桿", "排列", "支點位於施力與抗力之間", "答案")
        compare_system.equal("第二類槓桿", "排列", "抗力位於支點與施力之間", "答案")
        compare_system.equal("第三類槓桿", "排列", "施力位於支點與抗力之間", "答案")
        compare_system.equal("剪刀、鉗子、蹺蹺板", "例子", "第一類槓桿", "答案")
        compare_system.equal("獨輪車、開瓶器", "例子", "第二類槓桿", "答案")
        compare_system.equal("鑷子、人的前臂", "例子", "第三類槓桿", "答案")
        compare_system.notequal("所有槓桿", "敘述", "都一定省力", "錯誤觀念")

    @staticmethod
    def pulley():
        compare_system.equivalentto("定滑輪", "簡單機械", "軸固定不移動的滑輪", "定義")
        compare_system.equal("理想定滑輪", "主要功能", "改變施力方向但不省力", "答案")
        compare_system.equivalentto("動滑輪", "簡單機械", "滑輪會隨負載一起移動", "定義")
        compare_system.equal("單一理想動滑輪", "效果", "理想情況可使所需拉力減半", "答案")
        compare_system.equal("動滑輪省力", "代價", "需要拉較長的繩子", "答案")
        compare_system.equal("滑輪組理想機械利益", "判斷", "等於支撐活動負載的繩段數", "答案")
        compare_system.notequal("滑輪組省力", "敘述", "代表輸出功大於輸入功", "錯誤觀念")
        compare_system.equal("實際滑輪", "情況", "因摩擦與滑輪重量而效率小於 100%", "答案")

    @staticmethod
    def inclined_plane():
        compare_system.equivalentto("斜面", "簡單機械", "以較長距離換取較小施力的傾斜平面", "定義")
        compare_system.equal("斜面愈長且高度相同", "一般結果", "理想所需推力愈小", "答案")
        compare_system.equal("斜面省力", "代價", "移動距離增加", "答案")
        compare_system.calculatedby("理想斜面機械利益", "公式", "斜面長度 ÷ 高度", "答案")
        compare_system.equal("螺絲", "原理", "可視為繞在圓柱上的斜面", "答案")
        compare_system.equal("楔子", "原理", "可視為兩個斜面組成", "答案")
        compare_system.notequal("理想斜面", "敘述", "可以同時省力又省距離", "錯誤觀念")
        compare_system.equal("有摩擦斜面", "結果", "實際所需施力比理想情況大", "答案")

    @staticmethod
    def mechanical_advantage():
        compare_system.equivalentto("機械利益", "物理量", "輸出力與輸入力的比值", "定義")
        compare_system.calculatedby("實際機械利益", "公式", "MA = 輸出力 ÷ 輸入力", "答案")
        compare_system.equal("機械利益大於 1", "意義", "機械具有省力效果", "答案")
        compare_system.equal("機械利益小於 1", "可能意義", "以較大施力換取速度或距離優勢", "答案")
        compare_system.equal("理想機械", "功的關係", "輸入功等於輸出功", "答案")
        compare_system.calculatedby("機械效率", "公式", "輸出功 ÷ 輸入功 × 100%", "答案")
        compare_system.equalorsmaller("實際機械效率", "一般關係", "100%", "答案")
        compare_system.notequal("省力機械", "敘述", "也一定省功", "錯誤觀念")