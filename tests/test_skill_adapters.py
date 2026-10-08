from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
LOCATIONS = (".agents/skills", ".claude/skills")


class SkillAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="venture-adapters-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        (self.root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts" / "sync_skills.py", self.root / "scripts" / "sync_skills.py")
        self.add_skill("example")

    def add_skill(self, name: str, description: str = "A synthetic skill for adapter tests.") -> None:
        directory = self.root / "skills" / name
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: "{description}"\nlicense: MIT\n---\n\n'
            "# Synthetic workflow\n\nThe body must remain in the canonical file only.\n",
            encoding="utf-8",
        )

    def run_sync(self, *arguments: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts" / "sync_skills.py"), *arguments],
            cwd=self.root.parent,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def snapshot(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}

    def test_missing_adapters_fail_check_without_writing(self) -> None:
        before = self.snapshot()
        self.assertIn("Missing adapter", self.run_sync("--check", expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_generates_portable_adapters_without_copying_the_body(self) -> None:
        self.run_sync()
        for location in LOCATIONS:
            path = self.root / location / "example" / "SKILL.md"
            content = path.read_text(encoding="utf-8")
            self.assertFalse(path.is_symlink())
            self.assertIn("name: example", content)
            self.assertIn('description: "A synthetic skill for adapter tests."', content)
            self.assertNotIn("The body must remain", content)
            self.assertIn("not in this adapter directory", content)
            target = re.search(r"\[canonical skill\]\(([^)]+)\)", content)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual((path.parent / target.group(1)).resolve(), self.root / "skills" / "example" / "SKILL.md")
        self.run_sync("--check")

    def test_synchronization_is_idempotent(self) -> None:
        self.run_sync()
        before = self.snapshot()
        modified = {path: (self.root / path).stat().st_mtime_ns for path in before}
        self.run_sync()
        self.run_sync("--check")
        self.assertEqual(self.snapshot(), before)
        self.assertEqual({path: (self.root / path).stat().st_mtime_ns for path in before}, modified)

    def test_crlf_checkout_line_endings_do_not_look_like_local_edits(self) -> None:
        self.run_sync()
        for location in LOCATIONS:
            path = self.root / location / "example" / "SKILL.md"
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        before = self.snapshot()
        self.run_sync("--check")
        self.run_sync()
        self.assertEqual(self.snapshot(), before)

    def test_metadata_changes_require_refresh(self) -> None:
        self.run_sync()
        path = self.root / "skills" / "example" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("A synthetic skill", "An updated skill"), encoding="utf-8")
        self.assertIn("Stale adapter", self.run_sync("--check", expected=1).stderr)
        self.run_sync()
        self.run_sync("--check")

    def test_body_changes_do_not_require_duplicate_updates(self) -> None:
        self.run_sync()
        path = self.root / "skills" / "example" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nAnother canonical instruction.\n", encoding="utf-8")
        self.run_sync("--check")

    def test_addition_and_removal_refresh_only_managed_files(self) -> None:
        self.run_sync()
        notes = self.root / ".claude" / "skills" / "example" / "notes.txt"
        notes.write_text("Preserve unrelated notes.\n", encoding="utf-8")
        self.add_skill("replacement")
        (self.root / "skills" / "example" / "SKILL.md").unlink()
        self.run_sync("--check", expected=1)
        self.run_sync()
        self.assertEqual(notes.read_text(encoding="utf-8"), "Preserve unrelated notes.\n")
        for location in LOCATIONS:
            self.assertFalse((self.root / location / "example" / "SKILL.md").exists())
            self.assertTrue((self.root / location / "replacement" / "SKILL.md").is_file())
        self.run_sync("--check")

    def test_unrelated_skills_are_preserved(self) -> None:
        path = self.root / ".agents" / "skills" / "custom" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("User-owned skill.\n", encoding="utf-8")
        self.run_sync()
        self.run_sync("--check")
        self.assertEqual(path.read_text(encoding="utf-8"), "User-owned skill.\n")

    def test_collision_is_reported_before_any_write(self) -> None:
        path = self.root / ".claude" / "skills" / "example" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("User-owned conflicting skill.\n", encoding="utf-8")
        before = self.snapshot()
        self.assertIn("Unmanaged file", self.run_sync(expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_non_directory_parent_fails_before_any_write(self) -> None:
        (self.root / ".claude").write_text("Unrelated file.\n", encoding="utf-8")
        before = self.snapshot()
        self.assertIn("directory", self.run_sync(expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_local_adapter_edits_are_not_overwritten_or_deleted(self) -> None:
        self.run_sync()
        path = self.root / ".agents" / "skills" / "example" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nA local edit.\n", encoding="utf-8")
        before = self.snapshot()
        self.assertIn("local edits", self.run_sync(expected=1).stderr)
        self.assertEqual(self.snapshot(), before)
        self.add_skill("replacement")
        (self.root / "skills" / "example" / "SKILL.md").unlink()
        self.assertIn("local edits", self.run_sync(expected=1).stderr)
        self.assertIn("A local edit.", path.read_text(encoding="utf-8"))

    def test_missing_managed_adapter_can_be_restored(self) -> None:
        self.run_sync()
        (self.root / ".agents" / "skills" / "example" / "SKILL.md").unlink()
        self.run_sync("--check", expected=1)
        self.run_sync()
        self.run_sync("--check")

    def test_empty_canonical_tree_never_removes_adapters(self) -> None:
        self.run_sync()
        (self.root / "skills" / "example" / "SKILL.md").unlink()
        before = self.snapshot()
        self.assertIn("No canonical skills", self.run_sync(expected=1).stderr)
        self.assertEqual(self.snapshot(), before)

    def test_invalid_metadata_fails_before_writing(self) -> None:
        path = self.root / "skills" / "example" / "SKILL.md"
        original = path.read_text(encoding="utf-8")
        for content in (
            "# Missing metadata\n",
            original.replace("name: example", "name: wrong-name"),
            original.replace('"A synthetic skill for adapter tests."', '""'),
            original.replace('"A synthetic skill for adapter tests."', ""),
        ):
            with self.subTest(content=content):
                path.write_text(content, encoding="utf-8")
                before = self.snapshot()
                self.run_sync(expected=1)
                self.assertEqual(self.snapshot(), before)

    def test_manifest_cannot_manage_arbitrary_files(self) -> None:
        self.run_sync()
        path = self.root / ".agents" / "skill-adapters.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["files"]["../outside.txt"] = "0" * 64
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("invalid managed path", self.run_sync(expected=1).stderr)

    @unittest.skipIf(os.name == "nt", "Symlink creation may require elevated Windows privileges")
    def test_symlinked_adapter_directories_are_not_followed(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / ".agents").symlink_to(outside, target_is_directory=True)
        self.assertIn("symlink", self.run_sync(expected=1).stderr)
        self.assertEqual(list(outside.iterdir()), [])


class RepositoryAdapterTests(unittest.TestCase):
    def test_checked_in_adapters_are_current(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "sync_skills.py"), "--check"],
            env=ENV, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("52 adapters for 26 canonical skills", result.stdout)


if __name__ == "__main__":
    unittest.main()
