# KnowpareX Terminal Command Guide

> Complete bilingual terminal reference for KnowpareX and Learning Memory  
> KnowpareX 與 Learning Memory 完整雙語終端機指令手冊

This document explains the user-facing terminal commands implemented in
KnowpareX. It is separate from `README.md` and can be kept as a command handbook.

本文件說明 KnowpareX 已實作的使用者終端機指令。它與 `README.md` 分開，可以作為
獨立的指令手冊保存。

---

## 1. Command notation / 指令符號

Examples in this guide use these placeholders:

本手冊使用以下佔位符：

| Placeholder | Replace it with | 中文說明 |
|---|---|---|
| `KEYWORD` | A search term | 搜尋詞 |
| `CATEGORY` | A KnowpareX category | 知識分類 |
| `ITEM` | A topic inside a category | 分類中的主題 |
| `SUBJECT` | A curriculum subject | 課程科目 |
| `BOOK` | A curriculum book name | 課程冊別 |
| `UNIT` | A curriculum unit | 課程單元 |
| `RECORD_ID` | A Learning Memory ID | 學習紀錄 ID |
| `FILE` | A file path | 檔案路徑 |
| `DIRECTORY` | A folder path | 資料夾路徑 |

Do not type the placeholder literally. For example:

不要直接輸入佔位符。例如：

```bash
knowparex search "歐姆定律"
```

When a path contains spaces, wrap it in quotation marks:

路徑包含空格時，必須加上引號：

```bash
"$HOME/Desktop/LEARNING FILES/example.md"
```

---

## 2. Installation and version checks / 安裝與版本檢查

### Install from PyPI / 從 PyPI 安裝

```bash
python3 -m pip install knowparex
```

### Upgrade the installed package / 更新套件

```bash
python3 -m pip install --upgrade knowparex
```

### Install a local repository in editable mode / 以可編輯模式安裝本機儲存庫

Run this inside the repository folder:

在儲存庫資料夾中執行：

```bash
python3 -m pip install -e .
```

Editable mode means changes in the source folder are used without building a
new wheel every time.

可編輯模式表示修改原始碼後，不必每次重新建立 wheel。

### Check the installed version / 查看安裝版本

```bash
python3 -c "import knowparex; print(knowparex.__version__)"
```

### Show package installation information / 查看套件安裝資訊

```bash
python3 -m pip show knowparex
```

### Show main help / 顯示主要說明

```bash
knowparex --help
```

Alternative form if the `knowparex` executable is not found:

若系統找不到 `knowparex` 指令，可使用：

```bash
python3 -m knowparex.cli --help
```

---

## 3. Interactive comparison / 互動比較

### Open the default interactive mode

```bash
knowparex
```

Equivalent command:

```bash
knowparex compare
```

Standalone entry point:

```bash
knowparex-compare
```

This mode displays categories, asks you to select a category and item, and then
shows structured relationship records.

此模式會列出分類，要求選擇分類與項目，再顯示結構化知識關係。

Enter `0` when the prompt says that `0` exits. Press `Control + C` only when you
need to interrupt a command immediately.

提示顯示可用 `0` 結束時，請輸入 `0`。只有需要立即中止時才按 `Control + C`。

---

## 4. Categories and topics / 分類與主題

### List every built-in category / 列出所有內建分類

```bash
knowparex categories
```

Example output may include programming, mathematics, science, English, history,
geography, civics, and Chinese-language categories.

輸出可能包含程式設計、數學、自然、英文、歷史、地理、公民與國文分類。

### List items in one category / 列出分類中的項目

```bash
knowparex items CATEGORY
```

Example:

```bash
knowparex items 電學
```

### Display one topic / 顯示一個主題

```bash
knowparex topic CATEGORY ITEM
```

Example:

```bash
knowparex topic 電學 歐姆定律
```

### Display a topic as JSON / 以 JSON 顯示主題

```bash
knowparex topic CATEGORY ITEM --json
```

Example:

```bash
knowparex topic 電學 歐姆定律 --json
```

---

## 5. Search / 搜尋

### Basic search / 基本搜尋

```bash
knowparex search KEYWORD
```

Example:

```bash
knowparex search "牛頓第二定律"
```

By default, search uses the original structured knowledge database.

預設只搜尋原本的結構化知識庫。

