# Market Segmentation

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "market-segmentation",
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
    "segments": [],
    "comparison": []
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

### segments

| Field | Type |
|---|---|
| `segment` | text |
| `end_user` | text |
| `application` | text |
| `problem` | text |
| `payer` | text |
| `current_solution` | text |
| `access` | text |
| `evidence` | evidence |

### comparison

| Field | Type |
|---|---|
| `segment` | text |
| `urgency` | text |
| `buying_process` | text |
| `product_requirements` | text |
| `decision` | choice:shortlist,defer,reject |
| `reason` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
