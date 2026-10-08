# Entrepreneurship harness

Venture combines the existing entrepreneurship skills with a repeatable
working loop: establish the decision, load relevant context, do one bounded
piece of work, verify it, and leave durable state for the next session.

This is a repository-based harness for an agent you already use, not a hosted
agent service or an unattended research bot. Open the whole repository in
your agent so it can read the instructions and run the local tools. See
[client compatibility](compatibility.md) for native discovery, verified client
versions, and the opt-in completion guard.

## Architecture

| Subsystem | Venture implementation |
|---|---|
| Instructions | Root [AGENTS.md](../AGENTS.md), a Claude Code import, a Copilot entry point, and generated native skill adapters |
| Tools | Existing skill scripts, [workspace checks](../scripts/venture.py), [adapter checks](../scripts/sync_skills.py), and [offline client checks](../scripts/check_clients.py) |
| Environment | Python 3.9+, standard library only, no installation or network access during startup |
| State | A separate brief, task ledger, evidence register, plan, and progress log for each venture |
| Feedback | Draft and final checks, skill validators, a qualitative review rubric, and regression tests |

The instruction entry points share one canonical contract instead of maintaining
three independent copies. Other agents can be explicitly told to read it.

## Repository structure

The harness connects the individual skills without replacing them:

```text
AGENTS.md                       Shared agent instructions
CLAUDE.md                       Claude Code entry point
.github/copilot-instructions.md GitHub Copilot entry point
.agents/skills/                 Generated discovery adapters for shared clients
.claude/skills/                 Generated Claude-compatible discovery adapters
.claude/settings.json           Opt-in, workspace-scoped completion hook
init.sh                         Workspace initialization
docs/harness.md                 Lifecycle, routing, and state contracts
scripts/venture.py              Initialization and completion checks
scripts/sync_skills.py          Adapter generation and consistency checks
scripts/check_clients.py        Offline native client discovery checks
templates/                      Venture brief, task, evidence, and progress templates
skills/                         Venture skills and business-plan orchestration
tests/                          Harness and skill regression checks
ventures/                       Private working copies (ignored by Git)
```

Each skill has its own directory inside [skills/](../skills/):

```text
skills/market-segmentation/
|-- SKILL.md
|-- assets/
|   `-- workbook.md
|-- references/
|   `-- method.md
`-- scripts/
    |-- create_workbook.py
    `-- validate_workbook.py
```

- `SKILL.md` contains routing metadata, the operating workflow, evidence rules,
  completion gates, and handoff instructions.
- `references/method.md` provides decision rules, analytical methods, and a
  quality rubric.
- `assets/workbook.md` is a reusable evidence-and-decision template.
- `scripts/create_workbook.py` creates a dated working copy without external
  dependencies.
- `scripts/validate_workbook.py` checks required sections and unfinished
  placeholders.

This follows the Agent Skills progressive-disclosure model: metadata is used
for discovery, the concise skill instructions load when activated, and detailed
resources load only when needed.

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
If the founder has not confirmed the venture brief, start with discovery below.
Choose one task whose dependencies are `passing`; load only its relevant
skills, references, and evidence. Do not load all 25 workbooks by default.

## Founder discovery

A short pitch is an invitation to understand the venture, not permission to
invent the rest of it. Begin with the founder's existing notes and documents,
then ask focused follow-up questions one at a time. Adapt the next question to
the answer instead of delivering a long generic questionnaire.

Build enough shared understanding to cover:

| Topic | Useful follow-up |
|---|---|
| Customer and problem | Who experiences the problem, in what concrete situation, and what do they do today? |
| Solution and differentiation | What should change for that customer, and why might this approach be better than their workaround? |
| Business model | Who could pay, for what, and which parts are still hypotheses? |
| Stage and evidence | What exists now, what has been tried, and what has actually been observed? |
| Founder context | Why this venture, what capabilities and access exist, and what are the limits on time, money, geography, and ambition? |
| Plan purpose | Who will use the plan, for what decision, over what horizon? |

Ask for concrete examples when answers are vague; surface contradictions
rather than smoothing them over. Do not require a fixed interview length or
ask again for answers already in supplied materials. A founder can be unsure:
record the uncertainty, why it matters, and the next test instead of forcing a
fictional answer.

Write the understanding into the existing sections of `brief.md`, including
what the founder intends, what is known, what is only an assumption, and what
is explicitly out of scope. Reflect that understanding back to the founder
and invite correction. After the founder explicitly confirms it, save a dated
record of the questions, answers, corrections, and actual confirmation under
`raw/`, and fill the venture-brief task's `discovery` object:

- `confirmed_by`: the founder or authorized venture owner's name or role,
  not the drafting agent or an unrelated reviewer.
- `confirmed_on`: the actual confirmation date in `YYYY-MM-DD` format.
- `confirmation_source`: the local path to that record, for example
  `raw/founder-discovery.md`.

Both validation modes reject a `passing` venture-brief task without those
fields, an existing nonempty confirmation record, and a brief with substantive
content in every required section and no unfinished placeholders. Since the
remaining starter tasks depend on the brief, their progress cannot bypass
this gate. Founder confirmation aligns intent; it is not market validation.
The checker cannot authenticate a conversation or measure comprehension, so
agents must never fabricate the exchange or infer approval from silence.

If the founder is unavailable, leave the brief `in_progress` or `blocked`,
record the next question, and label any useful research or outline provisional.
Do not claim a finished business plan. When the intended venture changes,
reconfirm the updated brief and reset affected downstream tasks.

