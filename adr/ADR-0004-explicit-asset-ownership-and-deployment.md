# ADR-0004 — Explicit Asset Ownership and Separate Deployment

Status: Accepted

## Decision

Every Asset (`OBJ-AST-0001`) must have an explicit authoritative Owner for each effective interval or a visible ownership-reconciliation state. Ownership is modeled separately from custody, assignment, location, deployment, service purpose, management coverage, and external-system placement.

External hierarchy or placement in Datto RMM, TeamViewer, Intune, a PSA, documentation system, physical customer site, or another operational tool never establishes or changes canonical ownership.

Provider-deployed service hardware remains the appropriate Asset, Device, or Server type. Its provider ownership, customer deployment, custody, service role, management placement, and reporting classification are separate relationships or records. The Site Admin Box is the reference example.

The complete rules are maintained in `docs/design/asset-architecture.md`.

## Consequences

- Provider-owned equipment can remain visible in customer operations while being excluded from customer-owned asset, transfer, and acquisition schedules.
- Ownership transfer requires an explicit authorized and effective-dated lifecycle event.
- Connector ingestion and source-system moves cannot silently transfer ownership or create mode-specific Assets.
- Current custodian and location fields are derived conveniences, not substitutes for temporal relationships.
- Inventory and audit reports must declare inclusion rules instead of assuming site or portal membership equals ownership.
- Asset Work Functions and Work Sessions can coordinate deployment, management enrollment, maintenance, recovery, return, and ownership reconciliation without conflating those Actions.
