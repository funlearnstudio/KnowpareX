# ===========================================
# notes_biology_ecology_plant.py
# 生物：植物、生態系與環境
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class biology_ecology_plant:

    @staticmethod
    def plant_tissue():
        compare_system.equal("植物表皮組織", "主要功能", "保護並減少水分散失", "答案")
        compare_system.equal("分生組織", "主要功能", "細胞持續分裂使植物生長", "答案")
        compare_system.equal("木質部", "主要功能", "運輸水與無機鹽", "答案")
        compare_system.equal("韌皮部", "主要功能", "運輸糖等有機養分", "答案")
        compare_system.equal("葉肉組織", "主要功能", "進行光合作用", "答案")
        compare_system.equal("保衛細胞", "功能", "控制氣孔開閉", "答案")
        compare_system.notequal("木質部", "敘述", "主要向下運輸蔗糖", "錯誤觀念")

    @staticmethod
    def root():
        compare_system.equivalentto("根", "植物器官", "固定植物並吸收水與無機鹽的器官", "定義")
        compare_system.equal("根毛", "作用", "增加吸收水與礦物質的表面積", "答案")
        compare_system.equal("根冠", "功能", "保護根尖分生組織", "答案")
        compare_system.equal("根尖分生區", "功能", "細胞分裂", "答案")
        compare_system.equal("根的伸長區", "功能", "細胞伸長使根增長", "答案")
        compare_system.equal("根部吸收水", "主要方式之一", "滲透作用", "答案")
        compare_system.equal("礦物離子吸收", "可能方式", "主動運輸", "答案")
        compare_system.notequal("根", "敘述", "只能吸收純水而不能吸收礦物離子", "錯誤觀念")

    @staticmethod
    def stem():
        compare_system.equivalentto("莖", "植物器官", "支持葉與花並負責物質運輸的器官", "定義")
        compare_system.equal("莖的木質部", "功能", "運輸水與礦物質", "答案")
        compare_system.equal("莖的韌皮部", "功能", "運輸光合作用產物", "答案")
        compare_system.equal("草本莖", "一般特徵", "木質化程度較低", "答案")
        compare_system.equal("木本莖", "一般特徵", "次生生長與木質化較明顯", "答案")
        compare_system.equal("形成層", "功能", "產生次生木質部與次生韌皮部", "答案")
        compare_system.notequal("植物莖", "敘述", "只負責支持而不參與運輸", "錯誤觀念")

    @staticmethod
    def leaf():
        compare_system.equivalentto("葉", "植物器官", "主要進行光合作用、氣體交換與蒸散的器官", "定義")
        compare_system.equal("柵狀葉肉", "一般特徵", "葉綠體多且光合作用旺盛", "答案")
        compare_system.equal("海綿葉肉", "一般特徵", "細胞間隙較多以利氣體交換", "答案")
        compare_system.equal("氣孔", "功能", "進行氣體交換與水氣散失", "答案")
        compare_system.equal("葉脈", "組成", "木質部與韌皮部", "答案")
        compare_system.equal("上表皮角質層", "功能", "減少水分散失", "答案")
        compare_system.notequal("葉片", "敘述", "只在白天進行呼吸作用", "錯誤觀念")

    @staticmethod
    def transpiration():
        compare_system.equivalentto("蒸散作用", "植物生理", "水由植物表面以水氣形式散失的過程", "定義")
        compare_system.equal("蒸散主要位置", "題目", "葉片氣孔", "答案")
        compare_system.equal("蒸散拉力", "作用", "協助水由根沿木質部向上移動", "答案")
        compare_system.equal("溫度升高", "一般結果", "蒸散速率增加", "答案")
        compare_system.equal("空氣濕度升高", "一般結果", "蒸散速率降低", "答案")
        compare_system.equal("風速增加", "一般結果", "蒸散速率通常增加", "答案")
        compare_system.equal("氣孔關閉", "結果", "蒸散與 CO₂ 進入都減少", "答案")
        compare_system.notequal("蒸散作用", "敘述", "對植物完全沒有任何功能", "錯誤觀念")

    @staticmethod
    def plant_transport():
        compare_system.equal("木質部運輸方向", "一般情況", "主要由根向上", "答案")
        compare_system.equal("木質部運輸物質", "題目", "水與無機鹽", "答案")
        compare_system.equal("韌皮部運輸物質", "題目", "蔗糖等有機物", "答案")
        compare_system.equal("韌皮部運輸方向", "一般情況", "由來源器官運向需求或儲存器官", "答案")
        compare_system.equivalentto("來源", "植物運輸", "製造或釋出糖的部位", "定義")
        compare_system.equivalentto("庫", "植物運輸", "消耗或儲存糖的部位", "定義")
        compare_system.notequal("韌皮部", "敘述", "只會由上往下運輸", "錯誤觀念")

    @staticmethod
    def tropism():
        compare_system.equivalentto("向性", "植物反應", "植物生長方向受刺激方向影響的反應", "定義")
        compare_system.equal("向光性", "刺激", "光", "答案")
        compare_system.equal("向地性", "刺激", "重力", "答案")
        compare_system.equal("向觸性", "刺激", "接觸", "答案")
        compare_system.equal("莖", "向光性", "通常為正向光性", "答案")
        compare_system.equal("根", "向地性", "通常為正向地性", "答案")
        compare_system.equal("生長素分布不均", "結果", "可能造成器官彎曲生長", "答案")
        compare_system.notequal("向性", "敘述", "是植物快速移動整個身體的位置", "錯誤觀念")

    @staticmethod
    def flower():
        compare_system.equivalentto("花", "植物生殖器官", "被子植物進行有性生殖的重要器官", "定義")
        compare_system.equal("雄蕊", "組成", "花藥與花絲", "答案")
        compare_system.equal("花藥", "功能", "產生花粉", "答案")
        compare_system.equal("雌蕊", "組成", "柱頭、花柱與子房", "答案")
        compare_system.equal("胚珠", "位置", "子房內", "答案")
        compare_system.equal("花瓣", "可能功能", "吸引傳粉者", "答案")
        compare_system.equal("萼片", "主要功能", "保護花苞", "答案")
        compare_system.notequal("所有花", "敘述", "都具有鮮豔花瓣與香味", "錯誤觀念")

    @staticmethod
    def pollination_fertilization():
        compare_system.equivalentto("傳粉", "植物生殖", "花粉由花藥到達柱頭的過程", "定義")
        compare_system.equivalentto("受精", "植物生殖", "精細胞與卵細胞結合形成合子的過程", "定義")
        compare_system.equal("風媒花", "常見特徵", "花粉多且輕、花朵不一定鮮豔", "答案")
        compare_system.equal("蟲媒花", "常見特徵", "常有顏色、氣味或花蜜吸引昆蟲", "答案")
        compare_system.equal("被子植物花粉管", "功能", "將精細胞送至胚珠", "答案")
        compare_system.equal("雙重受精", "被子植物", "形成合子與胚乳", "答案")
        compare_system.notequal("傳粉", "概念", "已經完成精卵結合", "錯誤觀念")

    @staticmethod
    def seed_fruit():
        compare_system.equal("胚珠受精後", "發育", "形成種子", "答案")
        compare_system.equal("子房受精後", "一般發育", "形成果實", "答案")
        compare_system.equal("合子", "發育", "形成胚", "答案")
        compare_system.equal("胚乳", "主要功能", "提供或儲存胚發育所需養分", "答案")
        compare_system.equal("種皮", "來源之一", "胚珠外層構造", "答案")
        compare_system.equal("果實", "功能之一", "保護種子並協助散播", "答案")
        compare_system.notequal("所有可食果肉", "敘述", "都只由子房壁形成", "錯誤觀念")

    @staticmethod
    def germination():
        compare_system.equivalentto("萌發", "植物生長", "種子恢復生長並形成幼苗的過程", "定義")
        compare_system.equal("種子萌發基本條件", "題目", "適量水、氧氣與適宜溫度", "答案")
        compare_system.equal("水", "萌發作用", "活化代謝並使種子膨脹", "答案")
        compare_system.equal("氧氣", "萌發作用", "供細胞呼吸", "答案")
        compare_system.equal("胚根", "萌發順序", "通常先突破種皮", "答案")
        compare_system.equal("萌發初期能量來源", "題目", "種子儲存養分", "答案")
        compare_system.notequal("所有種子萌發", "敘述", "都必須立刻照光", "錯誤觀念")

    @staticmethod
    def ecology_levels():
        compare_system.equivalentto("個體", "生態層次", "一個生物", "定義")
        compare_system.equivalentto("族群", "生態層次", "同一地區同一物種的所有個體", "定義")
        compare_system.equivalentto("群集", "生態層次", "同一地區所有不同生物族群", "定義")
        compare_system.equivalentto("生態系", "生態層次", "群集與非生物環境及其交互作用", "定義")
        compare_system.equivalentto("生物圈", "生態層次", "地球上所有生態系的總和", "定義")
        compare_system.notequal("族群", "敘述", "包含同地區所有不同物種", "錯誤觀念")

    @staticmethod
    def habitat_niche():
        compare_system.equivalentto("棲地", "生態概念", "生物居住的環境位置", "定義")
        compare_system.equivalentto("生態棲位", "生態概念", "物種在生態系中的角色與資源使用方式", "定義")
        compare_system.equal("棲地", "比喻", "生物的地址", "答案")
        compare_system.equal("棲位", "比喻", "生物的職業與生活方式", "答案")
        compare_system.equal("兩物種棲位高度重疊", "可能結果", "競爭加劇", "答案")
        compare_system.notequal("棲地相同", "敘述", "棲位一定完全相同", "錯誤觀念")

    @staticmethod
    def population_growth():
        compare_system.equal("族群大小變化", "主要因素", "出生、死亡、遷入與遷出", "答案")
        compare_system.equivalentto("指數成長", "族群模型", "資源充足時成長率隨族群增加", "定義")
        compare_system.equivalentto("邏輯斯成長", "族群模型", "成長逐漸受環境負荷量限制", "定義")
        compare_system.equivalentto("環境負荷量", "生態概念", "環境能長期支持的最大族群量", "定義")
        compare_system.equal("資源減少", "可能結果", "族群成長率下降", "答案")
        compare_system.equal("密度制約因素", "例子", "疾病、競爭與捕食", "答案")
        compare_system.notequal("環境負荷量", "敘述", "永遠固定不變", "錯誤觀念")

    @staticmethod
    def interaction():
        compare_system.equivalentto("競爭", "生物交互作用", "生物爭奪有限資源而彼此受不利影響", "定義")
        compare_system.equivalentto("捕食", "生物交互作用", "捕食者捕捉並食用獵物", "定義")
        compare_system.equivalentto("寄生", "生物交互作用", "寄生者受益而宿主受害", "定義")
        compare_system.equivalentto("互利共生", "生物交互作用", "雙方皆受益", "定義")
        compare_system.equivalentto("片利共生", "生物交互作用", "一方受益而另一方影響不明顯", "定義")
        compare_system.equal("蜜蜂與開花植物", "交互作用", "常為互利關係", "答案")
        compare_system.equal("蛔蟲與人體", "交互作用", "寄生", "答案")
        compare_system.notequal("寄生者", "敘述", "通常會立即殺死所有宿主", "錯誤觀念")

    @staticmethod
    def food_chain_web():
        compare_system.equivalentto("食物鏈", "生態關係", "能量與物質沿取食關係傳遞的線性表示", "定義")
        compare_system.equivalentto("食物網", "生態關係", "多條食物鏈彼此交錯形成的網絡", "定義")
        compare_system.equal("食物鏈箭頭方向", "意義", "能量與物質傳遞方向", "答案")
        compare_system.equal("植物 → 蝗蟲 → 青蛙", "青蛙角色", "次級消費者", "答案")
        compare_system.equal("食物網", "優點", "較真實呈現複雜取食關係", "答案")
        compare_system.notequal("食物鏈箭頭", "敘述", "由捕食者指向被吃者", "錯誤觀念")

    @staticmethod
    def trophic_level():
        compare_system.equivalentto("生產者", "營養階層", "利用無機物製造有機物的生物", "定義")
        compare_system.equivalentto("消費者", "營養階層", "直接或間接攝食其他生物取得能量", "定義")
        compare_system.equivalentto("分解者", "營養角色", "分解遺體與排遺並回收物質", "定義")
        compare_system.equal("綠色植物", "角色", "生產者", "答案")
        compare_system.equal("草食動物", "角色", "初級消費者", "答案")
        compare_system.equal("真菌與許多細菌", "角色", "分解者", "答案")
        compare_system.notequal("分解者", "敘述", "不屬於生態系的重要成員", "錯誤觀念")

    @staticmethod
    def energy_pyramid():
        compare_system.equivalentto("能量金字塔", "生態模型", "顯示各營養階層可用能量逐級減少", "定義")
        compare_system.equal("能量進入多數生態系", "主要來源", "太陽光", "答案")
        compare_system.equal("營養階層上升", "可用能量", "減少", "答案")
        compare_system.equal("能量傳遞效率", "一般情況", "只有部分能量傳至下一階層", "答案")
        compare_system.equal("大量能量", "去向", "代謝後以熱散失", "答案")
        compare_system.equal("食物鏈長度", "限制因素之一", "高階營養層可用能量少", "答案")
        compare_system.notequal("能量", "敘述", "在生態系中像物質一樣完整循環", "錯誤觀念")

    @staticmethod
    def carbon_cycle():
        compare_system.equivalentto("碳循環", "物質循環", "碳在大氣、生物、海洋與岩石圈間移動的過程", "定義")
        compare_system.equal("光合作用", "碳循環", "將 CO₂ 固定為有機物", "答案")
        compare_system.equal("呼吸作用", "碳循環", "釋放 CO₂", "答案")
        compare_system.equal("分解作用", "碳循環", "將有機碳釋回環境", "答案")
        compare_system.equal("化石燃料燃燒", "結果", "增加大氣 CO₂", "答案")
        compare_system.equal("海洋", "碳循環", "可吸收與儲存大量碳", "答案")
        compare_system.notequal("碳循環", "敘述", "只發生於生物體內", "錯誤觀念")

    @staticmethod
    def nitrogen_cycle():
        compare_system.equivalentto("固氮作用", "氮循環", "將大氣 N₂ 轉為生物可利用含氮化合物", "定義")
        compare_system.equal("根瘤菌", "作用", "固氮", "答案")
        compare_system.equal("硝化作用", "結果", "將氨或銨轉為亞硝酸鹽與硝酸鹽", "答案")
        compare_system.equal("反硝化作用", "結果", "將硝酸鹽轉回 N₂", "答案")
        compare_system.equal("植物", "氮取得", "吸收土壤中的銨鹽或硝酸鹽", "答案")
        compare_system.equal("動物", "氮取得", "攝食含蛋白質或核酸的生物", "答案")
        compare_system.notequal("多數植物", "敘述", "可直接吸收大氣 N₂ 使用", "錯誤觀念")

    @staticmethod
    def succession():
        compare_system.equivalentto("生態演替", "生態過程", "群集組成隨時間逐漸改變的過程", "定義")
        compare_system.equivalentto("初級演替", "演替種類", "由缺乏土壤的裸露環境開始", "定義")
        compare_system.equivalentto("次級演替", "演替種類", "原群集受干擾但土壤仍保留", "定義")
        compare_system.equal("火山新生岩地", "演替", "初級演替", "答案")
        compare_system.equal("森林火災後土壤仍在", "演替", "次級演替", "答案")
        compare_system.equal("先驅物種", "作用", "最早建立並改變環境", "答案")
        compare_system.notequal("生態演替", "敘述", "必定朝唯一且永遠不變的終點前進", "錯誤觀念")

    @staticmethod
    def biodiversity():
        compare_system.equivalentto("生物多樣性", "生態概念", "基因、物種與生態系多樣性的總稱", "定義")
        compare_system.equal("基因多樣性", "意義", "同物種內遺傳差異", "答案")
        compare_system.equal("物種多樣性", "意義", "物種種類與分布均勻程度", "答案")
        compare_system.equal("生態系多樣性", "意義", "不同棲地與生態系種類", "答案")
        compare_system.equal("生物多樣性高", "可能優點", "提高生態系面對擾動的韌性", "答案")
        compare_system.equal("棲地破壞", "影響", "生物多樣性下降", "答案")
        compare_system.notequal("生物多樣性", "敘述", "只等於物種數量", "錯誤觀念")

    @staticmethod
    def conservation():
        compare_system.equivalentto("保育", "環境行動", "維護物種、棲地與生態系功能的行動", "定義")
        compare_system.equal("就地保育", "方式", "在原生棲地保護物種", "答案")
        compare_system.equal("移地保育", "方式", "在動物園、植物園或種原庫保存", "答案")
        compare_system.equal("建立保護區", "保育類型", "就地保育", "答案")
        compare_system.equal("種子庫", "保育類型", "移地保育", "答案")
        compare_system.equal("外來入侵種", "可能影響", "競爭、捕食或改變本地生態系", "答案")
        compare_system.notequal("保育", "敘述", "代表完全禁止人類使用任何自然資源", "錯誤觀念")