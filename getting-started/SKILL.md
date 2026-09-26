---
name: getting-started
description: "Turns a founder's interests, capabilities, idea, or technology into a testable venture starting point and a committed founding-team plan. Use when someone wants to start a company but lacks a focused idea, needs to compare idea sources, or must identify founding-team gaps before market work."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
  framework: disciplined-entrepreneurship
---

# Getting Started

## Goal

A venture thesis with a clearly stated source, founder motivation, initial capabilities, team gaps, and a short list of ideas ready for market segmentation.

This skill is a decision workflow, not a chapter summary. Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Founder motivations, values, and definition of success
- Existing ideas, technologies, domain access, or observed problems
- Founder skills, credibility, network, time, and financial constraints
- Potential cofounders and evidence of prior collaboration
- Non-negotiables such as geography, ethics, timing, or industry exclusions

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Classify the starting point as idea-led, technology-led, or passion/capability-led. Do not pretend these paths have identical evidence needs.
2. For a passion-led start, inventory recurring problems the team has privileged access to observe. Convert each into a problem statement without embedding a solution.
3. For an idea- or technology-led start, separate the underlying capability from its current application and list at least five plausible customer contexts.
4. Score candidate directions on founder commitment, unfair access to learning, urgency of the problem, plausible customer budget, and time to first evidence.
5. Run founder-alignment conversations covering ambition, roles, equity philosophy, decision rights, availability, and conflict handling.
6. Select a provisional venture thesis, explicitly label it as a hypothesis, and hand the candidate applications to market segmentation.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./getting-started-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./getting-started-workbook.md"
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

- Founder motivation and constraints brief
- Capability and access inventory
- Candidate problem/application list with evidence
- Founding-team gap map and recruiting priorities
- Provisional venture thesis and next research action

The work is complete only when:

- The thesis names a customer context and problem, not only a product.
- At least one founder has credible access to prospective users or domain evidence.
- Team members have discussed commitment, roles, and conflict expectations explicitly.
- The team can explain why it will spend the next several years on this problem.

## Gotchas

- Do not confuse enthusiasm for a technology with evidence of customer demand.
- Do not force a permanent idea choice before market segmentation.
- Do not use complementary resumes as a substitute for trust and shared values.
- Avoid recruiting a large team before the venture thesis has earned focus.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
