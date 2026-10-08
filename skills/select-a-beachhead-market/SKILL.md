---
name: select-a-beachhead-market
description: "Selects one focused beachhead market from researched segments and narrows it until customers share needs, buying behavior, and word of mouth. Use after market segmentation or when a startup is spreading effort across several markets."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Select a Beachhead Market

## Goal

One explicitly chosen, homogeneous beachhead market with a documented rationale, exclusions, and remaining segmentation risks.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Generating segments from scratch or adding adjacent markets to the first product.

## Inputs and missing data

Collect what is available before starting:

- Market segmentation matrix and interview evidence
- Founder goals, capabilities, and access advantages
- Segment urgency, budget, competition, and sales-cycle evidence
- Rough market sizes and product-fit implications
- Dependencies on partners, platforms, or regulation

<!-- input-policy:start -->
Compare explicit candidates. A provisional choice may use assumptions, but record exclusions and reversal conditions.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

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

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `selection`, `scorecard`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [build-an-end-user-profile](../build-an-end-user-profile/SKILL.md), [calculate-beachhead-market-tam](../calculate-beachhead-market-tam/SKILL.md). Standalone users may need to install these optional follow-ups.
