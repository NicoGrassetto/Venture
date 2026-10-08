#!/usr/bin/env python3
"""Build task-specific standalone skill assets from shared authoring sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from skill_contracts import CONTRACTS, Contract
from skill_names import RENAMES
from sync_skills import local_path
from workbook_runtime import empty_record, render_record


ROOT = Path(__file__).resolve().parent.parent


def section(content: str, heading: str, body: str) -> str:
    pattern = re.compile(r"^## " + re.escape(heading) + r"\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    replacement = f"## {heading}\n\n{body.strip()}\n\n"
    return pattern.sub(lambda match: replacement, content, count=1)


def skill_instructions(content: str, contract: Contract) -> str:
    for old, new in RENAMES.items():
        content = content.replace(old, new)
    content = re.sub(r'^  version: "[^"]+"$', '  version: "2.0.0"', content, flags=re.MULTILINE)
    content = re.sub(r"^# [^\n]+", f"# {contract['title']}", content, count=1, flags=re.MULTILINE)
    content = content.replace("## Required context", "## Inputs and missing data")
    policy = (
        f"{contract['input_gate']}\n\n"
        "Use `draft` for unfinished work, `research-plan` for a completed protocol, "
        "and `completed-analysis` only for an analysis actually performed. "
        "Never invent observations, founder approval, or external actions."
    )
    content = content.replace(
        "Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.",
        "",
    )
    inputs = re.search(r"^## Inputs and missing data\n(.*?)(?=^## |\Z)", content, re.MULTILINE | re.DOTALL)
    if inputs:
        body = re.sub(r"<!-- input-policy:start -->.*?<!-- input-policy:end -->", "", inputs.group(1), flags=re.DOTALL).strip()
        body += f"\n\n<!-- input-policy:start -->\n{policy}\n<!-- input-policy:end -->"
        content = section(content, "Inputs and missing data", body)
    if "## Use when / not for" not in content:
        content = content.replace("## Inputs and missing data", f"## Use when / not for\n\nUse this skill for the decision described in the goal.\nNot for: {contract['not_for']}\n\n## Inputs and missing data", 1)
    else:
        content = section(content, "Use when / not for", f"Use this skill for the decision described in the goal.\nNot for: {contract['not_for']}")
    contract_section = (
        "Use [the task-specific workbook](assets/workbook.md). Its structured record "
        f"contains these result tables: {', '.join(f'`{name}`' for name in contract['tables'])}.\n\n"
        "Read [the record format](references/record-format.md) for stages, evidence, and units, "
        "and [the synthetic worked example](references/example.md) for a complete result and failure case.\n"
        "A research plan leaves result tables empty and supplies a testable protocol instead."
    )
    if "## Output contract" not in content:
        content = content.replace("## Evidence rules", f"## Output contract\n\n{contract_section}\n\n## Evidence rules", 1)
    else:
        content = section(content, "Output contract", contract_section)
    content = section(content, "Evidence rules", (
        "Separate facts, inferences, and assumptions. Cite stable evidence IDs with "
        "sources, dates, confidence, and contradictions. Forecasts are not observations.\n"
        "Preserve negative results and define the next useful test. Obtain authorization "
        "before outreach, spending, publication, or commitments; protect identifying data."
    ))
    content = content.replace("## Completion contract", "## Deliverable and completion checks")
    readiness = (
        "Apply the outcome criteria below to `completed-analysis`. A `research-plan` "
        "can be complete as a protocol but does not satisfy observed-result criteria."
    )
    if readiness not in content:
        content = content.replace("## Deliverable and completion checks\n", f"## Deliverable and completion checks\n\n{readiness}\n", 1)
    handoff = (
        "Record the decision, declared stage, supporting and contradicting evidence, "
        "remaining uncertainty, and one next action with owner and date. "
        "Name any upstream artifact invalidated by the result.\n\n"
        "Next skills, when their inputs are ready: "
        + ", ".join(f"[{name}](../{name}/SKILL.md)" for name in contract["next_skills"])
        + ". Standalone users may need to install these optional follow-ups."
    )
    content = section(content, "Handoff", handoff)
    return content.rstrip() + "\n"


def outputs(root: Path) -> dict[str, str]:
    expected: dict[str, str] = {}
    runtime = (root / "scripts" / "workbook_runtime.py").read_text(encoding="utf-8")
    format_reference = (root / "templates" / "record-format.md").read_text(encoding="utf-8")
    for name, specification in CONTRACTS.items():
        contract: dict[str, object] = dict(specification)
        base = f"skills/{name}"
        skill = local_path(root, f"{base}/SKILL.md")
        expected[f"{base}/SKILL.md"] = skill_instructions(skill.read_text(encoding="utf-8"), specification)
        method_path = local_path(root, f"{base}/references/method.md")
        method = method_path.read_text(encoding="utf-8")
        for old, new in RENAMES.items():
            method = method.replace(old, new)
        method = re.sub(r"^# [^\n]+", f"# {contract['title']}: Method Reference", method, count=1, flags=re.MULTILINE)
        if "## Worked example" not in method:
            method = method.rstrip() + "\n\n## Worked example\n\nSee [the synthetic worked example](example.md) and [record format](record-format.md).\n"
        expected[f"{base}/references/method.md"] = method
        expected[f"{base}/assets/contract.json"] = json.dumps(contract, indent=2, ensure_ascii=False) + "\n"
        draft = empty_record(contract, "{VENTURE_NAME}")
        draft["date"] = "{DATE}"
        expected[f"{base}/assets/workbook.md"] = render_record(draft, str(contract["title"]), contract)
        expected[f"{base}/scripts/_workbook.py"] = runtime
        for command in ("create", "validate"):
            expected[f"{base}/scripts/{command}_workbook.py"] = (
                "#!/usr/bin/env python3\n"
                "# Generated by scripts/build_workbooks.py; shared runtime is bundled locally.\n"
                "from pathlib import Path\n"
                f"from _workbook import {command}_main\n\n\n"
                'if __name__ == "__main__":\n'
                f"    raise SystemExit({command}_main(Path(__file__).resolve().parent.parent))\n"
            )
        example = empty_record(contract, "Synthetic invoice-assistant example", "completed-analysis")
        example.update(
            synthetic=True, owner="Synthetic founder", date="2026-01-08",
            scope=contract["example_scope"], data=contract["example_data"],
            evidence=[{
                "id": "E-001", "type": "fact", "statement": "Synthetic illustration only; not an actual customer or financial observation.",
                "source": "https://example.com/synthetic-illustration", "date": "2026-01-08", "confidence": "low",
                "contradictions": "The example is constructed and cannot support a real business decision.", "next_test": "",
            }],
            decision="Use this shape to analyze the real venture; do not reuse these conclusions.",
            limitations="Synthetic fixture only. Source authenticity and business validity have not been established.",
            next_actions=[{"action": "Replace the illustration with authorized venture evidence", "owner": "Venture owner", "due_date": "2026-02-01", "evidence_expected": "Dated source records and reconciled inputs"}],
        )
        expected[f"{base}/references/example.md"] = (
            render_record(example, f"Synthetic worked example: {contract['title']}")
            + f"\n## Worked reasoning\n\n{contract['example_note']}\n"
            + f"\n## Failure case\n\n{contract['failure_case']}\n"
        )
        expected[f"{base}/references/record-format.md"] = format_reference
    return expected


def build(root: Path, check: bool) -> None:
    expected = outputs(root)
    differences = [name for name, content in expected.items() if not local_path(root, name).exists() or local_path(root, name).read_text(encoding="utf-8") != content]
    if check and differences:
        raise ValueError("Generated skill packages are stale: " + ", ".join(differences))
    if not check:
        for name in differences:
            path = local_path(root, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected[name], encoding="utf-8")
    print(f"{'Checked' if check else 'Built'} {len(CONTRACTS)} task-specific standalone packages.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing generated outputs")
    args = parser.parse_args()
    try:
        build(ROOT, args.check)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
