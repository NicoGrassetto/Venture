# Calculate Customer Lifetime Value: Method Reference

Use this reference when the core workflow requires deeper analysis. Keep the final artifact concise and move raw evidence to linked notes or data files.

## Decision objective

A cohort-aware, sensitivity-tested LTV model using contribution economics and explicit retention assumptions.

## Method notes

- General form: LTV = sum over periods of (retention probability x period contribution) / (1 + discount rate)^period.
- For transaction businesses, model order frequency, contribution per order, and active-customer probability separately.
- Report payback and cash timing alongside LTV later; a high LTV can still hide a financing problem.

The bundled numeric contract uses a nonincreasing cohort-survival curve and a
discount rate expressed per modeled period. Additional service cost excludes
costs already included in gross margin. If reactivation materially changes
active-customer probability, use a separately reviewed model rather than
forcing those observations into this survival-only representation.

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

## Worked example

See [the synthetic worked example](example.md) and [record format](record-format.md).
