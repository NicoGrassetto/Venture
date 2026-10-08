#!/usr/bin/env python3
"""Opt-in Stop/agentStop guard for one explicitly selected venture workspace."""

from __future__ import annotations

from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import re
import sys

from venture import ROOT, as_object, read_json, records, validate_workspace, workspace_path


def main() -> int:
    selected = os.environ.get("VENTURE_WORKSPACE", "").strip()
    if not selected:
        print("{}")
        print("SKIP: VENTURE_WORKSPACE is not set; no venture completion was checked.", file=sys.stderr)
        return 0
    try:
        event = as_object(json.load(sys.stdin), "hook input")
        active = event.get("stop_hook_active", False)
        if not isinstance(active, bool):
            raise ValueError("stop_hook_active must be a boolean")
    except (UnicodeError, ValueError) as error:
        print("{}")
        print(f"ERROR: invalid completion-hook input: {error}", file=sys.stderr)
        return 1

    workspace = (ROOT / Path(selected)).resolve()
    output = io.StringIO()
    final = False
    try:
        plan = workspace_path(workspace, "business-plan.md").read_text(encoding="utf-8")
        tasks = records(read_json(workspace_path(workspace, "tasks.json"), (1, 2)), "tasks", "tasks")
        final = bool(re.search(r"^\*\*Status:\*\* review-ready\s*$", plan, re.MULTILINE)) or any(
            task.get("id") == "business-plan" and task.get("status") == "passing" for task in tasks
        )
        with redirect_stdout(output):
            validate_workspace(workspace, final=final)
    except (OSError, UnicodeError, ValueError) as error:
        message = (
            f"Venture {'completion' if final else 'workspace'} validation failed: {error}. "
            "Fix the recorded state, or leave the plan explicitly draft/blocked and report the limitation. "
            "Do not invent founder confirmation, evidence, or successful verification."
        )
        print(f"ERROR: {message}", file=sys.stderr)
        if active:
            print("{}")
            print("ERROR: still unverified after a corrective turn; ending automatic retries, not approving completion.", file=sys.stderr)
            return 1
        print(json.dumps({"decision": "block", "reason": message}))
        return 0
    print("{}")
    print(output.getvalue().strip(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
