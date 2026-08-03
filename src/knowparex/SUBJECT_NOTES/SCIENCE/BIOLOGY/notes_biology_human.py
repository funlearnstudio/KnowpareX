# ===========================================
# notes_biology_human.py
# 生物：人體系統、恆定、免疫與生殖
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class biology_human:

    @staticmethod
    def organization():
        compare_system.equal("人體構造層次由小到大", "題目", "細胞、組織、器官、器官系統、個體", "答案")
        compare_system.equivalentto("組織", "構造層次", "構造與功能相似細胞形成的群體", "定義")
        compare_system.equivalentto("器官", "構造層次", "多種組織共同完成特定功能的構造", "定義")
        compare_system.equivalentto("器官系統", "構造層次", "多個器官協同完成主要生理功能", "定義")
        compare_system.equal("心臟", "層次", "器官", "答案")
        compare_system.equal("循環系統", "層次", "器官系統", "答案")
        compare_system.notequal("同一器官", "敘述", "只含一種組織", "錯誤觀念")

    @staticmethod
    def homeostasis():
        compare_system.equivalentto("恆定性", "生理概念", "維持體內環境在適當範圍的調節能力", "定義")
        compare_system.equal("人體恆定項目", "例子", "體溫、血糖、pH 與水分平衡", "答案")
        compare_system.equivalentto("負回饋", "調節機制", "反應抵消原本變化並使狀態回到設定範圍", "定義")
        compare_system.equal("體溫過高時流汗", "回饋", "負回饋", "答案")
        compare_system.equal("血糖過高時分泌胰島素", "回饋", "負回饋", "答案")
        compare_system.notequal("恆定性", "敘述", "代表所有體內數值永遠完全固定", "錯誤觀念")

    @staticmethod
    def digestive_system():
        compare_system.equivalentto("消化", "生理作用", "將大分子食物分解為可吸收小分子的過程", "定義")
        compare_system.equal("機械性消化", "例子", "咀嚼與胃的攪拌", "答案")
        compare_system.equal("化學性消化", "主要媒介", "消化酵素", "答案")
        compare_system.equal("消化道順序", "題目", "口腔、咽、食道、胃、小腸、大腸、肛門", "答案")
        compare_system.equal("小腸", "主要功能", "大部分消化與養分吸收", "答案")
        compare_system.equal("大腸", "主要功能之一", "吸收水分與形成糞便", "答案")
        compare_system.notequal("消化", "敘述", "只是把食物磨碎而不改變分子", "錯誤觀念")

    @staticmethod
    def mouth_stomach():
        compare_system.equal("唾液澱粉酶", "作用", "初步分解澱粉", "答案")
        compare_system.equal("口腔", "消化", "進行咀嚼與部分澱粉消化", "答案")
        compare_system.equal("食道蠕動", "功能", "將食團推向胃", "答案")
        compare_system.equal("胃酸", "功能", "提供酸性環境並抑制部分微生物", "答案")
        compare_system.equal("胃蛋白酶", "主要作用", "分解蛋白質", "答案")
        compare_system.equal("胃黏液", "功能", "保護胃壁免受酸與酵素傷害", "答案")
        compare_system.notequal("胃", "敘述", "是所有養分吸收的主要場所", "錯誤觀念")

    @staticmethod
    def intestine_liver_pancreas():
        compare_system.equal("小腸絨毛", "功能", "增加吸收表面積", "答案")
        compare_system.equal("胰液", "成分", "含多種消化酵素與碳酸氫根", "答案")
        compare_system.equal("膽汁", "製造器官", "肝臟", "答案")
        compare_system.equal("膽汁", "儲存器官", "膽囊", "答案")
        compare_system.equal("膽汁", "作用", "乳化脂肪以增加酵素作用面積", "答案")
        compare_system.equal("肝臟", "功能之一", "調節血糖、解毒與製造膽汁", "答案")
        compare_system.equal("胰臟", "功能", "兼具消化酵素分泌與內分泌功能", "答案")
        compare_system.notequal("膽汁", "敘述", "含脂肪酶並直接化學分解脂肪", "錯誤觀念")

    @staticmethod
    def respiratory_system():
        compare_system.equivalentto("呼吸系統", "器官系統", "進行空氣交換並協助氣體交換的系統", "定義")
        compare_system.equal("空氣通道順序", "簡化", "鼻、咽、喉、氣管、支氣管、肺泡", "答案")
        compare_system.equal("鼻腔", "功能", "過濾、溫暖與濕潤空氣", "答案")
        compare_system.equal("氣管纖毛與黏液", "功能", "攔截並排除異物", "答案")
        compare_system.equal("肺泡", "主要功能", "與微血管進行氣體交換", "答案")
        compare_system.equal("肺泡數量多", "優點", "增加氣體交換表面積", "答案")
        compare_system.notequal("肺部呼吸", "概念", "等同細胞呼吸", "錯誤觀念")

    @staticmethod
    def breathing():
        compare_system.equal("吸氣時橫膈", "動作", "收縮並下降", "答案")
        compare_system.equal("吸氣時胸腔體積", "變化", "增加", "答案")
        compare_system.equal("吸氣時肺內壓力", "變化", "低於外界大氣壓", "答案")
        compare_system.equal("呼氣時橫膈", "一般安靜呼吸", "放鬆並上升", "答案")
        compare_system.equal("呼氣時胸腔體積", "變化", "減少", "答案")
        compare_system.equal("氣體交換", "主要機制", "擴散", "答案")
        compare_system.notequal("肺", "敘述", "像幫浦一樣主動把自己充氣", "錯誤觀念")

    @staticmethod
    def gas_exchange():
        compare_system.equal("肺泡氧氣", "移動方向", "由肺泡擴散至血液", "答案")
        compare_system.equal("血液二氧化碳", "移動方向", "由血液擴散至肺泡", "答案")
        compare_system.equal("氧氣擴散", "驅動因素", "分壓差", "答案")
        compare_system.equal("紅血球血紅素", "主要功能", "攜帶氧氣", "答案")
        compare_system.equal("二氧化碳運輸", "主要形式之一", "碳酸氫根離子", "答案")
        compare_system.equal("組織微血管", "氧氣方向", "由血液擴散至組織細胞", "答案")
        compare_system.notequal("氣體交換", "敘述", "需要細胞主動運輸氧氣", "錯誤觀念")

    @staticmethod
    def circulatory_system():
        compare_system.equivalentto("循環系統", "器官系統", "運送氣體、養分、廢物、激素與熱量的系統", "定義")
        compare_system.equal("人體循環系統", "類型", "封閉式循環", "答案")
        compare_system.equal("循環系統組成", "題目", "心臟、血管與血液", "答案")
        compare_system.equal("肺循環", "路徑", "心臟與肺之間", "答案")
        compare_system.equal("體循環", "路徑", "心臟與全身組織之間", "答案")
        compare_system.equal("人體循環", "循環形式", "雙循環", "答案")
        compare_system.notequal("血液", "敘述", "會直接離開血管流入所有細胞間", "錯誤觀念")

    @staticmethod
    def heart():
        compare_system.equal("心臟腔室", "題目", "右心房、右心室、左心房、左心室", "答案")
        compare_system.equal("右心房", "接收", "來自全身的缺氧血", "答案")
        compare_system.equal("右心室", "輸出", "將血液送往肺", "答案")
        compare_system.equal("左心房", "接收", "來自肺的充氧血", "答案")
        compare_system.equal("左心室", "輸出", "將血液送往全身", "答案")
        compare_system.equal("左心室肌肉", "比較", "通常最厚", "答案")
        compare_system.equal("心臟瓣膜", "功能", "防止血液逆流", "答案")
        compare_system.notequal("動脈", "敘述", "一定運送含氧量高的血", "錯誤觀念")

    @staticmethod
    def blood_vessel():
        compare_system.equivalentto("動脈", "血管", "將血液由心臟送出的血管", "定義")
        compare_system.equivalentto("靜脈", "血管", "將血液送回心臟的血管", "定義")
        compare_system.equivalentto("微血管", "血管", "進行物質交換的細小血管", "定義")
        compare_system.equal("動脈壁", "一般特徵", "較厚且富彈性", "答案")
        compare_system.equal("靜脈", "常見構造", "具有防止逆流的瓣膜", "答案")
        compare_system.equal("微血管壁", "厚度", "通常只有一層細胞", "答案")
        compare_system.notequal("靜脈", "敘述", "永遠只運送缺氧血", "錯誤觀念")

    @staticmethod
    def blood():
        compare_system.equal("血液組成", "題目", "血漿、紅血球、白血球與血小板", "答案")
        compare_system.equal("血漿", "主要成分", "水", "答案")
        compare_system.equal("紅血球", "主要功能", "運輸氧氣", "答案")
        compare_system.equal("白血球", "主要功能", "防禦病原與免疫", "答案")
        compare_system.equal("血小板", "主要功能", "參與凝血", "答案")
        compare_system.equal("成熟紅血球", "哺乳類", "通常沒有細胞核", "答案")
        compare_system.notequal("血小板", "敘述", "是完整大型白血球", "錯誤觀念")

    @staticmethod
    def lymphatic_system():
        compare_system.equivalentto("淋巴系統", "器官系統", "回收組織液並參與免疫與脂質運輸的系統", "定義")
        compare_system.equal("淋巴管", "功能", "將多餘組織液送回血液循環", "答案")
        compare_system.equal("淋巴結", "功能", "過濾淋巴並提供免疫細胞作用場所", "答案")
        compare_system.equal("小腸乳糜管", "功能", "吸收部分脂質", "答案")
        compare_system.equal("淋巴液流動", "動力", "肌肉收縮與瓣膜協助", "答案")
        compare_system.notequal("淋巴系統", "敘述", "有像心臟一樣的中央幫浦", "錯誤觀念")

    @staticmethod
    def urinary_system():
        compare_system.equivalentto("泌尿系統", "器官系統", "排除含氮廢物並調節水、鹽與酸鹼平衡", "定義")
        compare_system.equal("泌尿系統組成", "題目", "腎臟、輸尿管、膀胱與尿道", "答案")
        compare_system.equal("腎臟", "主要功能", "過濾血液並形成尿液", "答案")
        compare_system.equal("輸尿管", "功能", "將尿液由腎臟送至膀胱", "答案")
        compare_system.equal("膀胱", "功能", "暫時儲存尿液", "答案")
        compare_system.equal("尿道", "功能", "將尿液排出體外", "答案")
        compare_system.notequal("尿液", "敘述", "直接由食物殘渣形成", "錯誤觀念")

    @staticmethod
    def nephron():
        compare_system.equivalentto("腎元", "腎臟構造", "腎臟形成尿液的基本功能單位", "定義")
        compare_system.equal("腎小球", "功能", "進行血液過濾", "答案")
        compare_system.equal("腎小囊", "功能", "接收濾液", "答案")
        compare_system.equal("腎小管", "功能", "再吸收與分泌", "答案")
        compare_system.equal("葡萄糖", "正常情況", "大部分被腎小管再吸收", "答案")
        compare_system.equal("尿素", "來源", "胺基酸分解產生的含氮廢物", "答案")
        compare_system.equal("ADH", "作用", "增加腎臟對水的再吸收", "答案")
        compare_system.notequal("腎小球濾液", "敘述", "成分完全等同最終尿液", "錯誤觀念")

    @staticmethod
    def nervous_system():
        compare_system.equivalentto("神經系統", "器官系統", "快速接收、整合資訊並控制反應的系統", "定義")
        compare_system.equal("中樞神經系統", "組成", "腦與脊髓", "答案")
        compare_system.equal("周圍神經系統", "組成", "中樞以外的神經", "答案")
        compare_system.equal("感覺神經元", "方向", "由受器傳向中樞", "答案")
        compare_system.equal("運動神經元", "方向", "由中樞傳向效應器", "答案")
        compare_system.equal("聯絡神經元", "主要位置", "中樞神經系統", "答案")
        compare_system.notequal("神經衝動", "敘述", "是電子沿神經像金屬電線般自由流動", "錯誤觀念")

    @staticmethod
    def neuron():
        compare_system.equivalentto("神經元", "細胞", "接收與傳遞神經訊息的細胞", "定義")
        compare_system.equal("樹突", "功能", "接收訊息", "答案")
        compare_system.equal("軸突", "功能", "將訊息傳離細胞體", "答案")
        compare_system.equal("髓鞘", "作用", "加快神經衝動傳導", "答案")
        compare_system.equal("突觸", "定義", "神經元與另一細胞傳遞訊息的接點", "答案")
        compare_system.equal("神經傳遞物質", "功能", "跨越突觸間隙傳遞化學訊號", "答案")
        compare_system.notequal("神經元", "敘述", "任何部分受傷後都能快速完全再生", "錯誤觀念")

    @staticmethod
    def reflex():
        compare_system.equivalentto("反射作用", "神經反應", "不需意識思考即可快速產生的反應", "定義")
        compare_system.equal("反射弧順序", "簡化", "受器、感覺神經、中樞、運動神經、效應器", "答案")
        compare_system.equal("膝反射", "類型", "脊髓反射", "答案")
        compare_system.equal("手碰熱物立刻縮回", "作用", "保護性反射", "答案")
        compare_system.equal("反射作用", "大腦", "訊息仍可之後傳至大腦產生感覺", "答案")
        compare_system.notequal("反射作用", "敘述", "完全不經任何中樞神經系統", "錯誤觀念")

    @staticmethod
    def endocrine_system():
        compare_system.equivalentto("內分泌系統", "調節系統", "以激素經血液傳遞訊息的調節系統", "定義")
        compare_system.equivalentto("激素", "化學訊息", "由內分泌腺分泌並作用於標的細胞的物質", "定義")
        compare_system.equal("內分泌腺", "特徵", "沒有導管，分泌物進入血液", "答案")
        compare_system.equal("激素作用", "特性", "只對具有相應受體的標的細胞產生效果", "答案")
        compare_system.equal("神經調節", "一般比較", "較快速且作用時間較短", "答案")
        compare_system.equal("內分泌調節", "一般比較", "較慢但作用時間可能較長", "答案")
        compare_system.notequal("激素", "敘述", "只在分泌腺附近作用", "錯誤觀念")

    @staticmethod
    def blood_glucose():
        compare_system.equal("胰島素", "分泌細胞", "胰臟 β 細胞", "答案")
        compare_system.equal("胰島素", "主要作用", "降低血糖", "答案")
        compare_system.equal("升糖素", "分泌細胞", "胰臟 α 細胞", "答案")
        compare_system.equal("升糖素", "主要作用", "提高血糖", "答案")
        compare_system.equal("血糖過高", "正常反應", "胰島素分泌增加", "答案")
        compare_system.equal("血糖過低", "正常反應", "升糖素分泌增加", "答案")
        compare_system.equal("肝醣", "作用", "儲存葡萄糖", "答案")
        compare_system.notequal("胰島素", "敘述", "直接將所有血糖排出體外", "錯誤觀念")

    @staticmethod
    def immune_system():
        compare_system.equivalentto("免疫系統", "防禦系統", "辨識並對抗病原與異常細胞的系統", "定義")
        compare_system.equal("第一道防線", "例子", "皮膚與黏膜", "答案")
        compare_system.equal("先天免疫", "特性", "反應快速且專一性較低", "答案")
        compare_system.equal("適應性免疫", "特性", "具有高度專一性與免疫記憶", "答案")
        compare_system.equal("白血球", "功能", "參與免疫防禦", "答案")
        compare_system.equal("淋巴器官", "例子", "淋巴結、脾臟與胸腺", "答案")
        compare_system.notequal("發炎", "敘述", "一定代表免疫系統完全失控", "錯誤觀念")

    @staticmethod
    def antibody():
        compare_system.equivalentto("抗原", "免疫概念", "能被免疫系統辨識並引發特定反應的物質", "定義")
        compare_system.equivalentto("抗體", "免疫蛋白", "由 B 細胞衍生漿細胞產生並專一結合抗原的蛋白質", "定義")
        compare_system.equal("B 細胞", "功能", "參與抗體型免疫", "答案")
        compare_system.equal("T 細胞", "功能", "協調免疫或殺死受感染細胞", "答案")
        compare_system.equal("記憶細胞", "作用", "使再次感染時反應更快速", "答案")
        compare_system.notequal("抗體", "敘述", "會直接殺死所有病原體", "錯誤觀念")
        compare_system.notequal("一種抗體", "敘述", "可專一辨識所有抗原", "錯誤觀念")

    @staticmethod
    def vaccine():
        compare_system.equivalentto("疫苗", "免疫預防", "以安全方式讓免疫系統接觸抗原並建立免疫記憶", "定義")
        compare_system.equal("疫苗", "主要效果", "降低特定感染或重症風險", "答案")
        compare_system.equal("疫苗接種後", "免疫", "產生記憶細胞", "答案")
        compare_system.equal("群體免疫", "概念", "足夠人口具有免疫可降低病原傳播", "答案")
        compare_system.notequal("疫苗", "敘述", "保證任何接種者永遠不會感染", "錯誤觀念")
        compare_system.notequal("抗生素", "敘述", "可取代疫苗預防所有病毒感染", "錯誤觀念")

    @staticmethod
    def musculoskeletal():
        compare_system.equal("骨骼系統", "功能", "支持、保護、運動與製造血球", "答案")
        compare_system.equal("骨骼肌", "控制", "多數可隨意控制", "答案")
        compare_system.equal("平滑肌", "位置", "內臟與血管壁", "答案")
        compare_system.equal("心肌", "位置", "心臟", "答案")
        compare_system.equal("肌肉收縮", "作用", "只能拉動骨骼，不能主動推長", "答案")
        compare_system.equal("拮抗肌", "關係", "一組收縮時另一組放鬆以產生相反動作", "答案")
        compare_system.equal("肌腱", "連接", "肌肉與骨骼", "答案")
        compare_system.equal("韌帶", "連接", "骨與骨", "答案")

    @staticmethod
    def reproductive_system():
        compare_system.equal("睪丸", "功能", "產生精子與睪固酮", "答案")
        compare_system.equal("卵巢", "功能", "產生卵與女性相關激素", "答案")
        compare_system.equal("精子", "染色體套數", "單套", "答案")
        compare_system.equal("卵細胞", "染色體套數", "單套", "答案")
        compare_system.equal("受精", "人類常見位置", "輸卵管", "答案")
        compare_system.equal("胚胎著床", "位置", "子宮內膜", "答案")
        compare_system.equal("胎盤", "功能", "母體與胎兒間進行物質交換並分泌激素", "答案")
        compare_system.notequal("母體血液與胎兒血液", "敘述", "正常情況下完全混合在一起", "錯誤觀念")

    @staticmethod
    def menstrual_cycle():
        compare_system.equal("月經週期", "調節", "由多種激素共同調控", "答案")
        compare_system.equal("FSH", "作用之一", "促進卵泡發育", "答案")
        compare_system.equal("LH 高峰", "作用", "促進排卵", "答案")
        compare_system.equal("雌激素", "作用之一", "促進子宮內膜增厚", "答案")
        compare_system.equal("黃體素", "作用之一", "維持子宮內膜", "答案")
        compare_system.equal("沒有懷孕時黃體退化", "結果", "激素下降並引發月經", "答案")
        compare_system.notequal("排卵日", "敘述", "每個人的每一個週期都固定在完全相同日期", "錯誤觀念")