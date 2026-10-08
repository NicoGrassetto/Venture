# Synthetic worked example: Map the Sales Process

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "map-the-sales-process",
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
    "sales_stages": [
      {
        "stage": "Paid pilot proposal",
        "customer_exit": "Owner signs the proposal",
        "seller_action": "Show a comparison using consented sample data",
        "owner": "Founder",
        "channel": "Qualified referral",
        "entered": 10,
        "converted": 2,
        "conversion_rate": 0.2,
        "elapsed_days": 7,
        "cost": 600,
        "evidence": [
          "E-001"
        ]
      }
    ],
    "bottlenecks": [
      {
        "stage": "Paid pilot proposal",
        "hypothesis": "Setup uncertainty delays decisions",
        "experiment": "Offer a bounded export-format review",
        "metric": "Proposal-to-paid-pilot conversion",
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

Two conversions out of ten entries is 20%, not evidence of scalable channel economics. Include founder time in acquisition costing.

## Failure case

Converted counts above entries, or rates that disagree with counts, are rejected.
