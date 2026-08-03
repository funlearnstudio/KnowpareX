# ===========================================
# notes_physics_magnetism.py
# 物理：磁場與電磁學
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_magnetism:

    @staticmethod
    def magnet():
        compare_system.equivalentto("磁鐵", "物體", "能產生磁場並吸引特定磁性物質的物體", "定義")
        compare_system.equal("磁極種類", "題目", "北極與南極", "答案")
        compare_system.equal("同名磁極", "交互作用", "互相排斥", "答案")
        compare_system.equal("異名磁極", "交互作用", "互相吸引", "答案")
        compare_system.equal("磁鐵磁力通常最強的位置", "題目", "兩端磁極附近", "答案")
        compare_system.equal("將條形磁鐵切成兩段", "結果", "每段仍各有南北兩極", "答案")
        compare_system.notequal("切開磁鐵", "結果", "可以得到單獨北極與單獨南極", "錯誤觀念")
        compare_system.equal("鐵、鈷、鎳", "材料", "常見磁性物質", "答案")

    @staticmethod
    def magnetic_field():
        compare_system.equivalentto("磁場", "物理概念", "磁鐵或電流周圍能產生磁力作用的空間", "定義")
        compare_system.equal("磁場方向", "定義", "小磁針北極所指的方向", "答案")
        compare_system.equal("磁鐵外部磁力線方向", "題目", "由北極指向南極", "答案")
        compare_system.equal("磁鐵內部磁力線方向", "題目", "由南極指向北極", "答案")
        compare_system.equal("磁力線", "形狀", "形成封閉曲線", "答案")
        compare_system.equal("磁力線愈密集", "意義", "磁場通常愈強", "答案")
        compare_system.notequal("磁力線", "敘述", "會彼此交叉", "錯誤觀念")
        compare_system.notequal("磁力線", "敘述", "是真實存在的細線", "錯誤觀念")

    @staticmethod
    def earth_magnetism():
        compare_system.equal("地球", "磁性", "可近似視為一個巨大磁鐵", "答案")
        compare_system.equal("指南針北端", "現象", "大致指向地理北方", "答案")
        compare_system.equal("地理北極附近", "地磁性質", "接近地磁南極", "答案")
        compare_system.equal("指南針", "原理", "磁針沿地球磁場方向排列", "答案")
        compare_system.equal("地磁場", "作用", "可協助阻擋部分太陽風帶電粒子", "答案")
        compare_system.equal("極光", "形成關係", "帶電粒子受地磁場引導後與大氣作用", "答案")
        compare_system.notequal("地理北極", "概念", "完全等同地磁北極", "錯誤觀念")

    @staticmethod
    def current_magnetic_field():
        compare_system.equal("載流導線周圍", "現象", "會產生磁場", "答案")
        compare_system.equivalentto("電流磁效應", "概念", "電流能在周圍建立磁場", "定義")
        compare_system.equal("直導線周圍磁力線", "形狀", "以導線為中心的同心圓", "答案")
        compare_system.equal("電流方向反轉", "結果", "磁場方向反轉", "答案")
        compare_system.equal("電流增大", "其他條件相同", "磁場通常增強", "結果")
        compare_system.equal("距離導線愈遠", "其他條件相同", "磁場通常愈弱", "結果")
        compare_system.equal("判斷直導線磁場方向", "方法", "右手定則", "答案")
        compare_system.equal("右手拇指", "直導線右手定則", "指向傳統電流方向", "答案")
        compare_system.equal("右手彎曲四指", "直導線右手定則", "指出磁場環繞方向", "答案")

    @staticmethod
    def solenoid():
        compare_system.equivalentto("螺線管", "裝置", "由許多圈導線繞成的線圈", "定義")
        compare_system.equal("通電螺線管的磁場", "特性", "類似條形磁鐵的磁場", "答案")
        compare_system.equal("螺線管電流增大", "條件", "磁場增強", "結果")
        compare_system.equal("螺線管單位長度匝數增加", "條件", "磁場增強", "結果")
        compare_system.equal("螺線管加入鐵芯", "條件", "磁場通常大幅增強", "結果")
        compare_system.equal("電流方向反轉", "結果", "螺線管南北極互換", "答案")
        compare_system.equal("判斷螺線管北極", "方法", "右手握線圈定則", "答案")
        compare_system.equal("右手四指", "螺線管定則", "沿線圈電流方向彎曲", "答案")
        compare_system.equal("右手拇指", "螺線管定則", "指向螺線管北極", "答案")

    @staticmethod
    def electromagnet():
        compare_system.equivalentto("電磁鐵", "裝置", "利用通電線圈產生磁性的裝置", "定義")
        compare_system.equal("電磁鐵斷電", "結果", "磁性大幅減弱或消失", "答案")
        compare_system.equal("增加線圈匝數", "方法", "可增強電磁鐵磁力", "答案")
        compare_system.equal("增加電流", "方法", "可增強電磁鐵磁力", "答案")
        compare_system.equal("加入軟鐵芯", "方法", "可增強電磁鐵磁力", "答案")
        compare_system.equal("電磁鐵優點", "題目", "磁性可控制，磁極可交換", "答案")
        compare_system.equal("電鈴、電磁起重機、繼電器", "例子", "電磁鐵的應用", "答案")
        compare_system.notequal("永久磁鐵", "敘述", "磁性可以靠開關直接關閉", "錯誤觀念")

    @staticmethod
    def magnetic_force_on_wire():
        compare_system.equal("載流導線置於磁場中", "現象", "可能受到磁力作用", "答案")
        compare_system.equal("導線受磁力方向", "關係", "垂直於電流方向與磁場方向", "答案")
        compare_system.equal("電流方向反轉", "結果", "磁力方向反轉", "答案")
        compare_system.equal("磁場方向反轉", "結果", "磁力方向反轉", "答案")
        compare_system.equal("電流與磁場平行", "條件", "磁力為 0", "結果")
        compare_system.calculatedby("載流導線磁力", "公式", "F = BIL sinθ", "答案")
        compare_system.equal("電流增大", "其他條件相同", "磁力增大", "結果")
        compare_system.equal("馬達", "基本原理", "通電線圈在磁場中受力而轉動", "答案")

    @staticmethod
    def electric_motor():
        compare_system.equivalentto("電動機", "裝置", "將電能轉換為機械能的裝置", "定義")
        compare_system.equal("電動機基本原理", "題目", "載流導線在磁場中受到磁力", "答案")
        compare_system.equal("直流馬達換向器", "作用", "定期改變線圈電流方向以維持轉動", "答案")
        compare_system.equal("馬達輸入能量", "題目", "電能", "答案")
        compare_system.equal("馬達主要輸出能量", "題目", "機械能", "答案")
        compare_system.equal("馬達運轉時", "伴隨轉換", "也會產生熱能與聲能", "答案")
        compare_system.equal("電風扇、洗衣機、電動車", "例子", "電動機的應用", "答案")

    @staticmethod
    def electromagnetic_induction():
        compare_system.equivalentto("電磁感應", "現象", "穿過線圈的磁通量改變時產生感應電動勢", "定義")
        compare_system.equal("磁鐵在線圈內保持靜止", "情況", "通常不產生持續感應電流", "答案")
        compare_system.equal("磁鐵快速移動", "其他條件相同", "感應電動勢通常較大", "結果")
        compare_system.equal("線圈匝數增加", "其他條件相同", "感應電動勢通常增大", "結果")
        compare_system.equal("磁場變化愈快", "條件", "感應電動勢通常愈大", "結果")
        compare_system.equal("磁鐵移動方向反轉", "結果", "感應電流方向反轉", "答案")
        compare_system.equivalentto("楞次定律", "定律", "感應電流產生的磁場會反抗磁通量的變化", "定義")
        compare_system.equal("發電機", "基本原理", "電磁感應", "答案")

    @staticmethod
    def generator():
        compare_system.equivalentto("發電機", "裝置", "將機械能轉換為電能的裝置", "定義")
        compare_system.equal("發電機基本原理", "題目", "電磁感應", "答案")
        compare_system.equal("線圈與磁場相對運動", "結果", "產生感應電動勢", "答案")
        compare_system.equal("發電機輸入能量", "題目", "機械能", "答案")
        compare_system.equal("發電機主要輸出能量", "題目", "電能", "答案")
        compare_system.notequal("發電機", "敘述", "憑空製造能量", "錯誤觀念")
        compare_system.equal("水力發電", "能量轉換", "水的位能與動能轉換為電能", "答案")
        compare_system.equal("風力發電", "能量轉換", "風的動能轉換為電能", "答案")

    @staticmethod
    def transformer():
        compare_system.equivalentto("變壓器", "裝置", "利用電磁感應改變交流電壓的裝置", "定義")
        compare_system.calculatedby("理想變壓器電壓比", "公式", "Vₛ/Vₚ = Nₛ/Nₚ", "答案")
        compare_system.equal("次級線圈匝數多於初級", "條件", "升壓變壓器", "答案")
        compare_system.equal("次級線圈匝數少於初級", "條件", "降壓變壓器", "答案")
        compare_system.equal("理想變壓器輸入功率", "關係", "等於輸出功率", "答案")
        compare_system.calculatedby("理想變壓器電流比", "公式", "Iₛ/Iₚ = Nₚ/Nₛ", "答案")
        compare_system.equal("長距離輸電採高電壓", "原因", "可降低相同功率下的電流與線路損耗", "答案")
        compare_system.equal("一般變壓器", "適用電流", "交流電", "答案")
        compare_system.notequal("一般變壓器", "敘述", "可直接對穩定直流電持續變壓", "錯誤觀念")