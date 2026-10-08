---
name: full-life-cycle-use-case
description: "Maps the customer's complete experience from recognizing a need through discovery, purchase, onboarding, use, support, value realization, renewal, and advocacy. Use when a team is focused only on product usage and may be missing adoption barriers."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Full Life Cycle Use Case

## Goal

A visual end-to-end customer journey that exposes every required interaction, stakeholder, dependency, and adoption risk around the product.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Persona and prioritized purchasing criteria
- Current customer workflow and alternatives
- Decision-making unit and acquisition evidence if available
- Product concept and expected operating environment
- Support, integration, renewal, disposal, and switching implications

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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
python3 scripts/create_workbook.py --venture "Venture name" --output "./full-life-cycle-use-case-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./full-life-cycle-use-case-workbook.md"
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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
