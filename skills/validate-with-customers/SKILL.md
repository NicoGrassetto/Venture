---
name: validate-with-customers
description: "Recruits qualified customers and synthesizes interviews or observations to test whether the customer profile, needs, value proposition, and product assumptions generalize. Use before deep product investment or when evidence depends on a few friendly contacts; distinguish a recruiting plan from completed research."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Validate with Customers

## Goal

A named pipeline of representative customers and a cross-customer evidence synthesis that confirms, revises, or rejects prior assumptions.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A lead list, a sales pitch, or claiming that a sample size proves the whole market.

## Inputs and missing data

Collect what is available before starting:

- Beachhead definition and recruiting criteria
- Persona, lifecycle, product concept, and value hypotheses
- Existing interview network and referral paths
- A consistent discussion and observation guide
- Criteria for confirming or revising assumptions

<!-- input-policy:start -->
Research-plan mode covers recruitment only. Completed analysis needs qualified participants, observed behavior, cross-customer synthesis, and an explicit sample limitation.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Define a justified target sample and recruiting criteria before collecting evidence. Use privacy-safe participant IDs and recruit independently of personal enthusiasm.
2. Diversify sources and avoid filling the list entirely with friends, one channel, or one organization.
3. Use a consistent protocol while allowing follow-up on unexpected evidence.
4. Capture current behavior, urgency, alternatives, buying context, value metrics, and reaction to the concept.
5. Code findings across customers rather than summarizing interviews one at a time.
6. Identify patterns, outliers, contradictions, and selection bias; revise the persona and upstream artifacts where required.
7. Decide whether evidence supports proceeding, further segmentation, or beachhead reconsideration.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./validate-with-customers-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./validate-with-customers-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `participants`, `synthesis`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Qualified participant list and target-sample rationale
- Interview protocol and research log
- Cross-customer evidence matrix
- Revised upstream assumptions
- Proceed/pivot/research-more decision

The work is complete only when:

- Actual qualified-customer observations are recorded, not merely a recruiting plan.
- A sample below its declared target produces an explicitly inconclusive result and a plan to close the gap.
- Evidence is compared across customers using consistent fields.
- Negative feedback changes analysis rather than being dismissed.
- The decision states what evidence would reverse it.

## Gotchas

- Do not count advisors, investors, or non-target users as customers.
- Do not pitch so heavily that interviews become sales calls.
- Referrals from one source can create a misleadingly homogeneous sample.
- A sample-size target is a learning checkpoint, not statistical proof that the whole market behaves alike.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [select-a-beachhead-market](../select-a-beachhead-market/SKILL.md), [profile-the-persona](../profile-the-persona/SKILL.md), [identify-key-assumptions](../identify-key-assumptions/SKILL.md). Standalone users may need to install these optional follow-ups.
