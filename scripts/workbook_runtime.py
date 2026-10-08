"""Shared authoring source, bundled into each standalone skill by build_workbooks.py."""

from __future__ import annotations

import argparse
from datetime import date
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


STAGES = ("draft", "research-plan", "completed-analysis")
SCENARIOS = ("conservative", "base", "upside")
PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\{(?:VENTURE_NAME|DATE)\}", re.IGNORECASE)
EMPTY_ANSWERS = {"unverified", "unknown", "n/a", "none", "tbc"}
RECORD = re.compile(r"<!-- venture-record:start -->\s*```json\s*\n(.*?)\n```\s*<!-- venture-record:end -->", re.DOTALL)
PLAN_COLUMNS = {
    "question": "text", "population": "text", "method": "text",
    "metric": "text", "threshold": "text", "owner": "text", "due_date": "date",
}
ACTION_COLUMNS = {"action": "text", "owner": "text", "due_date": "date", "evidence_expected": "text"}


def object_value(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise ValueError(f"{label}: expected an object")
    return dict(value)


def rows(value: object, label: str) -> list[dict[str, object]]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected an array")
    return [object_value(item, f"{label}[{index + 1}]") for index, item in enumerate(value)]


def string(value: object, label: str, complete: bool = True) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label}: expected text")
    if complete and (
        not value.strip() or PLACEHOLDERS.search(value) or value.strip().lower() in EMPTY_ANSWERS
    ):
        raise ValueError(f"{label}: unfinished or unsupported answer; provide a specific answer or a scoped uncertainty and next test")
    return value


def number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label}: expected a finite number")
    return float(value)


def iso_date(value: object, label: str, recorded: bool = False) -> str:
    result = string(value, label)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", result):
        raise ValueError(f"{label}: expected YYYY-MM-DD")
    parsed = date.fromisoformat(result)
    if recorded and parsed > date.today():
        raise ValueError(f"{label}: recorded dates cannot be in the future")
    return result


def load_contract(skill_root: Path) -> dict[str, object]:
    return object_value(json.loads((skill_root / "assets" / "contract.json").read_text(encoding="utf-8")), "contract")


def extract_record(content: str) -> dict[str, object]:
    matches = list(RECORD.finditer(content))
    if len(matches) != 1:
        raise ValueError("Expected one structured workbook record; use venture.py migrate for a legacy workspace")
    return object_value(json.loads(matches[0].group(1)), "workbook record")


def render_record(record: dict[str, object], title: str, contract: dict[str, object] | None = None) -> str:
    result = (
        f"# {title}\n\n"
        "The structured record is the source for the decision below. "
        "Do not replace missing research with invented results.\n\n"
        "<!-- venture-record:start -->\n```json\n"
        + json.dumps(record, indent=2, ensure_ascii=False)
        + "\n```\n<!-- venture-record:end -->\n"
    )
    if contract is not None:
        result += "\n## Output fields\n\nEach data table is an array of row objects. Every analysis row cites evidence IDs.\n"
        for name, value in object_value(contract["tables"], "tables").items():
            result += f"\n### {name}\n\n| Field | Type |\n|---|---|\n"
            result += "".join(f"| `{key}` | {kind} |\n" for key, kind in object_value(value, name).items())
        result += (
            "\n## Stage rules\n\n"
            "- `draft`: unfinished work; validate with `--allow-todo`.\n"
            "- `research-plan`: leave result tables empty; complete the research protocol and next actions.\n"
            "- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.\n"
            "\nA research-plan row needs question, population, method, metric, threshold, owner, and due_date.\n"
            "A next-action row needs action, owner, due_date, and evidence_expected.\n"
            "Read the bundled record-format reference for evidence fields and a complete worked example.\n"
        )
    return result


def empty_record(contract: dict[str, object], venture: str, stage: str = "draft") -> dict[str, object]:
    scope = object_value(contract["scope"], "contract.scope")
    tables = object_value(contract["tables"], "contract.tables")
    return {
        "schema_version": 2, "skill": contract["skill"], "stage": stage,
        "synthetic": False, "venture": venture, "owner": "TODO", "date": date.today().isoformat(),
        "scope": {key: "TODO" for key in scope},
        "evidence": [], "data": {key: [] for key in tables}, "research_plan": [],
        "decision": "TODO", "limitations": "TODO", "next_actions": [],
    }


