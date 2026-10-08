---
name: quantify-the-value-proposition
description: "Quantifies the persona's highest-priority improvement by comparing the current state with a credible future state using the product. Use when value claims are vague, pricing lacks a value anchor, or stakeholders need a one-page economic or operational case."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Quantify the Value Proposition

## Goal

A customer-verifiable, one-page value case with an explicit baseline, measurable change, calculation, evidence, and sensitivity range.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Vendor revenue, price selection, or monetizing every benefit without a defensible conversion.

## Inputs and missing data

Collect what is available before starting:

- Persona and top-ranked purchasing criterion
- Current-state lifecycle data
- Product-enabled future-state assumptions
- Customer metrics such as time, cost, revenue, risk, quality, or experience
- Evidence sources and confidence levels

<!-- input-policy:start -->
Choose a customer-recognized baseline, consistent unit, and credible realization factor; record disputes and unknowns.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

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

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `outcomes`, `validation`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [set-your-pricing-framework](../set-your-pricing-framework/SKILL.md), [define-product-concept](../define-product-concept/SKILL.md). Standalone users may need to install these optional follow-ups.
