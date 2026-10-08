# Identify Key Assumptions

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "identify-key-assumptions",
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
    "assumptions": [],
    "test_queue": []
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

### assumptions

| Field | Type |
|---|---|
| `id` | text |
| `hypothesis` | text |
| `category` | choice:desirability,viability,feasibility,operations,team,regulatory |
| `impact` | positive_integer |
| `uncertainty` | positive_integer |
| `risk_score` | positive_integer |
| `reversal_threshold` | text |
| `evidence` | evidence |

### test_queue

| Field | Type |
|---|---|
| `assumption_id` | text |
| `priority` | positive_integer |
| `dependency` | text |
| `next_evidence` | text |
| `owner` | text |
| `evidence` | evidence |

## Stage rules

- `draft`: unfinished work; validate with `--allow-todo`.
- `research-plan`: leave result tables empty; complete the research protocol and next actions.
- `completed-analysis`: fill every result table with evidence-linked rows and check calculations.

A research-plan row needs question, population, method, metric, threshold, owner, and due_date.
A next-action row needs action, owner, due_date, and evidence_expected.
Read the bundled record-format reference for evidence fields and a complete worked example.