def evidence_records(
    value: object, workbook: Path, workspace: Path | None, complete: bool
) -> dict[str, dict[str, object]]:
    found: dict[str, dict[str, object]] = {}
    for entry in rows(value, "evidence"):
        key = string(entry.get("id"), "evidence.id")
        if not re.fullmatch(r"E-\d{3,}", key) or key in found:
            raise ValueError(f"Invalid or duplicate evidence ID: {key}")
        kind = string(entry.get("type"), f"{key}.type")
        if kind not in {"fact", "inference", "assumption"}:
            raise ValueError(f"{key}: type must be fact, inference, or assumption")
        for field in ("statement", "contradictions"):
            string(entry.get(field), f"{key}.{field}", complete)
        iso_date(entry.get("date"), f"{key}.date", recorded=True)
        if entry.get("confidence") not in ("low", "medium", "high"):
            raise ValueError(f"{key}: invalid confidence")
        source = string(entry.get("source"), f"{key}.source", complete=False)
        next_test = string(entry.get("next_test"), f"{key}.next_test", complete=False)
        if kind == "assumption":
            string(next_test, f"{key}.next_test", complete)
        elif not source.strip():
            raise ValueError(f"{key}: facts and inferences require a source")
        if source:
            string(source, f"{key}.source", complete)
            parsed = urlsplit(source)
            if parsed.scheme:
                if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username is not None:
                    raise ValueError(f"{key}: source must be HTTP(S) without credentials or a local file")
            else:
                target = (workbook.parent / source).resolve()
                if workspace is not None:
                    try:
                        target.relative_to(workspace.resolve())
                    except ValueError as error:
                        raise ValueError(f"{key}: source escapes the workspace") from error
                if not target.is_file():
                    raise ValueError(f"{key}: source file does not exist: {source}")
        found[key] = entry
    if workspace is not None and found:
        register = object_value(json.loads((workspace / "evidence.json").read_text(encoding="utf-8")), "workspace evidence")
        global_claims = {string(entry.get("id"), "workspace claim ID"): entry for entry in rows(register.get("claims"), "workspace claims")}
        for key, entry in found.items():
            registered = global_claims.get(key)
            if registered is None:
                raise ValueError(f"{key}: not present in the workspace evidence register")
            local_claim = dict(entry)
            global_claim = dict(registered)
            for claim, base in ((local_claim, workbook.parent), (global_claim, workspace)):
                source = string(claim.get("source"), f"{key}.source", complete=False)
                if source and not urlsplit(source).scheme:
                    claim["source"] = str((base / source).resolve())
            if global_claim != local_claim:
                raise ValueError(f"{key}: workbook evidence must match the workspace register exactly")
    return found


def field(value: object, kind: str, label: str, evidence: dict[str, dict[str, object]], complete: bool) -> None:
    if not complete and isinstance(value, str) and PLACEHOLDERS.search(value):
        return
    if kind == "text":
        string(value, label, complete)
    elif kind == "date":
        iso_date(value, label)
    elif kind == "currency":
        if not re.fullmatch(r"[A-Z]{3}", string(value, label, complete)):
            raise ValueError(f"{label}: use a three-letter currency code")
    elif kind == "evidence":
        if not isinstance(value, list) or not value or not all(isinstance(key, str) for key in value):
            raise ValueError(f"{label}: cite at least one evidence ID")
        if len(set(value)) != len(value) or any(key not in evidence for key in value):
            raise ValueError(f"{label}: duplicate or unknown evidence ID")
    elif kind.startswith("choice:"):
        if value not in kind.removeprefix("choice:").split(","):
            raise ValueError(f"{label}: expected one of {kind.removeprefix('choice:')}")
    else:
        numeric = number(value, label)
        if kind in ("nonnegative", "nonnegative_integer", "probability") and numeric < 0:
            raise ValueError(f"{label}: must be nonnegative")
        if kind in ("positive", "positive_integer") and numeric <= 0:
            raise ValueError(f"{label}: must be positive")
        if kind in ("integer", "positive_integer", "nonnegative_integer") and type(value) is not int:
            raise ValueError(f"{label}: expected an integer")
        if kind == "probability" and numeric > 1:
            raise ValueError(f"{label}: probability must be between 0 and 1")
        if kind not in ("number", "nonnegative", "positive", "integer", "positive_integer", "nonnegative_integer", "probability"):
            raise ValueError(f"{label}: unsupported contract type {kind}")


