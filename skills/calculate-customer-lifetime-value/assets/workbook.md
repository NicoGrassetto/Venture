# Calculate Customer Lifetime Value

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-customer-lifetime-value",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "customer_unit": "TODO",
    "currency": "TODO",
    "period_unit": "TODO",
    "horizon_periods": "TODO",
    "discount_rate_per_period": "TODO"
  },
  "evidence": [],
  "data": {
    "cashflows": [],
    "summary": []
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

### cashflows

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `period` | positive_integer |
| `retention` | probability |
| `revenue_per_active_customer` | nonnegative |
| `gross_margin` | probability |
| `service_cost` | nonnegative |
| `expected_contribution` | number |
| `discounted_contribution` | number |
| `evidence` | evidence |

### summary

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `ltv` | number |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
