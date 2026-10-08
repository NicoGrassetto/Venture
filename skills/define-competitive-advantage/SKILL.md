---
name: define-competitive-advantage
description: "Defines the durable internal capability that lets a venture deliver customer value better than competitors and can be strengthened over time. Use when clarifying defensibility, prioritizing strategic investment, or separating a true core from temporary advantages."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Define Competitive Advantage

## Goal

A concise core statement supported by customer relevance, capability evidence, defensibility mechanisms, and a plan to compound it.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: A feature list or a customer-facing positioning chart.

## Inputs and missing data

Collect what is available before starting:

- Customer value proposition and purchasing priorities
- Team capabilities, assets, data, processes, network, and know-how
- Competitor and status-quo capabilities
- Learning loops and scale effects
- Potential intellectual property or contractual protections

<!-- input-policy:start -->
Trace a durable capability to customer value; when durability is unproven, keep it a hypothesis with a test and investment plan.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. List candidate sources of advantage: network effects, customer service, lowest cost, user experience, data, process, domain knowledge, or another compounding capability.
2. Trace each candidate to a customer outcome that matters in the beachhead.
3. Test rarity, difficulty of imitation, transferability, durability, and the team's ability to improve it.
4. Distinguish the core capability from product features, positioning, early entry, patents alone, or supplier arrangements.
5. Select one primary core and write it as a capability plus compounding mechanism, not a slogan.
6. Define investments, metrics, and operating choices that strengthen the core; identify tempting work that would dilute it.
7. Recheck fit as customer evidence evolves, but do not change the core casually.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./define-competitive-advantage-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./define-competitive-advantage-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `advantages`, `investments`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Core candidate analysis
- Selected core statement
- Customer-value trace
- Defensibility and imitation analysis
- Core-strengthening roadmap and metrics

The work is complete only when:

- The core directly improves a customer priority.
- Competitors cannot reproduce it quickly by copying a feature.
- The venture can invest in and measure its strengthening over time.
- The statement is narrow enough to guide resource allocation.

## Gotchas

- First-mover status is not a durable core.
- A patent may support a core but rarely constitutes the full capability.
- Culture is too vague unless translated into repeatable behaviors and outcomes.
- Competitive position describes perception; core describes the capability producing advantage.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [chart-your-competitive-position](../chart-your-competitive-position/SKILL.md), [develop-a-product-plan](../develop-a-product-plan/SKILL.md). Standalone users may need to install these optional follow-ups.
