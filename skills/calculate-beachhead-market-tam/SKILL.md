---
name: calculate-beachhead-market-tam
description: "Calculates the annual total addressable market for a beachhead using bottom-up customer counts and revenue per customer, then triangulates with top-down data. Use when sizing an initial market, checking whether it is focused yet meaningful, or documenting TAM assumptions."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Calculate Beachhead Market TAM

## Goal

A transparent annual revenue TAM range for the beachhead, with reproducible assumptions, sources, sensitivity analysis, and reconciliation.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Precise beachhead definition and inclusion criteria
- Bottom-up counts or a defensible path to estimate end users/customers
- Likely units purchased, usage, or annual contract structure
- Value and pricing hypotheses
- Independent top-down market data for triangulation

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
