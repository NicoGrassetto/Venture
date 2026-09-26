---
name: show-that-the-dogs-will-eat-the-dog-food
description: "Validates an MVBP with real customer usage, payment, retention, outcomes, and advocacy rather than compliments or sign-ups. Use during early launch to determine whether customers actually consume and value the product."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Show That the Dogs Will Eat the Dog Food

## Goal

An evidence-based product-consumption assessment with cohort trends, payment proof, customer outcomes, root causes, and a scale/iterate/pivot decision.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- MVBP and its success metrics
- Target customer cohorts and acquisition source
- Usage, activation, retention, payment, and outcome data
- Support interactions and qualitative feedback
- Advocacy, referral, or word-of-mouth evidence

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Define activation and meaningful usage based on delivered value, not superficial logins.
2. Instrument the full path from acquisition through onboarding, repeated use, outcome, payment, renewal, and referral.
3. Analyze cohorts over time rather than relying only on cumulative totals.
4. Pair behavioral data with interviews focused on why users progressed, stalled, churned, paid, or advocated.
5. Separate acquisition quality, onboarding friction, product value, reliability, and pricing as possible causes.
6. Compare results with predeclared MVBP thresholds and examine trends, not isolated anecdotes.
7. Decide to scale, iterate, narrow the market, revise the offer, or stop; specify the next evidence required.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./show-that-the-dogs-will-eat-the-dog-food-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./show-that-the-dogs-will-eat-the-dog-food-workbook.md"
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

- Consumption metric definitions
- Cohort funnel and retention analysis
- Payment and outcome evidence
- Root-cause synthesis
- Scale/iterate/pivot decision

The work is complete only when:

- Metrics reflect meaningful customer value.
- Real customers use and pay, or a documented binding payment path exists.
- Retention and repeated use are analyzed by cohort.
- The team acts on negative evidence with intellectual honesty.

## Gotchas

- Registrations, downloads, and compliments do not prove consumption.
- Aggregate growth can hide deteriorating cohorts.
- Heavy founder intervention can inflate engagement.
- Advocacy is stronger when customers act - refer, invite, review, or stake reputation.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