def fields(
    data: dict[str, object], columns: dict[str, object], label: str,
    evidence: dict[str, dict[str, object]], complete: bool,
) -> None:
    if set(data) != set(columns):
        raise ValueError(f"{label}: expected fields {', '.join(columns)}")
    for key, kind in columns.items():
        field(data[key], string(kind, "contract type"), f"{label}.{key}", evidence, complete)


def equal(actual: object, expected: float, label: str) -> None:
    if not math.isclose(number(actual, label), expected, rel_tol=1e-6, abs_tol=0.01):
        raise ValueError(f"{label}: expected {expected:.6g}, got {actual}")


def scenario_rows(data: list[dict[str, object]], label: str) -> None:
    if {entry.get("scenario") for entry in data} != set(SCENARIOS):
        raise ValueError(f"{label}: include conservative, base, and upside scenarios")


def ordered_periods(data: list[dict[str, object]], horizon: int, label: str, period: str) -> list[dict[str, object]]:
    if len(data) != horizon or sorted(number(entry[period], period) for entry in data) != list(range(1, horizon + 1)):
        raise ValueError(f"{label}: periods must cover 1..{horizon} exactly once")
    return sorted(data, key=lambda entry: number(entry[period], period))


def check_calculations(skill: str, scope: dict[str, object], data: dict[str, list[dict[str, object]]]) -> None:
    if skill == "select-a-beachhead-market":
        if len(data["selection"]) != 1:
            raise ValueError("Select exactly one beachhead")
        candidates = {string(row["candidate"], "candidate") for row in data["scorecard"]}
        for candidate in candidates:
            candidate_rows = [row for row in data["scorecard"] if row["candidate"] == candidate]
            equal(sum(number(row["weight"], "weight") for row in candidate_rows), 1, "criterion weights")
        for row in data["scorecard"]:
            equal(row["weighted_score"], number(row["weight"], "weight") * number(row["score"], "score"), "weighted_score")
        if data["selection"][0]["chosen_segment"] not in candidates:
            raise ValueError("The chosen segment must appear in the scorecard")
    elif skill == "profile-the-persona":
        ranks = [number(row["rank"], "rank") for row in data["purchasing_criteria"]]
        if sorted(ranks) != list(range(1, len(ranks) + 1)):
            raise ValueError("Purchasing criteria must have distinct consecutive ranks")
    elif skill == "map-customer-journey":
        if {row["state"] for row in data["journey"]} != {"current", "proposed"}:
            raise ValueError("Include both current and proposed customer journeys")
    elif skill == "validate-with-customers":
        participants = data["participants"]
        identities = [string(row["participant_id"], "participant_id") for row in participants]
        if len(set(identities)) != len(identities) or len(data["synthesis"]) != 1:
            raise ValueError("Use unique participants and one cross-customer synthesis")
        summary = data["synthesis"][0]
        equal(summary["observed_sample"], len(participants), "observed_sample")
        if len(participants) < number(scope["target_sample"], "target_sample") and summary["decision"] != "inconclusive":
            raise ValueError("A sample below the target must be reported as inconclusive")
    elif skill == "chart-your-competitive-position":
        if len(data["axes"]) != 2 or {row["axis"] for row in data["axes"]} != {"x", "y"}:
            raise ValueError("Define exactly one x axis and one y axis")
        if not any(row["kind"] == "status-quo" for row in data["alternatives"]):
            raise ValueError("Include the customer's status quo")
    elif skill == "map-the-sales-process":
        for row in data["sales_stages"]:
            entered = number(row["entered"], "entered")
            converted = number(row["converted"], "converted")
            if entered <= 0 or converted > entered:
                raise ValueError("Conversion requires positive entries and converted <= entered")
            equal(row["conversion_rate"], converted / entered, "conversion_rate")
    elif skill == "design-a-business-model":
        if len(data["selection"]) != 1 or data["selection"][0]["chosen_model"] not in {row["model"] for row in data["models"]}:
            raise ValueError("Select one of the documented business models")
    elif skill == "identify-key-assumptions":
        identities = [string(row["id"], "assumption id") for row in data["assumptions"]]
        if len(set(identities)) != len(identities):
            raise ValueError("Assumption IDs must be unique")
        for row in data["assumptions"]:
            impact = number(row["impact"], "impact")
            uncertainty = number(row["uncertainty"], "uncertainty")
            if impact > 5 or uncertainty > 5:
                raise ValueError("Impact and uncertainty use a 1-5 scale")
            equal(row["risk_score"], impact * uncertainty, "risk_score")
        if any(row["assumption_id"] not in identities for row in data["test_queue"]):
            raise ValueError("Test queue references an unknown assumption")
    elif skill == "test-key-assumptions":
        experiments = {string(row["id"], "experiment id"): row for row in data["experiments"]}
        if len(experiments) != len(data["experiments"]):
            raise ValueError("Experiment IDs must be unique")
        results = data["results"]
        if {row["experiment_id"] for row in results} != set(experiments) or len(results) != len(experiments):
            raise ValueError("Each experiment needs exactly one result")
        for result in results:
            experiment = experiments[string(result["experiment_id"], "experiment_id")]
            precommitted = iso_date(experiment["precommitted_on"], "precommitted_on", recorded=True)
            observed = iso_date(experiment["observed_on"], "observed_on", recorded=True)
            if precommitted > observed:
                raise ValueError("Precommitment must precede observations")
            actual = number(result["observed_value"], "observed_value")
            threshold = number(experiment["threshold"], "threshold")
            passed = actual >= threshold if experiment["comparison"] == "at-least" else actual <= threshold
            if result["outcome"] != ("pass" if passed else "fail"):
                raise ValueError("Experiment outcome contradicts the precommitted threshold")
    elif skill == "validate-customer-traction":
        for row in data["cohorts"]:
            acquired = number(row["acquired"], "acquired")
            activated = number(row["activated"], "activated")
            if activated > acquired or number(row["paid"], "paid") > acquired or number(row["retained"], "retained") > activated:
                raise ValueError("Impossible acquisition, activation, payment, or retention counts")
            equal(row["retention_rate"], number(row["retained"], "retained") / acquired, "retention_rate")
    elif skill in ("calculate-beachhead-market-tam", "calculate-follow-on-markets-tam"):
        scenario_rows(data["markets"], "markets")
        if skill == "calculate-beachhead-market-tam":
            scenario_rows(data["triangulation"], "triangulation")
        for row in data["markets"]:
            equal(row["annual_tam"], number(row["units"], "units") * number(row["annual_revenue_per_unit"], "annual_revenue_per_unit"), "annual_tam")
    elif skill == "calculate-customer-acquisition-cost":
        scenario_rows(data["acquisition"], "acquisition")
        for row in data["acquisition"]:
            cac = number(row["acquisition_spend"], "acquisition_spend") / number(row["new_paying_customers"], "new_paying_customers")
            equal(row["cac"], cac, "cac")
            equal(row["simple_payback_periods"], cac / number(row["contribution_per_period"], "contribution_per_period"), "simple_payback_periods")
    elif skill == "calculate-customer-lifetime-value":
        scenario_rows(data["cashflows"], "cashflows")
        scenario_rows(data["summary"], "summary")
        horizon = int(number(scope["horizon_periods"], "horizon_periods"))
        discount = number(scope["discount_rate_per_period"], "discount_rate_per_period")
        for scenario in SCENARIOS:
            cashflows = ordered_periods([row for row in data["cashflows"] if row["scenario"] == scenario], horizon, scenario, "period")
            previous = 1.0
            total = 0.0
            for row in cashflows:
                retention = number(row["retention"], "retention")
                if retention > previous:
                    raise ValueError("retention: survival probability cannot increase within a cohort")
                previous = retention
                contribution = retention * (
                    number(row["revenue_per_active_customer"], "revenue") * number(row["gross_margin"], "gross_margin")
                    - number(row["service_cost"], "service_cost")
                )
                discounted = contribution / (1 + discount) ** number(row["period"], "period")
                equal(row["expected_contribution"], contribution, "expected_contribution")
                equal(row["discounted_contribution"], discounted, "discounted_contribution")
                total += discounted
            summaries = [row for row in data["summary"] if row["scenario"] == scenario]
            if len(summaries) != 1:
                raise ValueError(f"{scenario}: require one LTV summary")
            equal(summaries[0]["ltv"], total, f"{scenario}.ltv")
    elif skill == "quantify-the-value-proposition":
        scenario_rows(data["outcomes"], "outcomes")
        for row in data["outcomes"]:
            delta = number(row["future"], "future") - number(row["baseline"], "baseline")
            if row["direction"] == "decrease":
                delta *= -1
            expected = delta * number(row["unit_value"], "unit_value") * number(row["frequency"], "frequency") * number(row["realization"], "realization")
            equal(row["realized_value"], expected, "realized_value")
    elif skill == "plan-operations":
        for row in data["capacity"]:
            required = number(row["demand_units"], "demand_units") * number(row["hours_per_unit"], "hours_per_unit")
            equal(row["required_hours"], required, "required_hours")
            equal(row["gap_hours"], max(0, required - number(row["available_hours"], "available_hours")), "gap_hours")
            equal(row["labor_cost"], required * number(row["cost_per_hour"], "cost_per_hour"), "labor_cost")
    elif skill == "build-financial-plan":
        scenario_rows(data["cashflow"], "cashflow")
        scenario_rows(data["summary"], "summary")
        horizon = int(number(scope["horizon_months"], "horizon_months"))
        for scenario in SCENARIOS:
            cashflows = ordered_periods([row for row in data["cashflow"] if row["scenario"] == scenario], horizon, scenario, "month")
            opening = number(scope["opening_cash"], "opening_cash")
            balances = [opening]
            first_negative = 0
            for row in cashflows:
                equal(row["opening_cash"], opening, "opening_cash continuity")
                revenue = number(row["units"], "units") * number(row["price"], "price")
                equal(row["revenue"], revenue, "revenue")
                operating = revenue - sum(number(row[key], key) for key in ("cogs", "opex", "taxes", "change_working_capital"))
                equal(row["operating_cash_flow"], operating, "operating_cash_flow")
                closing = opening + operating - number(row["capex"], "capex") + number(row["net_financing"], "net_financing")
                equal(row["closing_cash"], closing, "closing_cash")
                balances.append(closing)
                if closing < 0 and not first_negative:
                    first_negative = int(number(row["month"], "month"))
                opening = closing
            summaries = [row for row in data["summary"] if row["scenario"] == scenario]
            if len(summaries) != 1:
                raise ValueError(f"{scenario}: require one financial summary")
            summary = summaries[0]
            equal(summary["minimum_cash"], min(balances), "minimum_cash")
            equal(summary["additional_funding_needed"], max(0, -min(balances)), "additional_funding_needed")
            equal(summary["first_negative_month"], first_negative, "first_negative_month")


