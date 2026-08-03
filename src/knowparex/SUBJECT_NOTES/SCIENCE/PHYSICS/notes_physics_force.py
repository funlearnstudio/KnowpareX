# ===========================================
# notes_physics_force.py
# 物理：力與牛頓運動定律
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_force:

    @staticmethod
    def force():
        compare_system.equivalentto("力", "物理量", "物體之間的推、拉或其他交互作用", "定義")
        compare_system.equal("力的 SI 單位", "題目", "牛頓（N）", "答案")
        compare_system.equal("力", "物理量種類", "向量", "答案")
        compare_system.equal("力的三要素", "題目", "大小、方向、作用點", "答案")
        compare_system.equal("1 牛頓", "定義", "使 1 公斤物體產生 1 m/s² 加速度所需的力", "內容")
        compare_system.equal("力可以造成的效果", "題目", "改變運動狀態或使物體形變", "答案")
        compare_system.notequal("物體正在運動", "情況", "一定有合力沿運動方向作用", "錯誤觀念")

    @staticmethod
    def net_force():
        compare_system.equivalentto("合力", "物理量", "物體所受所有力的向量總和", "定義")
        compare_system.equal("向右 10 N 與向右 5 N", "受力情況", "合力為向右 15 N", "答案")
        compare_system.equal("向右 10 N 與向左 6 N", "受力情況", "合力為向右 4 N", "答案")
        compare_system.equal("向右 8 N 與向左 8 N", "受力情況", "合力為 0 N", "答案")
        compare_system.equal("合力為 0", "條件", "物體加速度為 0", "結果")
        compare_system.notequal("合力為 0", "條件", "物體一定靜止", "錯誤觀念")
        compare_system.equal("合力不為 0", "條件", "物體產生加速度", "結果")
        compare_system.equal("加速度方向", "牛頓第二定律", "與合力方向相同", "答案")

    @staticmethod
    def newton_first():
        compare_system.equivalentto("牛頓第一運動定律", "名稱", "慣性定律", "別名")
        compare_system.equal("物體不受合力作用", "條件", "保持靜止或做等速度直線運動", "結果")
        compare_system.equivalentto("慣性", "概念", "物體維持原本運動狀態的性質", "定義")
        compare_system.equal("質量較大的物體", "慣性", "通常具有較大的慣性", "結果")
        compare_system.bigger("10 公斤物體", "慣性", "2 公斤物體", "慣性")
        compare_system.equal("公車突然煞車時乘客向前傾", "現象", "慣性的表現", "原因")
        compare_system.equal("車輛安全帶", "用途", "減少乘客因慣性造成的傷害", "答案")
        compare_system.notequal("維持等速度運動", "條件", "需要持續有向前合力", "錯誤觀念")

    @staticmethod
    def newton_second():
        compare_system.equivalentto("牛頓第二運動定律", "定律", "物體加速度由合力與質量決定", "定義")
        compare_system.calculatedby("合力", "公式", "F = ma", "答案")
        compare_system.calculatedby("加速度", "公式", "a = F ÷ m", "答案")
        compare_system.calculatedby("質量", "公式", "m = F ÷ a", "答案")
        compare_system.equal("質量固定時，合力增大", "條件", "加速度增大", "結果")
        compare_system.equal("合力固定時，質量增大", "條件", "加速度減小", "結果")
        compare_system.equal("2 公斤物體受到 10 N 合力", "題目", "加速度為 5 m/s²", "答案")
        compare_system.equal("5 公斤物體產生 3 m/s² 加速度", "題目", "合力為 15 N", "答案")
        compare_system.equal("加速度方向", "關係", "與合力方向相同", "答案")

    @staticmethod
    def newton_third():
        compare_system.equivalentto("牛頓第三運動定律", "定律", "作用力與反作用力定律", "別名")
        compare_system.equal("作用力與反作用力", "大小", "大小相等", "答案")
        compare_system.equal("作用力與反作用力", "方向", "方向相反", "答案")
        compare_system.equal("作用力與反作用力", "作用物體", "分別作用在不同物體上", "答案")
        compare_system.equal("作用力與反作用力", "發生時間", "同時產生、同時消失", "答案")
        compare_system.notequal("作用力與反作用力", "關係", "會互相抵消", "錯誤觀念")
        compare_system.equal("人向後推地面", "作用", "地面向前推人", "反作用")
        compare_system.equal("火箭向後噴出氣體", "作用", "氣體向前推動火箭", "反作用")
        compare_system.equal("書本壓桌面", "作用", "桌面向上推書本", "反作用")

    @staticmethod
    def gravity():
        compare_system.equivalentto("萬有引力", "物理現象", "任何具有質量的物體之間皆有吸引力", "定義")
        compare_system.calculatedby("萬有引力", "公式", "F = Gm₁m₂ ÷ r²", "答案")
        compare_system.equal("兩物體質量增加", "條件", "萬有引力增加", "結果")
        compare_system.equal("兩物體距離增加", "條件", "萬有引力減小", "結果")
        compare_system.equal("距離增加為原來 2 倍", "條件", "萬有引力變為原來 1/4", "結果")
        compare_system.equal("地球吸引物體", "現象", "重力", "答案")
        compare_system.equal("萬有引力方向", "題目", "沿兩物體中心連線相互吸引", "答案")
        compare_system.notequal("只有地球", "天體", "具有萬有引力", "錯誤觀念")

    @staticmethod
    def weight():
        compare_system.equivalentto("重量", "物理量", "物體受到星球引力所形成的力", "定義")
        compare_system.calculatedby("重量", "公式", "W = mg", "答案")
        compare_system.equal("重量的 SI 單位", "題目", "牛頓（N）", "答案")
        compare_system.equal("質量的 SI 單位", "題目", "公斤（kg）", "答案")
        compare_system.equal("質量為 5 kg，取 g = 10 m/s²", "題目", "重量為 50 N", "答案")
        compare_system.equal("同一物體到月球", "情況", "質量不變，重量改變", "結果")
        compare_system.notequal("質量", "物理量", "重量", "物理量")
        compare_system.equal("重量方向", "地球表面附近", "鉛直向下", "答案")

    @staticmethod
    def normal_force():
        compare_system.equivalentto("正向力", "接觸力", "接觸面垂直施於物體的力", "定義")
        compare_system.equal("正向力方向", "題目", "垂直於接觸面", "答案")
        compare_system.equal("書本靜止放在水平桌面上", "情況", "正向力大小等於重量", "答案")
        compare_system.notequal("正向力", "物理量", "重量", "物理量")
        compare_system.notequal("任何情況下的正向力", "敘述", "一定等於重量", "錯誤觀念")
        compare_system.equal("物體放在斜面上", "情況", "正向力垂直於斜面", "答案")
        compare_system.equal("正向力", "來源", "物體與接觸面之間的電磁交互作用", "答案")

    @staticmethod
    def friction():
        compare_system.equivalentto("摩擦力", "接觸力", "阻礙接觸面相對運動或相對運動趨勢的力", "定義")
        compare_system.equal("摩擦力方向", "題目", "與相對運動或相對運動趨勢相反", "答案")
        compare_system.equivalentto("靜摩擦力", "種類", "接觸面尚未相對滑動時的摩擦力", "定義")
        compare_system.equivalentto("動摩擦力", "種類", "接觸面已相對滑動時的摩擦力", "定義")
        compare_system.equal("最大靜摩擦力", "一般關係", "通常大於動摩擦力", "答案")
        compare_system.equal("接觸面愈粗糙", "一般情況", "摩擦力通常愈大", "結果")
        compare_system.equal("正向力增大", "一般情況", "最大摩擦力增大", "結果")
        compare_system.notequal("物體沒有移動", "情況", "摩擦力一定為 0", "錯誤觀念")
        compare_system.equal("走路時腳向後推地面", "現象", "地面摩擦力向前推動人體", "答案")

    @staticmethod
    def tension():
        compare_system.equivalentto("張力", "接觸力", "繩子或線拉動物體時所施的力", "定義")
        compare_system.equal("張力方向", "題目", "沿著繩子的方向", "答案")
        compare_system.equal("理想輕繩", "條件", "同一條繩各處張力大小相同", "答案")
        compare_system.equal("繩子只能", "功能", "拉物體，不能推物體", "答案")
        compare_system.equal("物體由繩子靜止懸掛", "情況", "張力大小等於重量", "答案")
        compare_system.notequal("所有情況下的張力", "敘述", "一定等於物體重量", "錯誤觀念")
        compare_system.equal("繩子斷裂", "結果", "張力消失", "答案")

    @staticmethod
    def equilibrium():
        compare_system.equivalentto("平衡狀態", "力學", "物體所受合力為 0 的狀態", "定義")
        compare_system.equal("平衡狀態", "加速度", "0 m/s²", "答案")
        compare_system.equal("靜力平衡", "運動狀態", "物體保持靜止", "答案")
        compare_system.equal("動力平衡", "運動狀態", "物體做等速度直線運動", "答案")
        compare_system.notequal("物體平衡", "敘述", "物體一定靜止", "錯誤觀念")
        compare_system.equal("水平向右 10 N、向左 10 N", "受力情況", "水平方向平衡", "答案")
        compare_system.equal("靜止書本受到重力與正向力", "受力情況", "兩力大小相等、方向相反", "答案")