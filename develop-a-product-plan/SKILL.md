---
name: develop-a-product-plan
description: "Develops an evidence-driven product roadmap from the validated beachhead product into adjacent markets while preserving near-term focus. Use after MVBP consumption evidence to sequence capability, platform, and market expansion."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Develop a Product Plan

## Goal

A product and market evolution plan with horizons, dependencies, learning gates, resource implications, and explicit protection of beachhead execution.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- MVBP usage, payment, retention, and customer outcome evidence
- Beachhead gaps and customer requests
- Follow-on market analysis
- Core capability and architecture implications
- Resource, hiring, partner, and capital constraints

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Summarize what the beachhead evidence proves, disproves, and leaves uncertain.
2. Define product horizons: harden the beachhead, expand within it, enter the next adjacency, and enable longer-term platform options.
3. Map customer outcomes and market-entry goals before listing features.
4. Identify reusable capabilities, technical or operational foundations, and dependencies that unlock several future moves.
5. Sequence initiatives by evidence, strategic leverage, risk, and resource constraints; set learning or traction gates between horizons.
6. Explicitly defer attractive ideas that would distract from current customer value and retention.
7. Create a review cadence that updates the plan when evidence changes without turning it into a constantly shifting wish list.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./develop-a-product-plan-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./develop-a-product-plan-workbook.md"
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

- Evidence baseline
- Product horizons and outcomes
- Capability/dependency map
- Sequenced roadmap with gates
- Deferred opportunities and review cadence

The work is complete only when:

- Near-term work improves beachhead value, reliability, retention, or economics.
- Follow-on initiatives have explicit market and evidence triggers.
- Features trace to customer outcomes or enabling capabilities.
- The plan respects real resource and dependency constraints.

## Gotchas

- A roadmap is not a chronological feature wish list.
- Do not let distant TAM distract from current consumption evidence.
- Customer requests may be one-offs that weaken the focused product.
- Plans should change with evidence, but priorities need stable decision rules.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
