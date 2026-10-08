# Identify Key Assumptions: Method Reference

Use this reference when the core workflow requires deeper analysis. Keep the final artifact concise and move raw evidence to linked notes or data files.

## Decision objective

A complete assumption register with atomic statements, evidence status, dependency links, risk ranking, and test priority.

## Method notes

- Preferred format: 'For [population/context], [observable behavior/outcome] will be at least [threshold] within [time].'
- Rank impact by what breaks if false and uncertainty by evidence quality, recency, directness, and sample relevance.
- Map dependencies so tests of upstream assumptions occur before downstream optimization.

## Evidence hierarchy

Prefer evidence in this order, while accounting for relevance and sample bias:

1. Sustained customer behavior, payment, retention, or operational outcomes.
2. Binding commitments, deposits, signed proposals, or demonstrated effort.
3. Direct observation and recent specific examples from target customers.
4. Structured interviews with qualified customers and buying stakeholders.
5. Customer-provided records, workflow artifacts, and internal data.
6. Credible secondary research that matches the market definition.
7. Expert opinion and team judgment, clearly labeled as assumptions.

## Quality rubric

Score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Specificity | Vague or generic | Partly bounded | Population, context, unit, and horizon are explicit |
| Evidence | Opinion only | Some direct evidence | Multiple relevant sources including behavioral evidence |
| Traceability | No sources | Partial sourcing | Material claims link to dated sources and assumptions |
| Contradictions | Ignored | Mentioned | Analyzed and reflected in the decision |
| Actionability | No decision | General recommendation | Decision, owner, threshold, and next action are explicit |

A final score below 8/10 is not decision-grade. Either gather stronger evidence or narrow the claim.

## Review questions

- Can the team demonstrate: each assumption is specific enough for one focused test.
- Can the team demonstrate: high-impact assumptions from all major venture dimensions are included.
- Can the team demonstrate: existing evidence is separated from confidence or opinion.
- Can the team demonstrate: priority follows risk, not ease or team preference.

Also ask:

- What observation would make the current conclusion wrong?
- Which input has the greatest leverage on the decision?
- Is the evidence from the actual beachhead and actual decision makers?
- Have incentives, selection bias, and survivorship bias been considered?
- Is the next action the cheapest action that can materially reduce uncertainty?
