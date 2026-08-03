# ===========================================
# notes_chemistry_matter.py
# 化學：物質、性質與分離
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_matter:

    @staticmethod
    def matter():
        compare_system.equivalentto("物質", "化學概念", "具有質量並占有空間的東西", "定義")
        compare_system.equal("物質的基本分類", "題目", "純物質與混合物", "答案")
        compare_system.equal("純物質", "特徵", "具有固定組成與特定性質", "答案")
        compare_system.equal("混合物", "特徵", "組成比例可以改變", "答案")
        compare_system.equal("空氣", "物質分類", "均勻混合物", "答案")
        compare_system.equal("純水", "物質分類", "化合物", "答案")
        compare_system.equal("氧氣", "物質分類", "元素物質", "答案")
        compare_system.notequal("純物質", "敘述", "一定只含有一種原子", "錯誤觀念")

    @staticmethod
    def element_compound_mixture():
        compare_system.equivalentto("元素", "純物質", "由相同原子序的原子所構成的物質", "定義")
        compare_system.equivalentto("化合物", "純物質", "由兩種以上元素以固定比例化合形成的物質", "定義")
        compare_system.equivalentto("混合物", "物質分類", "不同物質以不固定比例混合而成", "定義")
        compare_system.equal("鐵（Fe）", "物質分類", "元素", "答案")
        compare_system.equal("水（H₂O）", "物質分類", "化合物", "答案")
        compare_system.equal("食鹽水", "物質分類", "混合物", "答案")
        compare_system.equal("化合物", "分離方式", "通常需要化學方法才能分解", "答案")
        compare_system.equal("混合物", "分離方式", "通常可以利用物理性質差異分離", "答案")

    @staticmethod
    def homogeneous_heterogeneous():
        compare_system.equivalentto("均勻混合物", "混合物", "各部分組成與性質大致相同的混合物", "定義")
        compare_system.equivalentto("非均勻混合物", "混合物", "不同部分組成或性質不完全相同的混合物", "定義")
        compare_system.equal("食鹽水", "分類", "均勻混合物", "答案")
        compare_system.equal("空氣", "分類", "均勻混合物", "答案")
        compare_system.equal("泥水", "分類", "非均勻混合物", "答案")
        compare_system.equal("油與水", "分類", "非均勻混合物", "答案")
        compare_system.equal("合金", "一般分類", "均勻混合物", "答案")
        compare_system.notequal("外觀看起來透明", "敘述", "一定是純物質", "錯誤觀念")

    @staticmethod
    def physical_property():
        compare_system.equivalentto("物理性質", "性質種類", "不改變物質化學組成即可觀察或測量的性質", "定義")
        compare_system.equal("顏色", "性質分類", "物理性質", "答案")
        compare_system.equal("密度", "性質分類", "物理性質", "答案")
        compare_system.equal("熔點", "性質分類", "物理性質", "答案")
        compare_system.equal("沸點", "性質分類", "物理性質", "答案")
        compare_system.equal("導電性", "性質分類", "物理性質", "答案")
        compare_system.equal("溶解度", "性質分類", "物理性質", "答案")
        compare_system.notequal("物理性質", "敘述", "一定需要讓物質發生反應才能測量", "錯誤觀念")

    @staticmethod
    def chemical_property():
        compare_system.equivalentto("化學性質", "性質種類", "物質發生化學變化時表現出的性質", "定義")
        compare_system.equal("可燃性", "性質分類", "化學性質", "答案")
        compare_system.equal("與酸反應的能力", "性質分類", "化學性質", "答案")
        compare_system.equal("氧化性", "性質分類", "化學性質", "答案")
        compare_system.equal("還原性", "性質分類", "化學性質", "答案")
        compare_system.equal("鐵容易生鏽", "性質分類", "化學性質", "答案")
        compare_system.equal("酒精可以燃燒", "性質分類", "化學性質", "答案")
        compare_system.notequal("化學性質", "敘述", "只描述物質的外觀", "錯誤觀念")

    @staticmethod
    def physical_change():
        compare_system.equivalentto("物理變化", "變化種類", "沒有產生新物質的變化", "定義")
        compare_system.equal("冰融化", "變化分類", "物理變化", "答案")
        compare_system.equal("水沸騰", "變化分類", "物理變化", "答案")
        compare_system.equal("糖溶於水", "一般分類", "物理變化", "答案")
        compare_system.equal("玻璃破裂", "變化分類", "物理變化", "答案")
        compare_system.equal("鐵絲彎曲", "變化分類", "物理變化", "答案")
        compare_system.equal("狀態改變", "一般分類", "物理變化", "答案")
        compare_system.notequal("物理變化", "敘述", "一定可以輕易恢復原狀", "錯誤觀念")

    @staticmethod
    def chemical_change():
        compare_system.equivalentto("化學變化", "變化種類", "產生一種或多種新物質的變化", "定義")
        compare_system.equal("燃燒", "變化分類", "化學變化", "答案")
        compare_system.equal("鐵生鏽", "變化分類", "化學變化", "答案")
        compare_system.equal("食物腐敗", "變化分類", "化學變化", "答案")
        compare_system.equal("酸鹼中和", "變化分類", "化學變化", "答案")
        compare_system.equal("產生氣體", "可能現象", "可能表示發生化學變化", "答案")
        compare_system.equal("形成沉澱", "可能現象", "可能表示發生化學變化", "答案")
        compare_system.notequal("出現顏色變化", "敘述", "一定代表發生化學反應", "錯誤觀念")

    @staticmethod
    def states_of_matter():
        compare_system.equal("固態", "粒子排列", "通常排列緊密且位置較固定", "答案")
        compare_system.equal("液態", "粒子特性", "粒子接近但可以彼此移動", "答案")
        compare_system.equal("氣態", "粒子特性", "粒子距離較遠並快速運動", "答案")
        compare_system.equal("固體", "形狀與體積", "通常具有固定形狀與固定體積", "答案")
        compare_system.equal("液體", "形狀與體積", "形狀隨容器改變但體積近似固定", "答案")
        compare_system.equal("氣體", "形狀與體積", "形狀與體積皆隨容器改變", "答案")
        compare_system.equal("氣體容易壓縮", "原因", "粒子間距離較大", "答案")
        compare_system.notequal("液體粒子", "敘述", "完全靜止不動", "錯誤觀念")

    @staticmethod
    def phase_change():
        compare_system.equal("熔化", "相變", "固態變成液態", "答案")
        compare_system.equal("凝固", "相變", "液態變成固態", "答案")
        compare_system.equal("汽化", "相變", "液態變成氣態", "答案")
        compare_system.equal("凝結", "相變", "氣態變成液態", "答案")
        compare_system.equal("昇華", "相變", "固態直接變成氣態", "答案")
        compare_system.equal("凝華", "相變", "氣態直接變成固態", "答案")
        compare_system.equal("熔化與汽化", "能量變化", "通常吸收能量", "答案")
        compare_system.equal("凝固與凝結", "能量變化", "通常放出能量", "答案")

    @staticmethod
    def density():
        compare_system.equivalentto("密度", "物理量", "單位體積所含的質量", "定義")
        compare_system.calculatedby("密度", "公式", "ρ = m ÷ V", "答案")
        compare_system.calculatedby("質量", "公式", "m = ρV", "答案")
        compare_system.calculatedby("體積", "公式", "V = m ÷ ρ", "答案")
        compare_system.equal("密度的 SI 單位", "題目", "kg/m³", "答案")
        compare_system.equal("常用密度單位", "題目", "g/cm³", "答案")
        compare_system.equal("質量 20 g、體積 5 cm³", "題目", "密度為 4 g/cm³", "答案")
        compare_system.notequal("同一純物質的密度", "敘述", "會因取樣量不同而改變", "錯誤觀念")

    @staticmethod
    def filtration():
        compare_system.equivalentto("過濾", "分離方法", "利用粒子大小差異分離不溶性固體與液體", "定義")
        compare_system.equal("泥水", "適合分離方法", "過濾", "答案")
        compare_system.equal("濾紙上留下的固體", "名稱", "濾渣", "答案")
        compare_system.equal("通過濾紙的液體", "名稱", "濾液", "答案")
        compare_system.notequal("食鹽水", "敘述", "可用普通濾紙分離出溶解的食鹽", "錯誤觀念")
        compare_system.equal("過濾", "主要依據", "不溶性固體顆粒與濾紙孔徑的差異", "答案")

    @staticmethod
    def distillation():
        compare_system.equivalentto("蒸餾", "分離方法", "利用物質沸點不同進行汽化與凝結分離", "定義")
        compare_system.equal("食鹽水取得純水", "適合方法", "蒸餾", "答案")
        compare_system.equal("蒸餾先發生", "步驟", "較易揮發成分汽化", "答案")
        compare_system.equal("冷凝管", "用途", "使蒸氣冷卻凝結成液體", "答案")
        compare_system.equal("原油分餾", "主要依據", "各成分沸點範圍不同", "答案")
        compare_system.notequal("蒸餾", "敘述", "只能分離固體與液體", "錯誤觀念")

    @staticmethod
    def chromatography():
        compare_system.equivalentto("色層分析", "分離方法", "利用各成分在固定相與移動相中的作用差異分離", "定義")
        compare_system.equal("墨水色素分離", "適合方法", "紙色層分析", "答案")
        compare_system.equal("移動速度不同", "原因", "各成分對溶劑與固定相的親和力不同", "答案")
        compare_system.equal("色層分析", "用途", "分離或初步鑑定混合物成分", "答案")
        compare_system.notequal("單一色點", "敘述", "一定代表物質絕對純淨", "錯誤觀念")
        compare_system.equal("溶劑前緣", "實驗要求", "通常需在溶劑蒸乾前標記", "答案")