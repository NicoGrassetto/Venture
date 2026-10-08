# Workbook record format

The JSON block between the workbook markers is the machine-checkable record.
Keep narrative notes outside it, but keep decisions and cited evidence in the
record too. Do not remove the markers or add a second record.

## Stages

- `draft`: working material with unresolved inputs. `--allow-todo` permits
  draft checks, not a completion claim.
- `research-plan`: a completed protocol, not completed research. Leave `data`
  tables empty. Fill scope, decision, limitations, next actions, and a
  `research_plan` with question, population, method, metric, precommitted
  threshold, owner, and due date.
- `completed-analysis`: an analysis was performed. Every task-specific table
  needs evidence-linked rows. Strategy and forecast inputs may be explicit
  assumptions; customer observation and experiment skills require sourced
  facts. Failed or inconclusive results are valid completed analyses.

Use `--require-analysis` when a result, rather than a plan, is needed.
A business plan can cite a research plan only as future work.

## Evidence

Every result row has an `evidence` array of IDs such as `["E-001"]`. Define
the IDs in the record's evidence array:

```json
{
  "id": "E-001",
  "type": "assumption",
  "statement": "A specific, falsifiable venture hypothesis.",
  "source": "",
  "date": "2026-01-01",
  "confidence": "low",
  "contradictions": "Describe contrary evidence or the limits of the search.",
  "next_test": "Describe the test, owner, timing, and decision threshold."
}
```

Use the actual date, not the illustrative date above. Facts and inferences
need a source; assumptions need a next test. Types are `fact`, `inference`,
and `assumption`; confidence is `low`, `medium`, or `high`. Local sources are
relative to the workbook file. HTTP(S) references are checked for shape, not
downloaded or verified for truth.

In a venture workspace, evidence records must match the central register.
Local source paths are relative to the workbook there and to the workspace
root in the central register; they must resolve to the same file inside that
workspace. For example, a workbook may cite `../raw/interview.md` while the
register cites `raw/interview.md`. Other evidence fields must match exactly.
The validator does not silently rewrite IDs or conflicting claims.

## Types and units

- Numbers are finite JSON numbers, never strings with currency symbols.
- Counts and periods use integers; probabilities and rates use fractions in
  `[0, 1]`, not percentages in `[0, 100]`.
- `date` uses `YYYY-MM-DD`; recording dates cannot be in the future.
- Currency is a three-letter uppercase code. Use one currency throughout a
  model and document any conversion assumptions.
- Financial scenarios are `conservative`, `base`, and `upside`.
- Local calculations check arithmetic, sequence, and denominators. They
  cannot detect a fabricated observation, a wrongly classified cost, or a
  forecast that is economically implausible.

## Completion review

Before calling an analysis complete, confirm that the intended decision is
served, material claims are traceable, contradictions affect the conclusion,
and the next action has an owner and due date. Inspect source material and
recompute consequential values. Do not award completion for filling fields.

The bundled worked example is marked `synthetic: true`. Validate it with
`--allow-example`; it must never be used as a real venture's evidence. A
standalone skill retains its own template, contract, runtime, and example.
