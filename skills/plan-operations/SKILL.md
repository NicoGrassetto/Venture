---
name: plan-operations
description: "Builds a delivery and operating plan with capacity, staffing, suppliers, costs, service boundaries, and contingencies. Use before making delivery promises or translating a business model into a financial forecast."
license: MIT
compatibility: "Python 3.9 or newer; standard library only."
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Plan Operations

## Goal

An owned, costed operating plan that can deliver the promised customer outcome
within actual capacity and constraints.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A feature roadmap or replacing jurisdiction-specific professional advice.

## Inputs and missing data

- Customer workflow, minimum offer, and service promise
- Demand units and planning period
- Founder and team availability, skills, costs, and ownership
- Suppliers, partners, lead times, systems, and quality requirements
- Legal, safety, privacy, or regulatory matters needing qualified review

<!-- input-policy:start -->
Define delivery units, a planning period, available capacity, owners, costs, suppliers, and failure contingencies before promising service levels.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define the delivery unit and service boundary; map the work from an accepted order to a verified customer outcome.
2. Estimate demand, required hours, available capacity, labor cost, and the bottleneck for each material activity.
3. Identify staffing and capability gaps. Account for founder time rather than treating manual work as free.
4. Map suppliers, systems, lead times, quality checks, ownership, and fallback options.
5. Test the delivery plan under a demand spike, supplier failure, staff absence, and a quality incident.
6. Reduce scope, add capacity, or change the service promise where the plan does not fit.
7. Feed the approved operating assumptions into the financial plan and set the next review trigger.

Read [references/method.md](references/method.md) for cost classification and capacity rules.

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./plan-operations-workbook.md"
python3 scripts/validate_workbook.py "./plan-operations-workbook.md"
```

Resolve paths from this skill's directory.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `capacity`, `dependencies`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

- Capacity and labor-cost calculations reconcile.
- Every critical dependency has an owner, failure trigger, and fallback.
- Capacity shortfalls produce a change in resources, scope, or promises.
- Cost assumptions can be traced into the financial plan without double counting.
- Qualified review is requested for consequential legal or regulated decisions.

## Gotchas

- Utilization is not the same as availability; leave capacity for variability and rework.
- A single founder cannot occupy several full-time roles simultaneously.
- Do not mistake a concierge pilot for scalable unit economics.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [build-financial-plan](../build-financial-plan/SKILL.md), [develop-a-product-plan](../develop-a-product-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