### Choose a data source / 選擇資料來源

```bash
knowparex search KEYWORD --source knowledge
knowparex search KEYWORD --source curriculum
knowparex search KEYWORD --source all
```

| Source | Meaning | 中文說明 |
|---|---|---|
| `knowledge` | Original relationship database | 原本關係式知識庫 |
| `curriculum` | Curriculum lesson database | 課程教材資料庫 |
| `all` | Search both sources | 同時搜尋兩者 |

### Summary mode / 摘要模式

```bash
knowparex search KEYWORD --summary
```

Shows a shorter result instead of every detailed record.

顯示較短摘要，而不是所有詳細紀錄。

### Exact matching / 完整匹配

```bash
knowparex search KEYWORD --exact
```

Uses stricter matching instead of ordinary substring matching.

使用較嚴格的完整內容匹配。

### Search topic names only / 只搜尋主題名稱

```bash
knowparex search KEYWORD --topic-only
```

### Search relationship records only / 只搜尋關係紀錄

```bash
knowparex search KEYWORD --record-only
```

`--topic-only` and `--record-only` cannot be used together.

`--topic-only` 與 `--record-only` 不能同時使用。

### Search inside one category / 限定分類

```bash
knowparex search KEYWORD --category CATEGORY
```

Example:

```bash
knowparex search "電阻" --category 電學
```

### Limit detailed records / 限制顯示數量

```bash
knowparex search KEYWORD --limit 10
```

The limit must be greater than zero.

數量必須大於零。

### JSON output / JSON 輸出

```bash
knowparex search KEYWORD --json
```

This is useful when another program needs to process the results.

適合讓其他程式繼續處理結果。

### Count results / 只計算結果數量

```bash
knowparex search KEYWORD --count
```

### Show one random matching record / 隨機顯示一筆

```bash
knowparex search KEYWORD --random
```

### Tree view / 樹狀顯示

```bash
knowparex search KEYWORD --tree
```

Groups results by category and topic.

依分類與主題整理結果。

### Open a topic from search results / 從搜尋結果開啟主題

```bash
knowparex search KEYWORD --open
```

KnowpareX displays candidate topics and asks you to select one.

KnowpareX 會列出候選主題並要求選擇。

### Combine compatible options / 組合可相容選項

```bash
knowparex search "函數" \
  --source curriculum \
  --summary \
  --limit 5
```

Only one display mode can normally be selected from `--json`, `--count`,
`--random`, `--tree`, and `--open`.

`--json`、`--count`、`--random`、`--tree`、`--open` 通常一次只能選一種顯示模式。

---

## 6. Text concept scanner / 文字概念掃描

The scanner finds concepts already registered in KnowpareX. It does not answer
the text or use AI.

掃描器會找出已存在於 KnowpareX 的概念；它不會回答內容，也不使用 AI。

### Scan one piece of text / 掃描一段文字

```bash
knowparex scan "TEXT"
```

Example:

```bash
knowparex scan "電壓等於電流乘以電阻。"
```

### Interactive scanning / 互動掃描

```bash
knowparex scan
```

When no text argument is supplied, KnowpareX enters interactive mode.

省略文字參數時，KnowpareX 進入互動模式。

### Choose the scanner source / 選擇掃描來源

```bash
knowparex scan "TEXT" --source knowledge
knowparex scan "TEXT" --source curriculum
knowparex scan "TEXT" --source all
```

### Set the minimum concept length / 設定最短概念字數

```bash
knowparex scan "TEXT" --min-length 3
```

Shorter terms are ignored. The value must be greater than zero.

較短的詞會被忽略；數值必須大於零。

### Scanner JSON output / 掃描器 JSON 輸出

```bash
knowparex scan "TEXT" --json
```

Combined example:

```bash
knowparex scan "二分搜尋會重複縮小搜尋範圍" \
  --source all \
  --min-length 2 \
  --json
```

---

## 7. Curriculum commands / 課程指令

### Show curriculum help / 顯示課程說明

```bash
knowparex curriculum --help
```

### List curriculum subjects / 列出課程科目

```bash
knowparex curriculum subjects
```

### List books for a subject / 列出科目的冊別

```bash
knowparex curriculum books SUBJECT
```

Example:

```bash
knowparex curriculum books math
```

