# Validate Customer Traction

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "validate-customer-traction",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer": "TODO",
    "cohort_window": "TODO",
    "retention_period": "TODO"
  },
  "evidence": [],
  "data": {
    "cohorts": [],
    "diagnosis": []
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

### cohorts

| Field | Type |
|---|---|
| `cohort` | text |
| `acquired` | positive_integer |
| `activated` | nonnegative_integer |
| `paid` | nonnegative_integer |
| `retained` | nonnegative_integer |
| `retention_rate` | probability |
| `customer_outcome` | text |
| `evidence` | evidence |

### diagnosis

| Field | Type |
|---|---|
| `cohort` | text |
| `bottleneck` | text |
| `contradiction` | text |
| `decision` | choice:scale,iterate,pivot,stop |
| `next_test` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
