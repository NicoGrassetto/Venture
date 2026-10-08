---
name: market-segmentation
description: "Generates and researches distinct market opportunities for a new venture using bottom-up primary research. Use when an idea or technology could serve multiple customers, when the target market is vague, or before choosing a beachhead market."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Market Segmentation

## Goal

A broad but evidence-backed map of market segments, each defined by a specific end user, application, and common buying context.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Choosing a winner before comparing distinct customer contexts.

## Inputs and missing data

Collect what is available before starting:

- Core capability or problem hypothesis
- Candidate end users and use cases
- Founder network and routes to interviewees
- Known alternatives and workarounds
- Initial constraints on geography, regulation, or channel

<!-- input-policy:start -->
Use a research plan when no qualified customer observations exist. Keep end user, payer, application, and access distinct.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

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

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `segments`, `comparison`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [select-a-beachhead-market](../select-a-beachhead-market/SKILL.md). Standalone users may need to install these optional follow-ups.
