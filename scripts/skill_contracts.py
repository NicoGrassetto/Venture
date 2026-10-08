"""Task-specific workbook contracts and deliberately synthetic worked examples."""

from __future__ import annotations

from typing import TypedDict


class Contract(TypedDict):
    skill: str
    title: str
    not_for: str
    input_gate: str
    next_skills: list[str]
    scope: dict[str, str]
    tables: dict[str, dict[str, str]]
    observations_required: bool
    observed_tables: list[str]
    example_scope: dict[str, object]
    example_data: dict[str, list[dict[str, object]]]
    example_note: str
    failure_case: str


CONTRACTS: dict[str, Contract] = {}
SCENARIO = "choice:conservative,base,upside"


def row(**values: object) -> dict[str, object]:
    return dict(values, evidence=["E-001"])


def define(
    skill: str, title: str, *, not_for: str, gate: str, next_skills: list[str],
    tables: dict[str, dict[str, str]], example: dict[str, list[dict[str, object]]],
    note: str, failure: str, scope: dict[str, str] | None = None,
    example_scope: dict[str, object] | None = None, observed_tables: list[str] | None = None,
) -> None:
    CONTRACTS[skill] = {
        "skill": skill, "title": title, "not_for": not_for, "input_gate": gate,
        "next_skills": next_skills,
        "scope": scope or {"customer": "text", "geography": "text", "decision_horizon": "text"},
        "tables": {name: dict(columns, evidence="evidence") for name, columns in tables.items()},
        "observations_required": bool(observed_tables),
        "observed_tables": observed_tables or [],
        "example_scope": example_scope or {
            "customer": "Small consulting teams", "geography": "Ireland", "decision_horizon": "Next 90 days",
        },
        "example_data": example, "example_note": note, "failure_case": failure,
    }


