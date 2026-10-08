# Calculate Customer Acquisition Cost

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-customer-acquisition-cost",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "currency": "TODO",
    "contribution_period": "TODO",
    "spend_window": "TODO",
    "sales_lag_periods": "TODO"
  },
  "evidence": [],
  "data": {
    "acquisition": [],
    "cost_coverage": []
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

### acquisition

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `cohort` | text |
| `acquisition_spend` | nonnegative |
| `new_paying_customers` | positive_integer |
| `cac` | nonnegative |
| `contribution_per_period` | positive |
| `simple_payback_periods` | nonnegative |
| `evidence` | evidence |

### cost_coverage

| Field | Type |
|---|---|
| `cost` | text |
| `treatment` | text |
| `allocation_basis` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
