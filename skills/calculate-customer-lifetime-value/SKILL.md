---
name: calculate-customer-lifetime-value
description: "Calculates discounted contribution profit from an average acquired customer using retention, revenue, gross margin, service cost, and cost of capital. Use to assess unit economics, compare with acquisition cost, or identify the highest-leverage LTV drivers."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Calculate Customer Lifetime Value

## Goal

A cohort-aware, sensitivity-tested LTV model using contribution economics and explicit retention assumptions.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Revenue-only lifetime value, acquisition cost, or assuming constant churn without evidence.

## Inputs and missing data

Collect what is available before starting:

- Revenue schedule by customer or cohort
- Gross margin and customer-specific service costs
- Retention, churn, repeat purchase, or contract duration
- Expansion, contraction, maintenance, and renewal assumptions
- Discount rate and time horizon appropriate for startup risk

<!-- input-policy:start -->
Specify the cohort, horizon, period-aligned discount rate, retention, revenue, margin, and non-duplicated service costs.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define the customer unit and acquisition cohort so revenue and costs are attributed consistently.
2. Model periodic revenue, gross profit, ongoing support/service cost, retention probability, and expansion or contraction.
3. Exclude acquisition cost from LTV so it can be compared separately with COCA.
4. Discount future contribution using a rate that reflects timing and risk.
5. Calculate conservative, base, and upside cases and identify the highest-sensitivity drivers.
6. Compare modeled assumptions with observed cohort data where available; label unsupported estimates.
7. Set an LTV improvement agenda focused on retention, margin, expansion, or service efficiency.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-customer-lifetime-value-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-customer-lifetime-value-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `cashflows`, `summary`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- LTV cash-flow model
- Retention and contribution assumptions
- Discounted low/base/high LTV
- Sensitivity analysis
- LTV improvement priorities

The work is complete only when:

- LTV uses contribution profit, not revenue.
- Acquisition cost is excluded from the LTV numerator.
- Retention and time horizon are explicit and cohort-consistent.
- Future cash flows are discounted and sensitivity-tested.

## Gotchas

- Do not use 1/churn mechanically when data is immature or churn is non-constant.
- Annual contracts do not guarantee indefinite renewals.
- Customer success, support, hosting, and fulfillment may be customer-specific costs.
- An LTV:COCA target is a diagnostic, not proof of cash-flow viability or payback speed.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [calculate-customer-acquisition-cost](../calculate-customer-acquisition-cost/SKILL.md), [build-financial-plan](../build-financial-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
