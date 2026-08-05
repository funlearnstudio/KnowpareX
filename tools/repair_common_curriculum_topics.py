#!/usr/bin/env python3
"""Repair common curriculum topics found by manual QA.

Run from the repository root:

    python3 tools/repair_common_curriculum_topics.py --write

The script updates ``src/knowparex/data/curriculum_integrated.js`` through the
existing curriculum rebuild pipeline.  It does not change the JavaScript data
schema.  A timestamped backup is created before writing.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from knowparex.curriculum_adapter import load_curriculum_js
from knowparex.curriculum_rebuild import (
    CURATED_UNITS,
    audit_data,
    rebuild_data,
    write_curriculum_js,
)


REPAIRS: dict[tuple[str, str], dict[str, Any]] = {
    ("math", "二次函數"): {
        "paragraphs": [
            "二次函數的一般形式是y=ax²+bx+c，其中a不等於0。它的圖形是拋物線；a大於0時開口向上，a小於0時開口向下，|a|愈大時圖形通常愈窄。",
            "拋物線的對稱軸是x=-b/(2a)，頂點位於對稱軸上。把對稱軸的x值代回函數即可求出頂點的y值。頂點是函數圖形的最高點或最低點。",
            "方程式ax²+bx+c=0的實數解對應圖形與x軸的交點。判別式Δ=b²-4ac可判斷交點數量：Δ>0有兩個相異實根，Δ=0有一個重根，Δ<0沒有實根。",
        ],
        "key_points": [
            {"topic": "一般形式", "explanation": "二次函數寫成y=ax²+bx+c，且a≠0。", "example": "y=2x²-3x+1是二次函數，其中a=2、b=-3、c=1。"},
            {"topic": "開口方向", "explanation": "a的正負決定拋物線開口方向，|a|影響圖形寬窄。", "example": "y=-x²+4開口向下，y=3x²開口向上且較窄。"},
            {"topic": "對稱軸與頂點", "explanation": "對稱軸為x=-b/(2a)，頂點在這條直線上。", "example": "y=2x²-8x+3的對稱軸為x=2，頂點為(2,-5)。"},
            {"topic": "零點與判別式", "explanation": "零點是ax²+bx+c=0的解，判別式決定實根數量。", "example": "x²-5x+6=0可分解為(x-2)(x-3)=0，所以零點為2與3。"},
        ],
        "formulas": [
            "一般形式：y=ax²+bx+c，a≠0。",
            "對稱軸：x=-b/(2a)。",
            "判別式：Δ=b²-4ac。",
        ],
    },
    ("science", "電流電壓與電阻"): {
        "paragraphs": [
            "電流是電荷通過導線截面的速率，電壓表示推動電荷移動的電位差，電阻則描述元件阻礙電流的程度。三者是分析直流電路的核心物理量。",
            "在溫度與元件狀態近似不變時，歐姆定律可寫成V=IR。電壓固定時，電阻愈大，電流愈小；電阻固定時，電壓愈大，電流愈大。",
            "串聯電路各處電流相同，總電阻等於各電阻相加；並聯電路各支路電壓相同，總電阻的倒數等於各支路電阻倒數之和。量測時，安培計串聯、伏特計並聯。",
        ],
        "key_points": [
            {"topic": "電流", "explanation": "電流表示單位時間內通過截面的電荷量，單位是安培A。", "example": "若6 V電池接3 Ω電阻，電流為2 A。"},
            {"topic": "電壓", "explanation": "電壓是兩點間的電位差，單位是伏特V。", "example": "電池兩端可提供固定的電位差以推動電荷。"},
            {"topic": "電阻", "explanation": "電阻表示元件阻礙電流的程度，單位是歐姆Ω。", "example": "在相同電壓下，6 Ω電阻的電流小於3 Ω電阻。"},
            {"topic": "歐姆定律", "explanation": "對歐姆性元件，電壓、電流與電阻滿足V=IR。", "example": "V=12 V、R=4 Ω時，I=3 A。"},
            {"topic": "串聯與並聯", "explanation": "串聯電流相同；並聯電壓相同。", "example": "2 Ω與4 Ω串聯時總電阻為6 Ω。"},
        ],
        "formulas": [
            "歐姆定律：V=IR。",
            "串聯：R總=R₁+R₂+⋯。",
            "並聯：1/R總=1/R₁+1/R₂+⋯。",
            "電功率：P=VI=I²R=V²/R。",
        ],
    },
    ("physics", "力與牛頓定律"): {
        "paragraphs": [
            "力會改變物體的運動狀態。分析受力時，要先選定研究物體並畫受力圖，只列出真正作用在該物體上的力，再決定正方向。",
            "牛頓第二定律指出，物體所受合力等於質量乘以加速度，即ΣF=ma。加速度方向與合力方向相同；若合力為零，物體可能靜止，也可能做等速度直線運動。",
            "牛頓第一定律描述慣性，牛頓第三定律描述作用力與反作用力。第三定律的一對力大小相等、方向相反，但作用在不同物體上，因此不能在同一物體的受力圖中互相抵消。",
        ],
        "key_points": [
            {"topic": "合力", "explanation": "合力是所有外力的向量和。", "example": "向右18 N、向左8 N時，合力為向右10 N。"},
            {"topic": "牛頓第二定律", "explanation": "合力、質量與加速度滿足ΣF=ma。", "example": "5 kg物體受10 N合力時，加速度為2 m/s²。"},
            {"topic": "慣性", "explanation": "物體傾向維持原本的靜止或等速度運動狀態。", "example": "車突然煞車時，乘客身體會傾向繼續向前。"},
            {"topic": "作用力與反作用力", "explanation": "兩力大小相等、方向相反，且作用在不同物體上。", "example": "人推牆時，牆也以同樣大小的力推人。"},
        ],
        "formulas": [
            "牛頓第二定律：ΣF=ma。",
            "重量：W=mg。",
        ],
    },
    ("science", "氧化還原"): {
        "paragraphs": [
            "氧化還原反應包含電子轉移。氧化是失去電子或氧化數上升；還原是得到電子或氧化數下降。兩個過程必定同時發生。",
            "使其他物質氧化的物質稱為氧化劑，它本身被還原；使其他物質還原的物質稱為還原劑，它本身被氧化。判斷時應追蹤元素反應前後的氧化數。",
            "例如Zn+Cu²⁺→Zn²⁺+Cu中，鋅由0變成+2，失去電子而被氧化；銅離子由+2變成0，得到電子而被還原。",
        ],
        "key_points": [
            {"topic": "氧化", "explanation": "失去電子或氧化數上升稱為氧化。", "example": "Zn→Zn²⁺+2e⁻是氧化半反應。"},
            {"topic": "還原", "explanation": "得到電子或氧化數下降稱為還原。", "example": "Cu²⁺+2e⁻→Cu是還原半反應。"},
            {"topic": "氧化劑與還原劑", "explanation": "氧化劑本身被還原，還原劑本身被氧化。", "example": "在Zn與Cu²⁺反應中，Cu²⁺是氧化劑，Zn是還原劑。"},
        ],
        "formulas": [
            "氧化：失去電子，氧化數上升。",
            "還原：得到電子，氧化數下降。",
            "Zn→Zn²⁺+2e⁻；Cu²⁺+2e⁻→Cu。",
        ],
    },
    ("chemistry", "莫耳與化學計量"): {
        "paragraphs": [
            "莫耳是物質量的單位。1 mol物質包含亞佛加厥常數個粒子，約為6.022×10²³個。粒子可以是原子、分子、離子或其他指定微粒。",
            "質量與莫耳數可用n=m/M換算，其中m是質量、M是莫耳質量。粒子數與莫耳數可用N=nN_A換算。計算前要先確認物質種類與單位。",
            "化學計量題先配平反應式，再把已知量換算成莫耳，依係數比求未知物質的莫耳數，最後轉回題目要求的質量、體積或粒子數。",
        ],
        "key_points": [
            {"topic": "莫耳", "explanation": "1 mol含約6.022×10²³個指定粒子。", "example": "1 mol水分子含約6.022×10²³個水分子。"},
            {"topic": "莫耳質量", "explanation": "莫耳質量是每莫耳物質的質量，常用單位為g/mol。", "example": "水的莫耳質量約為18 g/mol，因此36 g水約為2 mol。"},
            {"topic": "化學計量", "explanation": "配平後的係數表示各物質的莫耳比。", "example": "2H₂+O₂→2H₂O表示2 mol氫氣與1 mol氧氣生成2 mol水。"},
            {"topic": "限制試劑", "explanation": "最先被消耗完的反應物決定理論產量。", "example": "比較各反應物可生成的產物莫耳數，較小者對應限制試劑。"},
        ],
        "formulas": [
            "粒子數：N=nN_A，N_A≈6.022×10²³ mol⁻¹。",
            "質量換算：n=m/M。",
            "理想氣體：PV=nRT。",
            "百分產率=實際產量÷理論產量×100%。",
        ],
    },
    ("biology", "演化"): {
        "paragraphs": [
            "生物演化是族群的遺傳組成隨世代改變，而不是個體在一生中因需要而主動改變。突變與基因重組提供可遺傳變異。",
            "自然選擇發生在具有可遺傳差異的族群中。某些性狀使個體在特定環境下留下較多後代，相關等位基因便可能在後代族群中增加。",
            "除自然選擇外，遺傳漂變、基因流動與非隨機交配也會改變族群的遺傳組成。化石、同源構造與分子序列可用來推論共同祖先與親緣關係。",
        ],
        "key_points": [
            {"topic": "族群演化", "explanation": "演化是族群遺傳組成跨世代改變。", "example": "抗藥性細菌比例在抗生素環境下逐代增加，是族群層次的變化。"},
            {"topic": "可遺傳變異", "explanation": "突變與重組產生能遺傳給後代的差異。", "example": "同一族群中個體可能具有不同等位基因。"},
            {"topic": "自然選擇", "explanation": "在特定環境下留下較多後代的可遺傳性狀可能增加。", "example": "環境改變後，較適合該環境的個體平均留下更多後代。"},
            {"topic": "其他演化機制", "explanation": "遺傳漂變與基因流動也能改變等位基因頻率。", "example": "小族群可能因隨機事件失去某些等位基因。"},
        ],
        "formulas": [
            "哈溫平衡條件下：p+q=1。",
            "基因型頻率：p²+2pq+q²=1。",
        ],
    },
}


def find_target(data: dict[str, Any], subject: str, title: str) -> bool:
    for subject_key, subject_data in data.items():
        if subject_key != subject or not isinstance(subject_data, dict):
            continue
        stack = [subject_data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if node.get("name") == title and "lessonDetails" in node:
                    return True
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write repaired data")
    parser.add_argument(
        "--file",
        type=Path,
        default=ROOT / "src/knowparex/data/curriculum_integrated.js",
    )
    args = parser.parse_args()

    path = args.file.resolve()
    if not path.is_file():
        print(f"找不到課程資料檔：{path}", file=sys.stderr)
        return 1

    data = load_curriculum_js(path)
    found = []
    missing = []
    for key in REPAIRS:
        (found if find_target(data, *key) else missing).append("/".join(key))

    CURATED_UNITS.update(REPAIRS)
    counts = rebuild_data(data)
    report = {
        "targets_found": found,
        "targets_missing": missing,
        "rebuild": counts,
        "audit": audit_data(data),
    }

    if args.write:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = path.with_name(path.name + f".backup_{stamp}")
        shutil.copy2(path, backup)
        write_curriculum_js(path, data)
        report["backup"] = str(backup)
        report["written"] = str(path)

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())
