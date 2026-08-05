#!/usr/bin/env python3
"""Rewrite all junior/high earth-science units in batches of four."""
from __future__ import annotations
import argparse,json,shutil,sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from knowparex.curriculum_adapter import load_curriculum_js
from knowparex.curriculum_rebuild import write_curriculum_js
from knowparex.curriculum_quality import semantic_issues
FILE=ROOT/"src/knowparex/data/curriculum_integrated.js";STATE=ROOT/".knowparex_rewrite/earth_science_all_stages.json"
def p(t,e,x,c,f=[]):return(t,e,x,c,f)
C={
"interior":p("地球內部構造","地殼、地函與地核可依成分區分；岩石圈與軟流圈則依力學性質區分。","S波不能通過液態外核，是判斷外核狀態的重要證據。","把地函全說成液態岩漿。"),
"plate":p("板塊構造","岩石圈分成移動板塊；張裂、聚合與錯動邊界分別以分離、靠近與水平錯動為主。","中洋脊是張裂邊界，新海洋地殼在此形成。","把聚合邊界說成兩板塊彼此張開。"),
"quake":p("地震","地震由斷層突然錯動釋放能量；規模描述震源能量，震度描述某地搖晃程度。","同一地震規模只有一個，臺北與花蓮震度可不同。","把規模與各地震度當成同一數值。",["波速：v=fλ。"]),
"volcano":p("火山作用","岩漿上升與壓力降低、揮發分及構造環境有關；噴發型態受黏滯度和氣體影響。","富矽黏稠岩漿較易累積壓力並爆炸式噴發。","把所有地震主因都歸為火山活動。"),
"rock":p("岩石與礦物","礦物具有特定成分與晶體結構；岩石是礦物或其他物質的集合體。","花崗岩常含石英、長石與雲母。","把岩石名稱當成單一礦物名稱。"),
"cycle":p("岩石循環","火成、沉積與變質岩可經熔融、冷卻、風化沉積及變質作用互相轉換。","花崗岩風化成沉積物，固結後可形成沉積岩。","說板塊移動直接把任何岩石瞬間變成另一類。"),
"strata":p("地層、化石與年代","未受擾動地層通常下老上新；化石可用於相對定年，放射性同位素可估絕對年代。","指準化石分布時間短且範圍廣，可比對地層年代。","把化石本身當成岩石循環的驅動力。"),
"weather":p("天氣與氣候","天氣是短時間局地大氣狀態，氣候是長期統計特徵。","今日豪雨是天氣；某地30年雨季平均是氣候。","用單日寒冷否定長期暖化趨勢。"),
"pressure":p("氣壓與風","氣壓梯度力使空氣由高壓趨向低壓，地球自轉與摩擦使實際風向偏轉。","等壓線越密通常氣壓梯度越大、風較強。","說風只由高溫直接吹向低溫。"),
"front":p("鋒面與降水","鋒面是性質不同氣團交界；空氣抬升冷卻至飽和可凝結成雲並可能降水。","冷鋒使暖空氣快速抬升，常有較短而強的降雨。","把所有降雨都說成颱風造成。"),
"typhoon":p("颱風","颱風需暖海面、水氣與適當大氣環境，能量主要來自水氣凝結潛熱。","颱風登陸後失去暖海供能且摩擦增大，通常減弱。","把颱風中心低壓與鋒面主內容混為一談。"),
"ocean":p("海水與洋流","洋流受盛行風、密度差、地轉效應與海盆形狀影響，搬運熱量並影響氣候。","黑潮將低緯暖水帶向臺灣東側。","把洋流、潮汐與海浪說成同一種週期運動。"),
"tide":p("潮汐","潮汐主要由月球與太陽引力及地月系統運動造成，實際潮時受海岸與海盆影響。","朔望附近日月引潮力較同向，常形成大潮。","把潮汐說成只由海風吹動。"),
"moon":p("月相與日月食","月相源自日照月面的可見比例，不是地球影子；日月食需日、地、月接近一直線且靠近交點。","滿月時月球位於地球背日側，但多數滿月不發生月食。","把每月月相變化解釋成地球影子遮月。"),
"season":p("四季","四季主因是地軸傾斜，使太陽高度與晝長隨公轉改變，不是地日距離。","北半球夏季太陽較高、白晝較長，單位面積受能較多。","說地球靠近太陽時全球同時是夏季。"),
"solar":p("太陽系","太陽系含太陽、行星、矮行星、小天體與行星際物質；行星繞日方向與軌道具有共同形成線索。","類地行星較小且岩質，類木行星體積大且富氣體或冰。","把月球或所有彗星列為行星。"),
"star":p("恆星演化","恆星以核融合供能，質量決定主要演化路徑；高質量恆星壽命反而較短。","類太陽恆星經紅巨星後形成白矮星。","把恆星亮度變化都解釋為與地球距離改變。"),
"galaxy":p("星系與宇宙","星系由恆星、氣體、塵埃與暗物質等組成；宇宙尺度須區分天文單位、光年與百萬秒差距。","銀河系是含太陽系的棒旋星系。","把太陽系、銀河系與宇宙當成同一尺度。"),
"observe":p("觀測與資料判讀","觀測須記錄時間、位置、儀器、單位與不確定度；模型有解析度與假設限制。","地震站P、S波到時差可協助估震央距離。","只憑單站資料就宣稱精確三維震源位置。"),
"water":p("水文循環","水在蒸發、凝結、降水、入滲、逕流與地下水間轉移，受能量與地形控制。","都市鋪面增加會降低入滲並提高暴雨逕流。","把地下水當成不參與循環的固定水庫。"),
"climate":p("氣候變遷","氣候變遷由輻射強迫、回饋與內部變異共同影響；人為溫室氣體是近代暖化主因。","CO₂增加造成正輻射強迫，長期平均溫度上升。","把單次極端事件單獨當成全球氣候因果證明。"),
"hazard":p("地質災害與防災","危害、暴露度與脆弱度共同形成風險；地震、山崩、海嘯需不同監測與避難策略。","強震後若位於海岸並收到警報，應迅速往高處避難。","把災害風險只等同自然現象規模。"),
"remote":p("遙測與地圖","遙測由不同波段反射或輻射判讀地表；地圖投影、比例尺與解析度限制解讀。","植生在近紅外波段反射強，可用多光譜影像辨識。","把像元顏色直接當成肉眼真實顏色。"),
"system":p("地球系統","岩石圈、水圈、氣圈與生物圈透過物質與能量交換互相影響。","火山氣體進入大氣後可影響輻射與氣候。","把各圈層視為彼此獨立、沒有回饋。"),
"sustain":p("資源與永續","資源評估須考慮形成速率、蘊藏、開採衝擊、回收與代際公平。","地下水抽取超過補注可造成地層下陷。","把可再生資源誤認為可無限速度使用。"),
}
MAP={"地球內部與板塊":["interior","plate","quake"],"地震火山與地質作用":["quake","volcano","cycle"],"天氣與氣候":["weather","pressure","front"],"海洋與水文":["ocean","tide","water"],"日月地與太陽系":["moon","season","solar"],"宇宙與觀測":["star","galaxy","observe"],"地球系統概論":["system","interior","observe"],"岩石與地質年代":["rock","cycle","strata"],"板塊構造":["plate","interior","cycle"],"地震與火山":["quake","volcano","hazard"],"大氣與天氣":["weather","pressure","front"],"海洋與氣候":["ocean","tide","climate"],"天文觀測":["moon","star","observe"],"地科探究方法":["observe","system","hazard"],"水文循環":["water","weather","sustain"],"天氣系統與颱風":["pressure","front","typhoon"],"氣候變遷":["climate","ocean","observe"],"地質災害":["hazard","quake","volcano"],"太陽系":["solar","moon","season"],"恆星與星系":["star","galaxy","observe"],"遙測與地圖":["remote","observe","hazard"],"地科素養題":["observe","system","weather"],"地球環境變遷":["climate","cycle","strata"],"資源與永續":["sustain","water","system"],"宇宙演化":["galaxy","star","observe"],"觀測資料判讀":["observe","remote","weather"],"綜合探究":["observe","system","hazard"],"跨科閱讀":["system","climate","observe"],"學測地科複習":["plate","weather","moon"],"分科地科總複習":["strata","ocean","galaxy"]}
MAP["日月地與太陽系"]=["moon","season","tide"]
def details(title,stage):
 r=[C[k] for k in MAP[title]];depth="以生活現象、圖表判讀與防災為主" if stage=="junior_high" else "連結機制、時空尺度、資料分析與模型限制";ps=[f"{title}{depth}：{r[0][1]}；{r[1][1]}。",f"本單元也要掌握{r[2][0]}：{r[2][1]}判讀時須確認因果方向、時間尺度、空間尺度與證據限制。"]
 fs=[]
 for a in r:
  for f in a[4]:
   if f not in fs:fs.append(f)
 return{"lessonText":ps,"readableLesson":ps,"formulas":fs,"keyPoints":[{"topic":a[0],"explanation":a[1],"example":f"{a[0]}例：{a[2]}","commonTrap":a[3]} for a in r]}
