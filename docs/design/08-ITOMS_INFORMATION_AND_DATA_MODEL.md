# ITOMS Information and Data Model

**Status:** Proposed  
**Starter field catalog:** `/itoms_schema.csv`

ITOMS maintains a normalized, tenant-scoped operational graph with source provenance and retained history.

## Data layers

1. **Canonical metadata:** Domains, object types, relationship definitions, workflows, UI definitions, and policies.
2. **Tenant records:** Companies, people, assets, locations, identities, applications, risks, work, and related instances.
3. **Observations and evidence:** Imported facts, measurements, submissions, assertions, screenshots, documents, and logs.
4. **Derived state:** Scores, current location, attention weight, posture, recommendations, and other reproducible calculations.

## Rules

- Tenant record keys are distinct from canonical IDs.
- Every imported value retains its source, capture time, and verification state where material.
- Current-state conveniences do not replace historical event or interval records.
- Authoritative Asset ownership is explicit. Current custody, assignment, location, deployment, and external-system placement are separate temporal or source relationships and cannot be used as ownership proxies.
- Schema-driven forms store structured answers and retain rendered submissions as evidence when appropriate.
- Conflicts are reconciled explicitly; data from a new source does not silently overwrite verified truth.
- Sensitive fields are classified for internal, customer, restricted, or credential-bearing handling.
