# Map the Sales Process

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "map-the-sales-process",
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
    "sales_stages": [],
    "bottlenecks": []
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

### sales_stages

| Field | Type |
|---|---|
| `stage` | text |
| `customer_exit` | text |
| `seller_action` | text |
| `owner` | text |
| `channel` | text |
| `entered` | nonnegative_integer |
| `converted` | nonnegative_integer |
| `conversion_rate` | probability |
| `elapsed_days` | nonnegative |
| `cost` | nonnegative |
| `evidence` | evidence |

### bottlenecks

| Field | Type |
|---|---|
| `stage` | text |
| `hypothesis` | text |
| `experiment` | text |
| `metric` | text |
| `owner` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
