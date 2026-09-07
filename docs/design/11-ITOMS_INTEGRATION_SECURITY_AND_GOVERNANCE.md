# ITOMS Integration, Security, and Governance

**Status:** Proposed

Connectors extend the customer operations graph while maintaining least privilege, source provenance, tenant isolation, and auditability.

## Integration rules

- Each connector declares its purpose, permissions, supported objects, direction, cadence, and failure behavior.
- Assessment connectors are read-only and least-privileged by default.
- Operational write capabilities use separate authorization and explicit approval boundaries.
- Vendor identifiers map to canonical objects and never replace canonical identity.
- Connector health, last successful synchronization, exceptions, and reconciliation status are visible.
- Secret material is stored outside ordinary business records and never exposed through customer views.

## Governance rules

- Authorization considers tenant, role, relationship, Facet, purpose, and sensitivity.
- Material actions produce attributable audit records.
- Policies and Controls map to frameworks without duplicating the underlying canonical objects.
- Risk acceptance records the accepting Person, scope, rationale, evidence, and review date.
- Retention, residency, export, and deletion rules are explicit for each deployment and data class.
- Security architecture and durable permission changes require ADR review.

