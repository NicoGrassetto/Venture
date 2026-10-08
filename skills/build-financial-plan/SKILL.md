---
name: build-financial-plan
description: "Builds an integrated monthly financial plan with revenue drivers, operating costs, working capital, cash flow, runway signals, scenarios, and funding needs. Use when translating a venture plan into a resource decision or checking whether unit economics can support cash survival."
license: MIT
compatibility: "Python 3.9 or newer; standard library only."
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Build a Financial Plan

## Goal

A reproducible, scenario-based cash forecast connecting the business model,
sales assumptions, operating plan, and funding milestones.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Only TAM or unit economics, investment advice, or a guarantee that financing will be available.

## Inputs and missing data

- Customer unit, pricing, revenue timing, and sales assumptions
- Delivery capacity, costs, staffing, and supplier terms
- Opening cash, capital expenditure, financing, and tax assumptions
- Planning horizon and currency
- Observed results separated from untested forecasts

<!-- input-policy:start -->
Tie demand and price to the business model and costs to the operations plan. State timing, working capital, taxes, capital expenditure, and financing assumptions.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define a monthly horizon, one currency, customer unit, and opening cash balance.
2. Build conservative, base, and upside demand and pricing scenarios from named drivers.
3. Link COGS and operating expenses to the operating plan; keep acquisition costs, service costs, and overhead from being counted twice.
4. Model working-capital movement, taxes, capital expenditure, and net financing with explicit timing assumptions.
5. Reconcile monthly revenue, operating cash flow, opening/closing cash continuity, minimum cash, and additional funding required.
6. Identify the first negative-cash month and distinguish horizon-limited survival from indefinite runway.
7. Stress the most consequential assumptions and tie resource commitments to evidence and funding milestones.

Read [references/method.md](references/method.md) before classifying cash movements.

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./build-financial-plan-workbook.md"
python3 scripts/validate_workbook.py "./build-financial-plan-workbook.md"
```

Resolve paths from this skill's directory.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `cashflow`, `summary`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

- Every scenario covers each month exactly once and uses the same currency and customer unit.
- Revenue, cash movement, and opening/closing balances recompute from visible inputs.
- Costs and delivery volumes reconcile to the operating assumptions.
- Funding needs and shortfall timing are explicit; financing is not assumed to exist without evidence.
- The decision states what to do if the conservative case occurs.

## Gotchas

- Profit is not cash, and a large TAM is not a sales forecast.
- A financing inflow can conceal operating losses; show both.
- Zero first-negative-month means no shortfall within the horizon, not unlimited runway.
- Tax and financing decisions require qualified review; this model is not professional advice.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [identify-key-assumptions](../identify-key-assumptions/SKILL.md), [create-business-plan](../create-business-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
