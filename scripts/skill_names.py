"""Stable aliases for workspaces created before the skill-name migration."""

RENAMES = {
    "show-that-the-dogs-will-eat-the-dog-food": "validate-customer-traction",
    "getting-started": "discover-venture",
    "define-your-core": "define-competitive-advantage",
    "determine-the-customer-dmu": "map-buying-stakeholders",
    "map-the-customer-acquisition-process": "map-customer-buying-process",
    "full-life-cycle-use-case": "map-customer-journey",
    "high-level-product-specification": "define-product-concept",
    "identify-your-next-10-customers": "validate-with-customers",
}


def canonical_name(name: str) -> str:
    return RENAMES.get(name, name)
