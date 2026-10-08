---
name: define-the-minimum-viable-business-product
description: "Defines the smallest product that delivers real value, is paid for, and starts a measurable feedback loop across the business system. Use after key assumptions have been tested and before building or launching the first sellable product."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Define the Minimum Viable Business Product

## Goal

A tightly scoped MVBP specification with customer, value, payment, instrumentation, service boundaries, and learning goals.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A disconnected prototype or a long-term feature roadmap.

## Inputs and missing data

Collect what is available before starting:

- Validated persona, value proposition, and core use case
- Key assumption test results
- DMU, acquisition process, business model, and pricing framework
- Technical and operational constraints
- Learning objectives and success metrics

<!-- input-policy:start -->
Scope one complete, safe value-delivery and payment path. Proposed usage or payment is not observed traction.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Name the exact target customer, job, and measurable value the MVBP must deliver.
2. Define the three non-negotiables: sufficient customer value, customer payment, and a feedback loop for learning.
3. Select the minimum end-to-end workflow that proves the business, not merely a technical feature.
4. Separate must-have capabilities from manual operations, concierge work, deferred features, and explicit non-goals.
5. Specify payment terms, onboarding, support, reliability, compliance, and data collection needed for real use.
6. Define success, failure, safety, and stop conditions plus the metrics and qualitative feedback to collect.
7. Review scope against timeline and resources; remove anything that does not prove value or a critical business assumption.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./define-the-minimum-viable-business-product-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./define-the-minimum-viable-business-product-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `scope`, `launch_gates`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- MVBP scope and non-goals
- End-to-end customer workflow
- Payment and service design
- Instrumentation and feedback plan
- Launch gates and stop conditions

The work is complete only when:

- A customer can obtain meaningful value from the complete workflow.
- Payment or an equivalent binding commercial commitment is built into the test.
- Usage and outcome feedback can be measured.
- Manual work is explicit, safe, and not mistaken for scalable economics.

## Gotchas

- A minimum viable product is not automatically a viable business product.
- Do not ship a disconnected feature that cannot deliver the promised outcome.
- Free pilots obscure willingness to pay unless a binding conversion mechanism exists.
- Minimum scope does not excuse unsafe, illegal, or unreliable behavior.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [validate-customer-traction](../validate-customer-traction/SKILL.md), [plan-operations](../plan-operations/SKILL.md). Standalone users may need to install these optional follow-ups.