Optional stage filter:

```bash
knowparex curriculum books math --stage 高中
```

`--category` is accepted as another name for `--stage`:

`--category` 也可以代替 `--stage`：

```bash
knowparex curriculum books math --category 高中
```

### List units in a book / 列出冊別單元

```bash
knowparex curriculum units SUBJECT BOOK
```

Example:

```bash
knowparex curriculum units math 高一數學
```

With a stage filter:

```bash
knowparex curriculum units math 高一數學 --stage 高中
```

### Display a complete lesson / 顯示完整教材

```bash
knowparex curriculum lesson SUBJECT BOOK UNIT
```

Example:

```bash
knowparex curriculum lesson math 高一數學 二次函數
```

With a stage filter:

```bash
knowparex curriculum lesson math 高一數學 二次函數 --stage 高中
```

If more than one lesson matches, add the stage or use the exact book and unit
names shown by the `books` and `units` commands.

如果找到多筆教材，請加入學制，或使用 `books` 與 `units` 顯示的完整名稱。

---

## 8. Practice / 練習

### Start practice mode / 開始練習模式

```bash
knowparex practice
```

Standalone entry point:

```bash
knowparex-practice
```

Practice mode asks you to select a category and topic, creates questions from
relationship records, checks answers, reports a score, and stores incorrect
answers for later review.

練習模式會要求選擇分類與主題，從關係紀錄產生題目、檢查答案、計算分數，並保存錯題。

---

## 9. Wrong-answer review / 錯題複習

### Start wrong-answer review / 開始錯題複習

```bash
knowparex review
```

Standalone entry point:

```bash
knowparex-review
```

The review tool groups saved wrong answers by subject and unit. Correct answers
are removed; questions answered incorrectly remain for another review.

錯題工具會依科目與單元整理題目。答對後移除；仍答錯的題目會保留供下次複習。

If there are no saved wrong questions, it prints the wrong-question storage path.

若沒有錯題，程式會顯示錯題檔案的保存位置。

---

## 10. Database statistics / 資料庫統計

```bash
knowparex stats
```

Displays category count, topic count, relationship count, average records per
topic, the largest topic, category statistics, and common relationship types.

顯示分類數、主題數、關係數、平均紀錄、最大主題、各分類統計及常見關係。

---

## 11. Today's knowledge / 今日知識

```bash
knowparex today
```

Selects a topic from the current date. The result remains the same during the
same day.

根據日期選出一個主題；同一天的結果保持相同。

---

## 12. Explain a topic / 解釋主題

```bash
knowparex explain CATEGORY ITEM
```

Example:

```bash
knowparex explain 電學 歐姆定律
```

Converts structured relationship records into readable sentences.

把結構化關係紀錄轉成較容易閱讀的文字。

---

## 13. Export a built-in topic / 匯出內建主題

This command exports a topic from the built-in knowledge database. It is
different from `knowparex learning export`, which exports a personal record.

此指令匯出內建知識主題，和匯出個人紀錄的 `knowparex learning export` 不同。

### Export as Markdown / 匯出為 Markdown

```bash
knowparex export CATEGORY ITEM --format md
```

### Export as plain text / 匯出為純文字

```bash
knowparex export CATEGORY ITEM --format txt
```

### Export as JSON / 匯出為 JSON

```bash
knowparex export CATEGORY ITEM --format json
```

### Choose the output filename / 指定輸出檔名

```bash
knowparex export CATEGORY ITEM \
  --format md \
  --output output-file.md
```

Example:

```bash
knowparex export 電學 歐姆定律 \
  --format md \
  --output ohms-law.md
```

---

## 14. Related topics / 相關主題

```bash
knowparex related CATEGORY ITEM
```

Example:

```bash
knowparex related 電學 歐姆定律
```

Limit the number of related topics:

限制相關主題數量：

```bash
knowparex related 電學 歐姆定律 --limit 5
```

The limit must be greater than zero.

數量必須大於零。

---

## 15. Learning Memory overview / Learning Memory 總覽

Learning Memory stores personal project-learning records separately from the
built-in knowledge database.

Learning Memory 會把個人專案學習紀錄與內建知識庫分開保存。

Show Learning Memory help:

```bash
knowparex learning --help
```

Standalone entry point:

```bash
knowparex-learning --help
```

