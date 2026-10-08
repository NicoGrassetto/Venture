---
name: create-business-plan
description: "Orchestrates the entrepreneurship skills into an evidence-backed business plan, with a persistent venture workspace, explicit assumptions, financial scenarios, review gates, and a resumable handoff. Use to create, revise, or assess a business plan rather than execute one skill in isolation."
license: MIT
compatibility: "Requires the full Venture repository and Python 3.9 or newer for workspace creation and validation."
metadata:
  author: entrepreneurship-skills
  version: "2.0.0"
---

# Create a Business Plan

## Goal

A decision-useful business plan whose claims, assumptions, financial logic,
risks, and next actions can be traced to persistent venture evidence.
The plan may be provisional; never manufacture validation to make it appear
complete.

## Required context

- Venture thesis, founder constraints, and current stage
- Intended audience and the decision the plan should support
- Geography, currency, planning horizon, and resource limits
- Available customer evidence, research, workbooks, and financial inputs
- Sharing permissions and the boundaries of authorized external work

Collect what is available. Turn missing inputs into explicit assumptions or
blocked work with an owner and a next test. Do not use that allowance to skip
founder discovery or substitute an invented venture for an unclear request.

## Use when / not for

Use for a new, revised, or assessed business plan tied to an explicit decision.
For a single market, pricing, or research question, use the focused skill
instead of creating every artifact in the full plan.

## Workflow

1. Read the repository [agent instructions](../../AGENTS.md) and
   [harness lifecycle](../../docs/harness.md). Identify or initialize a workspace.
2. Read its brief, task ledger, evidence register, and progress. Follow the
   [founder discovery protocol](../../docs/harness.md#founder-discovery): ask
   targeted follow-ups, understand the intended venture, and reflect it back
   for correction and explicit founder confirmation. A one-line pitch is not
   a completed brief. Confirm the audience and decision before selecting the
   plan's depth and time horizon; keep unconfirmed work provisional.
3. Triage venture-killing assumptions immediately after discovery using
   [identify-key-assumptions](../identify-key-assumptions/SKILL.md). Choose
   the smallest useful next test before expanding unsupported analysis.
   Pick one dependency-ready task; do not run every skill mechanically.
4. Gather authorized evidence, register material claims, and create skill
   workbooks only when they improve the decision. Distinguish work already
   performed from proposed interviews, experiments, or commitments.
5. Draft the plan from [assets/workbook.md](assets/workbook.md). Explain the
   customer problem, market, offering, differentiation, model, distribution,
   operations, team, financial scenarios, and risks. Write the executive
   summary after the supporting sections.
6. Use [plan-operations](../plan-operations/SKILL.md) for delivery capacity,
   costs, and contingencies, then [build-financial-plan](../build-financial-plan/SKILL.md)
   for an integrated cash forecast. Reconcile these with demand, pricing,
   and unit economics. Do not treat a forecast as traction.
7. Conduct a separate review using
   [references/method.md](references/method.md). Record objections and limits,
   repair failed checks, and obtain human review before consequential use.
8. Update task state and progress. If completion gates pass, label the plan
   `review-ready`; otherwise hand off a clearly labeled draft or blocker.

Paths above are relative to this skill directory. The commands below run from
the repository root, two directories above it:

```bash
bash init.sh --venture "Venture name" --output ventures/example
python3 scripts/venture.py validate ventures/example
python3 scripts/venture.py validate ventures/example --final
```

Resume an existing workspace with `validate`; initialization never overwrites
one. This orchestration skill needs its sibling skills and the root harness.
Individual skills remain usable independently.

## Completion contract

Produce:

- A scoped founder and venture brief with a recorded discovery conversation
  and explicit founder confirmation
- A business plan with traceable claims and explicit uncertainties
- An evidence register retaining contradictions and provenance
- Task-level verification and a separate review record
- A durable progress log and a concrete next action

A review-ready plan has a defined audience and decision, consistent customer
and financial units, evidence-linked material claims, realistic resources,
and prioritized risks with owners and tests. The final check must pass, and
the qualitative review must be recorded.

Use the workbook stages honestly: `draft` is unfinished work, `research-plan`
is a completed protocol, and `completed-analysis` is an analysis actually
performed. Research plans can appear as future work, not completed customer
validation. The risk-triage, operations, and financial artifacts require
completed analysis, even when some inputs remain explicit assumptions.

Readiness is not proof of product-market fit, lender approval, investability,
or legal compliance. A narrower plan with honest gaps is better than a
confident document supported by invented evidence.

## Handoff

End with the current decision, supporting and contradicting evidence,
unresolved risks, checks actually run, and the next action with its owner.
Name any earlier workbooks or plan sections invalidated by the latest evidence.
