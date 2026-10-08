#!/usr/bin/env python3
"""Create and validate persistent Venture workspaces without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
TEMPLATES = ROOT / "templates"
DOCUMENTS = {
    "brief.md": TEMPLATES / "brief.md",
    "business-plan.md": SKILLS / "create-business-plan" / "assets" / "workbook.md",
    "progress.md": TEMPLATES / "progress.md",
}
STATES = {"not_started", "in_progress", "blocked", "passing"}
UNFINISHED = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\{(?:VENTURE_NAME|DATE)\}")
CLAIM_ID = re.compile(r"\bE-\d{3,}\b")
SEED_FIELDS = ("title", "skills", "depends_on", "artifacts", "acceptance")
REVIEW_DIMENSIONS = (
    "decision_fit",
    "evidence_integrity",
    "coherence",
    "financial_reasoning",
    "actionability",
    "handoff_quality",
)


def as_object(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected a JSON object")
    result: dict[str, object] = {}
    for key, item in value.items():
        if not isinstance(key, str):
            raise ValueError(f"{label}: object keys must be strings")
        result[key] = item
    return result


def read_json(path: Path) -> dict[str, object]:
    try:
        value: object = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}: invalid JSON at line {error.lineno}: {error.msg}") from error
    data = as_object(value, str(path))
    version = data.get("schema_version")
    if type(version) is not int or version != 1:
        raise ValueError(f"{path}: schema_version must be 1")
    return data


def records(data: dict[str, object], key: str, label: str) -> list[dict[str, object]]:
    value = data.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{label}.{key}: expected an array")
    return [as_object(item, f"{label}.{key}[{index}]") for index, item in enumerate(value)]


def text(data: dict[str, object], key: str, label: str, allow_empty: bool = False) -> str:
    value = data.get(key)
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise ValueError(f"{label}.{key}: expected {'a' if allow_empty else 'a nonempty'} string")
    return value


def strings(
    data: dict[str, object], key: str, label: str, allow_empty: bool = False
) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValueError(f"{label}.{key}: expected {'an' if allow_empty else 'a nonempty'} array")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{label}.{key}: every item must be a nonempty string")
        if item in result:
            raise ValueError(f"{label}.{key}: duplicate value {item!r}")
        result.append(item)
    return result


def check_date(value: str, label: str) -> None:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"{label}: expected an ISO date (YYYY-MM-DD)")
    try:
        recorded = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{label}: invalid date {value!r}") from error
    if recorded > date.today():
        raise ValueError(f"{label}: a recording or review date cannot be in the future")


def workspace_path(workspace: Path, value: str, must_exist: bool = True) -> Path:
    relative = Path(value)
    if relative.is_absolute():
        raise ValueError(f"Workspace references must be relative: {value}")
    target = (workspace / relative).resolve()
    try:
        target.relative_to(workspace)
    except ValueError as error:
        raise ValueError(f"Reference escapes the workspace: {value}") from error
    if must_exist and not target.is_file():
        raise ValueError(f"Referenced file not found: {value}")
    return target


def check_source(workspace: Path, source: str) -> None:
    parsed = urlsplit(source)
    if parsed.scheme in {"http", "https"}:
        if not parsed.hostname or parsed.username is not None or parsed.password is not None:
            raise ValueError(f"Source must be a valid URL without embedded credentials: {source}")
    elif parsed.scheme:
        raise ValueError(f"Unsupported source URL scheme: {parsed.scheme}")
    else:
        workspace_path(workspace, source)


def validate_evidence(workspace: Path, final: bool) -> set[str]:
    data = read_json(workspace_path(workspace, "evidence.json"))
    known: set[str] = set()
    for claim in records(data, "claims", "evidence"):
        claim_id = text(claim, "id", "claim")
        if not CLAIM_ID.fullmatch(claim_id) or claim_id in known:
            raise ValueError(f"Invalid or duplicate evidence ID: {claim_id}")
        known.add(claim_id)
        kind = text(claim, "type", claim_id)
        if kind not in {"fact", "inference", "assumption"}:
            raise ValueError(f"{claim_id}: type must be fact, inference, or assumption")
        text(claim, "statement", claim_id)
        text(claim, "contradictions", claim_id)
        if text(claim, "confidence", claim_id) not in {"low", "medium", "high"}:
            raise ValueError(f"{claim_id}: confidence must be low, medium, or high")
        check_date(text(claim, "date", claim_id), f"{claim_id}.date")
        source = text(claim, "source", claim_id, allow_empty=True)
        next_test = text(claim, "next_test", claim_id, allow_empty=True)
        if source.strip():
            check_source(workspace, source)
        elif kind != "assumption":
            raise ValueError(f"{claim_id}: facts and inferences require a source")
        if kind == "assumption" and not next_test.strip():
            raise ValueError(f"{claim_id}: an assumption requires a next_test")
        if final and any(UNFINISHED.search(value) for value in claim.values() if isinstance(value, str)):
            raise ValueError(f"{claim_id}: unfinished evidence placeholder")
    return known


def has_content(section: str) -> bool:
    lines = re.sub(r"<!--.*?-->", "", section, flags=re.DOTALL).splitlines()
    for index, line in enumerate(lines):
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        if re.fullmatch(r"[\s|:-]+", value) or re.fullmatch(r"\*\*[^*]+:\*\*", value):
            continue
        if value.startswith("|") and index + 1 < len(lines):
            if re.fullmatch(r"[\s|:-]+", lines[index + 1]):
                continue
        if re.search(r"\w", value):
            return True
    return False


def check_complete_document(filename: str, document: str) -> None:
    if UNFINISHED.search(document):
        raise ValueError(f"{filename}: unfinished placeholder")
    headings = list(re.finditer(r"^## (.+)$", document, re.MULTILINE))
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(document)
        if not has_content(document[heading.end():end]):
            raise ValueError(f"{filename}: empty section '{heading.group(1)}'")


def validate_documents(workspace: Path, evidence: set[str], final: bool) -> None:
    for filename, template in DOCUMENTS.items():
        document = workspace_path(workspace, filename).read_text(encoding="utf-8")
        required = re.findall(r"^## (.+)$", template.read_text(encoding="utf-8"), re.MULTILINE)
        headings = list(re.finditer(r"^## (.+)$", document, re.MULTILINE))
        names = [heading.group(1) for heading in headings]
        for heading in required:
            if names.count(heading) != 1:
                raise ValueError(f"{filename}: expected exactly one heading '## {heading}'")
        unknown = set(CLAIM_ID.findall(document)) - evidence
        if unknown:
            raise ValueError(f"{filename}: unknown evidence IDs: {', '.join(sorted(unknown))}")
        if final:
            check_complete_document(filename, document)
            if filename == "business-plan.md":
                if not re.search(r"^\*\*Status:\*\* review-ready\s*$", document, re.MULTILINE):
                    raise ValueError("business-plan.md: final status must be review-ready")
                if not CLAIM_ID.search(document):
                    raise ValueError("business-plan.md: cite registered evidence IDs in the plan")


def validate_discovery(workspace: Path, task: dict[str, object], passing: bool) -> None:
    label = "venture-brief.discovery"
    if "discovery" not in task:
        if passing:
            raise ValueError(
                f"{label}: founder confirmation is required before passing; "
                "add the discovery fields from templates/tasks.json and complete founder discovery"
            )
        return
    discovery = as_object(task["discovery"], label)
    values = {
        field: text(discovery, field, label, allow_empty=not passing)
        for field in ("confirmed_by", "confirmed_on", "confirmation_source")
    }
    if passing and any(UNFINISHED.search(value) for value in values.values()):
        raise ValueError(f"{label}: unfinished founder confirmation")
    if values["confirmed_on"]:
        check_date(values["confirmed_on"], f"{label}.confirmed_on")
    if values["confirmation_source"]:
        source = values["confirmation_source"]
        if urlsplit(source).scheme or urlsplit(source).netloc:
            raise ValueError(f"{label}: confirmation_source must be a local workspace file")
        record = workspace_path(workspace, source).read_text(encoding="utf-8")
        if passing and (UNFINISHED.search(record) or not has_content(record)):
            raise ValueError(f"{label}: confirmation record is empty or unfinished")
    if passing:
        brief = workspace_path(workspace, "brief.md").read_text(encoding="utf-8")
        check_complete_document("brief.md", brief)


def validate_review(task: dict[str, object], passing: bool) -> None:
    scores = as_object(task.get("review_scores"), "business-plan.review_scores")
    if set(scores) != set(REVIEW_DIMENSIONS):
        raise ValueError("business-plan.review_scores: include all six rubric dimensions")
    completed: dict[str, int] = {}
    for dimension, value in scores.items():
        if value is None and not passing:
            continue
        if type(value) is not int or value not in {0, 1, 2}:
            raise ValueError(f"business-plan.review_scores.{dimension}: expected a score from 0 to 2")
        completed[dimension] = value
    if passing and (
        sum(completed.values()) < 10
        or 0 in completed.values()
        or completed["evidence_integrity"] != 2
    ):
        raise ValueError("Business-plan review requires at least 10/12, no zero, and evidence integrity of 2")


def validate_graph(dependencies: dict[str, list[str]]) -> None:
    visited: set[str] = set()
    visiting: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visiting:
            raise ValueError(f"Task dependency cycle involving {task_id}")
        if task_id in visited:
            return
        visiting.add(task_id)
        for dependency in dependencies[task_id]:
            if dependency not in dependencies:
                raise ValueError(f"{task_id}: unknown dependency {dependency}")
            visit(dependency)
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in dependencies:
        visit(task_id)


def validate_tasks(workspace: Path, evidence: set[str], final: bool) -> tuple[int, int]:
    data = read_json(workspace_path(workspace, "tasks.json"))
    venture = text(data, "venture", "tasks")
    if UNFINISHED.search(venture):
        raise ValueError("tasks.venture: replace the venture name placeholder")
    tasks = records(data, "tasks", "tasks")
    seed = {
        text(task, "id", "template"): task
        for task in records(read_json(TEMPLATES / "tasks.json"), "tasks", "template")
    }
    states: dict[str, str] = {}
    dependencies: dict[str, list[str]] = {}
    for task in tasks:
        task_id = text(task, "id", "task")
        if not re.fullmatch(r"[a-z][a-z0-9-]*", task_id) or task_id in states:
            raise ValueError(f"Invalid or duplicate task ID: {task_id}")
        text(task, "title", task_id)
        status = text(task, "status", task_id)
        if status not in STATES:
            raise ValueError(f"{task_id}: invalid status {status!r}")
        states[task_id] = status
        dependencies[task_id] = strings(task, "depends_on", task_id, allow_empty=True)
        strings(task, "acceptance", task_id)
        for skill in strings(task, "skills", task_id):
            if not re.fullmatch(r"[a-z][a-z0-9-]*", skill) or not (SKILLS / skill / "SKILL.md").is_file():
                raise ValueError(f"{task_id}: unknown skill {skill}")
        if task_id in seed:
            for field in SEED_FIELDS:
                if task.get(field) != seed[task_id].get(field):
                    raise ValueError(f"{task_id}: retain the starter {field}; extend the ledger with additional tasks")
        for artifact in strings(task, "artifacts", task_id):
            workspace_path(workspace, artifact, must_exist=status == "passing")
        references = strings(task, "evidence", task_id, allow_empty=True)
        for reference in references:
            if reference not in evidence:
                raise ValueError(f"{task_id}: unknown evidence ID {reference}")
        for field in ("owner", "reviewer", "reviewed_on", "verification"):
            value = text(task, field, task_id, allow_empty=status != "passing")
            if status == "passing" and UNFINISHED.search(value):
                raise ValueError(f"{task_id}.{field}: unfinished review placeholder")
            if field == "reviewed_on" and value:
                check_date(value, f"{task_id}.{field}")
        if status == "passing" and not references:
            raise ValueError(f"{task_id}: passing requires recorded evidence")
        if task_id == "venture-brief":
            validate_discovery(workspace, task, status == "passing")
        if task_id == "business-plan":
            validate_review(task, status == "passing")
    missing = set(seed) - set(states)
    if missing:
        raise ValueError(f"Missing required starter tasks: {', '.join(sorted(missing))}")
    validate_graph(dependencies)
    if list(states.values()).count("in_progress") > 1:
        raise ValueError("Only one task may be in_progress at a time")
    for task_id, status in states.items():
        if status in {"in_progress", "passing"}:
            for dependency in dependencies[task_id]:
                if states[dependency] != "passing":
                    raise ValueError(f"{task_id}: dependency {dependency} is not passing")
    unfinished = [task_id for task_id, status in states.items() if status != "passing"]
    if final and unfinished:
        raise ValueError(f"Unfinished tasks: {', '.join(unfinished)}")
    return len(states) - len(unfinished), len(states)


def validate_workbooks(workspace: Path, final: bool) -> None:
    for workbook in sorted((workspace / "workbooks").rglob("*.md")):
        workspace_path(workspace, workbook.relative_to(workspace).as_posix())
        suffix = "-workbook.md"
        if not workbook.name.endswith(suffix):
            raise ValueError(f"Use <skill-name>-workbook.md for chapter workbooks: {workbook.name}")
        skill = workbook.name[:-len(suffix)]
        validator = SKILLS / skill / "scripts" / "validate_workbook.py"
        if not validator.is_file():
            raise ValueError(f"No chapter validator for {workbook.name}")
        command = [sys.executable, str(validator), str(workbook)]
        if not final:
            command.append("--allow-todo")
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip(), file=sys.stderr)
        if result.returncode:
            raise ValueError(f"Chapter validation failed: {workbook.name}")
        if final and UNFINISHED.search(workbook.read_text(encoding="utf-8")):
            raise ValueError(f"Chapter validation failed: {workbook.name} has unfinished placeholders")


def validate_workspace(workspace: Path, final: bool = False) -> None:
    workspace = workspace.resolve()
    for directory in ("raw", "workbooks"):
        if not workspace_path(workspace, directory, must_exist=False).is_dir():
            raise ValueError(f"Missing workspace directory: {directory}")
    evidence = validate_evidence(workspace, final)
    validate_documents(workspace, evidence, final)
    passing, total = validate_tasks(workspace, evidence, final)
    validate_workbooks(workspace, final)
    mode = "Review-ready structure" if final else "Draft structure"
    print(f"{mode} valid: {passing}/{total} tasks passing.")
    print("Structural checks do not establish evidence truth or business viability.")


def initialize(venture: str, output: Path) -> None:
    venture = venture.strip()
    if not venture or any(ord(character) < 32 for character in venture):
        raise ValueError("Venture name must be a nonempty single line")
    if UNFINISHED.search(venture):
        raise ValueError("Venture name must not contain an unfinished placeholder")
    if output.exists() or output.is_symlink():
        raise ValueError(f"Refusing to overwrite existing output: {output}; use validate to resume")
    rendered = {
        filename: template.read_text(encoding="utf-8")
        .replace("{VENTURE_NAME}", venture)
        .replace("{DATE}", date.today().isoformat())
        for filename, template in DOCUMENTS.items()
    }
    for filename in ("tasks.json", "evidence.json"):
        data = read_json(TEMPLATES / filename)
        if filename == "tasks.json":
            data["venture"] = venture
        rendered[filename] = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    output.mkdir(parents=True)
    for filename, content in rendered.items():
        with (output / filename).open("x", encoding="utf-8") as destination:
            destination.write(content)
    for directory in ("raw", "workbooks"):
        (output / directory).mkdir()
    print(f"Created workspace: {output.resolve()}")
    validate_workspace(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("init", help="Create a new venture workspace without overwriting")
    create.add_argument("--venture", required=True)
    create.add_argument("--output", required=True, type=Path)
    validate = commands.add_parser("validate", help="Check a venture workspace and its recorded state")
    validate.add_argument("workspace", type=Path)
    validate.add_argument("--final", action="store_true", help="Require review-ready completion, not just draft structure")
    args = parser.parse_args()
    try:
        if args.command == "init":
            initialize(args.venture, args.output)
        else:
            validate_workspace(args.workspace, final=args.final)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
