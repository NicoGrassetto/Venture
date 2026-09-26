---
name: define-the-minimum-viable-business-product
description: "Defines the smallest product that delivers real value, is paid for, and starts a measurable feedback loop across the business system. Use after key assumptions have been tested and before building or launching the first sellable product."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Define the Minimum Viable Business Product

## Goal

A tightly scoped MVBP specification with customer, value, payment, instrumentation, service boundaries, and learning goals.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Validated persona, value proposition, and core use case
- Key assumption test results
- DMU, acquisition process, business model, and pricing framework
- Technical and operational constraints
- Learning objectives and success metrics

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
