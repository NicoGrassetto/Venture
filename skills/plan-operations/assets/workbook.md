# Plan Operations

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "plan-operations",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer": "TODO",
    "delivery_unit": "TODO",
    "planning_period": "TODO",
    "currency": "TODO"
  },
  "evidence": [],
  "data": {
    "capacity": [],
    "dependencies": []
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

### capacity

| Field | Type |
|---|---|
| `activity` | text |
| `demand_units` | nonnegative |
| `hours_per_unit` | positive |
| `available_hours` | nonnegative |
| `required_hours` | nonnegative |
| `gap_hours` | nonnegative |
| `cost_per_hour` | nonnegative |
| `labor_cost` | nonnegative |
| `owner` | text |
| `evidence` | evidence |

### dependencies

| Field | Type |
|---|---|
| `supplier_or_dependency` | text |
| `lead_days` | nonnegative_integer |
| `failure_trigger` | text |
| `fallback` | text |
| `owner` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
