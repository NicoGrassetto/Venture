# Synthetic worked example: Build a Financial Plan

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "build-financial-plan",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "currency": "EUR",
    "horizon_months": 3,
    "opening_cash": 1000,
    "customer_unit": "Paying practice"
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
    "cashflow": [
      {
        "scenario": "conservative",
        "month": 1,
        "opening_cash": 1000.0,
        "units": 2,
        "price": 100,
        "revenue": 200,
        "cogs": 40,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": -240,
        "closing_cash": 760.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "conservative",
        "month": 2,
        "opening_cash": 760.0,
        "units": 2,
        "price": 100,
        "revenue": 200,
        "cogs": 40,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": -240,
        "closing_cash": 520.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "conservative",
        "month": 3,
        "opening_cash": 520.0,
        "units": 2,
        "price": 100,
        "revenue": 200,
        "cogs": 40,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": -240,
        "closing_cash": 280.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "month": 1,
        "opening_cash": 1000.0,
        "units": 5,
        "price": 100,
        "revenue": 500,
        "cogs": 100,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 0,
        "closing_cash": 1000.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "month": 2,
        "opening_cash": 1000.0,
        "units": 5,
        "price": 100,
        "revenue": 500,
        "cogs": 100,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 0,
        "closing_cash": 1000.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "month": 3,
        "opening_cash": 1000.0,
        "units": 5,
        "price": 100,
        "revenue": 500,
        "cogs": 100,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 0,
        "closing_cash": 1000.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "month": 1,
        "opening_cash": 1000.0,
        "units": 10,
        "price": 100,
        "revenue": 1000,
        "cogs": 200,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 400,
        "closing_cash": 1400.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "month": 2,
        "opening_cash": 1400.0,
        "units": 10,
        "price": 100,
        "revenue": 1000,
        "cogs": 200,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 400,
        "closing_cash": 1800.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "month": 3,
        "opening_cash": 1800.0,
        "units": 10,
        "price": 100,
        "revenue": 1000,
        "cogs": 200,
        "opex": 400,
        "taxes": 0,
        "change_working_capital": 0,
        "capex": 0,
        "net_financing": 0,
        "operating_cash_flow": 400,
        "closing_cash": 2200.0,
        "evidence": [
          "E-001"
        ]
      }
    ],
    "summary": [
      {
        "scenario": "conservative",
        "minimum_cash": 280.0,
        "additional_funding_needed": 0,
        "first_negative_month": 0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "minimum_cash": 1000.0,
        "additional_funding_needed": 0,
        "first_negative_month": 0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "minimum_cash": 1000.0,
        "additional_funding_needed": 0,
        "first_negative_month": 0,
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

Revenue is units times price. Operating cash subtracts COGS, operating expenses, taxes, and increased working capital. Closing cash adds net financing and subtracts capex. first_negative_month=0 means no shortfall within the modeled horizon, not infinite runway.

## Failure case

Missing months, mixed currencies, incorrect cash continuity, unsupported funding, or arithmetic inconsistencies require correction. Evidence review still checks cost classification and financing credibility.