def validate_record(
    record: dict[str, object], contract: dict[str, object], workbook: Path,
    allow_draft: bool = False, allow_example: bool = False, workspace: Path | None = None,
) -> str:
    if type(record.get("schema_version")) is not int or record["schema_version"] != 2:
        raise ValueError("Workbook schema_version must be 2")
    if record.get("skill") != contract["skill"]:
        raise ValueError("Workbook skill does not match its validator")
    stage = string(record.get("stage"), "stage")
    if stage not in STAGES:
        raise ValueError(f"stage must be one of {STAGES}")
    if stage == "draft" and not allow_draft:
        raise ValueError("Draft is unfinished; use --allow-todo for a draft check, not completion")
    if type(record.get("synthetic")) is not bool:
        raise ValueError("synthetic must be a boolean")
    if record["synthetic"] and not allow_example:
        raise ValueError("Synthetic example is not venture evidence; use --allow-example only to inspect examples")
    complete = stage != "draft"
    for key in ("venture", "owner", "decision", "limitations"):
        string(record.get(key), key, complete)
    iso_date(record.get("date"), "date", recorded=True)
    evidence = evidence_records(record.get("evidence"), workbook, workspace, complete)
    scope = object_value(record.get("scope"), "scope")
    fields(scope, object_value(contract["scope"], "contract.scope"), "scope", evidence, complete)
    data = object_value(record.get("data"), "data")
    tables = object_value(contract["tables"], "contract.tables")
    if set(data) != set(tables):
        raise ValueError(f"data must contain exactly: {', '.join(tables)}")
    parsed: dict[str, list[dict[str, object]]] = {}
    for name, columns in tables.items():
        parsed[name] = rows(data[name], name)
        if stage == "completed-analysis" and not parsed[name]:
            raise ValueError(f"{name}: completed analysis requires at least one row")
        if stage == "research-plan" and parsed[name]:
            raise ValueError("Research plans must not mix planned work with result tables; put existing context in evidence")
        for index, row in enumerate(parsed[name]):
            fields(row, object_value(columns, name), f"{name}[{index + 1}]", evidence, complete)
    plan = rows(record.get("research_plan"), "research_plan")
    actions = rows(record.get("next_actions"), "next_actions")
    if stage == "research-plan" and not plan:
        raise ValueError("research-plan requires a population, method, metric, threshold, owner, and due date")
    if complete and not actions:
        raise ValueError("A completed deliverable needs a next action, owner, and date")
    for name, entries, columns in (("research_plan", plan, PLAN_COLUMNS), ("next_actions", actions, ACTION_COLUMNS)):
        for index, row in enumerate(entries):
            fields(row, dict(columns), f"{name}[{index + 1}]", evidence, complete)
    if stage == "completed-analysis":
        if not evidence:
            raise ValueError("Completed analysis requires recorded evidence or explicit assumptions")
        if contract.get("observations_required") and not any(entry["type"] == "fact" for entry in evidence.values()):
            raise ValueError("This completed analysis requires sourced observations, not assumptions alone")
        observed_tables = contract.get("observed_tables", [])
        if not isinstance(observed_tables, list) or not all(isinstance(name, str) for name in observed_tables):
            raise ValueError("contract.observed_tables must be a list of table names")
        for name in observed_tables:
            for row in parsed[name]:
                citations = row["evidence"]
                if not isinstance(citations, list) or not any(
                    isinstance(key, str) and evidence[key]["type"] == "fact" for key in citations
                ):
                    raise ValueError(f"{name}: each observed-result row must cite a sourced fact")
        check_calculations(string(contract["skill"], "skill"), scope, parsed)
    return stage


