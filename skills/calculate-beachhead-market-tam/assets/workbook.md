# Calculate Beachhead Market TAM

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-beachhead-market-tam",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer_unit": "TODO",
    "geography": "TODO",
    "currency": "TODO",
    "revenue_period": "TODO"
  },
  "evidence": [],
  "data": {
    "markets": [],
    "triangulation": []
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

### markets

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `market` | text |
| `units` | nonnegative |
| `annual_revenue_per_unit` | nonnegative |
| `annual_tam` | nonnegative |
| `exclusions` | text |
| `evidence` | evidence |

### triangulation

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `top_down_annual_tam` | nonnegative |
| `difference_explanation` | text |
| `next_source` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
