from __future__ import annotations

import copy
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SCRIPT = ROOT / "scripts" / "venture.py"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")


class VentureTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="venture-harness-test-")
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.workspace = self.directory / "venture with spaces"
        self.run_cli("init", "--venture", 'A "quoted" venture', "--output", self.workspace)

    def run_cli(self, *arguments: object, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *(str(argument) for argument in arguments)],
            cwd=self.directory,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def load(self, filename: str) -> dict:
        return json.loads((self.workspace / filename).read_text(encoding="utf-8"))

    def save(self, filename: str, data: dict) -> None:
        (self.workspace / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def add_assumption(self) -> None:
        self.save("evidence.json", {
            "schema_version": 1,
            "claims": [{
                "id": "E-001",
                "type": "assumption",
                "statement": "Synthetic test assumption, not market evidence.",
                "source": "",
                "date": date.today().isoformat(),
                "confidence": "low",
                "contradictions": "No real research was performed for this test fixture.",
                "next_test": "A test owner must verify this before any real decision.",
            }],
        })

    def finish_fixture(self) -> None:
        self.add_assumption()
        (self.workspace / "raw" / "founder-discovery.md").write_text(
            "Synthetic founder confirmation for automated tests only.\n"
            "The test founder confirms the brief describes their intended venture.\n",
            encoding="utf-8",
        )
        for filename in ("brief.md", "business-plan.md", "progress.md"):
            path = self.workspace / filename
            content = path.read_text(encoding="utf-8").replace(
                "TODO", "Synthetic assumption E-001; test owner must verify before acting."
            )
            content = content.replace("**Status:** draft", "**Status:** review-ready")
            path.write_text(content, encoding="utf-8")
        data = self.load("tasks.json")
        for task in data["tasks"]:
            task.update(
                status="passing",
                evidence=["E-001"],
                owner="Test owner",
                reviewer="Synthetic reviewer",
                reviewed_on=date.today().isoformat(),
                verification="Automated structural fixture only, not an actual business review.",
            )
            if task["id"] == "business-plan":
                task["review_scores"] = {dimension: 2 for dimension in task["review_scores"]}
            if task["id"] == "venture-brief":
                task["discovery"] = {
                    "confirmed_by": "Synthetic founder",
                    "confirmed_on": date.today().isoformat(),
                    "confirmation_source": "raw/founder-discovery.md",
                }
        self.save("tasks.json", data)

    def test_initialization_preserves_names_and_creates_empty_state(self) -> None:
        self.assertEqual(self.load("tasks.json")["venture"], 'A "quoted" venture')
        self.assertEqual(self.load("evidence.json")["claims"], [])
        self.assertTrue((self.workspace / "raw").is_dir())
        self.assertTrue((self.workspace / "workbooks").is_dir())
        for filename in ("brief.md", "business-plan.md", "progress.md"):
            content = (self.workspace / filename).read_text(encoding="utf-8")
            self.assertIn('A "quoted" venture', content)
            self.assertNotIn("{DATE}", content)
            self.assertNotIn("{VENTURE_NAME}", content)

    def test_draft_pass_is_not_completion(self) -> None:
        result = self.run_cli("validate", self.workspace)
        self.assertIn("Draft structure valid: 0/6", result.stdout)
        result = self.run_cli("validate", self.workspace, "--final", expected=1)
        self.assertIn("unfinished", result.stderr)

    def test_initialization_never_overwrites(self) -> None:
        path = self.workspace / "brief.md"
        path.write_text("Keep this existing work.\n", encoding="utf-8")
        result = self.run_cli("init", "--venture", "Replacement", "--output", self.workspace, expected=1)
        self.assertIn("Refusing to overwrite", result.stderr)
        self.assertEqual(path.read_text(encoding="utf-8"), "Keep this existing work.\n")

    def test_initialization_rejects_empty_existing_directory(self) -> None:
        target = self.directory / "existing"
        target.mkdir()
        self.run_cli("init", "--venture", "Example", "--output", target, expected=1)
        self.assertEqual(list(target.iterdir()), [])

    def test_initialization_rejects_blank_or_multiline_names(self) -> None:
        for name in ("   ", "First\nSecond", "{VENTURE_NAME}"):
            with self.subTest(name=name):
                target = self.directory / "invalid"
                self.run_cli("init", "--venture", name, "--output", target, expected=1)
                self.assertFalse(target.exists())

    def test_bootstrap_works_outside_repository(self) -> None:
        result = subprocess.run(
            ["bash", str(ROOT / "init.sh"), "--venture", "Shell venture", "--output", "shell-output"],
            cwd=self.directory,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.directory / "shell-output" / "business-plan.md").is_file())

    def test_reviewed_fixture_passes_final(self) -> None:
        self.finish_fixture()
        result = self.run_cli("validate", self.workspace, "--final")
        self.assertIn("Review-ready structure valid: 6/6", result.stdout)
        self.assertIn("do not establish evidence truth", result.stdout)

    def test_discovery_confirmation_is_required_before_brief_passes(self) -> None:
        self.finish_fixture()
        data = self.load("tasks.json")
        del data["tasks"][0]["discovery"]
        self.save("tasks.json", data)
        for flags in ((), ("--final",)):
            with self.subTest(flags=flags):
                result = self.run_cli("validate", self.workspace, *flags, expected=1)
                self.assertIn("discovery", result.stderr)

    def test_discovery_requires_founder_date_and_confirmation_source(self) -> None:
        self.finish_fixture()
        original = self.load("tasks.json")
        cases = (
            ("confirmed_by", ""),
            ("confirmed_by", "TODO"),
            ("confirmed_by", True),
            ("confirmed_on", ""),
            ("confirmed_on", "not-a-date"),
            ("confirmed_on", (date.today() + timedelta(days=1)).isoformat()),
            ("confirmation_source", ""),
            ("confirmation_source", "raw/missing.md"),
            ("confirmation_source", "https://example.com/not-a-local-record"),
        )
        for key, value in cases:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(original)
                data["tasks"][0]["discovery"][key] = value
                self.save("tasks.json", data)
                self.run_cli("validate", self.workspace, expected=1)

    def test_discovery_record_cannot_be_empty_or_a_placeholder(self) -> None:
        self.finish_fixture()
        source = self.workspace / "raw" / "founder-discovery.md"
        for content in ("", "# Discovery\n<!-- Awaiting founder. -->\n", "TODO: ask the founder."):
            with self.subTest(content=content):
                source.write_text(content, encoding="utf-8")
                self.run_cli("validate", self.workspace, expected=1)

    def test_discovery_record_cannot_escape_workspace(self) -> None:
        self.finish_fixture()
        outside = self.directory / "confirmation.md"
        outside.write_text("Synthetic outside confirmation.\n", encoding="utf-8")
        source = self.workspace / "raw" / "founder-discovery.md"
        source.unlink()
        source.symlink_to(outside)
        self.assertIn("escapes", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_discovery_rejects_a_one_sentence_brief_with_empty_sections(self) -> None:
        self.finish_fixture()
        path = self.workspace / "brief.md"
        headings = re.findall(r"^## (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE)
        path.write_text(
            "# Venture Brief\n\n"
            + "\n\n".join(
                f"## {heading}\n" + ("I want to build an AI app.\n" if heading == "Venture thesis" else "")
                for heading in headings
            ),
            encoding="utf-8",
        )
        self.assertIn("empty section", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_discovery_rejects_an_unfinished_brief_before_downstream_work(self) -> None:
        self.finish_fixture()
        path = self.workspace / "brief.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nTODO: understand the founder.\n", encoding="utf-8")
        self.assertIn("unfinished", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_discovery_allows_legacy_drafts_to_resume_without_confirmation(self) -> None:
        data = self.load("tasks.json")
        data["tasks"][0].pop("discovery", None)
        data["tasks"][0]["status"] = "in_progress"
        self.save("tasks.json", data)
        result = self.run_cli("validate", self.workspace)
        self.assertIn("0/6 tasks passing", result.stdout)

    def test_discovery_unlocks_market_work_without_requiring_a_finished_plan(self) -> None:
        self.finish_fixture()
        data = self.load("tasks.json")
        data["tasks"][1]["status"] = "in_progress"
        for task in data["tasks"][2:]:
            task["status"] = "not_started"
        self.save("tasks.json", data)
        (self.workspace / "business-plan.md").write_text(
            (SKILLS / "create-business-plan" / "assets" / "workbook.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        self.assertIn("1/6 tasks passing", self.run_cli("validate", self.workspace).stdout)

    def test_missing_document_and_heading_fail(self) -> None:
        path = self.workspace / "brief.md"
        original = path.read_text(encoding="utf-8")
        path.unlink()
        self.assertIn("brief.md", self.run_cli("validate", self.workspace, expected=1).stderr)
        path.write_text(original.replace("## Venture thesis", "## Renamed"), encoding="utf-8")
        self.assertIn("Venture thesis", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_malformed_json_and_schema_versions_fail(self) -> None:
        original = self.load("tasks.json")
        (self.workspace / "tasks.json").write_text("{broken", encoding="utf-8")
        self.assertIn("invalid JSON", self.run_cli("validate", self.workspace, expected=1).stderr)
        for version in (True, 2, "1"):
            with self.subTest(version=version):
                changed = copy.deepcopy(original)
                changed["schema_version"] = version
                self.save("tasks.json", changed)
                self.assertIn("schema_version", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_duplicate_missing_and_weakened_starter_tasks_fail(self) -> None:
        original = self.load("tasks.json")
        duplicate = copy.deepcopy(original)
        duplicate["tasks"].append(copy.deepcopy(duplicate["tasks"][0]))
        missing = copy.deepcopy(original)
        missing["tasks"].pop()
        weakened = copy.deepcopy(original)
        weakened["tasks"][0]["acceptance"] = ["Declare success."]
        for changed, message in ((duplicate, "duplicate"), (missing, "Missing required"), (weakened, "retain")):
            with self.subTest(message=message):
                self.save("tasks.json", changed)
                self.assertIn(message, self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_only_one_task_may_be_active(self) -> None:
        data = self.load("tasks.json")
        data["tasks"][0]["status"] = "in_progress"
        data["tasks"][1]["status"] = "in_progress"
        self.save("tasks.json", data)
        self.assertIn("Only one", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_active_task_requires_passing_dependencies(self) -> None:
        data = self.load("tasks.json")
        data["tasks"][1]["status"] = "in_progress"
        self.save("tasks.json", data)
        self.assertIn("dependency", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_unknown_and_cyclic_dependencies_fail(self) -> None:
        original = self.load("tasks.json")
        for dependencies, message in ((["missing"], "unknown dependency"), (["followup"], "cycle")):
            with self.subTest(dependencies=dependencies):
                data = copy.deepcopy(original)
                extra = copy.deepcopy(data["tasks"][0])
                extra.update(id="followup", depends_on=dependencies)
                data["tasks"].append(extra)
                self.save("tasks.json", data)
                self.assertIn(message, self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_invalid_status_and_field_types_fail(self) -> None:
        original = self.load("tasks.json")
        for key, value in (("status", "done"), ("depends_on", "venture-brief"), ("skills", ["missing-skill"]), ("owner", 17)):
            with self.subTest(key=key):
                data = copy.deepcopy(original)
                data["tasks"][0][key] = value
                self.save("tasks.json", data)
                self.run_cli("validate", self.workspace, expected=1)

    def test_passing_requires_evidence_review_and_real_dates(self) -> None:
        self.finish_fixture()
        original = self.load("tasks.json")
        future = (date.today() + timedelta(days=1)).isoformat()
        cases = (
            ("evidence", []),
            ("reviewer", ""),
            ("verification", "TODO"),
            ("reviewed_on", "2026-02-30"),
            ("reviewed_on", future),
        )
        for key, value in cases:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(original)
                data["tasks"][0][key] = value
                self.save("tasks.json", data)
                self.run_cli("validate", self.workspace, expected=1)

    def test_passing_dependents_are_invalidated_by_unfinished_upstream(self) -> None:
        self.finish_fixture()
        data = self.load("tasks.json")
        data["tasks"][0]["status"] = "blocked"
        self.save("tasks.json", data)
        self.assertIn("dependency", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_unknown_evidence_references_fail(self) -> None:
        data = self.load("tasks.json")
        data["tasks"][0]["evidence"] = ["E-999"]
        self.save("tasks.json", data)
        self.assertIn("unknown evidence ID", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_plan_citations_must_exist(self) -> None:
        path = self.workspace / "business-plan.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nClaim E-999.\n", encoding="utf-8")
        self.assertIn("unknown evidence IDs", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_evidence_types_sources_and_assumption_tests_are_required(self) -> None:
        self.add_assumption()
        original = self.load("evidence.json")
        cases = (
            ("type", "opinion"),
            ("type", "fact"),
            ("confidence", "certain"),
            ("next_test", ""),
            ("date", "not-a-date"),
            ("source", "raw/missing.md"),
            ("source", "ftp://example.com/source"),
        )
        for key, value in cases:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(original)
                data["claims"][0][key] = value
                self.save("evidence.json", data)
                self.run_cli("validate", self.workspace, expected=1)

    def test_duplicate_evidence_ids_fail(self) -> None:
        self.add_assumption()
        data = self.load("evidence.json")
        data["claims"].append(copy.deepcopy(data["claims"][0]))
        self.save("evidence.json", data)
        self.assertIn("duplicate evidence ID", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_fact_can_reference_an_existing_local_source(self) -> None:
        self.add_assumption()
        source = self.workspace / "raw" / "synthetic-notes.md"
        source.write_text("Test fixture, not actual customer evidence.\n", encoding="utf-8")
        data = self.load("evidence.json")
        data["claims"][0].update(type="fact", source="raw/synthetic-notes.md")
        self.save("evidence.json", data)
        self.run_cli("validate", self.workspace)

    def test_local_sources_cannot_escape_workspace(self) -> None:
        self.add_assumption()
        outside = self.directory / "outside.md"
        outside.write_text("Synthetic outside file.\n", encoding="utf-8")
        (self.workspace / "raw" / "linked.md").symlink_to(outside)
        original = self.load("evidence.json")
        for source in ("../outside.md", str(outside), "raw/linked.md"):
            with self.subTest(source=source):
                data = copy.deepcopy(original)
                data["claims"][0]["source"] = source
                self.save("evidence.json", data)
                self.run_cli("validate", self.workspace, expected=1)

    def test_state_files_cannot_be_external_symlinks(self) -> None:
        for filename in ("evidence.json", "tasks.json"):
            with self.subTest(filename=filename):
                path = self.workspace / filename
                content = path.read_text(encoding="utf-8")
                outside = self.directory / filename
                outside.write_text(content, encoding="utf-8")
                path.unlink()
                path.symlink_to(outside)
                try:
                    self.run_cli("validate", self.workspace, expected=1)
                finally:
                    path.unlink()
                    path.write_text(content, encoding="utf-8")

    def test_additional_artifacts_cannot_escape_workspace(self) -> None:
        data = self.load("tasks.json")
        extra = copy.deepcopy(data["tasks"][0])
        extra.update(id="followup", artifacts=["../outside.md"])
        data["tasks"].append(extra)
        self.save("tasks.json", data)
        self.assertIn("escapes", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_final_rejects_empty_sections_and_draft_status(self) -> None:
        self.finish_fixture()
        path = self.workspace / "business-plan.md"
        original = path.read_text(encoding="utf-8")
        empty = re.sub(
            r"(## Problem and customer\n).*?(\n## Market opportunity)",
            r"\1\n<!-- No substantive content. -->\n\2",
            original,
            flags=re.DOTALL,
        )
        for content, message in ((empty, "empty section"), (original.replace("review-ready", "draft"), "review-ready")):
            with self.subTest(message=message):
                path.write_text(content, encoding="utf-8")
                self.assertIn(message, self.run_cli("validate", self.workspace, "--final", expected=1).stderr)

    def test_review_thresholds_are_enforced(self) -> None:
        self.finish_fixture()
        original = self.load("tasks.json")
        full = original["tasks"][-1]["review_scores"]
        cases = {
            "total-nine": dict(full, financial_reasoning=1, actionability=1, handoff_quality=1),
            "zero-score": dict(full, handoff_quality=0),
            "weak-evidence": dict(full, evidence_integrity=1),
            "boolean-score": dict(full, decision_fit=True),
            "unfinished-score": dict(full, decision_fit=None),
            "out-of-range": dict(full, decision_fit=3),
        }
        for label, scores in cases.items():
            with self.subTest(label=label):
                data = copy.deepcopy(original)
                data["tasks"][-1]["review_scores"] = scores
                self.save("tasks.json", data)
                self.run_cli("validate", self.workspace, "--final", expected=1)
        data = copy.deepcopy(original)
        data["tasks"][-1]["review_scores"] = dict(full, actionability=1, handoff_quality=1)
        self.save("tasks.json", data)
        self.run_cli("validate", self.workspace, "--final")

    def test_final_rejects_unfinished_tasks(self) -> None:
        self.finish_fixture()
        data = self.load("tasks.json")
        data["tasks"][-1]["status"] = "in_progress"
        self.save("tasks.json", data)
        self.assertIn("Unfinished tasks", self.run_cli("validate", self.workspace, "--final", expected=1).stderr)

    def test_chapter_validator_is_reused_in_draft_and_final_modes(self) -> None:
        self.finish_fixture()
        workbook = self.workspace / "workbooks" / "market-segmentation-workbook.md"
        result = subprocess.run(
            [sys.executable, str(SKILLS / "market-segmentation" / "scripts" / "create_workbook.py"),
             "--venture", "Synthetic fixture", "--output", str(workbook)],
            env=ENV, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.run_cli("validate", self.workspace)
        result = self.run_cli("validate", self.workspace, "--final", expected=1)
        self.assertIn("Chapter validation failed", result.stderr)
        workbook.write_text(
            workbook.read_text(encoding="utf-8").replace("TODO", "Synthetic test fixture only"),
            encoding="utf-8",
        )
        self.run_cli("validate", self.workspace, "--final")

    def test_unknown_workbooks_are_not_silently_ignored(self) -> None:
        path = self.workspace / "workbooks" / "unknown-workbook.md"
        path.write_text("# Unknown workbook\n", encoding="utf-8")
        self.assertIn("No chapter validator", self.run_cli("validate", self.workspace, expected=1).stderr)

    def test_nested_workbooks_are_validated(self) -> None:
        self.finish_fixture()
        path = self.workspace / "workbooks" / "research" / "getting-started-workbook.md"
        path.parent.mkdir()
        template = (SKILLS / "getting-started" / "assets" / "workbook.md").read_text(encoding="utf-8")
        path.write_text(
            template.replace("{VENTURE_NAME}", "Synthetic fixture").replace("{DATE}", date.today().isoformat()),
            encoding="utf-8",
        )
        self.run_cli("validate", self.workspace)
        self.assertIn("Chapter validation failed", self.run_cli("validate", self.workspace, "--final", expected=1).stderr)

    def test_final_rejects_other_workbook_placeholders(self) -> None:
        self.finish_fixture()
        path = self.workspace / "workbooks" / "getting-started-workbook.md"
        template = (SKILLS / "getting-started" / "assets" / "workbook.md").read_text(encoding="utf-8")
        template = template.replace("{VENTURE_NAME}", "Synthetic fixture").replace("{DATE}", date.today().isoformat())
        for placeholder in ("TBD", "FIXME"):
            with self.subTest(placeholder=placeholder):
                path.write_text(template.replace("TODO", placeholder), encoding="utf-8")
                self.run_cli("validate", self.workspace, "--final", expected=1)


class RepositoryTests(unittest.TestCase):
    def test_every_skill_is_routed(self) -> None:
        data = json.loads((ROOT / "templates" / "tasks.json").read_text(encoding="utf-8"))
        routed = {skill for task in data["tasks"] for skill in task["skills"]}
        available = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
        self.assertEqual(len(available), 26)
        self.assertEqual(list(ROOT.glob("*/SKILL.md")), [])
        self.assertEqual(routed, available)

    def test_agent_adapters_reference_canonical_instructions(self) -> None:
        self.assertIn("@AGENTS.md", (ROOT / "CLAUDE.md").read_text(encoding="utf-8"))
        copilot = (ROOT / ".github" / "copilot-instructions.md").read_text(encoding="utf-8")
        self.assertIn("../AGENTS.md", copilot)

    def test_local_documentation_links_resolve(self) -> None:
        documents = [
            ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "CLAUDE.md",
            ROOT / ".github" / "copilot-instructions.md",
            ROOT / "docs" / "harness.md",
            *sorted(SKILLS.rglob("*.md")),
        ]
        for document in documents:
            content = document.read_text(encoding="utf-8")
            targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)|(?:href|src)=\"([^\"]+)\"", content)
            for markdown, html in targets:
                target = markdown or html
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                with self.subTest(document=document.name, target=target):
                    path = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
                    self.assertTrue(path.exists(), f"{document}: missing target {target}")
                    if parsed.fragment and path.suffix == ".md":
                        headings = re.findall(r"^#{1,6} (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE)
                        anchors = {
                            re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
                            for heading in headings
                        }
                        self.assertIn(parsed.fragment, anchors)

    def test_all_existing_chapter_workflows_still_work(self) -> None:
        creators = sorted(SKILLS.glob("*/scripts/create_workbook.py"))
        self.assertEqual(len(creators), 25)
        with tempfile.TemporaryDirectory(prefix="venture-chapter-test-") as temporary:
            for creator in creators:
                with self.subTest(skill=creator.parent.parent.name):
                    workbook = Path(temporary) / f"{creator.parent.parent.name}.md"
                    create = subprocess.run(
                        [sys.executable, str(creator), "--venture", "Regression fixture", "--output", str(workbook)],
                        env=ENV, capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(create.returncode, 0, create.stdout + create.stderr)
                    validator = creator.with_name("validate_workbook.py")
                    for flags, expected in ((["--allow-todo"], 0), ([], 1)):
                        result = subprocess.run(
                            [sys.executable, str(validator), str(workbook), *flags],
                            env=ENV, capture_output=True, text=True, check=False,
                        )
                        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
