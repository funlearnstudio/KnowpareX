# ===========================================
# notes_physics_electricity.py
# 物理：靜電、電流與電路
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_electricity:

    @staticmethod
    def electric_charge():
        compare_system.equivalentto("電荷", "物理量", "物體所具有的電性", "定義")
        compare_system.equal("電荷的 SI 單位", "題目", "庫侖（C）", "答案")
        compare_system.equal("電荷種類", "題目", "正電荷與負電荷", "答案")
        compare_system.equal("同種電荷", "交互作用", "互相排斥", "答案")
        compare_system.equal("異種電荷", "交互作用", "互相吸引", "答案")
        compare_system.equal("質子", "帶電情況", "帶正電", "答案")
        compare_system.equal("電子", "帶電情況", "帶負電", "答案")
        compare_system.equal("中子", "帶電情況", "不帶電", "答案")
        compare_system.equal("物體失去電子", "結果", "物體帶正電", "答案")
        compare_system.equal("物體得到電子", "結果", "物體帶負電", "答案")
        compare_system.equivalentto("電荷守恆", "定律", "孤立系統的總電量保持不變", "定義")

    @staticmethod
    def charging():
        compare_system.equal("摩擦起電", "過程", "不同物體接觸摩擦後電子發生轉移", "答案")
        compare_system.equal("接觸起電", "過程", "帶電體接觸導體後使電荷重新分布", "答案")
        compare_system.equal("感應起電", "過程", "不直接接觸而利用電荷分離使物體帶電", "答案")
        compare_system.equal("摩擦起電時移動的粒子", "題目", "電子", "答案")
        compare_system.notequal("摩擦起電", "敘述", "產生新的電荷", "錯誤觀念")
        compare_system.equal("摩擦起電", "本質", "電子由一物體轉移至另一物體", "答案")
        compare_system.equal("導體接地", "作用", "使電子可以在物體與大地之間移動", "答案")
        compare_system.equal("驗電器", "用途", "檢驗物體是否帶電", "答案")

    @staticmethod
    def conductor_and_insulator():
        compare_system.equivalentto("導體", "材料", "電荷較容易在其中移動的物質", "定義")
        compare_system.equivalentto("絕緣體", "材料", "電荷不容易在其中移動的物質", "定義")
        compare_system.equal("金屬", "材料種類", "通常是良導體", "答案")
        compare_system.equal("人體", "材料種類", "可以導電", "答案")
        compare_system.equal("乾燥塑膠", "材料種類", "通常是絕緣體", "答案")
        compare_system.equal("橡膠", "材料種類", "通常是絕緣體", "答案")
        compare_system.equal("銅線外包塑膠", "設計", "內部導電、外部絕緣", "答案")
        compare_system.notequal("絕緣體", "敘述", "任何情況下都完全不導電", "錯誤觀念")

    @staticmethod
    def coulomb_law():
        compare_system.equivalentto("庫侖力", "物理量", "兩電荷之間的靜電作用力", "定義")
        compare_system.calculatedby("庫侖力大小", "公式", "F = k|q₁q₂| ÷ r²", "答案")
        compare_system.equal("兩電荷量增加", "條件", "庫侖力增大", "結果")
        compare_system.equal("兩電荷距離增加", "條件", "庫侖力減小", "結果")
        compare_system.equal("距離變為原來 2 倍", "條件", "庫侖力變為原來 1/4", "結果")
        compare_system.equal("其中一電荷量變為原來 3 倍", "條件", "庫侖力變為原來 3 倍", "結果")
        compare_system.equal("同號電荷", "庫侖力方向", "互相排斥", "答案")
        compare_system.equal("異號電荷", "庫侖力方向", "互相吸引", "答案")

    @staticmethod
    def electric_field():
        compare_system.equivalentto("電場", "物理概念", "電荷周圍能對其他電荷產生電力的空間", "定義")
        compare_system.calculatedby("電場強度", "公式", "E = F ÷ q", "答案")
        compare_system.equal("電場強度的 SI 單位", "題目", "牛頓／庫侖（N/C）", "答案")
        compare_system.equal("正試驗電荷受力方向", "關係", "與電場方向相同", "答案")
        compare_system.equal("負電荷受力方向", "關係", "與電場方向相反", "答案")
        compare_system.equal("正點電荷的電場線", "方向", "向外放射", "答案")
        compare_system.equal("負點電荷的電場線", "方向", "向內集中", "答案")
        compare_system.equal("電場線愈密集", "意義", "電場通常愈強", "答案")
        compare_system.notequal("電場線", "敘述", "是真實存在的物質線條", "錯誤觀念")

    @staticmethod
    def electric_potential():
        compare_system.equivalentto("電位", "物理量", "單位正電荷所具有的電位能", "定義")
        compare_system.calculatedby("電位", "公式", "V = U ÷ q", "答案")
        compare_system.equal("電位的 SI 單位", "題目", "伏特（V）", "答案")
        compare_system.equivalentto("電位差", "物理量", "兩點之間每單位電荷的電位能差", "定義")
        compare_system.calculatedby("電位差", "公式", "ΔV = ΔU ÷ q", "答案")
        compare_system.equal("1 伏特", "定義", "每 1 庫侖電荷具有 1 焦耳能量差", "內容")
        compare_system.equal("正電荷自然移動", "理想情況", "由高電位移向低電位", "答案")
        compare_system.notequal("電位", "物理量", "電位能", "物理量")

    @staticmethod
    def current():
        compare_system.equivalentto("電流", "物理量", "單位時間內通過導線截面的電量", "定義")
        compare_system.calculatedby("電流", "公式", "I = Q ÷ t", "答案")
        compare_system.equal("電流的 SI 單位", "題目", "安培（A）", "答案")
        compare_system.equal("1 安培", "定義", "每秒通過 1 庫侖電量", "內容")
        compare_system.equal("10 C 電量在 5 秒內通過", "題目", "電流為 2 A", "答案")
        compare_system.equal("傳統電流方向", "定義", "正電荷移動的方向", "答案")
        compare_system.equal("金屬導線內電子移動方向", "關係", "與傳統電流方向相反", "答案")
        compare_system.equal("形成穩定電流", "基本條件", "閉合電路與電位差", "答案")
        compare_system.notequal("電子移動速度", "敘述", "等於電能傳播速度", "錯誤觀念")

    @staticmethod
    def voltage():
        compare_system.equivalentto("電壓", "物理量", "電路兩點之間的電位差", "定義")
        compare_system.equal("電壓的 SI 單位", "題目", "伏特（V）", "答案")
        compare_system.equal("電池", "作用", "在電路兩端維持電位差", "答案")
        compare_system.equal("電壓愈大", "相同電阻下", "電流通常愈大", "結果")
        compare_system.equal("伏特計", "用途", "測量元件兩端的電壓", "答案")
        compare_system.equal("伏特計接法", "題目", "與待測元件並聯", "答案")
        compare_system.equal("理想伏特計電阻", "題目", "非常大", "答案")
        compare_system.notequal("電池沒有接通電路", "敘述", "兩端一定沒有電壓", "錯誤觀念")

    @staticmethod
    def resistance():
        compare_system.equivalentto("電阻", "物理量", "導體阻礙電流通過的程度", "定義")
        compare_system.equal("電阻的 SI 單位", "題目", "歐姆（Ω）", "答案")
        compare_system.equal("導線長度增加", "其他條件相同", "電阻增大", "結果")
        compare_system.equal("導線截面積增加", "其他條件相同", "電阻減小", "結果")
        compare_system.equal("材料不同", "條件", "電阻率可能不同", "結果")
        compare_system.calculatedby("均勻導線電阻", "公式", "R = ρL ÷ A", "答案")
        compare_system.equal("金屬溫度升高", "一般情況", "電阻通常增大", "結果")
        compare_system.equal("歐姆計", "用途", "測量電阻", "答案")

    @staticmethod
    def ohms_law():
        compare_system.equivalentto("歐姆定律", "定律", "溫度固定時，導體電流與電壓成正比", "定義")
        compare_system.calculatedby("歐姆定律", "公式", "V = IR", "答案")
        compare_system.calculatedby("電流", "公式", "I = V ÷ R", "答案")
        compare_system.calculatedby("電阻", "公式", "R = V ÷ I", "答案")
        compare_system.equal("電壓 12 V、電阻 4 Ω", "題目", "電流為 3 A", "答案")
        compare_system.equal("電流 2 A、電阻 5 Ω", "題目", "電壓為 10 V", "答案")
        compare_system.equal("相同電壓下電阻增大", "條件", "電流減小", "結果")
        compare_system.notequal("所有電路元件", "敘述", "都完全符合歐姆定律", "錯誤觀念")

    @staticmethod
    def ammeter_and_voltmeter():
        compare_system.equal("安培計", "用途", "測量電流", "答案")
        compare_system.equal("安培計接法", "題目", "與待測元件串聯", "答案")
        compare_system.equal("理想安培計電阻", "題目", "接近 0", "答案")
        compare_system.equal("伏特計", "用途", "測量電位差", "答案")
        compare_system.equal("伏特計接法", "題目", "與待測元件並聯", "答案")
        compare_system.equal("理想伏特計電阻", "題目", "非常大", "答案")
        compare_system.notequal("安培計", "接法", "直接跨接在電池兩端", "危險錯誤")
        compare_system.equal("電表正負端接反", "直流電路", "指針可能反向偏轉", "結果")

    @staticmethod
    def series_circuit():
        compare_system.equivalentto("串聯電路", "電路種類", "元件依序連接成單一路徑的電路", "定義")
        compare_system.equal("串聯電路各處電流", "關係", "相等", "答案")
        compare_system.equal("串聯電路總電壓", "關係", "各元件電壓降總和", "答案")
        compare_system.calculatedby("串聯總電阻", "公式", "R總 = R₁ + R₂ + ⋯", "答案")
        compare_system.equal("串聯增加一個電阻", "電源電壓固定", "總電阻增大、總電流減小", "結果")
        compare_system.equal("串聯其中一處斷路", "結果", "整個電路沒有電流", "答案")
        compare_system.equal("2 Ω 與 3 Ω 串聯", "題目", "總電阻為 5 Ω", "答案")
        compare_system.equal("相同燈泡串聯", "一般結果", "每顆通常比單獨接電池時暗", "答案")

    @staticmethod
    def parallel_circuit():
        compare_system.equivalentto("並聯電路", "電路種類", "元件分別連接在相同兩端點的電路", "定義")
        compare_system.equal("並聯各支路電壓", "關係", "相等", "答案")
        compare_system.equal("並聯總電流", "關係", "各支路電流總和", "答案")
        compare_system.calculatedby("並聯總電阻", "公式", "1/R總 = 1/R₁ + 1/R₂ + ⋯", "答案")
        compare_system.smaller("並聯總電阻", "關係", "任一支路電阻", "關係")
        compare_system.equal("並聯增加一條支路", "電壓固定", "總電阻減小、總電流增大", "結果")
        compare_system.equal("並聯一支路斷路", "結果", "其他正常支路仍可工作", "答案")
        compare_system.equal("相同電阻 R 兩個並聯", "題目", "總電阻為 R/2", "答案")
        compare_system.equal("家庭用電器", "主要連接方式", "並聯", "答案")

    @staticmethod
    def electric_power():
        compare_system.equivalentto("電功率", "物理量", "電器每秒轉換電能的速率", "定義")
        compare_system.calculatedby("電功率", "公式", "P = VI", "答案")
        compare_system.calculatedby("電功率", "電阻形式", "P = I²R", "答案")
        compare_system.calculatedby("電功率", "電壓形式", "P = V² ÷ R", "答案")
        compare_system.equal("電功率的 SI 單位", "題目", "瓦特（W）", "答案")
        compare_system.equal("電壓 12 V、電流 2 A", "題目", "電功率為 24 W", "答案")
        compare_system.equal("額定功率較大", "相同使用時間", "通常消耗較多電能", "結果")
        compare_system.notequal("功率 100 W", "敘述", "每秒消耗 100 庫侖電量", "錯誤觀念")

    @staticmethod
    def electric_energy():
        compare_system.equivalentto("電能", "能量", "電流通過元件時所轉換或傳遞的能量", "定義")
        compare_system.calculatedby("電能", "公式", "E = Pt", "答案")
        compare_system.calculatedby("電能", "電路公式", "E = VIt", "答案")
        compare_system.equal("電能的 SI 單位", "題目", "焦耳（J）", "答案")
        compare_system.equal("家庭電費常用單位", "題目", "度（kWh）", "答案")
        compare_system.equal("1 度電", "單位換算", "1 kWh", "答案")
        compare_system.equal("1 kWh", "單位換算", "3.6 × 10⁶ J", "答案")
        compare_system.equal("1000 W 電器使用 2 小時", "題目", "消耗 2 度電", "答案")

    @staticmethod
    def safety():
        compare_system.equal("保險絲", "作用", "電流過大時熔斷並切斷電路", "答案")
        compare_system.equal("無熔絲開關", "作用", "電流過大時自動跳脫", "答案")
        compare_system.equal("接地線", "作用", "將漏電電流導入大地以降低觸電風險", "答案")
        compare_system.equal("潮濕環境", "觸電風險", "通常較高", "答案")
        compare_system.equal("人體電阻降低", "相同電壓下", "通過人體的電流增大", "結果")
        compare_system.equal("家庭插座過度串接", "風險", "可能造成過大電流與電線過熱", "答案")
        compare_system.notequal("鳥停在單一高壓電線上", "敘述", "一定會因高電壓而觸電", "錯誤觀念")
        compare_system.equal("觸電危險程度", "主要因素", "通過人體的電流大小與時間", "答案")