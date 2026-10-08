<p align="center">
  <img src=".github/assets/golden-gate-pixel.gif" alt="Golden Gate Bridge pixel art" width="224" />
</p>

<p align="center">
  Your bridge from idea to reality.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license" /></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> &middot;
  <a href="#structure">Structure</a> &middot;
  <a href="#how-it-works">How it works</a> &middot;
  <a href="#use">Use</a> &middot;
  <a href="#skills">Skills</a> &middot;
  <a href="#special-thanks">Special thanks</a> &middot;
  <a href="LICENSE">License</a>
</p>

## Overview

Venture is an agent harness for entrepreneurship and evidence-backed business
plan creation. It connects focused skills with a repeatable workflow, persistent
venture state, and checks that distinguish a draft from a reviewed deliverable.

Actionable [Agent Skills](https://agentskills.io/) teach an agent how to make
venture decisions, gather evidence, create decision artifacts, and validate
the results.

## Structure

The harness connects the individual skills without replacing them:

```text
AGENTS.md                       Shared agent instructions
CLAUDE.md                       Claude Code entry point
.github/copilot-instructions.md GitHub Copilot entry point
.agents/skills/                Generated discovery adapters for shared clients
.claude/skills/                Generated Claude-compatible discovery adapters
.claude/settings.json          Opt-in, workspace-scoped completion hook
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

Each skill has its own directory inside [skills/](skills/):

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

## How it works

1. **Understand the venture.** Ask targeted follow-up questions, record the
   venture, audience, constraints, and planning horizon, then reflect the
   understanding back for the founder to correct and confirm.
2. **Select one task.** Read persistent state and load only the skills
   needed for the current decision.
3. **Gather evidence.** Distinguish facts, inferences, and assumptions; retain
   sources, dates, contradictions, and the next useful tests.
4. **Build and review.** Synthesize the business plan, reconcile financial
   scenarios, and check it against explicit completion and review criteria.
5. **Hand off.** Save verified progress, remaining uncertainty, and one next
   action so another session can continue without reconstructing the chat.

Read the [agent instructions](AGENTS.md) and
[harness guide](docs/harness.md) for the operating rules. The harness works
with an agent you already use; it is not a hosted service. Structural checks
do not establish source truth, financial correctness, or business viability.

## Use

### Agent compatibility

Native discovery adapters are included for OpenCode, GitHub Copilot, Claude
Code, and Codex while [skills/](skills/) remains the source of truth. Use the
full checkout; no global skill registration is needed for those documented
discovery locations.

Copilot CLI and Codex have passed local, offline discovery checks. OpenCode,
Claude Code, and live conversation behavior remain unverified in this
environment. See [client compatibility](docs/compatibility.md) for exact
versions, checks, and the optional completion guard.

### Run the harness

Open the whole repository in your agent. Python 3.9 or newer is required;
there are no third-party dependencies.

```bash
bash init.sh --venture "Example Venture" --output ventures/example
python3 scripts/venture.py validate ventures/example
```

Then give the agent a bounded request:

```text
Read AGENTS.md and use ventures/example as the workspace.
Help me develop this venture into a business plan for an internal go/no-go
decision. Start with the brief, label unknowns, and work on one task at a time.
```

The agent should not jump from a one-line pitch to a finished plan. It first
clarifies the customer, problem, solution, business model, current stage,
founder constraints, and plan purpose. The brief cannot pass without a recorded
founder confirmation. See the [discovery protocol](docs/harness.md#founder-discovery).

Resume by reading the workspace's brief, tasks, evidence, and progress rather
than initializing it again. Startup never overwrites an existing directory.
Keep sensitive research in the ignored workspace and arrange private backups;
Git ignore rules are not access controls.

After the work and separate review are complete, run:

```bash
python3 scripts/venture.py validate ventures/example --final
```

This stricter check intentionally fails for a new or unfinished workspace.
It requires recorded evidence, reviewed tasks, complete artifacts, and passing
review scores. A review-ready plan is not the same as a validated business.

### Use individual skills

The full checkout exposes the bundled skills through its native adapters.
For standalone use, install the canonical skill directory from
[skills/](skills/), not a generated adapter. In GitHub Copilot CLI, for example,
use `copilot skill add ./skills/market-segmentation` from the repository root,
then reload skills. Remove obsolete custom registrations if they duplicate
or shadow skills already discovered through the adapters.

You can explicitly invoke a skill by name:

```text
Use the market-segmentation skill to identify and research possible markets for this idea.
```

Within a skill directory, create and validate a workbook:

```bash
python3 scripts/create_workbook.py \
  --venture "Example Venture" \
  --output ./market-segmentation-workbook.md

python3 scripts/validate_workbook.py ./market-segmentation-workbook.md
```

The validator intentionally fails while `TODO` placeholders remain. Use
`--allow-todo` only for an in-progress structural check.

## Skills

Use [create-business-plan](skills/create-business-plan/) to orchestrate the full
business-plan workflow. It requires the full repository; the other skills
below remain independently usable.

| Skill |
|---|
| [`getting-started`](skills/getting-started/) |
| [`market-segmentation`](skills/market-segmentation/) |
| [`select-a-beachhead-market`](skills/select-a-beachhead-market/) |
| [`build-an-end-user-profile`](skills/build-an-end-user-profile/) |
| [`calculate-beachhead-market-tam`](skills/calculate-beachhead-market-tam/) |
| [`profile-the-persona`](skills/profile-the-persona/) |
| [`full-life-cycle-use-case`](skills/full-life-cycle-use-case/) |
| [`high-level-product-specification`](skills/high-level-product-specification/) |
| [`quantify-the-value-proposition`](skills/quantify-the-value-proposition/) |
| [`identify-your-next-10-customers`](skills/identify-your-next-10-customers/) |
| [`define-your-core`](skills/define-your-core/) |
| [`chart-your-competitive-position`](skills/chart-your-competitive-position/) |
| [`determine-the-customer-dmu`](skills/determine-the-customer-dmu/) |
| [`map-the-customer-acquisition-process`](skills/map-the-customer-acquisition-process/) |
| [`calculate-follow-on-markets-tam`](skills/calculate-follow-on-markets-tam/) |
| [`design-a-business-model`](skills/design-a-business-model/) |
| [`set-your-pricing-framework`](skills/set-your-pricing-framework/) |
| [`calculate-customer-lifetime-value`](skills/calculate-customer-lifetime-value/) |
| [`map-the-sales-process`](skills/map-the-sales-process/) |
| [`calculate-customer-acquisition-cost`](skills/calculate-customer-acquisition-cost/) |
| [`identify-key-assumptions`](skills/identify-key-assumptions/) |
| [`test-key-assumptions`](skills/test-key-assumptions/) |
| [`define-the-minimum-viable-business-product`](skills/define-the-minimum-viable-business-product/) |
| [`show-that-the-dogs-will-eat-the-dog-food`](skills/show-that-the-dogs-will-eat-the-dog-food/) |
| [`develop-a-product-plan`](skills/develop-a-product-plan/) |

## Special thanks:

- **Bill Aulet**, for [*Disciplined Entrepreneurship: 24 Steps to a Successful Startup*](https://www.d-eship.com/), which inspired the entrepreneurship workflows.
- **WalkingLabs**, for the [Learn Harness Engineering course](https://walkinglabs.github.io/learn-harness-engineering/en/), which informed the harness design.
- [Agent Skills specification](https://agentskills.io/specification)
- [GitHub Copilot Agent Skills documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)

## License

Venture is available under the [MIT License](LICENSE).
