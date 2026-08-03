from knowparex.PROGRAMMING_NOTES import compare_system
class chinese_literature:
    @staticmethod
    def literary_genres():
        compare_system.definition('文學體裁', '文學常識', '依表達方式、形式與功能區分作品類型', '中文解釋')
        compare_system.typeof('詩歌', '文學體裁', '韻文', '類型')
        compare_system.typeof('散文', '文學體裁', '非韻文', '類型')
        compare_system.typeof('小說', '文學體裁', '敘事文學', '類型')
        compare_system.typeof('戲劇', '文學體裁', '舞臺表演文學', '類型')

    @staticmethod
    def prose():
        compare_system.definition('散文', '文學體裁', '形式自由、不必押韻，重視真情實感與思想表達', '中文解釋')
        compare_system.typeof('記敘文', '散文', '以事件與人物為主要內容', '類型')
        compare_system.typeof('抒情文', '散文', '以情感抒發為主要內容', '類型')
        compare_system.typeof('說明文', '散文', '以解說事理與知識為主要內容', '類型')
        compare_system.typeof('議論文', '散文', '以提出論點與論證為主要內容', '類型')

    @staticmethod
    def classical_prose():
        compare_system.definition('古文', '古典文學', '以文言寫成的散文', '中文解釋')
        compare_system.related('先秦散文', '古文發展', '諸子散文與歷史散文', '內容')
        compare_system.related('唐宋古文運動', '文學運動', '反對過度雕飾駢文並提倡先秦兩漢散文精神', '中文解釋')

    @staticmethod
    def parallel_prose():
        compare_system.definition('駢文', '古典散文', '重視對偶、聲律與辭藻的文體', '中文解釋')
        compare_system.related('四六文', '駢文', '句式常以四字、六字為主', '特徵')
        compare_system.opposite('駢文', '文體', '散體文', '形式對照')

    @staticmethod
    def poetry():
        compare_system.definition('詩', '韻文', '以精鍊語言、節奏與意象表達情志', '中文解釋')
        compare_system.typeof('古體詩', '詩', '格律限制較少', '類型')
        compare_system.typeof('近體詩', '詩', '講究平仄、對仗與押韻', '類型')
        compare_system.typeof('現代詩', '詩', '形式較自由並重視現代語言與意象', '類型')

    @staticmethod
    def ancient_poetry():
        compare_system.definition('古體詩', '古典詩歌', '唐代近體詩形成前後皆可創作、格律較自由的詩體', '中文解釋')
        compare_system.related('樂府詩', '古體詩', '可歌唱且題材廣泛', '關係')
        compare_system.related('五言古詩', '古體詩', '每句多為五字', '形式')
        compare_system.related('七言古詩', '古體詩', '每句多為七字', '形式')

    @staticmethod
    def regulated_verse():
        compare_system.definition('近體詩', '古典詩歌', '唐代成熟、格律嚴謹的詩體', '中文解釋')
        compare_system.typeof('絕句', '近體詩', '四句', '形式')
        compare_system.typeof('律詩', '近體詩', '八句', '形式')
        compare_system.related('頷聯與頸聯', '律詩', '通常要求對仗', '規則')

    @staticmethod
    def jueju():
        compare_system.definition('絕句', '近體詩', '全詩四句，可分五言與七言', '中文解釋')
        compare_system.related('起承轉合', '絕句結構', '常見章法', '關係')

    @staticmethod
    def lushi():
        compare_system.definition('律詩', '近體詩', '全詩八句，分首聯、頷聯、頸聯、尾聯', '中文解釋')
        compare_system.partof('首聯', '律詩', '律詩', '結構')
        compare_system.partof('頷聯', '律詩', '律詩', '結構')
        compare_system.partof('頸聯', '律詩', '律詩', '結構')
        compare_system.partof('尾聯', '律詩', '律詩', '結構')

    @staticmethod
    def yuefu():
        compare_system.definition('樂府', '古典詩歌', '原為音樂官署，後也指其採集或仿作的詩歌', '中文解釋')
        compare_system.related('敘事性', '樂府詩', '常見特色', '關係')
        compare_system.related('民歌精神', '樂府詩', '反映社會生活與人民情感', '關係')

    @staticmethod
    def shijing():
        compare_system.definition('《詩經》', '經典', '中國最早的詩歌總集', '中文解釋')
        compare_system.partof('風', '《詩經》', '地方民歌', '內容')
        compare_system.partof('雅', '《詩經》', '朝會宴享樂歌', '內容')
        compare_system.partof('頌', '《詩經》', '宗廟祭祀樂歌', '內容')
        compare_system.related('賦比興', '《詩經》', '常見表現手法', '關係')

    @staticmethod
    def chuci():
        compare_system.definition('楚辭', '古典文學', '戰國楚地形成、帶有地方色彩的詩歌體式', '中文解釋')
        compare_system.related('屈原', '楚辭', '重要代表作家', '人物')
        compare_system.related('香草美人', '楚辭', '常見象徵系統', '特色')

    @staticmethod
    def fu():
        compare_system.definition('賦', '古典文體', '介於詩與散文之間，常鋪陳描寫事物', '中文解釋')
        compare_system.related('鋪陳', '賦', '重要表現方式', '特色')
        compare_system.related('漢賦', '賦', '漢代盛行', '時期')

    @staticmethod
    def ci():
        compare_system.definition('詞', '古典韻文', '配合曲調填寫、句式長短不齊的文體', '中文解釋')
        compare_system.related('詞牌', '詞', '規定句數、字數與聲律', '功能')
        compare_system.typeof('婉約派', '詞風', '含蓄細膩', '類型')
        compare_system.typeof('豪放派', '詞風', '氣勢開闊', '類型')

    @staticmethod
    def qu():
        compare_system.definition('曲', '古典韻文', '元代興盛、可配樂演唱的文體', '中文解釋')
        compare_system.typeof('散曲', '曲', '小令與套數', '類型')
        compare_system.typeof('雜劇', '曲', '結合唱、白、科的戲劇形式', '類型')

    @staticmethod
    def modern_poetry():
        compare_system.definition('現代詩', '現代文學', '使用現代語言且形式較自由的詩', '中文解釋')
        compare_system.related('意象', '現代詩', '構成情感與思想的重要媒介', '功能')
        compare_system.related('分行', '現代詩', '創造節奏與視覺效果', '功能')

    @staticmethod
    def novel():
        compare_system.definition('小說', '敘事文學', '透過人物、情節、環境與觀點建構虛構世界', '中文解釋')
        compare_system.partof('人物', '小說要素', '小說', '關係')
        compare_system.partof('情節', '小說要素', '小說', '關係')
        compare_system.partof('環境', '小說要素', '小說', '關係')
        compare_system.partof('敘事觀點', '小說要素', '小說', '關係')

    @staticmethod
    def classical_novel():
        compare_system.definition('古典小說', '古典文學', '以文言或白話寫成的傳統敘事作品', '中文解釋')
        compare_system.typeof('志怪小說', '古典小說', '記錄鬼神怪異', '類型')
        compare_system.typeof('志人小說', '古典小說', '記錄人物言行軼事', '類型')
        compare_system.typeof('傳奇小說', '古典小說', '唐代成熟的文言短篇小說', '類型')
        compare_system.typeof('章回小說', '古典小說', '分回敘述的長篇白話小說', '類型')

    @staticmethod
    def zhiguai():
        compare_system.definition('志怪小說', '古典小說', '以神怪、異聞為主要內容', '中文解釋')
        compare_system.related('六朝', '志怪小說', '興盛時期', '關係')

    @staticmethod
    def zhiren():
        compare_system.definition('志人小說', '古典小說', '記錄人物言談、品格與軼事', '中文解釋')
        compare_system.related('《世說新語》', '志人小說', '代表作品', '關係')

    @staticmethod
    def tang_chuanqi():
        compare_system.definition('唐傳奇', '古典小說', '唐代文言短篇小說，情節完整且人物較鮮明', '中文解釋')
        compare_system.resultsin('唐傳奇成熟', '文學發展', '中國小說由筆記走向有意識創作', '結果')

    @staticmethod
    def chapter_novel():
        compare_system.definition('章回小說', '古典小說', '以回目分章、說書形式發展的長篇白話小說', '中文解釋')
        compare_system.related('四大奇書', '明代小說', '《三國演義》《水滸傳》《西遊記》《金瓶梅》', '內容')
        compare_system.related('《紅樓夢》', '章回小說', '清代長篇小說代表', '關係')

    @staticmethod
    def drama():
        compare_system.definition('戲劇', '文學體裁', '以角色對話與舞臺行動呈現衝突', '中文解釋')
        compare_system.partof('臺詞', '戲劇要素', '戲劇', '關係')
        compare_system.partof('舞臺指示', '戲劇要素', '戲劇', '關係')
        compare_system.partof('衝突', '戲劇要素', '戲劇', '關係')

    @staticmethod
    def traditional_opera():
        compare_system.definition('傳統戲曲', '表演藝術', '融合唱、念、做、打與音樂舞蹈', '中文解釋')
        compare_system.related('元雜劇', '傳統戲曲', '元代代表戲劇形式', '關係')
        compare_system.related('南戲與傳奇', '傳統戲曲', '宋元明清戲劇發展', '關係')

    @staticmethod
    def literary_movements():
        compare_system.definition('文學運動', '文學史', '作家群體針對文學觀念、形式與語言提出改革', '中文解釋')
        compare_system.related('古文運動', '文學運動', '唐宋提倡古文', '關係')
        compare_system.related('白話文運動', '文學運動', '近代提倡白話取代文言作為主要書寫語言', '關係')

    @staticmethod
    def tang_song_masters():
        compare_system.definition('唐宋八大家', '文學群體', '唐宋古文運動重要作家合稱', '中文解釋')
        compare_system.partof('韓愈、柳宗元', '唐宋八大家', '唐代作家', '成員')
        compare_system.partof('歐陽脩、蘇洵、蘇軾、蘇轍、王安石、曾鞏', '唐宋八大家', '宋代作家', '成員')

    @staticmethod
    def jianan_seven():
        compare_system.definition('建安七子', '文學群體', '東漢末建安時期七位重要文人', '中文解釋')
        compare_system.related('建安風骨', '文學特色', '慷慨悲涼、關懷現實', '關係')

    @staticmethod
    def bamboo_seven():
        compare_system.definition('竹林七賢', '文學群體', '魏晉時期七位崇尚自然、玄學與個性解放的文人', '中文解釋')
        compare_system.related('魏晉風度', '文化史', '重視個性與精神自由', '關係')

    @staticmethod
    def four_books():
        compare_system.definition('四書', '儒家經典', '《論語》《孟子》《大學》《中庸》的合稱', '中文解釋')
        compare_system.partof('《論語》', '四書', '四書', '成員')
        compare_system.partof('《孟子》', '四書', '四書', '成員')
        compare_system.partof('《大學》', '四書', '四書', '成員')
        compare_system.partof('《中庸》', '四書', '四書', '成員')

    @staticmethod
    def five_classics():
        compare_system.definition('五經', '儒家經典', '《詩》《書》《禮》《易》《春秋》的合稱', '中文解釋')
        compare_system.partof('《詩經》', '五經', '五經', '成員')
        compare_system.partof('《尚書》', '五經', '五經', '成員')
        compare_system.partof('《禮記》', '五經', '五經', '成員')
        compare_system.partof('《易經》', '五經', '五經', '成員')
        compare_system.partof('《春秋》', '五經', '五經', '成員')

    @staticmethod
    def historical_prose():
        compare_system.definition('歷史散文', '古典文學', '記錄歷史事件與人物的散文', '中文解釋')
        compare_system.typeof('編年體', '史書體例', '依年代排列史事', '類型')
        compare_system.typeof('紀傳體', '史書體例', '以本紀、列傳等記錄人物與制度', '類型')
        compare_system.typeof('國別體', '史書體例', '按國家分類記錄史事', '類型')

    @staticmethod
    def chronicle_history():
        compare_system.definition('編年體', '史書體例', '依年月先後編排史事', '中文解釋')
        compare_system.exampleof('《左傳》', '史書', '編年體', '體例')
        compare_system.exampleof('《資治通鑑》', '史書', '編年體', '體例')

    @staticmethod
    def biographical_history():
        compare_system.definition('紀傳體', '史書體例', '以人物傳記為中心並配合本紀、表、書等', '中文解釋')
        compare_system.exampleof('《史記》', '史書', '紀傳體', '體例')

    @staticmethod
    def country_history():
        compare_system.definition('國別體', '史書體例', '分國記錄史事', '中文解釋')
        compare_system.exampleof('《國語》', '史書', '國別體', '體例')
        compare_system.exampleof('《戰國策》', '史書', '國別體', '體例')

    @staticmethod
    def taiwan_literature():
        compare_system.definition('臺灣文學', '文學史', '在臺灣歷史與社會脈絡中形成的多語、多族群文學', '中文解釋')
        compare_system.related('原住民族文學', '臺灣文學', '口傳與書面創作的重要部分', '關係')
        compare_system.related('日治時期新文學', '臺灣文學', '現代文學發展的重要階段', '關係')
        compare_system.related('戰後臺灣文學', '臺灣文學', '多元主題與形式持續發展', '關係')

    @staticmethod
    def nativist_literature():
        compare_system.definition('鄉土文學', '臺灣文學', '關注土地、人民、地方生活與社會現實', '中文解釋')
        compare_system.related('現實關懷', '鄉土文學', '常見特色', '關係')

    @staticmethod
    def nature_writing():
        compare_system.definition('自然書寫', '現代文學', '描寫自然並反思人與環境關係', '中文解釋')
        compare_system.related('生態倫理', '自然書寫', '常見議題', '關係')

    @staticmethod
    def travel_writing():
        compare_system.definition('旅行文學', '現代文學', '以旅行經驗、地方觀察與文化思考為內容', '中文解釋')
        compare_system.related('空間與自我', '旅行文學', '常見主題', '關係')

    @staticmethod
    def oral_literature():
        compare_system.definition('口傳文學', '民間文學', '透過口耳相傳保存的故事、歌謠與傳說', '中文解釋')
        compare_system.typeof('神話', '口傳文學', '解釋世界起源與族群信仰', '類型')
        compare_system.typeof('傳說', '口傳文學', '與特定人物、地點或歷史相關', '類型')
        compare_system.typeof('民間故事', '口傳文學', '反映社會價值與想像', '類型')
