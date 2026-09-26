---
name: map-the-customer-acquisition-process
description: "Maps the customer's internal process from first awareness through evaluation, approvals, contracting, payment, and implementation. Use to expose sales-cycle length, procurement, regulation, budgeting, and other obstacles before forecasting revenue."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Map the Customer Acquisition Process

## Goal

A validated customer-side buying process with stages, owners, artifacts, timing, dependencies, failure modes, and a realistic path to payment.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- DMU map and stakeholder evidence
- Recent comparable purchases
- Budget cycle and purchasing authority
- Procurement, legal, security, regulatory, and implementation requirements
- Payment and vendor-onboarding mechanics

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Choose a concrete customer archetype and start from the trigger that creates active consideration.
2. Reconstruct every customer action and approval through committed funds, contract, payment, and readiness to use.
3. For each stage, record owner, entry condition, exit condition, artifact, elapsed time, and common failure.
4. Overlay budget timing, procurement thresholds, security/legal reviews, regulation, partner dependencies, and implementation capacity.
5. Identify the critical path and stages that can run in parallel.
6. Validate timing with customers and distinguish best case, typical case, and delayed case.
7. Translate the map into seller evidence requirements and forecast milestones without turning it into the seller's sales-process map.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./map-the-customer-acquisition-process-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./map-the-customer-acquisition-process-workbook.md"
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

- Customer acquisition process map
- Stage timing and critical path
- Required artifacts and approvals
- Obstacle and mitigation register
- Forecast implications

The work is complete only when:

- The process ends with payment and implementation readiness, not verbal interest.
- Every stage has a customer-side owner and exit condition.
- Budget and purchasing authority are explicit.
- Timing is grounded in comparable purchases.

## Gotchas

- Do not confuse the customer's buying process with the startup's selling activities.
- A signed agreement may precede payment or implementation by months.
- Security, legal, or vendor onboarding can dominate cycle time.
- Consumer processes can include app-store, household, financing, or platform constraints.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
