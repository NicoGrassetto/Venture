---
name: discover-venture
description: "Understands the founder's intended venture through focused follow-up questions, a reflected and confirmed brief, and explicit constraints and unknowns. Use when starting or clarifying a venture, comparing ideas, or identifying team and evidence gaps before market work."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Discover a Venture

## Goal

A venture thesis with a clearly stated source, founder motivation, initial capabilities, team gaps, and a short list of ideas ready for market segmentation.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Use when / not for

Use this skill for the decision described in the goal.
Not for: Product design, market sizing, or inventing a venture from a one-line pitch.

## Inputs and missing data

Collect what is available before starting:

- Founder motivations, values, and definition of success
- Existing ideas, technologies, domain access, or observed problems
- Founder skills, credibility, network, time, and financial constraints
- Potential cofounders and evidence of prior collaboration
- Non-negotiables such as geography, ethics, timing, or industry exclusions

Missing market evidence need not block exploration. Mark unknowns, state their
decision impact, and turn the most consequential unknowns into research actions.
Missing understanding of the founder's intent requires clarification, not
invented answers.

<!-- input-policy:start -->
Clarify intent with the founder. A completed analysis needs an actual reflected summary and explicit founder confirmation; silence is not confirmation.

Use `draft` for unfinished work, `research-plan` for a completed protocol, and `completed-analysis` only for an analysis actually performed. Never invent observations, founder approval, or external actions.
<!-- input-policy:end -->

## Founder discovery

Treat a one-sentence pitch as a starting point, not a complete venture brief.
Read existing material first, then ask focused questions one at a time and
follow up on the answers. Establish:

- The target customer, problem, current workaround, and a concrete example
- The intended solution, differentiation, payer, and business model hypothesis
- The current stage, work already done, and evidence versus expectations
- Founder motivation, capabilities, resources, constraints, and non-negotiables
- The purpose of the plan, intended audience, and decision it must support

Do not demand a fixed number of answers or repeat questions already resolved
by supplied material. Explicitly record genuine unknowns and their next tests.
Reflect the understanding back to the founder, invite corrections, and obtain
explicit confirmation before calling the brief complete. Save the questions,
answers, corrections, and confirmation source and date with the working
artifact. If the founder is unavailable, leave the brief provisional and record
the next question; do not simulate consent or claim the founder was interviewed.

## Workflow

1. Classify the starting point as idea-led, technology-led, or passion/capability-led. Do not pretend these paths have identical evidence needs.
2. For a passion-led start, inventory recurring problems the team has privileged access to observe. Convert each into a problem statement without embedding a solution.
3. For an idea- or technology-led start, separate the underlying capability from its current application and compare plausible customer contexts without padding a list to meet an arbitrary count.
4. Score candidate directions on founder commitment, unfair access to learning, urgency of the problem, plausible customer budget, and time to first evidence.
5. With cofounders, discuss ambition, roles, equity philosophy, decision rights, availability, and conflict handling. For a solo founder, document capacity, missing ownership, and decision constraints.
6. Select a provisional venture thesis, explicitly label it as a hypothesis, and hand the candidate applications to market segmentation.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./discover-venture-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./discover-venture-workbook.md"
```

Fix every validation error. Warnings may remain only when the workbook explicitly explains the missing evidence and next action.

## Output contract

Use [the task-specific workbook](assets/workbook.md). Its structured record contains these result tables: `venture`, `constraints`.

Read [the record format](references/record-format.md) for stages, evidence, and units, and [the synthetic worked example](references/example.md) for a complete result and failure case.
A research plan leaves result tables empty and supplies a testable protocol instead.

## Evidence rules

Separate facts, inferences, and assumptions. Cite stable evidence IDs with sources, dates, confidence, and contradictions. Forecasts are not observations.
Preserve negative results and define the next useful test. Obtain authorization before outreach, spending, publication, or commitments; protect identifying data.

## Deliverable and completion checks

Apply the outcome criteria below to `completed-analysis`. A `research-plan` can be complete as a protocol but does not satisfy observed-result criteria.

Produce:

- Founder motivation and constraints brief
- Capability and access inventory
- Candidate problem/application list with evidence
- Founding-team gap map and recruiting priorities
- Provisional venture thesis and next research action

The work is complete only when:

- The founder has confirmed the reflected understanding of the intended venture.
- The thesis names a customer context and problem, not only a product.
- At least one founder has credible access to prospective users or domain evidence.
- Cofounders have discussed commitment, roles, and conflict expectations; a solo founder has documented capacity and ownership gaps.
- The team can explain why it will spend the next several years on this problem.

## Gotchas

- Do not confuse enthusiasm for a technology with evidence of customer demand.
- Do not force a permanent idea choice before market segmentation.
- Do not use complementary resumes as a substitute for trust and shared values.
- Avoid recruiting a large team before the venture thesis has earned focus.

## Handoff

Record the decision, declared stage, supporting and contradicting evidence, remaining uncertainty, and one next action with owner and date. Name any upstream artifact invalidated by the result.

Next skills, when their inputs are ready: [identify-key-assumptions](../identify-key-assumptions/SKILL.md), [market-segmentation](../market-segmentation/SKILL.md). Standalone users may need to install these optional follow-ups.
