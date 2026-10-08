---
name: calculate-follow-on-markets-tam
description: "Sizes adjacent follow-on markets and shows a credible expansion sequence beyond the beachhead without diluting current focus. Use to test long-term potential, support product-platform decisions, or communicate a growth path."
license: MIT
metadata:
  author: entrepreneurship-skills
  version: "1.0.0"
---

# Calculate Follow-on Markets TAM

## Goal

A directional broader-TAM model and prioritized adjacency roadmap linked to transferable product, channel, brand, data, and capability advantages.

Produce an evidence-backed artifact, expose uncertainty, and end with a clear decision or next test.

## Required context

Collect what is available before starting:

- Beachhead TAM and assumptions
- Candidate adjacent users, applications, geographies, or channels
- Transferable product and core capabilities
- Incremental requirements and market-entry barriers
- Customer and ecosystem evidence for adjacency

Do not block on missing inputs. Mark unknowns, state their decision impact, and turn the most consequential unknowns into research actions.

## Workflow

1. Define adjacency dimensions explicitly: same user/new use, new user/same use, geography, channel, vertical, or platform side.
2. List candidate follow-on markets without adding them to current beachhead scope.
3. Estimate each market directionally using transparent units and ranges.
4. Assess leverage from the beachhead: references, product reuse, data, brand, channel, partnerships, and core capability.
5. Assess incremental burden: features, regulation, sales motion, support, localization, capital, and new competitors.
6. Prioritize a sequence based on attractiveness, transferability, and learning dependencies.
7. State trigger conditions for expansion and what must remain true in the beachhead first.

Read [references/method.md](references/method.md) when applying the decision rules, calculations, or quality rubric. Use [assets/workbook.md](assets/workbook.md) as the deliverable structure.
Resolve all bundled file paths relative to the directory containing this `SKILL.md`.

To create a working copy:

```bash
python3 scripts/create_workbook.py --venture "Venture name" --output "./calculate-follow-on-markets-tam-workbook.md"
```

Before finalizing, run:

```bash
python3 scripts/validate_workbook.py "./calculate-follow-on-markets-tam-workbook.md"
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

- Follow-on market map
- Directional TAM ranges
- Adjacency leverage/burden analysis
- Expansion sequence
- Expansion triggers and constraints

The work is complete only when:

- Follow-on markets are separate from beachhead TAM.
- Each adjacency has a clear transfer mechanism from the beachhead.
- Sizing uses visible assumptions and appropriately broad ranges.
- The roadmap preserves near-term beachhead focus.

## Gotchas

- Do not sum every conceivable market into a headline number.
- A large adjacent TAM may require a different product and company.
- Geographic expansion can change regulation, channels, and purchasing criteria.
- This is strategic validation, not a detailed operating plan.

## Handoff

End with:

1. **Decision:** the current conclusion in one sentence.
2. **Evidence:** the strongest supporting and contradicting evidence.
3. **Unknowns:** the assumptions most likely to change the decision.
4. **Next actions:** owners and dates for the smallest useful follow-up work.
5. **Downstream updates:** which prior or later venture artifacts must change.
