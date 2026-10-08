# Synthetic worked example: Calculate Beachhead Market TAM

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "calculate-beachhead-market-tam",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer_unit": "Practice",
    "geography": "Ireland",
    "currency": "EUR",
    "revenue_period": "year"
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
    "markets": [
      {
        "scenario": "conservative",
        "market": "Owner-managed consultancies",
        "units": 100,
        "annual_revenue_per_unit": 960,
        "annual_tam": 96000,
        "exclusions": "Large firms with procurement-heavy workflows",
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "market": "Owner-managed consultancies",
        "units": 200,
        "annual_revenue_per_unit": 960,
        "annual_tam": 192000,
        "exclusions": "Large firms with procurement-heavy workflows",
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "market": "Owner-managed consultancies",
        "units": 300,
        "annual_revenue_per_unit": 960,
        "annual_tam": 288000,
        "exclusions": "Large firms with procurement-heavy workflows",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "triangulation": [
      {
        "scenario": "conservative",
        "top_down_annual_tam": 100000,
        "difference_explanation": "Illustrative independent estimate uses a slightly different price assumption",
        "next_source": "Reconcile eligible-practice count against recent registry data",
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "top_down_annual_tam": 200000,
        "difference_explanation": "Illustrative independent estimate uses a slightly different price assumption",
        "next_source": "Reconcile eligible-practice count against recent registry data",
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "top_down_annual_tam": 300000,
        "difference_explanation": "Illustrative independent estimate uses a slightly different price assumption",
        "next_source": "Reconcile eligible-practice count against recent registry data",
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

For the base case, 200 practices times EUR 960 per year gives EUR 192,000 annual TAM. This is 100% market potential, not forecast sales.

## Failure case

Mixing monthly prices with annual revenue, missing scenarios, or a total that differs from units times annual revenue is rejected.
