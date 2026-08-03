# ===========================================
# notes_earth_atmosphere_ocean.py
# 地球科學：大氣、天氣、氣候、水循環與海洋
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class earth_atmosphere_ocean:

    @staticmethod
    def atmosphere_composition():
        compare_system.equal("乾燥空氣中最多氣體", "題目", "氮氣", "答案")
        compare_system.approximatelyequal("氮氣體積比例", "乾燥空氣", "78%", "答案")
        compare_system.approximatelyequal("氧氣體積比例", "乾燥空氣", "21%", "答案")
        compare_system.equal("氬氣", "大氣比例", "約 0.93%", "答案")
        compare_system.equal("二氧化碳", "大氣比例", "少量但具重要氣候與生物作用", "答案")
        compare_system.equal("水氣含量", "特性", "隨時間與地點明顯改變", "答案")
        compare_system.notequal("大氣", "敘述", "只由氧氣組成", "錯誤觀念")

    @staticmethod
    def atmosphere_layers():
        compare_system.equal("大氣層由低至高", "主要分層", "對流層、平流層、中氣層、增溫層", "答案")
        compare_system.equal("對流層", "主要現象", "大多數天氣現象", "答案")
        compare_system.equal("平流層", "重要構造", "臭氧層", "答案")
        compare_system.equal("中氣層", "現象之一", "多數流星在此燒蝕", "答案")
        compare_system.equal("增溫層", "溫度", "隨高度增加而升高", "答案")
        compare_system.equal("對流層溫度", "一般趨勢", "隨高度升高而降低", "答案")
        compare_system.notequal("大氣分層", "敘述", "各層邊界像固體牆面完全分隔", "錯誤觀念")

    @staticmethod
    def ozone_layer():
        compare_system.equal("臭氧層主要位置", "題目", "平流層", "答案")
        compare_system.equal("臭氧層", "功能", "吸收大部分有害紫外線", "答案")
        compare_system.equal("臭氧分子", "化學式", "O₃", "答案")
        compare_system.equal("氯氟碳化物", "影響", "可促進平流層臭氧分解", "答案")
        compare_system.equal("臭氧洞", "主要區域", "南極春季特別明顯", "答案")
        compare_system.notequal("臭氧層破洞", "敘述", "代表大氣中出現真正完全沒有氣體的洞", "錯誤觀念")
        compare_system.notequal("地表臭氧", "敘述", "對人體一定有益", "錯誤觀念")

    @staticmethod
    def air_pressure():
        compare_system.equivalentto("氣壓", "物理量", "大氣對單位面積施加的力", "定義")
        compare_system.equal("高度增加", "一般結果", "氣壓降低", "答案")
        compare_system.equal("暖空氣", "相同條件", "密度通常較低", "答案")
        compare_system.equal("冷空氣", "相同條件", "密度通常較高", "答案")
        compare_system.equal("等壓線", "定義", "連接相同氣壓地點的線", "答案")
        compare_system.equal("等壓線密集", "意義", "氣壓梯度較大、風通常較強", "答案")
        compare_system.notequal("高氣壓", "敘述", "代表該處溫度一定最高", "錯誤觀念")

    @staticmethod
    def wind():
        compare_system.equivalentto("風", "大氣運動", "空氣相對地表的水平運動", "定義")
        compare_system.equal("風形成主要原因", "題目", "氣壓差", "答案")
        compare_system.equal("氣壓梯度力", "方向", "由高壓指向低壓", "答案")
        compare_system.equal("科氏力", "北半球", "使運動物體向右偏", "答案")
        compare_system.equal("科氏力", "南半球", "使運動物體向左偏", "答案")
        compare_system.equal("近地面摩擦", "影響", "降低風速並改變風向", "答案")
        compare_system.notequal("風", "敘述", "會完全沿高壓直線吹向低壓而不受其他力量影響", "錯誤觀念")

    @staticmethod
    def high_low_pressure():
        compare_system.equal("北半球高氣壓近地面風", "旋轉", "順時針向外", "答案")
        compare_system.equal("北半球低氣壓近地面風", "旋轉", "逆時針向內", "答案")
        compare_system.equal("高氣壓中心", "垂直氣流", "下沉", "答案")
        compare_system.equal("低氣壓中心", "垂直氣流", "上升", "答案")
        compare_system.equal("高氣壓", "一般天氣", "較晴朗穩定", "答案")
        compare_system.equal("低氣壓", "一般天氣", "較易形成雲雨", "答案")
        compare_system.notequal("低氣壓", "敘述", "一定每天都有颱風", "錯誤觀念")

    @staticmethod
    def humidity():
        compare_system.equivalentto("絕對濕度", "濕度", "單位體積空氣中水氣的實際質量", "定義")
        compare_system.equivalentto("相對濕度", "濕度", "實際水氣量相對於同溫飽和水氣量的比例", "定義")
        compare_system.equal("溫度降低且水氣量不變", "相對濕度", "增加", "答案")
        compare_system.equal("溫度升高且水氣量不變", "相對濕度", "降低", "答案")
        compare_system.equal("相對濕度達 100%", "狀態", "空氣達飽和", "答案")
        compare_system.equal("露點", "定義", "空氣冷卻至飽和時的溫度", "答案")
        compare_system.notequal("相對濕度 100%", "敘述", "代表空氣全部由水構成", "錯誤觀念")

    @staticmethod
    def cloud():
        compare_system.equivalentto("雲", "大氣現象", "空氣中懸浮微小水滴或冰晶的集合", "定義")
        compare_system.equal("雲形成", "基本條件", "空氣冷卻達飽和並有凝結核", "答案")
        compare_system.equal("空氣上升", "一般結果", "膨脹冷卻", "答案")
        compare_system.equal("積雲", "外觀", "塊狀且垂直發展", "答案")
        compare_system.equal("層雲", "外觀", "廣泛層狀", "答案")
        compare_system.equal("卷雲", "高度與成分", "高空冰晶雲", "答案")
        compare_system.equal("積雨雲", "天氣", "常伴隨雷雨與強對流", "答案")
        compare_system.notequal("雲", "敘述", "主要由水蒸氣本身形成可見白色", "錯誤觀念")

    @staticmethod
    def precipitation():
        compare_system.equivalentto("降水", "天氣現象", "水滴或冰晶由雲中落至地面的現象", "定義")
        compare_system.equal("雨", "形成", "液態水滴落下", "答案")
        compare_system.equal("雪", "形成", "冰晶在低溫條件下落至地面", "答案")
        compare_system.equal("冰雹", "形成", "強對流雲中冰粒反覆上升增長", "答案")
        compare_system.equal("地形雨", "原因", "濕空氣受山脈抬升冷卻", "答案")
        compare_system.equal("對流雨", "原因", "地表加熱使暖濕空氣強烈上升", "答案")
        compare_system.equal("鋒面雨", "原因", "冷暖氣團交會抬升", "答案")
        compare_system.notequal("所有雲", "敘述", "都一定會產生地面降水", "錯誤觀念")

    @staticmethod
    def air_mass_front():
        compare_system.equivalentto("氣團", "大氣", "溫度與濕度性質較均一的大範圍空氣", "定義")
        compare_system.equivalentto("鋒面", "天氣系統", "兩個性質不同氣團的交界", "定義")
        compare_system.equal("冷鋒", "特徵", "冷空氣推進並迫使暖空氣快速抬升", "答案")
        compare_system.equal("暖鋒", "特徵", "暖空氣沿冷空氣上方緩慢爬升", "答案")
        compare_system.equal("滯留鋒", "特徵", "鋒面移動緩慢並可能帶來持續降雨", "答案")
        compare_system.equal("囚錮鋒", "形成", "冷鋒追上暖鋒", "答案")
        compare_system.notequal("鋒面", "敘述", "是兩團空氣間固定不動的實體牆", "錯誤觀念")

    @staticmethod
    def cold_warm_front():
        compare_system.equal("冷鋒坡度", "比較", "較陡", "答案")
        compare_system.equal("冷鋒降雨", "常見", "較短暫但可能強烈", "答案")
        compare_system.equal("冷鋒通過後", "氣溫", "通常下降", "答案")
        compare_system.equal("暖鋒坡度", "比較", "較緩", "答案")
        compare_system.equal("暖鋒降雨", "常見", "範圍較廣且較持續", "答案")
        compare_system.equal("暖鋒通過後", "氣溫", "通常上升", "答案")
        compare_system.notequal("暖鋒", "敘述", "一定完全沒有降雨", "錯誤觀念")

    @staticmethod
    def typhoon():
        compare_system.equivalentto("颱風", "熱帶氣旋", "形成於西北太平洋的強烈暖心低壓系統", "定義")
        compare_system.equal("颱風能量來源", "主要", "暖海水蒸發與水氣凝結潛熱", "答案")
        compare_system.equal("颱風形成海溫", "一般條件", "海面溫度較高", "答案")
        compare_system.equal("颱風眼", "天氣", "風較弱且可能短暫少雲", "答案")
        compare_system.equal("眼牆", "天氣", "風雨通常最強", "答案")
        compare_system.equal("北半球颱風環流", "方向", "逆時針", "答案")
        compare_system.equal("颱風登陸後", "一般結果", "失去水氣與熱量來源而減弱", "答案")
        compare_system.notequal("颱風眼經過", "敘述", "代表颱風已完全離開", "錯誤觀念")

    @staticmethod
    def monsoon():
        compare_system.equivalentto("季風", "風系", "因大陸與海洋季節性受熱差異造成風向明顯轉換", "定義")
        compare_system.equal("東亞夏季風", "一般方向", "由海洋吹向大陸", "答案")
        compare_system.equal("東亞冬季風", "一般方向", "由大陸吹向海洋", "答案")
        compare_system.equal("夏季大陸", "氣壓", "相對低壓", "答案")
        compare_system.equal("冬季大陸", "氣壓", "相對高壓", "答案")
        compare_system.equal("台灣冬季東北季風", "影響", "北部與東北部較常迎風降雨", "答案")
        compare_system.notequal("季風", "敘述", "每天固定早晚反向的局部風", "錯誤觀念")

    @staticmethod
    def land_sea_breeze():
        compare_system.equal("海風", "時間", "白天較常出現", "答案")
        compare_system.equal("海風方向", "題目", "由海洋吹向陸地", "答案")
        compare_system.equal("陸風", "時間", "夜晚較常出現", "答案")
        compare_system.equal("陸風方向", "題目", "由陸地吹向海洋", "答案")
        compare_system.equal("白天陸地", "受熱", "比海洋快", "答案")
        compare_system.equal("夜晚陸地", "冷卻", "比海洋快", "答案")
        compare_system.notequal("海陸風", "敘述", "尺度與季風完全相同", "錯誤觀念")

    @staticmethod
    def weather_climate():
        compare_system.equivalentto("天氣", "大氣狀態", "某地短時間的大氣狀況", "定義")
        compare_system.equivalentto("氣候", "大氣統計", "一地長期天氣的平均與變異特徵", "定義")
        compare_system.equal("今天下雨", "分類", "天氣", "答案")
        compare_system.equal("台灣夏季炎熱潮濕", "分類", "氣候特徵", "答案")
        compare_system.equal("氣候分析", "時間尺度", "通常需數十年資料", "答案")
        compare_system.notequal("某一天寒冷", "敘述", "即可證明全球氣候沒有暖化", "錯誤觀念")

    @staticmethod
    def climate_factors():
        compare_system.equal("緯度", "氣候影響", "影響太陽入射角與能量", "答案")
        compare_system.equal("海拔升高", "一般結果", "氣溫降低", "答案")
        compare_system.equal("距海遠近", "影響", "影響溫差與濕度", "答案")
        compare_system.equal("洋流", "影響", "改變沿岸溫度與水氣", "答案")
        compare_system.equal("地形", "影響", "形成迎風雨與背風乾燥", "答案")
        compare_system.equal("盛行風", "影響", "輸送熱量與水氣", "答案")
        compare_system.notequal("同緯度地區", "敘述", "氣候一定完全相同", "錯誤觀念")

    @staticmethod
    def water_cycle():
        compare_system.equivalentto("水循環", "地球系統", "水在海洋、陸地、大氣與生物間移動的過程", "定義")
        compare_system.equal("蒸發", "水循環", "液態水變為水氣", "答案")
        compare_system.equal("凝結", "水循環", "水氣形成液滴或冰晶", "答案")
        compare_system.equal("降水", "水循環", "水由大氣回到地表", "答案")
        compare_system.equal("入滲", "水循環", "水進入土壤與地下", "答案")
        compare_system.equal("逕流", "水循環", "水沿地表流向河川海洋", "答案")
        compare_system.equal("蒸散", "水循環", "植物將水氣釋放至大氣", "答案")
        compare_system.notequal("水循環", "敘述", "會製造出全新的水分子總量", "錯誤觀念")

    @staticmethod
    def groundwater():
        compare_system.equivalentto("地下水", "水資源", "儲存在地下岩層與孔隙中的水", "定義")
        compare_system.equivalentto("含水層", "地質構造", "可儲存並傳輸地下水的岩層", "定義")
        compare_system.equal("地下水面", "定義", "飽和帶上界", "答案")
        compare_system.equal("抽取地下水過量", "可能結果", "地層下陷與海水入侵", "答案")
        compare_system.equal("地表污染物", "影響", "可能入滲污染地下水", "答案")
        compare_system.equal("地下水補注", "來源", "降水入滲", "答案")
        compare_system.notequal("地下水", "敘述", "是地下巨大的完全空洞河流", "錯誤觀念")

    @staticmethod
    def ocean_salinity():
        compare_system.equivalentto("鹽度", "海水性質", "海水中溶解鹽類的含量", "定義")
        compare_system.approximatelyequal("全球海水平均鹽度", "數值", "約 35‰", "答案")
        compare_system.equal("蒸發增加", "其他條件相同", "鹽度增加", "答案")
        compare_system.equal("降水增加", "其他條件相同", "鹽度降低", "答案")
        compare_system.equal("河水大量注入", "一般結果", "近岸鹽度降低", "答案")
        compare_system.equal("海冰形成", "附近海水", "鹽度可能增加", "答案")
        compare_system.notequal("所有海域", "敘述", "鹽度完全相同", "錯誤觀念")

    @staticmethod
    def ocean_current():
        compare_system.equivalentto("洋流", "海洋運動", "海水長距離且有方向性的流動", "定義")
        compare_system.equal("表層洋流", "主要驅動", "盛行風", "答案")
        compare_system.equal("深層環流", "主要驅動", "海水密度差", "答案")
        compare_system.equal("海水密度", "影響因素", "溫度與鹽度", "答案")
        compare_system.equal("暖流", "沿岸影響", "通常增溫並增加水氣", "答案")
        compare_system.equal("寒流", "沿岸影響", "通常降溫並可能使氣候較乾", "答案")
        compare_system.equal("洋流", "作用", "重新分配全球熱量", "答案")
        compare_system.notequal("洋流", "敘述", "只由潮汐作用產生", "錯誤觀念")

    @staticmethod
    def wave_tide():
        compare_system.equivalentto("海浪", "海洋現象", "主要由風將能量傳給海面形成的波動", "定義")
        compare_system.equivalentto("潮汐", "海洋現象", "海面受月球與太陽引力而週期升降", "定義")
        compare_system.equal("潮汐主要影響天體", "題目", "月球", "答案")
        compare_system.equal("朔與望附近", "潮差", "大潮", "答案")
        compare_system.equal("上弦與下弦附近", "潮差", "小潮", "答案")
        compare_system.equal("海嘯", "主要成因之一", "海底地震造成大量海水位移", "答案")
        compare_system.notequal("海嘯", "敘述", "只是風特別強造成的大型普通海浪", "錯誤觀念")

    @staticmethod
    def el_nino_la_nina():
        compare_system.equivalentto("聖嬰現象", "海氣現象", "赤道中東太平洋海溫異常偏暖並改變環流", "定義")
        compare_system.equivalentto("反聖嬰現象", "海氣現象", "赤道中東太平洋海溫異常偏冷", "定義")
        compare_system.equal("聖嬰期間", "東太平洋", "海溫偏高", "答案")
        compare_system.equal("聖嬰期間", "信風", "通常減弱", "答案")
        compare_system.equal("反聖嬰期間", "信風", "通常增強", "答案")
        compare_system.equal("聖嬰與反聖嬰", "影響", "可改變全球降雨、溫度與風暴分布", "答案")
        compare_system.notequal("聖嬰現象", "敘述", "代表全球每一地區都一定變暖", "錯誤觀念")