---
name: identify-key-assumptions
description: "Decomposes the venture plan into specific, falsifiable assumptions and ranks them by impact and uncertainty. Use before designing experiments, when a plan hides unsupported beliefs, or to focus validation effort on venture-killing risks."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Identify Key Assumptions

## Goal

A complete assumption register with atomic statements, evidence status, dependency links, risk ranking, and test priority.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Turning verified facts into guesses or designing experiments before prioritizing the risk.

## Inputs and missing data

Collect what is available before starting:

- Artifacts from market, product, value, DMU, business model, pricing, and economics work
- Forecasts and calculations with key drivers
- Claims that rely on customer behavior or third parties
- Technical, regulatory, operational, and team constraints
- Current evidence and its limitations

<!-- input-policy:start -->
Start after founder discovery, not only after a full plan exists. Rank desirability, viability, feasibility, operational, and team uncertainties.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Start with the founder brief and available artifacts. Separate verified facts from uncertain causal claims, and record the latter as explicit assumptions without demoting facts to guesses.
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

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `assumptions`, `test_queue`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

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

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [test-key-assumptions](../test-key-assumptions/SKILL.md). Standalone users may need to install these optional follow-ups.