define(
    "discover-venture", "Discover a Venture",
    not_for="Product design, market sizing, or inventing a venture from a one-line pitch.",
    gate="Clarify intent with the founder. A completed analysis needs an actual reflected summary and explicit founder confirmation; silence is not confirmation.",
    next_skills=["identify-key-assumptions", "market-segmentation"],
    tables={
        "venture": {"problem": "text", "current_workaround": "text", "proposed_solution": "text", "difference": "text", "payer_and_model": "text", "founder_confirmation": "text"},
        "constraints": {"resource": "text", "availability": "text", "boundary": "text", "owner": "text"},
    },
    example={
        "venture": [row(problem="Consultants lose billable work when invoices are late.", current_workaround="A shared spreadsheet and manual reminders.", proposed_solution="Prepare draft invoices for the owner to approve.", difference="Reuse project records instead of retyping them.", payer_and_model="The practice owner; monthly subscription is an untested hypothesis.", founder_confirmation="Synthetic founder confirms this scope, with no automatic sending.")],
        "constraints": [row(resource="Founder time", availability="Eight hours per week", boundary="No external contact or invoice sending without approval", owner="Founder")],
    },
    note="The confirmation concerns intended scope, not evidence that customers want the product. A solo founder needs no invented cofounder agreement.",
    failure="A thesis alone, an empty constraints table, or an assumption substituted for the founder's confirmation cannot complete discovery.",
    observed_tables=["venture"],
)
define(
    "market-segmentation", "Market Segmentation",
    not_for="Choosing a winner before comparing distinct customer contexts.",
    gate="Use a research plan when no qualified customer observations exist. Keep end user, payer, application, and access distinct.",
    next_skills=["select-a-beachhead-market"],
    tables={
        "segments": {"segment": "text", "end_user": "text", "application": "text", "problem": "text", "payer": "text", "current_solution": "text", "access": "text"},
        "comparison": {"segment": "text", "urgency": "text", "buying_process": "text", "product_requirements": "text", "decision": "choice:shortlist,defer,reject", "reason": "text"},
    },
    example={
        "segments": [row(segment="Owner-managed consultancies", end_user="Practice owner", application="Monthly client invoicing", problem="Re-entering approved project hours", payer="Practice owner", current_solution="Spreadsheet and accounting package", access="Local professional network")],
        "comparison": [row(segment="Owner-managed consultancies", urgency="Repeated at month end", buying_process="Owner approves within a monthly software budget", product_requirements="Import approved time records", decision="shortlist", reason="Reachable users and one bounded workflow")],
    },
    note="This single-row illustration shows the record shape; real segmentation should compare plausible alternatives and retain rejected candidates.",
    failure="Industry labels without an end user or buying process, or unknown evidence IDs, fail the contract.",
    observed_tables=["segments"],
)
define(
    "select-a-beachhead-market", "Select a Beachhead Market",
    not_for="Generating segments from scratch or adding adjacent markets to the first product.",
    gate="Compare explicit candidates. A provisional choice may use assumptions, but record exclusions and reversal conditions.",
    next_skills=["build-an-end-user-profile", "calculate-beachhead-market-tam"],
    tables={
        "selection": {"chosen_segment": "text", "inclusions": "text", "exclusions": "text", "homogeneity": "text", "reversal_trigger": "text"},
        "scorecard": {"candidate": "text", "criterion": "text", "weight": "probability", "score": "probability", "weighted_score": "nonnegative", "rationale": "text"},
    },
    example={
        "selection": [row(chosen_segment="Owner-managed consultancies", inclusions="One owner approves invoices and buys software", exclusions="Large firms requiring procurement integrations", homogeneity="Monthly time-based invoicing and owner approval", reversal_trigger="Qualified interviews show incompatible workflows")],
        "scorecard": [row(candidate="Owner-managed consultancies", criterion="Access to qualified users", weight=1.0, score=0.8, weighted_score=0.8, rationale="A reachable local network; illustrative single criterion")],
    },
    note="Weights sum to one per candidate. Scores organize judgment; they are not proof of demand. Test whether plausible weight changes reverse the choice.",
    failure="Multiple chosen segments, inconsistent weights, or a weighted score that is not weight times score are rejected.",
)
define(
    "build-an-end-user-profile", "Build an End-user Profile",
    not_for="Profiling the paying organization or replacing customer research with decorative demographics.",
    gate="Separate users from buyers and beneficiaries. With no observations, create a recruiting plan rather than claim a validated profile.",
    next_skills=["profile-the-persona", "validate-with-customers"],
    tables={
        "attributes": {"attribute": "text", "observed_range": "text", "decision_consequence": "text", "inclusion": "text", "exclusion": "text"},
        "screener": {"question": "text", "qualifying_answer": "text", "reason": "text"},
    },
    example={
        "attributes": [row(attribute="Invoice ownership", observed_range="Owner prepares and approves invoices", decision_consequence="Design for one accountable approver", inclusion="Personally handles monthly billing", exclusion="Never sees billing workflow")],
        "screener": [row(question="Walk through your last invoice preparation.", qualifying_answer="Can describe the actual steps they performed", reason="Confirms first-hand workflow knowledge")],
    },
    note="Keep an attribute only when it changes recruiting, product, or adoption decisions. Organization size is not a substitute for an end-user profile.",
    failure="A profile based only on assumptions must remain a research plan, and an attribute without a decision consequence is incomplete.",
    observed_tables=["attributes"],
)
define(
    "profile-the-persona", "Profile the Persona",
    not_for="A market-wide profile, a fictional composite presented as real, or a buyer map.",
    gate="Use a real representative user's sourced observations and a privacy-safe identifier; do not invent a biography.",
    next_skills=["map-customer-journey", "quantify-the-value-proposition"],
    tables={
        "persona": {"participant_id": "text", "representativeness": "text", "goal": "text", "workaround": "text", "motivation": "text"},
        "purchasing_criteria": {"rank": "positive_integer", "criterion": "text", "tradeoff": "text", "product_implication": "text"},
    },
    example={
        "persona": [row(participant_id="P-01", representativeness="Owner also prepares monthly invoices", goal="Send accurate invoices without losing a billable afternoon", workaround="Reconcile time sheets manually", motivation="Avoid embarrassing billing corrections")],
        "purchasing_criteria": [row(rank=1, criterion="Accuracy before speed", tradeoff="Will accept an extra approval step to prevent wrong invoices", product_implication="Require review before sending")],
    },
    note="A persona is a decision anchor, not statistical evidence about the whole market. Revisit it when other qualified users contradict the pattern.",
    failure="Duplicate priority ranks or a fictional assumption presented as an observed participant fail completion.",
    observed_tables=["persona", "purchasing_criteria"],
)
define(
    "map-customer-journey", "Map the Customer Journey",
    not_for="Only the product's screens or only the seller's sales funnel.",
    gate="Map the current journey before the proposed one; include purchase, use, support, and renewal where relevant.",
    next_skills=["define-product-concept", "map-customer-buying-process"],
    tables={
        "journey": {"stage": "text", "state": "choice:current,proposed", "actor": "text", "action": "text", "artifact": "text", "time_cost": "text", "failure_mode": "text"},
        "barriers": {"barrier": "text", "handoff": "text", "mitigation": "text", "owner": "text", "validation": "text"},
    },
    example={
        "journey": [
            row(stage="Prepare invoices", state="current", actor="Practice owner", action="Copy approved hours", artifact="Draft invoice", time_cost="Two hours each month", failure_mode="Hours omitted"),
            row(stage="Prepare invoices", state="proposed", actor="Practice owner", action="Review imported hours", artifact="Review queue", time_cost="Thirty-minute hypothesis", failure_mode="Incorrect import mapping"),
        ],
        "barriers": [row(barrier="Accounting export format", handoff="Time records to billing", mitigation="Test an export with the owner", owner="Founder", validation="Compare totals against an approved invoice")],
    },
    note="Current-state observations and proposed-state hypotheses must stay visibly distinct. Customer-side handoffs matter even when no screen is involved.",
    failure="A map with only a proposed journey or no accountable barrier owner cannot complete the analysis.",
)
define(
    "define-product-concept", "Define the Product Concept",
    not_for="A build-ready technical specification or a feature backlog.",
    gate="A concept can be provisional, but define the customer outcome, storyboard, non-goals, and an unled comprehension test.",
    next_skills=["quantify-the-value-proposition", "test-key-assumptions"],
    tables={
        "storyboard": {"step": "positive_integer", "user_action": "text", "input": "text", "visible_output": "text", "benefit": "text", "non_goal": "text"},
        "concept_test": {"participant_id": "text", "prompt": "text", "observed_understanding": "text", "revision": "text"},
    },
    example={
        "storyboard": [row(step=1, user_action="Review imported hours before approving an invoice", input="Approved time sheet", visible_output="Invoice preview with highlighted differences", benefit="Avoid retyping while retaining control", non_goal="Automatic sending or bookkeeping advice")],
        "concept_test": [row(participant_id="P-01", prompt="Explain what you think happens after approval.", observed_understanding="Participant expected a draft, not an automatically sent invoice", revision="Label the action Create draft")],
    },
    note="A text storyboard is acceptable before mockups exist. Record the user's explanation rather than the presenter's explanation.",
    failure="Missing visible outputs or unsourced claims that users understood the concept should remain a research plan.",
    observed_tables=["concept_test"],
)
define(
    "validate-with-customers", "Validate with Customers",
    not_for="A lead list, a sales pitch, or claiming that a sample size proves the whole market.",
    gate="Research-plan mode covers recruitment only. Completed analysis needs qualified participants, observed behavior, cross-customer synthesis, and an explicit sample limitation.",
    next_skills=["select-a-beachhead-market", "profile-the-persona", "identify-key-assumptions"],
    scope={"customer": "text", "geography": "text", "target_sample": "positive_integer"},
    example_scope={"customer": "Owner-managed consultancies", "geography": "Ireland", "target_sample": 3},
    tables={
        "participants": {"participant_id": "text", "qualification": "text", "method": "choice:interview,observation,transaction", "current_behavior": "text", "finding": "text"},
        "synthesis": {"observed_sample": "nonnegative_integer", "pattern": "text", "contradiction": "text", "decision": "choice:proceed,revise,inconclusive", "sample_limitation": "text"},
    },
    example={
        "participants": [row(participant_id="P-01", qualification="Owner handles actual monthly invoices", method="interview", current_behavior="Reconciles time sheets manually", finding="Accuracy matters more than fully automatic sending")],
        "synthesis": [row(observed_sample=1, pattern="Manual reconciliation may create avoidable effort", contradiction="This participant prefers an approval step", decision="inconclusive", sample_limitation="Only one of three planned independent participants; recruit from another channel")],
    },
    note="A shortfall can produce an honest inconclusive analysis, but not a proceed decision. Set a justified sample target rather than applying a universal count.",
    failure="Recruiting contacts alone are not completed interviews. A sample below the declared target cannot produce proceed or revise as if the target were met.",
    observed_tables=["participants"],
)
define(
    "define-competitive-advantage", "Define Competitive Advantage",
    not_for="A feature list or a customer-facing positioning chart.",
    gate="Trace a durable capability to customer value; when durability is unproven, keep it a hypothesis with a test and investment plan.",
    next_skills=["chart-your-competitive-position", "develop-a-product-plan"],
    tables={
        "advantages": {"capability": "text", "customer_value": "text", "imitation_barrier": "text", "compounding_mechanism": "text", "weakness": "text"},
        "investments": {"capability": "text", "investment": "text", "metric": "text", "owner": "text", "tradeoff": "text"},
    },
    example={
        "advantages": [row(capability="Reliable mapping of consulting project records", customer_value="Fewer invoice corrections", imitation_barrier="Verified edge-case dataset, still small", compounding_mechanism="Each approved correction improves mapping tests", weakness="Competitors may gain similar data")],
        "investments": [row(capability="Reliable mapping", investment="Maintain consented, anonymized edge-case tests", metric="Correction rate per imported invoice", owner="Product lead", tradeoff="Defer unrelated integrations")],
    },
    note="Durability is a claim to test, not something a new venture can declare into existence. Include a credible imitation scenario.",
    failure="A slogan without a compounding mechanism or an investment without a measure fails the output contract.",
)
define(
    "chart-your-competitive-position", "Chart Your Competitive Position",
    not_for="Internal capability analysis or choosing axes to guarantee a favorable chart.",
    gate="Use the customer's priorities and include the current workaround. A proposed product's position can be a labeled hypothesis.",
    next_skills=["define-competitive-advantage", "define-product-concept"],
    tables={
        "axes": {"axis": "choice:x,y", "customer_priority": "text", "low_anchor": "text", "high_anchor": "text"},
        "alternatives": {"alternative": "text", "kind": "choice:product,competitor,status-quo", "x_score": "probability", "y_score": "probability", "uncertainty": "text"},
    },
    example={
        "axes": [row(axis="x", customer_priority="Invoice accuracy", low_anchor="Corrections after sending", high_anchor="Accurate before approval"), row(axis="y", customer_priority="Preparation effort", low_anchor="Retype every line", high_anchor="Review prefilled draft")],
        "alternatives": [row(alternative="Shared spreadsheet", kind="status-quo", x_score=0.6, y_score=0.2, uncertainty="Single observed workflow"), row(alternative="Proposed invoice assistant", kind="product", x_score=0.7, y_score=0.8, uncertainty="Untested hypothesis, not superiority evidence")],
    },
    note="Scores need anchored meanings and sources. The example does not establish that the proposed product wins.",
    failure="Missing x/y definitions, out-of-range scores, or omitting the status quo are rejected.",
)
define(
    "map-buying-stakeholders", "Map Buying Stakeholders",
    not_for="The sequence of purchase steps or assuming that the user controls the budget.",
    gate="Adapt to the buying context: one person may hold several roles in a simple purchase; complex purchases need separately evidenced authority and veto power.",
    next_skills=["map-customer-buying-process"],
    tables={
        "stakeholders": {"role": "text", "person_or_title": "text", "authority": "text", "success_criterion": "text", "proof_needed": "text", "objection": "text"},
        "relationships": {"from_role": "text", "to_role": "text", "influence": "text", "access_action": "text", "owner": "text"},
    },
    example={
        "stakeholders": [row(role="User and economic buyer", person_or_title="Practice owner", authority="Approves the small software budget", success_criterion="Accurate invoices with less preparation", proof_needed="Comparison against a recent invoice", objection="Will not permit automatic sending")],
        "relationships": [row(from_role="Practice owner", to_role="External accountant", influence="Accountant checks export compatibility", access_action="Request permission for a format review", owner="Founder")],
    },
    note="Do not invent extra stakeholders for a simple purchase or force household buyers into organizational titles.",
    failure="A title without buying authority or required proof is insufficient.",
)
define(
    "map-customer-buying-process", "Map the Customer Buying Process",
    not_for="The venture's marketing activities or CRM stage names.",
    gate="Ground timing in actual comparable purchases when possible; distinguish observed timing from forecast assumptions.",
    next_skills=["map-the-sales-process", "calculate-customer-acquisition-cost"],
    tables={
        "buying_stages": {"stage": "text", "customer_owner": "text", "entry_condition": "text", "exit_evidence": "text", "elapsed_days": "nonnegative", "dependency": "text"},
        "obstacles": {"obstacle": "text", "impact": "text", "mitigation": "text", "owner": "text"},
    },
    example={
        "buying_stages": [row(stage="Approve paid pilot", customer_owner="Practice owner", entry_condition="Draft invoice matches a recent approved invoice", exit_evidence="Signed paid-pilot acceptance", elapsed_days=7, dependency="Confirm accountant export format")],
        "obstacles": [row(obstacle="Export format mismatch", impact="Pilot cannot begin", mitigation="Validate one sample file before quoting the pilot", owner="Founder")],
    },
    note="A signed agreement, payment, and implementation readiness can occur at different times; represent each material delay.",
    failure="Missing customer-side owners, exit evidence, or negative elapsed times fail validation.",
)
define(
    "map-the-sales-process", "Map the Sales Process",
    not_for="The customer's internal approval process or counting leads as paying customers.",
    gate="Separate founder-led exceptions from the repeatable sales motion. Conversion rates must have a defined stage denominator.",
    next_skills=["calculate-customer-acquisition-cost", "build-financial-plan"],
    tables={
        "sales_stages": {"stage": "text", "customer_exit": "text", "seller_action": "text", "owner": "text", "channel": "text", "entered": "nonnegative_integer", "converted": "nonnegative_integer", "conversion_rate": "probability", "elapsed_days": "nonnegative", "cost": "nonnegative"},
        "bottlenecks": {"stage": "text", "hypothesis": "text", "experiment": "text", "metric": "text", "owner": "text"},
    },
    example={
        "sales_stages": [row(stage="Paid pilot proposal", customer_exit="Owner signs the proposal", seller_action="Show a comparison using consented sample data", owner="Founder", channel="Qualified referral", entered=10, converted=2, conversion_rate=0.2, elapsed_days=7, cost=600)],
        "bottlenecks": [row(stage="Paid pilot proposal", hypothesis="Setup uncertainty delays decisions", experiment="Offer a bounded export-format review", metric="Proposal-to-paid-pilot conversion", owner="Founder")],
    },
    note="Two conversions out of ten entries is 20%, not evidence of scalable channel economics. Include founder time in acquisition costing.",
    failure="Converted counts above entries, or rates that disagree with counts, are rejected.",
)
define(
    "design-a-business-model", "Design a Business Model",
    not_for="Selecting exact prices or constructing a financial forecast before identifying who pays.",
    gate="Compare coherent value and money flows; free participants need an explicit payer or funding mechanism.",
    next_skills=["set-your-pricing-framework", "plan-operations"],
    tables={
        "models": {"model": "text", "payer": "text", "value_recipient": "text", "charging_unit": "text", "payment_timing": "text", "cost_driver": "text", "incentive_risk": "text"},
        "selection": {"chosen_model": "text", "reason": "text", "rejected_alternative": "text", "critical_assumption": "text", "next_test": "text"},
    },
    example={
        "models": [row(model="Monthly subscription", payer="Practice owner", value_recipient="Owner and billing assistant", charging_unit="Practice per month", payment_timing="Monthly in advance", cost_driver="Import support and hosting", incentive_risk="Heavy users may consume disproportionate support")],
        "selection": [row(chosen_model="Monthly subscription", reason="Predictable charge matches a monthly workflow", rejected_alternative="Per-invoice commission", critical_assumption="Recurring value exceeds the subscription", next_test="Offer a bounded paid pilot without claiming prior demand")],
    },
    note="The model can be chosen provisionally before a precise price is known. Make its payment timing usable in the cash forecast.",
    failure="A selected model absent from the alternatives or an unnamed payer is incomplete.",
)
define(
    "set-your-pricing-framework", "Set Your Pricing Framework",
    not_for="Choosing the business model or treating competitor prices as willingness-to-pay evidence.",
    gate="State the value metric, package boundary, and price hypothesis. Do not invent accepted prices when only proposals exist.",
    next_skills=["test-key-assumptions", "calculate-customer-lifetime-value"],
    scope={"customer": "text", "currency": "currency", "billing_period": "choice:month,year,transaction"},
    example_scope={"customer": "Owner-managed consultancies", "currency": "EUR", "billing_period": "month"},
    tables={
        "packages": {"package": "text", "metric": "text", "price": "nonnegative", "included_value": "text", "fence": "text", "value_anchor": "text"},
        "price_tests": {"package": "text", "method": "text", "threshold": "text", "discount_rule": "text", "owner": "text"},
    },
    example={
        "packages": [row(package="Owner plan", metric="Practice per month", price=80, included_value="Draft preparation and approval", fence="One practice and one export format", value_anchor="Illustrative avoided preparation effort, not a measured saving")],
        "price_tests": [row(package="Owner plan", method="Authorized paid-pilot proposal", threshold="Two of five qualified prospects accept without permanent discount", discount_rule="Temporary pilot credit with explicit expiry", owner="Founder")],
    },
    note="A test design does not prove this price. Completed pricing analysis may contain hypotheses; observed acceptance needs its own evidence.",
    failure="A negative price, missing billing period, or discount without a boundary fails the record contract.",
)
define(
    "identify-key-assumptions", "Identify Key Assumptions",
    not_for="Turning verified facts into guesses or designing experiments before prioritizing the risk.",
    gate="Start after founder discovery, not only after a full plan exists. Rank desirability, viability, feasibility, operational, and team uncertainties.",
    next_skills=["test-key-assumptions"],
    tables={
        "assumptions": {"id": "text", "hypothesis": "text", "category": "choice:desirability,viability,feasibility,operations,team,regulatory", "impact": "positive_integer", "uncertainty": "positive_integer", "risk_score": "positive_integer", "reversal_threshold": "text"},
        "test_queue": {"assumption_id": "text", "priority": "positive_integer", "dependency": "text", "next_evidence": "text", "owner": "text"},
    },
    example={
        "assumptions": [row(id="A-001", hypothesis="Owners will pay for draft preparation while retaining approval", category="viability", impact=5, uncertainty=4, risk_score=20, reversal_threshold="No qualified prospect accepts an authorized paid pilot")],
        "test_queue": [row(assumption_id="A-001", priority=1, dependency="Founder approves outreach scope", next_evidence="Paid-pilot proposal decisions and objections", owner="Founder")],
    },
    note="Use a 1-5 impact and uncertainty scale. A score of 20 prioritizes a test; it is not a probability or proof of risk.",
    failure="Compound hypotheses, out-of-range ratings, incorrect risk multiplication, or queue references to missing assumptions fail the checks.",
)
define(
    "test-key-assumptions", "Test Key Assumptions",
    not_for="Claiming an experiment ran when only its protocol exists or changing thresholds after seeing results.",
    gate="Use research-plan mode before authorized execution. Completed analysis requires dated observations, the precommitted threshold, and an evidence-following decision.",
    next_skills=["identify-key-assumptions", "define-the-minimum-viable-business-product"],
    tables={
        "experiments": {"id": "text", "hypothesis": "text", "population": "text", "metric": "text", "sample_size": "positive_integer", "threshold": "number", "comparison": "choice:at-least,at-most", "precommitted_on": "date", "observed_on": "date"},
        "results": {"experiment_id": "text", "observed_value": "number", "outcome": "choice:pass,fail", "decision": "text", "confounds": "text"},
    },
    example={
        "experiments": [row(id="X-001", hypothesis="Qualified owners accept a bounded paid pilot", population="Five owner-managed practices", metric="Number accepting without permanent discount", sample_size=5, threshold=2, comparison="at-least", precommitted_on="2026-01-01", observed_on="2026-01-08")],
        "results": [row(experiment_id="X-001", observed_value=1, outcome="fail", decision="Revise the offer and investigate setup objections before expanding", confounds="Small referral-based synthetic sample")],
    },
    note="One acceptance misses a threshold of two. The correct output is a failed test and an evidence-led next action, not a lower threshold.",
    failure="A pass verdict that contradicts the threshold, or a precommitment dated after observations, is rejected.",
    observed_tables=["experiments", "results"],
)
define(
    "define-the-minimum-viable-business-product", "Define the Minimum Viable Business Product",
    not_for="A disconnected prototype or a long-term feature roadmap.",
    gate="Scope one complete, safe value-delivery and payment path. Proposed usage or payment is not observed traction.",
    next_skills=["validate-customer-traction", "plan-operations"],
    tables={
        "scope": {"capability": "text", "customer_value": "text", "delivery": "choice:product,manual,partner", "boundary": "text", "owner": "text"},
        "launch_gates": {"gate": "text", "metric": "text", "threshold": "text", "payment_path": "text", "stop_condition": "text"},
    },
    example={
        "scope": [row(capability="Create a reviewable invoice draft", customer_value="Avoid retyping while retaining control", delivery="manual", boundary="One approved export format; no automatic sending", owner="Founder")],
        "launch_gates": [row(gate="Bounded paid pilot", metric="Accurate drafts reviewed by the owner", threshold="Every draft reconciles to approved hours", payment_path="Explicit paid-pilot agreement before service", stop_condition="Stop if incorrect invoices could be sent")],
    },
    note="Manual work is acceptable when capacity, responsibility, and cost are explicit. A payment path is not proof that payment occurred.",
    failure="No accountable delivery owner, no payment path, or absent stop conditions makes the scope incomplete.",
)
define(
    "validate-customer-traction", "Validate Customer Traction",
    not_for="Sign-up totals, compliments, or declaring product-market fit from one cohort.",
    gate="Completed analysis needs actual usage, payment, and cohort observations. A future instrumentation plan belongs in research-plan mode.",
    next_skills=["develop-a-product-plan", "calculate-customer-lifetime-value"],
    scope={"customer": "text", "cohort_window": "text", "retention_period": "text"},
    example_scope={"customer": "Owner-managed practices", "cohort_window": "January paid-pilot entrants", "retention_period": "Second monthly billing cycle"},
    tables={
        "cohorts": {"cohort": "text", "acquired": "positive_integer", "activated": "nonnegative_integer", "paid": "nonnegative_integer", "retained": "nonnegative_integer", "retention_rate": "probability", "customer_outcome": "text"},
        "diagnosis": {"cohort": "text", "bottleneck": "text", "contradiction": "text", "decision": "choice:scale,iterate,pivot,stop", "next_test": "text"},
    },
    example={
        "cohorts": [row(cohort="January pilots", acquired=10, activated=8, paid=6, retained=4, retention_rate=0.4, customer_outcome="Four owners repeated the approved draft workflow")],
        "diagnosis": [row(cohort="January pilots", bottleneck="Second-cycle setup effort", contradiction="Some paid users did not return", decision="iterate", next_test="Observe the second-cycle import with consent")],
    },
    note="Retention here uses acquired customers as its denominator, explicitly. Do not switch to paid or activated denominators to improve the reported percentage.",
    failure="Impossible funnel counts, an incorrect retention denominator, or assumption-only traction data cannot pass.",
    observed_tables=["cohorts"],
)
define(
    "develop-a-product-plan", "Develop a Product Plan",
    not_for="A build specification or promising expansion without evidence gates.",
    gate="Sequence customer outcomes and dependencies. If consumption evidence is missing, keep expansion conditional rather than claiming readiness.",
    next_skills=["plan-operations", "build-financial-plan"],
    tables={
        "roadmap": {"initiative": "text", "horizon": "choice:now,next,later", "outcome": "text", "dependency": "text", "evidence_gate": "text", "owner": "text", "resource_limit": "text"},
        "deferred": {"opportunity": "text", "reason": "text", "revisit_trigger": "text"},
    },
    example={
        "roadmap": [row(initiative="Reduce repeat import setup", horizon="now", outcome="Owners complete the second billing cycle", dependency="Observe actual repeat workflow", evidence_gate="Second-cycle retention improves without more founder hours", owner="Product lead", resource_limit="Two weeks before another integration")],
        "deferred": [row(opportunity="Large-firm procurement integration", reason="Different buying motion and support burden", revisit_trigger="Reliable repeat use and positive contribution in the current segment")],
    },
    note="A roadmap remains useful before all hypotheses are proven if commitments are conditional and resources are bounded.",
    failure="Features with no outcome, dependency, evidence gate, or owner fail completion.",
)