Available subcommands:

```text
add
list
due
review
import
export
```

Current Learning Memory is a local record and spaced-review scheduler. It does
not yet use AI, generate questions, understand knowledge relationships, monitor
source files, or send notifications.

目前 Learning Memory 是本機紀錄與間隔複習排程器。它尚未使用 AI、自動出題、
理解知識關係、監視來源檔案或發送通知。

---

## 16. Add a Learning Memory record / 新增學習紀錄

### Minimal command / 最短指令

```bash
knowparex learning add "TITLE"
```

Example:

```bash
knowparex learning add "Binary search"
```

### Add a subject / 加入科目

```bash
knowparex learning add "Binary search" --subject APCS
```

### Add a summary / 加入摘要

```bash
knowparex learning add "Binary search" \
  --subject APCS \
  --summary "I learned how monotonic conditions make binary search possible."
```

### Add comma-separated tags / 加入逗號分隔標籤

```bash
knowparex learning add "Binary search" \
  --subject APCS \
  --summary "I learned the closed-interval implementation." \
  --tags algorithm,search,boundary
```

The command prints the new record ID and first review date.

指令會顯示新紀錄 ID 與第一次複習日期。

---

## 17. List Learning Memory records / 列出學習紀錄

```bash
knowparex learning list
```

Each line shows:

每一行顯示：

```text
RECORD_ID | TITLE | SUBJECT | next: NEXT_REVIEW_DATE
```

If no records exist, KnowpareX prints `No learning records yet.`

若沒有紀錄，KnowpareX 會顯示 `No learning records yet.`。

---

## 18. Show reviews due today / 顯示今日到期複習

```bash
knowparex learning due
```

This displays records whose next review date is today or earlier.

顯示下次複習日期為今天或更早的紀錄。

Use this before opening your notes. Try to recall the content first, then check
the source.

建議先執行此指令，再打開筆記。先從記憶回答，之後才查看來源。

If nothing is due, it prints `Nothing is due for review.`

若沒有到期項目，會顯示 `Nothing is due for review.`。

---

## 19. Record a completed review / 記錄完成複習

```bash
knowparex learning review RECORD_ID RATING
```

You can use the full ID, a unique ID prefix, or an exact title.

可以使用完整 ID、唯一 ID 前綴或完全相同的標題。

Example using an ID:

```bash
knowparex learning review 25b80ce31b01 2
```

Example using an exact title:

```bash
knowparex learning review "二分搜尋" 2
```

| Rating | Meaning | Result | 中文 |
|---:|---|---|---|
| `0` | Forgot | Reset to first step | 忘記，回到第一階段 |
| `1` | Difficult | Keep current step | 困難，保持目前階段 |
| `2` | Remembered | Advance one step | 想起來，前進一階 |
| `3` | Easy | Advance two steps | 很簡單，前進兩階 |

Current intervals:

目前間隔：

```text
1 → 3 → 7 → 14 → 30 → 60 → 120 days
```

Only ratings `0`, `1`, `2`, and `3` are accepted.

只接受 `0`、`1`、`2`、`3`。

---

## 20. Import one learning file / 匯入單一學習檔案

Supported formats:

支援格式：

```text
.md
.txt
.py
```

Basic command:

```bash
knowparex learning import FILE
```

Example:

```bash
knowparex learning import \
  "$HOME/Desktop/LEARNING FILES/example.md"
```

Add subject and tags:

```bash
knowparex learning import \
  "$HOME/Desktop/LEARNING FILES/example.md" \
  --subject APCS \
  --tags project,apcs
```

For Markdown, the first `# Heading` becomes the record title. Otherwise, the
filename becomes the title. KnowpareX stores a snapshot of the file contents and
the original absolute source path.

Markdown 的第一個 `# 標題` 會成為紀錄標題；否則使用檔名。KnowpareX 會保存內容快照
與原始絕對路徑。

Important: importing a single file again may create another record in the
current version. Check `knowparex learning list` before repeating an import.

注意：目前版本重複匯入單一檔案時可能建立另一筆紀錄。重新匯入前請先執行
`knowparex learning list`。

---

## 21. Import a learning directory / 匯入學習資料夾

Import supported files directly inside one folder:

```bash
knowparex learning import DIRECTORY
```

Example:

