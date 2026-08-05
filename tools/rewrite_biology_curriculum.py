#!/usr/bin/env python3
"""Rewrite junior- and high-school biology in four-unit checkpoints."""
from __future__ import annotations
import argparse,json,shutil,sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from knowparex.curriculum_adapter import load_curriculum_js
from knowparex.curriculum_rebuild import write_curriculum_js
from knowparex.curriculum_quality import semantic_issues
FILE=ROOT/"src/knowparex/data/curriculum_integrated.js";STATE=ROOT/".knowparex_rewrite/biology_all_stages.json"
def point(t,e,x,c):return{"topic":t,"explanation":e,"example":f"{t}例：{x}","commonTrap":c}
def lesson(title,level,points,formulas=[]):
 depth="以可觀察現象與生活情境建立基礎概念" if level=="junior_high" else "連結細胞與分子機制、調控關係及實驗證據"
 e0=points[0]['explanation'].rstrip('。');e1=points[1]['explanation'].rstrip('。');e2=points[2]['explanation'].rstrip('。')
 return{"lessonText":[f"{title}的學習重點是{points[0]['topic']}與{points[1]['topic']}，{depth}：{e0}，同時{e1}。",f"本單元也必須掌握{points[2]['topic']}：{e2}；判讀時要區分構造與功能、物質流向與能量流向，並以直接證據支持結論。"],"readableLesson":[],"formulas":formulas,"keyPoints":points}
