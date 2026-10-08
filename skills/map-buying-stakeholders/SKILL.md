---
name: map-buying-stakeholders
description: "Maps the decision-making unit for acquiring the product, including champion, primary economic buyer, end user, influencers, and veto holders. Use for B2B or complex consumer purchases when adoption depends on multiple stakeholders."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Map Buying Stakeholders

## Goal

A role-based, named DMU map showing each stakeholder's criteria, influence, evidence needs, objections, and relationships.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: The sequence of purchase steps or assuming that the user controls the budget.

## Inputs and missing data

Collect what is available before starting:

- Persona and product use context
- Actual recent purchase examples
- Organizational structure or household decision context
- Budget ownership and authorization rules
- Technical, legal, security, procurement, or social influences

<!-- input-policy:start -->
Adapt to the buying context: one person may hold several roles in a simple purchase; complex purchases need separately evidenced authority and veto power.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Workflow

1. Start from a recent comparable purchase and reconstruct who initiated, evaluated, approved, blocked, paid, used, and implemented it.
2. Identify the champion and primary economic buyer first, then map end users, influencers, procurement, and veto power.
3. Name real people or role titles where possible; avoid generic labels with no organizational location.
4. For each role, document success criteria, fears, authority, evidence required, and likely objections.
5. Map relationships, information flow, and conflicts between roles.
6. Identify missing access and define a plan for the champion to reach stakeholders the team cannot reach directly.
7. Validate the map across comparable buying contexts. Use organizations for B2B and actual individual or household decisions for consumer purchases.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./map-buying-stakeholders-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./map-buying-stakeholders-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `stakeholders`, `relationships`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- DMU role map
- Named stakeholder table
- Criteria and objection matrix
- Relationship/influence map
- Access and evidence plan

The work is complete only when:

- Champion and primary economic buyer are identified separately unless evidence proves they are the same.
- Potential veto holders are explicit.
- Each stakeholder has role-specific success criteria and proof needs.
- The map is based on actual purchasing behavior, not only an org chart.

## Gotchas

- Job title does not reliably reveal buying authority.
- A friendly end user is not necessarily a champion with influence.
- Procurement may negotiate but not own the economic decision.
- Consumer purchases can still involve multiple influencers and vetoes.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [map-customer-buying-process](../map-customer-buying-process/SKILL.md). Standalone users may need to install these optional follow-ups.
