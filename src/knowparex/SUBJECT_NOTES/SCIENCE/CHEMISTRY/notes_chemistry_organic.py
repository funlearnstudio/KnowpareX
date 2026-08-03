# ===========================================
# notes_chemistry_organic.py
# 化學：有機化學與生活化學
# ===========================================

from knowparex.PROGRAMMING_NOTES import compare_system
class chemistry_organic:

    @staticmethod
    def organic_compound():
        compare_system.equivalentto("有機化合物", "化合物", "以碳為主要骨架的一大類化合物", "定義")
        compare_system.equal("有機化合物常見元素", "題目", "C、H、O、N、S、鹵素等", "答案")
        compare_system.equal("碳原子", "鍵結能力", "可形成四個共價鍵", "答案")
        compare_system.equal("碳原子", "結構能力", "可形成長鏈、支鏈與環狀骨架", "答案")
        compare_system.notequal("所有含碳化合物", "敘述", "都一定分類為有機化合物", "錯誤觀念")
        compare_system.equal("CO₂、CO、碳酸鹽", "一般分類", "通常歸入無機化合物", "答案")

    @staticmethod
    def hydrocarbon():
        compare_system.equivalentto("烴", "有機化合物", "只由碳與氫兩種元素組成的化合物", "定義")
        compare_system.equivalentto("烷類", "烴", "只含碳—碳單鍵的飽和烴", "定義")
        compare_system.equivalentto("烯類", "烴", "含有至少一個碳—碳雙鍵的不飽和烴", "定義")
        compare_system.equivalentto("炔類", "烴", "含有至少一個碳—碳三鍵的不飽和烴", "定義")
        compare_system.equal("甲烷", "化學式", "CH₄", "答案")
        compare_system.equal("乙烯", "化學式", "C₂H₄", "答案")
        compare_system.equal("乙炔", "化學式", "C₂H₂", "答案")

    @staticmethod
    def alkane():
        compare_system.equal("烷類通式", "非環狀飽和烴", "CₙH₂ₙ₊₂", "答案")
        compare_system.equal("甲烷", "分子式", "CH₄", "答案")
        compare_system.equal("乙烷", "分子式", "C₂H₆", "答案")
        compare_system.equal("丙烷", "分子式", "C₃H₈", "答案")
        compare_system.equal("丁烷", "分子式", "C₄H₁₀", "答案")
        compare_system.equal("烷類燃燒", "氧氣充足", "主要生成 CO₂ 與 H₂O", "答案")
        compare_system.equal("烷類", "反應性", "通常比烯類低", "答案")

    @staticmethod
    def alkene_alkyne():
        compare_system.equal("烯類通式", "單一雙鍵非環狀烴", "CₙH₂ₙ", "答案")
        compare_system.equal("炔類通式", "單一三鍵非環狀烴", "CₙH₂ₙ₋₂", "答案")
        compare_system.equal("乙烯", "官能結構", "C=C", "答案")
        compare_system.equal("乙炔", "官能結構", "C≡C", "答案")
        compare_system.equal("烯類", "常見反應", "加成反應", "答案")
        compare_system.equal("溴水褪色", "可能用途", "檢驗碳—碳雙鍵等不飽和鍵", "答案")
        compare_system.notequal("不飽和烴", "敘述", "代表分子中含有水", "錯誤觀念")

    @staticmethod
    def isomer():
        compare_system.equivalentto("同分異構物", "化合物關係", "分子式相同但結構不同的化合物", "定義")
        compare_system.equal("正丁烷與異丁烷", "關係", "同分異構物", "答案")
        compare_system.equal("同分異構物", "分子式", "相同", "答案")
        compare_system.equal("同分異構物", "結構與性質", "可能不同", "答案")
        compare_system.equal("碳數增加", "一般結果", "可能的結構異構物數目增加", "答案")
        compare_system.notequal("同分異構物", "敘述", "只是同一物質的不同名稱", "錯誤觀念")

    @staticmethod
    def functional_group():
        compare_system.equivalentto("官能基", "有機結構", "決定有機物典型反應性質的原子或原子團", "定義")
        compare_system.equal("羥基", "表示", "-OH", "答案")
        compare_system.equal("羧基", "表示", "-COOH", "答案")
        compare_system.equal("胺基", "表示", "-NH₂", "答案")
        compare_system.equal("醛基", "表示", "-CHO", "答案")
        compare_system.equal("酯基", "表示", "-COO-", "答案")
        compare_system.equal("相同官能基的化合物", "一般特徵", "具有相似化學反應性", "答案")

    @staticmethod
    def alcohol():
        compare_system.equivalentto("醇", "有機化合物", "含有連接飽和碳原子的羥基之化合物", "定義")
        compare_system.equal("甲醇", "分子式", "CH₃OH", "答案")
        compare_system.equal("乙醇", "分子式", "C₂H₅OH", "答案")
        compare_system.equal("乙醇", "常見用途", "溶劑、燃料與消毒用途", "答案")
        compare_system.equal("低碳醇溶於水", "原因之一", "羥基可與水形成氫鍵", "答案")
        compare_system.equal("乙醇燃燒", "主要生成物", "CO₂ 與 H₂O", "答案")
        compare_system.notequal("甲醇", "敘述", "可以安全飲用", "錯誤觀念")

    @staticmethod
    def carboxylic_acid():
        compare_system.equivalentto("羧酸", "有機化合物", "含有羧基 -COOH 的化合物", "定義")
        compare_system.equal("甲酸", "分子式", "HCOOH", "答案")
        compare_system.equal("乙酸", "分子式", "CH₃COOH", "答案")
        compare_system.equal("食醋主要酸性成分", "題目", "乙酸", "答案")
        compare_system.equal("羧酸", "酸鹼性", "通常為弱酸", "答案")
        compare_system.equal("羧酸與鹼", "反應", "可發生中和反應", "答案")
        compare_system.equal("羧酸與醇", "特定條件", "可形成酯與水", "答案")

    @staticmethod
    def ester():
        compare_system.equivalentto("酯", "有機化合物", "常由羧酸與醇脫水反應形成的化合物", "定義")
        compare_system.equivalentto("酯化反應", "有機反應", "羧酸與醇生成酯與水的反應", "定義")
        compare_system.equal("許多低分子酯", "氣味", "具有水果香味", "答案")
        compare_system.equal("酯", "常見用途", "香料與溶劑", "答案")
        compare_system.equal("酯水解", "結果", "可生成羧酸與醇或其衍生物", "答案")
        compare_system.equal("油脂", "結構分類", "甘油與脂肪酸形成的酯", "答案")

    @staticmethod
    def polymer():
        compare_system.equivalentto("聚合物", "高分子", "由大量重複單元連接形成的大分子", "定義")
        compare_system.equivalentto("單體", "分子", "可參與聚合形成聚合物的小分子", "定義")
        compare_system.equal("乙烯聚合", "生成物", "聚乙烯", "答案")
        compare_system.equal("聚乙烯重複單元", "來源", "乙烯", "答案")
        compare_system.equal("蛋白質", "天然聚合物", "由胺基酸單元組成", "答案")
        compare_system.equal("澱粉與纖維素", "天然聚合物", "由葡萄糖相關單元組成", "答案")
        compare_system.notequal("所有聚合物", "敘述", "都不能自然分解", "錯誤觀念")

    @staticmethod
    def addition_polymerization():
        compare_system.equivalentto("加成聚合", "聚合反應", "不飽和單體打開多重鍵後連接形成高分子的反應", "定義")
        compare_system.equal("乙烯形成聚乙烯", "反應類型", "加成聚合", "答案")
        compare_system.equal("加成聚合", "常見單體特徵", "含有 C=C 等不飽和鍵", "答案")
        compare_system.equal("加成聚合", "副產物", "通常沒有小分子副產物", "答案")
        compare_system.equal("聚氯乙烯單體", "題目", "氯乙烯", "答案")
        compare_system.equal("聚苯乙烯單體", "題目", "苯乙烯", "答案")

    @staticmethod
    def condensation_polymerization():
        compare_system.equivalentto("縮合聚合", "聚合反應", "多官能基單體結合並常釋出小分子的聚合反應", "定義")
        compare_system.equal("縮合聚合常見副產物", "題目", "H₂O、HCl 等小分子", "答案")
        compare_system.equal("聚酯", "形成方式", "可由二元酸與二元醇縮合形成", "答案")
        compare_system.equal("耐綸", "聚合物種類", "聚醯胺", "答案")
        compare_system.equal("蛋白質形成", "鍵結", "胺基酸間形成肽鍵並放出水", "答案")
        compare_system.notequal("縮合聚合", "敘述", "一定不產生任何副產物", "錯誤觀念")

    @staticmethod
    def carbohydrate():
        compare_system.equivalentto("醣類", "生物分子", "由碳、氫、氧為主構成的重要有機化合物", "定義")
        compare_system.equal("葡萄糖", "分類", "單醣", "答案")
        compare_system.equal("蔗糖", "分類", "雙醣", "答案")
        compare_system.equal("澱粉", "分類", "多醣", "答案")
        compare_system.equal("纖維素", "分類", "多醣", "答案")
        compare_system.equal("葡萄糖", "生物功能", "重要能量來源", "答案")
        compare_system.equal("植物儲存醣類", "主要形式之一", "澱粉", "答案")
        compare_system.equal("植物細胞壁", "主要成分之一", "纖維素", "答案")

    @staticmethod
    def lipid():
        compare_system.equivalentto("脂質", "生物分子", "多數不易溶於水的一大類有機物", "定義")
        compare_system.equal("油脂", "主要組成", "甘油與脂肪酸形成的酯", "答案")
        compare_system.equal("脂肪", "常溫狀態", "通常偏固態", "答案")
        compare_system.equal("油", "常溫狀態", "通常偏液態", "答案")
        compare_system.equal("不飽和脂肪酸", "結構", "含有一個或多個碳—碳雙鍵", "答案")
        compare_system.equal("脂質", "生物功能", "儲存能量、構成細胞膜與保溫", "答案")
        compare_system.notequal("所有脂質", "敘述", "都對人體有害", "錯誤觀念")

    @staticmethod
    def protein():
        compare_system.equivalentto("蛋白質", "生物高分子", "由胺基酸以肽鍵連接形成的高分子", "定義")
        compare_system.equal("蛋白質基本單體", "題目", "胺基酸", "答案")
        compare_system.equal("胺基酸之間的鍵", "名稱", "肽鍵", "答案")
        compare_system.equal("酵素", "主要化學種類", "多數是蛋白質", "答案")
        compare_system.equal("蛋白質變性", "結果", "立體結構改變並可能失去功能", "答案")
        compare_system.equal("高溫或極端 pH", "可能作用", "使蛋白質變性", "答案")
        compare_system.notequal("蛋白質變性", "敘述", "一定代表肽鍵全部斷裂成胺基酸", "錯誤觀念")

    @staticmethod
    def detergent():
        compare_system.equivalentto("界面活性劑", "物質", "同時具有親水端與疏水端並能降低界面張力的物質", "定義")
        compare_system.equal("清潔劑疏水端", "作用", "與油脂接觸", "答案")
        compare_system.equal("清潔劑親水端", "作用", "與水接觸", "答案")
        compare_system.equal("微胞", "結構", "界面活性劑包圍油脂形成的集合體", "答案")
        compare_system.equal("肥皂遇硬水", "可能現象", "形成皂垢並降低清潔效果", "答案")
        compare_system.equal("合成清潔劑", "硬水中", "通常較不易形成皂垢", "答案")
        compare_system.notequal("清潔劑", "敘述", "直接把油脂化學分解成不存在", "錯誤觀念")