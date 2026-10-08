# Synthetic worked example: Map the Customer Journey

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "map-customer-journey",
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
    "journey": [
      {
        "stage": "Prepare invoices",
        "state": "current",
        "actor": "Practice owner",
        "action": "Copy approved hours",
        "artifact": "Draft invoice",
        "time_cost": "Two hours each month",
        "failure_mode": "Hours omitted",
        "evidence": [
          "E-001"
        ]
      },
      {
        "stage": "Prepare invoices",
        "state": "proposed",
        "actor": "Practice owner",
        "action": "Review imported hours",
        "artifact": "Review queue",
        "time_cost": "Thirty-minute hypothesis",
        "failure_mode": "Incorrect import mapping",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "barriers": [
      {
        "barrier": "Accounting export format",
        "handoff": "Time records to billing",
        "mitigation": "Test an export with the owner",
        "owner": "Founder",
        "validation": "Compare totals against an approved invoice",
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

Current-state observations and proposed-state hypotheses must stay visibly distinct. Customer-side handoffs matter even when no screen is involved.

## Failure case

A map with only a proposed journey or no accountable barrier owner cannot complete the analysis.
