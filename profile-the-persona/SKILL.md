---
name: profile-the-persona
description: "Selects and deeply profiles one real representative end user in the beachhead, including motivations and prioritized purchasing criteria. Use after the end-user profile when a team needs a concrete decision anchor for product, messaging, and tradeoffs."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Profile the Persona

## Goal

A fact-based primary persona tied to a real person, with observable goals, context, behavior, and prioritized purchasing criteria.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Validated end-user profile
- Candidate representative users and interview access
- Observed workflows, motivations, frustrations, and social context
- Purchasing and adoption criteria
- Product and positioning decisions the persona must inform

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
