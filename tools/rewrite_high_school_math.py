#!/usr/bin/env python3
"""Checkpointed rewrite of all 36 high-school mathematics units.

Automated checks do not constitute formal mathematics-teacher review.
"""
from __future__ import annotations
import argparse,json,shutil,sys
from datetime import datetime
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from knowparex.curriculum_adapter import load_curriculum_js  # noqa:E402
from knowparex.curriculum_rebuild import write_curriculum_js  # noqa:E402
from knowparex.curriculum_quality import semantic_issues  # noqa:E402
FILE=ROOT/"src/knowparex/data/curriculum_integrated.js";STATE=ROOT/".knowparex_rewrite/high_school_math.json"
# key: topic, explanation, checked example, misconception, formulas
C:dict[str,tuple[str,str,str,str,list[str]]]={
"real":("實數與區間","實數包含有理數與無理數，可在數線上排序；區間端點是否包含須由括號判讀。","x≥-2且x<3寫成[-2,3)。","把無理數誤認為不能在數線上表示。",[]),
"abs":("絕對值","|x-a|表示x與a在數線上的距離，因此永遠非負。","|x-2|≤3等價於-1≤x≤5。","解|x|=-2而忽略絕對值不可能為負。",["|x-a|≤r ⇔ a-r≤x≤a+r（r≥0）。"]),
"radical":("根式條件","實數範圍內偶次根的被開方數須非負，分母另須不為0。","√(x-1)的定義域是x≥1；1/√(x-1)則為x>1。","只檢查根號而漏掉分母不能為0。",[]),
"algebra":("代數式運算","展開、因式分解與約分都須保持等式成立條件，約分前先標記不可為0的因式。","(x²-1)/(x-1)=x+1，但原式限定x≠1。","約分後忘記保留原分式的排除值。",[]),
"poly":("多項式與餘式","多項式除法滿足f(x)=q(x)g(x)+r(x)，且r次數低於g。","f(x)=x²+3x+2除以x+1的餘數f(-1)=0。","把餘式定理套到除式不是x-a的情形而不轉換。",["餘式定理：f(x)除以x-a的餘數為f(a)。"]),
"line":("直線斜率與方程","非鉛直直線斜率是y變化量除以x變化量；鉛直線斜率不存在。","過(1,2)、(3,6)的直線斜率2，方程y-2=2(x-1)。","分母x₂-x₁=0時仍計算斜率。",["m=(y₂-y₁)/(x₂-x₁)，x₂≠x₁。","點斜式：y-y₁=m(x-x₁)。"]),
"circle":("圓的方程","圓由到固定中心等距的點組成，半徑必須為正。","(x-2)²+(y+1)²=9的圓心(2,-1)、半徑3。","從(x-h)²+(y-k)²讀圓心時漏改括號內符號。",["(x-h)²+(y-k)²=r²，r>0。"]),
"quadratic":("二次函數","二次函數y=ax²+bx+c要求a≠0，圖形是拋物線，a的正負決定開口。","y=2x²-8x+5的對稱軸x=2，頂點值-3。","用兩點斜率作為二次函數全圖的固定斜率。",["y=ax²+bx+c，a≠0。","對稱軸x=-b/(2a)。"]),
"parabola":("拋物線焦準定義","拋物線是到焦點與準線距離相等的點集，標準式須辨認開口方向與參數p。","y²=8x可寫y²=4px，故p=2、焦點(2,0)、準線x=-2。","把4p直接當成焦距p。",["y²=4px：焦點(p,0)、準線x=-p，p≠0。"]),
"model":("建模流程","建模需界定變數、單位、假設與適用範圍，再用資料估參數並驗證殘差。","計程車費可在固定起跳價與每公里費率假設下建立分段線性模型。","只因模型通過已知資料點就宣稱能無限外插。",[]),
"sequence":("數列","數列是依正整數索引排列的數；等差看相鄰差，等比看相鄰比且除數不為0。","等差數列3,7,11,…的a₁₀=3+9×4=39。","把第n項與前n項和混為一談。",["等差：a_n=a₁+(n-1)d。","等比：a_n=a₁r^(n-1)。"]),
"series":("級數求和","級數是數列各項相加，公式需符合等差或等比結構及項數條件。","1+2+⋯+100=100×101/2=5050。","無限等比級數在|r|≥1時仍套收斂公式。",["等差和：S_n=n(a₁+a_n)/2。","無限等比和：S=a₁/(1-r)，|r|<1。"]),
"count":("排列與組合","排列關心順序，組合只關心選取集合；計數前先判斷是否可重複。","從5人選主席與副主席有P(5,2)=20種；只選2名代表有C(5,2)=10種。","把組合數直接當成機率，未除以等可能樣本數。",["P(n,r)=n!/(n-r)!。","C(n,r)=n!/[r!(n-r)!]，0≤r≤n。"]),
"prob":("機率","等可能有限樣本中，事件機率是有利結果數除以樣本數，必介於0與1。","公平骰子擲出偶數的機率3/6=1/2。","把有利排列數直接報為機率或得到大於1的答案。",["P(A)=|A|/|S|（有限等可能），0≤P(A)≤1。"]),
"stats":("描述統計","平均數描述中心但受極端值影響，中位數較穩健；標準差描述資料對平均數的散布。","資料1,2,2,5的平均2.5、中位數2。","把標準差當成資料單位平方。",["x̄=Σx_i/n。","母體變異數σ²=Σ(x_i-μ)²/N。"]),
"exp":("指數函數","指數函數f(x)=a^x要求a>0且a≠1，定義域為全體實數、值域為正實數。","2^(-3)=1/8；f(x)=2^x為遞增。","把(a+b)^x錯拆成a^x+b^x。",["a^(x+y)=a^x a^y；a>0。","a^(-x)=1/a^x；a>0。"]),
"log":("對數函數","log_a x是a^y=x的反函數表示，底數a>0且a≠1，真數x>0。","log₂8=3；log₁₀0.01=-2。","漏寫底數與真數條件，或把log(x+y)拆成logx+logy。",["log_a(xy)=log_ax+log_ay，x,y>0，a>0且a≠1。","log_a(x/y)=log_ax-log_ay，x,y>0。"]),
"trigratio":("三角比","直角三角形中sin、cos、tan由邊長比定義；tanθ要求cosθ≠0。","3-4-5三角形對較小銳角有sinθ=3/5、cosθ=4/5。","未辨認對邊與鄰邊，或在tan未定義角度硬套公式。",["tanθ=sinθ/cosθ，cosθ≠0。"]),
"trig":("三角函數","弧度使角度與弧長直接連結；sin、cos定義於所有實數，tan在cosx=0時未定義。","sin(π/6)=1/2，cosπ=-1。","混用度數與弧度，或漏掉tan定義域。",["sin²x+cos²x=1。","tanx=sinx/cosx，x≠π/2+kπ。"]),
"triggraph":("三角圖形與恆等式","y=Asin(Bx+C)+D的振幅|A|，B≠0時週期2π/|B|；恆等式須在兩側有定義處成立。","y=3sin(2x)振幅3、週期π。","把恆等式當成可忽略分母為0限制的方程。",["sin(α±β)=sinαcosβ±cosαsinβ。","週期T=2π/|B|，B≠0。"]),
"vec2":("平面向量","向量有大小與方向，座標運算逐分量進行；內積連結夾角與投影。","u=(1,2)、v=(3,-1)，u+v=(4,1)，u·v=1。","把向量大小與向量本身相加減混用。",["u·v=|u||v|cosθ。","|u|=√(u₁²+u₂²)。"]),
"space":("空間幾何","空間中的點、線、面關係需用方向與法向量判斷，平面圖投影可能造成錯覺。","方向向量(1,0,0)與法向量(0,0,1)內積0，對應直線方向平行該平面。","從透視圖直接判斷兩線相交。",[]),
"matrix":("矩陣運算","矩陣加法要求同型；AB可乘需A欄數等於B列數，且通常AB≠BA。","[[1,2],[0,1]][[2],[3]]=[[8],[3]]。","逐元素相乘誤當成矩陣乘法。",["若A為m×n、B為n×p，則AB為m×p。"]),
"transform":("線性變換","線性變換保持向量加法與純量倍，矩陣的欄向量是基底向量的像。","矩陣[[0,-1],[1,0]]把(1,0)轉成(0,1)，表示逆時針旋轉90°。","平移含常數項卻直接稱為二維線性變換。",["T(u+v)=T(u)+T(v)，T(cu)=cT(u)。"]),
"conic":("圓錐曲線","橢圓、拋物線、雙曲線可由焦點與距離條件定義；標準式參數不可混放。","x²/9+y²/4=1為橢圓，c=√(9-4)=√5。","把橢圓a²=b²+c²與雙曲線c²=a²+b²混用。",["橢圓：x²/a²+y²/b²=1，a>b>0，c²=a²-b²。","雙曲線：x²/a²-y²/b²=1，a,b>0，c²=a²+b²。"]),
"vec3":("空間向量","三維向量逐分量運算；內積判斷夾角，叉積產生垂直於兩向量的法向量。","(1,0,0)×(0,1,0)=(0,0,1)。","把叉積當成可交換，忽略v×u=-(u×v)。",["u·v=u₁v₁+u₂v₂+u₃v₃。","|u×v|=|u||v|sinθ。"]),
"condprob":("條件機率","P(A|B)是在B已發生的縮小樣本空間中計算A，要求P(B)>0。","袋中3紅2藍，不放回先抽紅後再抽紅的條件機率為2/4=1/2。","把P(A|B)與P(B|A)互換。",["P(A|B)=P(A∩B)/P(B)，P(B)>0。"]),
"bayes":("貝氏定理","貝氏定理用先驗機率與似然更新後驗機率，分母是觀察證據的全機率。","疾病率1%、敏感度90%、偽陽性率5%時，陽性後患病率=0.009/(0.009+0.0495)≈0.1538。","忽略低基準率而把敏感度直接當後驗機率。",["P(A|B)=P(B|A)P(A)/P(B)，P(B)>0。"]),
"infer":("統計推論","樣本統計量用來估計母體參數；抽樣方法、標準誤與信賴程度共同影響不確定性。","同變異下樣本數由100增至400，平均數標準誤減半。","把95%信賴區間解讀為已算出的固定區間有95%隨機機率含參數。",["SE(x̄)=σ/√n（σ已知或作理論表示）。"]),
"limit":("極限","極限描述x接近某值時f(x)的趨勢，不要求函數在該點有定義或等於極限。","lim(x→2)(x²-4)/(x-2)=lim(x→2)(x+2)=4，但原式x≠2。","直接代入得到0/0後把極限判為0。",["若極限存在：lim(f+g)=limf+limg。"]),
"deriv":("導數","導數是差商在時間或位置增量趨近0的極限，是瞬時變化率；平均變化率只使用有限區間。","f(x)=x²，f′(3)=lim(h→0)[(3+h)²-9]/h=6。","把區間平均變化率直接當作端點導數結論。",["f′(x)=lim(h→0)[f(x+h)-f(x)]/h（極限存在）。"]),
"derivapp":("導數應用","導數符號判斷增減，臨界點需連同端點與不可微點檢查；f′=0只是極值候選。","f(x)=x²-4x在[0,5]的臨界點x=2，值-4；端點值0、5，故最小值-4、最大值5。","看到f′(c)=0就必然宣稱c是極值。",[]),
"integral":("積分","不定積分是一族反導函數，須加常數C；定積分是帶號累積量，可由微積分基本定理計算。","∫2x dx=x²+C；∫₀²2x dx=[x²]₀²=4。","不定積分漏寫+C，或把定積分一律當正面積。",["∫_a^b f(x)dx=F(b)-F(a)，F′=f。"]),
"integralapp":("定積分應用","幾何面積需積分上函數減下函數並保證順序，跨越x軸時要分段取絕對面積。","y=x與y=x²在[0,1]間面積∫₀¹(x-x²)dx=1/6。","直接積分f而未檢查正負就稱為幾何面積。",[]),
"investigate":("數學探究","探究從可檢驗問題出發，提出猜想、找例證與反例，再以推理或證明界定成立條件。","觀察前幾項得到規律後，仍可用數學歸納法證明對所有正整數成立。","用有限幾個例子取代一般證明。",[]),
}
U={
"實數與絕對值":["real","abs","radical"],"式的運算與多項式":["algebra","poly","radical"],"直線方程式":["line","vec2","algebra"],"圓方程式":["circle","line","algebra"],"多項式函數":["poly","quadratic","algebra"],"數學建模入門":["model","line","stats"],
"數列級數":["sequence","series","algebra"],"排列組合":["count","algebra","prob"],"機率":["prob","count","condprob"],"數據分析":["stats","prob","model"],"指數與對數":["exp","log","algebra"],"三角比":["trigratio","trig","circle"],
"三角函數":["trig","trigratio","triggraph"],"三角恆等與圖形":["triggraph","trig","algebra"],"平面向量":["vec2","line","circle"],"空間概念":["space","vec3","line"],"矩陣運算":["matrix","algebra","transform"],"線性變換":["transform","matrix","vec2"],
"圓錐曲線":["conic","parabola","circle"],"空間向量":["vec3","space","line"],"條件機率":["condprob","prob","count"],"貝氏定理":["bayes","condprob","prob"],"統計推論入門":["infer","stats","prob"],"數學探究專題":["investigate","model","stats"],
"極限概念":["limit","algebra","sequence"],"微分與導數":["deriv","limit","line"],"導數應用":["derivapp","deriv","quadratic"],"積分概念":["integral","limit","deriv"],"定積分應用":["integralapp","integral","circle"],"學測數學總複習":["quadratic","prob","vec2"],
"微積分整合":["limit","deriv","integral"],"機率統計整合":["prob","stats","infer"],"向量矩陣整合":["vec2","vec3","matrix"],"函數圖形整合":["quadratic","exp","triggraph"],"素養混合題":["model","prob","investigate"],"分科測驗總複習":["derivapp","integralapp","condprob"]}
def details(title:str)->dict[str,Any]:
 rows=[C[k] for k in U[title]]
 p1=f"{title}聚焦於{rows[0][0]}與{rows[1][0]}：{rows[0][1]}；{rows[1][1]}"
 p2=f"本單元也需要{rows[2][0]}：{rows[2][1]}計算時須逐步核對定義域、參數條件、符號與結果範圍。"
 formulas=[]
 for r in rows:
  for f in r[4]:
   if f not in formulas: formulas.append(f)
 return {"lessonText":[p1,p2],"readableLesson":[p1,p2],"formulas":formulas,"keyPoints":[{"topic":r[0],"explanation":r[1],"example":f"{r[0]}例：{r[2]}","commonTrap":r[3]} for r in rows]}
