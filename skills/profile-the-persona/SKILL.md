---
name: profile-the-persona
description: "Selects and deeply profiles one real representative end user in the beachhead, including motivations and prioritized purchasing criteria. Use after the end-user profile when a team needs a concrete decision anchor for product, messaging, and tradeoffs."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Profile the Persona

## Goal

A fact-based primary persona tied to a real person, with observable goals, context, behavior, and prioritized purchasing criteria.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A market-wide profile, a fictional composite presented as real, or a buyer map.

## Inputs and missing data

Collect what is available before starting:

- Validated end-user profile
- Candidate representative users and interview access
- Observed workflows, motivations, frustrations, and social context
- Purchasing and adoption criteria
- Product and positioning decisions the persona must inform

<!-- input-policy:start -->
Use a real representative user's sourced observations and a privacy-safe identifier; do not invent a biography.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Choose one real person who sits near the center of the target profile and is informative, accessible, and credible.
2. Interview and observe the person in context. Capture behavior and artifacts, not only stated preferences.
3. Document goals, fears, incentives, workarounds, environment, influences, and a day-in-the-life narrative.
4. Elicit purchasing criteria by forcing tradeoffs. Rank criteria in order rather than listing everything as important.
5. Separate facts, quotes, observations, interpretations, and untested assumptions.
6. Create a visible persona fact sheet and test whether the team makes the same product tradeoffs when using it.
7. Revisit the persona when next-customer evidence shows it is atypical or market scope changes.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./profile-the-persona-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./profile-the-persona-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `persona`, `purchasing_criteria`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Primary persona fact sheet
- Day-in-the-life and context map
- Prioritized purchasing criteria
- Evidence and assumption annotations
- Decision examples influenced by the persona

The work is complete only when:

- The persona is based on a real target user, not a fictional composite alone.
- Purchasing criteria are explicitly ranked.
- The profile includes emotional and social motivations as well as functional needs.
- The persona changes at least one real product, messaging, or research decision.

## Gotchas

- Do not create multiple equal personas to avoid prioritization.
- Do not substitute a stock photo and demographics for evidence.
- The persona is not automatically the economic buyer.
- A charismatic interviewee may be memorable but unrepresentative.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [map-customer-journey](../map-customer-journey/SKILL.md), [quantify-the-value-proposition](../quantify-the-value-proposition/SKILL.md). Standalone users may need to install these optional follow-ups.
