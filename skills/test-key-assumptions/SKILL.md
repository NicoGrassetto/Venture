---
name: test-key-assumptions
description: "Designs and runs low-cost, ethical experiments for prioritized venture assumptions with thresholds and decision rules defined in advance. Use after assumptions are ranked or when teams need evidence stronger than interviews and opinions."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Test Key Assumptions

## Goal

Decision-grade experiment results that update confidence and trigger a clear proceed, revise, pivot, or stop action.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Claiming an experiment ran when only its protocol exists or changing thresholds after seeing results.

## Inputs and missing data

Collect what is available before starting:

- Prioritized atomic assumptions
- Current evidence and baseline confidence
- Observable proxy or direct behavior for each assumption
- Resource, time, legal, and ethical constraints
- Decision thresholds and available participants

<!-- input-policy:start -->
Use research-plan mode before authorized execution. Completed analysis requires dated observations, the precommitted threshold, and an evidence-following decision.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Select the highest-risk testable assumption, respecting dependency order.
2. Choose the cheapest experiment that can produce behaviorally relevant evidence without creating unacceptable false positives.
3. Define hypothesis, population, method, metric, pass/fail threshold, sample rationale, duration, and decision rule before launch.
4. Identify confounds, selection bias, instrumentation risk, and ethical or legal constraints.
5. Run the experiment consistently and preserve raw observations.
6. Analyze results against the precommitted rule; report uncertainty and surprising evidence.
7. Update the assumption register and decide to proceed, revise, pivot, stop, or run a stronger test.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./test-key-assumptions-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./test-key-assumptions-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `experiments`, `results`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Experiment brief
- Instrumentation and raw-data plan
- Results analysis
- Updated assumption confidence
- Decision and next experiment

The work is complete only when:

- The threshold and decision rule are set before observing results.
- The measured behavior is meaningfully connected to the assumption.
- Results include failures, drop-offs, and contradictory evidence.
- The decision follows the evidence rather than post-hoc rationalization.

## Gotchas

- Survey intent is weaker than actual behavior or commitment.
- A landing-page click may test messaging rather than willingness to pay.
- Do not lower a threshold after seeing disappointing results.
- Avoid experiments that deceive, harm, or create obligations the team cannot fulfill.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [identify-key-assumptions](../identify-key-assumptions/SKILL.md), [define-the-minimum-viable-business-product](../define-the-minimum-viable-business-product/SKILL.md). Standalone users may need to install these optional follow-ups.