```bash
knowparex learning import \
  "$HOME/Documents/APCS Notes" \
  --subject APCS
```

Include subfolders:

```bash
knowparex learning import \
  "$HOME/Documents/APCS Notes" \
  --recursive \
  --subject APCS \
  --tags imported,apcs
```

Directory import skips source paths that already exist in Learning Memory.

資料夾匯入會跳過 Learning Memory 中已存在的來源路徑。

It does not automatically synchronize a file after that file changes.

原始檔案之後修改時，目前不會自動同步。

---

## 22. Export a Learning Memory page / 匯出學習頁面

```bash
knowparex learning export RECORD_ID
```

The default output directory is:

預設輸出資料夾：

```text
knowparex-learning-pages
```

Choose another output directory:

```bash
knowparex learning export RECORD_ID \
  --output "$HOME/Desktop/KnowpareX Learning Pages"
```

Example:

```bash
knowparex learning export 25b80ce31b01 \
  --output "$HOME/Desktop/KnowpareX Learning Pages"
```

The result is a Markdown page containing the title, subject, tags, last review,
summary, and learning notes.

輸出為 Markdown，包含標題、科目、標籤、上次複習、摘要與學習內容。

Review exported content before publishing it. Imported notes may contain private
paths, names, account information, secrets, or unfinished material.

公開前請檢查內容是否包含私人路徑、姓名、帳戶資訊、機密或未完成內容。

---

## 23. Learning Memory storage / 學習記憶保存位置

On macOS, Learning Memory normally uses:

macOS 通常使用：

```text
~/Library/Application Support/KnowpareX/learning_records.json
```

Open the folder in Finder:

```bash
open "$HOME/Library/Application Support/KnowpareX"
```

Display the JSON neatly:

```bash
python3 -m json.tool \
  "$HOME/Library/Application Support/KnowpareX/learning_records.json"
```

Normal updates should be made with KnowpareX commands instead of editing the JSON
manually.

一般更新應使用 KnowpareX 指令，不建議直接手動修改 JSON。

---

## 24. Wrong-question storage / 錯題保存位置

Wrong answers from practice are stored separately from Learning Memory.

練習錯題與 Learning Memory 分開保存。

Open the KnowpareX data folder:

```bash
open "$HOME/Library/Application Support/KnowpareX"
```

The relevant files are normally:

```text
wrong_questions.json
learning_records.json
```

---

## 25. Testing the Learning Memory feature / 測試 Learning Memory

Run from the repository root:

在儲存庫根目錄執行：

```bash
python3 -m unittest discover \
  -s tests \
  -p "test_learning_memory.py" \
  -v
```

Expected ending:

```text
Ran 2 tests
OK
```

Run all discovered tests:

```bash
python3 -m unittest discover -s tests -v
```

Run Python syntax compilation:

```bash
python3 -m compileall -q src
```

---

## 26. A complete daily workflow / 完整每日流程

### Step 1: Check due items / 查看到期項目

```bash
knowparex learning due
```

### Step 2: Recall without notes / 不看筆記回想

Explain the idea, solve a related problem, or rewrite important code before
checking the source.

先解釋觀念、完成相關題目或重寫重要程式，再查看來源。

### Step 3: Record the rating / 記錄評分

```bash
knowparex learning review RECORD_ID RATING
```

### Step 4: Add today's important learning / 加入今天的重要學習

```bash
knowparex learning add "TITLE" \
  --subject "SUBJECT" \
  --summary "WHAT I LEARNED" \
  --tags tag1,tag2
```

### Step 5: Import a detailed note when needed / 必要時匯入詳細筆記

```bash
knowparex learning import "FILE" \
  --subject "SUBJECT" \
  --tags tag1,tag2
```

---

## 27. Common errors / 常見錯誤

### `command not found: knowparex`

Reinstall the local repository:

```bash
cd /path/to/KnowpareX
python3 -m pip install -e .
```

Or use:

```bash
python3 -m knowparex.cli --help
```

### `No module named knowparex`

Check the active Python and installation:

```bash
which python3
python3 -m pip show knowparex
```

Then install using the same Python:

```bash
python3 -m pip install -e .
```

### `learning` is an invalid command

The installed copy does not include Learning Memory, or another Python
installation is running an older version.

