---
name: calculate-follow-on-markets-tam
description: "Sizes adjacent follow-on markets and shows a credible expansion sequence beyond the beachhead without diluting current focus. Use to test long-term potential, support product-platform decisions, or communicate a growth path."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Calculate Follow-on Markets TAM

## Goal

A directional broader-TAM model and prioritized adjacency roadmap linked to transferable product, channel, brand, data, and capability advantages.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A revenue forecast, valuation, or summing overlapping markets.

## Inputs and missing data

Collect what is available before starting:

- Beachhead TAM and assumptions
- Candidate adjacent users, applications, geographies, or channels
- Transferable product and core capabilities
- Incremental requirements and market-entry barriers
- Customer and ecosystem evidence for adjacency

<!-- input-policy:start -->
Specify economic units, annual revenue per unit, exclusions, and source assumptions. Missing inputs belong in a research plan, not made-up totals.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define adjacency dimensions explicitly: same user/new use, new user/same use, geography, channel, vertical, or platform side.
2. List candidate follow-on markets without adding them to current beachhead scope.
3. Estimate each market directionally using transparent units and ranges.
4. Assess leverage from the beachhead: references, product reuse, data, brand, channel, partnerships, and core capability.
5. Assess incremental burden: features, regulation, sales motion, support, localization, capital, and new competitors.
6. Prioritize a sequence based on attractiveness, transferability, and learning dependencies.
7. State trigger conditions for expansion and what must remain true in the beachhead first.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-follow-on-markets-tam-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-follow-on-markets-tam-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `markets`, `expansion_gates`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Follow-on market map
- Directional TAM ranges
- Adjacency leverage/burden analysis
- Expansion sequence
- Expansion triggers and constraints

The work is complete only when:

- Follow-on markets are separate from beachhead TAM.
- Each adjacency has a clear transfer mechanism from the beachhead.
- Sizing uses visible assumptions and appropriately broad ranges.
- The roadmap preserves near-term beachhead focus.

## Gotchas

- Do not sum every conceivable market into a headline number.
- A large adjacent TAM may require a different product and company.
- Geographic expansion can change regulation, channels, and purchasing criteria.
- This is strategic validation, not a detailed operating plan.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [develop-a-product-plan](../develop-a-product-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
