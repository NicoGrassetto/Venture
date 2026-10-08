# Define the Minimum Viable Business Product

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "define-the-minimum-viable-business-product",
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
    "scope": [],
    "launch_gates": []
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

### scope

| Field | Type |
|---|---|
| `capability` | text |
| `customer_value` | text |
| `delivery` | choice:product,manual,partner |
| `boundary` | text |
| `owner` | text |
| `evidence` | evidence |

### launch_gates

| Field | Type |
|---|---|
| `gate` | text |
| `metric` | text |
| `threshold` | text |
| `payment_path` | text |
| `stop_condition` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
