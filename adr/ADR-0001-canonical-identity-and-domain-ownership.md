# ADR-0001 — Canonical Identity and Domain Ownership

Status: Accepted

## Decision

ITOMS first-class concepts receive permanent canonical IDs. Canonical object IDs use the `OBJ-` namespace. Every first-class object belongs to exactly one Primary Domain, represented by a permanent `DOM-` ID. A stable `DomainTag` accompanies the Domain for readability but is not the primary key.

Canonical relationships refer to concepts by ID rather than mutable names. Tenant/runtime record identifiers remain separate from canonical type IDs.

## Consequences

- Renaming an object does not break references.
- Documentation, code generation, schema, workflows, UI metadata, and AI tooling can share a stable vocabulary.
- Cross-domain views are expressed through Facets and relationships instead of changing object ownership.
- Company DNS names must use `PrimaryInternetDomain` to avoid collision with architectural Domain terminology.
