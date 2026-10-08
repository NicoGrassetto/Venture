---
name: map-the-sales-process
description: "Designs the venture's sales process from awareness through education, conversion, onboarding, and a scalable long-term acquisition motion. Use after mapping the customer's buying process or when forecasting activities and acquisition cost."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Map the Sales Process

## Goal

A staged seller-side process with channels, activities, conversion assumptions, costs, ownership, evidence, and evolution from early founder sales to scale.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: The customer's internal approval process or counting leads as paying customers.

## Inputs and missing data

Collect what is available before starting:

- Customer acquisition process and DMU
- Awareness, education, evaluation, and purchase needs
- Channel options and sales resources
- Expected conversion, cycle time, and deal economics
- Short-, medium-, and long-term go-to-market hypotheses

<!-- input-policy:start -->
Separate founder-led exceptions from the repeatable sales motion. Conversion rates must have a defined stage denominator.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Mirror the customer's buying stages, then define the seller activity and evidence that helps the customer exit each stage.
2. Specify entry/exit criteria, owner, channel, content, tool, elapsed time, and direct cost for each stage.
3. Separate awareness, education, validation, commercial close, payment, onboarding, and expansion.
4. Model early founder-led sales distinctly from transitional and mature repeatable motions.
5. Estimate stage conversions and cycle times using ranges; mark unvalidated assumptions.
6. Identify automation, partner, product-led, community, referral, or inside-sales opportunities that may reduce long-term COCA.
7. Define instrumentation and experiments to improve bottleneck stages.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./map-the-sales-process-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./map-the-sales-process-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `sales_stages`, `bottlenecks`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Sales process map
- Stage definitions and ownership
- Channel and content plan
- Conversion/cycle-time model
- Evolution roadmap and instrumentation

The work is complete only when:

- Seller stages align with how customers actually buy.
- Each stage has measurable entry and exit criteria.
- Founder-led exceptions are not treated as the scalable steady state.
- Costs and conversion assumptions can feed the COCA model.

## Gotchas

- The customer acquisition process is customer-side; this skill designs seller-side actions.
- A CRM stage name without exit evidence is not a process.
- Early high-touch sales can validate value but distort long-term economics.
- Do not optimize lead volume when a later stage is the real bottleneck.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [calculate-customer-acquisition-cost](../calculate-customer-acquisition-cost/SKILL.md), [build-financial-plan](../build-financial-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
