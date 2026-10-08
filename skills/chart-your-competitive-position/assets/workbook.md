# Chart Your Competitive Position

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "chart-your-competitive-position",
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
    "axes": [],
    "alternatives": []
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

### axes

| Field | Type |
|---|---|
| `axis` | choice:x,y |
| `customer_priority` | text |
| `low_anchor` | text |
| `high_anchor` | text |
| `evidence` | evidence |

### alternatives

| Field | Type |
|---|---|
| `alternative` | text |
| `kind` | choice:product,competitor,status-quo |
| `x_score` | probability |
| `y_score` | probability |
| `uncertainty` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