目前執行的版本沒有 Learning Memory，或另一套 Python 正在使用舊版本。

```bash
python3 -c "import knowparex; print(knowparex.__file__)"
python3 -c "import knowparex; print(knowparex.__version__)"
python3 -m pip install -e .
```

### File not found during import / 匯入時找不到檔案

Check the exact path:

```bash
ls "$HOME/Desktop/LEARNING FILES/example.md"
```

You can drag a file from Finder into Terminal to paste its complete path.

可以把 Finder 裡的檔案拖進終端機，自動貼上完整路徑。

### Unsupported file type / 不支援的檔案格式

Current Learning Memory supports only:

```text
.md
.txt
.py
```

PDF, Word, and notebook importing are not implemented yet.

目前尚未實作 PDF、Word 與 Notebook 匯入。

### Learning record not found / 找不到學習紀錄

List the IDs and titles:

```bash
knowparex learning list
```

Then copy the correct ID into the review or export command.

再把正確 ID 複製到複習或匯出指令。

### Ambiguous learning record / 學習紀錄不明確

This can happen when an ID prefix matches more than one record or duplicate exact
titles exist. Use the complete record ID.

ID 前綴符合多筆資料或存在重複標題時可能發生。請使用完整紀錄 ID。

### No wrong questions to review / 沒有錯題

Complete practice questions first:

```bash
knowparex practice
```

Incorrect answers are saved for:

```bash
knowparex review
```

---

## 28. Quick command index / 快速指令索引

```text
knowparex
knowparex --help
knowparex compare
knowparex categories
knowparex items CATEGORY
knowparex topic CATEGORY ITEM
knowparex topic CATEGORY ITEM --json
knowparex search KEYWORD [OPTIONS]
knowparex scan [TEXT] [OPTIONS]
knowparex curriculum subjects
knowparex curriculum books SUBJECT [--stage STAGE]
knowparex curriculum units SUBJECT BOOK [--stage STAGE]
knowparex curriculum lesson SUBJECT BOOK UNIT [--stage STAGE]
knowparex practice
knowparex review
knowparex stats
knowparex today
knowparex explain CATEGORY ITEM
knowparex export CATEGORY ITEM [--format md|txt|json] [--output FILE]
knowparex related CATEGORY ITEM [--limit NUMBER]
knowparex learning add TITLE [--summary TEXT] [--subject TEXT] [--tags TAGS]
knowparex learning list
knowparex learning due
knowparex learning review RECORD RATING
knowparex learning import PATH [--subject TEXT] [--tags TAGS] [--recursive]
knowparex learning export RECORD [--output DIRECTORY]
knowparex-compare
knowparex-practice
knowparex-review
knowparex-learning
```

---

## 29. Command discovery / 自行查看指令

When the program changes, built-in help is the most current reference:

程式更新後，內建說明通常是最新參考：

```bash
knowparex --help
knowparex search --help
knowparex scan --help
knowparex curriculum --help
knowparex curriculum books --help
knowparex curriculum units --help
knowparex curriculum lesson --help
knowparex related --help
knowparex export --help
knowparex learning --help
knowparex learning add --help
knowparex learning review --help
knowparex learning import --help
knowparex learning export --help
```

---

## 30. Current feature boundary / 目前功能界線

KnowpareX currently has two different forms of review:

KnowpareX 目前有兩種不同複習：

| Command | Reviews | 中文 |
|---|---|---|
| `knowparex review` | Wrong answers created by practice mode | 複習練習模式產生的錯題 |
| `knowparex learning review` | Personal projects and imported learning files | 複習個人專案與匯入檔案 |

It also has two different export commands:

也有兩種不同匯出：

| Command | Exports | 中文 |
|---|---|---|
| `knowparex export` | Built-in knowledge topics | 匯出內建知識主題 |
| `knowparex learning export` | Personal Learning Memory records | 匯出個人學習紀錄 |

Learning Memory remembers the imported snapshot and review schedule. It does not
yet automatically connect an imported file to related KnowpareX topics. The
existing `scan` command can manually inspect a piece of text for known concepts,
but automatic connection is a future feature.

Learning Memory 會保存匯入快照與複習排程，但尚未自動連接相關 KnowpareX 主題。
現有 `scan` 指令可以手動掃描文字中的已知概念；自動連接屬於未來功能。
