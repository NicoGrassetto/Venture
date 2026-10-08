---
name: determine-the-customer-dmu
description: "Maps the decision-making unit for acquiring the product, including champion, primary economic buyer, end user, influencers, and veto holders. Use for B2B or complex consumer purchases when adoption depends on multiple stakeholders."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Determine the Customer DMU

## Goal

A role-based, named DMU map showing each stakeholder's criteria, influence, evidence needs, objections, and relationships.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Persona and product use context
- Actual recent purchase examples
- Organizational structure or household decision context
- Budget ownership and authorization rules
- Technical, legal, security, procurement, or social influences

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Start from a recent comparable purchase and reconstruct who initiated, evaluated, approved, blocked, paid, used, and implemented it.
2. Identify the champion and primary economic buyer first, then map end users, influencers, procurement, and veto power.
3. Name real people or role titles where possible; avoid generic labels with no organizational location.
4. For each role, document success criteria, fears, authority, evidence required, and likely objections.
5. Map relationships, information flow, and conflicts between roles.
6. Identify missing access and define a plan for the champion to reach stakeholders the team cannot reach directly.
7. Validate the map with more than one organization because role titles and authority vary.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./determine-the-customer-dmu-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./determine-the-customer-dmu-workbook.md"
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

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
