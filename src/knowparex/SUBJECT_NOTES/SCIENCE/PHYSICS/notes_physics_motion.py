# ===========================================
# notes_physics_motion.py
# 物理：運動學
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_motion:

    @staticmethod
    def distance():
        compare_system.equivalentto("路程", "物理量", "物體實際移動路徑的總長度", "定義")
        compare_system.equal("路程的 SI 單位", "題目", "公尺（m）", "答案")
        compare_system.equal("路程", "物理量種類", "純量", "答案")
        compare_system.equal("純量", "定義", "只有大小，沒有方向的物理量", "內容")
        compare_system.equal("向東走 3 公尺，再向西走 4 公尺", "運動情況", "路程為 7 公尺", "答案")
        compare_system.equal("沿著 400 公尺跑道完整跑一圈", "運動情況", "路程為 400 公尺", "答案")
        compare_system.equal("向前走 20 公尺，再向後走 10 公尺", "運動情況", "路程為 30 公尺", "答案")
        compare_system.equal("物體保持靜止", "運動情況", "路程為 0 公尺", "答案")

    @staticmethod
    def displacement():
        compare_system.equivalentto("位移", "物理量", "物體由起點到終點的位置變化", "定義")
        compare_system.calculatedby("位移", "目標", "末位置－初位置", "公式")
        compare_system.equal("位移的 SI 單位", "題目", "公尺（m）", "答案")
        compare_system.equal("位移", "物理量種類", "向量", "答案")
        compare_system.equal("向量", "定義", "同時具有大小與方向的物理量", "內容")
        compare_system.equal("向東走 3 公尺，再向西走 4 公尺", "運動情況", "位移為向西 1 公尺", "答案")
        compare_system.equal("完整繞一圈後回到起點", "運動情況", "位移為 0 公尺", "答案")
        compare_system.equal("初位置為 2 公尺，末位置為 11 公尺", "題目", "位移為 9 公尺", "答案")
        compare_system.equal("初位置為 8 公尺，末位置為 3 公尺", "題目", "位移為 -5 公尺", "答案")

    @staticmethod
    def distance_and_displacement():
        compare_system.equalorbigger("路程", "運動量值", "位移的大小", "關係")
        compare_system.notequal("路程", "物理量", "位移", "物理量")
        compare_system.equal("全程沿同一直線且不改變方向", "條件", "路程等於位移的大小", "結果")
        compare_system.equal("最後回到起點", "條件", "位移為 0", "結果")
        compare_system.equal("最後回到起點", "條件", "路程不一定為 0", "結果")
        compare_system.equal("繞圓形跑道完整跑一圈", "運動情況", "位移為 0", "答案")
        compare_system.equal("繞圓形跑道完整跑一圈", "運動情況", "路程等於圓周長", "答案")

    @staticmethod
    def speed():
        compare_system.equivalentto("速率", "物理量", "單位時間內通過的路程", "定義")
        compare_system.calculatedby("平均速率", "目標", "總路程 ÷ 總時間", "公式")
        compare_system.equal("速率的 SI 單位", "題目", "公尺／秒（m/s）", "答案")
        compare_system.equal("常用速率單位", "題目", "公里／小時（km/h）", "答案")
        compare_system.equal("100 公尺用時 20 秒", "題目", "平均速率為 5 m/s", "答案")
        compare_system.equal("120 公里用時 2 小時", "題目", "平均速率為 60 km/h", "答案")
        compare_system.approximatelyequal("36 km/h", "速率", "10 m/s", "速率")
        compare_system.approximatelyequal("72 km/h", "速率", "20 m/s", "速率")
        compare_system.equal("速率", "物理量種類", "純量", "答案")

    @staticmethod
    def velocity():
        compare_system.equivalentto("速度", "物理量", "單位時間內的位移變化", "定義")
        compare_system.calculatedby("平均速度", "目標", "位移 ÷ 時間", "公式")
        compare_system.equal("速度的 SI 單位", "題目", "公尺／秒（m/s）", "答案")
        compare_system.equal("速度", "物理量種類", "向量", "答案")
        compare_system.equal("向東位移 20 公尺，用時 4 秒", "題目", "平均速度為向東 5 m/s", "答案")
        compare_system.equal("繞跑道一圈回到起點，用時 50 秒", "題目", "平均速度為 0 m/s", "答案")
        compare_system.notequal("速率", "物理量", "速度", "物理量")
        compare_system.equal("速度改變", "情況", "大小改變或方向改變", "定義")
        compare_system.equal("物體等速率做圓周運動", "情況", "速度仍然持續改變", "結果")

    @staticmethod
    def acceleration():
        compare_system.equivalentto("加速度", "物理量", "速度隨時間的變化率", "定義")
        compare_system.calculatedby("平均加速度", "目標", "速度變化量 ÷ 經過時間", "公式")
        compare_system.calculatedby("加速度", "符號公式", "a = Δv ÷ Δt", "公式")
        compare_system.equal("加速度的 SI 單位", "題目", "公尺／秒平方（m/s²）", "答案")
        compare_system.equal("速度由 0 m/s 增加到 20 m/s，共用 5 秒", "題目", "加速度為 4 m/s²", "答案")
        compare_system.equal("速度由 20 m/s 降到 5 m/s，共用 3 秒", "題目", "加速度為 -5 m/s²", "答案")
        compare_system.equal("速度大小與方向都不改變", "條件", "加速度為 0", "結果")
        compare_system.notequal("加速度為負", "情況", "物體一定向後運動", "錯誤觀念")
        compare_system.equal("加速度方向與速度方向相反", "條件", "物體速率通常減小", "結果")
        compare_system.equal("加速度方向與速度方向相同", "條件", "物體速率通常增加", "結果")

    @staticmethod
    def uniform_motion():
        compare_system.equivalentto("等速度運動", "運動種類", "速度大小與方向皆保持不變", "定義")
        compare_system.equal("等速度運動", "加速度", "0 m/s²", "答案")
        compare_system.calculatedby("等速度運動的位移", "目標", "速度 × 時間", "公式")
        compare_system.calculatedby("等速度運動", "符號公式", "Δx = vt", "公式")
        compare_system.equal("速度為 5 m/s，運動 4 秒", "題目", "位移為 20 公尺", "答案")
        compare_system.equal("等速度運動的位置—時間圖", "圖形", "斜直線", "答案")
        compare_system.equal("位置—時間圖的斜率", "物理意義", "速度", "答案")
        compare_system.equal("位置—時間圖斜率為 0", "圖形意義", "物體靜止", "答案")

    @staticmethod
    def uniformly_accelerated_motion():
        compare_system.equivalentto("等加速度運動", "運動種類", "加速度保持不變的運動", "定義")
        compare_system.calculatedby("末速度", "公式", "v = v₀ + at", "答案")
        compare_system.calculatedby("位移", "公式", "Δx = v₀t + 1/2 at²", "答案")
        compare_system.calculatedby("速度平方關係", "公式", "v² = v₀² + 2aΔx", "答案")
        compare_system.equal("初速度為 0，加速度為 2 m/s²，經過 5 秒", "題目", "末速度為 10 m/s", "答案")
        compare_system.equal("初速度為 3 m/s，加速度為 2 m/s²，經過 4 秒", "題目", "末速度為 11 m/s", "答案")
        compare_system.equal("速度—時間圖為斜直線", "條件", "加速度固定", "結果")
        compare_system.equal("速度—時間圖的斜率", "物理意義", "加速度", "答案")
        compare_system.equal("速度—時間圖下方的面積", "物理意義", "位移", "答案")

    @staticmethod
    def free_fall():
        compare_system.equivalentto("自由落體", "運動種類", "只受重力作用的落下運動", "定義")
        compare_system.equal("忽略空氣阻力時的自由落體加速度", "地球表面附近", "約 9.8 m/s² 向下", "答案")
        compare_system.approximatelyequal("重力加速度 g", "近似值", "10 m/s²", "常用近似")
        compare_system.equal("不同質量物體在真空中同時自由落下", "情況", "加速度相同", "結果")
        compare_system.notequal("較重的物體", "自由落體", "一定比較輕的物體先落地", "錯誤觀念")
        compare_system.calculatedby("由靜止自由落下的速度", "公式", "v = gt", "答案")
        compare_system.calculatedby("由靜止自由落下的距離", "公式", "h = 1/2 gt²", "答案")
        compare_system.equal("由靜止自由落下 2 秒，取 g = 10 m/s²", "題目", "速度為 20 m/s 向下", "答案")
        compare_system.equal("由靜止自由落下 2 秒，取 g = 10 m/s²", "題目", "下降距離為 20 公尺", "答案")

    @staticmethod
    def graph():
        compare_system.equal("位置—時間圖的斜率", "物理意義", "速度", "答案")
        compare_system.equal("速度—時間圖的斜率", "物理意義", "加速度", "答案")
        compare_system.equal("速度—時間圖與時間軸之間的面積", "物理意義", "位移", "答案")
        compare_system.equal("位置—時間圖為水平線", "圖形", "物體靜止", "答案")
        compare_system.equal("位置—時間圖斜率愈大", "圖形", "速度大小通常愈大", "答案")
        compare_system.equal("速度—時間圖為水平線", "圖形", "速度固定", "答案")
        compare_system.equal("速度—時間圖向上傾斜", "圖形", "加速度為正", "答案")
        compare_system.equal("速度—時間圖向下傾斜", "圖形", "加速度為負", "答案")