Existing workspaces stay in place when skills move into `skills/`. Legacy
drafts without `discovery` still validate. Before restoring a legacy brief to
`passing`, add the three discovery fields from
[the task template](../templates/tasks.json), complete or confirm the brief,
and record the actual exchange. Until then, reset that task and affected
dependents to unfinished; do not reinitialize or overwrite the workspace.

## Skill routing

Use [create-business-plan](../skills/create-business-plan/SKILL.md) to orchestrate
the full business-plan workflow. It requires the full repository; the other
skills below remain independently usable.

The starter task ledger groups related decisions, not mandatory research
ceremonies. Revisit earlier decisions when evidence changes. A review-ready
plan can describe untested assumptions and future experiments; it must not
claim that those experiments or the associated skills were completed.

| Task | Skills to select as needed |
|---|---|
| Venture brief | [Getting started](../skills/getting-started/SKILL.md) |
| Market and customer | [Segmentation](../skills/market-segmentation/SKILL.md), [beachhead](../skills/select-a-beachhead-market/SKILL.md), [end-user profile](../skills/build-an-end-user-profile/SKILL.md), [beachhead TAM](../skills/calculate-beachhead-market-tam/SKILL.md), [persona](../skills/profile-the-persona/SKILL.md), [next ten customers](../skills/identify-your-next-10-customers/SKILL.md) |
| Value and competition | [Life-cycle use case](../skills/full-life-cycle-use-case/SKILL.md), [product specification](../skills/high-level-product-specification/SKILL.md), [value proposition](../skills/quantify-the-value-proposition/SKILL.md), [core](../skills/define-your-core/SKILL.md), [competitive position](../skills/chart-your-competitive-position/SKILL.md) |
| Business model and sales | [Acquisition process](../skills/map-the-customer-acquisition-process/SKILL.md), [decision-making unit](../skills/determine-the-customer-dmu/SKILL.md), [business model](../skills/design-a-business-model/SKILL.md), [pricing](../skills/set-your-pricing-framework/SKILL.md), [LTV](../skills/calculate-customer-lifetime-value/SKILL.md), [sales process](../skills/map-the-sales-process/SKILL.md), [acquisition cost](../skills/calculate-customer-acquisition-cost/SKILL.md) |
| Validation and growth | [Follow-on markets](../skills/calculate-follow-on-markets-tam/SKILL.md), [key assumptions](../skills/identify-key-assumptions/SKILL.md), [experiments](../skills/test-key-assumptions/SKILL.md), [MVBP](../skills/define-the-minimum-viable-business-product/SKILL.md), [consumption evidence](../skills/show-that-the-dogs-will-eat-the-dog-food/SKILL.md), [product plan](../skills/develop-a-product-plan/SKILL.md) |
| Business-plan synthesis | [Create a business plan](../skills/create-business-plan/SKILL.md) |

### Use individual skills

The full checkout exposes the bundled skills through its native adapters.
For standalone use, install the canonical skill directory from
[skills/](../skills/), not a generated adapter. In GitHub Copilot CLI, for example,
use `copilot skill add ./skills/market-segmentation` from the repository root,
then reload skills. Remove obsolete custom registrations if they duplicate
or shadow skills already discovered through the adapters. See
[client compatibility](compatibility.md#native-discovery) for discovery details.

You can explicitly invoke a skill by name:

```text
Use the market-segmentation skill to identify and research possible markets for this idea.
```

To use a skill without changing its bundled template:

```bash
python3 skills/market-segmentation/scripts/create_workbook.py \
  --venture "Example Venture" \
  --output ventures/example/workbooks/market-segmentation-workbook.md

python3 skills/market-segmentation/scripts/validate_workbook.py \
  ventures/example/workbooks/market-segmentation-workbook.md --allow-todo
```

Use `<skill-name>-workbook.md` filenames in `workbooks/`; nested folders are
also checked. The workspace checker reuses the matching skill validators
and rejects remaining `TODO`, `TBD`, or `FIXME` placeholders in final mode.
Store other research under `raw/`. Remove `--allow-todo` when declaring an
individual workbook complete.

## Task state

`tasks.json` tracks venture decisions and their verification.
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
evidence records, local source paths, and skill workbook structure.
Passing tasks need artifacts, recorded review, and valid evidence IDs.

Final mode additionally requires every task to be passing, no unfinished
placeholders in the workspace documents or evidence, completed skill
workbooks, and an explicit `review-ready` plan status. Unknowns may remain
only as clear, scoped uncertainties with owners and next tests, not as empty
fields or disguised facts.

The checker cannot verify source truth, research quality, financial arithmetic,
legal compliance, or a reviewer's identity. Apply the
[review rubric](../skills/create-business-plan/references/method.md), inspect source
material, and recompute important numbers. A structural pass is not an
investment recommendation or a promise of business success.

Before leaving, update `progress.md` with the current decision, changed
artifacts, commands and results, unresolved issues, and one next action.
Keep state in files rather than relying on chat history. A blocked or draft
handoff is a valid outcome when evidence is missing.

## Maintaining the harness

```bash
python3 scripts/sync_skills.py --check
python3 -m unittest discover -s tests -v
```

The suite exercises startup and finalization, malformed state, founder
confirmation, evidence and dependency gates, and all existing skill
create/validate workflows under `skills/`. It also covers adapter ownership
and drift, client discovery response checks, and the completion-hook contract.
GitHub Actions runs the same suite. Add a regression case when a real agent
failure exposes a missing guardrail; avoid adding instructions without an
observed need.
