# Synthetic worked example: Identify Key Assumptions

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "identify-key-assumptions",
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
    "assumptions": [
      {
        "id": "A-001",
        "hypothesis": "Owners will pay for draft preparation while retaining approval",
        "category": "viability",
        "impact": 5,
        "uncertainty": 4,
        "risk_score": 20,
        "reversal_threshold": "No qualified prospect accepts an authorized paid pilot",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "test_queue": [
      {
        "assumption_id": "A-001",
        "priority": 1,
        "dependency": "Founder approves outreach scope",
        "next_evidence": "Paid-pilot proposal decisions and objections",
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

Use a 1-5 impact and uncertainty scale. A score of 20 prioritizes a test; it is not a probability or proof of risk.

## Failure case

Compound hypotheses, out-of-range ratings, incorrect risk multiplication, or queue references to missing assumptions fail the checks.
