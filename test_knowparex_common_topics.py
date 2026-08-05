#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path


TOPICS = [
    "二次函數",
    "勾股定理",
    "歐姆定律",
    "牛頓第二定律",
    "氧化還原",
    "莫耳",
    "光合作用",
    "細胞呼吸",
    "自然選擇",
    "板塊運動",
]

BAD_PHRASES = [
    "理解某主題要先建立概念邊界",
    "要先建立概念邊界",
    "每一項都要寫出已知條件",
    "用單位、原始資料、反例或另一種方法檢查",
    "比較處理組與對照組時，兩組必須來自同一母群",
    "Unknown topic:",
]

OUTPUT_DIR = Path("knowparex_common_topic_results")


def normalize(line: str) -> str:
    return re.sub(r"\s+", "", line).strip("。；，、:：")


def repeated_long_lines(text: str) -> list[tuple[str, int]]:
    normalized_lines = [
        normalize(line)
        for line in text.splitlines()
        if len(normalize(line)) >= 35
    ]
    counts = Counter(normalized_lines)
    return [
        (line, count)
        for line, count in counts.items()
        if count >= 2
    ]


def run_topic(topic: str) -> tuple[bool, list[str], str]:
    command = [
        "knowparex",
        "search",
        topic,
        "--source",
        "curriculum",
        "--open",
    ]

    result = subprocess.run(
        command,
        input="1\n",
        text=True,
        capture_output=True,
        timeout=90,
    )

    combined = (result.stdout or "") + (result.stderr or "")
    problems: list[str] = []

    if result.returncode != 0:
        problems.append(f"指令結束碼為 {result.returncode}")

    for phrase in BAD_PHRASES:
        if phrase in combined:
            problems.append(f"出現舊模板或錯誤文字：{phrase}")

    duplicates = repeated_long_lines(combined)
    if duplicates:
        preview = duplicates[0][0][:45]
        problems.append(f"偵測到重複長句：{preview}…")

    if "【重點知識】" not in combined:
        problems.append("沒有找到【重點知識】區塊")

    if len(combined.strip()) < 180:
        problems.append("輸出內容過短或沒有成功開啟文章")

    return not problems, problems, combined


def main() -> int:
    if shutil.which("knowparex") is None:
        print("找不到 knowparex 指令。請先確認套件已安裝。")
        return 1

    OUTPUT_DIR.mkdir(exist_ok=True)

    passed = 0
    failed = 0

    print("=" * 62)
    print("KnowpareX 常見主題內容測試")
    print("=" * 62)

    for index, topic in enumerate(TOPICS, start=1):
        print(f"[{index:02d}/{len(TOPICS)}] 測試：{topic}")

        try:
            ok, problems, output = run_topic(topic)
        except subprocess.TimeoutExpired:
            ok = False
            problems = ["執行超過 90 秒"]
            output = ""

        output_path = OUTPUT_DIR / f"{index:02d}_{topic}.txt"
        output_path.write_text(output, encoding="utf-8")

        if ok:
            passed += 1
            print("  結果：初步通過")
        else:
            failed += 1
            print("  結果：需要檢查")
            for problem in problems:
                print(f"  - {problem}")

    print()
    print("=" * 62)
    print(f"初步通過：{passed}")
    print(f"需要檢查：{failed}")
    print(f"完整輸出資料夾：{OUTPUT_DIR.resolve()}")
    print("=" * 62)
    print()
    print("注意：這是自動初篩，不代表學科內容已由專家審定。")

    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
