from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.skill_contracts import CONTRACTS
from scripts.workbook_runtime import empty_record, extract_record, render_record, validate_record


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")


class WorkbookTests(unittest.TestCase):
    def example(self, skill: str) -> dict:
        return extract_record((SKILLS / skill / "references" / "example.md").read_text(encoding="utf-8"))

    def validate(self, skill: str, record: dict, **options: object) -> str:
        return validate_record(record, dict(CONTRACTS[skill]), SKILLS / skill / "references" / "example.md", **options)

    def test_every_worked_example_passes_its_own_contract(self) -> None:
        self.assertEqual(len(CONTRACTS), 27)
        for skill in CONTRACTS:
            with self.subTest(skill=skill):
                self.assertEqual(self.validate(skill, self.example(skill), allow_example=True), "completed-analysis")

    def test_examples_are_never_accepted_as_actual_venture_evidence(self) -> None:
        for skill in CONTRACTS:
            with self.subTest(skill=skill), self.assertRaisesRegex(ValueError, "Synthetic"):
                self.validate(skill, self.example(skill))

    def test_all_analysis_tables_require_rows(self) -> None:
        for skill, contract in CONTRACTS.items():
            for table in contract["tables"]:
                with self.subTest(skill=skill, table=table), self.assertRaisesRegex(ValueError, "at least one row"):
                    record = self.example(skill)
                    record["data"][table] = []
                    self.validate(skill, record, allow_example=True)

    def test_every_declared_column_is_required(self) -> None:
        for skill, contract in CONTRACTS.items():
            for table, columns in contract["tables"].items():
                for column in columns:
                    with self.subTest(skill=skill, table=table, column=column), self.assertRaisesRegex(ValueError, "expected fields"):
                        record = self.example(skill)
                        del record["data"][table][0][column]
                        self.validate(skill, record, allow_example=True)

    def test_unverified_substitution_cannot_complete_an_ltv_workbook(self) -> None:
        record = empty_record(dict(CONTRACTS["calculate-customer-lifetime-value"]), "Synthetic test")
        record = json.loads(json.dumps(record).replace("TODO", "Unverified"))
        record["stage"] = "completed-analysis"
        with self.assertRaisesRegex(ValueError, "unfinished"):
            self.validate("calculate-customer-lifetime-value", record)

    def test_drafts_are_explicitly_incomplete(self) -> None:
        for skill in CONTRACTS:
            record = empty_record(dict(CONTRACTS[skill]), "Test venture")
            with self.subTest(skill=skill):
                with self.assertRaisesRegex(ValueError, "Draft is unfinished"):
                    self.validate(skill, record)
                self.assertEqual(self.validate(skill, record, allow_draft=True), "draft")

    def test_research_plan_is_valid_without_inventing_results(self) -> None:
        for skill in CONTRACTS:
            with self.subTest(skill=skill):
                record = self.example(skill)
                record.update(stage="research-plan", synthetic=False, evidence=[])
                record["data"] = {table: [] for table in record["data"]}
                record["research_plan"] = [{
                    "question": "Will the customer approve a paid pilot?",
                    "population": "Five qualified practice owners",
                    "method": "Authorized proposal test",
                    "metric": "Number accepting the bounded proposal",
                    "threshold": "At least two of five",
                    "owner": "Founder", "due_date": "2026-12-01",
                }]
                self.assertEqual(self.validate(skill, record), "research-plan")
                record["data"] = self.example(skill)["data"]
                with self.assertRaisesRegex(ValueError, "must not mix"):
                    self.validate(skill, record)

    def test_analysis_cannot_use_a_recruiting_plan_in_place_of_observations(self) -> None:
        record = self.example("validate-with-customers")
        record["evidence"][0].update(type="assumption", next_test="Recruit three independent target customers")
        with self.assertRaisesRegex(ValueError, "requires sourced observations"):
            self.validate("validate-with-customers", record, allow_example=True)

    def test_an_unused_fact_cannot_launder_assumption_only_observation_rows(self) -> None:
        record = self.example("validate-with-customers")
        assumption = copy.deepcopy(record["evidence"][0])
        assumption.update(id="E-002", type="assumption", next_test="Interview the participant after obtaining consent.")
        record["evidence"].append(assumption)
        record["data"]["participants"][0]["evidence"] = ["E-002"]
        with self.assertRaisesRegex(ValueError, "each observed-result row"):
            self.validate("validate-with-customers", record, allow_example=True)

    def test_unknown_duplicate_or_missing_evidence_is_rejected(self) -> None:
        skill = "calculate-customer-lifetime-value"
        for mutation in ("unknown", "duplicate", "source"):
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                record = self.example(skill)
                if mutation == "unknown":
                    record["data"]["cashflows"][0]["evidence"] = ["E-999"]
                elif mutation == "duplicate":
                    record["evidence"].append(copy.deepcopy(record["evidence"][0]))
                else:
                    record["evidence"][0]["source"] = ""
                self.validate(skill, record, allow_example=True)

    def test_every_numeric_model_detects_wrong_output(self) -> None:
        cases = (
            ("calculate-beachhead-market-tam", "markets", "annual_tam"),
            ("calculate-follow-on-markets-tam", "markets", "annual_tam"),
            ("calculate-customer-acquisition-cost", "acquisition", "cac"),
            ("calculate-customer-lifetime-value", "cashflows", "discounted_contribution"),
            ("quantify-the-value-proposition", "outcomes", "realized_value"),
            ("plan-operations", "capacity", "gap_hours"),
            ("build-financial-plan", "cashflow", "closing_cash"),
            ("identify-key-assumptions", "assumptions", "risk_score"),
            ("select-a-beachhead-market", "scorecard", "weighted_score"),
        )
        for skill, table, column in cases:
            with self.subTest(skill=skill), self.assertRaises(ValueError):
                record = self.example(skill)
                record["data"][table][0][column] += 1
                self.validate(skill, record, allow_example=True)

    def test_numeric_types_and_ranges_are_enforced(self) -> None:
        skill = "calculate-customer-lifetime-value"
        for value in (True, "0.5", -0.1, 1.1, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                record = self.example(skill)
                record["data"]["cashflows"][0]["retention"] = value
                self.validate(skill, record, allow_example=True)

    def test_required_scenarios_and_periods_cannot_be_omitted(self) -> None:
        for skill, table in (("calculate-customer-lifetime-value", "cashflows"), ("build-financial-plan", "cashflow")):
            with self.subTest(skill=skill):
                record = self.example(skill)
                record["data"][table].pop()
                with self.assertRaisesRegex(ValueError, "periods"):
                    self.validate(skill, record, allow_example=True)
                record = self.example(skill)
                record["data"][table] = [row for row in record["data"][table] if row["scenario"] != "upside"]
                with self.assertRaisesRegex(ValueError, "scenarios"):
                    self.validate(skill, record, allow_example=True)

    def test_cash_continuity_and_funding_summary_are_checked(self) -> None:
        for table, field in (("cashflow", "opening_cash"), ("summary", "additional_funding_needed"), ("summary", "first_negative_month")):
            with self.subTest(field=field), self.assertRaises(ValueError):
                record = self.example("build-financial-plan")
                record["data"][table][0][field] += 1
                self.validate("build-financial-plan", record, allow_example=True)

    def test_customer_sample_shortfall_must_be_inconclusive(self) -> None:
        record = self.example("validate-with-customers")
        record["data"]["synthesis"][0]["decision"] = "proceed"
        with self.assertRaisesRegex(ValueError, "inconclusive"):
            self.validate("validate-with-customers", record, allow_example=True)

    def test_experiment_verdict_and_precommitment_are_checked(self) -> None:
        skill = "test-key-assumptions"
        record = self.example(skill)
        record["data"]["results"][0]["outcome"] = "pass"
        with self.assertRaisesRegex(ValueError, "threshold"):
            self.validate(skill, record, allow_example=True)
        record = self.example(skill)
        record["data"]["experiments"][0]["precommitted_on"] = "2026-01-09"
        with self.assertRaisesRegex(ValueError, "Precommitment"):
            self.validate(skill, record, allow_example=True)

    def test_funnel_rates_cannot_change_denominator(self) -> None:
        for skill, table, field in (("map-the-sales-process", "sales_stages", "conversion_rate"), ("validate-customer-traction", "cohorts", "retention_rate")):
            with self.subTest(skill=skill), self.assertRaises(ValueError):
                record = self.example(skill)
                record["data"][table][0][field] = 0.9
                self.validate(skill, record, allow_example=True)

    def test_local_evidence_matches_workspace_by_resolved_path(self) -> None:
        with tempfile.TemporaryDirectory(prefix="venture-source-test-") as temporary:
            workspace = Path(temporary)
            (workspace / "raw").mkdir()
            (workspace / "workbooks").mkdir()
            (workspace / "raw" / "notes.txt").write_text("Synthetic test notes.\n", encoding="utf-8")
            record = self.example("validate-with-customers")
            record["evidence"][0]["source"] = "../raw/notes.txt"
            registered = copy.deepcopy(record["evidence"][0])
            registered["source"] = "raw/notes.txt"
            (workspace / "evidence.json").write_text(json.dumps({"schema_version": 1, "claims": [registered]}), encoding="utf-8")
            path = workspace / "workbooks" / "validation.md"
            validate_record(record, dict(CONTRACTS["validate-with-customers"]), path, allow_example=True, workspace=workspace)
            registered["statement"] = "Conflicting evidence must not silently replace the workbook claim."
            (workspace / "evidence.json").write_text(json.dumps({"schema_version": 1, "claims": [registered]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "match the workspace"):
                validate_record(record, dict(CONTRACTS["validate-with-customers"]), path, allow_example=True, workspace=workspace)

    def test_standalone_package_needs_no_repository_runtime(self) -> None:
        with tempfile.TemporaryDirectory(prefix="venture-standalone-") as temporary:
            root = Path(temporary)
            skill = root / "calculate-customer-lifetime-value"
            shutil.copytree(SKILLS / skill.name, skill)
            output = root / "working.md"
            result = subprocess.run(
                [sys.executable, str(skill / "scripts" / "create_workbook.py"), "--venture", "Standalone test", "--output", str(output)],
                cwd=root, env=ENV, capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            for target, flags, expected in (
                (output, ["--allow-todo"], 0),
                (output, [], 1),
                (skill / "references" / "example.md", ["--allow-example"], 0),
            ):
                result = subprocess.run(
                    [sys.executable, str(skill / "scripts" / "validate_workbook.py"), str(target), *flags],
                    cwd=root, env=ENV, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)

    def test_record_round_trip_preserves_escaped_venture_names(self) -> None:
        record = empty_record(dict(CONTRACTS["plan-operations"]), 'Owner "A" & team')
        self.assertEqual(extract_record(render_record(record, "Plan")), record)

    def test_generated_packages_are_current(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_workbooks.py"), "--check"],
            env=ENV, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
