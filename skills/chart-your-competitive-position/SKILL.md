---
name: chart-your-competitive-position
description: "Charts the venture, direct alternatives, and customer status quo against the persona's two most important purchasing priorities. Use to test positioning, expose weak differentiation, or communicate qualitative value in customer terms."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Chart Your Competitive Position

## Goal

An evidence-backed competitive position chart and positioning narrative centered on customer priorities rather than vendor-selected features.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Persona's prioritized purchasing criteria
- Customer status quo and alternative solutions
- Evidence of how customers perceive each option
- Product and value proposition
- Uncertainty and source quality by rating

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
