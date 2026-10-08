---
name: map-customer-journey
description: "Maps the customer's complete experience from recognizing a need through discovery, purchase, onboarding, use, support, value realization, renewal, and advocacy. Use when a team is focused only on product usage and may be missing adoption barriers."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Map the Customer Journey

## Goal

A visual end-to-end customer journey that exposes every required interaction, stakeholder, dependency, and adoption risk around the product.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Only the product's screens or only the seller's sales funnel.

## Inputs and missing data

Collect what is available before starting:

- Persona and prioritized purchasing criteria
- Current customer workflow and alternatives
- Decision-making unit and acquisition evidence if available
- Product concept and expected operating environment
- Support, integration, renewal, disposal, and switching implications

<!-- input-policy:start -->
Map the current journey before the proposed one; include purchase, use, support, and renewal where relevant.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Set the lifecycle boundaries from initial trigger through post-use, renewal, replacement, or disposal.
2. Map the current journey without the product before mapping the future journey.
3. For each stage, record actor, action, channel, artifact, decision, emotion, time, cost, and failure mode.
4. Include discovery, evaluation, authorization, installation, onboarding, training, support, measurement, payment, renewal, and advocacy where relevant.
5. Mark handoffs between users, buyers, IT, legal, operations, partners, or other stakeholders.
6. Identify barriers that the product alone does not solve and assign mitigation owners.
7. Validate the map through customer walkthroughs and revise any stage customers describe differently.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./map-customer-journey-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./map-customer-journey-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `journey`, `barriers`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Current-state lifecycle map
- Future-state lifecycle map
- Stakeholder and handoff overlay
- Adoption barrier register
- Validation notes and design implications

The work is complete only when:

- The map begins before product use and ends after value realization.
- Each stage names an actor and observable action.
- Non-product barriers and organizational handoffs are visible.
- Target customers have reviewed the sequence.

## Gotchas

- A product use case is only one portion of the full lifecycle.
- Do not omit payment, support, renewal, switching, or disposal because they feel operational.
- Do not map the ideal future state before understanding the current state.
- Different actors may own adjacent stages and create hidden failure points.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [define-product-concept](../define-product-concept/SKILL.md), [map-customer-buying-process](../map-customer-buying-process/SKILL.md). Standalone users may need to install these optional follow-ups.
