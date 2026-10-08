# Agent compatibility

Use the full Venture checkout in an agent with local file and terminal access.
The canonical instructions remain in [AGENTS.md](../AGENTS.md), and all actual
skill workflows, templates, and scripts remain in [skills/](../skills/).

## Native discovery

| Client | Instructions | Native skill entry points |
|---|---|---|
| OpenCode | [AGENTS.md](../AGENTS.md) | [.agents/skills/](../.agents/skills/) and Claude-compatible discovery |
| GitHub Copilot agent mode / CLI | [Copilot instructions](../.github/copilot-instructions.md), pointing to the shared contract | [.agents/skills/](../.agents/skills/) and Claude-compatible discovery |
| Claude Code | [CLAUDE.md](../CLAUDE.md), importing the shared contract | [.claude/skills/](../.claude/skills/) |
| Codex | [AGENTS.md](../AGENTS.md) | [.agents/skills/](../.agents/skills/) |

Both native directories contain generated entry points, not copies of the
workflow bodies. Each entry point keeps the canonical discovery metadata and
instructs the agent to read the canonical skill before working. Relative
resources and commands resolve from that canonical directory, not the adapter.
This works without symlinks or special filesystem privileges.

Do not install an adapter directory on its own: it depends on the full
checkout. Install a canonical skill directory for standalone use.
The business-plan orchestration skill always requires the full harness.
Do not also register the canonical collection as a custom skill location in
a client already discovering the adapters; remove obsolete registrations if
they create duplicates or shadow repository skills.

## Refresh and check adapters

From the repository root:

```bash
# After adding, renaming, removing, or changing a skill's discovery metadata.
python3 scripts/sync_skills.py

# Read-only check for missing, stale, conflicting, or locally edited adapters.
python3 scripts/sync_skills.py --check
```

The generator manages only the paths recorded in
[.agents/skill-adapters.json](../.agents/skill-adapters.json). It preflights
ownership before writing, refuses symlinks and conflicting files, and preserves
unrelated skills and notes. Removed skills lose only their unchanged generated
entry points; directories containing other files are retained. An empty
canonical skill tree is an error, not permission to delete all adapters.
Ownership checks normalize LF and CRLF line endings so a Windows Git checkout
does not look like a manual edit.

Do not edit generated adapters directly. If the check finds local edits,
preserve them outside the generated file and reconcile any intended changes
into the canonical skill. Restore the previously generated adapter and its
matching manifest from a known-good revision before regenerating; the tool
will not silently discard the edit. Do not hand-edit checksums to bypass this
protection.

Body-only changes need no adapter refresh because the body is read from the
canonical file. Adapter checks run during [initialization](../init.sh) and in
[CI](../.github/workflows/validate-harness.yml).

## What has actually been verified

Recorded on 2026-10-08 on macOS:

| Client | Version | Verified result |
|---|---|---|
| GitHub Copilot CLI | 1.0.93 | Offline native listing finds all 26 bundled skills enabled and exactly once; the shared and Copilot-specific instruction entry points are discovered |
| Codex CLI | 0.155.1 | Local app-server `skills/list` finds all 26 bundled skills enabled and exactly once |
| OpenCode | Not installed | Adapter structure and links checked; native discovery and conversation behavior not verified |
| Claude Code | Not installed | Adapter structure, instruction import, and hook contract checked; native discovery and conversation behavior not verified |

Run the available native checks yourself:

```bash
python3 scripts/check_clients.py --client copilot
python3 scripts/check_clients.py --client codex
```

These commands use temporary client homes, do not forward provider credentials,
do not change global configuration, and do not start model turns. Vendor
built-in skills may also appear, but every bundled skill must appear exactly
once, be enabled, and resolve to a repository adapter. Missing clients, disabled
skills, duplicate names, shadowed paths, loader errors, or malformed responses
fail explicitly.

