# Synthetic worked example: Chart Your Competitive Position

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "chart-your-competitive-position",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer": "Small consulting teams",
    "geography": "Ireland",
    "decision_horizon": "Next 90 days"
  },
  "evidence": [
    {
      "id": "E-001",
      "type": "fact",
      "statement": "Synthetic illustration only; not an actual customer or financial observation.",
      "source": "https://example.com/synthetic-illustration",
      "date": "2026-01-08",
      "confidence": "low",
      "contradictions": "The example is constructed and cannot support a real business decision.",
      "next_test": ""
    }
  ],
  "data": {
    "axes": [
      {
        "axis": "x",
        "customer_priority": "Invoice accuracy",
        "low_anchor": "Corrections after sending",
        "high_anchor": "Accurate before approval",
        "evidence": [
          "E-001"
        ]
      },
      {
        "axis": "y",
        "customer_priority": "Preparation effort",
        "low_anchor": "Retype every line",
        "high_anchor": "Review prefilled draft",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "alternatives": [
      {
        "alternative": "Shared spreadsheet",
        "kind": "status-quo",
        "x_score": 0.6,
        "y_score": 0.2,
        "uncertainty": "Single observed workflow",
        "evidence": [
          "E-001"
        ]
      },
      {
        "alternative": "Proposed invoice assistant",
        "kind": "product",
        "x_score": 0.7,
        "y_score": 0.8,
        "uncertainty": "Untested hypothesis, not superiority evidence",
        "evidence": [
          "E-001"
        ]
      }
    ]
  },
  "research_plan": [],
  "decision": "Use this shape to analyze the real venture; do not reuse these conclusions.",
  "limitations": "Synthetic fixture only. Source authenticity and business validity have not been established.",
  "next_actions": [
    {
      "action": "Replace the illustration with authorized venture evidence",
      "owner": "Venture owner",
      "due_date": "2026-02-01",
      "evidence_expected": "Dated source records and reconciled inputs"
    }
  ]
}
```
<!-- venture-record:end -->

## Worked reasoning

Scores need anchored meanings and sources. The example does not establish that the proposed product wins.

## Failure case

Missing x/y definitions, out-of-range scores, or omitting the status quo are rejected.
