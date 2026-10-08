# Calculate Customer Lifetime Value: Method Reference

Use this reference when the core workflow requires deeper analysis. Keep the final artifact concise and move raw evidence to linked notes or data files.

## Decision objective

A cohort-aware, sensitivity-tested LTV model using contribution economics and explicit retention assumptions.

## Method notes

- General form: LTV = sum over periods of (retention probability x period contribution) / (1 + discount rate)^period.
- For transaction businesses, model order frequency, contribution per order, and active-customer probability separately.
- Report payback and cash timing alongside LTV later; a high LTV can still hide a financing problem.

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

- Can the team demonstrate: lTV uses contribution profit, not revenue.
- Can the team demonstrate: acquisition cost is excluded from the LTV numerator.
- Can the team demonstrate: retention and time horizon are explicit and cohort-consistent.
- Can the team demonstrate: future cash flows are discounted and sensitivity-tested.

Also ask:

- What observation would make the current conclusion wrong?
- Which input has the greatest leverage on the decision?
- Is the evidence from the actual beachhead and actual decision makers?
- Have incentives, selection bias, and survivorship bias been considered?
- Is the next action the cheapest action that can materially reduce uncertainty?
