# ADR-0002 — Context Layers and Canonical Persistence

Status: Accepted

## Decision

ITOMS maintains one Canonical Data layer. Organization Profile, Operating Model, Lens, Permissions, and Current Scope are applied to that layer to produce Effective Context for a request or session.

Context layers may change defaults, behavior, responsibility, visibility, presentation, and available capabilities. They do not create mode-specific copies of canonical records and do not change canonical identity.

Canonical Persistence is required: changing a profile, operating mode, Lens, service tier, workspace, or responsible party never deletes or recreates Canonical Data. Historical state and temporal relationships remain available subject to Permissions, lifecycle, and retention policy.

The complete definitions and resolution rules are maintained in `docs/design/context-architecture.md`.

## Consequences

- Internal IT, MSP-managed, co-managed, federated, and self-hosted arrangements operate on the same canonical records.
- A mode change is implemented through context configuration and effective-dated responsibility, not data migration to a parallel model.
- Lens and Facet behavior is separated from authorization; presentation cannot grant access or override a denial.
- Context resolution must be enforced by services and data boundaries, not solely by UI visibility.
- Derived context and caches must be reproducible from canonical records and context inputs.
- Features must identify their canonical objects, capabilities, context inputs, and archival behavior.
