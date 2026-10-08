from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.skill_names import RENAMES
from scripts.workbook_runtime import extract_record


ROOT = Path(__file__).resolve().parent.parent
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")


class MigrationTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="venture-migration-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.workspace = self.root / "legacy venture"
        self.cli("init", "--venture", "Legacy venture", "--output", self.workspace)
        self.legacy = json.loads((ROOT / "templates" / "tasks-v1.json").read_text(encoding="utf-8"))
        self.legacy["venture"] = "Legacy venture"
        self.write_tasks(self.legacy)

    def cli(self, *arguments: object, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "venture.py"), *(str(argument) for argument in arguments)],
            cwd=self.root, env=ENV, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def write_tasks(self, data: dict) -> None:
        (self.workspace / "tasks.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def snapshot(self) -> dict[str, bytes]:
        return {path.relative_to(self.workspace).as_posix(): path.read_bytes() for path in self.workspace.rglob("*") if path.is_file()}

    def test_v1_validation_requests_explicit_migration(self) -> None:
        self.assertIn("migrate", self.cli("validate", self.workspace, expected=1).stderr)

    def test_dry_run_does_not_write(self) -> None:
        before = self.snapshot()
        result = self.cli("migrate", self.workspace, "--dry-run")
        self.assertIn("Would update tasks.json", result.stdout)
        self.assertEqual(before, self.snapshot())

    def test_all_renamed_workbooks_preserve_paths_notes_and_backups(self) -> None:
        originals = {}
        for old in RENAMES:
            path = self.workspace / "workbooks" / f"{old}-workbook.md"
            content = f"# Previous {old} analysis\n\nKeep this user-owned reasoning and TODO notes verbatim.\n"
            path.write_text(content, encoding="utf-8")
            originals[path] = content
        before_tasks = (self.workspace / "tasks.json").read_bytes()
        self.cli("migrate", self.workspace)
        migrated = json.loads((self.workspace / "tasks.json").read_text(encoding="utf-8"))
        self.assertEqual(migrated["schema_version"], 2)
        self.assertEqual(len(migrated["tasks"]), 9)
        for task in migrated["tasks"]:
            self.assertEqual(task["status"], "not_started")
            self.assertTrue(all(skill not in RENAMES for skill in task["skills"]))
        backups = list((self.workspace / ".migration-backups").iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "tasks.json").read_bytes(), before_tasks)
        for path, content in originals.items():
            updated = path.read_text(encoding="utf-8")
            self.assertTrue(updated.endswith(content))
            record = extract_record(updated)
            self.assertEqual(record["stage"], "draft")
            self.assertEqual(record["skill"], RENAMES[path.name.removesuffix("-workbook.md")])
            self.assertEqual((backups[0] / path.relative_to(self.workspace)).read_text(encoding="utf-8"), content)
        self.cli("validate", self.workspace)
        self.cli("validate", self.workspace, "--final", expected=1)

    def test_migration_is_idempotent(self) -> None:
        self.cli("migrate", self.workspace)
        before = self.snapshot()
        self.assertIn("already uses v2", self.cli("migrate", self.workspace).stdout)
        self.assertEqual(self.snapshot(), before)

    def test_older_drafts_receive_missing_confirmation_fields_without_approval(self) -> None:
        data = copy.deepcopy(self.legacy)
        del data["tasks"][0]["discovery"]
        self.write_tasks(data)
        self.cli("migrate", self.workspace)
        migrated = json.loads((self.workspace / "tasks.json").read_text(encoding="utf-8"))
        brief = migrated["tasks"][0]
        self.assertEqual(brief["discovery"], {"confirmed_by": "", "confirmed_on": "", "confirmation_source": ""})
        self.assertEqual(brief["status"], "not_started")
        self.cli("validate", self.workspace)

    def test_custom_tasks_and_review_history_are_preserved(self) -> None:
        data = copy.deepcopy(self.legacy)
        data["tasks"][0].update(status="passing", verification="Prior review must remain visible.")
        extra = copy.deepcopy(data["tasks"][0])
        extra.update(id="founder-followup", title="A custom founder action", depends_on=["venture-brief"])
        data["tasks"].append(extra)
        self.write_tasks(data)
        self.cli("migrate", self.workspace)
        result = json.loads((self.workspace / "tasks.json").read_text(encoding="utf-8"))
        tasks = {task["id"]: task for task in result["tasks"]}
        self.assertIn("founder-followup", tasks)
        self.assertEqual(tasks["founder-followup"]["title"], "A custom founder action")
        self.assertEqual(tasks["venture-brief"]["verification"], "Prior review must remain visible.")
        self.assertEqual(tasks["venture-brief"]["status"], "not_started")

    def test_customized_starter_contract_is_not_silently_overwritten(self) -> None:
        data = copy.deepcopy(self.legacy)
        data["tasks"][0]["acceptance"] = ["User customization that must be reconciled."]
        self.write_tasks(data)
        before = self.snapshot()
        self.assertIn("customized", self.cli("migrate", self.workspace, expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_custom_task_collision_with_new_starter_is_preserved(self) -> None:
        data = copy.deepcopy(self.legacy)
        task = copy.deepcopy(data["tasks"][0])
        task["id"] = "risk-triage"
        data["tasks"].append(task)
        self.write_tasks(data)
        before = self.snapshot()
        self.assertIn("conflict", self.cli("migrate", self.workspace, expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_review_ready_plan_returns_to_draft(self) -> None:
        path = self.workspace / "business-plan.md"
        original = path.read_text(encoding="utf-8").replace("**Status:** draft", "**Status:** review-ready")
        path.write_text(original, encoding="utf-8")
        self.cli("migrate", self.workspace)
        self.assertIn("**Status:** draft", path.read_text(encoding="utf-8"))
        backup = next((self.workspace / ".migration-backups").iterdir())
        self.assertEqual((backup / "business-plan.md").read_text(encoding="utf-8"), original)

    @unittest.skipIf(os.name == "nt", "Symlinks can require elevated Windows privileges")
    def test_migration_does_not_follow_external_workbook_symlinks(self) -> None:
        external = self.root / "private.md"
        external.write_text("Preserve outside content.\n", encoding="utf-8")
        (self.workspace / "workbooks" / "getting-started-workbook.md").symlink_to(external)
        before_tasks = (self.workspace / "tasks.json").read_bytes()
        self.assertIn("symlink", self.cli("migrate", self.workspace, expected=1).stderr)
        self.assertEqual((self.workspace / "tasks.json").read_bytes(), before_tasks)
        self.assertEqual(external.read_text(encoding="utf-8"), "Preserve outside content.\n")


if __name__ == "__main__":
    unittest.main()
