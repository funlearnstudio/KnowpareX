# ===========================================
# notes_physics_light.py
# 物理：光、反射、折射與成像
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_light:

    @staticmethod
    def light():
        compare_system.equivalentto("光", "物理現象", "人眼可感知的一部分電磁波", "定義")
        compare_system.equal("光在真空中", "情況", "可以傳播", "答案")
        compare_system.equal("真空中的光速", "近似值", "3.0 × 10⁸ m/s", "答案")
        compare_system.equal("光在均勻介質中", "基本模型", "沿直線傳播", "答案")
        compare_system.equal("影子的形成", "主要原因", "光沿直線傳播且被不透明物體阻擋", "答案")
        compare_system.equal("日食與月食", "主要原理", "光直線傳播與天體遮擋", "答案")
        compare_system.notequal("人眼看到物體", "敘述", "是眼睛主動發出光照到物體", "錯誤觀念")
        compare_system.equal("看見不發光物體", "原因", "物體反射的光進入眼睛", "答案")

    @staticmethod
    def luminous_object():
        compare_system.equivalentto("發光體", "物體種類", "本身能發出可見光的物體", "定義")
        compare_system.equal("太陽", "分類", "發光體", "答案")
        compare_system.equal("點亮的燈泡", "分類", "發光體", "答案")
        compare_system.equal("月球", "分類", "本身不是可見光發光體", "答案")
        compare_system.equal("月球可被看見", "原因", "反射太陽光", "答案")
        compare_system.equal("鏡子", "分類", "反光物體而非一般發光體", "答案")
        compare_system.notequal("看得見的物體", "敘述", "一定都是發光體", "錯誤觀念")

    @staticmethod
    def reflection():
        compare_system.equivalentto("光的反射", "現象", "光照到介面後返回原介質", "定義")
        compare_system.equal("入射角", "定義", "入射光線與法線的夾角", "答案")
        compare_system.equal("反射角", "定義", "反射光線與法線的夾角", "答案")
        compare_system.equal("反射定律", "關係", "入射角等於反射角", "答案")
        compare_system.equal("入射光線、反射光線與法線", "關係", "位於同一平面", "答案")
        compare_system.notequal("入射角", "敘述", "光線與鏡面的夾角", "錯誤觀念")
        compare_system.equal("光垂直入射鏡面", "結果", "沿原路反射", "答案")

    @staticmethod
    def regular_and_diffuse_reflection():
        compare_system.equivalentto("規則反射", "反射種類", "平行光照到平滑表面後仍有規則地反射", "定義")
        compare_system.equivalentto("漫反射", "反射種類", "平行光照到粗糙表面後向不同方向反射", "定義")
        compare_system.equal("平面鏡", "主要反射", "規則反射", "答案")
        compare_system.equal("紙張與牆面", "主要反射", "漫反射", "答案")
        compare_system.equal("漫反射", "反射定律", "每一道光仍遵守反射定律", "答案")
        compare_system.notequal("漫反射", "敘述", "代表光沒有遵守反射定律", "錯誤觀念")
        compare_system.equal("從不同方向看見紙張", "原因", "紙張產生漫反射", "答案")

    @staticmethod
    def plane_mirror():
        compare_system.equal("平面鏡成像", "像的種類", "虛像", "答案")
        compare_system.equal("平面鏡像與物體", "大小關係", "等大", "答案")
        compare_system.equal("像到鏡面的距離", "關係", "等於物體到鏡面的距離", "答案")
        compare_system.equal("平面鏡像", "方向特性", "正立", "答案")
        compare_system.equal("平面鏡像與物體", "位置關係", "相對鏡面對稱", "答案")
        compare_system.equal("虛像", "特性", "不能直接投影在光屏上", "答案")
        compare_system.notequal("平面鏡中的像", "敘述", "真的位於鏡子後方", "錯誤觀念")
        compare_system.equal("人向鏡子靠近 1 公尺", "結果", "人與像的距離減少 2 公尺", "答案")

    @staticmethod
    def spherical_mirror():
        compare_system.equivalentto("凹面鏡", "鏡面", "反射面向內凹的球面鏡", "定義")
        compare_system.equivalentto("凸面鏡", "鏡面", "反射面向外凸的球面鏡", "定義")
        compare_system.equal("平行主軸光線照到凹面鏡", "結果", "反射後通過焦點", "答案")
        compare_system.equal("平行主軸光線照到凸面鏡", "結果", "反射後像是由鏡後焦點發散", "答案")
        compare_system.equal("凸面鏡成像", "一般特性", "正立、縮小、虛像", "答案")
        compare_system.equal("凸面鏡", "優點", "視野較廣", "答案")
        compare_system.equal("道路轉角鏡", "應用", "凸面鏡", "答案")
        compare_system.equal("化妝鏡或牙醫鏡", "常見應用", "凹面鏡放大成像", "答案")

    @staticmethod
    def refraction():
        compare_system.equivalentto("光的折射", "現象", "光進入不同介質時因速率改變而改變方向", "定義")
        compare_system.equal("光由空氣斜射入玻璃", "一般結果", "折射光偏向法線", "答案")
        compare_system.equal("光由玻璃斜射入空氣", "一般結果", "折射光偏離法線", "答案")
        compare_system.equal("光垂直入射介面", "結果", "方向不偏折但速率改變", "答案")
        compare_system.equal("折射時光的頻率", "關係", "保持不變", "答案")
        compare_system.equal("折射時光速", "關係", "通常改變", "答案")
        compare_system.equal("折射時波長", "關係", "通常改變", "答案")
        compare_system.equal("水中物體看起來較淺", "原因", "光的折射", "答案")
        compare_system.notequal("折射", "敘述", "是光的頻率改變造成的", "錯誤觀念")

    @staticmethod
    def refractive_index():
        compare_system.equivalentto("折射率", "物理量", "真空光速與介質中光速的比值", "定義")
        compare_system.calculatedby("折射率", "公式", "n = c ÷ v", "答案")
        compare_system.equal("折射率", "物理量種類", "無單位純量", "答案")
        compare_system.equal("介質折射率愈大", "一般關係", "光在其中速率愈小", "答案")
        compare_system.equal("真空折射率", "數值", "1", "答案")
        compare_system.calculatedby("司乃耳定律", "公式", "n₁sinθ₁ = n₂sinθ₂", "答案")
        compare_system.equal("光由低折射率進入高折射率介質", "一般結果", "偏向法線", "答案")
        compare_system.equal("光由高折射率進入低折射率介質", "一般結果", "偏離法線", "答案")

    @staticmethod
    def total_internal_reflection():
        compare_system.equivalentto("全反射", "現象", "光完全反射回原介質而沒有折射出去", "定義")
        compare_system.equal("全反射條件一", "題目", "光由高折射率介質射向低折射率介質", "答案")
        compare_system.equal("全反射條件二", "題目", "入射角大於臨界角", "答案")
        compare_system.equal("入射角等於臨界角", "結果", "折射角為 90°", "答案")
        compare_system.calculatedby("臨界角", "公式", "sinθc = n₂/n₁", "答案")
        compare_system.equal("光纖", "原理", "全反射", "答案")
        compare_system.equal("鑽石閃耀", "原因之一", "內部多次全反射", "答案")
        compare_system.notequal("光由空氣進入玻璃", "情況", "可發生全反射", "錯誤觀念")

    @staticmethod
    def lens():
        compare_system.equivalentto("凸透鏡", "透鏡", "中央厚、邊緣薄的會聚透鏡", "定義")
        compare_system.equivalentto("凹透鏡", "透鏡", "中央薄、邊緣厚的發散透鏡", "定義")
        compare_system.equal("平行主軸光線通過凸透鏡", "結果", "折射後會聚於焦點", "答案")
        compare_system.equal("平行主軸光線通過凹透鏡", "結果", "折射後像是由物側焦點發散", "答案")
        compare_system.equal("凹透鏡成像", "一般特性", "正立、縮小、虛像", "答案")
        compare_system.equal("凸透鏡", "可能成像", "實像或虛像", "答案")
        compare_system.equal("焦距", "定義", "光心到焦點的距離", "答案")
        compare_system.equal("透鏡光心附近的光線", "薄透鏡近似", "方向近似不變", "答案")

    @staticmethod
    def convex_lens_image():
        compare_system.equal("物體在凸透鏡 2f 外", "成像", "倒立、縮小、實像", "答案")
        compare_system.equal("物體在凸透鏡 2f 處", "成像", "倒立、等大、實像", "答案")
        compare_system.equal("物體在凸透鏡 f 與 2f 之間", "成像", "倒立、放大、實像", "答案")
        compare_system.equal("物體在凸透鏡焦點上", "成像", "折射光平行，遠處不形成有限實像", "答案")
        compare_system.equal("物體在凸透鏡焦點內", "成像", "正立、放大、虛像", "答案")
        compare_system.equal("放大鏡", "原理", "物體放在凸透鏡焦點內", "答案")
        compare_system.equal("照相機", "成像", "在感光元件上形成倒立實像", "答案")
        compare_system.equal("投影機", "成像", "形成放大的實像", "答案")

    @staticmethod
    def lens_formula():
        compare_system.calculatedby("薄透鏡公式", "公式", "1/f = 1/do + 1/di", "答案")
        compare_system.calculatedby("線性放大率", "公式", "m = hi/ho = -di/do", "答案")
        compare_system.equal("實像", "一般光學符號", "可由實際光線會聚形成", "答案")
        compare_system.equal("虛像", "一般光學意義", "由光線反向延長線交會形成", "答案")
        compare_system.equal("放大率絕對值大於 1", "意義", "像比物體大", "答案")
        compare_system.equal("放大率絕對值小於 1", "意義", "像比物體小", "答案")
        compare_system.equal("放大率為負", "常見符號意義", "像相對物體倒立", "答案")
        compare_system.equal("放大率為正", "常見符號意義", "像相對物體正立", "答案")

    @staticmethod
    def eye():
        compare_system.equal("眼睛的水晶體", "功能", "調整焦距使影像落在視網膜上", "答案")
        compare_system.equal("視網膜", "功能", "接收光刺激並轉換為神經訊號", "答案")
        compare_system.equal("正常眼睛看遠物", "調節", "水晶體較扁、焦距較長", "答案")
        compare_system.equal("正常眼睛看近物", "調節", "水晶體較凸、焦距較短", "答案")
        compare_system.equal("近視", "成像問題", "遠物影像形成於視網膜前", "答案")
        compare_system.equal("近視矯正", "透鏡", "凹透鏡", "答案")
        compare_system.equal("遠視", "成像問題", "近物影像傾向形成於視網膜後", "答案")
        compare_system.equal("遠視矯正", "透鏡", "凸透鏡", "答案")
        compare_system.equal("老花眼", "主要原因", "水晶體彈性降低、近距離調節能力下降", "答案")

    @staticmethod
    def color():
        compare_system.equal("可見光", "範圍", "電磁波譜中人眼可見的一小段", "答案")
        compare_system.equal("白光通過三稜鏡", "現象", "色散成不同顏色", "答案")
        compare_system.equal("色散", "主要原因", "不同波長的光折射率不同", "答案")
        compare_system.equal("可見光中紅光", "一般比較", "波長較長、頻率較低", "答案")
        compare_system.equal("可見光中紫光", "一般比較", "波長較短、頻率較高", "答案")
        compare_system.equal("光的三原色", "題目", "紅、綠、藍", "答案")
        compare_system.equal("紅光加綠光", "加色混合", "黃光", "答案")
        compare_system.equal("綠光加藍光", "加色混合", "青光", "答案")
        compare_system.equal("紅光加藍光", "加色混合", "洋紅光", "答案")
        compare_system.equal("紅、綠、藍光適當等量混合", "結果", "白光", "答案")