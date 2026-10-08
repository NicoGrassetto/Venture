---
name: define-product-concept
description: "Creates a low-cost visual product specification and customer-facing brochure that communicate the experience, features, and benefits without premature implementation detail. Use after mapping the lifecycle or when a concept is too vague to test consistently."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Define the Product Concept

## Goal

A shared, testable product concept expressed through visuals, key workflows, boundaries, and benefit-led messaging.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A build-ready technical specification or a feature backlog.

## Inputs and missing data

Collect what is available before starting:

- Persona and full lifecycle use case
- Quantified or qualitative customer priorities
- Known technical, regulatory, and operational constraints
- Assumptions that require concept testing
- Existing sketches, prototypes, or competitor examples

<!-- input-policy:start -->
A concept can be provisional, but define the customer outcome, storyboard, non-goals, and an unled comprehension test.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

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
python3 scripts/create_workbook.py --venture "Venture name" --output "./define-product-concept-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./define-product-concept-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `storyboard`, `concept_test`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [quantify-the-value-proposition](../quantify-the-value-proposition/SKILL.md), [test-key-assumptions](../test-key-assumptions/SKILL.md). Standalone users may need to install these optional follow-ups.
