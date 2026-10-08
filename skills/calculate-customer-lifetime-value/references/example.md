# Synthetic worked example: Calculate Customer Lifetime Value

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-customer-lifetime-value",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer_unit": "Acquired practice",
    "currency": "EUR",
    "period_unit": "month",
    "horizon_periods": 2,
    "discount_rate_per_period": 0.01
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
    "cashflows": [
      {
        "scenario": "conservative",
        "period": 1,
        "retention": 1.0,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 70.0,
        "discounted_contribution": 69.3069306930693,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "conservative",
        "period": 2,
        "retention": 0.6,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 42.0,
        "discounted_contribution": 41.17243407509068,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "period": 1,
        "retention": 1.0,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 70.0,
        "discounted_contribution": 69.3069306930693,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "period": 2,
        "retention": 0.8,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 56.0,
        "discounted_contribution": 54.89657876678757,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "period": 1,
        "retention": 1.0,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 70.0,
        "discounted_contribution": 69.3069306930693,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "period": 2,
        "retention": 0.9,
        "revenue_per_active_customer": 100,
        "gross_margin": 0.8,
        "service_cost": 10,
        "expected_contribution": 63.0,
        "discounted_contribution": 61.75865111263602,
        "evidence": [
          "E-001"
        ]
      }
    ],
    "summary": [
      {
        "scenario": "conservative",
        "ltv": 110.47936476815998,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "ltv": 124.20350945985687,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "ltv": 131.06558180570534,
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

Expected contribution is survival probability times (active-customer revenue times gross margin minus additional service cost). Discount each period separately and sum; acquisition cost is excluded.

## Failure case

Retention above one or increasing across a cohort, missing periods, double-counted service costs, or incorrect discounted totals require correction. Arithmetic checks cannot detect a misclassified cost.
