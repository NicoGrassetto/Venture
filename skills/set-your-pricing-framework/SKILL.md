---
name: set-your-pricing-framework
description: "Creates a value-based pricing framework with metric, fences, packaging, and evidence plan rather than a single arbitrary price. Use after choosing a business model or when pricing is anchored to cost, competitors, or unsupported willingness-to-pay."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Set Your Pricing Framework

## Goal

A testable pricing architecture tied to customer value, segment differences, purchase friction, and the chosen business model.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Choosing the business model or treating competitor prices as willingness-to-pay evidence.

## Inputs and missing data

Collect what is available before starting:

- Quantified customer value and purchasing priorities
- Business model and chargeable unit
- Customer budget and approval thresholds
- Competitive alternatives and status quo costs
- Early-customer strategic value and discount conditions

<!-- input-policy:start -->
State the value metric, package boundary, and price hypothesis. Do not invent accepted prices when only proposals exist.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Choose a pricing metric that scales with customer value and is measurable, predictable, and difficult to game.
2. Define value-based reference points: quantified value, alternatives, budget thresholds, and risk reduction.
3. Design packages and fences only where customer needs or willingness to pay differ meaningfully.
4. Set provisional list-price ranges and target capture rates; keep cost as a viability floor, not the primary anchor.
5. Plan pricing research using behavioral evidence such as purchase tests, proposals, deposits, or negotiated pilots.
6. Define discount authority, expiration, exchange of value, and treatment of lighthouse customers.
7. Document how pricing will be reviewed as evidence, product scope, and market maturity change.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./set-your-pricing-framework-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./set-your-pricing-framework-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `packages`, `price_tests`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Pricing metric decision
- Value and alternative anchors
- Packaging and fence architecture
- Provisional price ranges
- Discount policy and testing plan

The work is complete only when:

- The metric correlates with realized customer value.
- A customer can understand and forecast the charge.
- Discounts exchange for explicit value and do not silently reset reference price.
- The framework is consistent with the business model and buying process.

## Gotchas

- Cost-plus pricing ignores the customer's value.
- Competitor prices are context, not proof of willingness to pay.
- Too many packages create friction and weak evidence.
- Early discounts should be exceptional, time-bound, and strategically justified.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [test-key-assumptions](../test-key-assumptions/SKILL.md), [calculate-customer-lifetime-value](../calculate-customer-lifetime-value/SKILL.md). Standalone users may need to install these optional follow-ups.
