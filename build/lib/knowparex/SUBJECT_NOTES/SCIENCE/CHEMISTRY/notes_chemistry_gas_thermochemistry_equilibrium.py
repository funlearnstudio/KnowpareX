# ===========================================
# notes_chemistry_gas_thermochemistry_equilibrium.py
# 化學：氣體、反應熱、速率與平衡
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_gas_thermochemistry_equilibrium:

    @staticmethod
    def gas_pressure():
        compare_system.equivalentto("氣體壓力", "物理量", "氣體粒子碰撞容器壁所形成的單位面積作用力", "定義")
        compare_system.equal("氣體粒子運動加快", "定容條件", "碰撞更頻繁且更強，壓力增加", "答案")
        compare_system.equal("氣體莫耳數增加", "定容定溫", "壓力增加", "答案")
        compare_system.equal("容器體積減小", "定溫定量", "壓力增加", "答案")
        compare_system.equal("壓力 SI 單位", "題目", "帕斯卡（Pa）", "答案")
        compare_system.equal("常見氣體壓力單位", "題目", "atm、kPa、mmHg", "答案")
        compare_system.notequal("氣體壓力", "敘述", "只作用於容器底部", "錯誤觀念")

    @staticmethod
    def boyle_law():
        compare_system.equivalentto("波以耳定律", "氣體定律", "定溫定量氣體壓力與體積成反比", "定義")
        compare_system.calculatedby("波以耳定律", "公式", "P₁V₁ = P₂V₂", "答案")
        compare_system.equal("體積減為一半", "定溫定量", "壓力增為 2 倍", "答案")
        compare_system.equal("體積增為 3 倍", "定溫定量", "壓力變為 1/3", "答案")
        compare_system.equal("P-V 圖", "波以耳定律", "反比曲線", "答案")
        compare_system.notequal("波以耳定律", "敘述", "溫度改變時仍可直接忽略溫度影響", "錯誤觀念")

    @staticmethod
    def charles_law():
        compare_system.equivalentto("查理定律", "氣體定律", "定壓定量氣體體積與絕對溫度成正比", "定義")
        compare_system.calculatedby("查理定律", "公式", "V₁/T₁ = V₂/T₂", "答案")
        compare_system.equal("絕對溫度增加為 2 倍", "定壓定量", "體積增加為 2 倍", "答案")
        compare_system.equal("氣體定律中的溫度", "要求", "使用克耳文 K", "答案")
        compare_system.equal("攝氏溫度轉 K", "公式", "T = t + 273.15", "答案")
        compare_system.notequal("查理定律", "敘述", "可直接用攝氏溫度比例計算", "錯誤觀念")

    @staticmethod
    def gay_lussac_law():
        compare_system.equivalentto("給呂薩克定律", "氣體定律", "定容定量氣體壓力與絕對溫度成正比", "定義")
        compare_system.calculatedby("給呂薩克定律", "公式", "P₁/T₁ = P₂/T₂", "答案")
        compare_system.equal("絕對溫度增加", "定容定量", "壓力增加", "答案")
        compare_system.equal("密閉剛性容器加熱", "可能結果", "內部氣體壓力上升", "答案")
        compare_system.notequal("定容加熱氣體", "敘述", "壓力保持不變", "錯誤觀念")

    @staticmethod
    def avogadro_law():
        compare_system.equivalentto("亞佛加厥定律", "氣體定律", "同溫同壓下氣體體積與莫耳數成正比", "定義")
        compare_system.equal("同溫同壓下相同體積氣體", "關係", "含有相同數目的分子", "答案")
        compare_system.equal("氣體莫耳數增加為 2 倍", "定溫定壓", "體積增加為 2 倍", "答案")
        compare_system.calculatedby("亞佛加厥定律", "公式", "V₁/n₁ = V₂/n₂", "答案")
        compare_system.notequal("相同體積不同氣體", "敘述", "在任何溫壓下粒子數都相同", "錯誤觀念")

    @staticmethod
    def ideal_gas():
        compare_system.calculatedby("理想氣體方程式", "公式", "PV = nRT", "答案")
        compare_system.equal("P", "理想氣體式", "壓力", "答案")
        compare_system.equal("V", "理想氣體式", "體積", "答案")
        compare_system.equal("n", "理想氣體式", "莫耳數", "答案")
        compare_system.equal("T", "理想氣體式", "絕對溫度", "答案")
        compare_system.equal("R", "理想氣體式", "氣體常數", "答案")
        compare_system.equal("理想氣體近似較佳", "一般條件", "低壓高溫", "答案")
        compare_system.notequal("所有真實氣體", "敘述", "在所有條件下都完全符合理想氣體模型", "錯誤觀念")

    @staticmethod
    def partial_pressure():
        compare_system.equivalentto("道耳頓分壓定律", "氣體定律", "非反應性混合氣體總壓等於各氣體分壓總和", "定義")
        compare_system.calculatedby("總壓", "公式", "P總 = P₁ + P₂ + ⋯", "答案")
        compare_system.calculatedby("分壓", "莫耳分率公式", "Pᵢ = XᵢP總", "答案")
        compare_system.equal("氣體莫耳分率", "公式", "Xᵢ = nᵢ/n總", "答案")
        compare_system.equal("兩氣體分壓各 0.4 atm 與 0.6 atm", "總壓", "1.0 atm", "答案")
        compare_system.notequal("混合氣體總壓", "敘述", "等於各氣體體積直接相加", "錯誤觀念")

    @staticmethod
    def thermochemistry():
        compare_system.equivalentto("熱化學", "化學領域", "研究化學反應與物理變化中能量變化的領域", "定義")
        compare_system.equivalentto("系統", "熱力學", "研究時選定的物質或空間", "定義")
        compare_system.equivalentto("環境", "熱力學", "系統以外的部分", "定義")
        compare_system.equal("系統吸熱", "環境", "環境放熱", "答案")
        compare_system.equal("系統放熱", "環境", "環境吸熱", "答案")
        compare_system.notequal("熱量", "敘述", "是系統本身固定儲存的一種物質", "錯誤觀念")

    @staticmethod
    def endothermic_exothermic():
        compare_system.equivalentto("吸熱反應", "反應", "系統由環境吸收熱量的反應", "定義")
        compare_system.equivalentto("放熱反應", "反應", "系統向環境放出熱量的反應", "定義")
        compare_system.equal("吸熱反應 ΔH", "符號", "大於 0", "答案")
        compare_system.equal("放熱反應 ΔH", "符號", "小於 0", "答案")
        compare_system.equal("燃燒", "一般熱效應", "放熱", "答案")
        compare_system.equal("光合作用", "能量需求", "需要吸收能量", "答案")
        compare_system.notequal("環境溫度下降", "敘述", "系統一定在放熱", "錯誤觀念")

    @staticmethod
    def enthalpy():
        compare_system.equivalentto("焓", "熱力學狀態函數", "定壓條件下常用於描述系統能量變化的量", "定義")
        compare_system.calculatedby("反應焓變", "公式", "ΔH = H生成物 - H反應物", "答案")
        compare_system.equal("ΔH < 0", "反應分類", "放熱反應", "答案")
        compare_system.equal("ΔH > 0", "反應分類", "吸熱反應", "答案")
        compare_system.equal("反應逆向進行", "焓變", "大小相同、符號相反", "答案")
        compare_system.equal("方程式係數全部乘 2", "焓變", "也乘 2", "答案")
        compare_system.notequal("焓", "敘述", "可以直接測量系統的絕對值", "錯誤觀念")

    @staticmethod
    def hess_law():
        compare_system.equivalentto("赫斯定律", "熱化學定律", "總反應焓變只與初態和終態有關", "定義")
        compare_system.equal("反應分成多步進行", "焓變", "各步驟焓變相加等於總焓變", "答案")
        compare_system.equal("將方程式反向", "操作", "ΔH 改變正負號", "答案")
        compare_system.equal("將方程式乘以 n", "操作", "ΔH 也乘以 n", "答案")
        compare_system.equal("赫斯定律成立原因", "題目", "焓是狀態函數", "答案")
        compare_system.notequal("反應路徑不同", "敘述", "總焓變一定不同", "錯誤觀念")

    @staticmethod
    def bond_energy():
        compare_system.equivalentto("鍵能", "能量", "氣相中斷裂 1 mol 特定化學鍵所需的平均能量", "定義")
        compare_system.equal("斷裂化學鍵", "能量變化", "吸收能量", "答案")
        compare_system.equal("形成化學鍵", "能量變化", "放出能量", "答案")
        compare_system.calculatedby("反應焓近似值", "鍵能公式", "Σ斷鍵能 - Σ成鍵能", "答案")
        compare_system.equal("較強化學鍵", "一般特徵", "鍵能較大", "答案")
        compare_system.notequal("鍵能表", "敘述", "對任何分子都提供完全精確相同的鍵能", "錯誤觀念")

    @staticmethod
    def reaction_rate():
        compare_system.equivalentto("反應速率", "物理量", "反應物消耗或生成物形成的快慢", "定義")
        compare_system.calculatedby("平均反應速率", "概念公式", "濃度變化量 ÷ 時間變化量", "答案")
        compare_system.equal("反應物濃度增加", "一般結果", "反應速率增加", "答案")
        compare_system.equal("溫度升高", "一般結果", "反應速率增加", "答案")
        compare_system.equal("固體表面積增加", "一般結果", "反應速率增加", "答案")
        compare_system.equal("加入催化劑", "一般結果", "反應速率增加", "答案")
        compare_system.notequal("反應速率快", "敘述", "代表生成物平衡量一定較多", "錯誤觀念")

    @staticmethod
    def collision_theory():
        compare_system.equivalentto("碰撞理論", "反應模型", "粒子必須有效碰撞才能發生反應", "定義")
        compare_system.equal("有效碰撞條件之一", "題目", "碰撞能量足夠", "答案")
        compare_system.equal("有效碰撞條件之二", "題目", "碰撞方向適當", "答案")
        compare_system.equal("溫度升高", "微觀影響", "高能粒子比例增加", "答案")
        compare_system.equal("濃度升高", "微觀影響", "單位時間碰撞次數增加", "答案")
        compare_system.notequal("所有粒子碰撞", "敘述", "都一定形成生成物", "錯誤觀念")

    @staticmethod
    def activation_energy():
        compare_system.equivalentto("活化能", "能量", "反應粒子形成有效碰撞所需克服的最低能量障礙", "定義")
        compare_system.equal("活化能較低", "一般結果", "反應通常較快", "答案")
        compare_system.equal("催化劑", "作用", "提供活化能較低的替代反應路徑", "答案")
        compare_system.equal("催化劑", "對反應焓", "不改變", "答案")
        compare_system.equal("催化劑", "對平衡常數", "不改變", "答案")
        compare_system.equal("催化劑", "對正逆反應", "通常都加速", "答案")
        compare_system.notequal("催化劑", "敘述", "會在反應中被永久大量消耗", "錯誤觀念")

    @staticmethod
    def equilibrium():
        compare_system.equivalentto("化學平衡", "狀態", "可逆反應正逆反應速率相等的動態狀態", "定義")
        compare_system.equal("平衡時正反應速率", "關係", "等於逆反應速率", "答案")
        compare_system.equal("平衡時各物質濃度", "特徵", "保持固定但不一定相等", "答案")
        compare_system.equivalentto("動態平衡", "概念", "微觀反應持續但宏觀量保持不變", "定義")
        compare_system.equal("密閉系統", "化學平衡", "通常是建立平衡的重要條件", "答案")
        compare_system.notequal("達到平衡", "敘述", "反應完全停止", "錯誤觀念")
        compare_system.notequal("達到平衡", "敘述", "反應物與生成物濃度一定相同", "錯誤觀念")

    @staticmethod
    def equilibrium_constant():
        compare_system.equivalentto("平衡常數", "物理量", "固定溫度下平衡組成依方程式係數形成的比值", "定義")
        compare_system.equal("平衡常數 K 很大", "一般意義", "平衡較偏向生成物", "答案")
        compare_system.equal("平衡常數 K 很小", "一般意義", "平衡較偏向反應物", "答案")
        compare_system.equal("平衡常數", "主要影響因素", "溫度", "答案")
        compare_system.equal("加入催化劑", "對 K", "不改變", "答案")
        compare_system.equal("改變濃度", "對固定溫度的 K", "不改變", "答案")
        compare_system.notequal("K 很大", "敘述", "代表反應速率一定很快", "錯誤觀念")

    @staticmethod
    def le_chatelier():
        compare_system.equivalentto("勒沙特列原理", "平衡原理", "平衡系統受擾動後會朝減弱擾動的方向移動", "定義")
        compare_system.equal("增加反應物濃度", "一般結果", "平衡向消耗反應物方向移動", "答案")
        compare_system.equal("移除生成物", "一般結果", "平衡向生成物方向移動", "答案")
        compare_system.equal("氣體反應加壓", "一般結果", "平衡偏向氣體莫耳數較少的一側", "答案")
        compare_system.equal("放熱反應升高溫度", "一般結果", "平衡偏向吸熱的逆反應方向", "答案")
        compare_system.equal("加入催化劑", "平衡位置", "不改變", "答案")
        compare_system.notequal("平衡移動", "敘述", "平衡常數一定改變", "錯誤觀念")