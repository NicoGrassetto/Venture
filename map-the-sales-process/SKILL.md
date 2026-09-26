---
name: map-the-sales-process
description: "Designs the venture's sales process from awareness through education, conversion, onboarding, and a scalable long-term acquisition motion. Use after mapping the customer's buying process or when forecasting activities and acquisition cost."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Map the Sales Process

## Goal

A staged seller-side process with channels, activities, conversion assumptions, costs, ownership, evidence, and evolution from early founder sales to scale.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Customer acquisition process and DMU
- Awareness, education, evaluation, and purchase needs
- Channel options and sales resources
- Expected conversion, cycle time, and deal economics
- Short-, medium-, and long-term go-to-market hypotheses

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
