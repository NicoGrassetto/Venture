---
name: select-a-beachhead-market
description: "Selects one focused beachhead market from researched segments and narrows it until customers share needs, buying behavior, and word of mouth. Use after market segmentation or when a startup is spreading effort across several markets."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Select a Beachhead Market

## Goal

One explicitly chosen, homogeneous beachhead market with a documented rationale, exclusions, and remaining segmentation risks.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Market segmentation matrix and interview evidence
- Founder goals, capabilities, and access advantages
- Segment urgency, budget, competition, and sales-cycle evidence
- Rough market sizes and product-fit implications
- Dependencies on partners, platforms, or regulation

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Remove candidates that conflict with founder values, lack accessible customers, require unaffordable capabilities, or cannot support a focused first product.
2. Compare remaining segments on customer value, economic attractiveness, competitive position, access, buying speed, and strategic leverage.
3. Use a consistent decision matrix, then inspect whether the result changes under reasonable weight adjustments.
4. Choose one segment. State why it wins now and why other attractive segments are deferred rather than blended into scope.
5. Run the homogeneity test: customers buy similar products for similar reasons, can be reached similarly, and can credibly influence one another.
6. Subsegment again if the chosen market fails the homogeneity test.
7. Write a falsifiable beachhead definition and a list of signals that would force reconsideration.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./select-a-beachhead-market-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./select-a-beachhead-market-workbook.md"
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

- Beachhead selection scorecard
- Chosen market definition
- Deferred-market register
- Homogeneity test
- Reconsideration triggers

The work is complete only when:

- Exactly one market is selected for current execution.
- The market definition specifies end user, application, context, and geography where relevant.
- Customers can plausibly create word of mouth within the market.
- The team can reach enough customers to learn and sell without building several products.

## Gotchas

- Do not select the largest TAM by default.
- Do not combine adjacent markets to avoid making a hard choice.
- Founder access is valuable, but access without urgent customer value is insufficient.
- A beachhead is a sequencing choice, not a claim that other markets are bad.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
