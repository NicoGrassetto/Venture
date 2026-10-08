---
name: develop-a-product-plan
description: "Develops an evidence-driven product roadmap from the validated beachhead product into adjacent markets while preserving near-term focus. Use after MVBP consumption evidence to sequence capability, platform, and market expansion."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Develop a Product Plan

## Goal

A product and market evolution plan with horizons, dependencies, learning gates, resource implications, and explicit protection of beachhead execution.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A build specification or promising expansion without evidence gates.

## Inputs and missing data

Collect what is available before starting:

- MVBP usage, payment, retention, and customer outcome evidence
- Beachhead gaps and customer requests
- Follow-on market analysis
- Core capability and architecture implications
- Resource, hiring, partner, and capital constraints

<!-- input-policy:start -->
Sequence customer outcomes and dependencies. If consumption evidence is missing, keep expansion conditional rather than claiming readiness.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Summarize what the beachhead evidence proves, disproves, and leaves uncertain.
2. Define product horizons: harden the beachhead, expand within it, enter the next adjacency, and enable longer-term platform options.
3. Map customer outcomes and market-entry goals before listing features.
4. Identify reusable capabilities, technical or operational foundations, and dependencies that unlock several future moves.
5. Sequence initiatives by evidence, strategic leverage, risk, and resource constraints; set learning or traction gates between horizons.
6. Explicitly defer attractive ideas that would distract from current customer value and retention.
7. Create a review cadence that updates the plan when evidence changes without turning it into a constantly shifting wish list.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./develop-a-product-plan-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./develop-a-product-plan-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `roadmap`, `deferred`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Evidence baseline
- Product horizons and outcomes
- Capability/dependency map
- Sequenced roadmap with gates
- Deferred opportunities and review cadence

The work is complete only when:

- Near-term work improves beachhead value, reliability, retention, or economics.
- Follow-on initiatives have explicit market and evidence triggers.
- Features trace to customer outcomes or enabling capabilities.
- The plan respects real resource and dependency constraints.

## Gotchas

- A roadmap is not a chronological feature wish list.
- Do not let distant TAM distract from current consumption evidence.
- Customer requests may be one-offs that weaken the focused product.
- Plans should change with evidence, but priorities need stable decision rules.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [plan-operations](../plan-operations/SKILL.md), [build-financial-plan](../build-financial-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
