---
name: chart-your-competitive-position
description: "Charts the venture, direct alternatives, and customer status quo against the persona's two most important purchasing priorities. Use to test positioning, expose weak differentiation, or communicate qualitative value in customer terms."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Chart Your Competitive Position

## Goal

An evidence-backed competitive position chart and positioning narrative centered on customer priorities rather than vendor-selected features.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Internal capability analysis or choosing axes to guarantee a favorable chart.

## Inputs and missing data

Collect what is available before starting:

- Persona's prioritized purchasing criteria
- Customer status quo and alternative solutions
- Evidence of how customers perceive each option
- Product and value proposition
- Uncertainty and source quality by rating

<!-- input-policy:start -->
Use the customer's priorities and include the current workaround. A proposed product's position can be a labeled hypothesis.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Choose the persona's top two independent purchasing priorities; do not substitute attributes the product happens to win.
2. Define observable anchors for low and high performance on each axis.
3. Include direct competitors, indirect substitutes, doing nothing, and internal workarounds.
4. Place alternatives using customer evidence, not internal opinion; show uncertainty when evidence is limited.
5. Plot the proposed product and test whether its claimed position follows from the specification and core.
6. If the product is not clearly preferred on the chart, revise the offering, market, priorities, or positioning rather than manipulating axes.
7. Write a concise positioning narrative and validate it with target customers.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./chart-your-competitive-position-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./chart-your-competitive-position-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `axes`, `alternatives`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Axis definitions and evidence
- Competitive position chart
- Alternative-by-alternative notes
- Positioning narrative
- Strategic response if differentiation is weak

The work is complete only when:

- Axes are the persona's top priorities and are meaningfully distinct.
- The status quo is included.
- Placements have evidence or visible uncertainty.
- The chart implies a real customer choice, not merely a marketing claim.

## Gotchas

- Do not cherry-pick axes after seeing competitor positions.
- Market share, company size, or feature count may not reflect purchasing priorities.
- The customer's current workaround is often the toughest competitor.
- A two-axis chart simplifies reality; preserve material caveats.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [define-competitive-advantage](../define-competitive-advantage/SKILL.md), [define-product-concept](../define-product-concept/SKILL.md). Standalone users may need to install these optional follow-ups.
