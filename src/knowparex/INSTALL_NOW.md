# 直接套用

把三個檔案放進：

```text
src/knowparex/
├── cli.py
├── knowledge_service.py
├── curriculum_adapter.py
└── data/
    └── curriculum_integrated.js
```

在 `pyproject.toml` 確保有：

```toml
[tool.setuptools.package-data]
knowparex = ["data/*.js"]
```

本機立即測試：

```bash
python3 -m pip install -e .
knowparex curriculum subjects
knowparex curriculum books math --stage 高中
knowparex curriculum units math 高一上 --stage 高中
knowparex curriculum lesson math 高一上 函數 --stage 高中

knowparex search "三次函數"
knowparex search "三次函數" --source curriculum
knowparex scan "三次函數" --source curriculum
```

規則：

- 不寫 `--source`：只使用原本知識庫。
- `--source curriculum`：只使用課程資料。
- `--source all`：兩邊一起使用。
