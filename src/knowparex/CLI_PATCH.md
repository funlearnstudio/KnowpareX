# 將 CLI 改成「資料來源分開」

## 1. search 加入參數

在 search_parser 建立後加入：

```python
search_parser.add_argument(
    "--source",
    choices=("knowledge", "curriculum", "all"),
    default="knowledge",
    help=(
        "搜尋來源：knowledge=原本知識庫，"
        "curriculum=課程資料，all=兩者"
    ),
)
```

呼叫 search_main 時加入：

```python
source=args.source,
```

然後把：

```python
def search_main(...):
```

改成包含：

```python
def search_main(..., source="knowledge"):
```

在 search_main 裡所有：

```python
get_categories()
get_items(category)
get_topic_data(category, item)
```

改成：

```python
get_categories(source=source)
get_items(category, source=source)
get_topic_data(category, item, source=source)
```

---

## 2. scan 加入參數

```python
scan_parser.add_argument(
    "--source",
    choices=("knowledge", "curriculum", "all"),
    default="knowledge",
    help="掃描來源，預設只掃描原本知識庫",
)
```

呼叫：

```python
scan_main(
    args.text,
    minimum_length=args.min_length,
    json_output=args.json,
    source=args.source,
)
```

修改：

```python
def collect_scan_topics(*, minimum_length=2, source="knowledge"):
```

裡面改成：

```python
for category in get_categories(source=source):
    for item in get_items(category, source=source):
        records = get_topic_data(category, item, source=source)
```

`scan_main()` 也新增 `source="knowledge"`，並傳進
`collect_scan_topics()`。

---

## 3. 建議新增獨立 curriculum 指令

讓課程瀏覽完全不混進 categories/items/topic：

```bash
knowparex curriculum subjects
knowparex curriculum books math
knowparex curriculum units math 高一上
knowparex curriculum lesson math 高一上 "實數與絕對值"
```

---

## 使用結果

### 原本知識庫（預設）

```bash
knowparex search "絕對值"
knowparex scan "三次函數"
```

### 只查課程

```bash
knowparex search "絕對值" --source curriculum
knowparex scan "三次函數" --source curriculum
```

### 明確要求兩邊一起查

```bash
knowparex search "絕對值" --source all
knowparex scan "三次函數" --source all
```

這樣預設永遠不會把兩組資料混在一起。