for skill, title in (
    ("calculate-beachhead-market-tam", "Calculate Beachhead Market TAM"),
    ("calculate-follow-on-markets-tam", "Calculate Follow-on Markets TAM"),
):
    follow_on = skill == "calculate-follow-on-markets-tam"
    define(
        skill, title,
        not_for="A revenue forecast, valuation, or summing overlapping markets.",
        gate="Specify economic units, annual revenue per unit, exclusions, and source assumptions. Missing inputs belong in a research plan, not made-up totals.",
        next_skills=["develop-a-product-plan"] if follow_on else ["design-a-business-model"],
        scope={"customer_unit": "text", "geography": "text", "currency": "currency", "revenue_period": "choice:year"},
        example_scope={"customer_unit": "Practice", "geography": "Ireland", "currency": "EUR", "revenue_period": "year"},
        tables={
            "markets": {"scenario": SCENARIO, "market": "text", "units": "nonnegative", "annual_revenue_per_unit": "nonnegative", "annual_tam": "nonnegative", "exclusions": "text"},
            "expansion_gates" if follow_on else "triangulation": (
                {"market": "text", "transferable_capability": "text", "incremental_burden": "text", "entry_trigger": "text"}
                if follow_on else {"scenario": SCENARIO, "top_down_annual_tam": "nonnegative", "difference_explanation": "text", "next_source": "text"}
            ),
        },
        example={
            "markets": [
                row(scenario=scenario, market="Adjacent professional practices" if follow_on else "Owner-managed consultancies", units=units, annual_revenue_per_unit=960, annual_tam=units * 960, exclusions="Large firms with procurement-heavy workflows")
                for scenario, units in zip(("conservative", "base", "upside"), (100, 200, 300))
            ],
            "expansion_gates" if follow_on else "triangulation": (
                [row(market="Adjacent professional practices", transferable_capability="Approved-time import", incremental_burden="Different billing conventions", entry_trigger="Reliable retention in the current segment")]
                if follow_on else [
                    row(scenario=scenario, top_down_annual_tam=units * 1000, difference_explanation="Illustrative independent estimate uses a slightly different price assumption", next_source="Reconcile eligible-practice count against recent registry data")
                    for scenario, units in zip(("conservative", "base", "upside"), (100, 200, 300))
                ]
            ),
        },
        note="For the base case, 200 practices times EUR 960 per year gives EUR 192,000 annual TAM. This is 100% market potential, not forecast sales.",
        failure="Mixing monthly prices with annual revenue, missing scenarios, or a total that differs from units times annual revenue is rejected.",
    )

