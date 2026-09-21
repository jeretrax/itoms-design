# ITOMS Integration, Security, and Governance

**Status:** Proposed

Connectors extend the customer operations graph while maintaining least privilege, source provenance, tenant isolation, and auditability.

## Integration rules

- Each connector declares its purpose, permissions, supported objects, direction, cadence, and failure behavior.
- Assessment connectors are read-only and least-privileged by default.
- Operational write capabilities use separate authorization and explicit approval boundaries.
- Vendor identifiers map to canonical objects and never replace canonical identity.
- Vendor sites, groups, tenants, folders, and management placement remain source mappings. They never establish or change Asset ownership.
- Connector health, last successful synchronization, exceptions, and reconciliation status are visible.
- Secret material is stored outside ordinary business records and never exposed through customer views.
- Every ingestion or interaction path resolves to an Information Guard Channel policy. Connector authorization does not imply permission for persistence, disclosure, secondary use, or AI processing.
- Monitoring collectors declare source, cadence, scope, provenance, expected failure behavior, and entity-resolution behavior. Collector access does not make the collector authoritative for the canonical subject it observes.
- Source-native artifacts, normalized Observations, and derived evaluations remain distinguishable. Sensitive sources such as DMARC forensic or failure reports require an explicit Channel policy and must not be assumed available.
- Local Agent traffic resolves to purpose-distinct enrollment, health, telemetry, control/configuration, job, result, update, and support flows even when one transport multiplexes them. Each flow retains independent authorization, Information Guard, priority, retention, failure, and audit behavior.
- Agent messages carry or resolve tenant, workload identity, canonical Device candidate, purpose, capture or issue time, applicable contract/configuration version, and correlation metadata. Delayed delivery remains distinguishable from current state.
- Platform-to-agent jobs are capability-scoped, expiring, replay-resistant, and independently validated at the Device. Connector or platform access never implies unrestricted SYSTEM or root execution.
- Agent-to-platform delivery is idempotent or safely deduplicated where practical. Queue gaps, expiry, overflow, rejected jobs, and lost intervals remain visible rather than being interpreted as healthy state.

## Governance rules

- Authorization considers tenant, role, relationship, Operating Model, purpose, and sensitivity. Lens and Facet configuration may reduce what is presented but never grant access.
- Material actions produce attributable audit records.
- Policies and Controls map to frameworks without duplicating the underlying canonical objects.
- Risk acceptance records the accepting Person, scope, rationale, evidence, and review date.
- Retention, residency, export, and deletion rules are explicit for each deployment and data class.
- Security architecture and durable permission changes require ADR review.
- Information Guard retains auditable enforcement decisions without retaining raw values that policy requires to be destroyed.
- Broad monitoring summaries and restricted investigative Evidence use separate permission checks; a visible status or count does not reveal protected underlying content.
- Operational monitoring Evidence is referenced by GRC, Assessments, reports, and audits rather than copied into separate evidence stores.
- Imported Frameworks and Requirements retain publisher, version, source identifier, source text, effective period, and import provenance. Import must not overwrite local mapping, applicability, Assessment, or Evidence history.
- Automated or imported Evidence remains an input. It cannot silently approve an Assessment Result, certify compliance, or change Current Posture.

The reusable collector-to-posture flow is defined in [`control-monitoring-architecture.md`](control-monitoring-architecture.md).

The endpoint trust and communication contract is defined in [`local-agent-platform-architecture.md`](local-agent-platform-architecture.md).

Unified GRC governance and posture semantics are defined in [`grc-architecture.md`](grc-architecture.md).
