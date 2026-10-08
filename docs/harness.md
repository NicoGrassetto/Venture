# Entrepreneurship harness

Venture combines the existing entrepreneurship skills with a repeatable
working loop: establish the decision, load relevant context, do one bounded
piece of work, verify it, and leave durable state for the next session.

This is a repository-based harness for an agent you already use, not a hosted
agent service or an unattended research bot. Open the whole repository in
your agent so it can read the instructions and run the local tools.

## Architecture

The design adapts the five-subsystem model in
[Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/).
The files here use original, entrepreneurship-specific instructions.

| Subsystem | Venture implementation |
|---|---|
| Instructions | Root [AGENTS.md](../AGENTS.md), a Claude Code import, and a Copilot entry point |
| Tools | Existing chapter scripts plus [scripts/venture.py](../scripts/venture.py) |
| Environment | Python 3.9+, standard library only, no installation or network access during startup |
| State | A separate brief, task ledger, evidence register, plan, and progress log for each venture |
| Feedback | Draft and final checks, chapter validators, a qualitative review rubric, and regression tests |

The instruction entry points share one canonical contract instead of maintaining
three independent copies. Other agents can be explicitly told to read it.

## Create and resume a venture

From the repository root:

```bash
bash init.sh --venture "Example Venture" --output ventures/example
python3 scripts/venture.py validate ventures/example
```

Initialization creates:

```text
ventures/example/
|-- brief.md
|-- tasks.json
|-- evidence.json
|-- business-plan.md
|-- progress.md
|-- raw/
`-- workbooks/
```

Initialization refuses an existing output directory, including an empty one.
Resume with `validate` instead of initializing again. Paths passed on the
command line are relative to your current working directory. There are no
third-party dependencies, downloads, or automatic external actions.

`ventures/` is ignored by Git to reduce accidental disclosure. This is not
encryption or a backup system. Keep access-controlled backups, minimize
personal information, and review every file before sharing it. If you choose
another output location, arrange equivalent protections yourself.

At the start of each session, read the brief, tasks, and latest progress.
Confirm the plan audience, decision, current constraints, and evidence gaps.
Choose one task whose dependencies are `passing`; load only its relevant
skills, references, and evidence. Do not load all 25 workbooks by default.

## Skill routing

The starter task ledger groups related decisions, not mandatory research
ceremonies. Revisit earlier decisions when evidence changes. A review-ready
plan can describe untested assumptions and future experiments; it must not
claim that those experiments or the associated chapter skills were completed.

| Task | Skills to select as needed |
|---|---|
| Venture brief | [Getting started](../getting-started/SKILL.md) |
| Market and customer | [Segmentation](../market-segmentation/SKILL.md), [beachhead](../select-a-beachhead-market/SKILL.md), [end-user profile](../build-an-end-user-profile/SKILL.md), [beachhead TAM](../calculate-beachhead-market-tam/SKILL.md), [persona](../profile-the-persona/SKILL.md), [next ten customers](../identify-your-next-10-customers/SKILL.md) |
| Value and competition | [Life-cycle use case](../full-life-cycle-use-case/SKILL.md), [product specification](../high-level-product-specification/SKILL.md), [value proposition](../quantify-the-value-proposition/SKILL.md), [core](../define-your-core/SKILL.md), [competitive position](../chart-your-competitive-position/SKILL.md) |
| Business model and sales | [Acquisition process](../map-the-customer-acquisition-process/SKILL.md), [decision-making unit](../determine-the-customer-dmu/SKILL.md), [business model](../design-a-business-model/SKILL.md), [pricing](../set-your-pricing-framework/SKILL.md), [LTV](../calculate-customer-lifetime-value/SKILL.md), [sales process](../map-the-sales-process/SKILL.md), [acquisition cost](../calculate-customer-acquisition-cost/SKILL.md) |
| Validation and growth | [Follow-on markets](../calculate-follow-on-markets-tam/SKILL.md), [key assumptions](../identify-key-assumptions/SKILL.md), [experiments](../test-key-assumptions/SKILL.md), [MVBP](../define-the-minimum-viable-business-product/SKILL.md), [consumption evidence](../show-that-the-dogs-will-eat-the-dog-food/SKILL.md), [product plan](../develop-a-product-plan/SKILL.md) |
| Business-plan synthesis | [Create a business plan](../create-business-plan/SKILL.md) |

To use a chapter without changing its bundled template:

```bash
python3 market-segmentation/scripts/create_workbook.py \
  --venture "Example Venture" \
  --output ventures/example/workbooks/market-segmentation-workbook.md

