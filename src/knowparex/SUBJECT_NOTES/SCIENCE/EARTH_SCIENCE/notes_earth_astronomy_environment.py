# ===========================================
# notes_earth_astronomy_environment.py
# 地球科學：天文、太陽系、地月系統、氣候與環境
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class earth_astronomy_environment:

    @staticmethod
    def universe_scale():
        compare_system.equal("天文單位 AU", "定義", "地球與太陽平均距離", "答案")
        compare_system.approximatelyequal("1 AU", "距離", "1.496 × 10⁸ km", "答案")
        compare_system.equivalentto("光年", "距離單位", "光在真空中一年行進的距離", "定義")
        compare_system.notequal("光年", "概念", "時間單位", "錯誤觀念")
        compare_system.equal("太陽系", "所屬", "銀河系", "答案")
        compare_system.equal("銀河系", "類型", "棒旋星系", "答案")
        compare_system.equal("銀河系", "宇宙中", "只是眾多星系之一", "答案")

    @staticmethod
    def big_bang():
        compare_system.equivalentto("大霹靂理論", "宇宙學理論", "宇宙由早期高溫高密度狀態膨脹演化至今", "定義")
        compare_system.equal("星系紅移", "證據", "宇宙正在膨脹", "答案")
        compare_system.equal("宇宙微波背景輻射", "證據", "早期宇宙殘留輻射", "答案")
        compare_system.equal("輕元素比例", "證據", "符合早期宇宙核合成預測", "答案")
        compare_system.equal("宇宙膨脹", "意義", "星系間平均尺度增加", "答案")
        compare_system.notequal("大霹靂", "敘述", "是在既有空間某一點發生普通爆炸", "錯誤觀念")
        compare_system.notequal("宇宙膨脹", "敘述", "代表所有物體自身都以相同比例膨脹", "錯誤觀念")

    @staticmethod
    def star():
        compare_system.equivalentto("恆星", "天體", "以核心核融合產生能量並自行發光的天體", "定義")
        compare_system.equal("恆星主要成分", "題目", "氫與氦", "答案")
        compare_system.equal("主序星主要能源", "題目", "氫核融合成氦", "答案")
        compare_system.equal("恆星顏色", "關係", "與表面溫度相關", "答案")
        compare_system.equal("藍色恆星", "一般溫度", "比紅色恆星高", "答案")
        compare_system.equal("太陽", "分類", "主序星", "答案")
        compare_system.notequal("所有亮點天體", "敘述", "都是恆星", "錯誤觀念")

    @staticmethod
    def stellar_evolution():
        compare_system.equal("恆星形成", "場所", "分子雲或星雲", "答案")
        compare_system.equal("原恆星", "演化", "重力收縮使核心溫度升高", "答案")
        compare_system.equal("主序星", "能量", "核心氫融合", "答案")
        compare_system.equal("類太陽恆星末期", "可能階段", "紅巨星、行星狀星雲、白矮星", "答案")
        compare_system.equal("大質量恆星末期", "可能階段", "超紅巨星與超新星", "答案")
        compare_system.equal("超新星後", "可能殘骸", "中子星或黑洞", "答案")
        compare_system.equal("恆星壽命", "質量增加", "通常變短", "答案")
        compare_system.notequal("質量最大恆星", "敘述", "燃料最多所以壽命一定最長", "錯誤觀念")

    @staticmethod
    def hertzsprung_russell():
        compare_system.equivalentto("赫羅圖", "天文圖表", "以恆星光度與表面溫度分類恆星的圖", "定義")
        compare_system.equal("赫羅圖橫軸", "常見", "表面溫度或光譜型", "答案")
        compare_system.equal("赫羅圖縱軸", "常見", "光度或絕對星等", "答案")
        compare_system.equal("主序帶", "分布", "由高溫高光度延伸至低溫低光度", "答案")
        compare_system.equal("白矮星", "特徵", "高溫但低光度", "答案")
        compare_system.equal("紅巨星", "特徵", "低溫但高光度", "答案")
        compare_system.notequal("恆星表面溫度", "敘述", "在赫羅圖一定由左至右升高", "錯誤觀念")

    @staticmethod
    def solar_system():
        compare_system.equal("太陽系中心天體", "題目", "太陽", "答案")
        compare_system.equal("八大行星順序", "由內至外", "水星、金星、地球、火星、木星、土星、天王星、海王星", "答案")
        compare_system.equal("類地行星", "成員", "水星、金星、地球、火星", "答案")
        compare_system.equal("類木行星", "成員", "木星、土星、天王星、海王星", "答案")
        compare_system.equal("小行星帶", "主要位置", "火星與木星軌道之間", "答案")
        compare_system.equal("柯伊伯帶", "位置", "海王星軌道外", "答案")
        compare_system.notequal("冥王星", "現行分類", "八大行星之一", "錯誤觀念")

    @staticmethod
    def terrestrial_jovian():
        compare_system.equal("類地行星", "表面", "具有固體表面", "答案")
        compare_system.equal("類地行星", "平均密度", "較高", "答案")
        compare_system.equal("類木行星", "體積", "通常較大", "答案")
        compare_system.equal("類木行星", "主要成分", "氣體與冰類物質", "答案")
        compare_system.equal("類木行星", "衛星與環", "通常較多", "答案")
        compare_system.equal("木星", "太陽系", "最大行星", "答案")
        compare_system.equal("土星", "特徵", "具有顯著行星環", "答案")
        compare_system.notequal("類木行星", "敘述", "具有像地球一樣可站立的清楚固體表面", "錯誤觀念")

    @staticmethod
    def earth_rotation():
        compare_system.equivalentto("地球自轉", "地球運動", "地球繞自轉軸旋轉的運動", "定義")
        compare_system.equal("地球自轉方向", "由北極上空看", "逆時針", "答案")
        compare_system.equal("地球自轉方向", "一般描述", "由西向東", "答案")
        compare_system.equal("地球自轉週期", "恆星日", "約 23 小時 56 分", "答案")
        compare_system.equal("太陽日", "長度", "約 24 小時", "答案")
        compare_system.equal("晝夜交替", "主要原因", "地球自轉", "答案")
        compare_system.equal("天體東升西落", "表觀原因", "地球由西向東自轉", "答案")
        compare_system.notequal("四季變化", "敘述", "主要由地球每天自轉造成", "錯誤觀念")

    @staticmethod
    def earth_revolution_seasons():
        compare_system.equivalentto("地球公轉", "地球運動", "地球繞太陽運行的運動", "定義")
        compare_system.approximatelyequal("地球公轉週期", "時間", "365.25 日", "答案")
        compare_system.equal("地軸傾角", "近似值", "23.5°", "答案")
        compare_system.equal("四季形成主要原因", "題目", "地軸傾斜與地球公轉", "答案")
        compare_system.equal("北半球夏季", "太陽直射", "較偏北且白晝較長", "答案")
        compare_system.equal("北半球冬季", "太陽直射", "較偏南且白晝較短", "答案")
        compare_system.notequal("四季形成", "敘述", "主要因地球夏天離太陽較近", "錯誤觀念")

    @staticmethod
    def solstice_equinox():
        compare_system.equal("春分與秋分", "全球晝夜", "接近等長", "答案")
        compare_system.equal("春分太陽直射", "緯度", "赤道", "答案")
        compare_system.equal("秋分太陽直射", "緯度", "赤道", "答案")
        compare_system.equal("北半球夏至太陽直射", "緯度", "北回歸線", "答案")
        compare_system.equal("北半球冬至太陽直射", "緯度", "南回歸線", "答案")
        compare_system.equal("北半球夏至", "白晝", "全年最長附近", "答案")
        compare_system.equal("北半球冬至", "白晝", "全年最短附近", "答案")

    @staticmethod
    def moon_orbit():
        compare_system.equal("月球", "地球", "天然衛星", "答案")
        compare_system.equal("月球公轉方向", "一般描述", "由西向東", "答案")
        compare_system.approximatelyequal("月球恆星月", "週期", "27.3 日", "答案")
        compare_system.approximatelyequal("月相週期朔望月", "週期", "29.5 日", "答案")
        compare_system.equal("月球自轉週期", "關係", "約等於其公轉週期", "答案")
        compare_system.equal("月球總以近似同一面朝向地球", "原因", "同步自轉", "答案")
        compare_system.notequal("月球背面", "敘述", "永遠完全沒有陽光照射", "錯誤觀念")

    @staticmethod
    def moon_phase():
        compare_system.equivalentto("月相", "天文現象", "由地球看見月球受光部分形狀隨位置改變", "定義")
        compare_system.equal("朔", "月相", "新月", "答案")
        compare_system.equal("上弦月", "時間", "朔後約 7 至 8 日", "答案")
        compare_system.equal("望", "月相", "滿月", "答案")
        compare_system.equal("下弦月", "時間", "望後約 7 至 8 日", "答案")
        compare_system.equal("月相形成", "原因", "月球繞地球公轉造成觀察角度改變", "答案")
        compare_system.notequal("月相", "敘述", "由地球影子每天遮住月球形成", "錯誤觀念")

    @staticmethod
    def solar_eclipse():
        compare_system.equivalentto("日食", "天文現象", "月球位於太陽與地球之間並遮住太陽", "定義")
        compare_system.equal("日食可能月相", "題目", "朔", "答案")
        compare_system.equal("日全食", "觀察位置", "月球本影區", "答案")
        compare_system.equal("日偏食", "觀察位置", "月球半影區", "答案")
        compare_system.equal("日環食", "原因之一", "月球視直徑小於太陽視直徑", "答案")
        compare_system.equal("日食不是每月發生", "原因", "月球軌道面與黃道面有傾角", "答案")
        compare_system.notequal("日食", "敘述", "地球位於太陽與月球之間", "錯誤觀念")

    @staticmethod
    def lunar_eclipse():
        compare_system.equivalentto("月食", "天文現象", "月球進入地球影子", "定義")
        compare_system.equal("月食可能月相", "題目", "望", "答案")
        compare_system.equal("月全食", "位置", "月球完全進入地球本影", "答案")
        compare_system.equal("月偏食", "位置", "月球部分進入地球本影", "答案")
        compare_system.equal("月全食月面偏紅", "原因", "地球大氣散射與折射紅光進入本影", "答案")
        compare_system.equal("月食可見範圍", "一般比較", "通常大於日全食可見範圍", "答案")
        compare_system.notequal("月食", "敘述", "月球位於太陽與地球之間", "錯誤觀念")

    @staticmethod
    def sun():
        compare_system.equal("太陽", "分類", "恆星", "答案")
        compare_system.equal("太陽主要成分", "題目", "氫與氦", "答案")
        compare_system.equal("太陽核心", "能量來源", "核融合", "答案")
        compare_system.equal("光球層", "特徵", "主要可見表面", "答案")
        compare_system.equal("太陽黑子", "溫度", "比周圍光球低", "答案")
        compare_system.equal("日冕", "位置", "太陽外層稀薄大氣", "答案")
        compare_system.equal("太陽風", "組成", "高速帶電粒子", "答案")
        compare_system.notequal("太陽", "敘述", "靠普通燃燒煤炭產生能量", "錯誤觀念")

    @staticmethod
    def electromagnetic_spectrum():
        compare_system.equal("電磁波由低頻至高頻", "順序", "無線電波、微波、紅外線、可見光、紫外線、X 射線、伽瑪射線", "答案")
        compare_system.equal("電磁波頻率增加", "波長", "減小", "答案")
        compare_system.equal("電磁波頻率增加", "單一光子能量", "增加", "答案")
        compare_system.equal("可見光", "範圍", "電磁波譜的一小部分", "答案")
        compare_system.equal("紅外線", "應用", "熱感測與遙控器", "答案")
        compare_system.equal("X 射線", "應用", "醫學影像", "答案")
        compare_system.equal("紫外線", "影響", "可造成皮膚與 DNA 損傷", "答案")
        compare_system.notequal("電磁波", "敘述", "必須透過空氣或其他介質才能傳播", "錯誤觀念")

    @staticmethod
    def greenhouse_effect():
        compare_system.equivalentto("溫室效應", "大氣現象", "大氣吸收並再放射地表紅外線使地表較溫暖", "定義")
        compare_system.equal("自然溫室效應", "作用", "使地球維持適合生命的溫度", "答案")
        compare_system.equal("主要溫室氣體", "例子", "水氣、CO₂、CH₄ 與 N₂O", "答案")
        compare_system.equal("人為增強溫室效應", "主要來源之一", "燃燒化石燃料增加 CO₂", "答案")
        compare_system.equal("甲烷", "來源例子", "畜牧、濕地與化石燃料系統", "答案")
        compare_system.notequal("溫室效應", "概念", "臭氧層破洞", "錯誤觀念")
        compare_system.notequal("溫室氣體", "敘述", "阻止所有熱量離開地球", "錯誤觀念")

    @staticmethod
    def climate_change():
        compare_system.equivalentto("氣候變遷", "氣候現象", "氣候平均狀態或變異特徵的長期改變", "定義")
        compare_system.equal("現代全球暖化", "主要驅動", "人為溫室氣體增加", "答案")
        compare_system.equal("全球平均海平面上升", "原因", "海水熱膨脹與陸冰融化", "答案")
        compare_system.equal("冰川退縮", "影響", "改變水資源與海平面", "答案")
        compare_system.equal("極端高溫", "氣候變遷", "發生機率與強度可能增加", "答案")
        compare_system.equal("海洋吸收 CO₂", "結果", "造成海洋酸化", "答案")
        compare_system.notequal("某地單次寒流", "敘述", "可推翻長期全球暖化趨勢", "錯誤觀念")

    @staticmethod
    def sea_level():
        compare_system.equal("海水受熱", "體積", "膨脹", "答案")
        compare_system.equal("陸地冰川與冰蓋融化", "結果", "增加海洋水量", "答案")
        compare_system.equal("漂浮海冰融化", "直接海平面影響", "相對較小", "答案")
        compare_system.equal("海平面上升", "風險", "沿海淹水、侵蝕與鹽水入侵", "答案")
        compare_system.equal("區域海平面", "影響因素", "地層升降、洋流與重力變化", "答案")
        compare_system.notequal("全球海平面上升", "敘述", "每個海岸上升幅度必定完全相同", "錯誤觀念")

    @staticmethod
    def natural_hazard():
        compare_system.equivalentto("天然災害", "災害", "自然現象對人類社會與環境造成重大損失的事件", "定義")
        compare_system.equal("地震災害", "例子", "建物倒塌、液化、山崩與海嘯", "答案")
        compare_system.equal("颱風災害", "例子", "強風、豪雨、洪水與土石流", "答案")
        compare_system.equal("火山災害", "例子", "熔岩、火山灰、火山碎屑流與氣體", "答案")
        compare_system.equal("災害風險", "組成概念", "危害、暴露度與脆弱度", "答案")
        compare_system.equal("防災", "目的", "降低傷亡與損失而非阻止所有自然現象", "答案")
        compare_system.notequal("天然現象", "敘述", "不論是否影響人類都一定稱為災害", "錯誤觀念")

    @staticmethod
    def renewable_energy():
        compare_system.equivalentto("再生能源", "能源", "可在人類時間尺度內自然補充的能源", "定義")
        compare_system.equal("太陽能", "分類", "再生能源", "答案")
        compare_system.equal("風力", "分類", "再生能源", "答案")
        compare_system.equal("水力", "分類", "再生能源", "答案")
        compare_system.equal("地熱", "分類", "再生能源", "答案")
        compare_system.equal("化石燃料", "分類", "非再生能源", "答案")
        compare_system.equal("再生能源", "限制", "可能受天氣、地點、儲能與土地使用影響", "答案")
        compare_system.notequal("再生能源", "敘述", "完全沒有任何環境影響", "錯誤觀念")

    @staticmethod
    def sustainability():
        compare_system.equivalentto("永續發展", "發展概念", "滿足當代需求且不損害後代滿足需求的能力", "定義")
        compare_system.equal("永續發展面向", "題目", "環境、社會與經濟", "答案")
        compare_system.equal("節能", "作用", "降低能源消耗與排放", "答案")
        compare_system.equal("循環經濟", "目標", "減少廢棄並延長材料使用週期", "答案")
        compare_system.equal("減量、再使用、回收", "概念", "資源管理原則", "答案")
        compare_system.equal("生態足跡", "用途", "估算人類活動對生物生產性土地與水域的需求", "答案")
        compare_system.notequal("永續發展", "敘述", "只關心環境而完全不考慮人類生活", "錯誤觀念")