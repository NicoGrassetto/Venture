---
name: build-an-end-user-profile
description: "Builds a demographic, behavioral, and contextual profile of the beachhead market's end users. Use after selecting a beachhead, when the target customer is still abstract, or to define who should and should not be included in customer research."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Build an End-user Profile

## Goal

A research-backed end-user profile that makes the beachhead concrete and guides recruiting, product decisions, and later persona selection.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Profiling the paying organization or replacing customer research with decorative demographics.

## Inputs and missing data

Collect what is available before starting:

- Beachhead market definition
- Interview notes and observed customer behavior
- User attributes that change needs or adoption
- Environmental, workflow, and technology context
- Known exclusions and edge cases

<!-- input-policy:start -->
Separate users from buyers and beneficiaries. With no observations, create a recruiting plan rather than claim a validated profile.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

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

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `attributes`, `screener`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [profile-the-persona](../profile-the-persona/SKILL.md), [validate-with-customers](../validate-with-customers/SKILL.md). Standalone users may need to install these optional follow-ups.
