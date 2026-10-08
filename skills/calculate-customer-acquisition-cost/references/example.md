# Synthetic worked example: Calculate Customer Acquisition Cost

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-customer-acquisition-cost",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "currency": "EUR",
    "contribution_period": "month",
    "spend_window": "January acquisition cohort",
    "sales_lag_periods": 1
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
    "acquisition": [
      {
        "scenario": "conservative",
        "cohort": "January pilots",
        "acquisition_spend": 1200,
        "new_paying_customers": 2,
        "cac": 600.0,
        "contribution_per_period": 40,
        "simple_payback_periods": 15.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "cohort": "January pilots",
        "acquisition_spend": 1200,
        "new_paying_customers": 4,
        "cac": 300.0,
        "contribution_per_period": 40,
        "simple_payback_periods": 7.5,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "cohort": "January pilots",
        "acquisition_spend": 1200,
        "new_paying_customers": 6,
        "cac": 200.0,
        "contribution_per_period": 40,
        "simple_payback_periods": 5.0,
        "evidence": [
          "E-001"
        ]
      }
    ],
    "cost_coverage": [
      {
        "cost": "Founder outreach time and acquisition tools",
        "treatment": "Included in fully loaded spend",
        "allocation_basis": "Recorded hours and invoices attributable to this cohort",
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

Base CAC is EUR 1,200 / 4 = EUR 300. Simple payback is 7.5 months at a constant EUR 40 monthly contribution; use a cash schedule if contribution or retention varies.

## Failure case

Zero paying customers, omitted cost treatment, or inconsistent CAC/payback arithmetic fail the checks.
