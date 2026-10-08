# Map the Customer Buying Process

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "map-customer-buying-process",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer": "TODO",
    "geography": "TODO",
    "decision_horizon": "TODO"
  },
  "evidence": [],
  "data": {
    "buying_stages": [],
    "obstacles": []
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

### buying_stages

| Field | Type |
|---|---|
| `stage` | text |
| `customer_owner` | text |
| `entry_condition` | text |
| `exit_evidence` | text |
| `elapsed_days` | nonnegative |
| `dependency` | text |
| `evidence` | evidence |

### obstacles

| Field | Type |
|---|---|
| `obstacle` | text |
| `impact` | text |
| `mitigation` | text |
| `owner` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
