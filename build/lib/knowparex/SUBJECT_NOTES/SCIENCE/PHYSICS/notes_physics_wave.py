# ===========================================
# notes_physics_wave.py
# 物理：振動、波與聲音
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class physics_wave:

    @staticmethod
    def vibration():
        compare_system.equivalentto("振動", "運動", "物體在平衡位置附近往返運動", "定義")
        compare_system.equivalentto("平衡位置", "位置", "物體所受合力為 0 的位置", "定義")
        compare_system.equivalentto("振幅", "物理量", "物體偏離平衡位置的最大距離", "定義")
        compare_system.equivalentto("週期", "物理量", "完成一次完整振動所需的時間", "定義")
        compare_system.equivalentto("頻率", "物理量", "每秒完成的振動次數", "定義")
        compare_system.equal("頻率的 SI 單位", "題目", "赫茲（Hz）", "答案")
        compare_system.calculatedby("頻率與週期", "公式", "f = 1/T", "答案")
        compare_system.equal("週期為 0.5 秒", "題目", "頻率為 2 Hz", "答案")
        compare_system.equal("頻率為 4 Hz", "題目", "週期為 0.25 秒", "答案")

    @staticmethod
    def simple_harmonic_motion():
        compare_system.equivalentto("簡諧運動", "運動種類", "恢復力與位移成正比且方向相反的週期運動", "定義")
        compare_system.calculatedby("彈簧恢復力", "公式", "F = -kx", "答案")
        compare_system.equal("簡諧運動在平衡位置", "速度", "速度大小最大", "答案")
        compare_system.equal("簡諧運動在端點", "速度", "速度為 0", "答案")
        compare_system.equal("簡諧運動在平衡位置", "加速度", "加速度為 0", "答案")
        compare_system.equal("簡諧運動在端點", "加速度", "加速度大小最大", "答案")
        compare_system.equal("理想彈簧振子總能量", "忽略阻力", "保持不變", "答案")
        compare_system.calculatedby("彈簧振子週期", "公式", "T = 2π√(m/k)", "答案")
        compare_system.equal("彈簧振子質量增加", "條件", "週期增加", "結果")
        compare_system.equal("彈簧常數增加", "條件", "週期減小", "結果")

    @staticmethod
    def pendulum():
        compare_system.equivalentto("單擺", "系統", "細線懸掛小球並在重力作用下擺動的系統", "定義")
        compare_system.calculatedby("小角度單擺週期", "公式", "T = 2π√(L/g)", "答案")
        compare_system.equal("單擺長度增加", "條件", "週期增加", "結果")
        compare_system.equal("重力加速度增加", "條件", "週期減小", "結果")
        compare_system.equal("小角度單擺週期", "關係", "與擺錘質量無關", "答案")
        compare_system.equal("擺錘通過最低點", "速度", "速度大小最大", "答案")
        compare_system.equal("擺錘到達最高點", "速度", "瞬間速度為 0", "答案")
        compare_system.notequal("擺幅任意增大", "敘述", "單擺週期完全不變", "錯誤觀念")

    @staticmethod
    def wave():
        compare_system.equivalentto("波", "物理現象", "振動或擾動在空間中的傳播", "定義")
        compare_system.equal("波傳播的主要內容", "題目", "能量與資訊", "答案")
        compare_system.notequal("波傳播", "敘述", "介質粒子會隨波一路移到遠方", "錯誤觀念")
        compare_system.equivalentto("機械波", "波的種類", "需要介質才能傳播的波", "定義")
        compare_system.equivalentto("電磁波", "波的種類", "不需要物質介質也能傳播的波", "定義")
        compare_system.equal("聲波", "種類", "機械波", "答案")
        compare_system.equal("光波", "種類", "電磁波", "答案")
        compare_system.equal("水面波", "現象", "主要傳遞能量而非大量水體前進", "答案")

    @staticmethod
    def transverse_and_longitudinal():
        compare_system.equivalentto("橫波", "波的種類", "介質振動方向垂直於波傳播方向", "定義")
        compare_system.equivalentto("縱波", "波的種類", "介質振動方向平行於波傳播方向", "定義")
        compare_system.equal("繩波", "典型分類", "橫波", "答案")
        compare_system.equal("空氣中的聲波", "典型分類", "縱波", "答案")
        compare_system.equal("橫波最高點", "名稱", "波峰", "答案")
        compare_system.equal("橫波最低點", "名稱", "波谷", "答案")
        compare_system.equal("縱波粒子密集處", "名稱", "密部", "答案")
        compare_system.equal("縱波粒子稀疏處", "名稱", "疏部", "答案")

    @staticmethod
    def wavelength_frequency_speed():
        compare_system.equivalentto("波長", "物理量", "相鄰兩個同相位點之間的距離", "定義")
        compare_system.equal("波長的 SI 單位", "題目", "公尺（m）", "答案")
        compare_system.calculatedby("波速", "公式", "v = fλ", "答案")
        compare_system.equal("頻率 5 Hz、波長 2 m", "題目", "波速為 10 m/s", "答案")
        compare_system.equal("波速固定時頻率增加", "條件", "波長減小", "結果")
        compare_system.equal("波進入不同介質", "一般情況", "頻率保持不變", "答案")
        compare_system.equal("波進入不同介質", "一般情況", "波速與波長可能改變", "答案")
        compare_system.equal("同一介質中的波速", "主要決定因素", "介質性質", "答案")

    @staticmethod
    def reflection():
        compare_system.equivalentto("波的反射", "現象", "波遇到邊界後返回原介質", "定義")
        compare_system.equal("反射時波的頻率", "關係", "保持不變", "答案")
        compare_system.equal("反射時波速", "同一介質", "保持不變", "答案")
        compare_system.equal("反射時波長", "同一介質", "保持不變", "答案")
        compare_system.equal("固定端反射的繩波", "相位", "上下顛倒", "答案")
        compare_system.equal("自由端反射的繩波", "相位", "不顛倒", "答案")
        compare_system.equal("回聲", "現象", "聲波反射後再次被聽見", "答案")
        compare_system.equal("雷達與聲納", "應用", "利用波的反射測量距離或位置", "答案")

    @staticmethod
    def refraction():
        compare_system.equivalentto("波的折射", "現象", "波進入不同介質時因波速改變而改變方向", "定義")
        compare_system.equal("折射時頻率", "關係", "保持不變", "答案")
        compare_system.equal("折射時波速", "關係", "通常改變", "答案")
        compare_system.equal("折射時波長", "關係", "通常改變", "答案")
        compare_system.equal("垂直入射不同介質", "情況", "方向不偏折但波速仍可能改變", "答案")
        compare_system.equal("波速減小且斜向入射", "一般情況", "折射方向偏向法線", "答案")
        compare_system.equal("波速增大且斜向入射", "一般情況", "折射方向偏離法線", "答案")
        compare_system.notequal("折射", "敘述", "是頻率改變造成的", "錯誤觀念")

    @staticmethod
    def diffraction():
        compare_system.equivalentto("繞射", "波動現象", "波通過狹縫或繞過障礙物後向各方向展開", "定義")
        compare_system.equal("狹縫寬度接近波長", "條件", "繞射較明顯", "結果")
        compare_system.equal("波長較長", "相同狹縫下", "繞射通常較明顯", "結果")
        compare_system.equal("聲音可繞過牆角", "原因", "聲波具有繞射現象", "答案")
        compare_system.equal("低頻聲波", "特性", "波長較長，通常較容易繞射", "答案")
        compare_system.notequal("只有水波", "敘述", "會發生繞射", "錯誤觀念")
        compare_system.equal("光通過極小狹縫", "現象", "也會發生繞射", "答案")

    @staticmethod
    def interference():
        compare_system.equivalentto("干涉", "波動現象", "兩列或多列波重疊後形成合成波", "定義")
        compare_system.equivalentto("建設性干涉", "干涉種類", "波峰與波峰或波谷與波谷重疊而振幅增大", "定義")
        compare_system.equivalentto("破壞性干涉", "干涉種類", "波峰與波谷重疊而振幅減小", "定義")
        compare_system.equal("完全相同且反相的兩波重疊", "結果", "可能瞬間完全抵消", "答案")
        compare_system.notequal("波互相抵消後", "敘述", "能量永久消失", "錯誤觀念")
        compare_system.equal("降噪耳機", "原理之一", "利用破壞性干涉降低噪音", "答案")
        compare_system.equal("干涉", "基本原理", "波的疊加原理", "答案")

    @staticmethod
    def standing_wave():
        compare_system.equivalentto("駐波", "波動現象", "兩列同頻率反向行進波干涉形成固定節點與腹點", "定義")
        compare_system.equal("駐波中始終不振動的位置", "名稱", "節點", "答案")
        compare_system.equal("駐波中振幅最大的位置", "名稱", "腹點", "答案")
        compare_system.equal("相鄰節點距離", "關係", "半個波長", "答案")
        compare_system.equal("相鄰腹點距離", "關係", "半個波長", "答案")
        compare_system.equal("相鄰節點與腹點距離", "關係", "四分之一波長", "答案")
        compare_system.equal("弦樂器發聲", "關係", "弦上形成駐波", "答案")
        compare_system.equal("駐波", "能量傳遞", "沒有明顯的淨能量向單一方向傳播", "答案")

    @staticmethod
    def sound():
        compare_system.equivalentto("聲音", "物理現象", "物體振動產生並透過介質傳播的機械波", "定義")
        compare_system.equal("空氣中的聲波", "波形", "縱波", "答案")
        compare_system.equal("聲音在真空中", "情況", "無法傳播", "答案")
        compare_system.equal("聲音在固體、液體、氣體中", "情況", "皆可傳播", "答案")
        compare_system.equal("一般情況下聲速", "介質比較", "固體通常大於液體，液體通常大於氣體", "答案")
        compare_system.equal("空氣溫度升高", "一般情況", "聲速增加", "結果")
        compare_system.notequal("聲音大小", "敘述", "由聲速決定", "錯誤觀念")
        compare_system.equal("聲音傳播", "主要內容", "能量而非空氣整體向前移動", "答案")

    @staticmethod
    def pitch_loudness_timbre():
        compare_system.equivalentto("音調", "聲音特性", "人耳感覺聲音高低的特性", "定義")
        compare_system.equal("頻率增加", "結果", "音調升高", "答案")
        compare_system.equivalentto("響度", "聲音特性", "人耳感覺聲音強弱的特性", "定義")
        compare_system.equal("振幅增加", "一般結果", "聲音通常較響亮", "答案")
        compare_system.equivalentto("音色", "聲音特性", "用來分辨不同聲源的聲音品質", "定義")
        compare_system.equal("音色", "主要相關因素", "波形與泛音組成", "答案")
        compare_system.notequal("音調高", "敘述", "聲音一定比較大聲", "錯誤觀念")
        compare_system.notequal("振幅增加", "敘述", "聲音頻率一定增加", "錯誤觀念")

    @staticmethod
    def resonance():
        compare_system.equivalentto("共振", "現象", "外力頻率接近系統固有頻率時振幅明顯增加", "定義")
        compare_system.equal("共振條件", "題目", "驅動頻率接近固有頻率", "答案")
        compare_system.equal("盪鞦韆定時推動", "現象", "可形成共振並增大振幅", "答案")
        compare_system.equal("樂器共鳴箱", "用途", "利用共振增強聲音", "答案")
        compare_system.equal("建築物與橋梁", "工程", "需避免危險共振", "答案")
        compare_system.notequal("共振", "敘述", "代表系統沒有能量損失", "錯誤觀念")
        compare_system.equal("阻尼增加", "一般結果", "共振峰通常降低", "答案")

    @staticmethod
    def doppler_effect():
        compare_system.equivalentto("都卜勒效應", "現象", "波源與觀察者相對運動造成觀察頻率改變", "定義")
        compare_system.equal("聲源接近觀察者", "結果", "觀察到的頻率升高", "答案")
        compare_system.equal("聲源遠離觀察者", "結果", "觀察到的頻率降低", "答案")
        compare_system.equal("救護車接近時", "現象", "警笛音調較高", "答案")
        compare_system.equal("救護車遠離時", "現象", "警笛音調較低", "答案")
        compare_system.notequal("都卜勒效應", "敘述", "聲源本身發出的頻率一定改變", "錯誤觀念")
        compare_system.equal("雷達測速", "應用", "利用電磁波的都卜勒效應", "答案")
        compare_system.equal("天文紅移與藍移", "應用", "可判斷天體相對運動", "答案")