---
name: define-your-core
description: "Defines the durable internal capability that lets a venture deliver customer value better than competitors and can be strengthened over time. Use when clarifying defensibility, prioritizing strategic investment, or separating a true core from temporary advantages."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Define Your Core

## Goal

A concise core statement supported by customer relevance, capability evidence, defensibility mechanisms, and a plan to compound it.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Customer value proposition and purchasing priorities
- Team capabilities, assets, data, processes, network, and know-how
- Competitor and status-quo capabilities
- Learning loops and scale effects
- Potential intellectual property or contractual protections

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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
python3 scripts/create_workbook.py --venture "Venture name" --output "./define-your-core-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./define-your-core-workbook.md"
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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
