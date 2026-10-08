# Synthetic worked example: Define the Product Concept

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "define-product-concept",
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
    "storyboard": [
      {
        "step": 1,
        "user_action": "Review imported hours before approving an invoice",
        "input": "Approved time sheet",
        "visible_output": "Invoice preview with highlighted differences",
        "benefit": "Avoid retyping while retaining control",
        "non_goal": "Automatic sending or bookkeeping advice",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "concept_test": [
      {
        "participant_id": "P-01",
        "prompt": "Explain what you think happens after approval.",
        "observed_understanding": "Participant expected a draft, not an automatically sent invoice",
        "revision": "Label the action Create draft",
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

A text storyboard is acceptable before mockups exist. Record the user's explanation rather than the presenter's explanation.

## Failure case

Missing visible outputs or unsourced claims that users understood the concept should remain a research plan.
