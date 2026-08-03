from knowparex.PROGRAMMING_NOTES import compare_system
class social_geography:
    @staticmethod
    def geographic_inquiry():
        compare_system.definition('地理學', '社會科學', '研究人地關係、空間分布與區域差異的學科', '中文解釋')
        compare_system.requires('地理探究', '學習方法', '觀察、資料蒐集、地圖判讀與解釋', '能力')

    @staticmethod
    def map_basics():
        compare_system.definition('地圖', '地理工具', '以符號與比例縮小呈現地表空間資訊', '中文解釋')
        compare_system.partof('圖名、比例尺、方向標與圖例', '地圖要素', '地圖', '關係')

    @staticmethod
    def latitude_longitude_time():
        compare_system.definition('緯度', '地理座標', '以赤道為基準表示南北位置', '中文解釋')
        compare_system.definition('經度', '地理座標', '以本初子午線為基準表示東西位置', '中文解釋')
        compare_system.causes('地球自轉', '原因', '不同經度地方時間不同', '結果')

    @staticmethod
    def gis_remote_sensing():
        compare_system.definition('地理資訊系統', '地理工具', '整合、分析與呈現具有空間位置的資料', '中文解釋')
        compare_system.definition('遙測', '地理工具', '利用衛星或航空影像取得地表資訊', '中文解釋')

    @staticmethod
    def plate_tectonics():
        compare_system.definition('板塊構造', '自然地理', '岩石圈板塊移動造成地震、火山與山脈等現象', '中文解釋')
        compare_system.resultsin('板塊聚合', '地形作用', '褶皺山脈、海溝或火山弧', '結果')

    @staticmethod
    def landform_processes():
        compare_system.definition('風化', '地形作用', '岩石在原地破碎或化學改變', '中文解釋')
        compare_system.definition('侵蝕', '地形作用', '流水、風、冰或海浪移除地表物質', '中文解釋')
        compare_system.definition('堆積', '地形作用', '搬運能力降低後物質沉積', '中文解釋')

    @staticmethod
    def river_coast_karst():
        compare_system.related('沖積平原與三角洲', '河流地形', '河流堆積形成', '關係')
        compare_system.related('海蝕崖與沙洲', '海岸地形', '海浪侵蝕或沿岸堆積形成', '關係')
        compare_system.definition('喀斯特地形', '地形', '石灰岩受水溶蝕形成的特殊地形', '中文解釋')

    @staticmethod
    def climate_elements_factors():
        compare_system.partof('氣溫、降水、風與氣壓', '氣候要素', '氣候', '關係')
        compare_system.related('緯度、海拔、距海遠近、洋流與地形', '氣候因素', '造成各地氣候差異', '功能')

    @staticmethod
    def monsoon_typhoon():
        compare_system.definition('季風', '氣候現象', '因海陸熱力差異造成風向隨季節顯著改變', '中文解釋')
        compare_system.definition('颱風', '天氣系統', '形成於暖海面的強烈熱帶氣旋', '中文解釋')

    @staticmethod
    def water_ocean():
        compare_system.definition('水循環', '自然地理', '水在海洋、大氣、陸地與生物間循環移動', '中文解釋')
        compare_system.definition('洋流', '海洋地理', '海水長距離有規律流動', '中文解釋')

    @staticmethod
    def population():
        compare_system.definition('人口分布', '人文地理', '人口在空間上的集中與稀疏情形', '中文解釋')
        compare_system.definition('人口轉型', '人口地理', '社會由高出生高死亡逐步轉為低出生低死亡的過程', '中文解釋')
        compare_system.definition('人口遷移', '人口地理', '人口跨越一定空間並改變居住地的移動', '中文解釋')

    @staticmethod
    def urbanization_settlement():
        compare_system.definition('都市化', '人文地理', '都市人口比例與都市生活方式增加的過程', '中文解釋')
        compare_system.definition('聚落', '人文地理', '人群集中居住與活動的空間', '中文解釋')

    @staticmethod
    def industries():
        compare_system.definition('第一級產業', '產業地理', '直接利用自然資源的農林漁牧活動', '中文解釋')
        compare_system.definition('第二級產業', '產業地理', '製造、加工與營造等活動', '中文解釋')
        compare_system.definition('第三級產業', '產業地理', '提供商業、運輸、金融與教育等服務', '中文解釋')

    @staticmethod
    def globalization_trade():
        compare_system.definition('全球化', '經濟地理', '跨國商品、資本、資訊與人員流動增加', '中文解釋')
        compare_system.related('全球生產鏈', '經濟地理', '產品不同環節分布於多個國家', '中文解釋')

    @staticmethod
    def taiwan_geography():
        compare_system.definition('臺灣地理位置', '區域地理', '位於東亞島弧、亞洲大陸與太平洋交界', '中文解釋')
        compare_system.related('中央山脈與西部平原', '臺灣地形', '影響人口、交通與產業分布', '關係')
        compare_system.related('季風、颱風與地形', '臺灣氣候', '影響降水與災害', '關係')

    @staticmethod
    def east_southeast_south_asia():
        compare_system.definition('東亞', '區域地理', '人口稠密、都市化與製造業發達的區域', '中文解釋')
        compare_system.definition('東南亞', '區域地理', '位於印度洋與太平洋交通要衝的區域', '中文解釋')
        compare_system.definition('南亞', '區域地理', '以印度次大陸為核心並深受季風影響的區域', '中文解釋')

    @staticmethod
    def west_asia_africa():
        compare_system.definition('西亞與北非', '區域地理', '乾燥氣候、能源資源與宗教文化多元的區域', '中文解釋')
        compare_system.definition('非洲', '區域地理', '自然環境與文化高度多樣的洲', '中文解釋')

    @staticmethod
    def europe_americas_oceania():
        compare_system.definition('歐洲', '區域地理', '都市化程度高、區域整合與產業多元的地區', '中文解釋')
        compare_system.definition('北美洲', '區域地理', '高度都市化並具有大型農業與服務經濟的區域', '中文解釋')
        compare_system.definition('拉丁美洲', '區域地理', '受殖民歷史與多元族群文化影響的區域', '中文解釋')
        compare_system.definition('大洋洲', '區域地理', '包括澳洲、紐西蘭與太平洋島嶼的區域', '中文解釋')

    @staticmethod
    def hazards_climate_sustainability():
        compare_system.definition('天然災害', '環境議題', '自然現象對人類社會造成損害的事件', '中文解釋')
        compare_system.definition('氣候變遷', '環境議題', '長期氣候平均與極端事件模式改變', '中文解釋')
        compare_system.definition('永續發展', '地理與公民議題', '兼顧環境、社會與經濟，滿足當代與未來世代需求', '中文解釋')