define(
    "calculate-customer-acquisition-cost", "Calculate Customer Acquisition Cost",
    not_for="Cost per lead or attributing all acquisition to the final sales call.",
    gate="Use paying-customer cohorts and fully loaded spend. With zero acquisitions, CAC is undefined: report the limitation rather than divide by zero.",
    next_skills=["calculate-customer-lifetime-value", "build-financial-plan"],
    scope={"currency": "currency", "contribution_period": "choice:month,year", "spend_window": "text", "sales_lag_periods": "nonnegative_integer"},
    example_scope={"currency": "EUR", "contribution_period": "month", "spend_window": "January acquisition cohort", "sales_lag_periods": 1},
    tables={
        "acquisition": {"scenario": SCENARIO, "cohort": "text", "acquisition_spend": "nonnegative", "new_paying_customers": "positive_integer", "cac": "nonnegative", "contribution_per_period": "positive", "simple_payback_periods": "nonnegative"},
        "cost_coverage": {"cost": "text", "treatment": "text", "allocation_basis": "text"},
    },
    example={
        "acquisition": [row(scenario=scenario, cohort="January pilots", acquisition_spend=1200, new_paying_customers=count, cac=1200 / count, contribution_per_period=40, simple_payback_periods=1200 / count / 40) for scenario, count in zip(("conservative", "base", "upside"), (2, 4, 6))],
        "cost_coverage": [row(cost="Founder outreach time and acquisition tools", treatment="Included in fully loaded spend", allocation_basis="Recorded hours and invoices attributable to this cohort")],
    },
    note="Base CAC is EUR 1,200 / 4 = EUR 300. Simple payback is 7.5 months at a constant EUR 40 monthly contribution; use a cash schedule if contribution or retention varies.",
    failure="Zero paying customers, omitted cost treatment, or inconsistent CAC/payback arithmetic fail the checks.",
)
ltv_cashflows = []
ltv_summary = []
for scenario, retained in zip(("conservative", "base", "upside"), (0.6, 0.8, 0.9)):
    total = 0.0
    for period in (1, 2):
        retention = retained ** (period - 1)
        contribution = retention * (100 * 0.8 - 10)
        discounted = contribution / 1.01 ** period
        total += discounted
        ltv_cashflows.append(row(scenario=scenario, period=period, retention=retention, revenue_per_active_customer=100, gross_margin=0.8, service_cost=10, expected_contribution=contribution, discounted_contribution=discounted))
    ltv_summary.append(row(scenario=scenario, ltv=total))
