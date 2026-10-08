---
name: calculate-beachhead-market-tam
description: "Calculates the annual total addressable market for a beachhead using bottom-up customer counts and revenue per customer, then triangulates with top-down data. Use when sizing an initial market, checking whether it is focused yet meaningful, or documenting TAM assumptions."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Calculate Beachhead Market TAM

## Goal

A transparent annual revenue TAM range for the beachhead, with reproducible assumptions, sources, sensitivity analysis, and reconciliation.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A revenue forecast, valuation, or summing overlapping markets.

## Inputs and missing data

Collect what is available before starting:

- Precise beachhead definition and inclusion criteria
- Bottom-up counts or a defensible path to estimate end users/customers
- Likely units purchased, usage, or annual contract structure
- Value and pricing hypotheses
- Independent top-down market data for triangulation

<!-- input-policy:start -->
Specify economic units, annual revenue per unit, exclusions, and source assumptions. Missing inputs belong in a research plan, not made-up totals.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define the unit of count and prevent double counting: end users, accounts, sites, seats, transactions, or another economic unit.
2. Build a bottom-up count from named sources, sampled populations, channel records, or customer-level extrapolation.
3. Estimate annual revenue per unit using a pricing hypothesis consistent with the business model; separate volume from price.
4. Calculate low, base, and high TAM scenarios and identify the assumptions driving the spread.
5. Create an independent top-down estimate, applying explicit filters until it matches the beachhead definition.
6. Reconcile the estimates. Investigate material differences instead of averaging them automatically.
7. Document data dates, source quality, exclusions, and the next evidence that would narrow uncertainty.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-beachhead-market-tam-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-beachhead-market-tam-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `markets`, `triangulation`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Bottom-up TAM model
- Top-down triangulation
- Low/base/high scenario table
- Source and assumption register
- Reconciliation narrative

The work is complete only when:

- TAM represents annual revenue at 100% beachhead share, not company valuation or global industry spend.
- The bottom-up model can be recalculated from visible inputs.
- Counts and price use compatible units and time periods.
- Top-down filters end at the same market definition as the bottom-up model.

## Gotchas

- Do not present a top-down report number as the primary calculation.
- Do not multiply end users by enterprise contract price unless end users are the paying unit.
- Avoid false precision when sources are weak.
- Do not silently include follow-on markets in beachhead TAM.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [design-a-business-model](../design-a-business-model/SKILL.md). Standalone users may need to install these optional follow-ups.
