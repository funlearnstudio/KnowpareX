# KnowpareX 分離式資料來源

這一版不會自動把原本知識庫與 MindLeapX 課程資料混在一起。

## 原則

- `knowledge`：原本的 KnowpareX 知識資料
- `curriculum`：82,215 行課程資料
- `all`：只有使用者明確要求時才合併

## 預設行為

```bash
knowparex search "函數"
```

只查原本知識庫。

```bash
knowparex search "函數" --source curriculum
```

只查課程資料。

```bash
knowparex search "函數" --source all
```

才會查兩邊。

同樣規則適用於 `scan`。

## 安裝

1. 保留原本的 `curriculum_adapter.py`
2. 用這份 `knowledge_service.py` 取代上一版
3. 按照 `CLI_PATCH.md` 修改 CLI 的 `search` 與 `scan`
