# ===========================================
# notes_chemistry_atom_periodic.py
# 化學：原子結構與週期表
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_atom_periodic:

    @staticmethod
    def atom():
        compare_system.equivalentto("原子", "化學概念", "保有元素化學性質的基本粒子", "定義")
        compare_system.equal("原子中心", "位置", "原子核", "答案")
        compare_system.equal("原子核外", "粒子", "電子", "答案")
        compare_system.equal("原子核", "組成", "質子與中子", "答案")
        compare_system.equal("原子大部分體積", "特徵", "由電子活動的空間構成", "答案")
        compare_system.equal("原子大部分質量", "位置", "集中在原子核", "答案")
        compare_system.notequal("原子", "敘述", "是絕對不可再分割的粒子", "錯誤觀念")

    @staticmethod
    def proton_neutron_electron():
        compare_system.equal("質子", "電荷", "+1", "答案")
        compare_system.equal("中子", "電荷", "0", "答案")
        compare_system.equal("電子", "電荷", "-1", "答案")
        compare_system.equal("質子相對質量", "近似值", "1", "答案")
        compare_system.equal("中子相對質量", "近似值", "1", "答案")
        compare_system.approximatelyequal("電子相對質量", "數值", "1/1836", "近似值")
        compare_system.equal("決定元素種類的粒子數", "題目", "質子數", "答案")
        compare_system.equal("影響原子化學性質的重要粒子", "題目", "最外層電子", "答案")

    @staticmethod
    def atomic_number():
        compare_system.equivalentto("原子序", "物理量", "原子核中的質子數", "定義")
        compare_system.equal("原子序符號", "題目", "Z", "答案")
        compare_system.equal("中性原子的電子數", "關係", "等於質子數", "答案")
        compare_system.equal("碳的原子序為 6", "意義", "碳原子含有 6 個質子", "答案")
        compare_system.equal("質子數改變", "結果", "元素種類改變", "答案")
        compare_system.notequal("中子數改變", "敘述", "元素種類一定改變", "錯誤觀念")

    @staticmethod
    def mass_number():
        compare_system.equivalentto("質量數", "物理量", "原子核內質子數與中子數的總和", "定義")
        compare_system.calculatedby("質量數", "公式", "A = 質子數 + 中子數", "答案")
        compare_system.calculatedby("中子數", "公式", "中子數 = A - Z", "答案")
        compare_system.equal("質量數符號", "題目", "A", "答案")
        compare_system.equal("質子 8、中子 8", "題目", "質量數為 16", "答案")
        compare_system.notequal("質量數", "概念", "週期表上的平均原子量", "錯誤觀念")

    @staticmethod
    def isotope():
        compare_system.equivalentto("同位素", "原子種類", "質子數相同但中子數不同的原子", "定義")
        compare_system.equal("同位素", "元素種類", "相同", "答案")
        compare_system.equal("同位素", "質量數", "不同", "答案")
        compare_system.equal("碳-12 與碳-14", "關係", "互為同位素", "答案")
        compare_system.equal("氫-1、氫-2、氫-3", "關係", "互為同位素", "答案")
        compare_system.equal("同位素的化學性質", "一般情況", "相似", "答案")
        compare_system.equal("同位素的物理性質", "一般情況", "可能不同", "答案")
        compare_system.notequal("同位素", "敘述", "質子數不同但中子數相同", "錯誤觀念")

    @staticmethod
    def average_atomic_mass():
        compare_system.equivalentto("平均原子量", "物理量", "各天然同位素質量依豐度加權的平均值", "定義")
        compare_system.calculatedby("平均原子量", "公式", "Σ（同位素質量 × 天然豐度）", "答案")
        compare_system.equal("週期表上的原子量通常不是整數", "原因", "是天然同位素的加權平均", "答案")
        compare_system.equal("氯的平均原子量約 35.45", "意義", "不是每個氯原子都具有 35.45 的質量數", "答案")
        compare_system.notequal("平均原子量", "敘述", "等於質子數與中子數直接相加", "錯誤觀念")
        compare_system.equal("同位素豐度改變", "結果", "樣品的平均原子量可能改變", "答案")

    @staticmethod
    def ion():
        compare_system.equivalentto("離子", "粒子", "因失去或得到電子而帶電的原子或原子團", "定義")
        compare_system.equivalentto("陽離子", "離子", "帶正電的離子", "定義")
        compare_system.equivalentto("陰離子", "離子", "帶負電的離子", "定義")
        compare_system.equal("原子失去電子", "結果", "形成陽離子", "答案")
        compare_system.equal("原子得到電子", "結果", "形成陰離子", "答案")
        compare_system.equal("Na⁺", "形成方式", "鈉原子失去 1 個電子", "答案")
        compare_system.equal("Cl⁻", "形成方式", "氯原子得到 1 個電子", "答案")
        compare_system.notequal("形成離子", "敘述", "原子核中的質子數會改變", "錯誤觀念")

    @staticmethod
    def electron_shell():
        compare_system.equivalentto("電子層", "原子模型", "電子依能量分布的主要層次", "定義")
        compare_system.equal("第一電子層最大電子數", "基礎模型", "2", "答案")
        compare_system.equal("第二電子層最大電子數", "基礎模型", "8", "答案")
        compare_system.equal("最外層電子", "別名", "價電子", "答案")
        compare_system.equal("價電子", "重要性", "與化學反應與化學鍵密切相關", "答案")
        compare_system.equal("同族主族元素", "一般關係", "價電子數相同或相似", "答案")
        compare_system.notequal("所有電子", "敘述", "具有完全相同的能量", "錯誤觀念")

    @staticmethod
    def electron_configuration():
        compare_system.equal("鈉原子電子排列", "基礎層模型", "2、8、1", "答案")
        compare_system.equal("氯原子電子排列", "基礎層模型", "2、8、7", "答案")
        compare_system.equal("氖原子電子排列", "基礎層模型", "2、8", "答案")
        compare_system.equal("主族元素週期數", "一般關係", "等於主要占據電子層數", "答案")
        compare_system.equal("最外層達穩定排列", "一般結果", "元素通常較不易反應", "答案")
        compare_system.equal("鈉形成 Na⁺", "電子排列變化", "2、8、1 變成 2、8", "答案")
        compare_system.equal("氯形成 Cl⁻", "電子排列變化", "2、8、7 變成 2、8、8", "答案")

    @staticmethod
    def periodic_table():
        compare_system.equivalentto("週期表", "化學工具", "依原子序排列並呈現元素週期性質的表格", "定義")
        compare_system.equal("週期表排列依據", "題目", "原子序遞增", "答案")
        compare_system.equal("週期表橫列", "名稱", "週期", "答案")
        compare_system.equal("週期表直行", "名稱", "族", "答案")
        compare_system.equal("同族元素", "一般特徵", "具有相似的化學性質", "答案")
        compare_system.equal("同週期元素", "一般特徵", "主要電子層數相同", "答案")
        compare_system.notequal("現代週期表", "敘述", "依原子量大小排列", "錯誤觀念")

    @staticmethod
    def metal_nonmetal_metalloid():
        compare_system.equivalentto("金屬", "元素分類", "通常具有導電、導熱、延展與金屬光澤等性質", "定義")
        compare_system.equivalentto("非金屬", "元素分類", "通常缺乏典型金屬性質的元素", "定義")
        compare_system.equivalentto("類金屬", "元素分類", "性質介於金屬與非金屬之間的元素", "定義")
        compare_system.equal("週期表左側與中央", "主要元素類型", "金屬", "答案")
        compare_system.equal("週期表右上方", "主要元素類型", "非金屬", "答案")
        compare_system.equal("矽", "元素分類", "類金屬", "答案")
        compare_system.equal("金屬形成離子", "一般傾向", "失去電子形成陽離子", "答案")
        compare_system.equal("非金屬形成離子", "一般傾向", "得到電子形成陰離子", "答案")

    @staticmethod
    def alkali_metal():
        compare_system.equivalentto("鹼金屬", "元素族", "週期表第 1 族中除氫以外的金屬元素", "定義")
        compare_system.equal("鹼金屬價電子數", "題目", "1", "答案")
        compare_system.equal("鹼金屬形成離子", "一般電荷", "+1", "答案")
        compare_system.equal("鈉與鉀", "分類", "鹼金屬", "答案")
        compare_system.equal("鹼金屬與水", "一般情況", "可發生明顯反應", "答案")
        compare_system.equal("鹼金屬由上往下", "一般趨勢", "反應性增強", "答案")
        compare_system.notequal("氫", "敘述", "具有所有典型鹼金屬性質", "錯誤觀念")

    @staticmethod
    def alkaline_earth():
        compare_system.equivalentto("鹼土金屬", "元素族", "週期表第 2 族元素", "定義")
        compare_system.equal("鹼土金屬價電子數", "題目", "2", "答案")
        compare_system.equal("鹼土金屬常形成離子", "一般電荷", "+2", "答案")
        compare_system.equal("鎂與鈣", "分類", "鹼土金屬", "答案")
        compare_system.equal("鹼土金屬反應性", "一般比較", "通常低於同週期鹼金屬", "答案")
        compare_system.equal("鈣離子", "符號", "Ca²⁺", "答案")

    @staticmethod
    def halogen():
        compare_system.equivalentto("鹵素", "元素族", "週期表第 17 族元素", "定義")
        compare_system.equal("鹵素價電子數", "題目", "7", "答案")
        compare_system.equal("鹵素常形成離子", "一般電荷", "-1", "答案")
        compare_system.equal("氟、氯、溴、碘", "分類", "鹵素", "答案")
        compare_system.equal("鹵素單質", "常見形式", "雙原子分子", "答案")
        compare_system.equal("鹵素由上往下", "一般趨勢", "反應性通常降低", "答案")
        compare_system.equal("氯離子", "符號", "Cl⁻", "答案")

    @staticmethod
    def noble_gas():
        compare_system.equivalentto("鈍氣", "元素族", "週期表第 18 族元素", "定義")
        compare_system.equal("鈍氣最外層電子", "一般特徵", "接近穩定滿層排列", "答案")
        compare_system.equal("氦、氖、氬", "分類", "鈍氣", "答案")
        compare_system.equal("鈍氣化學反應性", "一般特徵", "較低", "答案")
        compare_system.equal("鈍氣常溫下", "物態", "氣體", "答案")
        compare_system.equal("氖氣", "應用", "霓虹燈", "答案")
        compare_system.notequal("鈍氣", "敘述", "在任何條件下都完全不能形成化合物", "錯誤觀念")

    @staticmethod
    def periodic_trend():
        compare_system.equal("同週期由左至右", "原子半徑一般趨勢", "減小", "答案")
        compare_system.equal("同族由上至下", "原子半徑一般趨勢", "增大", "答案")
        compare_system.equal("同週期由左至右", "第一游離能一般趨勢", "增大", "答案")
        compare_system.equal("同族由上至下", "第一游離能一般趨勢", "減小", "答案")
        compare_system.equal("同週期由左至右", "電負度一般趨勢", "增大", "答案")
        compare_system.equal("氟", "電負度", "週期表中最高", "答案")
        compare_system.notequal("週期趨勢", "敘述", "所有元素都毫無例外完全符合簡單趨勢", "錯誤觀念")