python3 market-segmentation/scripts/validate_workbook.py \
  ventures/example/workbooks/market-segmentation-workbook.md --allow-todo
```

Use `<skill-name>-workbook.md` filenames in `workbooks/`; nested folders are
also checked. The workspace checker reuses the matching chapter validators
and rejects remaining `TODO`, `TBD`, or `FIXME` placeholders in final mode.
Store other research under `raw/`. Remove `--allow-todo` when declaring an
individual workbook complete.

## Task state

`tasks.json` is the venture equivalent of the guide's feature tracker.
Retain the starter tasks and their acceptance criteria, dependencies, skills,
and required artifact paths. Additional tasks may be added for the venture.

| Status | Meaning |
|---|---|
| `not_started` | No completed work is being claimed |
| `in_progress` | The single active, dependency-ready task |
| `blocked` | Work cannot continue; explain why and name the next action in progress |
| `passing` | The scoped deliverable was checked and reviewed, with its evidence recorded |

For a passing task, fill `owner`, `reviewer`, `reviewed_on` (an ISO date), and
`verification` (the checks, results, review findings, and limitations). Its
`evidence` list must contain existing claim IDs, and its artifacts must exist.
A reviewer may be a person or a clearly identified agent review pass; never
record a human approval that did not occur. Consequential external use still
requires human review and authorization.

The business-plan task also has six `review_scores`, initially `null`. Record
integer scores from 0 to 2 after reviewing. Passing requires at least 10/12,
no zero, and `evidence_integrity` equal to 2; a prose claim of approval alone
does not satisfy this check.

`passing` means the stated decision artifact meets its acceptance criteria.
It does not mean the venture, market, forecasts, or experiments are proven.
Explain inapplicable methods and untested assumptions in the verification
record rather than fabricating completed research.

When a material input changes, reset affected passing tasks and their dependent
tasks to `not_started` or `blocked`. Keep the previous decision and its evidence
in the progress log. Re-review the changed artifacts before restoring `passing`.

## Evidence register

`evidence.json` starts empty. Add records only for actual research or explicitly
labeled assumptions. The following is a format example, not venture evidence:

```json
{
  "id": "E-001",
  "type": "assumption",
  "statement": "A specific, falsifiable hypothesis for this venture.",
  "source": "",
  "date": "YYYY-MM-DD",
  "confidence": "low",
  "contradictions": "Describe contrary evidence or the limits of the search.",
  "next_test": "Name the test, owner, deadline, and decision threshold."
}
```

Append records to the `claims` array. IDs must be unique. Types are `fact`,
`inference`, or `assumption`; confidence is `low`, `medium`, or `high`.
Use the actual recording date, and include a source's publication or observation
date in its research notes. Explain the reasoning behind an inference.

Facts and inferences need a source: an HTTP(S) URL or an existing file path
relative to the workspace, such as `raw/interview-001.md`. An assumption may
have no source, but must have a concrete `next_test`. Local references must stay
inside the workspace. Sources are never downloaded or executed by the checker.

Cite IDs such as `E-001` beside material claims in the plan and workbooks.
Preserve contradictory observations. Reconcile inconsistent claims rather
than selecting whichever source supports the preferred story.

## Verification and handoff

```bash
# In-progress structural checks; unfinished work is expected.
python3 scripts/venture.py validate ventures/example

# Completion checks; run after the separate plan review.
python3 scripts/venture.py validate ventures/example --final
```

Both modes check required files and headings, the task graph, allowed states,
evidence records, local source paths, and chapter workbook structure.
Passing tasks need artifacts, recorded review, and valid evidence IDs.

Final mode additionally requires every task to be passing, no unfinished
placeholders in the workspace documents or evidence, completed chapter
workbooks, and an explicit `review-ready` plan status. Unknowns may remain
only as clear, scoped uncertainties with owners and next tests, not as empty
fields or disguised facts.

The checker cannot verify source truth, research quality, financial arithmetic,
legal compliance, or a reviewer's identity. Apply the
[review rubric](../create-business-plan/references/method.md), inspect source
material, and recompute important numbers. A structural pass is not an
investment recommendation or a promise of business success.

Before leaving, update `progress.md` with the current decision, changed
artifacts, commands and results, unresolved issues, and one next action.
Keep state in files rather than relying on chat history. A blocked or draft
handoff is a valid outcome when evidence is missing.

## Maintaining the harness

```bash
python3 -m unittest discover -s tests -v
```

The suite exercises startup and finalization, malformed state, evidence and
dependency gates, and all existing chapter create/validate workflows.
GitHub Actions runs the same suite. Add a regression case when a real agent
failure exposes a missing guardrail; avoid adding instructions without an
observed need.
