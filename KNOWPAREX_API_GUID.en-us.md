<!--
English edition generated from the Traditional Chinese technical guide.
Executable code blocks, CLI commands, API identifiers, and literal database keys are preserved exactly.
Chinese curriculum names are retained and followed by English glosses where appropriate.
-->

# KnowpareX Complete Technical Documentation and User Guide

> 適用版本：整合「原本知識庫＋MindLeapX 課程資料」功能後的版本  
> 作者：Steve Lin／林炫銓  
> This document covers installation, command-line tools, data-source selection, curriculum features, the Python API, relationship functions, wrong-answer storage, and all currently registered categories and topics.

## Highlights of This Release

- Retains all original KnowpareX knowledge data, search, scanning, practice, wrong-answer review, export, and relationship functions.
- Adds browsing support for MindLeapX curriculum data.
- Keeps the original knowledge database and curriculum data separate by default.
- Allows `search` and `scan` to select a data source with `--source`.
- Adds the `curriculum subjects`, `books`, `units`, and `lesson` commands.
- Loads curriculum data automatically from inside the package, so users do not need to provide a file path.

---

## Table of Contents

1. [Installation, Updates, and Packaging Curriculum Data](#installation-updates-and-packaging-curriculum-data)
2. [Minimal Usage Example](#minimal-usage-example)
3. [Command-Line Interface](#command-line-interface)
   - [Data-Source Rules](#data-source-rules)
   - [Curriculum Commands](#curriculum-commands)
   - [Search](#search)
   - [Text Concept Scanner](#text-concept-scanner)
4. [Main Python API](#main-python-api)
5. [The Central library Registry](#the-central-library-registry)
6. [compare_system Data Control](#comparesystem-data-control)
7. [Programming Concept and Syntax Comparison Functions](#programming-concept-and-syntax-comparison-functions)
8. [Mathematical Relationship Functions](#mathematical-relationship-functions)
9. [General Knowledge Relationship Functions](#general-knowledge-relationship-functions)
10. [Package and Ecosystem Relationship Functions](#package-and-ecosystem-relationship-functions)
11. [Custom Relationships and Low-Level Functions](#custom-relationships-and-low-level-functions)
12. [Wrong-Answer Storage API](#wrong-answer-storage-api)
13. [Complete Examples](#complete-examples)
14. [All Current Categories and Topics](#all-current-categories-and-topics)
15. [Frequently Asked Questions and Troubleshooting](#frequently-asked-questions-and-troubleshooting)

---
# 1. Installation, Updates, and Packaging Curriculum Data

## Install from PyPI

### Windows

Recommended:

```powershell
py -m pip install knowparex
```

If `py` is unavailable on your computer, use:

```powershell
python -m pip install knowparex
```

### macOS / Linux

```bash
python3 -m pip install knowparex
```

---

## Update to the Latest Version

### Windows

```powershell
py -m pip install --upgrade knowparex
```

or:

```powershell
python -m pip install --upgrade knowparex
```

### macOS / Linux

```bash
python3 -m pip install --upgrade knowparex
```

---

## Check the Installed Version

### Windows

```powershell
py -m pip show knowparex
```

or:

```powershell
python -m pip show knowparex
```

### macOS / Linux

```bash
python3 -m pip show knowparex
```

---

## Verify the Installation

```bash
knowparex categories
```

If the installation is successful, the terminal will display all available categories.

If Windows displays:

```text
'knowparex' is not recognized as an internal or external command
```

Close and reopen PowerShell or Command Prompt. If the command still does not work, make sure Python's `Scripts` directory is included in `PATH`.<br>

Check from Python:

```python
import knowparex

print(knowparex.__version__)
```


## Published Releases Must Include the Curriculum Data File

The curriculum feature automatically reads:

```text
knowparex/data/curriculum_integrated.js
```

Users do not need to provide `--file` or know the physical file path.

When using `setuptools`, make sure `pyproject.toml` contains:

```toml
[tool.setuptools.package-data]
knowparex = ["data/*.js"]
```

It is also recommended to add the following to `MANIFEST.in`:

```text
recursive-include src/knowparex/data *.js
```

After building the package, verify that the wheel contains the curriculum data:

```bash
python3 -m build
unzip -l dist/*.whl | grep curriculum_integrated.js
```

If `knowparex/data/curriculum_integrated.js` is missing, the curriculum feature will not find its data after publication to PyPI.
---

# 2. Minimal Usage Example

```python
from knowparex import get_categories, get_items, get_topic_data

print(get_categories())
print(get_items("電學"))

records = get_topic_data("電學", "歐姆定律")

for record in records:
    print(record)
```

Import the main public interfaces at once:

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

# 3. Command-Line Interface

## Interactive Query

```bash
knowparex
```

or:

```bash
knowparex compare
```

Standalone command:

```bash
knowparex-compare
```
## Text Concept Scanner

KnowpareX provides the `scan` command, which identifies concepts from a block of text when those concepts already exist in the selected database.

This feature does not answer questions or automatically explain the entire passage. It compares the input with KnowpareX categories, topics, and structured knowledge fields, then lists the matched concepts.

### Interactive Scanning

Run:

```bash
knowparex scan
```

Use curriculum data only:

```bash
knowparex scan --source curriculum
```

Use both data sources:

```bash
knowparex scan --source all
```

### One-Time Scan

```bash
knowparex scan "流汗時汗水蒸發會吸收汽化潛熱"
```

Use the curriculum data source:

```bash
knowparex scan "絕對值表示數在線上與零的距離" --source curriculum
```

Available options:

```text
--source       knowledge、curriculum 或 all
--min-length   最短概念字數，預設 2
--json         以 JSON 輸出
```

## Practice / Test

```bash
knowparex practice
```

or:

```bash
knowparex-practice
```

## Review Wrong Answers

```bash
knowparex review
```

or:

```bash
knowparex-review
```

## List All Categories

```bash
knowparex categories
```

## List All Topics in a Category

```bash
knowparex items "電學"
```

## Display Topic Data / Output JSON

```bash
knowparex topic "電學" "歐姆定律"
knowparex topic "有機化學" "醇" --json
```
## Data-Source Rules

KnowpareX currently supports three data sources:

| Value | Description |
|---|---|
| `knowledge` | The original KnowpareX knowledge database; this is the default |
| `curriculum` | MindLeapX curriculum data |
| `all` | Use both data sources |

The default behavior does not mix data sources:

```bash
knowparex search "函數"
knowparex scan "函數"
```

The commands above use only `knowledge`.

Use the curriculum data source:

```bash
knowparex search "函數" --source curriculum
knowparex scan "函數" --source curriculum
```

The sources are combined only when explicitly requested:

```bash
knowparex search "函數" --source all
knowparex scan "函數" --source all
```

## Curriculum Commands

Curriculum data is organized as 學制 (education stage) → 科目 (subject) → 冊別 (book / volume) → 單元 (unit).

### List All Subjects

```bash
knowparex curriculum subjects
```

The output contains each subject code and its Chinese name, for example:

```text
math    數學
chinese 國文
physics 物理
```

### List Books for a Subject

```bash
knowparex curriculum books math
```

Optionally restrict the education stage:

```bash
knowparex curriculum books math --stage 高中
```

`--category` is an alias for `--stage`:

```bash
knowparex curriculum books math --category 高中
```

### List Units in a Book

```bash
knowparex curriculum units math 高一上
```

When duplicate names are possible, specify the education stage:

```bash
knowparex curriculum units math 高一上 --stage 高中
```

### Display a Lesson

```bash
knowparex curriculum lesson math 高一上 函數 --stage 高中
```

The unit name may be a partial keyword. If multiple units match, the program asks for a more specific name or for `--stage`.

### Command Syntax Overview

```text
knowparex curriculum subjects
knowparex curriculum books <科目> [--stage <學制>]
knowparex curriculum units <科目> <冊別> [--stage <學制>]
knowparex curriculum lesson <科目> <冊別> <單元> [--stage <學制>]
```

> `curriculum` and the following `subjects`, `books`, `units`, or `lesson` are subcommands and cannot be omitted arbitrarily.

## Search

KnowpareX can search category names, topic names, and all structured knowledge records.

KnowpareX can search category names, topic names, and all structured knowledge records.

### Basic Search

```bash
knowparex search "能量"
```

只搜尋課程資料：

```bash
knowparex search "能量" --source curriculum
```

同時搜尋兩種資料：

```bash
knowparex search "能量" --source all
```

The default search checks:

- Category names
- Topic names
- Relationship fields
- Left-side content and labels
- Right-side content and labels

The default search covers:

- Category names
- Topic names
- Relationship fields
- Left-side content and labels
- Right-side content and labels

---

### Summary Mode

Show search statistics and matching topics without displaying every knowledge record.

Show search statistics and matching topics without displaying every knowledge record.

```bash
knowparex search "能量" --summary
```

---

### Exact Match

Only match fields whose complete content equals the search keyword.

Match only fields whose entire content equals the search keyword.

```bash
knowparex search "醇" --exact
```

For example, this can match `醇` without matching `乙醇` or `醇厚`.

For example, this can match 醇 (alcohol) without matching 乙醇 (ethanol) or 醇厚 (mellow / rich).

---

### Topic-Only Search

Search only category and topic names.

Search only category and topic names.

```bash
knowparex search "水" --topic-only
```

---

### Record-Only Search

Search only the structured knowledge records, without treating category or topic names as direct matches.

Search only structured knowledge records, without treating category or topic names as direct matches.

```bash
knowparex search "電流" --record-only
```

---

### Search Within One Category

Search only inside a specified category.

Search only within the specified category.

```bash
knowparex search "電流" --category "磁學"
```

---

### Limit Displayed Records

Limit the number of detailed knowledge records shown in the terminal.

Limit the number of detailed records displayed in the terminal.

```bash
knowparex search "水" --limit 20
```

---

### JSON Search Output

Return structured JSON for websites, scripts, or other applications.

Return structured JSON for websites, scripts, or other applications.

```bash
knowparex search "能量" --json
```

---

### Combine Search Options

Search options can be combined.

Search options can be combined.

```bash
knowparex search "電流" --category "磁學" --limit 10
```

```bash
knowparex search "能量" --summary --category "熱學與熱力學"
```
### Count Results

Show only the number of matching categories, topics, and knowledge records.

Show only the counts of matching categories, topics, and knowledge records.

```bash
knowparex search "水" --count
```

This is useful when a keyword produces a large number of results.

This is useful for checking the size of a large result set before displaying it.

---

### Random Result

Randomly select one matching knowledge record.

Randomly select one matching knowledge record.

```bash
knowparex search "能量" --random
```

This can also be combined with a category filter:

It can also be combined with a category filter:

```bash
knowparex search "能量" --category "植物與生態" --random
```

This mode can be used for quick review or discovering unexpected connections.

This mode is useful for quick review or discovering unexpected knowledge connections.

---

### Tree View

Display matching topics grouped by category in a tree structure.

Display matching topics in a tree grouped by category.

```bash
knowparex search "能量" --tree
```

Example:

```text
├── 植物與生態
    ├── 能量金字塔（7 筆）
    └── 食物鏈與食物網（2 筆）
├── 熱學與熱力學
    ├── 內能（1 筆）
    └── 潛熱（4 筆）
└── 細胞與代謝
    └── ATP（3 筆）
```

This mode provides a compact overview of how one keyword appears across different subjects.

This mode provides a compact view of how a keyword is distributed across categories and topics.

---

### Open a Topic from Search

Display a numbered topic list and open the complete selected topic.

Display a numbered topic list and open the full selected topic.

```bash
knowparex search "能量" --open
```

Example:

```text
1. 植物與生態 / 能量金字塔
2. 細胞與代謝 / ATP
3. 熱學與熱力學 / 內能
0. 取消

請輸入要開啟的主題編號：
```

After selecting a topic, KnowpareX displays all records in that topic, not only records containing the search keyword.

After selection, KnowpareX displays every record in the topic, not only records containing the keyword.

---
## Additional Tools

### Database Statistics

```bash
knowparex stats
```

Displays category counts, topic counts, knowledge-record counts, averages, largest topics, and common relationship types.

Display category counts, topic counts, knowledge-record counts, averages, the largest topic, and common relationship types.

### Today's Knowledge

```bash
knowparex today
```

Displays one recommended topic each day. The result remains the same during the same calendar day.

Recommend one topic per day; the result stays the same throughout the same calendar day.

### Explain a Topic

```bash
knowparex explain "有機化學" "醇"
```

Converts structured records into readable sentences without adding information outside the database.

Convert structured records into readable sentences without adding information outside the database.

### Export a Topic

```bash
knowparex export "有機化學" "醇" --format md
knowparex export "有機化學" "醇" --format txt
knowparex export "有機化學" "醇" --format json
```

Specify an output filename:

```bash
knowparex export "有機化學" "醇" --format json --output alcohol.json
```

Supported formats:

- `md`
- `txt`
- `json`

### Related Topics

```bash
knowparex related "有機化學" "醇"
```

Limit the number of results:

```bash
knowparex related "有機化學" "醇" --limit 5
```

Related topics are estimated from shared text and knowledge fields. The result is intended for exploration and may include unexpected matches.

Related topics are estimated from shared text and knowledge fields. This feature is intended for exploration and may produce unexpected matches.
### Search Display Options
Available search options:

```text
--source        Select knowledge, curriculum, or all
--summary       Show only the summary and matching topics
--exact         Match complete field contents only
--topic-only    Search category and topic names only
--record-only   Search knowledge records only
--category      Search inside one specified category
--limit         Limit the number of displayed records
--json          Output search results as JSON
```

```text
--count     Show search result counts only
--random    Show one random matching record
--tree      Display matching topics as a category tree
--open      Select and open a complete topic
```

```text
--source    選擇 knowledge、curriculum 或 all
--count     只顯示搜尋統計
--random    隨機顯示一筆符合紀錄
--tree      以分類樹狀結構顯示主題
--open      選擇並開啟完整主題
```

Only one of `--count`, `--random`, `--tree`, `--open`, or `--json` should be used at a time.

Only one of `--count`, `--random`, `--tree`, `--open`, or `--json` may be used at a time.

## View Help

```bash
knowparex --help
```

---

# 4. Main Python API

## `get_categories(source="knowledge") -> list[str]`

Return all category names from the selected data source.

- `knowledge`: the original knowledge database
- `curriculum`: curriculum data
- `all`: merge both sources

```python
from knowparex import get_categories

for category in get_categories():
    print(category)

for category in get_categories(source="curriculum"):
    print(category)
```

## `get_items(category: str, source="knowledge") -> list[str]`

Return all topics in a category from the selected data source.

```python
from knowparex import get_items

items = get_items("電學")

course_items = get_items(
    "課程 / 高中 / 數學",
    source="curriculum",
)

for item in items:
    print(item)
```

A missing category raises `KeyError`:

```python
try:
    items = get_items("不存在的分類")
except KeyError as error:
    print(error)
```

## `get_topic_data(category: str, item: str, source="knowledge") -> list[dict]`

Return relationship records for a topic from the selected data source. The original knowledge database executes a registered function, while curriculum data is converted dynamically by the curriculum adapter into the same record format.

```python
from knowparex import get_topic_data

records = get_topic_data("電學", "歐姆定律")

for record in records:
    print(record)
```

Record format:

```python
{
    "relation": "關係名稱",
    "code_a": "左側內容",
    "language_a": "左側標籤",
    "code_b": "右側內容",
    "language_b": "右側標籤",
}
```

Formatted display:

```python
for record in get_topic_data("電學", "歐姆定律"):
    print(
        f'{record["code_a"]} '
        f'--[{record["relation"]}]--> '
        f'{record["code_b"]}'
    )
```

## `topic_exists(category: str, item: str, source="knowledge") -> bool`

Check whether a category and topic exist in the selected data source.

```python
from knowparex import topic_exists

print(topic_exists("電學", "歐姆定律"))
```

Safe lookup:

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

## Curriculum Python API

These functions are available from:

```python
from knowparex.curriculum_adapter import (
    get_subjects,
    get_books,
    get_units,
    find_curriculum_topic,
    get_curriculum_categories,
    get_curriculum_items,
    get_curriculum_topic_data,
)
```

### `get_subjects()`

List all curriculum subject codes and their Chinese names.

```python
for subject in get_subjects():
    print(subject["key"], subject["name"])
```

### `get_books(subject, stage=None)`

List the books / volumes for a subject.

```python
books = get_books("math", stage="高中")
```

### `get_units(subject, book, stage=None)`

List the units in a book / volume.

```python
units = get_units("math", "高一上", stage="高中")
```

### `find_curriculum_topic(subject, book, unit, stage=None)`

Resolve the curriculum category and topic names used by KnowpareX from a subject, book / volume, and unit keyword.

```python
category, item = find_curriculum_topic(
    "math",
    "高一上",
    "函數",
    stage="高中",
)
```

### `get_curriculum_topic_data(category, item)`

Return structured relationship records for a curriculum unit.

```python
records = get_curriculum_topic_data(category, item)
```

Curriculum records use the same unified KnowpareX format:

```python
{
    "relation": "關係名稱",
    "code_a": "左側內容",
    "language_a": "左側標籤",
    "code_b": "右側內容",
    "language_b": "右側標籤",
}
```

---

# 5. The Central `library` Registry

`library` is a two-level dictionary:

```python
library = {
    "分類名稱": {
        "項目名稱": 函式,
    },
}
```

Import:

```python
from knowparex import library
```

List all categories:

```python
for category in library:
    print(category)
```

List all topics in a category:

```python
for item in library["電學"]:
    print(item)
```

Execute a topic directly:

```python
library["電學"]["歐姆定律"]()
```

Safe execution:

```python
category = "電學"
item = "歐姆定律"

if category in library and item in library[category]:
    library[category][item]()
else:
    print("找不到分類或項目")
```

When registering a new topic in `system_library.py`, do not add parentheses on the right-hand side:

```python
# 正確：儲存函式本身
"歐姆定律": physics_electricity.ohms_law

# 錯誤：匯入時立刻執行
"歐姆定律": physics_electricity.ohms_law()
```

---

# 6. `compare_system` Data Control

Import:

```python
from knowparex import compare_system
```

| Function | Generated Relationship |
|---|---|
| `set_show(value)` | `None` |
| `clear_data()` | `None` |
| `get_data()` | `None` |
| `save_data(relation, code_a, language_a, code_b, language_b)` | `None` |
| `nothing()` | `None` |

## `set_show(value)`

Control whether relationship functions print their output immediately.

```python
compare_system.set_show(True)
compare_system.set_show(False)
```

## `clear_data()`

Clear previously collected relationship data.

```python
compare_system.clear_data()
```

## `get_data()`

Return a copy of the collected data.

```python
records = compare_system.get_data()
```

## Collect Data Without Immediate Output

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

For normal topic lookup, prefer `get_topic_data()` because it already performs this process automatically.

---

# 7. Programming Concept and Syntax Comparison Functions

These functions use four parameters:

```python
compare_system.函式名稱(
    code_a,
    language_a,
    code_b,
    language_b,
)
```

| Function | Generated Relationship |
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

## 3 × 3 Comparison Matrix

| Concept \ Syntax | Different | Similar | Same |
|---|---|---|---|
| 不同 | `different` | `codedifferentbutsyntaxsimilar` | `codedifferentbutsyntaxsame` |
| 相似 | `codesimilarbutsyntaxdifferent` | `similar` | `codesimilarbutsyntaxsame` |
| 相同 | `codesamebutsyntaxdifferent` | `codesamebutsyntaxsimilar` | `exactsame` |

Example:

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

# 8. Mathematical Relationship Functions

These functions use four parameters:

```python
compare_system.函式名稱(
    code_a,
    language_a,
    code_b,
    language_b,
)
```

| Function | Generated Relationship |
|---|---|
| `inverselyproportionalto(code_a, language_a, code_b, language_b)` | `反比於 (Inversely Proportional To)` |
| `approximately(code_a, language_a, code_b, language_b)` | `約為 (Approximately)` |
| `equal(code_a, language_a, code_b, language_b)` | `=` |
| `bigger(code_a, language_a, code_b, language_b)` | `>` |
| `smaller(code_a, language_a, code_b, language_b)` | `<` |
| `equalorbigger(code_a, language_a, code_b, language_b)` | `>=` |
| `equalorsmaller(code_a, language_a, code_b, language_b)` | `<=` |
| `notequal(code_a, language_a, code_b, language_b)` | `!=` |
| `approximatelyequal(code_a, language_a, code_b, language_b)` | `≈` |
| `proportionalto(code_a, language_a, code_b, language_b)` | `正比於 (Proportional To)` |
| `equivalentto(code_a, language_a, code_b, language_b)` | `等價於 (Equivalent To)` |
| `calculatedby(code_a, language_a, code_b, language_b)` | `計算方式 (Calculated By)` |
| `simplifiedto(code_a, language_a, code_b, language_b)` | `化簡為 (Simplified To)` |
| `factorizedto(code_a, language_a, code_b, language_b)` | `因式分解為 (Factorized To)` |

Example:

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

# 9. General Knowledge Relationship Functions

These functions use four parameters:

```python
compare_system.函式名稱(
    content_a,
    label_a,
    content_b,
    label_b,
)
```

| Function | Generated Relationship |
|---|---|
| `definition(content_a, label_a, content_b, label_b)` | `定義為 (Defined As)` |
| `exampleof(content_a, label_a, content_b, label_b)` | `是……的例子 (Is an Example Of)` |
| `partof(content_a, label_a, content_b, label_b)` | `是……的一部分 (Is Part Of)` |
| `typeof(content_a, label_a, content_b, label_b)` | `是……的一種類型 (Is a Type Of)` |
| `causes(content_a, label_a, content_b, label_b)` | `造成 (Causes)` |
| `resultsin(content_a, label_a, content_b, label_b)` | `導致 (Results In)` |
| `requires(content_a, label_a, content_b, label_b)` | `需要 (Requires)` |
| `before(content_a, label_a, content_b, label_b)` | `在……之前 (Before)` |
| `after(content_a, label_a, content_b, label_b)` | `在……之後 (After)` |
| `opposite(content_a, label_a, content_b, label_b)` | `與……相反 (Opposite Of)` |
| `related(content_a, label_a, content_b, label_b)` | `與……相關 (Related To)` |
| `translates(content_a, label_a, content_b, label_b)` | `翻譯為 (Translates To)` |
| `composedof(content_a, label_a, content_b, label_b)` | `由……組成 (Composed Of)` |
| `functionof(content_a, label_a, content_b, label_b)` | `功能是 (Function Is)` |
| `locatedin(content_a, label_a, content_b, label_b)` | `位於 (Located In)` |
| `characterizedby(content_a, label_a, content_b, label_b)` | `特徵是 (Characterized By)` |

Example:

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

# 10. Package and Ecosystem Relationship Functions

| Function | Generated Relationship |
|---|---|
| `samepurpose(content_a, label_a, content_b, label_b)` | `用途相近 (Similar Purpose)` |
| `alternativeof(content_a, label_a, content_b, label_b)` | `可作為……的替代方案 (Alternative To)` |
| `equivalentrole(content_a, label_a, content_b, label_b)` | `在生態系中的角色相近 (Equivalent Ecosystem Role)` |
| `wrapperof(content_a, label_a, content_b, label_b)` | `是……的語言綁定或包裝 (Language Binding or Wrapper Of)` |
| `depends_on(content_a, label_a, content_b, label_b)` | `依賴 (Depends On)` |
| `builtwith(content_a, label_a, content_b, label_b)` | `以……建構 (Built With)` |
| `provides(content_a, label_a, content_b, label_b)` | `提供 (Provides)` |
| `usedfor(content_a, label_a, content_b, label_b)` | `用於 (Used For)` |
| `customrelation(relation, content_a, label_a, content_b, label_b)` | `None` |

Example:

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

# 11. Custom Relationships and Low-Level Functions

## `customrelation(...)`

Create a custom relationship when no dedicated function exists.

```python
compare_system.customrelation(
    "生態系角色相近",
    "pygame",
    "Python 套件",
    "raylib",
    "C/C++ 函式庫",
)
```

Full signature:

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

Create and store a low-level relationship record directly.

```python
record = compare_system.save_data(
    "定義為",
    "變數",
    "程式概念",
    "用來保存資料的名稱",
    "中文解釋",
)
```

Return format:

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

Represent a topic that currently has no data.

```python
record = compare_system.nothing()
```

Returns:

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

# 12. Wrong-Answer Storage API

These functions are available from:

```python
from knowparex.storage import (
    get_data_directory,
    get_wrong_questions_path,
    load_wrong_questions,
    save_wrong_questions,
)
```

## `get_data_directory() -> Path`

Return the KnowpareX user-data directory, creating it when necessary.

Typical locations:

```text
macOS:
~/Library/Application Support/KnowpareX/

Windows:
%APPDATA%/KnowpareX/

Linux:
$XDG_DATA_HOME/KnowpareX/
或 ~/.local/share/KnowpareX/
```

Usage:

```python
from knowparex.storage import get_data_directory

print(get_data_directory())
```

## `get_wrong_questions_path() -> Path`

Return the full path to the wrong-answer JSON file.

```python
from knowparex.storage import get_wrong_questions_path

print(get_wrong_questions_path())
```

## `load_wrong_questions() -> list[dict]`

Load wrong answers. If the file is missing, malformed, or unreadable, return an empty list.

```python
from knowparex.storage import load_wrong_questions

questions = load_wrong_questions()
```

## `save_wrong_questions(questions) -> Path`

Save wrong answers and return the file path.

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

These functions normally do not need to be called manually. Use:

```bash
knowparex practice
knowparex review
```

instead.

---

# 13. Complete Examples

## Example 1: Simple Query Tool

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

## Example 2: Create Your Own Knowledge Topic

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

Then register the function in your own library:

```python
my_library = {
    "生物": {
        "光合作用": my_notes.photosynthesis,
    }
}

my_library["生物"]["光合作用"]()
```

## Example 3: Export a Topic as JSON

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

# 14. All Current Categories and Topics

This version contains **66 categories** and **1,580 registered topics**.

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

### 數與數系 (Numbers and Number Systems)

- `整數 (Integers)`
- `絕對值 (Absolute Value)`
- `分數 (Fractions)`
- `百分比 (Percentages)`
- `指數 (Exponents)`
- `根式 (Radicals)`

### 代數 (Algebra)

- `同類項 (Like Terms)`
- `分配律 (Distributive Property)`
- `因式分解 (Factorization)`
- `恆等式 (Identities)`

### 方程式與不等式 (Equations and Inequalities)

- `一元一次方程式 (Linear Equations in One Variable)`
- `聯立方程式 (Systems of Equations)`
- `二次方程式 (Quadratic Equations)`
- `不等式 (Inequalities)`

### 函數 (Functions)

- `函數值 (Function Values)`
- `一次函數 (Linear Functions)`
- `二次函數 (Quadratic Functions)`
- `定義域 (Domain)`

### 幾何 (Geometry)

- `三角形 (Triangles)`
- `畢氏定理 (Pythagorean Theorem)`
- `圓 (Circles)`
- `多邊形 (Polygons)`
- `坐標幾何 (Coordinate Geometry)`

### 三角函數 (Trigonometry)

- `基本三角比 (Basic Trigonometric Ratios)`
- `特殊角 (Special Angles)`
- `角度與弧度 (Degrees and Radians)`

### 數列 (Sequences)

- `等差數列 (Arithmetic Sequences)`
- `等比數列 (Geometric Sequences)`

### 機率 (Probability)

- `基本機率 (Basic Probability)`
- `餘事件 (Complementary Events)`

### 統計 (Statistics)

- `平均數 (Mean)`
- `中位數 (Median)`
- `眾數 (Mode)`
- `全距 (Range)`

### 電學 (Electricity)

- `電荷 (Electric Charge)`
- `起電 (Electrification)`
- `導體與絕緣體 (Conductors and Insulators)`
- `庫侖定律 (Coulomb's Law)`
- `電場 (Electric Field)`
- `電位 (Electric Potential)`
- `電流 (Electric Current)`
- `電壓 (Voltage)`
- `電阻 (Resistance)`
- `歐姆定律 (Ohm's Law)`
- `安培計與伏特計 (Ammeters and Voltmeters)`
- `串聯電路 (Series Circuits)`
- `並聯電路 (Parallel Circuits)`
- `電功率 (Electric Power)`
- `電能 (Electrical Energy)`
- `用電安全 (Electrical Safety)`

### 磁學 (Magnetism)

- `磁鐵 (Magnets)`
- `磁場 (Magnetic Field)`
- `地磁 (Earth's Magnetic Field)`
- `電流的磁效應 (Magnetic Effect of Electric Current)`
- `螺線管 (Solenoid)`
- `電磁鐵 (Electromagnet)`
- `載流導線的磁力 (Magnetic Force on a Current-Carrying Wire)`
- `電動機 (Electric Motor)`
- `電磁感應 (Electromagnetic Induction)`
- `發電機 (Generator)`
- `變壓器 (Transformer)`

### 波動與聲音 (Waves and Sound)

- `振動 (Vibration)`
- `簡諧運動 (Simple Harmonic Motion)`
- `單擺 (Simple Pendulum)`
- `波 (Waves)`
- `橫波與縱波 (Transverse and Longitudinal Waves)`
- `波長、頻率與波速 (Wavelength, Frequency, and Wave Speed)`
- `反射 (Reflection)`
- `折射 (Refraction)`
- `繞射 (Diffraction)`
- `干涉 (Interference)`
- `駐波 (Standing Waves)`
- `聲音 (Sound)`
- `音調、響度與音色 (Pitch, Loudness, and Timbre)`
- `共振 (Resonance)`
- `都卜勒效應 (Doppler Effect)`

### 光學 (Optics)

- `光 (Light)`
- `發光體 (Luminous Objects)`
- `反射 (Reflection)`
- `規則反射與漫反射 (Specular and Diffuse Reflection)`
- `平面鏡 (Plane Mirrors)`
- `球面鏡 (Spherical Mirrors)`
- `折射 (Refraction)`
- `折射率 (Refractive Index)`
- `全反射 (Total Internal Reflection)`
- `透鏡 (Lenses)`
- `凸透鏡成像 (Image Formation by Convex Lenses)`
- `透鏡公式 (Lens Equation)`
- `眼睛 (The Eye)`
- `色光 (Colored Light)`

### 熱學與熱力學 (Heat and Thermodynamics)

- `溫度 (Temperature)`
- `溫度計 (Thermometers)`
- `熱 (Heat)`
- `比熱 (Specific Heat Capacity)`
- `熱量測定 (Calorimetry)`
- `相變 (Phase Changes)`
- `潛熱 (Latent Heat)`
- `熱傳導 (Thermal Conduction)`
- `熱對流 (Convection)`
- `熱輻射 (Thermal Radiation)`
- `熱膨脹 (Thermal Expansion)`
- `氣體定律 (Gas Laws)`
- `內能 (Internal Energy)`
- `熱力學第一定律 (First Law of Thermodynamics)`

### 流體與簡單機械 (Fluids and Simple Machines)

- `壓力 (Pressure)`
- `液體壓力 (Liquid Pressure)`
- `大氣壓力 (Atmospheric Pressure)`
- `帕斯卡原理 (Pascal's Principle)`
- `浮力 (Buoyancy)`
- `浮沉 (Floating and Sinking)`
- `連續方程式 (Continuity Equation)`
- `白努力原理 (Bernoulli's Principle)`
- `力矩 (Torque)`
- `轉動平衡 (Rotational Equilibrium)`
- `槓桿 (Levers)`
- `滑輪 (Pulleys)`
- `斜面 (Inclined Planes)`
- `機械利益 (Mechanical Advantage)`

### 物質與分離 (Matter and Separation)

- `物質 (Matter)`
- `元素、化合物與混合物 (Elements, Compounds, and Mixtures)`
- `均勻與非均勻混合物 (Homogeneous and Heterogeneous Mixtures)`
- `物理性質 (Physical Properties)`
- `化學性質 (Chemical Properties)`
- `物理變化 (Physical Changes)`
- `化學變化 (Chemical Changes)`
- `物質三態 (Three States of Matter)`
- `相變 (Phase Changes)`
- `密度 (Density)`
- `過濾 (Filtration)`
- `蒸餾 (Distillation)`
- `色層分析 (Chromatography)`

### 原子與週期表 (Atoms and the Periodic Table)

- `原子 (Atoms)`
- `質子、中子與電子 (Protons, Neutrons, and Electrons)`
- `原子序 (Atomic Number)`
- `質量數 (Mass Number)`
- `同位素 (Isotopes)`
- `平均原子量 (Average Atomic Mass)`
- `離子 (Ions)`
- `電子層 (Electron Shells)`
- `電子排列 (Electron Configuration)`
- `週期表 (Periodic Table)`
- `金屬、非金屬與類金屬 (Metals, Nonmetals, and Metalloids)`
- `鹼金屬 (Alkali Metals)`
- `鹼土金屬 (Alkaline Earth Metals)`
- `鹵素 (Halogens)`
- `鈍氣 (Noble Gases)`
- `週期趨勢 (Periodic Trends)`

### 化學鍵與化學式 (Chemical Bonds and Formulas)

- `化學鍵 (Chemical Bonds)`
- `離子鍵 (Ionic Bonds)`
- `共價鍵 (Covalent Bonds)`
- `金屬鍵 (Metallic Bonds)`
- `路易斯結構 (Lewis Structures)`
- `八隅體規則 (Octet Rule)`
- `電負度 (Electronegativity)`
- `分子極性 (Molecular Polarity)`
- `分子間作用力 (Intermolecular Forces)`
- `氫鍵 (Hydrogen Bonding)`
- `分子形狀 (Molecular Geometry)`
- `化學式 (Chemical Formulas)`
- `離子化合物化學式 (Formulas of Ionic Compounds)`
- `常見離子 (Common Ions)`
- `命名 (Nomenclature)`

### 化學反應與莫耳 (Chemical Reactions and the Mole)

- `化學反應 (Chemical Reactions)`
- `質量守恆 (Conservation of Mass)`
- `平衡化學方程式 (Balancing Chemical Equations)`
- `反應類型 (Reaction Types)`
- `燃燒 (Combustion)`
- `降水 (Precipitation)`
- `莫耳 (The Mole)`
- `粒子數 (Number of Particles)`
- `莫耳質量 (Molar Mass)`
- `實驗式與分子式 (Empirical and Molecular Formulas)`
- `化學計量 (Stoichiometry)`
- `限量試劑 (Limiting Reagent)`
- `產率 (Yield)`

### 溶液與酸鹼 (Solutions, Acids, and Bases)

- `溶液 (Solutions)`
- `溶解度 (Solubility)`
- `飽和溶液 (Saturated Solutions)`
- `質量百分濃度 (Mass Percent Concentration)`
- `體積莫耳濃度 (Molar Concentration)`
- `稀釋 (Dilution)`
- `電解質 (Electrolytes)`
- `酸 (Acids)`
- `鹼 (Bases)`
- `強酸強鹼與弱酸弱鹼 (Strong and Weak Acids and Bases)`
- `pH`
- `pOH`
- `中和反應 (Neutralization)`
- `酸鹼指示劑 (Acid-Base Indicators)`
- `酸鹼滴定 (Acid-Base Titration)`
- `緩衝溶液 (Buffer Solutions)`

### 氧化還原與電化學 (Redox and Electrochemistry)

- `氧化與還原 (Oxidation and Reduction)`
- `氧化劑與還原劑 (Oxidizing and Reducing Agents)`
- `氧化數 (Oxidation Numbers)`
- `平衡氧化還原反應 (Balancing Redox Reactions)`
- `金屬活動性 (Metal Reactivity)`
- `腐蝕 (Corrosion)`
- `原電池 (Galvanic Cells)`
- `丹尼爾電池 (Daniell Cell)`
- `電解 (Electrolysis)`
- `電鍍 (Electroplating)`
- `法拉第定律 (Faraday's Laws)`
- `電池 (Batteries)`

### 氣體、熱化學與平衡 (Gases, Thermochemistry, and Equilibrium)

- `氣體壓力 (Gas Pressure)`
- `波以耳定律 (Boyle's Law)`
- `查理定律 (Charles's Law)`
- `給呂薩克定律 (Gay-Lussac's Law)`
- `亞佛加厥定律 (Avogadro's Law)`
- `理想氣體 (Ideal Gases)`
- `分壓 (Partial Pressure)`
- `熱化學 (Thermochemistry)`
- `吸熱與放熱 (Endothermic and Exothermic Processes)`
- `焓 (Enthalpy)`
- `赫斯定律 (Hess's Law)`
- `鍵能 (Bond Energy)`
- `反應速率 (Reaction Rate)`
- `碰撞理論 (Collision Theory)`
- `活化能 (Activation Energy)`
- `化學平衡 (Chemical Equilibrium)`
- `平衡常數 (Equilibrium Constant)`
- `勒沙特列原理 (Le Châtelier's Principle)`

### 有機化學 (Organic Chemistry)

- `有機化合物 (Organic Compounds)`
- `烴 (Hydrocarbons)`
- `烷類 (Alkanes)`
- `烯類與炔類 (Alkenes and Alkynes)`
- `同分異構物 (Isomers)`
- `官能基 (Functional Groups)`
- `醇 (Alcohols)`
- `羧酸 (Carboxylic Acids)`
- `酯 (Esters)`
- `聚合物 (Polymers)`
- `加成聚合 (Addition Polymerization)`
- `縮合聚合 (Condensation Polymerization)`
- `醣類 (Carbohydrates)`
- `脂質 (Lipids)`
- `蛋白質 (Proteins)`
- `清潔劑 (Detergents)`

### 細胞與代謝 (Cells and Metabolism)

- `細胞學說 (Cell Theory)`
- `原核細胞與真核細胞 (Prokaryotic and Eukaryotic Cells)`
- `細胞膜 (Cell Membrane)`
- `細胞質 (Cytoplasm)`
- `細胞核 (Nucleus)`
- `粒線體 (Mitochondria)`
- `葉綠體 (Chloroplasts)`
- `核糖體 (Ribosomes)`
- `內質網 (Endoplasmic Reticulum)`
- `高基氏體 (Golgi Apparatus)`
- `溶體與液胞 (Lysosomes and Vacuoles)`
- `細胞壁 (Cell Wall)`
- `擴散 (Diffusion)`
- `滲透作用 (Osmosis)`
- `主動運輸 (Active Transport)`
- `胞吞與胞吐 (Endocytosis and Exocytosis)`
- `酵素 (Enzymes)`
- `酵素專一性 (Enzyme Specificity)`
- `影響酵素活性的因素 (Factors Affecting Enzyme Activity)`
- `ATP`
- `光合作用 (Photosynthesis)`
- `細胞呼吸 (Cellular Respiration)`
- `發酵 (Fermentation)`

### 遺傳與演化 (Genetics and Evolution)

- `染色體 (Chromosomes)`
- `細胞週期 (Cell Cycle)`
- `有絲分裂 (Mitosis)`
- `減數分裂 (Meiosis)`
- `互換 (Crossing Over)`
- `DNA`
- `DNA複製 (DNA Replication)`
- `基因 (Genes)`
- `RNA`
- `轉錄 (Transcription)`
- `轉譯 (Translation)`
- `中心法則 (Central Dogma)`
- `孟德爾遺傳定律 (Mendelian Inheritance)`
- `基因型與表現型 (Genotype and Phenotype)`
- `顯性關係 (Dominance Relationships)`
- `血型 (Blood Types)`
- `性聯遺傳 (Sex-Linked Inheritance)`
- `突變 (Mutations)`
- `生物技術 (Biotechnology)`
- `PCR`
- `演化 (Evolution)`
- `自然選擇 (Natural Selection)`
- `演化證據 (Evidence for Evolution)`
- `物種形成 (Speciation)`
- `生物分類 (Biological Classification)`
- `三域系統 (Three-Domain System)`
- `病毒 (Viruses)`

### 植物與生態 (Plants and Ecology)

- `植物組織 (Plant Tissues)`
- `根 (Roots)`
- `莖 (Stems)`
- `葉 (Leaves)`
- `蒸散作用 (Transpiration)`
- `植物體內運輸 (Transport in Plants)`
- `向性 (Tropisms)`
- `花 (Flowers)`
- `傳粉與受精 (Pollination and Fertilization)`
- `種子與果實 (Seeds and Fruits)`
- `萌發 (Germination)`
- `生態層次 (Levels of Ecological Organization)`
- `棲地與棲位 (Habitat and Niche)`
- `族群成長 (Population Growth)`
- `生物交互作用 (Biological Interactions)`
- `食物鏈與食物網 (Food Chains and Food Webs)`
- `營養階層 (Trophic Levels)`
- `能量金字塔 (Energy Pyramids)`
- `碳循環 (Carbon Cycle)`
- `氮循環 (Nitrogen Cycle)`
- `生態演替 (Ecological Succession)`
- `生物多樣性 (Biodiversity)`
- `保育 (Conservation)`

### 人體生理 (Human Physiology)

- `人體構造層次 (Chinese curriculum term)`
- `恆定性 (Chinese curriculum term)`
- `消化系統 (Chinese curriculum term)`
- `口腔、食道與胃 (Chinese curriculum term)`
- `小腸、肝臟與胰臟 (Chinese curriculum term)`
- `呼吸系統 (Chinese curriculum term)`
- `呼吸運動 (Chinese curriculum term)`
- `氣體交換 (Chinese curriculum term)`
- `循環系統 (Chinese curriculum term)`
- `心臟 (Chinese curriculum term)`
- `血管 (Chinese curriculum term)`
- `血液 (Chinese curriculum term)`
- `淋巴系統 (Chinese curriculum term)`
- `泌尿系統 (Chinese curriculum term)`
- `腎元 (Chinese curriculum term)`
- `神經系統 (Chinese curriculum term)`
- `神經元 (Chinese curriculum term)`
- `反射作用 (Chinese curriculum term)`
- `內分泌系統 (Chinese curriculum term)`
- `血糖調節 (Chinese curriculum term)`
- `免疫系統 (Chinese curriculum term)`
- `抗原與抗體 (Chinese curriculum term)`
- `疫苗 (Chinese curriculum term)`
- `肌肉與骨骼系統 (Chinese curriculum term)`
- `生殖系統 (Chinese curriculum term)`
- `月經週期 (Chinese curriculum term)`

### 地質學 (Geology)

- `地球內部分層 (Chinese curriculum term)`
- `岩石圈與軟流圈 (Chinese curriculum term)`
- `大陸地殼與海洋地殼 (Chinese curriculum term)`
- `板塊構造 (Chinese curriculum term)`
- `張裂型板塊邊界 (Chinese curriculum term)`
- `聚合型板塊邊界 (Chinese curriculum term)`
- `錯動型板塊邊界 (Chinese curriculum term)`
- `大陸漂移 (Chinese curriculum term)`
- `海底擴張 (Chinese curriculum term)`
- `地震 (Chinese curriculum term)`
- `地震波 (Chinese curriculum term)`
- `地震規模與震度 (Chinese curriculum term)`
- `斷層 (Chinese curriculum term)`
- `褶皺 (Chinese curriculum term)`
- `火山 (Chinese curriculum term)`
- `岩漿黏度 (Chinese curriculum term)`
- `礦物 (Chinese curriculum term)`
- `火成岩 (Chinese curriculum term)`
- `沉積岩 (Chinese curriculum term)`
- `變質岩 (Chinese curriculum term)`
- `岩石循環 (Chinese curriculum term)`
- `風化、侵蝕與沉積 (Chinese curriculum term)`
- `相對定年 (Chinese curriculum term)`
- `放射性定年 (Chinese curriculum term)`

### 大氣與海洋 (Atmosphere and Oceans)

- `大氣組成 (Chinese curriculum term)`
- `大氣分層 (Chinese curriculum term)`
- `臭氧層 (Chinese curriculum term)`
- `氣壓 (Chinese curriculum term)`
- `風 (Chinese curriculum term)`
- `高低氣壓 (Chinese curriculum term)`
- `濕度 (Chinese curriculum term)`
- `雲 (Chinese curriculum term)`
- `降水 (Precipitation)`
- `氣團與鋒面 (Chinese curriculum term)`
- `冷鋒與暖鋒 (Chinese curriculum term)`
- `颱風 (Chinese curriculum term)`
- `季風 (Chinese curriculum term)`
- `海陸風 (Chinese curriculum term)`
- `天氣與氣候 (Chinese curriculum term)`
- `氣候因素 (Chinese curriculum term)`
- `水循環 (Chinese curriculum term)`
- `地下水 (Chinese curriculum term)`
- `海水鹽度 (Chinese curriculum term)`
- `洋流 (Chinese curriculum term)`
- `海浪與潮汐 (Chinese curriculum term)`
- `聖嬰與反聖嬰 (Chinese curriculum term)`

### 天文與環境 (Astronomy and the Environment)

- `宇宙尺度 (Chinese curriculum term)`
- `大霹靂理論 (Chinese curriculum term)`
- `恆星 (Chinese curriculum term)`
- `恆星演化 (Chinese curriculum term)`
- `赫羅圖 (Chinese curriculum term)`
- `太陽系 (Chinese curriculum term)`
- `類地行星與類木行星 (Chinese curriculum term)`
- `地球自轉 (Chinese curriculum term)`
- `地球公轉與四季 (Chinese curriculum term)`
- `二分二至 (Chinese curriculum term)`
- `月球運動 (Chinese curriculum term)`
- `月相 (Chinese curriculum term)`
- `日食 (Chinese curriculum term)`
- `月食 (Chinese curriculum term)`
- `太陽 (Chinese curriculum term)`
- `電磁波譜 (Chinese curriculum term)`
- `溫室效應 (Chinese curriculum term)`
- `氣候變遷 (Chinese curriculum term)`
- `海平面 (Chinese curriculum term)`
- `天然災害 (Chinese curriculum term)`
- `再生能源 (Chinese curriculum term)`
- `永續發展 (Chinese curriculum term)`

### 英文子句與句型 (English Clauses and Sentence Patterns)

- `simple_compound_complex`
- `relative_clause`
- `noun_clause`
- `adverb_clause`
- `conditionals`
- `reported_speech`
- `inversion`

### 英文文法 (English Grammar)

- `parts_of_speech`
- `subject_verb_agreement`
- `articles`
- `countable_uncountable`
- `pronouns`
- `comparatives_superlatives`
- `gerund_infinitive`
- `modals`
- `prepositions`

### 英文字首 (English Prefixes)

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

### 英文字根 (English Roots)

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

### 英文語意與通順 (English Semantics and Coherence)

- `context_clues`
- `logical_coherence`
- `reference_words`
- `collocation`
- `ambiguity`
- `concise_expression`

### 英文字尾 (English Suffixes)

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

### 英文時態與語態 (English Tenses and Voice)

- `present_simple`
- `present_progressive`
- `past_simple`
- `past_progressive`
- `present_perfect`
- `past_perfect`
- `future_forms`
- `passive_voice`
- `causative`

### 英文連接詞與閱讀 (English Connectors and Reading)

- `addition`
- `contrast`
- `cause_effect`
- `example_transition`
- `sequence_transition`
- `main_idea`
- `supporting_detail`
- `inference`
- `tone_purpose`

### 英文用法與常見錯誤 (English Usage and Common Errors)

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

### 英文作文 (English Writing)

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

### 臺灣歷史 (History of Taiwan)

- `史料與歷史研究 (Chinese curriculum term)`
- `臺灣史前時代 (Chinese curriculum term)`
- `南島語族與原住民族 (Chinese curriculum term)`
- `荷蘭與西班牙統治 (Chinese curriculum term)`
- `鄭氏政權 (Chinese curriculum term)`
- `清治時期 (Chinese curriculum term)`
- `清末改革 (Chinese curriculum term)`
- `馬關條約與割臺 (Chinese curriculum term)`
- `日本統治 (Chinese curriculum term)`
- `日本統治下的經濟與社會 (Chinese curriculum term)`
- `政治與社會運動 (Chinese curriculum term)`
- `皇民化運動 (Chinese curriculum term)`
- `戰後接收 (Chinese curriculum term)`
- `二二八事件 (Chinese curriculum term)`
- `戒嚴與白色恐怖 (Chinese curriculum term)`
- `戰後經濟發展 (Chinese curriculum term)`
- `民主化 (Chinese curriculum term)`
- `轉型正義 (Chinese curriculum term)`

### 中國歷史 (History of China)

- `中國古代文明 (Chinese curriculum term)`
- `夏商周 (Chinese curriculum term)`
- `春秋戰國 (Chinese curriculum term)`
- `諸子百家 (Chinese curriculum term)`
- `秦的統一 (Chinese curriculum term)`
- `漢帝國 (Chinese curriculum term)`
- `魏晉南北朝 (Chinese curriculum term)`
- `隋唐時期 (Chinese curriculum term)`
- `宋代 (Chinese curriculum term)`
- `元明清 (Chinese curriculum term)`
- `明清全球貿易 (Chinese curriculum term)`
- `鴉片戰爭 (Chinese curriculum term)`
- `自強運動與晚清改革 (Chinese curriculum term)`
- `甲午戰爭 (Chinese curriculum term)`
- `辛亥革命 (Chinese curriculum term)`
- `新文化運動與五四運動 (Chinese curriculum term)`
- `國民黨與共產黨 (Chinese curriculum term)`
- `抗日戰爭與國共內戰 (Chinese curriculum term)`
- `中華人民共和國與改革開放 (Chinese curriculum term)`

### 世界歷史 (World History)

- `古代河流文明 (Chinese curriculum term)`
- `古希臘文明 (Chinese curriculum term)`
- `古羅馬世界 (Chinese curriculum term)`
- `基督教與伊斯蘭文明 (Chinese curriculum term)`
- `中世紀歐洲 (Chinese curriculum term)`
- `十字軍東征與城市發展 (Chinese curriculum term)`
- `文藝復興與宗教改革 (Chinese curriculum term)`
- `科學革命與啟蒙運動 (Chinese curriculum term)`
- `地理大發現 (Chinese curriculum term)`
- `大西洋革命 (Chinese curriculum term)`
- `工業革命 (Chinese curriculum term)`
- `民族主義與帝國主義 (Chinese curriculum term)`
- `第一次世界大戰 (Chinese curriculum term)`
- `戰間期 (Chinese curriculum term)`
- `第二次世界大戰與猶太大屠殺 (Chinese curriculum term)`
- `聯合國與人權發展 (Chinese curriculum term)`
- `冷戰 (Chinese curriculum term)`
- `去殖民化 (Chinese curriculum term)`
- `全球化 (Chinese curriculum term)`

### 地理 (Geography)

- `地理探究 (Chinese curriculum term)`
- `地圖基礎 (Chinese curriculum term)`
- `經緯度與時區 (Chinese curriculum term)`
- `地理資訊系統與遙測 (Chinese curriculum term)`
- `板塊構造 (Chinese curriculum term)`
- `地形作用 (Chinese curriculum term)`
- `河流、海岸與喀斯特地形 (Chinese curriculum term)`
- `氣候要素與氣候因素 (Chinese curriculum term)`
- `季風與颱風 (Chinese curriculum term)`
- `水循環與海洋 (Chinese curriculum term)`
- `人口 (Chinese curriculum term)`
- `都市化與聚落 (Chinese curriculum term)`
- `產業活動 (Chinese curriculum term)`
- `全球化與國際貿易 (Chinese curriculum term)`
- `臺灣地理 (Chinese curriculum term)`
- `東亞、東南亞與南亞 (Chinese curriculum term)`
- `西亞與非洲 (Chinese curriculum term)`
- `歐洲、美洲與大洋洲 (Chinese curriculum term)`
- `天然災害、氣候變遷與永續發展 (Chinese curriculum term)`

### 公民與社會 (Civics and Society)

- `自我認同與社會化 (Chinese curriculum term)`
- `家庭與社會團體 (Chinese curriculum term)`
- `文化與社會規範 (Chinese curriculum term)`
- `社會階層與平等 (Chinese curriculum term)`
- `媒體與數位公民 (Chinese curriculum term)`
- `公民社會 (Social Studies / Civics)`
- `國家與政府 (Chinese curriculum term)`
- `民主政治與法治 (Chinese curriculum term)`
- `權力分立與憲法 (Chinese curriculum term)`
- `選舉、政黨與公民投票 (Chinese curriculum term)`
- `人權 (Chinese curriculum term)`
- `言論自由與隱私權 (Chinese curriculum term)`
- `法律制度 (Chinese curriculum term)`
- `民法、刑法與行政法 (Chinese curriculum term)`
- `消費者與勞動權益 (Chinese curriculum term)`
- `稀少性、選擇與機會成本 (Chinese curriculum term)`
- `供給與需求 (Chinese curriculum term)`
- `市場與政府 (Chinese curriculum term)`
- `貨幣與總體經濟 (Chinese curriculum term)`
- `國際貿易與全球治理 (Chinese curriculum term)`
- `社會福利、公共政策與公民參與 (Chinese curriculum term)`
- `社會探究 (Chinese curriculum term)`

### 國文文學常識 (Chinese Literature Knowledge)

- `文學體裁 (Chinese curriculum term)`
- `散文 (Chinese curriculum term)`
- `古文 (Chinese curriculum term)`
- `駢文 (Chinese curriculum term)`
- `詩 (Chinese curriculum term)`
- `古體詩 (Chinese curriculum term)`
- `近體詩 (Chinese curriculum term)`
- `絕句 (Chinese curriculum term)`
- `律詩 (Chinese curriculum term)`
- `樂府 (Chinese curriculum term)`
- `《詩經》 (Chinese curriculum term)`
- `楚辭 (Chinese curriculum term)`
- `賦 (Chinese curriculum term)`
- `詞 (Chinese curriculum term)`
- `曲 (Chinese curriculum term)`
- `現代詩 (Chinese curriculum term)`
- `小說 (Chinese curriculum term)`
- `古典小說 (Chinese curriculum term)`
- `志怪小說 (Chinese curriculum term)`
- `志人小說 (Chinese curriculum term)`
- `唐傳奇 (Chinese curriculum term)`
- `章回小說 (Chinese curriculum term)`
- `戲劇 (Chinese curriculum term)`
- `傳統戲曲 (Chinese curriculum term)`
- `文學運動 (Chinese curriculum term)`
- `唐宋八大家 (Chinese curriculum term)`
- `建安七子 (Chinese curriculum term)`
- `竹林七賢 (Chinese curriculum term)`
- `四書 (Chinese curriculum term)`
- `五經 (Chinese curriculum term)`
- `歷史散文 (Chinese curriculum term)`
- `編年體 (Chinese curriculum term)`
- `紀傳體 (Chinese curriculum term)`
- `國別體 (Chinese curriculum term)`
- `臺灣文學 (Chinese curriculum term)`
- `鄉土文學 (Chinese curriculum term)`
- `自然書寫 (Chinese curriculum term)`
- `旅行文學 (Chinese curriculum term)`
- `口傳文學 (Chinese curriculum term)`

### 國文語文常識 (Chinese Language Knowledge)

- `六書 (Chinese curriculum term)`
- `象形 (Chinese curriculum term)`
- `指事 (Chinese curriculum term)`
- `會意 (Chinese curriculum term)`
- `形聲 (Chinese curriculum term)`
- `轉注 (Chinese curriculum term)`
- `假借 (Chinese curriculum term)`
- `部首 (Chinese curriculum term)`
- `字形 (Chinese curriculum term)`
- `同音字 (Chinese curriculum term)`
- `形近字 (Chinese curriculum term)`
- `破音字 (Chinese curriculum term)`
- `正體字 (Chinese curriculum term)`
- `詞 (Chinese curriculum term)`
- `複合詞 (Chinese curriculum term)`
- `詞類 (Chinese curriculum term)`
- `名詞 (Chinese curriculum term)`
- `動詞 (Chinese curriculum term)`
- `形容詞 (Chinese curriculum term)`
- `副詞 (Chinese curriculum term)`
- `代詞 (Chinese curriculum term)`
- `介詞 (Chinese curriculum term)`
- `連詞 (Chinese curriculum term)`
- `助詞 (Chinese curriculum term)`
- `嘆詞 (Chinese curriculum term)`
- `句子成分 (Chinese curriculum term)`
- `主語 (Chinese curriculum term)`
- `賓語 (Chinese curriculum term)`
- `定語 (Chinese curriculum term)`
- `基本句型 (Chinese curriculum term)`
- `複句 (Chinese curriculum term)`
- `標點符號 (Chinese curriculum term)`
- `逗號 (Chinese curriculum term)`
- `頓號 (Chinese curriculum term)`
- `分號 (Chinese curriculum term)`
- `冒號 (Chinese curriculum term)`
- `引號 (Chinese curriculum term)`
- `破折號 (Chinese curriculum term)`
- `刪節號 (Chinese curriculum term)`
- `書名號 (Chinese curriculum term)`
- `成語 (Chinese curriculum term)`
- `諺語 (Chinese curriculum term)`
- `俗語 (Chinese curriculum term)`
- `歇後語 (Chinese curriculum term)`
- `對聯 (Chinese curriculum term)`
- `書信 (Chinese curriculum term)`
- `啟事 (Chinese curriculum term)`
- `柬帖 (Chinese curriculum term)`
- `稱謂 (Chinese curriculum term)`
- `年齡代稱 (Chinese curriculum term)`
- `季節與月份代稱 (Chinese curriculum term)`
- `天干地支 (Chinese curriculum term)`

### 國文修辭 (Chinese Rhetoric)

- `修辭 (Chinese curriculum term)`
- `明喻 (Chinese curriculum term)`
- `暗喻 (Chinese curriculum term)`
- `略喻 (Chinese curriculum term)`
- `借代 (Chinese curriculum term)`
- `擬人 (Chinese curriculum term)`
- `擬物 (Chinese curriculum term)`
- `誇飾 (Chinese curriculum term)`
- `排比 (Chinese curriculum term)`
- `對偶 (Chinese curriculum term)`
- `映襯 (Chinese curriculum term)`
- `正襯 (Chinese curriculum term)`
- `反襯 (Chinese curriculum term)`
- `設問 (Chinese curriculum term)`
- `反問 (Chinese curriculum term)`
- `反復 (Chinese curriculum term)`
- `頂真 (Chinese curriculum term)`
- `回文 (Chinese curriculum term)`
- `層遞 (Chinese curriculum term)`
- `遞升 (Chinese curriculum term)`
- `遞降 (Chinese curriculum term)`
- `引用 (Chinese curriculum term)`
- `用典 (Chinese curriculum term)`
- `象徵 (Chinese curriculum term)`
- `雙關 (Chinese curriculum term)`
- `婉曲 (Chinese curriculum term)`
- `倒反 (Chinese curriculum term)`
- `移覺 (Chinese curriculum term)`
- `摹寫 (Chinese curriculum term)`
- `動態描寫 (Chinese curriculum term)`
- `靜態描寫 (Chinese curriculum term)`
- `伏筆 (Chinese curriculum term)`
- `懸念 (Chinese curriculum term)`
- `倒敘 (Chinese curriculum term)`
- `插敘 (Chinese curriculum term)`
- `直抒胸臆 (Chinese curriculum term)`
- `間接抒情 (Chinese curriculum term)`
- `借景抒情 (Chinese curriculum term)`
- `託物言志 (Chinese curriculum term)`
- `情景交融 (Chinese curriculum term)`
- `首尾呼應 (Chinese curriculum term)`
- `比較 (Comparison)`
- `分類 (Classification)`
- `下定義 (Chinese curriculum term)`
- `舉例 (Chinese curriculum term)`
- `列數據 (Chinese curriculum term)`

### 國文文言文 (Classical Chinese)

- `文言文 (Chinese curriculum term)`
- `實詞 (Chinese curriculum term)`
- `虛詞 (Chinese curriculum term)`
- `一詞多義 (Chinese curriculum term)`
- `古今異義 (Chinese curriculum term)`
- `通假字 (Chinese curriculum term)`
- `詞類活用 (Chinese curriculum term)`
- `名詞作動詞 (Chinese curriculum term)`
- `名詞作狀語 (Chinese curriculum term)`
- `使動用法 (Chinese curriculum term)`
- `意動用法 (Chinese curriculum term)`
- `判斷句 (Chinese curriculum term)`
- `被動句 (Chinese curriculum term)`
- `倒裝句 (Chinese curriculum term)`
- `省略句 (Chinese curriculum term)`
- `固定句式 (Chinese curriculum term)`
- `之 (Chinese curriculum term)`
- `其 (Chinese curriculum term)`
- `而 (Chinese curriculum term)`
- `以 (Chinese curriculum term)`
- `於 (Chinese curriculum term)`
- `乃 (Chinese curriculum term)`
- `則 (Chinese curriculum term)`
- `者 (Chinese curriculum term)`
- `焉 (Chinese curriculum term)`
- `何 (Chinese curriculum term)`
- `乎 (Chinese curriculum term)`
- `信達雅 (Chinese curriculum term)`
- `直譯 (Chinese curriculum term)`
- `意譯 (Chinese curriculum term)`
- `文言翻譯 (Chinese curriculum term)`
- `文言閱讀 (Chinese curriculum term)`
- `文言議論 (Chinese curriculum term)`
- `文言敘事 (Chinese curriculum term)`
- `文言抒情 (Chinese curriculum term)`
- `古典詩歌意象 (Chinese curriculum term)`
- `古典詩歌閱讀 (Chinese curriculum term)`
- `起承轉合 (Chinese curriculum term)`
- `文化語境 (Chinese curriculum term)`
- `官職名 (Chinese curriculum term)`
- `名、字、號 (Chinese curriculum term)`

### 國文作文 (Chinese Composition)

- `寫作流程 (Chinese curriculum term)`
- `審題 (Chinese curriculum term)`
- `立意 (Chinese curriculum term)`
- `選材 (Chinese curriculum term)`
- `大綱 (Chinese curriculum term)`
- `分段 (Chinese curriculum term)`
- `主題句 (Chinese curriculum term)`
- `連貫 (Chinese curriculum term)`
- `過渡 (Chinese curriculum term)`
- `開頭 (Chinese curriculum term)`
- `開門見山 (Chinese curriculum term)`
- `情境開頭 (Chinese curriculum term)`
- `設問開頭 (Chinese curriculum term)`
- `引用開頭 (Chinese curriculum term)`
- `結尾 (Chinese curriculum term)`
- `總結式結尾 (Chinese curriculum term)`
- `呼應式結尾 (Chinese curriculum term)`
- `餘韻式結尾 (Chinese curriculum term)`
- `記敘文 (Chinese curriculum term)`
- `順敘 (Chinese curriculum term)`
- `人物描寫 (Chinese curriculum term)`
- `景物描寫 (Chinese curriculum term)`
- `事件描寫 (Chinese curriculum term)`
- `細節描寫 (Chinese curriculum term)`
- `抒情文 (Chinese curriculum term)`
- `說明文 (Chinese curriculum term)`
- `下定義 (Chinese curriculum term)`
- `議論文 (Chinese curriculum term)`
- `論點 (Chinese curriculum term)`
- `論據 (Chinese curriculum term)`
- `論證 (Chinese curriculum term)`
- `舉例論證 (Chinese curriculum term)`
- `對比論證 (Chinese curriculum term)`
- `因果論證 (Chinese curriculum term)`
- `引用論證 (Chinese curriculum term)`
- `反方觀點 (Chinese curriculum term)`
- `比較型作文 (Chinese curriculum term)`
- `問題解決型作文 (Chinese curriculum term)`
- `感想文 (Chinese curriculum term)`
- `閱讀心得 (Chinese curriculum term)`
- `圖表或圖像寫作 (Chinese curriculum term)`
- `材料作文 (Chinese curriculum term)`
- `命題作文 (Chinese curriculum term)`
- `自訂題目作文 (Chinese curriculum term)`
- `描寫 (Chinese curriculum term)`
- `感官描寫 (Chinese curriculum term)`
- `以描寫代替直說 (Chinese curriculum term)`
- `對話 (Chinese curriculum term)`
- `文章語調 (Chinese curriculum term)`
- `遣詞用字 (Chinese curriculum term)`
- `句式變化 (Chinese curriculum term)`
- `譬喻、排比、映襯、設問 (Chinese curriculum term)`
- `修改 (Chinese curriculum term)`
- `校對 (Chinese curriculum term)`
- `離題 (Chinese curriculum term)`
- `作文時間分配 (Chinese curriculum term)`
- `卷面與格式 (Chinese curriculum term)`

### 國文閱讀理解 (Chinese Reading Comprehension)

- `閱讀理解 (Chinese curriculum term)`
- `預覽 (Chinese curriculum term)`
- `預測 (Chinese curriculum term)`
- `提問 (Chinese curriculum term)`
- `理解監控 (Chinese curriculum term)`
- `重讀 (Chinese curriculum term)`
- `閱讀標記 (Chinese curriculum term)`
- `關鍵詞 (Chinese curriculum term)`
- `主旨 (Chinese curriculum term)`
- `主題 (Chinese curriculum term)`
- `段落大意 (Chinese curriculum term)`
- `主題句 (Chinese curriculum term)`
- `支持細節 (Chinese curriculum term)`
- `摘要 (Chinese curriculum term)`
- `改寫 (Chinese curriculum term)`
- `字面義 (Chinese curriculum term)`
- `語境義 (Chinese curriculum term)`
- `上下文線索 (Chinese curriculum term)`
- `指涉 (Chinese curriculum term)`
- `銜接 (Chinese curriculum term)`
- `連貫 (Chinese curriculum term)`
- `順序關係 (Chinese curriculum term)`
- `時間順序 (Chinese curriculum term)`
- `空間順序 (Chinese curriculum term)`
- `因果關係 (Chinese curriculum term)`
- `比較與對照 (Chinese curriculum term)`
- `問題解決結構 (Chinese curriculum term)`
- `分類結構 (Structure / Classification)`
- `總分結構 (Chinese curriculum term)`
- `轉承詞 (Chinese curriculum term)`
- `寫作目的 (Chinese curriculum term)`
- `作者觀點 (Chinese curriculum term)`
- `作者態度 (Chinese curriculum term)`
- `語氣 (Chinese curriculum term)`
- `客觀敘述 (Chinese curriculum term)`
- `事實 (Chinese curriculum term)`
- `明示訊息 (Chinese curriculum term)`
- `隱含訊息 (Chinese curriculum term)`
- `推論 (Chinese curriculum term)`
- `證據推論 (Chinese curriculum term)`
- `人物推論 (Chinese curriculum term)`
- `人物動機 (Chinese curriculum term)`
- `人物轉變 (Chinese curriculum term)`
- `衝突 (Chinese curriculum term)`
- `情節 (Chinese curriculum term)`
- `環境 (Chinese curriculum term)`
- `敘述者 (Chinese curriculum term)`
- `第一人稱敘事 (Chinese curriculum term)`
- `第三人稱敘事 (Chinese curriculum term)`
- `不可靠敘述者 (Chinese curriculum term)`
- `伏筆 (Chinese curriculum term)`
- `懸念 (Chinese curriculum term)`
- `倒敘 (Chinese curriculum term)`
- `插敘 (Chinese curriculum term)`
- `象徵 (Chinese curriculum term)`
- `意象 (Chinese curriculum term)`
- `氛圍 (Chinese curriculum term)`
- `反諷 (Chinese curriculum term)`
- `幽默 (Chinese curriculum term)`
- `諷刺 (Chinese curriculum term)`
- `記敘文閱讀 (Chinese curriculum term)`
- `抒情文閱讀 (Chinese curriculum term)`
- `說明文閱讀 (Chinese curriculum term)`
- `議論文閱讀 (Chinese curriculum term)`
- `論點 (Chinese curriculum term)`
- `論據 (Chinese curriculum term)`
- `論證 (Chinese curriculum term)`
- `反方觀點 (Chinese curriculum term)`
- `邏輯謬誤 (Chinese curriculum term)`
- `以偏概全 (Chinese curriculum term)`
- `錯誤因果 (Chinese curriculum term)`
- `非黑即白 (Chinese curriculum term)`
- `不當訴諸權威 (Chinese curriculum term)`
- `人身攻擊 (Chinese curriculum term)`
- `數據閱讀 (Chinese curriculum term)`
- `圖表閱讀 (Chinese curriculum term)`
- `表格閱讀 (Chinese curriculum term)`
- `資訊圖表 (Chinese curriculum term)`
- `圖文關係 (Chinese curriculum term)`
- `多文本閱讀 (Chinese curriculum term)`
- `跨文本比較 (Chinese curriculum term)`
- `來源評估 (Chinese curriculum term)`
- `偏見或偏向 (Chinese curriculum term)`
- `錯誤資訊 (Chinese curriculum term)`
- `事實查核 (Chinese curriculum term)`
- `廣告閱讀 (Chinese curriculum term)`
- `新聞閱讀 (Chinese curriculum term)`
- `文言文閱讀 (Chinese curriculum term)`
- `判斷文言字義 (Chinese curriculum term)`
- `判斷文言句式 (Chinese curriculum term)`
- `翻譯文言句 (Chinese curriculum term)`
- `判斷古文主旨 (Chinese curriculum term)`
- `古典詩歌閱讀 (Chinese curriculum term)`
- `詩中說話者 (Chinese curriculum term)`
- `分析詩歌意象 (Chinese curriculum term)`
- `判斷詩歌情感 (Chinese curriculum term)`
- `分析詩歌結構 (Chinese curriculum term)`
- `現代詩閱讀 (Chinese curriculum term)`
- `修辭效果 (Chinese curriculum term)`
- `用詞效果 (Chinese curriculum term)`
- `句式效果 (Chinese curriculum term)`
- `標題作用 (Chinese curriculum term)`
- `開頭作用 (Chinese curriculum term)`
- `結尾作用 (Chinese curriculum term)`
- `段落作用 (Chinese curriculum term)`
- `過渡段 (Chinese curriculum term)`
- `細節作用 (Chinese curriculum term)`
- `引用作用 (Chinese curriculum term)`
- `舉例作用 (Chinese curriculum term)`
- `數據作用 (Chinese curriculum term)`
- `對比作用 (Chinese curriculum term)`
- `描寫作用 (Chinese curriculum term)`
- `題幹 (Chinese curriculum term)`
- `檢索訊息題 (Chinese curriculum term)`
- `統整訊息題 (Chinese curriculum term)`
- `解釋題 (Chinese curriculum term)`
- `推論題 (Chinese curriculum term)`
- `評鑑題 (Chinese curriculum term)`
- `比較題 (Chinese curriculum term)`
- `開放式閱讀題 (Chinese curriculum term)`
- `選擇題策略 (Chinese curriculum term)`
- `干擾選項 (Chinese curriculum term)`
- `簡答題策略 (Chinese curriculum term)`
- `文本證據 (Chinese curriculum term)`
- `答案完整性 (Chinese curriculum term)`
- `閱讀速度 (Chinese curriculum term)`
- `閱讀時間分配 (Chinese curriculum term)`
- `閱讀題檢查 (Chinese curriculum term)`
- `國中會考閱讀 (Chinese curriculum term)`
- `高中國文閱讀 (Chinese curriculum term)`
- `素養導向閱讀 (Chinese curriculum term)`
- `跨領域閱讀 (Chinese curriculum term)`
- `長文閱讀 (Chinese curriculum term)`
- `難文閱讀 (Chinese curriculum term)`
- `閱讀筆記 (Chinese curriculum term)`
- `概念圖 (Chinese curriculum term)`
- `時間軸 (Chinese curriculum term)`
- `比較表 (Chinese curriculum term)`
- `問題與答案關係 (Chinese curriculum term)`
- `閱讀反思 (Chinese curriculum term)`
- `閱讀遷移 (Chinese curriculum term)`

### 國文作者 (Chinese Authors)

- `孔子 (Chinese curriculum term)`
- `孟子 (Chinese curriculum term)`
- `荀子 (Chinese curriculum term)`
- `老子 (Chinese curriculum term)`
- `莊子 (Chinese curriculum term)`
- `墨子 (Chinese curriculum term)`
- `韓非 (Chinese curriculum term)`
- `孫武 (Chinese curriculum term)`
- `屈原 (Chinese curriculum term)`
- `司馬遷 (Chinese curriculum term)`
- `班固 (Chinese curriculum term)`
- `賈誼 (Chinese curriculum term)`
- `曹操 (Chinese curriculum term)`
- `曹植 (Chinese curriculum term)`
- `陶淵明 (Chinese curriculum term)`
- `劉義慶 (Chinese curriculum term)`
- `酈道元 (Chinese curriculum term)`
- `王羲之 (Chinese curriculum term)`
- `李白 (Chinese curriculum term)`
- `杜甫 (Chinese curriculum term)`
- `王維 (Chinese curriculum term)`
- `孟浩然 (Chinese curriculum term)`
- `白居易 (Chinese curriculum term)`
- `韓愈 (Chinese curriculum term)`
- `柳宗元 (Chinese curriculum term)`
- `杜牧 (Chinese curriculum term)`
- `李商隱 (Chinese curriculum term)`
- `范仲淹 (Chinese curriculum term)`
- `歐陽脩 (Chinese curriculum term)`
- `王安石 (Chinese curriculum term)`
- `蘇洵 (Chinese curriculum term)`
- `蘇軾 (Chinese curriculum term)`
- `蘇轍 (Chinese curriculum term)`
- `曾鞏 (Chinese curriculum term)`
- `周敦頤 (Chinese curriculum term)`
- `司馬光 (Chinese curriculum term)`
- `李清照 (Chinese curriculum term)`
- `辛棄疾 (Chinese curriculum term)`
- `陸游 (Chinese curriculum term)`
- `文天祥 (Chinese curriculum term)`
- `朱熹 (Chinese curriculum term)`
- `關漢卿 (Chinese curriculum term)`
- `馬致遠 (Chinese curriculum term)`
- `施耐庵 (Chinese curriculum term)`
- `羅貫中 (Chinese curriculum term)`
- `吳承恩 (Chinese curriculum term)`
- `馮夢龍 (Chinese curriculum term)`
- `歸有光 (Chinese curriculum term)`
- `袁宏道 (Chinese curriculum term)`
- `張岱 (Chinese curriculum term)`
- `蒲松齡 (Chinese curriculum term)`
- `曹雪芹 (Chinese curriculum term)`
- `劉鶚 (Chinese curriculum term)`
- `梁啟超 (Chinese curriculum term)`
- `孫文 (Chinese curriculum term)`
- `魯迅 (Chinese curriculum term)`
- `胡適 (Chinese curriculum term)`
- `徐志摩 (Chinese curriculum term)`
- `朱自清 (Chinese curriculum term)`
- `冰心 (Chinese curriculum term)`
- `老舍 (Chinese curriculum term)`
- `沈從文 (Chinese curriculum term)`
- `巴金 (Chinese curriculum term)`
- `錢鍾書 (Chinese curriculum term)`
- `張愛玲 (Chinese curriculum term)`
- `林語堂 (Chinese curriculum term)`
- `豐子愷 (Chinese curriculum term)`
- `夏丏尊 (Chinese curriculum term)`
- `林海音 (Chinese curriculum term)`
- `琦君 (Chinese curriculum term)`
- `余光中 (Chinese curriculum term)`
- `楊牧 (Chinese curriculum term)`
- `張曉風 (Chinese curriculum term)`
- `簡媜 (Chinese curriculum term)`
- `龍應台 (Chinese curriculum term)`
- `廖鴻基 (Chinese curriculum term)`
- `劉克襄 (Chinese curriculum term)`
- `吳明益 (Chinese curriculum term)`
- `陳列 (Chinese curriculum term)`
- `陳芳明 (Chinese curriculum term)`
- `鄭愁予 (Chinese curriculum term)`
- `洛夫 (Chinese curriculum term)`
- `瘂弦 (Chinese curriculum term)`
- `周夢蝶 (Chinese curriculum term)`
- `白先勇 (Chinese curriculum term)`
- `黃春明 (Chinese curriculum term)`
- `王禎和 (Chinese curriculum term)`
- `鍾理和 (Chinese curriculum term)`
- `鍾肇政 (Chinese curriculum term)`
- `賴和 (Chinese curriculum term)`
- `楊逵 (Chinese curriculum term)`
- `呂赫若 (Chinese curriculum term)`
- `吳濁流 (Chinese curriculum term)`
- `李昂 (Chinese curriculum term)`
- `袁瓊瓊 (Chinese curriculum term)`
- `三毛 (Chinese curriculum term)`
- `杏林子 (Chinese curriculum term)`
- `林良 (Chinese curriculum term)`
- `林文月 (Chinese curriculum term)`
- `齊邦媛 (Chinese curriculum term)`
- `蔣勳 (Chinese curriculum term)`
- `徐仁修 (Chinese curriculum term)`
- `瓦歷斯·諾幹 (Chinese curriculum term)`
- `夏曼·藍波安 (Chinese curriculum term)`
- `巴代 (Chinese curriculum term)`
- `利格拉樂·阿烏 (Chinese curriculum term)`
- `陳耀昌 (Chinese curriculum term)`

### 國文課文整理 (Chinese Text Summaries)

- `《論語》選 (Chinese curriculum term)`
- `《孟子》選 (Chinese curriculum term)`
- `《莊子》選 (Chinese curriculum term)`
- `《老子》選 (Chinese curriculum term)`
- `公輸 (Chinese curriculum term)`
- `曹劌論戰 (Chinese curriculum term)`
- `鄒忌諷齊王納諫 (Chinese curriculum term)`
- `唐雎不辱使命 (Chinese curriculum term)`
- `馮諼客孟嘗君 (Chinese curriculum term)`
- `鴻門宴 (Chinese curriculum term)`
- `廉頗藺相如列傳 (Chinese curriculum term)`
- `屈原列傳 (Chinese curriculum term)`
- `過秦論 (Chinese curriculum term)`
- `陳情表 (Chinese curriculum term)`
- `蘭亭集序 (Chinese curriculum term)`
- `桃花源記 (Chinese curriculum term)`
- `歸去來辭 (Chinese curriculum term)`
- `飲酒 (Chinese curriculum term)`
- `《世說新語》選 (Chinese curriculum term)`
- `三峽 (Chinese curriculum term)`
- `木蘭詩 (Chinese curriculum term)`
- `出師表 (Chinese curriculum term)`
- `敕勒歌 (Chinese curriculum term)`
- `春江花月夜 (Chinese curriculum term)`
- `將進酒 (Chinese curriculum term)`
- `蜀道難 (Chinese curriculum term)`
- `行路難 (Chinese curriculum term)`
- `春望 (Chinese curriculum term)`
- `登高 (Chinese curriculum term)`
- `茅屋為秋風所破歌 (Chinese curriculum term)`
- `石壕吏 (Chinese curriculum term)`
- `山居秋暝 (Chinese curriculum term)`
- `送元二使安西 (Chinese curriculum term)`
- `過故人莊 (Chinese curriculum term)`
- `琵琶行 (Chinese curriculum term)`
- `賣炭翁 (Chinese curriculum term)`
- `師說 (Chinese curriculum term)`
- `馬說 (Chinese curriculum term)`
- `祭十二郎文 (Chinese curriculum term)`
- `小石潭記 (Chinese curriculum term)`
- `始得西山宴遊記 (Chinese curriculum term)`
- `捕蛇者說 (Chinese curriculum term)`
- `阿房宮賦 (Chinese curriculum term)`
- `錦瑟 (Chinese curriculum term)`
- `岳陽樓記 (Chinese curriculum term)`
- `醉翁亭記 (Chinese curriculum term)`
- `秋聲賦 (Chinese curriculum term)`
- `六國論 (Chinese curriculum term)`
- `赤壁賦 (Chinese curriculum term)`
- `後赤壁賦 (Chinese curriculum term)`
- `念奴嬌·赤壁懷古 (Chinese curriculum term)`
- `水調歌頭 (Chinese curriculum term)`
- `遊褒禪山記 (Chinese curriculum term)`
- `答司馬諫議書 (Chinese curriculum term)`
- `愛蓮說 (Chinese curriculum term)`
- `《資治通鑑》選 (Chinese curriculum term)`
- `聲聲慢 (Chinese curriculum term)`
- `破陣子·為陳同甫賦壯詞以寄之 (Chinese curriculum term)`
- `永遇樂·京口北固亭懷古 (Chinese curriculum term)`
- `過零丁洋 (Chinese curriculum term)`
- `天淨沙·秋思 (Chinese curriculum term)`
- `《竇娥冤》選 (Chinese curriculum term)`
- `項脊軒志 (Chinese curriculum term)`
- `晚遊六橋待月記 (Chinese curriculum term)`
- `湖心亭看雪 (Chinese curriculum term)`
- `《聊齋志異》選 (Chinese curriculum term)`
- `《紅樓夢》選 (Chinese curriculum term)`
- `《老殘遊記》選 (Chinese curriculum term)`
- `少年中國說 (Chinese curriculum term)`
- `最苦與最樂 (Chinese curriculum term)`
- `差不多先生傳 (Chinese curriculum term)`
- `孔乙己 (Chinese curriculum term)`
- `故鄉 (Chinese curriculum term)`
- `《阿Q正傳》選 (Chinese curriculum term)`
- `背影 (Chinese curriculum term)`
- `荷塘月色 (Chinese curriculum term)`
- `匆匆 (Chinese curriculum term)`
- `再別康橋 (Chinese curriculum term)`
- `《城南舊事》選 (Chinese curriculum term)`
- `桂花雨 (Chinese curriculum term)`
- `鄉愁 (Chinese curriculum term)`
- `聽聽那冷雨 (Chinese curriculum term)`
- `我的四個假想敵 (Chinese curriculum term)`
- `夏之絕句 (Chinese curriculum term)`
- `行道樹 (Chinese curriculum term)`
- `目送 (Chinese curriculum term)`
- `《討海人》選 (Chinese curriculum term)`
- `《海浪的記憶》選 (Chinese curriculum term)`
- `一桿秤仔 (Chinese curriculum term)`
- `送報伕 (Chinese curriculum term)`
- `兒子的大玩偶 (Chinese curriculum term)`
- `《魯冰花》選 (Chinese curriculum term)`
- `《臺北人》選 (Chinese curriculum term)`
- `《亞細亞的孤兒》選 (Chinese curriculum term)`
- `《撒哈拉的故事》選 (Chinese curriculum term)`
- `《荒野有歌》選 (Chinese curriculum term)`
- `《複眼人》選 (Chinese curriculum term)`

### 國文成語與國學 (Chinese Idioms and Traditional Studies)

- `安步當車 (Chinese curriculum term)`
- `安土重遷 (Chinese curriculum term)`
- `揠苗助長 (Chinese curriculum term)`
- `白駒過隙 (Chinese curriculum term)`
- `背水一戰 (Chinese curriculum term)`
- `閉門造車 (Chinese curriculum term)`
- `別出心裁 (Chinese curriculum term)`
- `不堪設想 (Chinese curriculum term)`
- `不落窠臼 (Chinese curriculum term)`
- `不一而足 (Chinese curriculum term)`
- `差強人意 (Chinese curriculum term)`
- `車水馬龍 (Chinese curriculum term)`
- `成竹在胸 (Chinese curriculum term)`
- `出類拔萃 (Chinese curriculum term)`
- `川流不息 (Chinese curriculum term)`
- `春風化雨 (Chinese curriculum term)`
- `大快朵頤 (Chinese curriculum term)`
- `當仁不讓 (Chinese curriculum term)`
- `東施效顰 (Chinese curriculum term)`
- `斷章取義 (Chinese curriculum term)`
- `耳濡目染 (Chinese curriculum term)`
- `方興未艾 (Chinese curriculum term)`
- `粉墨登場 (Chinese curriculum term)`
- `紛至沓來 (Chinese curriculum term)`
- `付與頑梗 (Chinese curriculum term)`
- `高山仰止 (Chinese curriculum term)`
- `格格不入 (Chinese curriculum term)`
- `功虧一簣 (Chinese curriculum term)`
- `故步自封 (Chinese curriculum term)`
- `光風霽月 (Chinese curriculum term)`
- `含英咀華 (Chinese curriculum term)`
- `河東獅吼 (Chinese curriculum term)`
- `囫圇吞棗 (Chinese curriculum term)`
- `渙然冰釋 (Chinese curriculum term)`
- `誨人不倦 (Chinese curriculum term)`
- `急於功名 (Chinese curriculum term)`
- `見賢思齊 (Chinese curriculum term)`
- `狡兔三窟 (Chinese curriculum term)`
- `津津有味 (Chinese curriculum term)`
- `涇渭分明 (Chinese curriculum term)`
- `舉一反三 (Chinese curriculum term)`
- `刻舟求劍 (Chinese curriculum term)`
- `空谷足音 (Chinese curriculum term)`
- `膾炙人口 (Chinese curriculum term)`
- `老馬識途 (Chinese curriculum term)`
- `李代桃僵 (Chinese curriculum term)`
- `量身訂做 (Chinese curriculum term)`
- `臨淵羨魚 (Chinese curriculum term)`
- `洛陽紙貴 (Chinese curriculum term)`
- `買櫝還珠 (Chinese curriculum term)`
- `茅塞頓開 (Chinese curriculum term)`
- `美輪美奐 (Chinese curriculum term)`
- `門可羅雀 (Chinese curriculum term)`
- `妙手偶得 (Chinese curriculum term)`
- `明日黃花 (Chinese curriculum term)`
- `目不交睫 (Chinese curriculum term)`
- `目無全牛 (Chinese curriculum term)`
- `南轅北轍 (Chinese curriculum term)`
- `嘔心瀝血 (Chinese curriculum term)`
- `蓬蓽生輝 (Chinese curriculum term)`
- `皮裡陽秋 (Chinese curriculum term)`
- `破釜沉舟 (Chinese curriculum term)`
- `杞人憂天 (Chinese curriculum term)`
- `前車之鑑 (Chinese curriculum term)`
- `晴天霹靂 (Chinese curriculum term)`
- `曲突徙薪 (Chinese curriculum term)`
- `如火如荼 (Chinese curriculum term)`
- `如數家珍 (Chinese curriculum term)`
- `三人成虎 (Chinese curriculum term)`
- `上行下效 (Chinese curriculum term)`
- `聲情並茂 (Chinese curriculum term)`
- `事半功倍 (Chinese curriculum term)`
- `守株待兔 (Chinese curriculum term)`
- `首當其衝 (Chinese curriculum term)`
- `殊途同歸 (Chinese curriculum term)`
- `水到渠成 (Chinese curriculum term)`
- `司空見慣 (Chinese curriculum term)`
- `曇花一現 (Chinese curriculum term)`
- `醍醐灌頂 (Chinese curriculum term)`
- `天花亂墜 (Chinese curriculum term)`
- `推心置腹 (Chinese curriculum term)`
- `望塵莫及 (Chinese curriculum term)`
- `未雨綢繆 (Chinese curriculum term)`
- `溫故知新 (Chinese curriculum term)`
- `毋庸置疑 (Chinese curriculum term)`
- `息息相關 (Chinese curriculum term)`
- `相形見絀 (Chinese curriculum term)`
- `小題大作 (Chinese curriculum term)`
- `信手拈來 (Chinese curriculum term)`
- `胸有成竹 (Chinese curriculum term)`
- `學富五車 (Chinese curriculum term)`
- `言過其實 (Chinese curriculum term)`
- `義正詞嚴 (Chinese curriculum term)`
- `以暴易暴 (Chinese curriculum term)`
- `一籌莫展 (Chinese curriculum term)`
- `雨過天晴 (Chinese curriculum term)`
- `一鳴驚人 (Chinese curriculum term)`
- `一日千里 (Chinese curriculum term)`
- `飲鴆止渴 (Chinese curriculum term)`
- `迎刃而解 (Chinese curriculum term)`
- `愚公移山 (Chinese curriculum term)`
- `緣木求魚 (Chinese curriculum term)`
- `擇善固執 (Chinese curriculum term)`
- `振聾發聵 (Chinese curriculum term)`
- `知微見著 (Chinese curriculum term)`
- `中流砥柱 (Chinese curriculum term)`
- `逐末忘本 (Chinese curriculum term)`
- `自相矛盾 (Chinese curriculum term)`
- `四書 (Chinese curriculum term)`
- `五經 (Chinese curriculum term)`
- `十三經 (Chinese curriculum term)`
- `前四史 (Chinese curriculum term)`
- `二十四史 (Chinese curriculum term)`
- `史書體例 (Chinese curriculum term)`
- `諸子百家 (Chinese curriculum term)`
- `儒家 (Chinese curriculum term)`
- `道家 (Chinese curriculum term)`
- `墨家 (Chinese curriculum term)`
- `法家 (Chinese curriculum term)`
- `唐宋八大家 (Chinese curriculum term)`
- `建安七子 (Chinese curriculum term)`
- `竹林七賢 (Chinese curriculum term)`
- `元曲四大家 (Chinese curriculum term)`
- `四大名著 (Chinese curriculum term)`
- `三言二拍 (Chinese curriculum term)`
- `古典文體 (Chinese curriculum term)`
- `記 (Chinese curriculum term)`
- `說 (Chinese curriculum term)`
- `序 (Chinese curriculum term)`
- `表 (Chinese curriculum term)`
- `書 (Chinese curriculum term)`
- `銘 (Chinese curriculum term)`
- `祭文 (Chinese curriculum term)`
- `對聯規則 (Chinese curriculum term)`
- `橫批 (Chinese curriculum term)`
- `敬辭 (Chinese curriculum term)`
- `謙辭 (Chinese curriculum term)`
- `家大舍小令外人 (Chinese curriculum term)`
- `年齡代稱 (Chinese curriculum term)`
- `婚姻代稱 (Chinese curriculum term)`
- `死亡代稱 (Chinese curriculum term)`
- `天干 (Chinese curriculum term)`
- `地支 (Chinese curriculum term)`
- `干支紀年 (Chinese curriculum term)`
- `十二時辰 (Chinese curriculum term)`
- `孟仲季 (Chinese curriculum term)`
- `農曆月份別稱 (Chinese curriculum term)`
- `二十四節氣 (Chinese curriculum term)`
- `春節 (Chinese curriculum term)`
- `元宵節 (Chinese curriculum term)`
- `清明節 (Chinese curriculum term)`
- `端午節 (Chinese curriculum term)`
- `七夕 (Chinese curriculum term)`
- `中秋節 (Chinese curriculum term)`
- `重陽節 (Chinese curriculum term)`
- `神話 (Chinese curriculum term)`
- `女媧補天 (Chinese curriculum term)`
- `夸父逐日 (Chinese curriculum term)`
- `精衛填海 (Chinese curriculum term)`
- `后羿射日 (Chinese curriculum term)`
- `嫦娥奔月 (Chinese curriculum term)`
- `書體 (Chinese curriculum term)`
- `篆書 (Chinese curriculum term)`
- `隸書 (Chinese curriculum term)`
- `楷書 (Chinese curriculum term)`
- `行書 (Chinese curriculum term)`
- `草書 (Chinese curriculum term)`
- `文房四寶 (Chinese curriculum term)`
- `四君子 (Chinese curriculum term)`
- `梅 (Chinese curriculum term)`
- `鶴 (Chinese curriculum term)`
- `東風 (Chinese curriculum term)`
- `青 (Chinese curriculum term)`
- `科舉制度 (Chinese curriculum term)`
- `秀才 (Chinese curriculum term)`
- `古代學校 (Chinese curriculum term)`
- `地理代稱 (Chinese curriculum term)`
- `書信代稱 (Chinese curriculum term)`
- `交友情誼代稱 (Chinese curriculum term)`
- `應用文 (Chinese curriculum term)`
- `書信結構 (Chinese curriculum term)`
- `信封書寫 (Chinese curriculum term)`
- `啟事格式 (Chinese curriculum term)`
- `柬帖格式 (Chinese curriculum term)`

### 國文考試與國寫 (Chinese Exams and Guided Writing)

- `國文考試準備 (Chinese curriculum term)`
- `國中教育會考國文 (Chinese curriculum term)`
- `高中國文評量 (Chinese curriculum term)`
- `學測國文 (Chinese curriculum term)`
- `國語文寫作能力測驗 (Chinese curriculum term)`
- `語文知識題 (Chinese curriculum term)`
- `字音題 (Chinese curriculum term)`
- `字形題 (Chinese curriculum term)`
- `詞義題 (Chinese curriculum term)`
- `成語題 (Chinese curriculum term)`
- `修辭題 (Chinese curriculum term)`
- `語法題 (Chinese curriculum term)`
- `文化常識題 (Chinese curriculum term)`
- `文言文題 (Chinese curriculum term)`
- `現代文閱讀題 (Chinese curriculum term)`
- `詩歌閱讀題 (Chinese curriculum term)`
- `多文本題 (Chinese curriculum term)`
- `混合題 (Chinese curriculum term)`
- `圖表閱讀題 (Chinese curriculum term)`
- `題幹判讀 (Chinese curriculum term)`
- `反向題 (Chinese curriculum term)`
- `最佳答案題 (Chinese curriculum term)`
- `排除法 (Chinese curriculum term)`
- `回文定位 (Chinese curriculum term)`
- `證據作答 (Chinese curriculum term)`
- `簡答題 (Chinese curriculum term)`
- `比較題作答 (Chinese curriculum term)`
- `原因題作答 (Chinese curriculum term)`
- `作用題作答 (Chinese curriculum term)`
- `主旨題作答 (Chinese curriculum term)`
- `標題題作答 (Chinese curriculum term)`
- `文言翻譯題 (Chinese curriculum term)`
- `文言比較題 (Chinese curriculum term)`
- `國文考試時間管理 (Chinese curriculum term)`
- `第一輪作答 (Chinese curriculum term)`
- `標記難題 (Chinese curriculum term)`
- `最後檢查 (Chinese curriculum term)`
- `錯題紀錄 (Chinese curriculum term)`
- `錯誤分類 (Chinese curriculum term)`
- `知識型錯誤 (Chinese curriculum term)`
- `理解型錯誤 (Chinese curriculum term)`
- `讀題型錯誤 (Chinese curriculum term)`
- `粗心型錯誤 (Chinese curriculum term)`
- `間隔複習 (Chinese curriculum term)`
- `主動回想 (Chinese curriculum term)`
- `模擬測驗 (Chinese curriculum term)`
- `國寫準備 (Chinese curriculum term)`
- `國寫審題 (Chinese curriculum term)`
- `材料解讀 (Chinese curriculum term)`
- `中心立意 (Chinese curriculum term)`
- `國寫大綱 (Chinese curriculum term)`
- `知性題寫作 (Chinese curriculum term)`
- `情意題寫作 (Chinese curriculum term)`
- `議論結構 (Chinese curriculum term)`
- `敘事結構 (Chinese curriculum term)`
- `國寫開頭 (Chinese curriculum term)`
- `國寫結尾 (Chinese curriculum term)`
- `例證選擇 (Chinese curriculum term)`
- `個人經驗材料 (Chinese curriculum term)`
- `公共議題材料 (Chinese curriculum term)`
- `回應反方 (Chinese curriculum term)`
- `段落統一性 (Chinese curriculum term)`
- `段落發展 (Chinese curriculum term)`
- `作文轉承 (Chinese curriculum term)`
- `具體細節 (Chinese curriculum term)`
- `以描寫呈現 (Chinese curriculum term)`
- `語言準確 (Chinese curriculum term)`
- `語言流暢 (Chinese curriculum term)`
- `表達深度 (Chinese curriculum term)`
- `避免套語 (Chinese curriculum term)`
- `避免空泛 (Chinese curriculum term)`
- `避免流水帳 (Chinese curriculum term)`
- `避免離題 (Chinese curriculum term)`
- `國寫修改 (Chinese curriculum term)`
- `國寫校對 (Chinese curriculum term)`
- `國寫時間管理 (Chinese curriculum term)`
- `內容評量 (Chinese curriculum term)`
- `組織評量 (Chinese curriculum term)`
- `語言評量 (Chinese curriculum term)`
- `卷面格式 (Chinese curriculum term)`
- `作文自我檢查 (Chinese curriculum term)`
- `國文讀書計畫 (Chinese curriculum term)`
- `每日閱讀 (Chinese curriculum term)`
- `定期寫作 (Chinese curriculum term)`
- `字詞複習 (Chinese curriculum term)`
- `文言複習 (Chinese curriculum term)`
- `閱讀複習 (Chinese curriculum term)`
- `考試當日策略 (Chinese curriculum term)`



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

---

# 15. Frequently Asked Questions and Troubleshooting

## `knowparex curriculum` Is Reported as an Invalid Command

First verify that the installed version includes the updated `cli.py`:

```bash
knowparex --help
knowparex curriculum --help
```

When developing locally, reinstall in editable mode:

```bash
python3 -m pip install -e .
```

## `curriculum_integrated.js` Cannot Be Found

Confirm that the file exists:

```text
src/knowparex/data/curriculum_integrated.js
```

Also confirm that `pyproject.toml` is configured:

```toml
[tool.setuptools.package-data]
knowparex = ["data/*.js"]
```

## `NameError: SCAN_IGNORED_CONCEPTS is not defined`

This means the scan exclusion set is missing from `cli.py`. The updated `cli.py` must define it before the scanning functions:

```python
SCAN_IGNORED_CONCEPTS = {
    "已知",
    "未知",
    "問題",
    "答案",
    "原因",
    "表示",
    "比較",
}
```

A production release may include more common generic terms to reduce noisy scan results.

## Search Results Include an Unwanted Data Source

By default, only the original knowledge database is used:

```bash
knowparex search "函數"
```

Explicitly select curriculum data:

```bash
knowparex search "函數" --source curriculum
```

Use both sources only when needed:

```bash
knowparex search "函數" --source all
```

## Multiple Curriculum Lessons Match

Specify an education stage or use a more complete unit name:

```bash
knowparex curriculum lesson math 高一上 "多項式函數" --stage 高中
```

## View Complete Command Help

```bash
knowparex --help
knowparex search --help
knowparex scan --help
knowparex curriculum --help
```

