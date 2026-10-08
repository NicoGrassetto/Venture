---
name: calculate-customer-lifetime-value
description: "Calculates discounted contribution profit from an average acquired customer using retention, revenue, gross margin, service cost, and cost of capital. Use to assess unit economics, compare with acquisition cost, or identify the highest-leverage LTV drivers."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Calculate Customer Lifetime Value

## Goal

A cohort-aware, sensitivity-tested LTV model using contribution economics and explicit retention assumptions.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Revenue schedule by customer or cohort
- Gross margin and customer-specific service costs
- Retention, churn, repeat purchase, or contract duration
- Expansion, contraction, maintenance, and renewal assumptions
- Discount rate and time horizon appropriate for startup risk

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Define the customer unit and acquisition cohort so revenue and costs are attributed consistently.
2. Model periodic revenue, gross profit, ongoing support/service cost, retention probability, and expansion or contraction.
3. Exclude acquisition cost from LTV so it can be compared separately with COCA.
4. Discount future contribution using a rate that reflects timing and risk.
5. Calculate conservative, base, and upside cases and identify the highest-sensitivity drivers.
6. Compare modeled assumptions with observed cohort data where available; label unsupported estimates.
7. Set an LTV improvement agenda focused on retention, margin, expansion, or service efficiency.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-customer-lifetime-value-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-customer-lifetime-value-workbook.md"
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

- LTV cash-flow model
- Retention and contribution assumptions
- Discounted low/base/high LTV
- Sensitivity analysis
- LTV improvement priorities

The work is complete only when:

- LTV uses contribution profit, not revenue.
- Acquisition cost is excluded from the LTV numerator.
- Retention and time horizon are explicit and cohort-consistent.
- Future cash flows are discounted and sensitivity-tested.

## Gotchas

- Do not use 1/churn mechanically when data is immature or churn is non-constant.
- Annual contracts do not guarantee indefinite renewals.
- Customer success, support, hosting, and fulfillment may be customer-specific costs.
- An LTV:COCA target is a diagnostic, not proof of cash-flow viability or payback speed.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
