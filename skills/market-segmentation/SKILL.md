---
name: market-segmentation
description: "Generates and researches distinct market opportunities for a new venture using bottom-up primary research. Use when an idea or technology could serve multiple customers, when the target market is vague, or before choosing a beachhead market."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Market Segmentation

## Goal

A broad but evidence-backed map of market segments, each defined by a specific end user, application, and common buying context.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Core capability or problem hypothesis
- Candidate end users and use cases
- Founder network and routes to interviewees
- Known alternatives and workarounds
- Initial constraints on geography, regulation, or channel

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Brainstorm end-user/application combinations without filtering too early. Treat the same user with a different use case as a different candidate segment.
2. Group candidates only when users share similar needs, buying process, word of mouth, and product requirements.
3. Define each segment narrowly enough that members plausibly reference one another and respond similarly to one product.
4. Conduct exploratory interviews and observation across diverse candidates. Ask about current behavior, consequences, budgets, and alternatives rather than pitching.
5. Create a segment profile for the most promising opportunities: end user, application, pain, current solution, beneficiaries, buyer, market access, and rough scale.
6. Eliminate segments that depend on incompatible products or buying motions; preserve uncertain segments as hypotheses rather than facts.
7. Produce a short list for beachhead selection with evidence strength and unanswered questions.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./market-segmentation-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./market-segmentation-workbook.md"
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

- Market segmentation matrix
- Primary research log with source and date
- Segment profiles for prioritized opportunities
- Evidence/assumption map
- Beachhead candidate shortlist

The work is complete only when:

- Segments are defined by end user plus application, not broad industries.
- Each priority segment includes direct customer evidence.
- Members within a segment share product needs and buying dynamics.
- The shortlist preserves multiple credible options without selecting the beachhead prematurely.

## Gotchas

- A paying customer request can be a distracting one-off rather than a scalable segment.
- Top-down industry categories are usually too broad for an initial market.
- The user, buyer, and beneficiary may be different people or organizations.
- Two-sided markets require segmenting both sides and stating which side constrains adoption.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