def rewrite(path:Path,batch:int)->dict[str,Any]:
 d=load_curriculum_js(path);units=[u for b in d["math"] if b.get("stage")=="high_school" for u in b.get("units",[])]
 titles=[u["name"] for u in units]
 if set(titles)!=set(U):raise SystemExit(f"白名單不一致 missing={set(titles)-set(U)} extra={set(U)-set(titles)}")
 done=0;failed=[];STATE.parent.mkdir(parents=True,exist_ok=True)
 for off in range(0,len(units),max(1,batch)):
  for u in units[off:off+max(1,batch)]:
   u["lessonDetails"]=details(u["name"]);issues=semantic_issues("math",u["name"],u["lessonDetails"])
   if issues:failed.append({"title":u["name"],"issues":issues})
   else:done+=1
  write_curriculum_js(path,d);STATE.write_text(json.dumps({"subject":"math","stage":"high_school","completed":done,"failed":failed,"last_offset":min(off+batch,len(units)),"batch_size":batch},ensure_ascii=False,indent=2),encoding="utf-8")
 return {"total":len(units),"completed":done,"failed":failed}
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--file",type=Path,default=FILE);ap.add_argument("--batch-size",type=int,default=4);ap.add_argument("--no-backup",action="store_true");a=ap.parse_args()
 if not a.no_backup:
  b=a.file.with_name(a.file.name+f".before_high_school_math_{datetime.now():%Y%m%d_%H%M%S}");shutil.copy2(a.file,b);print(f"backup={b}")
 r=rewrite(a.file,a.batch_size);print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if not r["failed"] else 2
if __name__=="__main__":raise SystemExit(main())