Offline discovery does not prove that a model follows the workflow. No live
founder interview or native Stop event has been certified by these checks.
Run the conversation checks below when evaluating a new client or version.
Private, Git-ignored venture files are not available in a fresh cloud checkout
unless you deliberately provide them through an approved private workflow.

## Optional completion guard

[.claude/settings.json](../.claude/settings.json) registers a single shared
`Stop` hook for Claude Code and Copilot CLI's Claude-compatible project
settings loader. There is no second Copilot hook registration, avoiding double
execution. Activate it only for the workspace a session should work on:

```bash
VENTURE_WORKSPACE=ventures/example claude
# Or:
VENTURE_WORKSPACE=ventures/example copilot
```

In PowerShell, set `$env:VENTURE_WORKSPACE = "ventures/example"` before launching
the client. The hook command requires Git and `python3` on PATH and a session
inside this checkout. It finds the repository root even when the working
directory is a nested skill directory. Client trust and hook settings still
control whether it runs.

Without `VENTURE_WORKSPACE`, the hook reports that it is inactive and does not
scan venture directories. With it set, [the handler](../scripts/completion_hook.py):

1. Checks only the explicitly selected workspace.
2. Uses draft validation during discovery, so asking the founder a question
   or pausing unfinished work is allowed.
3. Uses final validation if the plan claims `review-ready` or the business-plan
   task claims `passing`.
4. Blocks a failed check once and supplies the validation error to the agent.
5. If a forced corrective turn still fails, reports a hook error instead of
   creating an endless continuation loop. That error is not completion approval.

These checks inspect recorded state, not arbitrary natural-language claims.
They cannot authenticate founder confirmation, validate the truth of research,
or stop an agent from editing its own state files. A client can disable hooks,
and an already-stopping corrective turn may end with an error. Keep the human
review and evidence rules; do not treat this guard as an immutable policy.

The handler and shared shell command are covered by local regression tests.
Native hook firing is not yet integration-tested. This registration does not
promise a hook for Codex, OpenCode, Copilot cloud agent, or every Copilot IDE
surface. For those clients, run the explicit workspace checks and record their
results before a handoff.

## Conversation smoke test

Use a separate, disposable workspace with synthetic, non-sensitive input.
Do not run this against a real venture or grant permission to contact people,
publish content, or spend money.

1. Start the client at the repository root. Inspect its active instructions
   and native skill list. Confirm the 26 canonical names resolve exactly once.
2. Ask it to read the shared instructions, initialize a test workspace, and
   help with the deliberately vague pitch: "I want to build an AI app."
3. Verify the first useful response asks a focused clarification rather than
   inventing a customer, founder background, revenue, or completed plan.
4. Supply a concrete hypothetical customer problem and constraints. Check that
   follow-ups adapt to the answers and that assumptions remain labeled.
5. Confirm that the agent reflects its understanding back and waits for your
   explicit confirmation before marking the brief passing. Decline or correct
   the first summary to check that it incorporates the correction.
6. Check that native skill invocation follows the adapter to the canonical
   file, creates a workbook in the workspace, and runs its real validator.
7. In the disposable workspace, mark an unfinished plan `review-ready`.
   With the optional guard enabled, verify the native Stop event returns a
   blocking error, while a normal draft question can end its turn.
8. Record the client/model versions, actual commands, observed behavior,
   failures, and limitations. Do not label the client behavior verified merely
   because structural tests pass.

## Official references

- [OpenCode rules](https://opencode.ai/docs/rules/) and [skills](https://opencode.ai/docs/skills/)
- [Copilot skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) and [hooks](https://docs.github.com/en/copilot/reference/hooks-reference)
- [Claude Code memory](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), and [hooks](https://code.claude.com/docs/en/hooks)
- [Codex instructions](https://developers.openai.com/codex/guides/agents-md/), [skills](https://developers.openai.com/codex/skills/), and [app-server protocol](https://developers.openai.com/codex/app-server/)
