# Build a Financial Plan: Method Reference

## Monthly model

Use one currency and customer unit per model. For subscriptions, `units` means
active paying accounts in the month, not cumulative sign-ups. For transaction
businesses, use transactions and a per-transaction price. Do not mix these
units within a scenario.

- Revenue = units x price.
- Operating cash flow = revenue - COGS - operating expenses - taxes - change
  in working capital.
- Closing cash = opening cash + operating cash flow - capex + net financing.
- The following month's opening cash equals the prior closing cash.
- Additional funding needed = max(0, -minimum modeled cash).

A positive change in working capital consumes cash; a negative change releases
cash. Net financing can be negative for principal repayments. Do not also
place principal repayment in operating expenses.

## Scenarios and runway

Change demand, pricing, costs, or timing drivers explicitly, not a blanket
percentage on the final total. Include opening cash in the minimum-cash
calculation. `first_negative_month` is the first modeled month below zero;
zero means no shortfall within the specified horizon.

This is a simplified planning model, not a complete accounting system.
Non-cash expenses, multiple currencies, deferred revenue, inventory, and
complex financing may need a separate reconciled model and professional review.

## Cross-checks

Demand must be deliverable within operating capacity or an explicitly funded
capacity increase. Customer acquisition assumptions must agree with the sales
funnel; contribution assumptions must agree with LTV and acquisition-cost
work. Cite the same evidence IDs rather than creating disconnected numbers.

See [the worked example](example.md) and [record format](record-format.md).

## Worked example

See [the synthetic worked example](example.md) and [record format](record-format.md).
