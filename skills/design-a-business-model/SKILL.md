---
name: design-a-business-model
description: "Designs and compares how the venture creates, delivers, and captures value before setting exact prices. Use when choosing revenue logic, payer structure, transaction model, or a differentiated model that affects LTV and acquisition cost."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Design a Business Model

## Goal

A selected business model with explicit value flows, payer, revenue unit, cost drivers, incentives, risks, and experiment plan.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Value proposition, DMU, and acquisition process
- Who receives value and who controls money
- Usage frequency and transaction structure
- Channel, partner, and platform economics
- Competitive business models and switching constraints

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
