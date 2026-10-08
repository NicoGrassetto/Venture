# Synthetic worked example: Map the Customer Buying Process

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "map-customer-buying-process",
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
    "buying_stages": [
      {
        "stage": "Approve paid pilot",
        "customer_owner": "Practice owner",
        "entry_condition": "Draft invoice matches a recent approved invoice",
        "exit_evidence": "Signed paid-pilot acceptance",
        "elapsed_days": 7,
        "dependency": "Confirm accountant export format",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "obstacles": [
      {
        "obstacle": "Export format mismatch",
        "impact": "Pilot cannot begin",
        "mitigation": "Validate one sample file before quoting the pilot",
        "owner": "Founder",
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

A signed agreement, payment, and implementation readiness can occur at different times; represent each material delay.

## Failure case

Missing customer-side owners, exit evidence, or negative elapsed times fail validation.
