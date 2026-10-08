# Synthetic worked example: Discover a Venture

The structured record is the source for the decision below. Do not replace missing research with invented results.

<!-- venture-record:start -->
```json
{
  "schema_version": 2,
  "skill": "discover-venture",
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
    "venture": [
      {
        "problem": "Consultants lose billable work when invoices are late.",
        "current_workaround": "A shared spreadsheet and manual reminders.",
        "proposed_solution": "Prepare draft invoices for the owner to approve.",
        "difference": "Reuse project records instead of retyping them.",
        "payer_and_model": "The practice owner; monthly subscription is an untested hypothesis.",
        "founder_confirmation": "Synthetic founder confirms this scope, with no automatic sending.",
        "evidence": [
          "E-001"
        ]
      }
    ],
    "constraints": [
      {
        "resource": "Founder time",
        "availability": "Eight hours per week",
        "boundary": "No external contact or invoice sending without approval",
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

The confirmation concerns intended scope, not evidence that customers want the product. A solo founder needs no invented cofounder agreement.

## Failure case

A thesis alone, an empty constraints table, or an assumption substituted for the founder's confirmation cannot complete discovery.
