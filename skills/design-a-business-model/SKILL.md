---
name: design-a-business-model
description: "Designs and compares how the venture creates, delivers, and captures value before setting exact prices. Use when choosing revenue logic, payer structure, transaction model, or a differentiated model that affects LTV and acquisition cost."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Design a Business Model

## Goal

A selected business model with explicit value flows, payer, revenue unit, cost drivers, incentives, risks, and experiment plan.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Selecting exact prices or constructing a financial forecast before identifying who pays.

## Inputs and missing data

Collect what is available before starting:

- Value proposition, DMU, and acquisition process
- Who receives value and who controls money
- Usage frequency and transaction structure
- Channel, partner, and platform economics
- Competitive business models and switching constraints

<!-- input-policy:start -->
Compare coherent value and money flows; free participants need an explicit payer or funding mechanism.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Map all value recipients, payers, suppliers, partners, and flows of product, data, service, and money.
2. Generate several coherent business model alternatives, not merely several prices.
3. For each model, define payer, charge basis, timing, recurrence, ownership, channel, variable costs, and risk allocation.
4. Evaluate customer alignment, adoption friction, cash flow, gross margin, scalability, defensibility, and expected effects on LTV and COCA.
5. Check incentive compatibility and whether free participants are funded by a credible paying side.
6. Select a primary model and identify a small number of critical assumptions to test.
7. Define migration risks because changing a business model later can disrupt customers, channels, and operations.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./design-a-business-model-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./design-a-business-model-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `models`, `selection`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Value and money flow map
- Business model alternatives
- Comparison scorecard
- Selected model and rationale
- Critical assumptions and experiments

The work is complete only when:

- The model names a payer and a chargeable unit.
- Free usage has an explicit funding mechanism.
- Channel and partner incentives are economically coherent.
- The selected model can plausibly support attractive LTV and COCA.

## Gotchas

- Business model is not synonymous with price.
- Advertising, data, or cross-subsidy only works with a real paying customer.
- A familiar industry model may preserve competitors' advantages.
- Do not choose a model solely because customers say they prefer paying that way.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [set-your-pricing-framework](../set-your-pricing-framework/SKILL.md), [plan-operations](../plan-operations/SKILL.md). Standalone users may need to install these optional follow-ups.
