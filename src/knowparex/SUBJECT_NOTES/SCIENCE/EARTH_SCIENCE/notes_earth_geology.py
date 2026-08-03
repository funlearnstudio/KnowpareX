# ===========================================
# notes_earth_geology.py
# 地球科學：地球構造、板塊、岩石、地震與地質
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class earth_geology:

    @staticmethod
    def earth_layers():
        compare_system.equal("地球內部分層由外至內", "題目", "地殼、地函、外核、內核", "答案")
        compare_system.equal("地殼", "特徵", "地球最外層且相對薄", "答案")
        compare_system.equal("地函", "範圍", "地殼下方至外核上方", "答案")
        compare_system.equal("外核", "物態", "液態", "答案")
        compare_system.equal("內核", "物態", "固態", "答案")
        compare_system.equal("地核主要元素", "題目", "鐵與鎳", "答案")
        compare_system.notequal("地函", "敘述", "全部都是完全熔融的岩漿海洋", "錯誤觀念")

    @staticmethod
    def lithosphere_asthenosphere():
        compare_system.equivalentto("岩石圈", "地球構造", "由地殼與最上部剛性地函組成的堅硬外層", "定義")
        compare_system.equivalentto("軟流圈", "地球構造", "岩石圈下方較能緩慢塑性流動的地函區域", "定義")
        compare_system.equal("板塊", "構成", "岩石圈的一部分", "答案")
        compare_system.equal("板塊移動", "所在", "在軟流圈上方移動", "答案")
        compare_system.equal("軟流圈岩石", "物態", "主要仍為固態但可緩慢流動", "答案")
        compare_system.notequal("軟流圈", "敘述", "完全是低黏度液態岩漿", "錯誤觀念")

    @staticmethod
    def continental_oceanic_crust():
        compare_system.equal("大陸地殼", "平均厚度", "通常較厚", "答案")
        compare_system.equal("海洋地殼", "平均厚度", "通常較薄", "答案")
        compare_system.equal("大陸地殼", "平均密度", "通常較低", "答案")
        compare_system.equal("海洋地殼", "平均密度", "通常較高", "答案")
        compare_system.equal("海洋地殼主要岩性", "題目", "玄武岩質", "答案")
        compare_system.equal("大陸地殼常見岩性", "題目", "花崗岩質", "答案")
        compare_system.equal("海洋地殼年齡", "一般比較", "通常比大陸地殼年輕", "答案")

    @staticmethod
    def plate_tectonics():
        compare_system.equivalentto("板塊構造學說", "地球科學理論", "岩石圈由多個移動板塊構成並在邊界產生地質作用", "定義")
        compare_system.equal("板塊運動速率", "量級", "通常每年數公分", "答案")
        compare_system.equal("板塊運動動力", "可能來源", "地函對流、板塊拉力與洋脊推力", "答案")
        compare_system.equal("地震與火山", "分布", "多集中在板塊邊界", "答案")
        compare_system.equal("台灣", "地質位置", "接近歐亞板塊與菲律賓海板塊交界", "答案")
        compare_system.notequal("板塊", "敘述", "與大陸輪廓完全一一對應", "錯誤觀念")

    @staticmethod
    def divergent_boundary():
        compare_system.equivalentto("張裂型板塊邊界", "板塊邊界", "兩板塊彼此遠離的邊界", "定義")
        compare_system.equal("中洋脊", "板塊邊界", "張裂型邊界", "答案")
        compare_system.equal("張裂型邊界", "地質作用", "形成新海洋地殼", "答案")
        compare_system.equal("海底擴張", "發生位置", "中洋脊", "答案")
        compare_system.equal("東非裂谷", "類型", "大陸張裂環境", "答案")
        compare_system.equal("張裂型邊界地震", "一般特徵", "較淺", "答案")
        compare_system.notequal("張裂型邊界", "敘述", "主要消滅海洋地殼", "錯誤觀念")

    @staticmethod
    def convergent_boundary():
        compare_system.equivalentto("聚合型板塊邊界", "板塊邊界", "兩板塊彼此接近碰撞的邊界", "定義")
        compare_system.equal("海洋板塊與大陸板塊聚合", "一般結果", "較密海洋板塊隱沒", "答案")
        compare_system.equal("海洋板塊與海洋板塊聚合", "可能形成", "海溝與島弧", "答案")
        compare_system.equal("大陸板塊與大陸板塊碰撞", "可能形成", "大型褶皺山脈", "答案")
        compare_system.equal("聚合型邊界", "地震深度", "可由淺至深分布", "答案")
        compare_system.equal("隱沒帶", "火山", "常形成火山弧", "答案")
        compare_system.notequal("大陸—大陸碰撞", "敘述", "通常由一整塊大陸地殼輕易沉入深部地函", "錯誤觀念")

    @staticmethod
    def transform_boundary():
        compare_system.equivalentto("錯動型板塊邊界", "板塊邊界", "兩板塊沿水平方向互相滑動的邊界", "定義")
        compare_system.equal("錯動型邊界", "地殼生成消滅", "通常不明顯生成或消滅", "答案")
        compare_system.equal("聖安地列斯斷層", "類型", "錯動型板塊邊界", "答案")
        compare_system.equal("錯動型邊界", "主要災害", "淺源地震", "答案")
        compare_system.equal("錯動型邊界", "火山活動", "通常較少", "答案")
        compare_system.notequal("錯動型邊界", "敘述", "兩板塊彼此遠離形成中洋脊", "錯誤觀念")

    @staticmethod
    def continental_drift():
        compare_system.equivalentto("大陸漂移學說", "地質學說", "大陸曾聚合並隨時間移動至現今位置", "定義")
        compare_system.equal("提出大陸漂移學說者", "題目", "韋格納", "答案")
        compare_system.equal("南美洲與非洲海岸線", "證據", "形狀可相互拼合", "答案")
        compare_system.equal("跨洲相同化石", "意義", "支持大陸過去相連", "答案")
        compare_system.equal("跨洲岩層與山脈連續", "意義", "支持大陸過去相連", "答案")
        compare_system.equal("古冰川痕跡", "用途", "推測古大陸位置與氣候", "答案")
        compare_system.notequal("韋格納當時", "敘述", "已完整解釋板塊運動機制並立即被全面接受", "錯誤觀念")

    @staticmethod
    def seafloor_spreading():
        compare_system.equivalentto("海底擴張", "地質過程", "新海洋地殼於中洋脊生成並向兩側移動", "定義")
        compare_system.equal("海洋地殼年齡", "距中洋脊", "距離愈遠通常愈老", "答案")
        compare_system.equal("海洋沉積物厚度", "距中洋脊", "距離愈遠通常愈厚", "答案")
        compare_system.equal("海底磁條帶", "特徵", "中洋脊兩側近似對稱", "答案")
        compare_system.equal("磁條帶", "成因", "地磁反轉與新岩漿冷卻記錄", "答案")
        compare_system.equal("海底擴張證據", "例子", "岩齡、磁條帶與熱流分布", "答案")
        compare_system.notequal("最老海洋地殼", "位置", "位於中洋脊正中央", "錯誤觀念")

    @staticmethod
    def earthquake():
        compare_system.equivalentto("地震", "地質現象", "岩層突然破裂或滑動釋放能量造成的地面震動", "定義")
        compare_system.equal("震源", "定義", "地下開始破裂並釋放能量的位置", "答案")
        compare_system.equal("震央", "定義", "震源正上方的地表位置", "答案")
        compare_system.equal("斷層", "定義", "岩層發生相對位移的破裂面", "答案")
        compare_system.equal("彈性回跳理論", "內容", "岩石累積應力後突然破裂並回彈", "答案")
        compare_system.equal("餘震", "發生", "主震後斷層附近持續調整", "答案")
        compare_system.notequal("震央", "敘述", "一定是地震破裂最深的位置", "錯誤觀念")

    @staticmethod
    def seismic_wave():
        compare_system.equal("P 波", "波形", "縱波", "答案")
        compare_system.equal("S 波", "波形", "橫波", "答案")
        compare_system.equal("P 波速度", "比較", "快於 S 波", "答案")
        compare_system.equal("P 波", "介質", "可通過固體、液體與氣體", "答案")
        compare_system.equal("S 波", "介質", "不能通過液體", "答案")
        compare_system.equal("表面波", "一般特徵", "常造成較強地表破壞", "答案")
        compare_system.equal("P-S 到時差", "用途", "推算與震央的距離", "答案")
        compare_system.notequal("S 波", "敘述", "可直接穿過液態外核", "錯誤觀念")

    @staticmethod
    def magnitude_intensity():
        compare_system.equivalentto("地震規模", "地震量度", "描述地震釋放能量大小的數值", "定義")
        compare_system.equivalentto("地震震度", "地震量度", "某地實際感受到的搖晃與影響程度", "定義")
        compare_system.equal("同一地震", "規模", "通常只有一個主要規模值", "答案")
        compare_system.equal("同一地震", "震度", "不同地點可以不同", "答案")
        compare_system.equal("距震央較近", "一般情況", "震度通常較大", "答案")
        compare_system.equal("地質鬆軟區", "影響", "可能放大地震波", "答案")
        compare_system.notequal("規模", "概念", "某棟建築物搖晃程度", "錯誤觀念")

    @staticmethod
    def fault():
        compare_system.equivalentto("正斷層", "斷層", "張力作用下上盤相對下降", "定義")
        compare_system.equivalentto("逆斷層", "斷層", "壓縮作用下上盤相對上升", "定義")
        compare_system.equivalentto("平移斷層", "斷層", "兩側岩塊主要沿水平方向相對移動", "定義")
        compare_system.equal("正斷層", "主要應力", "張力", "答案")
        compare_system.equal("逆斷層", "主要應力", "壓縮力", "答案")
        compare_system.equal("平移斷層", "主要應力", "剪切力", "答案")
        compare_system.notequal("斷層", "敘述", "只要岩層破裂但沒有位移也一定稱為斷層", "錯誤觀念")

    @staticmethod
    def fold():
        compare_system.equivalentto("褶皺", "地質構造", "岩層受力後彎曲形成的構造", "定義")
        compare_system.equivalentto("背斜", "褶皺", "岩層向上拱起的構造", "定義")
        compare_system.equivalentto("向斜", "褶皺", "岩層向下凹陷的構造", "定義")
        compare_system.equal("褶皺常見作用力", "題目", "壓縮力", "答案")
        compare_system.equal("背斜核心", "未倒轉理想情況", "較老岩層", "答案")
        compare_system.equal("向斜核心", "未倒轉理想情況", "較年輕岩層", "答案")
        compare_system.notequal("褶皺", "敘述", "只可能形成於完全熔融岩漿", "錯誤觀念")

    @staticmethod
    def volcano():
        compare_system.equivalentto("岩漿", "熔融物質", "位於地下的熔融或部分熔融岩石物質", "定義")
        compare_system.equivalentto("熔岩", "熔融物質", "噴出地表後的岩漿", "定義")
        compare_system.equal("火山噴發物", "例子", "熔岩、火山灰、氣體與火山碎屑", "答案")
        compare_system.equal("隱沒帶", "火山", "常形成火山弧", "答案")
        compare_system.equal("中洋脊", "火山作用", "常有玄武岩質岩漿活動", "答案")
        compare_system.equal("熱點", "火山", "可形成板塊內火山鏈", "答案")
        compare_system.notequal("所有火山", "敘述", "都只位於板塊邊界", "錯誤觀念")

    @staticmethod
    def magma_viscosity():
        compare_system.equal("岩漿二氧化矽含量增加", "一般結果", "黏度增加", "答案")
        compare_system.equal("岩漿溫度升高", "一般結果", "黏度降低", "答案")
        compare_system.equal("岩漿黏度高", "氣體逸散", "較困難", "答案")
        compare_system.equal("岩漿黏度高且氣體多", "噴發", "較可能爆炸性噴發", "答案")
        compare_system.equal("玄武岩質岩漿", "一般特徵", "二氧化矽較低、黏度較低", "答案")
        compare_system.equal("流紋岩質岩漿", "一般特徵", "二氧化矽較高、黏度較高", "答案")
        compare_system.notequal("岩漿黏度", "敘述", "只由岩漿顏色決定", "錯誤觀念")

    @staticmethod
    def mineral():
        compare_system.equivalentto("礦物", "天然物質", "天然形成、通常無機、固態且具特定化學組成與晶體結構的物質", "定義")
        compare_system.equal("礦物鑑定性質", "例子", "顏色、條痕、硬度、解理與光澤", "答案")
        compare_system.equal("莫氏硬度", "用途", "比較礦物抗刮能力", "答案")
        compare_system.equal("石英莫氏硬度", "數值", "7", "答案")
        compare_system.equal("滑石莫氏硬度", "數值", "1", "答案")
        compare_system.equal("金剛石莫氏硬度", "數值", "10", "答案")
        compare_system.notequal("礦物顏色", "敘述", "永遠是最可靠且唯一鑑定特徵", "錯誤觀念")

    @staticmethod
    def igneous_rock():
        compare_system.equivalentto("火成岩", "岩石", "岩漿或熔岩冷卻凝固形成的岩石", "定義")
        compare_system.equivalentto("侵入岩", "火成岩", "岩漿在地下緩慢冷卻形成的岩石", "定義")
        compare_system.equivalentto("噴出岩", "火成岩", "熔岩在地表或近地表快速冷卻形成的岩石", "定義")
        compare_system.equal("花崗岩", "分類", "侵入岩", "答案")
        compare_system.equal("玄武岩", "分類", "噴出岩", "答案")
        compare_system.equal("冷卻較慢", "晶粒", "通常較大", "答案")
        compare_system.equal("冷卻較快", "晶粒", "通常較小", "答案")
        compare_system.notequal("所有火成岩", "敘述", "都具有大型清楚晶體", "錯誤觀念")

    @staticmethod
    def sedimentary_rock():
        compare_system.equivalentto("沉積岩", "岩石", "沉積物經壓密、膠結或化學與生物作用形成的岩石", "定義")
        compare_system.equal("砂岩", "分類", "碎屑沉積岩", "答案")
        compare_system.equal("頁岩", "分類", "碎屑沉積岩", "答案")
        compare_system.equal("石灰岩", "形成", "可由化學沉澱或生物遺骸形成", "答案")
        compare_system.equal("沉積岩", "常見構造", "層理", "答案")
        compare_system.equal("化石", "常見岩石", "沉積岩", "答案")
        compare_system.notequal("沉積岩", "敘述", "由岩漿直接冷卻形成", "錯誤觀念")

    @staticmethod
    def metamorphic_rock():
        compare_system.equivalentto("變質岩", "岩石", "原有岩石受熱、壓力或流體作用但未完全熔融形成的岩石", "定義")
        compare_system.equal("變質作用", "條件", "高溫、高壓與化學活性流體", "答案")
        compare_system.equal("頁岩變質", "可能形成", "板岩", "答案")
        compare_system.equal("石灰岩變質", "形成", "大理岩", "答案")
        compare_system.equal("花崗岩變質", "可能形成", "片麻岩", "答案")
        compare_system.equal("葉理", "形成原因", "礦物在定向壓力下排列", "答案")
        compare_system.notequal("變質作用", "敘述", "岩石必須先完全熔化", "錯誤觀念")

    @staticmethod
    def rock_cycle():
        compare_system.equivalentto("岩石循環", "地質循環", "火成岩、沉積岩與變質岩彼此轉換的過程", "定義")
        compare_system.equal("任何岩石風化侵蝕", "結果", "可形成沉積物", "答案")
        compare_system.equal("沉積物壓密膠結", "結果", "形成沉積岩", "答案")
        compare_system.equal("岩石受熱受壓", "結果", "形成變質岩", "答案")
        compare_system.equal("岩石熔融", "結果", "形成岩漿", "答案")
        compare_system.equal("岩漿冷卻", "結果", "形成火成岩", "答案")
        compare_system.notequal("岩石循環", "敘述", "每塊岩石都依固定單一路徑轉換", "錯誤觀念")

    @staticmethod
    def weathering_erosion():
        compare_system.equivalentto("風化", "地質作用", "岩石在原地破碎或化學改變的過程", "定義")
        compare_system.equivalentto("侵蝕", "地質作用", "風、水、冰或重力移走物質的過程", "定義")
        compare_system.equivalentto("搬運", "地質作用", "沉積物被介質帶往其他地點", "定義")
        compare_system.equivalentto("沉積", "地質作用", "搬運能力下降後物質堆積", "定義")
        compare_system.equal("溫度變化使岩石裂開", "作用", "物理風化", "答案")
        compare_system.equal("酸性水溶解石灰岩", "作用", "化學風化", "答案")
        compare_system.notequal("風化", "敘述", "一定包含物質被搬走", "錯誤觀念")

    @staticmethod
    def relative_dating():
        compare_system.equivalentto("相對定年", "地質方法", "判斷地層或事件先後而不直接給出數值年齡", "定義")
        compare_system.equal("地層疊置律", "內容", "未受擾動地層通常下老上新", "答案")
        compare_system.equal("切割關係", "內容", "切穿其他構造者通常較年輕", "答案")
        compare_system.equal("包裹體", "關係", "被包裹岩塊通常比包裹它的岩石老", "答案")
        compare_system.equal("指準化石", "用途", "比對與判定地層相對年代", "答案")
        compare_system.notequal("相對定年", "敘述", "可直接告訴岩石精確形成於幾年前", "錯誤觀念")

    @staticmethod
    def radiometric_dating():
        compare_system.equivalentto("放射性定年", "定年方法", "利用放射性同位素衰變推算岩石或物質年齡", "定義")
        compare_system.equivalentto("半衰期", "放射性", "母同位素數量減少至一半所需時間", "定義")
        compare_system.equal("經過一個半衰期", "母同位素剩餘", "1/2", "答案")
        compare_system.equal("經過兩個半衰期", "母同位素剩餘", "1/4", "答案")
        compare_system.equal("碳-14 定年", "適用", "較年輕的有機遺留物", "答案")
        compare_system.equal("鈾鉛定年", "適用", "古老岩石與礦物", "答案")
        compare_system.notequal("半衰期", "敘述", "會因樣本大小或一般溫度改變而大幅改變", "錯誤觀念")