def create_main(skill_root: Path) -> int:
    parser = argparse.ArgumentParser(description="Create a task-specific workbook without overwriting existing work.")
    parser.add_argument("--venture", required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--stage", choices=STAGES, default="draft")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    try:
        contract = load_contract(skill_root)
        output = args.output or Path(f"{contract['skill']}-workbook.md")
        if output.exists() and not args.force:
            raise ValueError(f"Refusing to overwrite existing file: {output}")
        venture = string(args.venture, "venture")
        if "\n" in venture or "\r" in venture:
            raise ValueError("Venture name must be a single line")
        content = render_record(empty_record(contract, venture, args.stage), string(contract["title"], "title"), contract)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w" if args.force else "x", encoding="utf-8") as destination:
            destination.write(content)
        print(f"Created {output}; fill its task-specific record before claiming completion.")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


def validate_main(skill_root: Path) -> int:
    parser = argparse.ArgumentParser(description="Check a workbook's declared stage, task-specific fields, evidence, and calculations.")
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--allow-todo", action="store_true", help="Permit draft records; never declares completed analysis")
    parser.add_argument("--allow-example", action="store_true", help="Validate a clearly marked synthetic example")
    parser.add_argument("--require-analysis", action="store_true")
    parser.add_argument("--workspace", type=Path, help="Require evidence to match this workspace's register")
    args = parser.parse_args()
    try:
        record = extract_record(args.workbook.read_text(encoding="utf-8"))
        stage = validate_record(record, load_contract(skill_root), args.workbook, args.allow_todo, args.allow_example, args.workspace)
        if args.require_analysis and stage != "completed-analysis":
            raise ValueError("Completed analysis is required; a draft or research plan is not a result")
        print(f"Validated {stage}: {args.workbook}")
        print("Research plans are not observed results; checks cannot establish source truth or business viability.")
    except (OSError, UnicodeError, ValueError, OverflowError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0
