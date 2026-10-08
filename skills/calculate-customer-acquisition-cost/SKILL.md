---
name: calculate-customer-acquisition-cost
description: "Calculates fully loaded customer acquisition cost from top-down sales and marketing spending divided by acquired customers, then diagnoses payback and reduction levers. Use to test unit economics or replace unrealistic activity-by-activity acquisition estimates."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Calculate Customer Acquisition Cost

## Goal

A period- and cohort-aligned COCA model including all acquisition costs, with channel views, payback analysis, and reduction priorities.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Sales and marketing spend by period
- Compensation, tools, content, events, discounts, partner fees, and allocated overhead
- Customers acquired by period and channel
- Sales-cycle lag between spend and acquisition
- LTV and contribution schedule for payback comparison

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Define the acquired-customer event and cohort consistently, excluding leads, trials, and renewals unless the model explicitly treats them.
2. Collect fully loaded acquisition spending, including labor and less visible program or channel costs.
3. Align spend with the customers it generated using a reasonable sales-cycle lag.
4. Calculate blended and channel-specific COCA where attribution is credible; preserve unattributed spend rather than deleting it.
5. Compare COCA with LTV, gross contribution, and cash payback timing.
6. Run sensitivity analysis on conversion, cycle time, channel mix, compensation, and organic/referral contribution.
7. Prioritize structural reductions such as product simplification, stronger referrals, shorter cycles, better qualification, or lower-cost channels.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-customer-acquisition-cost-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-customer-acquisition-cost-workbook.md"
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

- Fully loaded spend ledger
- Customer cohort and lag mapping
- Blended and channel COCA
- LTV:COCA and payback analysis
- COCA reduction experiments

The work is complete only when:

- The numerator includes all material acquisition costs.
- The denominator counts acquired paying customers consistently.
- Spend and acquisitions are time-aligned.
- COCA is paired with payback and LTV rather than interpreted alone.

## Gotchas

- Bottom-up 'cost of one sales call' calculations omit failures and overhead.
- Founder labor is not free even if no salary is paid.
- Organic customers can be supported by brand, content, community, or product investments.
- Channel attribution can create false precision; retain a blended view.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
