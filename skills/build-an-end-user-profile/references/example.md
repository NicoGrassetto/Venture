# Synthetic worked example: Build an End-user Profile

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "build-an-end-user-profile",
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
    "attributes": [
      {
        "attribute": "Invoice ownership",
        "observed_range": "Owner prepares and approves invoices",
        "decision_consequence": "Design for one accountable approver",
        "inclusion": "Personally handles monthly billing",
        "exclusion": "Never sees billing workflow",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "screener": [
      {
        "question": "Walk through your last invoice preparation.",
        "qualifying_answer": "Can describe the actual steps they performed",
        "reason": "Confirms first-hand workflow knowledge",
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

Keep an attribute only when it changes recruiting, product, or adoption decisions. Organization size is not a substitute for an end-user profile.

## Failure case

A profile based only on assumptions must remain a research plan, and an attribute without a decision consequence is incomplete.
