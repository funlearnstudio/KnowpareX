#!/usr/bin/env python3
"""Apply systemic KnowpareX curriculum quality and search hardening.

This tool is intentionally conservative: it fixes ranking, removes obviously
cross-topic matches from ``search --open``, runs the existing full rebuild, and
produces a report of units that still need human subject review. It never
claims that automated checks equal expert verification.

Run from the repository root:

    python3 tools/apply_full_quality_hardening.py --write
"""

from __future__ import annotations

import argparse
import json
import py_compile
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "src/knowparex/cli.py"
DATA = ROOT / "src/knowparex/data/curriculum_integrated.js"

OLD_SORT = '''    sorted_topics = sorted(
        matched_topics,
        key=lambda topic: (
            topic not in direct_topic_matches,
            topic[0],
            topic[1],
        ),
    )
'''

NEW_SORT = '''    def _search_bigrams(value: object) -> set[str]:
        normalized = re.sub(
            r"[^0-9a-z\\u4e00-\\u9fff]+",
            "",
            str(value).casefold(),
        )
        if len(normalized) < 2:
            return {normalized} if normalized else set()
        return {
            normalized[index:index + 2]
            for index in range(len(normalized) - 1)
        }

    query_bigrams = _search_bigrams(original_keyword)

    def _topic_relevance(topic: tuple[str, str]) -> tuple:
        category, item = topic
        normalized_item = item.casefold().strip()
        item_bigrams = _search_bigrams(item)
        overlap = len(query_bigrams & item_bigrams)
        union = len(query_bigrams | item_bigrams) or 1
        title_similarity = overlap / union
        record_count = len(grouped_records.get(topic, []))

        if normalized_item == normalized_keyword:
            title_score = 1000
        elif normalized_keyword in normalized_item:
            title_score = 850
        elif normalized_item in normalized_keyword:
            title_score = 700
        else:
            title_score = int(title_similarity * 600)

        return (
            -(title_score + min(record_count, 10) * 5),
            topic not in direct_topic_matches,
            category,
            item,
        )

    sorted_topics = sorted(matched_topics, key=_topic_relevance)

    # ``--open`` is for choosing the intended topic, not browsing every unit
    # whose long article happens to contain the query.  When a title-related
    # result exists, hide zero-title-similarity record-only noise.
    if open_topic:
        title_related = []
        for topic in sorted_topics:
            item_bigrams = _search_bigrams(topic[1])
            overlap = len(query_bigrams & item_bigrams)
            union = len(query_bigrams | item_bigrams) or 1
            similarity = overlap / union
            if (
                topic in direct_topic_matches
                or normalized_keyword in topic[1].casefold()
                or similarity >= 0.20
            ):
                title_related.append(topic)
        if title_related:
            sorted_topics = title_related[:20]
'''


def patch_cli(write: bool) -> dict:
    text = CLI.read_text(encoding="utf-8")
    if NEW_SORT in text:
        return {"status": "already_patched", "path": str(CLI)}
    if OLD_SORT not in text:
        return {
            "status": "not_patched",
            "path": str(CLI),
            "reason": "expected sort block not found",
        }
    if not write:
        return {"status": "would_patch", "path": str(CLI)}

    backup = CLI.with_name(CLI.name + ".before_quality_hardening")
    shutil.copy2(CLI, backup)
    CLI.write_text(text.replace(OLD_SORT, NEW_SORT, 1), encoding="utf-8")
    try:
        py_compile.compile(str(CLI), doraise=True)
    except Exception:
        shutil.copy2(backup, CLI)
        raise
    return {
        "status": "patched",
        "path": str(CLI),
        "backup": str(backup),
    }


def run_rebuild(write: bool) -> dict:
    if str(ROOT / "src") not in sys.path:
        sys.path.insert(0, str(ROOT / "src"))
    from knowparex.curriculum_adapter import load_curriculum_js
    from knowparex.curriculum_rebuild import audit_data, rebuild_data, write_curriculum_js

    data = load_curriculum_js(DATA)
    counts = rebuild_data(data)
    audit = audit_data(data)
    result = {"rebuild": counts, "audit": audit}
    if write:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = DATA.with_name(DATA.name + f".before_hardening_{stamp}")
        shutil.copy2(DATA, backup)
        write_curriculum_js(DATA, data)
        result["backup"] = str(backup)
        result["written"] = str(DATA)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    report = {
        "cli": patch_cli(args.write),
        "curriculum": run_rebuild(args.write),
        "note": (
            "Automated checks can remove structural and ranking errors, but "
            "cannot certify every lesson as expert-reviewed."
        ),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
