---
name: validate-customer-traction
description: "Validates an MVBP with real customer usage, payment, retention, outcomes, and advocacy rather than compliments or sign-ups. Use during early launch to determine whether customers actually consume and value the product."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Validate Customer Traction

## Goal

An evidence-based product-consumption assessment with cohort trends, payment proof, customer outcomes, root causes, and a scale/iterate/pivot decision.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Sign-up totals, compliments, or declaring product-market fit from one cohort.

## Inputs and missing data

Collect what is available before starting:

- MVBP and its success metrics
- Target customer cohorts and acquisition source
- Usage, activation, retention, payment, and outcome data
- Support interactions and qualitative feedback
- Advocacy, referral, or word-of-mouth evidence

<!-- input-policy:start -->
Completed analysis needs actual usage, payment, and cohort observations. A future instrumentation plan belongs in research-plan mode.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define activation and meaningful usage based on delivered value, not superficial logins.
2. Instrument the full path from acquisition through onboarding, repeated use, outcome, payment, renewal, and referral.
3. Analyze cohorts over time rather than relying only on cumulative totals.
4. Pair behavioral data with interviews focused on why users progressed, stalled, churned, paid, or advocated.
5. Separate acquisition quality, onboarding friction, product value, reliability, and pricing as possible causes.
6. Compare results with predeclared MVBP thresholds and examine trends, not isolated anecdotes.
7. Decide to scale, iterate, narrow the market, revise the offer, or stop; specify the next evidence required.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./validate-customer-traction-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./validate-customer-traction-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `cohorts`, `diagnosis`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Consumption metric definitions
- Cohort funnel and retention analysis
- Payment and outcome evidence
- Root-cause synthesis
- Scale/iterate/pivot decision

The work is complete only when:

- Metrics reflect meaningful customer value.
- Real customers use and pay, or a documented binding payment path exists.
- Retention and repeated use are analyzed by cohort.
- The team acts on negative evidence with intellectual honesty.

## Gotchas

- Registrations, downloads, and compliments do not prove consumption.
- Aggregate growth can hide deteriorating cohorts.
- Heavy founder intervention can inflate engagement.
- Advocacy is stronger when customers act - refer, invite, review, or stake reputation.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [develop-a-product-plan](../develop-a-product-plan/SKILL.md), [calculate-customer-lifetime-value](../calculate-customer-lifetime-value/SKILL.md). Standalone users may need to install these optional follow-ups.
