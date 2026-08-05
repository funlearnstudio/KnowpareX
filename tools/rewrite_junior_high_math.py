#!/usr/bin/env python3
"""Rewrite all 36 junior-high mathematics units, four per checkpoint."""
from __future__ import annotations
import argparse,json,shutil,sys
from datetime import datetime
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/"src"))
from tools.rewrite_high_school_math import C  # noqa:E402
from knowparex.curriculum_adapter import load_curriculum_js  # noqa:E402
from knowparex.curriculum_rebuild import write_curriculum_js  # noqa:E402
from knowparex.curriculum_quality import semantic_issues  # noqa:E402
FILE=ROOT/"src/knowparex/data/curriculum_integrated.js";STATE=ROOT/".knowparex_rewrite/junior_high_math.json"
def q(t,e,x,c,f=[]):return(t,e,x,c,f)
J={
"integer":q("正負數與數線","正數在0右側、負數在0左側；相反數距0相等而方向相反，絕對值是到0的距離。","-3+5=2，|-7|=7。","負數相加時只看絕對值而漏掉符號。",["|x|≥0。"]),
"index":q("整數指數律","同底數相乘指數相加、相除指數相減；除法要求底數不為0。","2³×2⁴=2⁷=128；2⁵/2²=2³=8。","把(a+b)²錯寫成a²+b²。",["a^m/a^n=a^(m-n)，a≠0。"]),
"fraction":q("分數運算","分數加減先通分，乘法分子分母相乘，除以非零數等於乘其倒數。","3/4-1/6=9/12-2/12=7/12。","分子分母分別相加處理分數加法。",["a/b÷c/d=ad/(bc)，b,c,d≠0。"]),
"linear":q("一元一次方程式","方程式兩邊做相同可逆運算可保持解集合，含分母時先標記分母不為0。","3x-5=10得3x=15，所以x=5。","移項只改符號卻不理解是兩邊同加減。",[]),
"ratio":q("比例與反比例","正比例y=kx；反比例y=k/x且x≠0，兩者圖形與變化方式不同。","y=3x時x=4得y=12；y=12/x時x=4得y=3。","把反比例誤寫成y=kx或允許x=0。",["正比例：y=kx。","反比例：y=k/x，x≠0。"]),
"coord":q("坐標平面","點(x,y)先沿水平x軸再沿垂直y軸定位，象限由兩座標符號決定。","(-2,3)位於第二象限。","把(x,y)順序顛倒。",[]),
"system":q("二元一次聯立方程式","聯立方程式的解須同時滿足兩式，可用代入或消去法。","x+y=7、x-y=1相加得2x=8，故(x,y)=(4,3)。","只滿足其中一式就當成聯立解。",[]),
"ineq":q("一元一次不等式","不等式兩邊同乘或同除負數時不等號方向必須反轉。","-2x>6同除-2得x<-3。","除以負數後忘記反轉不等號。",[]),
"triangle":q("三角形性質","三角形內角和180°，任兩邊和大於第三邊。","邊長3、4、5可成三角形，且3+4>5。","只檢查最短兩邊以外的無關組合。",["A+B+C=180°。","a+b>c（任兩邊）。"]),
"parallel":q("平行線與四邊形","平行線被截線所成同位角相等；平行四邊形兩組對邊平行且相等。","平行四邊形一內角70°，相鄰角110°。","把一組對邊平行的梯形直接判為平行四邊形。",[]),
"pythag":q("勾股定理","只有直角三角形才有兩股平方和等於斜邊平方；逆定理可用邊長判斷直角。","直角三角形兩股6、8，斜邊√(36+64)=10。","在非直角三角形直接套a²+b²=c²。",["直角三角形：a²+b²=c²，c為斜邊。"]),
"factor":q("因式分解","因式分解把多項式寫成乘積，可用提公因式、公式或分組。","x²-5x+6=(x-2)(x-3)。","把因式分解等號右側仍寫成加法形式。",["a²-b²=(a-b)(a+b)。"]),
"rational":q("分式與根式","分式分母不得為0；實數範圍偶次根內須非負，化簡不能改變定義域。","√50=5√2；1/(x-2)要求x≠2。","約分後忘記原分母排除值，或令√(-1)為實數。",["√(a²)=|a|（a為實數）。"]),
"proof":q("幾何推理","證明要由已知、定義與定理逐步推出結論，圖形外觀不能代替理由。","由兩直線平行可用錯角相等，再配合ASA證明三角形全等。","把圖上看似相等當成已知條件。",[]),
"congruent":q("三角形全等","全等表示形狀與大小完全相同，可用SSS、SAS、ASA、AAS或直角三角形RHS判定。","兩三角形兩邊及夾角分別相等，可由SAS判定全等。","用SSA一般情形判定全等。",[]),
"similar":q("相似形","相似形對應角相等、對應邊成同一比例；全等是相似比為1的特殊情形。","3-4-5與6-8-10三角形相似，對應邊比1:2。","把面積比誤認為邊長比，或把相似直接說成全等。",["相似比k時，周長比k、面積比k²。"]),
"circlejunior":q("圓、弦與切線","圓心到弦的垂線平分弦；切線垂直於通過切點的半徑。","半徑5的圓中，圓心到弦距3，半弦長√(25-9)=4。","把任一與半徑垂直的直線都當切線，未確認切點。",[]),
"inscribed":q("圓周角","同弧所對圓周角相等，圓周角等於同弧圓心角的一半；直徑所對圓周角90°。","同弧圓心角120°，圓周角60°。","把圓周角直接等同圓心角。",["同弧：圓周角=圓心角/2。"]),
"quadeq":q("一元二次方程式","ax²+bx+c=0要求a≠0，可用因式分解、配方法或公式解。","x²-5x+6=0得(x-2)(x-3)=0，解2、3。","因式乘積為0時漏掉其中一個解。",["x=[-b±√(b²-4ac)]/(2a)，a≠0且實根需b²-4ac≥0。"]),
"box":q("盒狀圖","盒狀圖呈現最小值、Q1、中位數、Q3與最大值，四分位距IQR=Q3-Q1。","資料1,2,3,4,5的中位數3。","把盒子寬度當成資料筆數或頻率。",["IQR=Q3-Q1。"]),
"solid":q("立體圖形","體積與表面積單位分別是長度三次方與二次方；展開圖須保持面與邊的連接。","半徑3、高5的圓柱體積π×3²×5=45π。","把表面積平方單位與體積立方單位混用。",["圓柱體積V=πr²h，r>0、h>0。"]),
"frequency":q("次數、頻率與機率","次數是出現筆數，頻率是次數除以總次數；理論機率來自模型，實驗頻率只是估計。","擲硬幣100次出現正面56次，正面頻率0.56，但公平硬幣理論機率仍0.5。","把一次實驗頻率直接當成永遠不變的理論機率。",["頻率=次數/總次數，0≤頻率≤1。"]),
}
C.update(J)
U={"整數與數線":["integer","abs","index"],"因數倍數與分數運算":["fraction","integer","index"],"一元一次方程式":["linear","algebra","fraction"],"比與比例式":["ratio","fraction","linear"],"坐標平面":["coord","line","integer"],"資料與統計":["stats","frequency","model"],"二元一次聯立方程式":["system","linear","line"],"一元一次不等式":["ineq","integer","linear"],"線型函數":["line","ratio","coord"],"三角形基本性質":["triangle","pythag","proof"],"平行與四邊形":["parallel","triangle","proof"],"機率初步":["prob","frequency","count"],"乘法公式與多項式":["algebra","poly","index"],"平方根與畢氏定理":["radical","pythag","rational"],"因式分解":["factor","algebra","quadeq"],"分式與根式運算":["rational","radical","fraction"],"一次函數應用":["line","model","ratio"],"幾何證明入門":["proof","triangle","parallel"],"等差數列與級數":["sequence","series","algebra"],"三角形全等":["congruent","triangle","proof"],"平行四邊形與梯形":["parallel","triangle","congruent"],"相似形入門":["similar","triangle","ratio"],"圓的基本性質":["circlejunior","circle","pythag"],"統計與盒狀圖":["box","stats","frequency"],"比例線段與相似形":["similar","ratio","parallel"],"圓周角與切線":["inscribed","circlejunior","circle"],"二次函數":["quadratic","parabola","quadeq"],"一元二次方程式":["quadeq","factor","quadratic"],"機率與排列組合入門":["prob","count","frequency"],"會考代數複習":["linear","factor","quadeq"],"二次函數應用":["quadratic","model","quadeq"],"立體圖形":["solid","pythag","circle"],"推理證明整合":["proof","congruent","similar"],"幾何與坐標整合":["coord","line","circle"],"資料判讀":["stats","frequency","prob"],"會考總複習":["linear","pythag","prob"]}
def details(t:str)->dict[str,Any]:
 r=[C[k] for k in U[t]];ps=[f"{t}聚焦於{r[0][0]}與{r[1][0]}：{r[0][1]}；{r[1][1]}",f"本單元也運用{r[2][0]}：{r[2][1]}解題時須核對定義、條件、符號、圖形與單位。"]
 fs=[]
 for a in r:
  for f in a[4]:
   if f not in fs:fs.append(f)
 return{"lessonText":ps,"readableLesson":ps,"formulas":fs,"keyPoints":[{"topic":a[0],"explanation":a[1],"example":f"{a[0]}例：{a[2]}","commonTrap":a[3]} for a in r]}
