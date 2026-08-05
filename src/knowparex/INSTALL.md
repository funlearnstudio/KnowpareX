# KnowpareX 課程推薦搜尋更新

請把以下檔案覆蓋到專案：

```text
src/knowparex/curriculum_adapter.py
src/knowparex/cli.py
```

重新安裝或建置後測試：

```bash
knowparex curriculum lesson math 高一上 "多項式函數" --stage 高中
```

課程文章底部會新增：

```text
【推薦搜尋】

1. 函數
   來源：知識庫
   位置：函數 / 一次函數
   相關概念：函數
   搜尋：knowparex search "函數" --source knowledge
```

推薦來源會同時包含：

- 原本 KnowpareX 知識庫
- MindLeapX 課程資料

推薦依據：

- 課程單元名稱
- 重點知識名稱
- 公式中的中文概念名稱

目前課程本身、重複名稱與通用詞會自動排除。
