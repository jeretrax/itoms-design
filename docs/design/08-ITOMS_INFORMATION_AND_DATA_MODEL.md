# ITOMS Information and Data Model

**Status:** Proposed  
**Starter field catalog:** `/itoms_schema.csv`

ITOMS maintains a normalized, tenant-scoped operational graph with source provenance and retained history.

## Data layers

1. **Canonical metadata:** Domains, object types, relationship definitions, workflows, UI definitions, and policies.
2. **Tenant records:** Companies, people, assets, locations, identities, applications, risks, work, and related instances.
3. **Observations and evidence:** Imported facts, measurements, submissions, assertions, screenshots, documents, and logs.
4. **Derived state:** Scores, current location, attention weight, posture, recommendations, and other reproducible calculations.

For Control Monitoring, a source-native artifact may be retained as governed Evidence; normalization produces attributable Observations; evaluation produces reproducible State or Condition; and a Finding records an evidence-backed conclusion requiring disposition. These layers must not be collapsed merely because one service processes them together.

## Rules

- Tenant record keys are distinct from canonical IDs.
- Every imported value retains its source, capture time, and verification state where material.
- Current-state conveniences do not replace historical event or interval records.
- Authoritative Asset ownership is explicit. Current custody, assignment, location, deployment, and external-system placement are separate temporal or source relationships and cannot be used as ownership proxies.
- Schema-driven forms store structured answers and retain rendered submissions as evidence when appropriate.
- Conflicts are reconciled explicitly; data from a new source does not silently overwrite verified truth.
- Sensitive fields are classified for internal, customer, restricted, or credential-bearing handling.
- Monitoring history retains the source, reporting interval, evaluation rule and version, applicable Control, threshold, exception, first and last seen times, recurrence, verification, and collection gaps when material.
- Operations, Assessments, GRC, reports, and audits reference the same governed Evidence rather than creating consumer-specific copies. Effective Context and Permissions still determine which content each consumer may access.
- Raw telemetry may be summarized or expired according to approved retention policy without erasing required historical posture, provenance, enforcement decisions, or audit evidence.

See [`control-monitoring-architecture.md`](control-monitoring-architecture.md) for the reusable evaluation boundary.

For GRC, Framework and Requirement versions, many-to-many Control mappings, scoped Control Implementations, Evidence metadata, Assessment Results, Findings, Remediations, and posture calculation policy remain separately traceable. Current Posture is based on approved assessment history. Planned Posture is a labeled projection from accepted Remediations. Target Posture is an approved desired baseline. None may overwrite the others.

`Policy.VerificationPercent` is a compatibility convenience field, not authoritative assessment history. Unified posture is derived from scoped, versioned records under [`grc-architecture.md`](grc-architecture.md).