def rewrite(path:Path,batch:int):
 d=load_curriculum_js(path);us=[u for b in d["math"] if b.get("stage")=="junior_high" for u in b["units"]];assert set(u["name"] for u in us)==set(U);done=0;failed=[];STATE.parent.mkdir(parents=True,exist_ok=True)
 for o in range(0,len(us),batch):
  for u in us[o:o+batch]:u["lessonDetails"]=details(u["name"]);z=semantic_issues("math",u["name"],u["lessonDetails"]);failed.append({"title":u["name"],"issues":z}) if z else None;done+=not z
  write_curriculum_js(path,d);STATE.write_text(json.dumps({"subject":"math","stage":"junior_high","completed":done,"failed":failed,"last_offset":min(o+batch,len(us)),"batch_size":batch},ensure_ascii=False,indent=2),encoding="utf-8")
 return{"total":len(us),"completed":done,"failed":failed}
def main():
 a=argparse.ArgumentParser();a.add_argument("--file",type=Path,default=FILE);a.add_argument("--batch-size",type=int,default=4);a.add_argument("--no-backup",action="store_true");x=a.parse_args()
 if not x.no_backup:b=x.file.with_name(x.file.name+f".before_junior_high_math_{datetime.now():%Y%m%d_%H%M%S}");shutil.copy2(x.file,b);print(f"backup={b}")
 r=rewrite(x.file,x.batch_size);print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if not r["failed"] else 2
if __name__=="__main__":raise SystemExit(main())