def rewrite(path,batch):
 d=load_curriculum_js(path);us=[(b["stage"],u) for b in d["earth"] if b.get("stage") in("junior_high","high_school") for u in b["units"]];assert len(us)==30 and set(u["name"] for _,u in us)==set(MAP);cnt={"junior_high":0,"high_school":0};fail=[];STATE.parent.mkdir(parents=True,exist_ok=True)
 for o in range(0,len(us),batch):
  for st,u in us[o:o+batch]:u["lessonDetails"]=details(u["name"],st);z=semantic_issues("earth_"+st,u["name"],u["lessonDetails"]);fail.append({"stage":st,"title":u["name"],"issues":z}) if z else None;cnt[st]+=not z
  write_curriculum_js(path,d);STATE.write_text(json.dumps({**cnt,"failed":fail,"last_offset":min(o+batch,len(us)),"batch_size":batch},ensure_ascii=False,indent=2),encoding="utf-8")
 return{**cnt,"failed":fail,"total":len(us)}
def main():
 a=argparse.ArgumentParser();a.add_argument("--file",type=Path,default=FILE);a.add_argument("--batch-size",type=int,default=4);a.add_argument("--no-backup",action="store_true");x=a.parse_args()
 if not x.no_backup:b=x.file.with_name(x.file.name+f".before_earth_science_all_stages_{datetime.now():%Y%m%d_%H%M%S}");shutil.copy2(x.file,b);print(f"backup={b}")
 r=rewrite(x.file,x.batch_size);print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if not r["failed"] else 2
if __name__=="__main__":raise SystemExit(main())
