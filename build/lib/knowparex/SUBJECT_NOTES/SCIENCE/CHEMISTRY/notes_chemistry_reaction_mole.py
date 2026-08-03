# ===========================================
# notes_chemistry_reaction_mole.py
# 化學：反應、方程式與莫耳
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_reaction_mole:

    @staticmethod
    def chemical_reaction():
        compare_system.equivalentto("化學反應", "化學變化", "反應物重新排列形成生成物的過程", "定義")
        compare_system.equal("化學反應中原子", "基本原則", "重新排列但不憑空產生或消失", "答案")
        compare_system.equal("反應物", "位置", "化學方程式箭頭左側", "答案")
        compare_system.equal("生成物", "位置", "化學方程式箭頭右側", "答案")
        compare_system.equal("化學反應", "可能現象", "產生氣體、沉澱、光、熱或顏色變化", "答案")
        compare_system.notequal("沒有明顯現象", "敘述", "一定沒有發生化學反應", "錯誤觀念")

    @staticmethod
    def conservation_of_mass():
        compare_system.equivalentto("質量守恆定律", "化學定律", "密閉系統中反應前後總質量相等", "定義")
        compare_system.equal("反應前總質量", "密閉系統", "等於反應後總質量", "答案")
        compare_system.equal("化學反應中元素種類", "關係", "反應前後相同", "答案")
        compare_system.equal("化學反應中各元素原子總數", "關係", "反應前後相同", "答案")
        compare_system.equal("開放容器反應後質量減少", "可能原因", "氣體離開系統", "答案")
        compare_system.notequal("生成氣體後天平讀數變小", "敘述", "代表質量被消滅", "錯誤觀念")

    @staticmethod
    def balancing_equation():
        compare_system.equivalentto("平衡化學方程式", "操作", "調整係數使各元素原子數在反應前後相等", "定義")
        compare_system.equal("平衡方程式時可改變", "題目", "係數", "答案")
        compare_system.equal("平衡方程式時不可任意改變", "題目", "化學式下標", "答案")
        compare_system.equal("H₂ + O₂ → H₂O", "平衡結果", "2H₂ + O₂ → 2H₂O", "答案")
        compare_system.equal("N₂ + H₂ → NH₃", "平衡結果", "N₂ + 3H₂ → 2NH₃", "答案")
        compare_system.equal("係數", "意義", "反應物與生成物的粒子數或莫耳數比例", "答案")
        compare_system.notequal("平衡化學方程式", "敘述", "代表反應物全部一定完全反應", "錯誤觀念")

    @staticmethod
    def reaction_type():
        compare_system.equivalentto("化合反應", "反應類型", "兩種以上物質形成較少種類生成物", "定義")
        compare_system.equivalentto("分解反應", "反應類型", "一種物質分解成兩種以上物質", "定義")
        compare_system.equivalentto("單置換反應", "反應類型", "一元素取代化合物中的另一元素", "定義")
        compare_system.equivalentto("複分解反應", "反應類型", "兩化合物交換離子形成新物質", "定義")
        compare_system.equal("2H₂ + O₂ → 2H₂O", "反應類型", "化合反應", "答案")
        compare_system.equal("2H₂O₂ → 2H₂O + O₂", "反應類型", "分解反應", "答案")
        compare_system.equal("Zn + 2HCl → ZnCl₂ + H₂", "反應類型", "單置換反應", "答案")
        compare_system.equal("AgNO₃ + NaCl → AgCl + NaNO₃", "反應類型", "複分解反應", "答案")

    @staticmethod
    def combustion():
        compare_system.equivalentto("燃燒", "反應", "物質與氧化劑快速反應並放出能量的過程", "定義")
        compare_system.equal("完全燃燒碳氫化合物", "主要生成物", "CO₂ 與 H₂O", "答案")
        compare_system.equal("氧氣不足的不完全燃燒", "可能生成物", "CO 或碳煙", "答案")
        compare_system.equal("燃燒三要素", "題目", "可燃物、助燃物與達到著火溫度", "答案")
        compare_system.equal("移除燃燒三要素之一", "結果", "可以滅火", "答案")
        compare_system.equal("燃燒反應", "熱量變化", "通常為放熱反應", "答案")
        compare_system.notequal("任何物質與氧反應", "敘述", "都一定出現明顯火焰", "錯誤觀念")

    @staticmethod
    def precipitation():
        compare_system.equivalentto("沉澱反應", "反應", "水溶液中形成難溶固體的反應", "定義")
        compare_system.equal("Ag⁺ 與 Cl⁻", "反應", "形成 AgCl 沉澱", "答案")
        compare_system.equal("Ba²⁺ 與 SO₄²⁻", "反應", "形成 BaSO₄ 沉澱", "答案")
        compare_system.equal("沉澱符號", "化學方程式", "↓ 或 (s)", "答案")
        compare_system.equal("淨離子方程式", "內容", "只保留實際發生變化的離子或物質", "答案")
        compare_system.equal("Ag⁺ + Cl⁻", "淨離子方程式生成物", "AgCl(s)", "答案")
        compare_system.notequal("所有離子化合物", "敘述", "在水中都高度可溶", "錯誤觀念")

    @staticmethod
    def mole():
        compare_system.equivalentto("莫耳", "物質的量單位", "含有亞佛加厥常數個基本粒子的物質的量", "定義")
        compare_system.equal("莫耳的 SI 單位符號", "題目", "mol", "答案")
        compare_system.approximatelyequal("亞佛加厥常數", "數值", "6.022 × 10²³ mol⁻¹", "答案")
        compare_system.equal("1 mol 水分子", "粒子數", "約 6.022 × 10²³ 個水分子", "答案")
        compare_system.equal("2 mol 原子", "粒子數", "約 1.2044 × 10²⁴ 個原子", "答案")
        compare_system.notequal("莫耳", "概念", "質量單位", "錯誤觀念")

    @staticmethod
    def particle_number():
        compare_system.calculatedby("粒子數", "公式", "N = nNₐ", "答案")
        compare_system.calculatedby("莫耳數", "公式", "n = N ÷ Nₐ", "答案")
        compare_system.equal("0.5 mol 分子", "粒子數", "約 3.011 × 10²³ 個分子", "答案")
        compare_system.equal("1 mol H₂O", "氫原子數", "約 1.2044 × 10²⁴ 個氫原子", "答案")
        compare_system.equal("1 mol CO₂", "氧原子莫耳數", "2 mol 氧原子", "答案")
        compare_system.notequal("1 mol 所有物質", "敘述", "質量都相同", "錯誤觀念")

    @staticmethod
    def molar_mass():
        compare_system.equivalentto("莫耳質量", "物理量", "每莫耳物質的質量", "定義")
        compare_system.equal("莫耳質量常用單位", "題目", "g/mol", "答案")
        compare_system.calculatedby("莫耳數", "質量公式", "n = m ÷ M", "答案")
        compare_system.calculatedby("質量", "公式", "m = nM", "答案")
        compare_system.equal("H₂O 莫耳質量", "題目", "約 18 g/mol", "答案")
        compare_system.equal("CO₂ 莫耳質量", "題目", "約 44 g/mol", "答案")
        compare_system.equal("NaCl 莫耳質量", "題目", "約 58.5 g/mol", "答案")
        compare_system.equal("36 g H₂O", "莫耳數", "約 2 mol", "答案")

    @staticmethod
    def empirical_molecular_formula():
        compare_system.equivalentto("實驗式", "化學式", "化合物中各元素原子數的最簡整數比", "定義")
        compare_system.equivalentto("分子式", "化學式", "一個分子中各元素實際原子數", "定義")
        compare_system.equal("葡萄糖分子式", "題目", "C₆H₁₂O₆", "答案")
        compare_system.equal("葡萄糖實驗式", "題目", "CH₂O", "答案")
        compare_system.equal("分子式", "關係", "是實驗式的整數倍", "答案")
        compare_system.calculatedby("倍數", "公式", "分子莫耳質量 ÷ 實驗式莫耳質量", "答案")
        compare_system.notequal("離子化合物化學式", "敘述", "一定代表單一分子的實際原子數", "錯誤觀念")

    @staticmethod
    def stoichiometry():
        compare_system.equivalentto("化學計量", "計算", "利用平衡方程式係數關係計算反應物與生成物的量", "定義")
        compare_system.equal("2H₂ + O₂ → 2H₂O", "莫耳比", "2：1：2", "答案")
        compare_system.equal("3 mol O₂ 完全反應", "所需 H₂", "6 mol", "答案")
        compare_system.equal("2 mol O₂ 完全反應", "生成 H₂O", "4 mol", "答案")
        compare_system.equal("方程式係數比", "可代表", "粒子數比與莫耳數比", "答案")
        compare_system.notequal("方程式係數比", "敘述", "通常直接等於質量比", "錯誤觀念")
        compare_system.equal("化學計量計算第一步", "方法", "先確認方程式已平衡", "答案")

    @staticmethod
    def limiting_reagent():
        compare_system.equivalentto("限量試劑", "反應物", "反應中最先完全消耗並限制生成物量的反應物", "定義")
        compare_system.equivalentto("過量試劑", "反應物", "反應完成後仍有剩餘的反應物", "定義")
        compare_system.equal("生成物理論量", "主要決定因素", "限量試劑", "答案")
        compare_system.equal("判斷限量試劑", "方法", "將各反應物量與方程式需求比例比較", "答案")
        compare_system.notequal("質量最少的反應物", "敘述", "一定是限量試劑", "錯誤觀念")
        compare_system.equal("限量試劑完全耗盡", "結果", "反應停止或無法繼續生成相同產物", "答案")

    @staticmethod
    def ex_yield():
        compare_system.equivalentto("理論產量", "產量", "依限量試劑與化學計量可得到的最大產量", "定義")
        compare_system.equivalentto("實際產量", "產量", "實驗真正取得的生成物量", "定義")
        compare_system.calculatedby("百分產率", "公式", "實際產量 ÷ 理論產量 × 100%", "答案")
        compare_system.equal("理論產量 10 g、實際產量 8 g", "題目", "百分產率為 80%", "答案")
        compare_system.equalorsmaller("一般實驗百分產率", "常見關係", "100%", "答案")
        compare_system.equal("產率低於 100%", "可能原因", "副反應、未完全反應或操作損失", "答案")
        compare_system.notequal("百分產率超過 100%", "敘述", "一定表示創造了額外物質", "錯誤觀念")