# KnowpareX Learning Memory / 學習記憶

Learning Memory records what you learned from projects, schedules later reviews,
imports existing notes, and exports readable Markdown learning pages.

學習記憶可以記錄專案中學到的內容、安排日後複習、匯入現有筆記，並匯出容易閱讀的 Markdown 教學頁面。

## Add a project / 新增專案

```bash
knowparex learning add "Binary search project" \
  --subject APCS \
  --summary "I learned how monotonic conditions make binary search possible." \
  --tags algorithm,search
```

## Check and complete reviews / 查看並完成複習

```bash
knowparex learning due
knowparex learning review RECORD_ID 2
```

Ratings / 評分：

- `0`: forgot; restart at one day / 忘記了，隔天重新開始
- `1`: difficult; keep the current step / 很困難，維持目前階段
- `2`: remembered; advance one step / 成功想起，前進一個階段
- `3`: easy; advance two steps / 很容易，前進兩個階段

The first scheduler uses review intervals of 1, 3, 7, 14, 30, 60, and 120 days.

第一版排程使用 1、3、7、14、30、60、120 天的複習間隔。

## Import existing files / 匯入現有檔案

Supported formats are Markdown, plain text, and Python source files.

目前支援 Markdown、純文字與 Python 程式檔。

```bash
knowparex learning import ./my-notes --recursive --subject APCS
```

Already imported source paths are skipped to avoid simple duplicates.

已匯入過的來源路徑會自動跳過，避免產生簡單重複項目。

## Export a learning page / 匯出教學頁面

```bash
knowparex learning export RECORD_ID --output ./public-learning-pages
```

The result is a Markdown file that can be placed on GitHub or used by a static-site
generator. Review the content before publishing because imported notes may contain
private paths, names, or unfinished information.

輸出結果是可以放上 GitHub 或交給靜態網站產生器的 Markdown 檔。公開之前請先檢查內容，因為匯入的筆記可能包含私人路徑、姓名或尚未完成的資料。

## Python API

```python
from knowparex import add_learning_record, due_learning_records

record = add_learning_record(
    "My APCS project",
    summary="What I understood and what I still need to practice.",
    subject="APCS",
)

for item in due_learning_records():
    print(item.title, item.next_review_on)
```

Personal data is stored in KnowpareX's normal per-user data directory as
`learning_records.json`; it is not written into the installed Python package.

個人資料會儲存在 KnowpareX 一般的使用者資料目錄中，檔名為 `learning_records.json`，不會寫進已安裝的 Python 套件。
