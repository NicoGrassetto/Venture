# Synthetic worked example: Select a Beachhead Market

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "select-a-beachhead-market",
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
    "selection": [
      {
        "chosen_segment": "Owner-managed consultancies",
        "inclusions": "One owner approves invoices and buys software",
        "exclusions": "Large firms requiring procurement integrations",
        "homogeneity": "Monthly time-based invoicing and owner approval",
        "reversal_trigger": "Qualified interviews show incompatible workflows",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "scorecard": [
      {
        "candidate": "Owner-managed consultancies",
        "criterion": "Access to qualified users",
        "weight": 1.0,
        "score": 0.8,
        "weighted_score": 0.8,
        "rationale": "A reachable local network; illustrative single criterion",
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

Weights sum to one per candidate. Scores organize judgment; they are not proof of demand. Test whether plausible weight changes reverse the choice.

## Failure case

Multiple chosen segments, inconsistent weights, or a weighted score that is not weight times score are rejected.
