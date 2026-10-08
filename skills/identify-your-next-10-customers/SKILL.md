---
name: identify-your-next-10-customers
description: "Identifies and interviews at least ten additional beachhead customers to test whether the persona, needs, value proposition, and product assumptions generalize. Use before deep product investment or when existing evidence depends on only a few friendly contacts."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Identify Your Next 10 Customers

## Goal

A named pipeline of representative customers and a cross-customer evidence synthesis that confirms, revises, or rejects prior assumptions.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Beachhead definition and recruiting criteria
- Persona, lifecycle, product concept, and value hypotheses
- Existing interview network and referral paths
- A consistent discussion and observation guide
- Criteria for confirming or revising assumptions

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Create a list of at least ten named, reachable customers that fit the beachhead independently of personal enthusiasm.
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
python3 scripts/create_workbook.py --venture "Venture name" --output "./identify-your-next-10-customers-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./identify-your-next-10-customers-workbook.md"
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

- Named next-10 customer list
- Interview protocol and research log
- Cross-customer evidence matrix
- Revised upstream assumptions
- Proceed/pivot/research-more decision

The work is complete only when:

- At least ten qualified customers are named or a documented recruiting plan explains remaining gaps.
- Evidence is compared across customers using consistent fields.
- Negative feedback changes analysis rather than being dismissed.
- The decision states what evidence would reverse it.

## Gotchas

- Do not count advisors, investors, or non-target users as customers.
- Do not pitch so heavily that interviews become sales calls.
- Referrals from one source can create a misleadingly homogeneous sample.
- Ten interviews are a checkpoint, not a statistically magical number.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
