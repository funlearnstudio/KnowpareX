from knowparex.PROGRAMMING_NOTES import compare_system
class history_world:
    @staticmethod
    def ancient_river_civilizations():
        compare_system.definition('兩河流域文明', '古代文明', '發展於底格里斯河與幼發拉底河流域的文明', '中文解釋')
        compare_system.definition('古埃及文明', '古代文明', '發展於尼羅河流域的文明', '中文解釋')
        compare_system.definition('印度河文明', '古代文明', '發展於南亞印度河流域的城市文明', '中文解釋')

    @staticmethod
    def ancient_greece():
        compare_system.definition('古希臘文明', '古代文明', '以城邦政治、哲學與藝術著稱的地中海文明', '中文解釋')
        compare_system.related('雅典', '城邦', '公民政治與民主制度發展的重要城邦', '特徵')
        compare_system.related('斯巴達', '城邦', '重視軍事訓練與紀律的城邦', '特徵')

    @staticmethod
    def roman_world():
        compare_system.definition('羅馬共和', '古代政治', '以元老院、執政官與公民制度構成的政治體制', '中文解釋')
        compare_system.definition('羅馬帝國', '古代帝國', '羅馬由共和轉為皇帝統治後形成的廣大帝國', '中文解釋')
        compare_system.related('羅馬法', '法律史', '影響後世歐洲法律傳統', '影響')

    @staticmethod
    def christianity_islam():
        compare_system.definition('基督教', '世界宗教', '起源於西亞並在羅馬帝國內傳播的宗教', '中文解釋')
        compare_system.definition('伊斯蘭文明', '世界史', '以伊斯蘭教為核心並連結西亞、北非等地的文明', '中文解釋')
        compare_system.related('翻譯運動', '伊斯蘭文明', '保存並發展希臘、波斯與印度知識', '影響')

    @staticmethod
    def medieval_europe():
        compare_system.definition('封建制度', '中世紀歐洲', '領主與附庸以土地、效忠與軍事義務維繫關係', '中文解釋')
        compare_system.related('莊園制度', '經濟社會', '以農業莊園為中心的地方經濟', '特徵')
        compare_system.related('天主教會', '中世紀歐洲', '宗教、教育、文化與政治的重要力量', '影響')

    @staticmethod
    def crusades_towns():
        compare_system.definition('十字軍東征', '中世紀世界史', '11至13世紀西歐基督徒前往東地中海的軍事行動', '中文解釋')
        compare_system.resultsin('地中海貿易復甦', '中世紀變化', '城市與市民階層成長', '結果')

    @staticmethod
    def renaissance_reformation():
        compare_system.definition('文藝復興', '歐洲史', '14至16世紀重視古典文化、人文精神與藝術創新的運動', '中文解釋')
        compare_system.definition('宗教改革', '歐洲史', '16世紀對西方教會制度與信仰實踐提出改革的運動', '中文解釋')

    @staticmethod
    def scientific_revolution_enlightenment():
        compare_system.definition('科學革命', '世界史', '16至17世紀以觀察、實驗與數學重新理解自然的變革', '中文解釋')
        compare_system.definition('啟蒙運動', '思想史', '18世紀強調理性、自然權利與政治改革的思想運動', '中文解釋')

    @staticmethod
    def age_of_exploration():
        compare_system.definition('地理大發現', '世界史', '15世紀後歐洲航海擴張並建立全球海路的過程', '中文解釋')
        compare_system.definition('哥倫布大交換', '世界史', '新舊大陸之間人口、作物、動物與疾病的大規模交流', '中文解釋')
        compare_system.definition('大西洋奴隸貿易', '世界史', '非洲人口被強迫運往美洲的殖民貿易', '中文解釋')

    @staticmethod
    def atlantic_revolutions():
        compare_system.definition('美國獨立革命', '世界史', '北美十三殖民地反抗英國並建立美國的革命', '中文解釋')
        compare_system.definition('法國大革命', '世界史', '1789年起推翻舊制度並重塑政治社會秩序的革命', '中文解釋')
        compare_system.related('人權宣言', '政治文件', '主張自由、平等與人民權利', '內容')

    @staticmethod
    def industrial_revolution():
        compare_system.definition('工業革命', '世界史', '18世紀後以機械、工廠與新動力改變生產方式的變革', '中文解釋')
        compare_system.resultsin('工業革命', '社會影響', '都市化、勞工階級與資本主義擴張', '結果')

    @staticmethod
    def nationalism_imperialism():
        compare_system.definition('民族主義', '近代思想', '具有共同歷史文化的民族應形成政治共同體', '中文解釋')
        compare_system.definition('新帝國主義', '世界史', '19世紀後工業強權在亞洲、非洲等地擴張殖民控制', '中文解釋')

    @staticmethod
    def world_war_one():
        compare_system.definition('第一次世界大戰', '世界史', '1914年至1918年以歐洲為中心並波及全球的戰爭', '中文解釋')
        compare_system.causes('軍國主義、同盟體系、帝國競爭與民族衝突', '背景', '第一次世界大戰', '結果')

    @staticmethod
    def interwar_period():
        compare_system.related('經濟大恐慌', '世界經濟', '1929年起全球經濟嚴重衰退', '中文解釋')
        compare_system.definition('法西斯主義', '政治思想', '強調極端民族主義、威權領袖與國家動員', '中文解釋')

    @staticmethod
    def world_war_two_holocaust():
        compare_system.definition('第二次世界大戰', '世界史', '1939年至1945年席捲歐亞非與太平洋的全球戰爭', '中文解釋')
        compare_system.definition('猶太大屠殺', '世界史', '納粹德國系統性迫害與屠殺歐洲猶太人的暴行', '中文解釋')

    @staticmethod
    def united_nations_human_rights():
        compare_system.definition('聯合國', '國際組織', '1945年成立以維護和平、促進合作與人權', '中文解釋')
        compare_system.related('世界人權宣言', '人權文件', '1948年通過的重要國際人權標準', '功能')

    @staticmethod
    def cold_war():
        compare_system.definition('冷戰', '世界史', '第二次世界大戰後美國與蘇聯兩大陣營的全球競爭', '中文解釋')
        compare_system.related('代理人戰爭', '冷戰現象', '兩強支持不同勢力進行區域衝突', '中文解釋')

    @staticmethod
    def decolonization():
        compare_system.definition('去殖民化', '世界史', '第二次世界大戰後殖民地爭取獨立的過程', '中文解釋')
        compare_system.resultsin('民族獨立運動', '歷史影響', '亞洲與非洲出現大量新國家', '結果')

    @staticmethod
    def globalization():
        compare_system.definition('全球化', '現代世界史', '商品、資本、資訊、人口與文化跨國流動加速', '中文解釋')
        compare_system.resultsin('全球化', '歷史影響', '經濟互賴增加但不平等與文化衝突也可能加深', '結果')

