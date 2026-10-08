# Synthetic worked example: Test Key Assumptions

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "test-key-assumptions",
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
    "experiments": [
      {
        "id": "X-001",
        "hypothesis": "Qualified owners accept a bounded paid pilot",
        "population": "Five owner-managed practices",
        "metric": "Number accepting without permanent discount",
        "sample_size": 5,
        "threshold": 2,
        "comparison": "at-least",
        "precommitted_on": "2026-01-01",
        "observed_on": "2026-01-08",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "results": [
      {
        "experiment_id": "X-001",
        "observed_value": 1,
        "outcome": "fail",
        "decision": "Revise the offer and investigate setup objections before expanding",
        "confounds": "Small referral-based synthetic sample",
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

One acceptance misses a threshold of two. The correct output is a failed test and an evidence-led next action, not a lower threshold.

## Failure case

A pass verdict that contradicts the threshold, or a precommitment dated after observations, is rejected.
