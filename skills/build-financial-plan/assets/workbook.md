# Build a Financial Plan

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "build-financial-plan",
  "stage": "draft",
  "synthetic": false,
  "venture": "{VENTURE_NAME}",
  "owner": "TODO",
  "date": "{DATE}",
  "scope": {
    "currency": "TODO",
    "horizon_months": "TODO",
    "opening_cash": "TODO",
    "customer_unit": "TODO"
  },
  "evidence": [],
  "data": {
    "cashflow": [],
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

### cashflow

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `month` | positive_integer |
| `opening_cash` | number |
| `units` | nonnegative |
| `price` | nonnegative |
| `revenue` | nonnegative |
| `cogs` | nonnegative |
| `opex` | nonnegative |
| `taxes` | nonnegative |
| `change_working_capital` | number |
| `capex` | nonnegative |
| `net_financing` | number |
| `operating_cash_flow` | number |
| `closing_cash` | number |
| `evidence` | evidence |

### summary

| Field | Type |
|---|---|
| `scenario` | choice:conservative,base,upside |
| `minimum_cash` | number |
| `additional_funding_needed` | nonnegative |
| `first_negative_month` | nonnegative_integer |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
