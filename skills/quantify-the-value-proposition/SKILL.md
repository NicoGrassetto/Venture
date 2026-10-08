---
name: quantify-the-value-proposition
description: "Quantifies the persona's highest-priority improvement by comparing the current state with a credible future state using the product. Use when value claims are vague, pricing lacks a value anchor, or stakeholders need a one-page economic or operational case."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Quantify the Value Proposition

## Goal

A customer-verifiable, one-page value case with an explicit baseline, measurable change, calculation, evidence, and sensitivity range.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Persona and top-ranked purchasing criterion
- Current-state lifecycle data
- Product-enabled future-state assumptions
- Customer metrics such as time, cost, revenue, risk, quality, or experience
- Evidence sources and confidence levels

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Choose one primary value dimension tied to the persona's top priority; keep secondary benefits subordinate.
2. Define the current-state baseline using the customer's units, process, frequency, and time horizon.
3. Map the future state and identify exactly which steps, rates, or outcomes change.
4. Calculate gross value with visible formulas and distinguish customer value from vendor revenue or price.
5. Build conservative, base, and upside cases; identify adoption, realization, and attribution assumptions.
6. Create a one-page visual comparison that a champion can retell internally.
7. Review the calculation with target customers and update inputs they dispute.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./quantify-the-value-proposition-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./quantify-the-value-proposition-workbook.md"
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

- As-is versus possible-state map
- Value calculation with sources
- Sensitivity scenarios
- One-page quantified value proposition
- Customer validation record

The work is complete only when:

- The metric matches the persona's first purchasing priority.
- The baseline and future state use the same units and horizon.
- All material assumptions are visible and sensitivity-tested.
- A customer recognizes the baseline and accepts the logic, even if inputs remain ranges.

## Gotchas

- Do not monetize every benefit; lead with the one customers prioritize.
- Do not equate product capability with realized customer value.
- Avoid unsupported ROI percentages and overly precise savings.
- Price is the share of value captured, not the value itself.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
