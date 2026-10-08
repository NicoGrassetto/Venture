---
name: identify-key-assumptions
description: "Decomposes the venture plan into specific, falsifiable assumptions and ranks them by impact and uncertainty. Use before designing experiments, when a plan hides unsupported beliefs, or to focus validation effort on venture-killing risks."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Identify Key Assumptions

## Goal

A complete assumption register with atomic statements, evidence status, dependency links, risk ranking, and test priority.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Artifacts from market, product, value, DMU, business model, pricing, and economics work
- Forecasts and calculations with key drivers
- Claims that rely on customer behavior or third parties
- Technical, regulatory, operational, and team constraints
- Current evidence and its limitations

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Walk through every prior artifact and convert material claims into explicit assumptions.
2. Break compound assumptions into atomic statements that one experiment could address.
3. Phrase each assumption so evidence could prove it wrong; include population, behavior, threshold, and time where relevant.
4. Classify assumptions across desirability, viability, feasibility, usability, channel, legal/regulatory, and team execution.
5. Record existing evidence, confidence, dependencies, and consequence if false.
6. Rank by impact and uncertainty, then identify leap-of-faith assumptions and dependency bottlenecks.
7. Select the next assumptions to test without designing the experiments yet.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./identify-key-assumptions-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./identify-key-assumptions-workbook.md"
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

- Atomic assumption register
- Evidence and confidence assessment
- Impact/uncertainty ranking
- Dependency map
- Prioritized test queue

The work is complete only when:

- Each assumption is specific enough for one focused test.
- High-impact assumptions from all major venture dimensions are included.
- Existing evidence is separated from confidence or opinion.
- Priority follows risk, not ease or team preference.

## Gotchas

- Do not hide several beliefs inside one sentence.
- Do not skip an assumption because it seems difficult to test.
- A forecast output is not an assumption; its causal inputs are.
- Avoid ranking only customer desirability while ignoring feasibility or economics.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
