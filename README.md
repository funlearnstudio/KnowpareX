# KnowpareX

> **Connect. Compare. Understand.**  
> **連結、比較、理解。**

A reusable Python package for knowledge relationships, programming comparisons, and school-subject learning data.

一個可重複使用的 Python 套件，以知識關係為核心，包含程式語言比較、高中學科資料、查詢介面與資料收集功能。
## Documentation／完整文件

For complete commands, APIs, relationship functions, and registered topics, see:

完整指令、API、關係函式與資料分類，請參考：

[`KNOWPAREX_API_GUIDE.md`](KNOWPAREX_API_GUIDE.md)

## Install / 安裝

From this folder:

```bash
python3 -m pip install .
```

For editable development mode:

```bash
python3 -m pip install -e .
```

## Import / 匯入

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

## Examples / 範例

```python
from knowparex import get_categories, get_items, get_topic_data

print(get_categories())
print(get_items("電學"))

data = get_topic_data("電學", "歐姆定律")
for record in data:
    print(record)
```

Direct function call:

```python
from knowparex import library

library["國文文學常識"]["唐宋八大家"]()
```

## Command line / 命令列

```bash
knowparex --categories
knowparex --items 電學
knowparex --topic 電學 歐姆定律
knowparex-compare
```

## Public API / 使用者介面

- `library` — central category and item registry
- `compare_system` — relationship functions and data collector
- `get_categories()` — list category names
- `get_items(category)` — list items in a category
- `get_topic_data(category, item)` — return structured topic records
- `topic_exists(category, item)` — check whether a topic exists

## Add new data / 新增資料

1. Add a note module under `src/knowparex/PROGRAMMING_NOTES` or `SUBJECT_NOTES`.
2. Use functions from `compare_system`.
3. Import the class in `system_library.py`.
4. Register the function in `library` without parentheses.

```python
"電學": {
    "歐姆定律": physics_electricity.ohms_law,
}
```

## License / 授權

- Original Python source code: MIT License (`LICENSE-CODE`)
- Original educational content: CC BY-NC-SA 4.0 (`LICENSE-CONTENT`)
- Third-party material keeps its original rights.

原創 Python 程式碼採 MIT License；原創學科內容採 CC BY-NC-SA 4.0。第三方內容仍受原權利條款約束。

## Built-in command-line tools／內建命令列工具

After installation, the tools can be started from any directory. No separate example file is required.
安裝後可在任何資料夾直接啟動，不需要另外複製範例程式。

```bash
knowparex compare
knowparex practice
knowparex review
```

Short standalone commands are also available:

```bash
knowparex-compare
knowparex-practice
knowparex-review
```

Wrong answers are saved in the current user's application-data directory, so they remain available even when the command is run from another folder.
錯題會儲存在目前使用者的應用程式資料目錄，因此從其他資料夾執行時仍可繼續複習。
