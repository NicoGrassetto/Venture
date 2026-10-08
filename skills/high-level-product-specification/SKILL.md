---
name: high-level-product-specification
description: "Creates a low-cost visual product specification and customer-facing brochure that communicate the experience, features, and benefits without premature implementation detail. Use after mapping the lifecycle or when a concept is too vague to test consistently."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# High-Level Product Specification

## Goal

A shared, testable product concept expressed through visuals, key workflows, boundaries, and benefit-led messaging.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Persona and full lifecycle use case
- Quantified or qualitative customer priorities
- Known technical, regulatory, and operational constraints
- Assumptions that require concept testing
- Existing sketches, prototypes, or competitor examples

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Select the few product interactions that prove the core customer value and lifecycle fit.
2. Create sketches, storyboards, diagrams, or wireframes at deliberately low fidelity.
3. Describe inputs, outputs, user actions, system behavior, and boundaries without specifying unnecessary implementation.
4. Annotate every major feature with the customer problem and benefit it serves.
5. Create a one-page brochure using customer language: problem, promise, key benefits, proof or rationale, and next action.
6. Test comprehension and desirability with target customers without leading them through the concept.
7. Revise cheaply; record requests that are out of scope rather than adding them automatically.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./high-level-product-specification-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./high-level-product-specification-workbook.md"
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

- Visual high-level product specification
- Core workflow/storyboard
- Scope and non-goals
- Benefit-led product brochure
- Concept test findings and revisions

The work is complete only when:

- A target customer can explain the product and benefit after reviewing the artifact.
- Features trace to persona priorities or lifecycle barriers.
- The artifact is cheap to revise and does not imply false implementation certainty.
- Non-goals prevent feedback from expanding scope silently.

## Gotchas

- Do not build a detailed prototype merely to make the concept feel real.
- Do not list features without connecting them to customer benefits.
- Avoid internal jargon and technical architecture in customer-facing material.
- Do not treat positive politeness as validated demand.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
