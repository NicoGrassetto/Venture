# Quantify the Value Proposition

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "quantify-the-value-proposition",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer": "TODO",
    "input_unit": "TODO",
    "value_unit": "TODO",
    "horizon": "TODO"
  },
  "evidence": [],
  "data": {
    "outcomes": [],
    "validation": []
  },
  "research_plan": [],
  "decision": "TODO",
  "limitations": "TODO",
  "next_actions": []
}
```
<!-- venture-record:end -->

## Output fields

Each data table is an array of row objects. Every analysis row cites evidence IDs.

### outcomes

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `baseline` | number |
| `future` | number |
| `direction` | choice:increase,decrease |
| `unit_value` | nonnegative |
| `frequency` | nonnegative |
| `realization` | probability |
| `realized_value` | number |
| `evidence` | evidence |

### validation

| Field | Type |
|---|---|
| `baseline_source` | text |
| `customer_response` | text |
| `disputed_input` | text |
| `next_test` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
