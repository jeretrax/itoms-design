# ADR-0010: Canonical Ontology v1 and Atlas integration

Status: Proposed

Date: 2026-10-03

## Context

IT Visualized / IT Atlas needs reusable, sourced knowledge while ITOMS preserves organization-specific truth. A parallel Atlas object schema would conflict with permanent ITOMS identities. The existing Compliance Driver Analyzer already describes Case, Source, Driver and applicability but defers their canonical boundaries.

## Proposed decision

Use the existing domain, object and field registries as the only authority for shared types. Preserve every existing ObjectID and PrimaryDomainID. Add the following proposed definitions to those registries:

- Compliance Driver `OBJ-DRV-0001`, GRC `DOM-GRC-0001`, RetainHistory.
- Guidance `OBJ-GDN-0001`, Knowledge & Evidence `DOM-KNO-0001`, Versioned.
- Objective `OBJ-OBJ-0001`, Knowledge & Evidence `DOM-KNO-0001`, Versioned.
- Implementation Option `OBJ-IOP-0001`, Knowledge & Evidence `DOM-KNO-0001`, Versioned.

Reuse Case `OBJ-CAS-0001` for Content Driver Case, Evidence `OBJ-EVD-0001` for Source, and Observation `OBJ-OBS-0001` for attributable Context Statements. Authority is a source-backed party role, not a replacement Company or Person type. Decision, applicability, adoption and exception remain versioned relationship/result records.

Keep Requirement `OBJ-REQ-0001` Framework-bound. Organization requirement is a scoped binding; an unmapped clause stays a Driver candidate until reviewed mapping. Keep Control Implementation `OBJ-CIM-0001` separate from reusable Implementation Option. Keep Findings in OPS and Evidence in KNO.

Promote selected existing and new relationship meanings to `itoms_relationships.csv` using the reserved REL namespace. This extends canonical relationship metadata without copying object definitions. Generated contract object-ID enums derive from `itoms_objects.csv` and CI rejects drift.

Atlas publishes versioned reference records. ITOMS consumes them through explicit Reference, Snapshot or ImportDerivative bindings, owns tenant state, and preserves the exact revisions used for decisions. The Compliance Driver Analyzer operates in the governed private boundary and produces reviewable proposals. Atlas cannot write assessments, certify compliance or overwrite tenant facts.

## Consequences and limits

- No existing ID, field, domain, lifecycle or meaning is removed or renamed.
- Four proposed objects and additive starter fields require review in the same canonical change.
- Snapshot and transport schemas describe bindings and messages, not a second domain schema.
- Service/work object promotion, scoring, formal applicability policy, reviewer qualifications, Atlas content licensing, enclave security and deployment remain explicit design gates.
- This ADR stays Proposed until reviewed. A draft PR is not an approval to deploy or to migrate production data.

## Sources

- [Canonical Ontology v1](../docs/design/canonical-ontology-v1.md)
- [Atlas ↔ ITOMS contract](../docs/design/atlas-itoms-schema-contract-v1.md)
- [Compliance Driver Analyzer](../docs/design/compliance-driver-analyzer.md)
- [GRC Architecture](../docs/design/grc-architecture.md)
- [Canonical rules](../ITOMS_CANONICAL_RULES.md)
- DR-011 in the [Design Register](../docs/design/12-ITOMS_DESIGN_REGISTER.md)
