# 🍐 KnowpareX

<p align="center">
  <img src="LOGO.png" width="180" alt="KnowpareX Logo">
</p>

<p align="center">

**Connect. Compare. Understand. Remember.**<br>
**連結、比較、理解、記住。**

*A structured knowledge database, learning toolkit, and personal review system for Python.*

*一套以結構化知識為核心，結合學習工具與個人複習排程的 Python 套件。*

</p>

---
## Official Website / 官方網站

Explore KnowpareX through its bilingual web interface:

透過中英雙語網頁介面探索 KnowpareX：

**[Open the KnowpareX Official Website / 開啟 KnowpareX 官方網站](https://knowparex.vercel.app/)**

The website provides knowledge search, topic relationships, curriculum exploration, concept comparison, active-recall practice, and spaced review—all without requiring an account.

網站提供知識搜尋、主題關聯、課程探索、概念比較、主動回想與間隔複習，而且不需要註冊帳號。


## What is KnowpareX? / KnowpareX 是什麼？

KnowpareX is a reusable Python package for structured knowledge management and
learning. It combines a searchable knowledge database, curriculum resources,
relationship-based learning, command-line tools, practice and review features,
and a personal Learning Memory system.

KnowpareX 是一套可重複使用的 Python 結構化知識與學習管理套件。它整合了
可搜尋知識庫、課程資源、關係式學習、命令列工具、練習與錯題複習，以及個人
Learning Memory 學習記憶系統。

KnowpareX can be used by:

- Students organizing and reviewing what they learn
- Teachers preparing structured learning material
- Python developers building educational applications
- Anyone exploring relationships between concepts

KnowpareX 適合：

- 整理與複習學習內容的學生
- 製作結構化教材的教師
- 開發教育應用程式的 Python 開發者
- 想探索不同概念之間關係的學習者

---

## ✨ What is new in 1.8.0? / 1.8.0 新功能

Version 1.8.0 introduces **Learning Memory**, a local system for recording
project-based learning and scheduling spaced reviews.

1.8.0 新增 **Learning Memory（學習記憶）**，可以保存專案學習紀錄並安排間隔複習。

### Learning Memory can currently:

- Add a project or learning record
- Store a title, subject, summary, tags, and learning notes
- Show everything that has been recorded
- Show records due for review
- Schedule the next review from a rating of 0–3
- Import Markdown, text, and Python files
- Skip files already imported from the same source path
- Export a record as a readable Markdown learning page
- Provide both command-line and Python interfaces

### Learning Memory 目前可以：

- 新增專案或學習紀錄
- 保存標題、科目、摘要、標籤及學習內容
- 列出所有已保存紀錄
- 顯示今天到期的複習項目
- 根據 0～3 的評分安排下一次複習
- 匯入 Markdown、純文字及 Python 檔案
- 跳過已從相同來源路徑匯入的檔案
- 把紀錄匯出成容易閱讀的 Markdown 教學頁面
- 提供命令列與 Python API

> Learning Memory is currently a record and review scheduler. It does not yet
> use AI, automatically understand the meaning of a file, generate questions,
> synchronize later file changes, or connect imported text to related KnowpareX
> topics. These are possible future stages.

> Learning Memory 目前是紀錄與複習排程器。它尚未使用 AI，也不會自動理解檔案、
> 產生題目、同步後續檔案修改，或把匯入文字連接到相關 KnowpareX 主題。這些可以作為
> 未來版本的發展方向。

Read the complete guide: [Learning Memory / 學習記憶](LEARNING_MEMORY.md)

---

## 📦 Installation / 安裝

Install the published package from PyPI:

從 PyPI 安裝正式版本：

```bash
python3 -m pip install knowparex
```

Update an existing installation:

更新現有版本：

```bash
python3 -m pip install --upgrade knowparex
```

Install a local Git checkout in editable mode:

以可編輯模式安裝本機 Git 專案：

```bash
git clone https://github.com/funlearnstudio/KnowpareX.git
cd KnowpareX
python3 -m pip install -e .
```

Check the installed version:

```bash
python3 -c "import knowparex; print(knowparex.__version__)"
```

---

## 🚀 Quick start / 快速開始

### Search the knowledge database / 搜尋知識庫

```bash
knowparex search "歐姆定律"
```

### Read one topic from Python / 使用 Python 讀取主題

```python
from knowparex import get_topic_data

records = get_topic_data("電學", "歐姆定律")

for record in records:
    print(record)
```

### Browse curriculum data / 瀏覽課程資料

```bash
knowparex curriculum subjects
knowparex curriculum books math --stage 高中
```

---

## 🧠 Learning Memory quick start / 學習記憶快速開始

### 1. Add what you learned / 新增學習內容

```bash
knowparex learning add "Binary search project" \
  --subject APCS \
  --summary "I learned that binary search requires a monotonic condition." \
  --tags algorithm,search
```

The command returns a short record ID. The ID can be used for later review and
export commands.

指令會回傳一組簡短紀錄 ID，之後可用於複習與匯出。

### 2. List saved records / 列出紀錄

```bash
knowparex learning list
```

### 3. Check today's reviews / 查看今日複習

```bash
knowparex learning due
```

Try to recall the idea before opening the original notes. Check the source only
after making a real attempt.

看到到期項目後，先不要打開原始筆記。請先從記憶回答，再查看資料。

### 4. Save the review result / 保存複習結果

```bash
knowparex learning review RECORD_ID 2
```

| Rating | Meaning | Scheduling behavior |
|---:|---|---|
| `0` | Forgot | Reset to the first step |
| `1` | Difficult | Stay at the current step |
| `2` | Remembered | Advance one step |
| `3` | Easy | Advance two steps |

| 評分 | 意思 | 排程結果 |
|---:|---|---|
| `0` | 忘記 | 回到第一階段 |
| `1` | 困難 | 保持目前階段 |
| `2` | 想起來了 | 前進一個階段 |
| `3` | 很簡單 | 前進兩個階段 |

The current interval sequence is:

目前的複習間隔為：

```text
1 → 3 → 7 → 14 → 30 → 60 → 120 days
```

---

## 📄 Import learning files / 匯入學習檔案

Supported formats:

支援格式：

- `.md` — Markdown learning notes
- `.txt` — plain-text explanations
- `.py` — Python projects and examples

Import one file:

匯入一個檔案：

```bash
knowparex learning import "$HOME/Documents/APCS/binary-search.md" \
  --subject APCS \
  --tags algorithm,search
```

Import every supported file in a folder and its subfolders:

匯入資料夾及子資料夾中的支援檔案：

```bash
knowparex learning import "$HOME/Documents/APCS" \
  --recursive \
  --subject APCS
```

When a file is imported, KnowpareX reads its text and stores a snapshot inside
the Learning Memory database. Later edits to the original file are not currently
synchronized automatically.

匯入時，KnowpareX 會讀取文字並把當下內容保存成快照。原始檔案之後的修改目前不會
自動同步。

---

## 🌐 Export learning pages / 匯出教學頁面

Export one record as Markdown:

把一筆紀錄匯出為 Markdown：

```bash
knowparex learning export RECORD_ID \
  --output "$HOME/Desktop/KnowpareX Learning Pages"
```

The generated page contains the title, subject, tags, summary, review information,
and learning notes. Review it before publishing because imported notes may contain
private paths, names, secrets, or unfinished material.

匯出頁面包含標題、科目、標籤、摘要、複習資訊及學習筆記。公開前請先檢查是否含有
私人路徑、姓名、機密資料或尚未完成的內容。

---

## 🐍 Learning Memory Python API

```python
from knowparex import (
    add_learning_record,
    due_learning_records,
    review_learning_record,
)

record = add_learning_record(
    "My APCS project",
    subject="APCS",
    summary="I learned how to trace array indexes.",
    tags=["array", "debugging"],
)

for due_record in due_learning_records():
    print(due_record.title, due_record.next_review_on)

review_learning_record(record.id, 2)
```

---

## 💾 Where personal data is stored / 個人資料位置

KnowpareX stores personal Learning Memory records in the normal per-user data
directory. On macOS, the file is normally:

KnowpareX 會把個人學習紀錄放在一般使用者資料目錄。macOS 通常位於：

```text
~/Library/Application Support/KnowpareX/learning_records.json
```

Open the directory in Finder:

```bash
open "$HOME/Library/Application Support/KnowpareX"
```

The file is not stored inside the installed Python package and is not uploaded
automatically.

這個檔案不會寫進已安裝的 Python 套件，也不會自動上傳。

---

## 🔧 Main command-line tools / 主要指令

```text
knowparex categories
knowparex items CATEGORY
knowparex topic CATEGORY ITEM
knowparex search KEYWORD
knowparex scan TEXT
knowparex curriculum ...
knowparex practice
knowparex review
knowparex learning ...
```

Learning Memory subcommands:

```text
add
list
due
review
import
export
```

Show help at any time:

```bash
knowparex learning --help
```

---

## 🧪 Development and testing / 開發與測試

Install the repository in editable mode:

```bash
python3 -m pip install -e .
```

Run the Learning Memory tests:

```bash
python3 -m unittest discover -s tests -p "test_learning_memory.py" -v
```

Run all discovered tests:

```bash
python3 -m unittest discover -s tests -v
```

---

## 🗺 Development roadmap / 開發路線

Possible future stages include:

未來可以發展：

1. Scan imported files for existing KnowpareX concepts<br>
   掃描匯入檔案並比對現有 KnowpareX 概念
2. Store relationships between learning records and knowledge topics<br>
   保存學習紀錄與知識主題之間的關係
3. Synchronize changed source files<br>
   同步已修改的來源檔案
4. Generate review questions with an optional AI integration<br>
   使用可選的 AI 整合產生複習問題
5. Export a complete static learning website<br>
   匯出完整的靜態學習網站

---

## 📚 Documentation / 文件
- [Quick Review Keywords / 快速回憶用法](KNOWPAREX_TERMINAL_GUIDE.md)
- [Learning Memory / 學習記憶](LEARNING_MEMORY.md)
- [Traditional Chinese API guide](KNOWPAREX_API_GUIDE.td-chi.md)
- [English API guide](KNOWPAREX_API_GUID.en-us.md)
- [Examples](examples/README.md)

---

## 📜 License / 授權

See [LICENSE-CODE](LICENSE-CODE) and [LICENSE-CONTENT](LICENSE-CONTENT) for the
code and content licensing terms.

程式碼與內容授權條款請參閱 [LICENSE-CODE](LICENSE-CODE) 及
[LICENSE-CONTENT](LICENSE-CONTENT)。
