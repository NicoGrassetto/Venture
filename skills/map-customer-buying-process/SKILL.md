---
name: map-customer-buying-process
description: "Maps the customer's internal process from first awareness through evaluation, approvals, contracting, payment, and implementation. Use to expose sales-cycle length, procurement, regulation, budgeting, and other obstacles before forecasting revenue."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Map the Customer Buying Process

## Goal

A validated customer-side buying process with stages, owners, artifacts, timing, dependencies, failure modes, and a realistic path to payment.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: The venture's marketing activities or CRM stage names.

## Inputs and missing data

Collect what is available before starting:

- DMU map and stakeholder evidence
- Recent comparable purchases
- Budget cycle and purchasing authority
- Procurement, legal, security, regulatory, and implementation requirements
- Payment and vendor-onboarding mechanics

<!-- input-policy:start -->
Ground timing in actual comparable purchases when possible; distinguish observed timing from forecast assumptions.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Choose a concrete customer archetype and start from the trigger that creates active consideration.
2. Reconstruct every customer action and approval through committed funds, contract, payment, and readiness to use.
3. For each stage, record owner, entry condition, exit condition, artifact, elapsed time, and common failure.
4. Overlay budget timing, procurement thresholds, security/legal reviews, regulation, partner dependencies, and implementation capacity.
5. Identify the critical path and stages that can run in parallel.
6. Validate timing with customers and distinguish best case, typical case, and delayed case.
7. Translate the map into seller evidence requirements and forecast milestones without turning it into the seller's sales-process map.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./map-customer-buying-process-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./map-customer-buying-process-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `buying_stages`, `obstacles`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Customer acquisition process map
- Stage timing and critical path
- Required artifacts and approvals
- Obstacle and mitigation register
- Forecast implications

The work is complete only when:

- The process ends with payment and implementation readiness, not verbal interest.
- Every stage has a customer-side owner and exit condition.
- Budget and purchasing authority are explicit.
- Timing is grounded in comparable purchases.

## Gotchas

- Do not confuse the customer's buying process with the startup's selling activities.
- A signed agreement may precede payment or implementation by months.
- Security, legal, or vendor onboarding can dominate cycle time.
- Consumer processes can include app-store, household, financing, or platform constraints.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [map-the-sales-process](../map-the-sales-process/SKILL.md), [calculate-customer-acquisition-cost](../calculate-customer-acquisition-cost/SKILL.md). Standalone users may need to install these optional follow-ups.
