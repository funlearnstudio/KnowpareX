# KnowpareX 1.1.0 完整函式庫與使用指南

> 適用版本：`knowparex 1.1.0`  
> 作者：Steve Lin／林炫銓  
> 這份文件整理套件的安裝方式、命令列工具、Python API、關係函式、資料儲存函式，以及目前註冊的全部分類與項目。

---

## 目錄

1. [安裝與更新](#1-安裝與更新)
2. [最短使用範例](#2-最短使用範例)
3. [命令列指令](#3-命令列指令)
4. [主要 Python API](#4-主要-python-api)
5. [library 中央資料庫](#5-library-中央資料庫)
6. [compare_system 資料控制](#6-compare_system-資料控制)
7. [程式概念與語法比較函式](#7-程式概念與語法比較函式)
8. [數學關係函式](#8-數學關係函式)
9. [一般知識關係函式](#9-一般知識關係函式)
10. [程式套件與生態系函式](#10-程式套件與生態系函式)
11. [自訂關係與底層函式](#11-自訂關係與底層函式)
12. [錯題資料儲存 API](#12-錯題資料儲存-api)
13. [完整程式範例](#13-完整程式範例)
14. [目前全部分類與項目](#14-目前全部分類與項目)

---
# 1. 安裝與更新

## 從 PyPI 安裝

### Windows

建議使用：

```powershell
py -m pip install knowparex
```

如果電腦無法使用 `py`，可以改用：

```powershell
python -m pip install knowparex
```

### macOS / Linux

```bash
python3 -m pip install knowparex
```

---

## 更新到最新版

### Windows

```powershell
py -m pip install --upgrade knowparex
```

或：

```powershell
python -m pip install --upgrade knowparex
```

### macOS / Linux

```bash
python3 -m pip install --upgrade knowparex
```

---

## 查看目前版本

### Windows

```powershell
py -m pip show knowparex
```

或：

```powershell
python -m pip show knowparex
```

### macOS / Linux

```bash
python3 -m pip show knowparex
```

---

## 確認安裝成功

```bash
knowparex categories
```

如果成功，終端機會顯示所有可用分類。

如果 Windows 出現：

```text
'knowparex' is not recognized as an internal or external command
```

請先關閉並重新開啟 PowerShell 或命令提示字元。若仍無法執行，請確認 Python 的 `Scripts` 資料夾已加入 `PATH`。<br>

Python 中查看：

```python
import knowparex

print(knowparex.__version__)
```
---

# 2. 最短使用範例

```python
from knowparex import get_categories, get_items, get_topic_data

print(get_categories())
print(get_items("電學"))

records = get_topic_data("電學", "歐姆定律")

for record in records:
    print(record)
```

一次匯入主要公開功能：

```python
from knowparex import (
    library,
    compare_system,
    get_categories,
    get_items,
    get_topic_data,
    topic_exists,
)
```

---

# 3. 命令列指令

## 互動式查詢

```bash
knowparex
```

或：

```bash
knowparex compare
```

獨立指令：

```bash
knowparex-compare
```

## 練習／測驗

```bash
knowparex practice
```

或：

```bash
knowparex-practice
```

## 複習錯題

```bash
knowparex review
```

或：

```bash
knowparex-review
```

## 列出全部分類

```bash
knowparex categories
```

## 列出一個分類中的全部項目

```bash
knowparex items "電學"
```

## 顯示主題資料 / 輸出 JSON

```bash
knowparex topic "電學" "歐姆定律"
knowparex topic "有機化學" "醇" --json
```
## Search / 搜尋

KnowpareX can search category names, topic names, and all structured knowledge records.

KnowpareX 可以搜尋分類名稱、主題名稱，以及所有結構化知識紀錄。

### Basic search / 基本搜尋

```bash
knowparex search "能量"
```

The default search checks:

- Category names
- Topic names
- Relationship fields
- Left-side content and labels
- Right-side content and labels

預設搜尋範圍包括：

- 分類名稱
- 主題名稱
- 關係欄位
- 左側內容與標籤
- 右側內容與標籤

---

### Summary mode / 摘要模式

Show search statistics and matching topics without displaying every knowledge record.

只顯示搜尋統計與符合的主題，不列出所有知識紀錄。

```bash
knowparex search "能量" --summary
```

---

### Exact match / 完全符合

Only match fields whose complete content equals the search keyword.

只匹配整個欄位內容完全等於搜尋文字的結果。

```bash
knowparex search "醇" --exact
```

For example, this can match `醇` without matching `乙醇` or `醇厚`.

例如，這可以只匹配「醇」，而不匹配「乙醇」或「醇厚」。

---

### Topic-only search / 只搜尋主題

Search only category and topic names.

只搜尋分類名稱與主題名稱。

```bash
knowparex search "水" --topic-only
```

---

### Record-only search / 只搜尋知識紀錄

Search only the structured knowledge records, without treating category or topic names as direct matches.

只搜尋結構化知識紀錄，不把分類或主題名稱視為直接命中。

```bash
knowparex search "電流" --record-only
```

---

### Search within one category / 限制搜尋分類

Search only inside a specified category.

只在指定分類中搜尋。

```bash
knowparex search "電流" --category "磁學"
```

---

### Limit displayed records / 限制顯示數量

Limit the number of detailed knowledge records shown in the terminal.

限制終端機顯示的詳細知識紀錄數量。

```bash
knowparex search "水" --limit 20
```

---

### JSON search output / JSON 搜尋輸出

Return structured JSON for websites, scripts, or other applications.

輸出結構化 JSON，方便網站、腳本或其他應用程式使用。

```bash
knowparex search "能量" --json
```

---

### Combine search options / 組合搜尋選項

Search options can be combined.

搜尋選項可以一起使用。

```bash
knowparex search "電流" --category "磁學" --limit 10
```

```bash
knowparex search "能量" --summary --category "熱學與熱力學"
```

Available search options:

```text
--summary       Show only the summary and matching topics
--exact         Match complete field contents only
--topic-only    Search category and topic names only
--record-only   Search knowledge records only
--category      Search inside one specified category
--limit         Limit the number of displayed records
--json          Output search results as JSON
```
## 查看說明

```bash
knowparex --help
```

---

# 4. 主要 Python API

## `get_categories() -> list[str]`

取得全部分類名稱。

```python
from knowparex import get_categories

for category in get_categories():
    print(category)
```

## `get_items(category: str) -> list[str]`

取得指定分類中的全部項目。

```python
from knowparex import get_items

items = get_items("電學")

for item in items:
    print(item)
```

分類不存在時會產生 `KeyError`：

```python
try:
    items = get_items("不存在的分類")
except KeyError as error:
    print(error)
```

## `get_topic_data(category: str, item: str) -> list[dict]`

執行一個知識函式，並取得其關係資料。

```python
from knowparex import get_topic_data

records = get_topic_data("電學", "歐姆定律")

for record in records:
    print(record)
```

每筆紀錄的格式：

```python
{
    "relation": "關係名稱",
    "code_a": "左側內容",
    "language_a": "左側標籤",
    "code_b": "右側內容",
    "language_b": "右側標籤",
}
```

格式化顯示：

```python
for record in get_topic_data("電學", "歐姆定律"):
    print(
        f'{record["code_a"]} '
        f'--[{record["relation"]}]--> '
        f'{record["code_b"]}'
    )
```

## `topic_exists(category: str, item: str) -> bool`

確認分類與項目是否存在。

```python
from knowparex import topic_exists

print(topic_exists("電學", "歐姆定律"))
```

安全查詢：

```python
from knowparex import topic_exists, get_topic_data

category = "電學"
item = "歐姆定律"

if topic_exists(category, item):
    print(get_topic_data(category, item))
else:
    print("找不到主題")
```

---

# 5. `library` 中央資料庫

`library` 是一個兩層字典：

```python
library = {
    "分類名稱": {
        "項目名稱": 函式,
    },
}
```

匯入：

```python
from knowparex import library
```

列出全部分類：

```python
for category in library:
    print(category)
```

列出分類中的全部項目：

```python
for item in library["電學"]:
    print(item)
```

直接執行一個項目：

```python
library["電學"]["歐姆定律"]()
```

安全執行：

```python
category = "電學"
item = "歐姆定律"

if category in library and item in library[category]:
    library[category][item]()
else:
    print("找不到分類或項目")
```

在 `system_library.py` 註冊新項目時，右側不能加括號：

```python
# 正確：儲存函式本身
"歐姆定律": physics_electricity.ohms_law

# 錯誤：匯入時立刻執行
"歐姆定律": physics_electricity.ohms_law()
```

---

# 6. `compare_system` 資料控制

匯入：

```python
from knowparex import compare_system
```

| 函式 | 產生的關係 |
|---|---|
| `set_show(value)` | `None` |
| `clear_data()` | `None` |
| `get_data()` | `None` |
| `save_data(relation, code_a, language_a, code_b, language_b)` | `None` |
| `nothing()` | `None` |

## `set_show(value)`

控制關係函式執行時是否立即印出內容。

```python
compare_system.set_show(True)
compare_system.set_show(False)
```

## `clear_data()`

清除先前收集的關係資料。

```python
compare_system.clear_data()
```

## `get_data()`

取得收集資料的副本。

```python
records = compare_system.get_data()
```

## 收集資料但不立即顯示

```python
from knowparex import library, compare_system

compare_system.clear_data()
compare_system.set_show(False)

try:
    library["電學"]["歐姆定律"]()
    records = compare_system.get_data()
finally:
    compare_system.set_show(True)

for record in records:
    print(record)
```

平常查詢主題時，建議優先使用 `get_topic_data()`，因為它已經自動完成上述流程。

---

# 7. 程式概念與語法比較函式

這些函式皆使用四個參數：

```python
compare_system.函式名稱(
    code_a,
    language_a,
    code_b,
    language_b,
)
```

| 函式 | 產生的關係 |
|---|---|
| `different(code_a, language_a, code_b, language_b)` | `DIFFERENT` |
| `codesimilarbutsyntaxsame(code_a, language_a, code_b, language_b)` | `CODE SIMILAR, SYNTAX SAME` |
| `codesamebutsyntaxsimilar(code_a, language_a, code_b, language_b)` | `CODE SAME, SYNTAX SIMILAR` |
| `codedifferentbutsyntaxsimilar(code_a, language_a, code_b, language_b)` | `CODE DIFFERENT, SYNTAX SIMILAR` |
| `codesimilarbutsyntaxdifferent(code_a, language_a, code_b, language_b)` | `CODE SIMILAR, SYNTAX DIFFERENT` |
| `codedifferentbutsyntaxsame(code_a, language_a, code_b, language_b)` | `CODE DIFFERENT, SYNTAX SAME` |
| `codesamebutsyntaxdifferent(code_a, language_a, code_b, language_b)` | `CODE SAME, SYNTAX DIFFERENT` |
| `similar(code_a, language_a, code_b, language_b)` | `SIMILAR` |
| `exactsame(code_a, language_a, code_b, language_b)` | `EXACT SAME` |
| `nodirectequivalent(code_a, language_a, code_b, language_b)` | `NO DIRECT EQUIVALENT` |

## 九宮格概念

| 概念＼語法 | 不同 | 相似 | 相同 |
|---|---|---|---|
| 不同 | `different` | `codedifferentbutsyntaxsimilar` | `codedifferentbutsyntaxsame` |
| 相似 | `codesimilarbutsyntaxdifferent` | `similar` | `codesimilarbutsyntaxsame` |
| 相同 | `codesamebutsyntaxdifferent` | `codesamebutsyntaxsimilar` | `exactsame` |

範例：

```python
from knowparex import compare_system

compare_system.codesamebutsyntaxsimilar(
    "return x;",
    "C++",
    "return x",
    "Python",
)
```

---

# 8. 數學關係函式

這些函式皆使用四個參數：

```python
compare_system.函式名稱(
    code_a,
    language_a,
    code_b,
    language_b,
)
```

| 函式 | 產生的關係 |
|---|---|
| `inverselyproportionalto(code_a, language_a, code_b, language_b)` | `反比於` |
| `approximately(code_a, language_a, code_b, language_b)` | `約為` |
| `equal(code_a, language_a, code_b, language_b)` | `=` |
| `bigger(code_a, language_a, code_b, language_b)` | `>` |
| `smaller(code_a, language_a, code_b, language_b)` | `<` |
| `equalorbigger(code_a, language_a, code_b, language_b)` | `>=` |
| `equalorsmaller(code_a, language_a, code_b, language_b)` | `<=` |
| `notequal(code_a, language_a, code_b, language_b)` | `!=` |
| `approximatelyequal(code_a, language_a, code_b, language_b)` | `≈` |
| `proportionalto(code_a, language_a, code_b, language_b)` | `正比於` |
| `equivalentto(code_a, language_a, code_b, language_b)` | `等價於` |
| `calculatedby(code_a, language_a, code_b, language_b)` | `計算方式` |
| `simplifiedto(code_a, language_a, code_b, language_b)` | `化簡為` |
| `factorizedto(code_a, language_a, code_b, language_b)` | `因式分解為` |

範例：

```python
compare_system.equal(
    "2 + 3",
    "算式",
    "5",
    "答案",
)
```

```python
compare_system.calculatedby(
    "動能",
    "物理量",
    "1/2 × m × v²",
    "公式",
)
```

---

# 9. 一般知識關係函式

這些函式皆使用四個參數：

```python
compare_system.函式名稱(
    content_a,
    label_a,
    content_b,
    label_b,
)
```

| 函式 | 產生的關係 |
|---|---|
| `definition(content_a, label_a, content_b, label_b)` | `定義為` |
| `exampleof(content_a, label_a, content_b, label_b)` | `是……的例子` |
| `partof(content_a, label_a, content_b, label_b)` | `是……的一部分` |
| `typeof(content_a, label_a, content_b, label_b)` | `是……的一種類型` |
| `causes(content_a, label_a, content_b, label_b)` | `造成` |
| `resultsin(content_a, label_a, content_b, label_b)` | `導致` |
| `requires(content_a, label_a, content_b, label_b)` | `需要` |
| `before(content_a, label_a, content_b, label_b)` | `在……之前` |
| `after(content_a, label_a, content_b, label_b)` | `在……之後` |
| `opposite(content_a, label_a, content_b, label_b)` | `與……相反` |
| `related(content_a, label_a, content_b, label_b)` | `與……相關` |
| `translates(content_a, label_a, content_b, label_b)` | `翻譯為` |
| `composedof(content_a, label_a, content_b, label_b)` | `由……組成` |
| `functionof(content_a, label_a, content_b, label_b)` | `功能是` |
| `locatedin(content_a, label_a, content_b, label_b)` | `位於` |
| `characterizedby(content_a, label_a, content_b, label_b)` | `特徵是` |

範例：

```python
compare_system.definition(
    "光合作用",
    "生物概念",
    "植物利用光能製造有機養分的過程",
    "中文解釋",
)
```

```python
compare_system.causes(
    "溫室氣體增加",
    "原因",
    "全球平均溫度上升",
    "結果",
)
```

---

# 10. 程式套件與生態系函式

| 函式 | 產生的關係 |
|---|---|
| `samepurpose(content_a, label_a, content_b, label_b)` | `用途相近` |
| `alternativeof(content_a, label_a, content_b, label_b)` | `可作為……的替代方案` |
| `equivalentrole(content_a, label_a, content_b, label_b)` | `在生態系中的角色相近` |
| `wrapperof(content_a, label_a, content_b, label_b)` | `是……的語言綁定或包裝` |
| `depends_on(content_a, label_a, content_b, label_b)` | `依賴` |
| `builtwith(content_a, label_a, content_b, label_b)` | `以……建構` |
| `provides(content_a, label_a, content_b, label_b)` | `提供` |
| `usedfor(content_a, label_a, content_b, label_b)` | `用於` |
| `customrelation(relation, content_a, label_a, content_b, label_b)` | `None` |

範例：

```python
compare_system.samepurpose(
    "pygame",
    "Python 套件",
    "raylib",
    "C/C++ 函式庫",
)
```

```python
compare_system.wrapperof(
    "某 Python 套件",
    "Python",
    "底層 C 函式庫",
    "C",
)
```

---

# 11. 自訂關係與底層函式

## `customrelation(...)`

建立沒有專用函式的自訂關係。

```python
compare_system.customrelation(
    "生態系角色相近",
    "pygame",
    "Python 套件",
    "raylib",
    "C/C++ 函式庫",
)
```

完整簽名：

```python
customrelation(
    relation,
    content_a,
    label_a,
    content_b,
    label_b,
)
```

## `save_data(...)`

直接建立並儲存一筆底層關係紀錄。

```python
record = compare_system.save_data(
    "定義為",
    "變數",
    "程式概念",
    "用來保存資料的名稱",
    "中文解釋",
)
```

回傳格式：

```python
{
    "relation": "定義為",
    "code_a": "變數",
    "language_a": "程式概念",
    "code_b": "用來保存資料的名稱",
    "language_b": "中文解釋",
}
```

## `nothing()`

表示目前主題沒有資料。

```python
record = compare_system.nothing()
```

回傳：

```python
{
    "relation": None,
    "code_a": None,
    "language_a": None,
    "code_b": None,
    "language_b": None,
}
```

---

# 12. 錯題資料儲存 API

這些函式位於：

```python
from knowparex.storage import (
    get_data_directory,
    get_wrong_questions_path,
    load_wrong_questions,
    save_wrong_questions,
)
```

## `get_data_directory() -> Path`

取得 KnowpareX 的使用者資料目錄，必要時自動建立。

大致位置：

```text
macOS:
~/Library/Application Support/KnowpareX/

Windows:
%APPDATA%/KnowpareX/

Linux:
$XDG_DATA_HOME/KnowpareX/
或 ~/.local/share/KnowpareX/
```

使用：

```python
from knowparex.storage import get_data_directory

print(get_data_directory())
```

## `get_wrong_questions_path() -> Path`

取得錯題 JSON 的完整路徑。

```python
from knowparex.storage import get_wrong_questions_path

print(get_wrong_questions_path())
```

## `load_wrong_questions() -> list[dict]`

讀取錯題。檔案不存在、格式錯誤或無法讀取時，回傳空清單。

```python
from knowparex.storage import load_wrong_questions

questions = load_wrong_questions()
```

## `save_wrong_questions(questions) -> Path`

儲存錯題並回傳檔案路徑。

```python
from knowparex.storage import save_wrong_questions

path = save_wrong_questions([
    {
        "question": "示範題目",
        "answer": "示範答案",
    }
])

print(path)
```

通常不需要手動操作這些函式，直接使用：

```bash
knowparex practice
knowparex review
```

即可。

---

# 13. 完整程式範例

## 範例一：簡單查詢器

```python
from knowparex import (
    get_categories,
    get_items,
    get_topic_data,
    topic_exists,
)


def main() -> None:
    print("所有分類：")
    for category in get_categories():
        print(f"- {category}")

    category = input("\n請輸入分類：").strip()
    item = input("請輸入項目：").strip()

    if not topic_exists(category, item):
        print("找不到這個主題。")
        return

    print(f"\n{category}／{item}")

    for record in get_topic_data(category, item):
        print(
            f'{record["code_a"]} '
            f'--[{record["relation"]}]--> '
            f'{record["code_b"]}'
        )


if __name__ == "__main__":
    main()
```

## 範例二：建立自己的知識主題

```python
from knowparex import compare_system


class my_notes:

    @staticmethod
    def photosynthesis() -> None:
        compare_system.definition(
            "光合作用",
            "生物概念",
            "植物利用光能製造有機養分的過程",
            "中文解釋",
        )

        compare_system.requires(
            "光合作用",
            "生物過程",
            "光、水與二氧化碳",
            "必要條件",
        )
```

接著把函式註冊到你自己的 library：

```python
my_library = {
    "生物": {
        "光合作用": my_notes.photosynthesis,
    }
}

my_library["生物"]["光合作用"]()
```

## 範例三：匯出主題為 JSON

```python
import json
from pathlib import Path

from knowparex import get_topic_data

records = get_topic_data("電學", "歐姆定律")

Path("ohms_law.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
```

---

# 14. 目前全部分類與項目

目前此版本共有 **66 個分類**、**1580 個已註冊項目**。

### if

- `if`
- `ex_if`

### dot

- `object_function`

### console

- `print`

### loop

- `for`
- `while`
- `do`

### type

- `bool`
- `int`
- `char`
- `auto`
- `string`
- `double`
- `float`

### return

- `return`
- `ex_return`

### array

- `normal`
- `normal_array`
- `vector`

### function

- `void`
- `int`
- `bool`
- `auto`
- `string`
- `double`
- `float`
- `char`

### math

- `sqrt`
- `pow`
- `random`
- `abs`
- `round`
- `floor`
- `ceil`
- `fmod`
- `max`
- `min`
- `sin`
- `cos`
- `tan`
- `log`
- `log10`
- `exp`

### random

- `random`

### class

- `class`
- `ex_class`

### 數與數系

- `整數`
- `絕對值`
- `分數`
- `百分比`
- `指數`
- `根式`

### 代數

- `同類項`
- `分配律`
- `因式分解`
- `恆等式`

### 方程式與不等式

- `一元一次方程式`
- `聯立方程式`
- `二次方程式`
- `不等式`

### 函數

- `函數值`
- `一次函數`
- `二次函數`
- `定義域`

### 幾何

- `三角形`
- `畢氏定理`
- `圓`
- `多邊形`
- `坐標幾何`

### 三角函數

- `基本三角比`
- `特殊角`
- `角度與弧度`

### 數列

- `等差數列`
- `等比數列`

### 機率

- `基本機率`
- `餘事件`

### 統計

- `平均數`
- `中位數`
- `眾數`
- `全距`

### 電學

- `電荷`
- `起電`
- `導體與絕緣體`
- `庫侖定律`
- `電場`
- `電位`
- `電流`
- `電壓`
- `電阻`
- `歐姆定律`
- `安培計與伏特計`
- `串聯電路`
- `並聯電路`
- `電功率`
- `電能`
- `用電安全`

### 磁學

- `磁鐵`
- `磁場`
- `地磁`
- `電流的磁效應`
- `螺線管`
- `電磁鐵`
- `載流導線的磁力`
- `電動機`
- `電磁感應`
- `發電機`
- `變壓器`

### 波動與聲音

- `振動`
- `簡諧運動`
- `單擺`
- `波`
- `橫波與縱波`
- `波長、頻率與波速`
- `反射`
- `折射`
- `繞射`
- `干涉`
- `駐波`
- `聲音`
- `音調、響度與音色`
- `共振`
- `都卜勒效應`

### 光學

- `光`
- `發光體`
- `反射`
- `規則反射與漫反射`
- `平面鏡`
- `球面鏡`
- `折射`
- `折射率`
- `全反射`
- `透鏡`
- `凸透鏡成像`
- `透鏡公式`
- `眼睛`
- `色光`

### 熱學與熱力學

- `溫度`
- `溫度計`
- `熱`
- `比熱`
- `熱量測定`
- `相變`
- `潛熱`
- `熱傳導`
- `熱對流`
- `熱輻射`
- `熱膨脹`
- `氣體定律`
- `內能`
- `熱力學第一定律`

### 流體與簡單機械

- `壓力`
- `液體壓力`
- `大氣壓力`
- `帕斯卡原理`
- `浮力`
- `浮沉`
- `連續方程式`
- `白努力原理`
- `力矩`
- `轉動平衡`
- `槓桿`
- `滑輪`
- `斜面`
- `機械利益`

### 物質與分離

- `物質`
- `元素、化合物與混合物`
- `均勻與非均勻混合物`
- `物理性質`
- `化學性質`
- `物理變化`
- `化學變化`
- `物質三態`
- `相變`
- `密度`
- `過濾`
- `蒸餾`
- `色層分析`

### 原子與週期表

- `原子`
- `質子、中子與電子`
- `原子序`
- `質量數`
- `同位素`
- `平均原子量`
- `離子`
- `電子層`
- `電子排列`
- `週期表`
- `金屬、非金屬與類金屬`
- `鹼金屬`
- `鹼土金屬`
- `鹵素`
- `鈍氣`
- `週期趨勢`

### 化學鍵與化學式

- `化學鍵`
- `離子鍵`
- `共價鍵`
- `金屬鍵`
- `路易斯結構`
- `八隅體規則`
- `電負度`
- `分子極性`
- `分子間作用力`
- `氫鍵`
- `分子形狀`
- `化學式`
- `離子化合物化學式`
- `常見離子`
- `命名`

### 化學反應與莫耳

- `化學反應`
- `質量守恆`
- `平衡化學方程式`
- `反應類型`
- `燃燒`
- `降水`
- `莫耳`
- `粒子數`
- `莫耳質量`
- `實驗式與分子式`
- `化學計量`
- `限量試劑`
- `產率`

### 溶液與酸鹼

- `溶液`
- `溶解度`
- `飽和溶液`
- `質量百分濃度`
- `體積莫耳濃度`
- `稀釋`
- `電解質`
- `酸`
- `鹼`
- `強酸強鹼與弱酸弱鹼`
- `pH`
- `pOH`
- `中和反應`
- `酸鹼指示劑`
- `酸鹼滴定`
- `緩衝溶液`

### 氧化還原與電化學

- `氧化與還原`
- `氧化劑與還原劑`
- `氧化數`
- `平衡氧化還原反應`
- `金屬活動性`
- `腐蝕`
- `原電池`
- `丹尼爾電池`
- `電解`
- `電鍍`
- `法拉第定律`
- `電池`

### 氣體、熱化學與平衡

- `氣體壓力`
- `波以耳定律`
- `查理定律`
- `給呂薩克定律`
- `亞佛加厥定律`
- `理想氣體`
- `分壓`
- `熱化學`
- `吸熱與放熱`
- `焓`
- `赫斯定律`
- `鍵能`
- `反應速率`
- `碰撞理論`
- `活化能`
- `化學平衡`
- `平衡常數`
- `勒沙特列原理`

### 有機化學

- `有機化合物`
- `烴`
- `烷類`
- `烯類與炔類`
- `同分異構物`
- `官能基`
- `醇`
- `羧酸`
- `酯`
- `聚合物`
- `加成聚合`
- `縮合聚合`
- `醣類`
- `脂質`
- `蛋白質`
- `清潔劑`

### 細胞與代謝

- `細胞學說`
- `原核細胞與真核細胞`
- `細胞膜`
- `細胞質`
- `細胞核`
- `粒線體`
- `葉綠體`
- `核糖體`
- `內質網`
- `高基氏體`
- `溶體與液胞`
- `細胞壁`
- `擴散`
- `滲透作用`
- `主動運輸`
- `胞吞與胞吐`
- `酵素`
- `酵素專一性`
- `影響酵素活性的因素`
- `ATP`
- `光合作用`
- `細胞呼吸`
- `發酵`

### 遺傳與演化

- `染色體`
- `細胞週期`
- `有絲分裂`
- `減數分裂`
- `互換`
- `DNA`
- `DNA複製`
- `基因`
- `RNA`
- `轉錄`
- `轉譯`
- `中心法則`
- `孟德爾遺傳定律`
- `基因型與表現型`
- `顯性關係`
- `血型`
- `性聯遺傳`
- `突變`
- `生物技術`
- `PCR`
- `演化`
- `自然選擇`
- `演化證據`
- `物種形成`
- `生物分類`
- `三域系統`
- `病毒`

### 植物與生態

- `植物組織`
- `根`
- `莖`
- `葉`
- `蒸散作用`
- `植物體內運輸`
- `向性`
- `花`
- `傳粉與受精`
- `種子與果實`
- `萌發`
- `生態層次`
- `棲地與棲位`
- `族群成長`
- `生物交互作用`
- `食物鏈與食物網`
- `營養階層`
- `能量金字塔`
- `碳循環`
- `氮循環`
- `生態演替`
- `生物多樣性`
- `保育`

### 人體生理

- `人體構造層次`
- `恆定性`
- `消化系統`
- `口腔、食道與胃`
- `小腸、肝臟與胰臟`
- `呼吸系統`
- `呼吸運動`
- `氣體交換`
- `循環系統`
- `心臟`
- `血管`
- `血液`
- `淋巴系統`
- `泌尿系統`
- `腎元`
- `神經系統`
- `神經元`
- `反射作用`
- `內分泌系統`
- `血糖調節`
- `免疫系統`
- `抗原與抗體`
- `疫苗`
- `肌肉與骨骼系統`
- `生殖系統`
- `月經週期`

### 地質學

- `地球內部分層`
- `岩石圈與軟流圈`
- `大陸地殼與海洋地殼`
- `板塊構造`
- `張裂型板塊邊界`
- `聚合型板塊邊界`
- `錯動型板塊邊界`
- `大陸漂移`
- `海底擴張`
- `地震`
- `地震波`
- `地震規模與震度`
- `斷層`
- `褶皺`
- `火山`
- `岩漿黏度`
- `礦物`
- `火成岩`
- `沉積岩`
- `變質岩`
- `岩石循環`
- `風化、侵蝕與沉積`
- `相對定年`
- `放射性定年`

### 大氣與海洋

- `大氣組成`
- `大氣分層`
- `臭氧層`
- `氣壓`
- `風`
- `高低氣壓`
- `濕度`
- `雲`
- `降水`
- `氣團與鋒面`
- `冷鋒與暖鋒`
- `颱風`
- `季風`
- `海陸風`
- `天氣與氣候`
- `氣候因素`
- `水循環`
- `地下水`
- `海水鹽度`
- `洋流`
- `海浪與潮汐`
- `聖嬰與反聖嬰`

### 天文與環境

- `宇宙尺度`
- `大霹靂理論`
- `恆星`
- `恆星演化`
- `赫羅圖`
- `太陽系`
- `類地行星與類木行星`
- `地球自轉`
- `地球公轉與四季`
- `二分二至`
- `月球運動`
- `月相`
- `日食`
- `月食`
- `太陽`
- `電磁波譜`
- `溫室效應`
- `氣候變遷`
- `海平面`
- `天然災害`
- `再生能源`
- `永續發展`

### 英文子句與句型

- `simple_compound_complex`
- `relative_clause`
- `noun_clause`
- `adverb_clause`
- `conditionals`
- `reported_speech`
- `inversion`

### 英文文法

- `parts_of_speech`
- `subject_verb_agreement`
- `articles`
- `countable_uncountable`
- `pronouns`
- `comparatives_superlatives`
- `gerund_infinitive`
- `modals`
- `prepositions`

### 英文字首

- `prefix_a_an`
- `prefix_anti`
- `prefix_auto`
- `prefix_bi`
- `prefix_co_com_con`
- `prefix_de`
- `prefix_dis`
- `prefix_en_em`
- `prefix_ex`
- `prefix_extra`
- `prefix_fore`
- `prefix_hyper`
- `prefix_hypo`
- `prefix_il_im_in_ir`
- `prefix_inter`
- `prefix_intra`
- `prefix_mal`
- `prefix_mega`
- `prefix_mid`
- `prefix_mis`
- `prefix_mono`
- `prefix_multi`
- `prefix_non`
- `prefix_over`
- `prefix_post`
- `prefix_pre`
- `prefix_pro`
- `prefix_re`
- `prefix_semi`
- `prefix_sub`
- `prefix_super`
- `prefix_trans`
- `prefix_tri`
- `prefix_under`
- `prefix_uni`

### 英文字根

- `root_act`
- `root_aud`
- `root_bio`
- `root_cap_capt_cept`
- `root_ced_ceed_cess`
- `root_chron`
- `root_cred`
- `root_dict`
- `root_duc_duct`
- `root_fac_fact_fect`
- `root_fer`
- `root_form`
- `root_geo`
- `root_graph_gram`
- `root_ject`
- `root_jur_jus`
- `root_log_logo`
- `root_manu`
- `root_meter_metr`
- `root_micro`
- `root_mit_miss`
- `root_mort`
- `root_mov_mot`
- `root_path`
- `root_ped_pod`
- `root_phon`
- `root_photo`
- `root_port`
- `root_rupt`
- `root_scrib_script`
- `root_sect`
- `root_spect_spic`
- `root_struct`
- `root_tele`
- `root_terr`
- `root_therm`
- `root_tract`
- `root_vac_van`
- `root_vid_vis`
- `root_voc_vok`
- `root_aqua`
- `root_astro`
- `root_bene`
- `root_circum`
- `root_dem`
- `root_gen`
- `root_hydr`
- `root_luc_lum`
- `root_magn`
- `root_min`
- `root_nov`
- `root_omni`
- `root_phil`
- `root_psych`
- `root_sol`
- `root_son`
- `root_temp`
- `root_ver`

### 英文語意與通順

- `context_clues`
- `logical_coherence`
- `reference_words`
- `collocation`
- `ambiguity`
- `concise_expression`

### 英文字尾

- `suffix_able_ible`
- `suffix_al`
- `suffix_ance_ence`
- `suffix_ant_ent`
- `suffix_ary`
- `suffix_dom`
- `suffix_er_or`
- `suffix_ful`
- `suffix_hood`
- `suffix_ic_ical`
- `suffix_ify`
- `suffix_ion_tion_sion`
- `suffix_ish`
- `suffix_ism`
- `suffix_ist`
- `suffix_ity`
- `suffix_ive`
- `suffix_ize_ise`
- `suffix_less`
- `suffix_ly`
- `suffix_ment`
- `suffix_ness`
- `suffix_ology`
- `suffix_ous`
- `suffix_ship`
- `suffix_ward_wards`
- `suffix_y`

### 英文時態與語態

- `present_simple`
- `present_progressive`
- `past_simple`
- `past_progressive`
- `present_perfect`
- `past_perfect`
- `future_forms`
- `passive_voice`
- `causative`

### 英文連接詞與閱讀

- `addition`
- `contrast`
- `cause_effect`
- `example_transition`
- `sequence_transition`
- `main_idea`
- `supporting_detail`
- `inference`
- `tone_purpose`

### 英文用法與常見錯誤

- `affect_effect`
- `accept_except`
- `borrow_lend`
- `say_tell_speak_talk`
- `fewer_less`
- `because_because_of`
- `despite_although`
- `comma_splice`
- `sentence_fragment`
- `run_on_sentence`
- `parallel_structure`

### 英文作文

- `paragraph_structure`
- `introduction`
- `body_paragraph`
- `conclusion`
- `opinion_essay`
- `narrative_essay`
- `descriptive_essay`
- `compare_contrast_essay`
- `problem_solution_essay`
- `revision_checklist`

### 臺灣歷史

- `史料與歷史研究`
- `臺灣史前時代`
- `南島語族與原住民族`
- `荷蘭與西班牙統治`
- `鄭氏政權`
- `清治時期`
- `清末改革`
- `馬關條約與割臺`
- `日本統治`
- `日本統治下的經濟與社會`
- `政治與社會運動`
- `皇民化運動`
- `戰後接收`
- `二二八事件`
- `戒嚴與白色恐怖`
- `戰後經濟發展`
- `民主化`
- `轉型正義`

### 中國歷史

- `中國古代文明`
- `夏商周`
- `春秋戰國`
- `諸子百家`
- `秦的統一`
- `漢帝國`
- `魏晉南北朝`
- `隋唐時期`
- `宋代`
- `元明清`
- `明清全球貿易`
- `鴉片戰爭`
- `自強運動與晚清改革`
- `甲午戰爭`
- `辛亥革命`
- `新文化運動與五四運動`
- `國民黨與共產黨`
- `抗日戰爭與國共內戰`
- `中華人民共和國與改革開放`

### 世界歷史

- `古代河流文明`
- `古希臘文明`
- `古羅馬世界`
- `基督教與伊斯蘭文明`
- `中世紀歐洲`
- `十字軍東征與城市發展`
- `文藝復興與宗教改革`
- `科學革命與啟蒙運動`
- `地理大發現`
- `大西洋革命`
- `工業革命`
- `民族主義與帝國主義`
- `第一次世界大戰`
- `戰間期`
- `第二次世界大戰與猶太大屠殺`
- `聯合國與人權發展`
- `冷戰`
- `去殖民化`
- `全球化`

### 地理

- `地理探究`
- `地圖基礎`
- `經緯度與時區`
- `地理資訊系統與遙測`
- `板塊構造`
- `地形作用`
- `河流、海岸與喀斯特地形`
- `氣候要素與氣候因素`
- `季風與颱風`
- `水循環與海洋`
- `人口`
- `都市化與聚落`
- `產業活動`
- `全球化與國際貿易`
- `臺灣地理`
- `東亞、東南亞與南亞`
- `西亞與非洲`
- `歐洲、美洲與大洋洲`
- `天然災害、氣候變遷與永續發展`

### 公民與社會

- `自我認同與社會化`
- `家庭與社會團體`
- `文化與社會規範`
- `社會階層與平等`
- `媒體與數位公民`
- `公民社會`
- `國家與政府`
- `民主政治與法治`
- `權力分立與憲法`
- `選舉、政黨與公民投票`
- `人權`
- `言論自由與隱私權`
- `法律制度`
- `民法、刑法與行政法`
- `消費者與勞動權益`
- `稀少性、選擇與機會成本`
- `供給與需求`
- `市場與政府`
- `貨幣與總體經濟`
- `國際貿易與全球治理`
- `社會福利、公共政策與公民參與`
- `社會探究`

### 國文文學常識

- `文學體裁`
- `散文`
- `古文`
- `駢文`
- `詩`
- `古體詩`
- `近體詩`
- `絕句`
- `律詩`
- `樂府`
- `《詩經》`
- `楚辭`
- `賦`
- `詞`
- `曲`
- `現代詩`
- `小說`
- `古典小說`
- `志怪小說`
- `志人小說`
- `唐傳奇`
- `章回小說`
- `戲劇`
- `傳統戲曲`
- `文學運動`
- `唐宋八大家`
- `建安七子`
- `竹林七賢`
- `四書`
- `五經`
- `歷史散文`
- `編年體`
- `紀傳體`
- `國別體`
- `臺灣文學`
- `鄉土文學`
- `自然書寫`
- `旅行文學`
- `口傳文學`

### 國文語文常識

- `六書`
- `象形`
- `指事`
- `會意`
- `形聲`
- `轉注`
- `假借`
- `部首`
- `字形`
- `同音字`
- `形近字`
- `破音字`
- `正體字`
- `詞`
- `複合詞`
- `詞類`
- `名詞`
- `動詞`
- `形容詞`
- `副詞`
- `代詞`
- `介詞`
- `連詞`
- `助詞`
- `嘆詞`
- `句子成分`
- `主語`
- `賓語`
- `定語`
- `基本句型`
- `複句`
- `標點符號`
- `逗號`
- `頓號`
- `分號`
- `冒號`
- `引號`
- `破折號`
- `刪節號`
- `書名號`
- `成語`
- `諺語`
- `俗語`
- `歇後語`
- `對聯`
- `書信`
- `啟事`
- `柬帖`
- `稱謂`
- `年齡代稱`
- `季節與月份代稱`
- `天干地支`

### 國文修辭

- `修辭`
- `明喻`
- `暗喻`
- `略喻`
- `借代`
- `擬人`
- `擬物`
- `誇飾`
- `排比`
- `對偶`
- `映襯`
- `正襯`
- `反襯`
- `設問`
- `反問`
- `反復`
- `頂真`
- `回文`
- `層遞`
- `遞升`
- `遞降`
- `引用`
- `用典`
- `象徵`
- `雙關`
- `婉曲`
- `倒反`
- `移覺`
- `摹寫`
- `動態描寫`
- `靜態描寫`
- `伏筆`
- `懸念`
- `倒敘`
- `插敘`
- `直抒胸臆`
- `間接抒情`
- `借景抒情`
- `託物言志`
- `情景交融`
- `首尾呼應`
- `比較`
- `分類`
- `下定義`
- `舉例`
- `列數據`

### 國文文言文

- `文言文`
- `實詞`
- `虛詞`
- `一詞多義`
- `古今異義`
- `通假字`
- `詞類活用`
- `名詞作動詞`
- `名詞作狀語`
- `使動用法`
- `意動用法`
- `判斷句`
- `被動句`
- `倒裝句`
- `省略句`
- `固定句式`
- `之`
- `其`
- `而`
- `以`
- `於`
- `乃`
- `則`
- `者`
- `焉`
- `何`
- `乎`
- `信達雅`
- `直譯`
- `意譯`
- `文言翻譯`
- `文言閱讀`
- `文言議論`
- `文言敘事`
- `文言抒情`
- `古典詩歌意象`
- `古典詩歌閱讀`
- `起承轉合`
- `文化語境`
- `官職名`
- `名、字、號`

### 國文作文

- `寫作流程`
- `審題`
- `立意`
- `選材`
- `大綱`
- `分段`
- `主題句`
- `連貫`
- `過渡`
- `開頭`
- `開門見山`
- `情境開頭`
- `設問開頭`
- `引用開頭`
- `結尾`
- `總結式結尾`
- `呼應式結尾`
- `餘韻式結尾`
- `記敘文`
- `順敘`
- `人物描寫`
- `景物描寫`
- `事件描寫`
- `細節描寫`
- `抒情文`
- `說明文`
- `下定義`
- `議論文`
- `論點`
- `論據`
- `論證`
- `舉例論證`
- `對比論證`
- `因果論證`
- `引用論證`
- `反方觀點`
- `比較型作文`
- `問題解決型作文`
- `感想文`
- `閱讀心得`
- `圖表或圖像寫作`
- `材料作文`
- `命題作文`
- `自訂題目作文`
- `描寫`
- `感官描寫`
- `以描寫代替直說`
- `對話`
- `文章語調`
- `遣詞用字`
- `句式變化`
- `譬喻、排比、映襯、設問`
- `修改`
- `校對`
- `離題`
- `作文時間分配`
- `卷面與格式`

### 國文閱讀理解

- `閱讀理解`
- `預覽`
- `預測`
- `提問`
- `理解監控`
- `重讀`
- `閱讀標記`
- `關鍵詞`
- `主旨`
- `主題`
- `段落大意`
- `主題句`
- `支持細節`
- `摘要`
- `改寫`
- `字面義`
- `語境義`
- `上下文線索`
- `指涉`
- `銜接`
- `連貫`
- `順序關係`
- `時間順序`
- `空間順序`
- `因果關係`
- `比較與對照`
- `問題解決結構`
- `分類結構`
- `總分結構`
- `轉承詞`
- `寫作目的`
- `作者觀點`
- `作者態度`
- `語氣`
- `客觀敘述`
- `事實`
- `明示訊息`
- `隱含訊息`
- `推論`
- `證據推論`
- `人物推論`
- `人物動機`
- `人物轉變`
- `衝突`
- `情節`
- `環境`
- `敘述者`
- `第一人稱敘事`
- `第三人稱敘事`
- `不可靠敘述者`
- `伏筆`
- `懸念`
- `倒敘`
- `插敘`
- `象徵`
- `意象`
- `氛圍`
- `反諷`
- `幽默`
- `諷刺`
- `記敘文閱讀`
- `抒情文閱讀`
- `說明文閱讀`
- `議論文閱讀`
- `論點`
- `論據`
- `論證`
- `反方觀點`
- `邏輯謬誤`
- `以偏概全`
- `錯誤因果`
- `非黑即白`
- `不當訴諸權威`
- `人身攻擊`
- `數據閱讀`
- `圖表閱讀`
- `表格閱讀`
- `資訊圖表`
- `圖文關係`
- `多文本閱讀`
- `跨文本比較`
- `來源評估`
- `偏見或偏向`
- `錯誤資訊`
- `事實查核`
- `廣告閱讀`
- `新聞閱讀`
- `文言文閱讀`
- `判斷文言字義`
- `判斷文言句式`
- `翻譯文言句`
- `判斷古文主旨`
- `古典詩歌閱讀`
- `詩中說話者`
- `分析詩歌意象`
- `判斷詩歌情感`
- `分析詩歌結構`
- `現代詩閱讀`
- `修辭效果`
- `用詞效果`
- `句式效果`
- `標題作用`
- `開頭作用`
- `結尾作用`
- `段落作用`
- `過渡段`
- `細節作用`
- `引用作用`
- `舉例作用`
- `數據作用`
- `對比作用`
- `描寫作用`
- `題幹`
- `檢索訊息題`
- `統整訊息題`
- `解釋題`
- `推論題`
- `評鑑題`
- `比較題`
- `開放式閱讀題`
- `選擇題策略`
- `干擾選項`
- `簡答題策略`
- `文本證據`
- `答案完整性`
- `閱讀速度`
- `閱讀時間分配`
- `閱讀題檢查`
- `國中會考閱讀`
- `高中國文閱讀`
- `素養導向閱讀`
- `跨領域閱讀`
- `長文閱讀`
- `難文閱讀`
- `閱讀筆記`
- `概念圖`
- `時間軸`
- `比較表`
- `問題與答案關係`
- `閱讀反思`
- `閱讀遷移`

### 國文作者

- `孔子`
- `孟子`
- `荀子`
- `老子`
- `莊子`
- `墨子`
- `韓非`
- `孫武`
- `屈原`
- `司馬遷`
- `班固`
- `賈誼`
- `曹操`
- `曹植`
- `陶淵明`
- `劉義慶`
- `酈道元`
- `王羲之`
- `李白`
- `杜甫`
- `王維`
- `孟浩然`
- `白居易`
- `韓愈`
- `柳宗元`
- `杜牧`
- `李商隱`
- `范仲淹`
- `歐陽脩`
- `王安石`
- `蘇洵`
- `蘇軾`
- `蘇轍`
- `曾鞏`
- `周敦頤`
- `司馬光`
- `李清照`
- `辛棄疾`
- `陸游`
- `文天祥`
- `朱熹`
- `關漢卿`
- `馬致遠`
- `施耐庵`
- `羅貫中`
- `吳承恩`
- `馮夢龍`
- `歸有光`
- `袁宏道`
- `張岱`
- `蒲松齡`
- `曹雪芹`
- `劉鶚`
- `梁啟超`
- `孫文`
- `魯迅`
- `胡適`
- `徐志摩`
- `朱自清`
- `冰心`
- `老舍`
- `沈從文`
- `巴金`
- `錢鍾書`
- `張愛玲`
- `林語堂`
- `豐子愷`
- `夏丏尊`
- `林海音`
- `琦君`
- `余光中`
- `楊牧`
- `張曉風`
- `簡媜`
- `龍應台`
- `廖鴻基`
- `劉克襄`
- `吳明益`
- `陳列`
- `陳芳明`
- `鄭愁予`
- `洛夫`
- `瘂弦`
- `周夢蝶`
- `白先勇`
- `黃春明`
- `王禎和`
- `鍾理和`
- `鍾肇政`
- `賴和`
- `楊逵`
- `呂赫若`
- `吳濁流`
- `李昂`
- `袁瓊瓊`
- `三毛`
- `杏林子`
- `林良`
- `林文月`
- `齊邦媛`
- `蔣勳`
- `徐仁修`
- `瓦歷斯·諾幹`
- `夏曼·藍波安`
- `巴代`
- `利格拉樂·阿烏`
- `陳耀昌`

### 國文課文整理

- `《論語》選`
- `《孟子》選`
- `《莊子》選`
- `《老子》選`
- `公輸`
- `曹劌論戰`
- `鄒忌諷齊王納諫`
- `唐雎不辱使命`
- `馮諼客孟嘗君`
- `鴻門宴`
- `廉頗藺相如列傳`
- `屈原列傳`
- `過秦論`
- `陳情表`
- `蘭亭集序`
- `桃花源記`
- `歸去來辭`
- `飲酒`
- `《世說新語》選`
- `三峽`
- `木蘭詩`
- `出師表`
- `敕勒歌`
- `春江花月夜`
- `將進酒`
- `蜀道難`
- `行路難`
- `春望`
- `登高`
- `茅屋為秋風所破歌`
- `石壕吏`
- `山居秋暝`
- `送元二使安西`
- `過故人莊`
- `琵琶行`
- `賣炭翁`
- `師說`
- `馬說`
- `祭十二郎文`
- `小石潭記`
- `始得西山宴遊記`
- `捕蛇者說`
- `阿房宮賦`
- `錦瑟`
- `岳陽樓記`
- `醉翁亭記`
- `秋聲賦`
- `六國論`
- `赤壁賦`
- `後赤壁賦`
- `念奴嬌·赤壁懷古`
- `水調歌頭`
- `遊褒禪山記`
- `答司馬諫議書`
- `愛蓮說`
- `《資治通鑑》選`
- `聲聲慢`
- `破陣子·為陳同甫賦壯詞以寄之`
- `永遇樂·京口北固亭懷古`
- `過零丁洋`
- `天淨沙·秋思`
- `《竇娥冤》選`
- `項脊軒志`
- `晚遊六橋待月記`
- `湖心亭看雪`
- `《聊齋志異》選`
- `《紅樓夢》選`
- `《老殘遊記》選`
- `少年中國說`
- `最苦與最樂`
- `差不多先生傳`
- `孔乙己`
- `故鄉`
- `《阿Q正傳》選`
- `背影`
- `荷塘月色`
- `匆匆`
- `再別康橋`
- `《城南舊事》選`
- `桂花雨`
- `鄉愁`
- `聽聽那冷雨`
- `我的四個假想敵`
- `夏之絕句`
- `行道樹`
- `目送`
- `《討海人》選`
- `《海浪的記憶》選`
- `一桿秤仔`
- `送報伕`
- `兒子的大玩偶`
- `《魯冰花》選`
- `《臺北人》選`
- `《亞細亞的孤兒》選`
- `《撒哈拉的故事》選`
- `《荒野有歌》選`
- `《複眼人》選`

### 國文成語與國學

- `安步當車`
- `安土重遷`
- `揠苗助長`
- `白駒過隙`
- `背水一戰`
- `閉門造車`
- `別出心裁`
- `不堪設想`
- `不落窠臼`
- `不一而足`
- `差強人意`
- `車水馬龍`
- `成竹在胸`
- `出類拔萃`
- `川流不息`
- `春風化雨`
- `大快朵頤`
- `當仁不讓`
- `東施效顰`
- `斷章取義`
- `耳濡目染`
- `方興未艾`
- `粉墨登場`
- `紛至沓來`
- `付與頑梗`
- `高山仰止`
- `格格不入`
- `功虧一簣`
- `故步自封`
- `光風霽月`
- `含英咀華`
- `河東獅吼`
- `囫圇吞棗`
- `渙然冰釋`
- `誨人不倦`
- `急於功名`
- `見賢思齊`
- `狡兔三窟`
- `津津有味`
- `涇渭分明`
- `舉一反三`
- `刻舟求劍`
- `空谷足音`
- `膾炙人口`
- `老馬識途`
- `李代桃僵`
- `量身訂做`
- `臨淵羨魚`
- `洛陽紙貴`
- `買櫝還珠`
- `茅塞頓開`
- `美輪美奐`
- `門可羅雀`
- `妙手偶得`
- `明日黃花`
- `目不交睫`
- `目無全牛`
- `南轅北轍`
- `嘔心瀝血`
- `蓬蓽生輝`
- `皮裡陽秋`
- `破釜沉舟`
- `杞人憂天`
- `前車之鑑`
- `晴天霹靂`
- `曲突徙薪`
- `如火如荼`
- `如數家珍`
- `三人成虎`
- `上行下效`
- `聲情並茂`
- `事半功倍`
- `守株待兔`
- `首當其衝`
- `殊途同歸`
- `水到渠成`
- `司空見慣`
- `曇花一現`
- `醍醐灌頂`
- `天花亂墜`
- `推心置腹`
- `望塵莫及`
- `未雨綢繆`
- `溫故知新`
- `毋庸置疑`
- `息息相關`
- `相形見絀`
- `小題大作`
- `信手拈來`
- `胸有成竹`
- `學富五車`
- `言過其實`
- `義正詞嚴`
- `以暴易暴`
- `一籌莫展`
- `雨過天晴`
- `一鳴驚人`
- `一日千里`
- `飲鴆止渴`
- `迎刃而解`
- `愚公移山`
- `緣木求魚`
- `擇善固執`
- `振聾發聵`
- `知微見著`
- `中流砥柱`
- `逐末忘本`
- `自相矛盾`
- `四書`
- `五經`
- `十三經`
- `前四史`
- `二十四史`
- `史書體例`
- `諸子百家`
- `儒家`
- `道家`
- `墨家`
- `法家`
- `唐宋八大家`
- `建安七子`
- `竹林七賢`
- `元曲四大家`
- `四大名著`
- `三言二拍`
- `古典文體`
- `記`
- `說`
- `序`
- `表`
- `書`
- `銘`
- `祭文`
- `對聯規則`
- `橫批`
- `敬辭`
- `謙辭`
- `家大舍小令外人`
- `年齡代稱`
- `婚姻代稱`
- `死亡代稱`
- `天干`
- `地支`
- `干支紀年`
- `十二時辰`
- `孟仲季`
- `農曆月份別稱`
- `二十四節氣`
- `春節`
- `元宵節`
- `清明節`
- `端午節`
- `七夕`
- `中秋節`
- `重陽節`
- `神話`
- `女媧補天`
- `夸父逐日`
- `精衛填海`
- `后羿射日`
- `嫦娥奔月`
- `書體`
- `篆書`
- `隸書`
- `楷書`
- `行書`
- `草書`
- `文房四寶`
- `四君子`
- `梅`
- `鶴`
- `東風`
- `青`
- `科舉制度`
- `秀才`
- `古代學校`
- `地理代稱`
- `書信代稱`
- `交友情誼代稱`
- `應用文`
- `書信結構`
- `信封書寫`
- `啟事格式`
- `柬帖格式`

### 國文考試與國寫

- `國文考試準備`
- `國中教育會考國文`
- `高中國文評量`
- `學測國文`
- `國語文寫作能力測驗`
- `語文知識題`
- `字音題`
- `字形題`
- `詞義題`
- `成語題`
- `修辭題`
- `語法題`
- `文化常識題`
- `文言文題`
- `現代文閱讀題`
- `詩歌閱讀題`
- `多文本題`
- `混合題`
- `圖表閱讀題`
- `題幹判讀`
- `反向題`
- `最佳答案題`
- `排除法`
- `回文定位`
- `證據作答`
- `簡答題`
- `比較題作答`
- `原因題作答`
- `作用題作答`
- `主旨題作答`
- `標題題作答`
- `文言翻譯題`
- `文言比較題`
- `國文考試時間管理`
- `第一輪作答`
- `標記難題`
- `最後檢查`
- `錯題紀錄`
- `錯誤分類`
- `知識型錯誤`
- `理解型錯誤`
- `讀題型錯誤`
- `粗心型錯誤`
- `間隔複習`
- `主動回想`
- `模擬測驗`
- `國寫準備`
- `國寫審題`
- `材料解讀`
- `中心立意`
- `國寫大綱`
- `知性題寫作`
- `情意題寫作`
- `議論結構`
- `敘事結構`
- `國寫開頭`
- `國寫結尾`
- `例證選擇`
- `個人經驗材料`
- `公共議題材料`
- `回應反方`
- `段落統一性`
- `段落發展`
- `作文轉承`
- `具體細節`
- `以描寫呈現`
- `語言準確`
- `語言流暢`
- `表達深度`
- `避免套語`
- `避免空泛`
- `避免流水帳`
- `避免離題`
- `國寫修改`
- `國寫校對`
- `國寫時間管理`
- `內容評量`
- `組織評量`
- `語言評量`
- `卷面格式`
- `作文自我檢查`
- `國文讀書計畫`
- `每日閱讀`
- `定期寫作`
- `字詞複習`
- `文言複習`
- `閱讀複習`
- `考試當日策略`



---

# 版本與文件維護

這份文件是依照 **KnowpareX 1.1.0** 的原始碼產生。

每次新增、刪除或重新命名函式後，建議同步更新：

- `README.md`
- 這份完整指南
- `CHANGELOG.md`
- `pyproject.toml` 的版本號

推薦檔名：

```text
KNOWPAREX_API_GUIDE.md
```
