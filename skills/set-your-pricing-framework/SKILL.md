---
name: set-your-pricing-framework
description: "Creates a value-based pricing framework with metric, fences, packaging, and evidence plan rather than a single arbitrary price. Use after choosing a business model or when pricing is anchored to cost, competitors, or unsupported willingness-to-pay."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Set Your Pricing Framework

## Goal

A testable pricing architecture tied to customer value, segment differences, purchase friction, and the chosen business model.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Quantified customer value and purchasing priorities
- Business model and chargeable unit
- Customer budget and approval thresholds
- Competitive alternatives and status quo costs
- Early-customer strategic value and discount conditions

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
