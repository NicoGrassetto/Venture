#!/usr/bin/env python3
"""Validate structure and completion signals in a Show That the Dogs Will Eat the Dog Food workbook."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_HEADINGS = ['Decision to make', 'Success definitions', 'Instrumentation and cohorts', 'Usage and retention', 'Payment and outcomes', 'Root causes and advocacy', 'Decision and next evidence', 'Final decision', 'Next actions', 'Change log']


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument(
        "--allow-todo",
        action="store_true",
        help="Allow TODO placeholders while still checking structure",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.workbook.is_file():
        raise SystemExit(f"Workbook not found: {args.workbook}")

    text = args.workbook.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE):
            errors.append(f"Missing required heading: ## {heading}")

    todo_count = len(re.findall(r"\bTODO\b", text))
    if todo_count and not args.allow_todo:
        errors.append(f"Workbook still contains {todo_count} TODO placeholder(s)")

    evidence_rows = [
        line
        for line in text.splitlines()
        if line.startswith("|") and "fact/inference/assumption" not in line and "---" not in line
    ]
    if len(evidence_rows) < 16:
        warnings.append("Evidence tables appear sparse; verify that material claims are sourced")

    if "Strongest contradicting evidence:" not in text:
        errors.append("Missing contradicting-evidence section")
    if "Reversal evidence:" not in text:
        errors.append("Missing reversal-evidence field")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1
    print(f"Validated {args.workbook}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
