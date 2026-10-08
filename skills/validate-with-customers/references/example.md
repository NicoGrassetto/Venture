# Synthetic worked example: Validate with Customers

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "validate-with-customers",
  "stage": "completed-analysis",
  "synthetic": true,
  "venture": "Synthetic invoice-assistant example",
  "owner": "Synthetic founder",
  "date": "2026-01-08",
  "scope": {
    "customer": "Owner-managed consultancies",
    "geography": "Ireland",
    "target_sample": 3
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
    "participants": [
      {
        "participant_id": "P-01",
        "qualification": "Owner handles actual monthly invoices",
        "method": "interview",
        "current_behavior": "Reconciles time sheets manually",
        "finding": "Accuracy matters more than fully automatic sending",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "synthesis": [
      {
        "observed_sample": 1,
        "pattern": "Manual reconciliation may create avoidable effort",
        "contradiction": "This participant prefers an approval step",
        "decision": "inconclusive",
        "sample_limitation": "Only one of three planned independent participants; recruit from another channel",
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

A shortfall can produce an honest inconclusive analysis, but not a proceed decision. Set a justified sample target rather than applying a universal count.

## Failure case

Recruiting contacts alone are not completed interviews. A sample below the declared target cannot produce proceed or revise as if the target were met.
