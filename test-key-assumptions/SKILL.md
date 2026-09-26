---
name: test-key-assumptions
description: "Designs and runs low-cost, ethical experiments for prioritized venture assumptions with thresholds and decision rules defined in advance. Use after assumptions are ranked or when teams need evidence stronger than interviews and opinions."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Test Key Assumptions

## Goal

Decision-grade experiment results that update confidence and trigger a clear proceed, revise, pivot, or stop action.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Prioritized atomic assumptions
- Current evidence and baseline confidence
- Observable proxy or direct behavior for each assumption
- Resource, time, legal, and ethical constraints
- Decision thresholds and available participants

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

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

## Evidence rules

- Prefer observed behavior, customer artifacts, transactions, and direct interviews over opinion or generic reports.
- Label each material statement as fact, inference, or assumption.
- Record source, date, customer/segment relevance, and confidence for decisive evidence.
- Preserve contradictory evidence and explain how it changes the conclusion.
- Use ranges and scenarios when inputs are uncertain; never hide uncertainty behind precise formatting.

## Completion contract

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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