def P(*rows):return[point(*r) for r in rows]
CELL=P(("細胞構造","細胞膜界定細胞，細胞質進行多種反應，細胞核保存遺傳資訊。","口腔皮膜細胞可見細胞膜、細胞質與細胞核。","把所有細胞都說成具有細胞壁與葉綠體。"),("胞器功能","胞器的構造配合功能，粒線體參與有氧呼吸，核糖體合成蛋白質。","肌肉細胞通常含較多粒線體以供能。","把粒線體說成製造葡萄糖的場所。"),("細胞學說","生物由細胞組成，細胞是基本構造功能單位，細胞來自既有細胞。","新細胞由母細胞分裂產生。","認為細胞能由非生命物質自行形成。"))
MEM=P(("選擇性通透","磷脂雙層與膜蛋白共同控制物質進出。","氧可順濃度梯度擴散通過膜。","把細胞膜視為完全不透的牆。"),("被動與主動運輸","被動運輸順梯度且不直接耗ATP；主動運輸逆梯度並需能量。","鈉鉀幫浦利用ATP維持離子梯度。","說協助性擴散因使用蛋白質就必須耗ATP。"),("滲透作用","水跨選擇性通透膜由水勢較高處移向較低處。","植物細胞置於高張溶液會失水。","把溶質移動誤稱為水的滲透。"))
META=P(("酵素","酵素降低活化能、加快速率，但不改變平衡位置。","過氧化氫酶可加速過氧化氫分解。","套用一般化學速率模板而忽略酵素專一性與變性。"),("ATP","ATP水解與磷酸基轉移可耦合需要能量的細胞反應。","主動運輸可由ATP水解提供能量。","把ATP說成長期儲存能量或由細胞膜自行製造。"),("代謝調控","代謝路徑受酵素量、底物、產物回饋與細胞狀態調控。","終產物可抑制路徑前段酵素。","認為溫度越高酵素永遠越快。"))
PHOTO=P(("光合作用","葉綠體將光能轉為化學能，光反應產生ATP與NADPH，碳反應固定CO₂。","葉片受光後可累積澱粉。","把光合作用說成植物在白天的呼吸。"),("細胞呼吸","糖解在細胞質；有氧後續主要在線粒體，氧為末端電子接受者。","萌發種子會消耗氧並釋放CO₂與熱。","把呼吸運動吸吐氣等同細胞呼吸。"),("物質與能量","兩作用的物質互相關聯，但能量由光進入並逐步以熱散失，不循環。","植物白天同時呼吸與光合作用。","說能量像碳元素一樣在生態系循環。"))
DIV=P(("有絲分裂","有絲分裂產生兩個與母細胞染色體組數相同的子細胞。","二倍體體細胞分裂後形成兩個二倍體細胞。","說有絲分裂產生四個單倍體細胞。"),("減數分裂","減數分裂經兩次分裂形成四個單倍體細胞並產生遺傳變異。","二倍體生殖母細胞可形成四個單倍體配子。","說減數分裂只複製DNA而不降低染色體組數。"),("DNA複製","DNA在分裂前以半保留方式複製，姐妹染色分體之後分離。","複製後每條染色體含兩條姐妹染色分體。","把DNA複製與蛋白質轉譯混為一談。"))
GENE=P(("孟德爾遺傳","等位基因在配子形成時分離；完全顯性單因子雜交Aa×Aa表型比3:1。","Aa×Aa基因型比1 AA:2 Aa:1 aa。","不檢查顯性、單基因等條件就套3:1。"),("DNA與基因","基因是DNA上的功能序列，染色體含DNA與蛋白質，等位基因是同座位的不同版本。","人類同源染色體相同座位可帶不同等位基因。","把基因、DNA與染色體當成大小相同的同義詞。"),("基因表現","轉錄以DNA為模板合成RNA，轉譯在核糖體依mRNA密碼子合成多肽。","mRNA由細胞核輸出後在核糖體被轉譯。","說DNA在核糖體直接複製成蛋白質。"))
EVOL=P(("自然選擇","可遺傳變異造成繁殖成功差異，使適應環境的性狀比例跨世代改變。","抗藥性細菌在抗生素環境下較易留下後代。","說個體因需要而主動產生適應突變。"),("遺傳漂變","有限族群的等位基因頻率可因隨機抽樣改變，小族群效應較強。","瓶頸後倖存個體的基因頻率可能偶然偏離原族群。","把遺傳漂變與自然選擇說成同一個非隨機機制。"),("分類與親緣","現代分類以共同祖先與多種證據建立親緣假說。","DNA序列與同源構造可共同支持親緣關係。","只依外形相似就判定最近親。"))
HUMAN=P(("消化與吸收","消化把大分子分解為可吸收小分子，主要吸收在小腸進行。","澱粉消化後形成葡萄糖並由小腸吸收。","把消化主內容寫成粒線體細胞呼吸。"),("循環與呼吸運動","循環運送物質；呼吸運動使空氣進出肺，肺泡進行氣體交換。","氧由肺泡擴散入血，再由紅血球運送。","把人體呼吸系統混入植物卡爾文循環。"),("神經與內分泌","神經訊息快速而短暫，激素經血液運送、作用較慢且持久。","血糖升高可促進胰島素分泌。","把所有協調反應都歸為神經或都歸為激素。"))
ECO=P(("族群與群集","族群是同時同地同種個體；群集是同地多物種族群。","池塘中所有吳郭魚是一個族群，多種生物合為群集。","把群集加上非生物環境才稱生態系的層次混淆。"),("生態系與能量","生態系含群集與非生物環境，能量沿食物網流動並逐階散失。","草的化學能可經兔傳給鷹，部分以熱散失。","把能量流動說成封閉循環。"),("物質循環與演替","水、碳、氮在生物與環境間循環；演替是群集組成隨時間改變。","火災後土壤仍在的恢復屬次級演替。","把季節性個體數變化一律稱演替。"))
PLANT=P(("植物運輸","木質部主要運水與礦物質，韌皮部運輸糖等有機物。","葉片製造的蔗糖可由韌皮部運往根。","把木質部說成只向下運糖。"),("氣孔與蒸散","保衛細胞調節氣孔，蒸散拉力協助水柱上升。","乾旱時氣孔關閉可減少失水。","認為水只靠根部主動推送到樹冠。"),("植物調節","植物以激素與向性反應調整生長。","幼苗向光彎曲與生長素分布有關。","把植物反應說成需要神經系統。"))
METHOD=P(("科學問題","問題需可觀察或量測，假說須能被證據檢驗。","比較光照對幼苗生長可量測高度變化。","先決定答案再挑選支持資料。"),("變因與對照","實驗只改變自變因，量測應變因並控制其他條件。","測酵素溫度效應時各組使用相同酵素與底物量。","同時改變多個條件仍宣稱單一因果。"),("資料判讀","重複、圖表與統計用來評估變異，相關不等於因果。","多次量測平均並呈現散布比單次值可靠。","只看平均值而忽略樣本量與變異。"))
MAP={
"生命世界與科學方法":METHOD,"細胞構造與功能":CELL,"物質進出細胞":MEM,"營養與消化":HUMAN,"植物運輸":PLANT,"生物體的協調":HUMAN,"恆定性":HUMAN,"生殖":DIV,"遺傳":GENE,"演化":EVOL,"生物分類":EVOL,"生態與環境":ECO,
"生命現象與細胞":CELL,"細胞膜與物質運輸":MEM,"酵素與能量代謝":META,"光合作用與呼吸作用":PHOTO,"細胞分裂":DIV,"生殖與遺傳":GENE,"DNA與基因表現":GENE,"演化與分類":EVOL,"植物構造與功能":PLANT,"動物生理與恆定":HUMAN,"神經與內分泌":HUMAN,"免疫與健康":HUMAN,"族群與群集":ECO,"生態系與保育":ECO,"生物技術":GENE,"實驗設計":METHOD,"遺傳工程與倫理":GENE,"演化證據整合":EVOL,"生態模型":ECO,"人體系統整合":HUMAN,"生物多樣性":ECO,"科學閱讀":METHOD,"探究與實作":METHOD,"分科生物總複習":GENE}
FORM={"光合作用與呼吸作用":["光合作用：6CO₂+6H₂O+光能→C₆H₁₂O₆+6O₂。","有氧呼吸：C₆H₁₂O₆+6O₂→6CO₂+6H₂O+能量。"],"遺傳":["Aa×Aa：基因型1:2:1；完全顯性表型3:1。"],"生殖與遺傳":["Aa×Aa：基因型1:2:1；完全顯性表型3:1。"]}
def rewrite(path,batch):
 d=load_curriculum_js(path);units=[]
 for b in d["biology"]:
  if b.get("stage") in("junior_high","high_school"):
   for u in b["units"]:units.append((b["stage"],u))
 assert len(units)==36 and set(u["name"] for _,u in units)==set(MAP);counts={"junior_high":0,"high_school":0};failed=[];STATE.parent.mkdir(parents=True,exist_ok=True)
 for off in range(0,len(units),batch):
  for stage,u in units[off:off+batch]:
   u["lessonDetails"]=lesson(u["name"],stage,MAP[u["name"]],FORM.get(u["name"],[]));u["lessonDetails"]["readableLesson"]=list(u["lessonDetails"]["lessonText"]);z=semantic_issues("biology_"+stage,u["name"],u["lessonDetails"])
   if z:failed.append({"stage":stage,"title":u["name"],"issues":z})
   else:counts[stage]+=1
  write_curriculum_js(path,d);STATE.write_text(json.dumps({**counts,"failed":failed,"last_offset":min(off+batch,len(units)),"batch_size":batch},ensure_ascii=False,indent=2),encoding="utf-8")
 return{**counts,"failed":failed,"total":len(units)}
def main():
 a=argparse.ArgumentParser();a.add_argument("--file",type=Path,default=FILE);a.add_argument("--batch-size",type=int,default=4);a.add_argument("--no-backup",action="store_true");x=a.parse_args()
 if not x.no_backup:b=x.file.with_name(x.file.name+f".before_biology_all_stages_{datetime.now():%Y%m%d_%H%M%S}");shutil.copy2(x.file,b);print(f"backup={b}")
 r=rewrite(x.file,x.batch_size);print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if not r["failed"] else 2
if __name__=="__main__":raise SystemExit(main())
