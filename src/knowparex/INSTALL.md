# Installation

Replace these files in your project:

```text
src/knowparex/curriculum_adapter.py
src/knowparex/cli.py
```

Then reinstall the development version:

```bash
python3 -m pip install -e .
```

Test:

```bash
knowparex curriculum lesson math 高一上 "多項式 函數" --stage 高中
```

The lesson command now displays a textbook-style article instead of a long
list of relationship records.

Search and scan still use a compact record representation containing only:

- lesson paragraphs
- knowledge-point explanations
- examples
- formulas or rules

The following are excluded:

- curriculum hierarchy metadata
- exam-focus templates
- generic mistakes
- practice templates
- output-skill labels
- source, copyright, and scope metadata
