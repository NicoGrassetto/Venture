#!/usr/bin/env python3
"""Create a working copy of the Identify Key Assumptions workbook."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venture", required=True, help="Venture or project name")
    parser.add_argument("--output", type=Path, default=Path("identify-key-assumptions-workbook.md"))
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output} (use --force)")

    skill_root = Path(__file__).resolve().parent.parent
    template_path = skill_root / "assets" / "workbook.md"
    if not template_path.is_file():
        raise SystemExit(f"Workbook template not found: {template_path}")

    content = template_path.read_text(encoding="utf-8")
    content = content.replace("{VENTURE_NAME}", args.venture)
    content = content.replace("{DATE}", date.today().isoformat())

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(f"Created {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
