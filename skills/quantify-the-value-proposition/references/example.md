# Synthetic worked example: Quantify the Value Proposition

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "quantify-the-value-proposition",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer": "Practice owner",
    "input_unit": "Hours per invoice cycle",
    "value_unit": "EUR per year",
    "horizon": "12 monthly cycles"
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
    "outcomes": [
      {
        "scenario": "conservative",
        "baseline": 2,
        "future": 0.5,
        "direction": "decrease",
        "unit_value": 50,
        "frequency": 12,
        "realization": 0.5,
        "realized_value": 450.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "base",
        "baseline": 2,
        "future": 0.5,
        "direction": "decrease",
        "unit_value": 50,
        "frequency": 12,
        "realization": 0.75,
        "realized_value": 675.0,
        "evidence": [
          "E-001"
        ]
      },
      {
        "scenario": "upside",
        "baseline": 2,
        "future": 0.5,
        "direction": "decrease",
        "unit_value": 50,
        "frequency": 12,
        "realization": 1.0,
        "realized_value": 900.0,
        "evidence": [
          "E-001"
        ]
      }
    ],
    "validation": [
      {
        "baseline_source": "Synthetic owner walkthrough",
        "customer_response": "Owner recognizes the current workflow but future savings are untested",
        "disputed_input": "Realization depends on export quality",
        "next_test": "Time a consented pilot cycle",
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

The base case is 1.5 hours saved times EUR 50/hour times 12 cycles times 75% realization = EUR 675/year. It is a value hypothesis, not observed savings.

## Failure case

Incompatible units, a realization factor above one, or a result that disagrees with the explicit inputs fails the checks.
