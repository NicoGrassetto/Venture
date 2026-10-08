---
name: calculate-customer-acquisition-cost
description: "Calculates fully loaded customer acquisition cost from top-down sales and marketing spending divided by acquired customers, then diagnoses payback and reduction levers. Use to test unit economics or replace unrealistic activity-by-activity acquisition estimates."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Calculate Customer Acquisition Cost

## Goal

A period- and cohort-aligned COCA model including all acquisition costs, with channel views, payback analysis, and reduction priorities.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Cost per lead or attributing all acquisition to the final sales call.

## Inputs and missing data

Collect what is available before starting:

- Sales and marketing spend by period
- Compensation, tools, content, events, discounts, partner fees, and allocated overhead
- Customers acquired by period and channel
- Sales-cycle lag between spend and acquisition
- LTV and contribution schedule for payback comparison

<!-- input-policy:start -->
Use paying-customer cohorts and fully loaded spend. With zero acquisitions, CAC is undefined: report the limitation rather than divide by zero.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define the acquired-customer event and cohort consistently, excluding leads, trials, and renewals unless the model explicitly treats them.
2. Collect fully loaded acquisition spending, including labor and less visible program or channel costs.
3. Align spend with the customers it generated using a reasonable sales-cycle lag.
4. Calculate blended and channel-specific COCA where attribution is credible; preserve unattributed spend rather than deleting it.
5. Compare COCA with LTV, gross contribution, and cash payback timing.
6. Run sensitivity analysis on conversion, cycle time, channel mix, compensation, and organic/referral contribution.
7. Prioritize structural reductions such as product simplification, stronger referrals, shorter cycles, better qualification, or lower-cost channels.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-customer-acquisition-cost-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-customer-acquisition-cost-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `acquisition`, `cost_coverage`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Fully loaded spend ledger
- Customer cohort and lag mapping
- Blended and channel COCA
- LTV:COCA and payback analysis
- COCA reduction experiments

The work is complete only when:

- The numerator includes all material acquisition costs.
- The denominator counts acquired paying customers consistently.
- Spend and acquisitions are time-aligned.
- COCA is paired with payback and LTV rather than interpreted alone.

## Gotchas

- Bottom-up 'cost of one sales call' calculations omit failures and overhead.
- Founder labor is not free even if no salary is paid.
- Organic customers can be supported by brand, content, community, or product investments.
- Channel attribution can create false precision; retain a blended view.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [calculate-customer-lifetime-value](../calculate-customer-lifetime-value/SKILL.md), [build-financial-plan](../build-financial-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