define(
    "calculate-customer-lifetime-value", "Calculate Customer Lifetime Value",
    not_for="Revenue-only lifetime value, acquisition cost, or assuming constant churn without evidence.",
    gate="Specify the cohort, horizon, period-aligned discount rate, retention, revenue, margin, and non-duplicated service costs.",
    next_skills=["calculate-customer-acquisition-cost", "build-financial-plan"],
    scope={"customer_unit": "text", "currency": "currency", "period_unit": "choice:month,year", "horizon_periods": "positive_integer", "discount_rate_per_period": "nonnegative"},
    example_scope={"customer_unit": "Acquired practice", "currency": "EUR", "period_unit": "month", "horizon_periods": 2, "discount_rate_per_period": 0.01},
    tables={
        "cashflows": {"scenario": SCENARIO, "period": "positive_integer", "retention": "probability", "revenue_per_active_customer": "nonnegative", "gross_margin": "probability", "service_cost": "nonnegative", "expected_contribution": "number", "discounted_contribution": "number"},
        "summary": {"scenario": SCENARIO, "ltv": "number"},
    },
    example={"cashflows": ltv_cashflows, "summary": ltv_summary},
    note="Expected contribution is survival probability times (active-customer revenue times gross margin minus additional service cost). Discount each period separately and sum; acquisition cost is excluded.",
    failure="Retention above one or increasing across a cohort, missing periods, double-counted service costs, or incorrect discounted totals require correction. Arithmetic checks cannot detect a misclassified cost.",
)
define(
    "quantify-the-value-proposition", "Quantify the Value Proposition",
    not_for="Vendor revenue, price selection, or monetizing every benefit without a defensible conversion.",
    gate="Choose a customer-recognized baseline, consistent unit, and credible realization factor; record disputes and unknowns.",
    next_skills=["set-your-pricing-framework", "define-product-concept"],
    scope={"customer": "text", "input_unit": "text", "value_unit": "text", "horizon": "text"},
    example_scope={"customer": "Practice owner", "input_unit": "Hours per invoice cycle", "value_unit": "EUR per year", "horizon": "12 monthly cycles"},
    tables={
        "outcomes": {"scenario": SCENARIO, "baseline": "number", "future": "number", "direction": "choice:increase,decrease", "unit_value": "nonnegative", "frequency": "nonnegative", "realization": "probability", "realized_value": "number"},
        "validation": {"baseline_source": "text", "customer_response": "text", "disputed_input": "text", "next_test": "text"},
    },
    example={
        "outcomes": [row(scenario=scenario, baseline=2, future=0.5, direction="decrease", unit_value=50, frequency=12, realization=factor, realized_value=1.5 * 50 * 12 * factor) for scenario, factor in zip(("conservative", "base", "upside"), (0.5, 0.75, 1.0))],
        "validation": [row(baseline_source="Synthetic owner walkthrough", customer_response="Owner recognizes the current workflow but future savings are untested", disputed_input="Realization depends on export quality", next_test="Time a consented pilot cycle")],
    },
    note="The base case is 1.5 hours saved times EUR 50/hour times 12 cycles times 75% realization = EUR 675/year. It is a value hypothesis, not observed savings.",
    failure="Incompatible units, a realization factor above one, or a result that disagrees with the explicit inputs fails the checks.",
)
define(
    "plan-operations", "Plan Operations",
    not_for="A feature roadmap or replacing jurisdiction-specific professional advice.",
    gate="Define delivery units, a planning period, available capacity, owners, costs, suppliers, and failure contingencies before promising service levels.",
    next_skills=["build-financial-plan", "develop-a-product-plan"],
    scope={"customer": "text", "delivery_unit": "text", "planning_period": "text", "currency": "currency"},
    example_scope={"customer": "Pilot practices", "delivery_unit": "Approved invoice batch", "planning_period": "One month", "currency": "EUR"},
    tables={
        "capacity": {"activity": "text", "demand_units": "nonnegative", "hours_per_unit": "positive", "available_hours": "nonnegative", "required_hours": "nonnegative", "gap_hours": "nonnegative", "cost_per_hour": "nonnegative", "labor_cost": "nonnegative", "owner": "text"},
        "dependencies": {"supplier_or_dependency": "text", "lead_days": "nonnegative_integer", "failure_trigger": "text", "fallback": "text", "owner": "text"},
    },
    example={
        "capacity": [row(activity="Review invoice imports", demand_units=20, hours_per_unit=0.5, available_hours=8, required_hours=10, gap_hours=2, cost_per_hour=30, labor_cost=300, owner="Operations owner")],
        "dependencies": [row(supplier_or_dependency="Accounting export access", lead_days=3, failure_trigger="Approved export cannot be obtained before the billing cycle", fallback="Reduce pilot scope; do not send unverified invoices", owner="Founder")],
    },
    note="Twenty batches at half an hour require ten hours; eight available hours leave a two-hour gap. The plan must reduce demand, add capacity, or change the promise before launch.",
    failure="Incorrect capacity or labor-cost arithmetic, unowned dependencies, or a missing fallback fails completion.",
)
cashflow = []
summaries = []
for scenario, units in zip(("conservative", "base", "upside"), (2, 5, 10)):
    opening = 1000.0
    balances = [opening]
    first_negative = 0
    for month in (1, 2, 3):
        revenue = units * 100
        cogs = units * 20
        operating = revenue - cogs - 400
        closing = opening + operating
        cashflow.append(row(scenario=scenario, month=month, opening_cash=opening, units=units, price=100, revenue=revenue, cogs=cogs, opex=400, taxes=0, change_working_capital=0, capex=0, net_financing=0, operating_cash_flow=operating, closing_cash=closing))
        if closing < 0 and not first_negative:
            first_negative = month
        balances.append(closing)
        opening = closing
    summaries.append(row(scenario=scenario, minimum_cash=min(balances), additional_funding_needed=max(0, -min(balances)), first_negative_month=first_negative))
