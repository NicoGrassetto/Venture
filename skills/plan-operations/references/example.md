# Synthetic worked example: Plan Operations

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "plan-operations",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer": "Pilot practices",
    "delivery_unit": "Approved invoice batch",
    "planning_period": "One month",
    "currency": "EUR"
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
    "capacity": [
      {
        "activity": "Review invoice imports",
        "demand_units": 20,
        "hours_per_unit": 0.5,
        "available_hours": 8,
        "required_hours": 10,
        "gap_hours": 2,
        "cost_per_hour": 30,
        "labor_cost": 300,
        "owner": "Operations owner",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "dependencies": [
      {
        "supplier_or_dependency": "Accounting export access",
        "lead_days": 3,
        "failure_trigger": "Approved export cannot be obtained before the billing cycle",
        "fallback": "Reduce pilot scope; do not send unverified invoices",
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

Twenty batches at half an hour require ten hours; eight available hours leave a two-hour gap. The plan must reduce demand, add capacity, or change the promise before launch.

## Failure case

Incorrect capacity or labor-cost arithmetic, unowned dependencies, or a missing fallback fails completion.
