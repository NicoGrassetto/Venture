---
name: build-an-end-user-profile
description: "Builds a demographic, behavioral, and contextual profile of the beachhead market's end users. Use after selecting a beachhead, when the target customer is still abstract, or to define who should and should not be included in customer research."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Build an End User Profile

## Goal

A research-backed end-user profile that makes the beachhead concrete and guides recruiting, product decisions, and later persona selection.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Beachhead market definition
- Interview notes and observed customer behavior
- User attributes that change needs or adoption
- Environmental, workflow, and technology context
- Known exclusions and edge cases

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Separate end users from economic buyers, influencers, and beneficiaries before profiling.
2. List candidate attributes across demographic, psychographic, behavioral, workflow, and environmental dimensions.
3. Retain only attributes that materially change the need, product use, adoption, or ability to reach the user.
4. Estimate ranges and distributions from evidence; do not invent false precision or an average person who does not exist.
5. Write inclusion and exclusion criteria that a researcher could use to recruit the right interviewees.
6. Check whether anyone on the founding team fits the profile; use the answer to identify empathy or access gaps, not to override research.
7. Validate the profile with additional interviews and revise contradictions.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./build-an-end-user-profile-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./build-an-end-user-profile-workbook.md"
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

- End-user profile
- Attribute evidence table
- Recruiting screener
- Inclusion and exclusion rules
- Founder empathy/access gap note

The work is complete only when:

- Every retained attribute has a stated decision consequence.
- The profile describes users, not the organization buying the product.
- Recruiting criteria can identify matching users consistently.
- The profile is broad enough to contain a market but specific enough to guide product choices.

## Gotchas

- Avoid decorative demographics that do not affect behavior.
- Do not collapse buyer and user into one profile without evidence.
- Do not treat founders who resemble users as sufficient research.
- Do not use stereotypes where direct evidence is available.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