define(
    "build-financial-plan", "Build a Financial Plan",
    not_for="Only TAM or unit economics, investment advice, or a guarantee that financing will be available.",
    gate="Tie demand and price to the business model and costs to the operations plan. State timing, working capital, taxes, capital expenditure, and financing assumptions.",
    next_skills=["identify-key-assumptions", "create-business-plan"],
    scope={"currency": "currency", "horizon_months": "positive_integer", "opening_cash": "nonnegative", "customer_unit": "text"},
    example_scope={"currency": "EUR", "horizon_months": 3, "opening_cash": 1000, "customer_unit": "Paying practice"},
    tables={
        "cashflow": {"scenario": SCENARIO, "month": "positive_integer", "opening_cash": "number", "units": "nonnegative", "price": "nonnegative", "revenue": "nonnegative", "cogs": "nonnegative", "opex": "nonnegative", "taxes": "nonnegative", "change_working_capital": "number", "capex": "nonnegative", "net_financing": "number", "operating_cash_flow": "number", "closing_cash": "number"},
        "summary": {"scenario": SCENARIO, "minimum_cash": "number", "additional_funding_needed": "nonnegative", "first_negative_month": "nonnegative_integer"},
    },
    example={"cashflow": cashflow, "summary": summaries},
    note="Revenue is units times price. Operating cash subtracts COGS, operating expenses, taxes, and increased working capital. Closing cash adds net financing and subtracts capex. first_negative_month=0 means no shortfall within the modeled horizon, not infinite runway.",
    failure="Missing months, mixed currencies, incorrect cash continuity, unsupported funding, or arithmetic inconsistencies require correction. Evidence review still checks cost classification and financing credibility.",
)
