# Synthetic worked example: Validate Customer Traction

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "validate-customer-traction",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer": "Owner-managed practices",
    "cohort_window": "January paid-pilot entrants",
    "retention_period": "Second monthly billing cycle"
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
    "cohorts": [
      {
        "cohort": "January pilots",
        "acquired": 10,
        "activated": 8,
        "paid": 6,
        "retained": 4,
        "retention_rate": 0.4,
        "customer_outcome": "Four owners repeated the approved draft workflow",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "diagnosis": [
      {
        "cohort": "January pilots",
        "bottleneck": "Second-cycle setup effort",
        "contradiction": "Some paid users did not return",
        "decision": "iterate",
        "next_test": "Observe the second-cycle import with consent",
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

Retention here uses acquired customers as its denominator, explicitly. Do not switch to paid or activated denominators to improve the reported percentage.

## Failure case

Impossible funnel counts, an incorrect retention denominator, or assumption-only traction data cannot pass.
