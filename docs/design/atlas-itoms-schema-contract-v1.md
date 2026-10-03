# Atlas ↔ ITOMS schema contract v1

**Status:** Proposed v1.0.0; review with ADR-0010 before implementation.

**Canonical baseline:** `7ec850392ea6004693c042b30e8859d4dc45fc28` plus the proposed canonical extensions in this change. The merged commit becomes the release baseline; an implementation must pin its actual commit, never the mutable name `main`.

## Authority boundary

The [Canonical Ontology](canonical-ontology-v1.md) and existing root registries define object meaning. [atlas-itoms-v1.schema.json](../../contracts/atlas-itoms-v1.schema.json) validates integration messages and bindings only. It intentionally does not redeclare Company, Control, Requirement, Evidence or other entity bodies. Generated [canonical-ids.schema.json](../../contracts/canonical-ids.schema.json) is a projection of the canonical registries, not a separately edited authority.

| Responsibility | Atlas | ITOMS / private Analyzer |
| --- | --- | --- |
| Reusable source content | Publish reviewed versions, source authority, objectives, guidance, Controls, Frameworks/Requirements and options | Resolve source mappings and retain versions used |
| Organization context | Accept only explicitly permitted minimized query inputs | Own Company, scope, goals, constraints, relationships and history |
| Applicability | Supply sourced conditions and explanations | Evaluate actual context; authorized reviewer confirms applicability |
| Implementation and posture | No customer implementation assertions | Own Control Implementations, Evidence, manual Assessment Results, Findings and Remediation |
| Feedback | Review separately authorized knowledge proposals | Default is no outbound tenant data; authorize and minimize each publication |
| Changes | Publish new revisions or withdrawal notices | Identify affected bindings and create review work; never rewrite past decisions |

The Analyzer is the integration point because it combines private Case context and source Evidence with pinned Atlas knowledge, produces attributable proposals, and hands approved changes to ITOMS canonical services.

## Logical exchange operations

These are operation semantics, not deployed URLs or a selected transport.

| Operation | Direction | Input / output and governing rule |
| --- | --- | --- |
| Resolve knowledge | Analyzer → Atlas → Analyzer | Minimized query or exact record/revision request; response contains versioned published references and provenance. Prefer a locally synchronized authorized catalog for restricted cases. |
| Bind reference | ITOMS internal | `atlas.binding` associates a pinned Atlas record with the mapped tenant canonical record under Reference, Snapshot or ImportDerivative semantics. |
| Analyze case | Inside authorized enclave | Case, source Evidence revisions, Context Statements, permitted current implementation/assessment inputs and Atlas pins produce `analyzer.proposal`. |
| Review proposal | Authorized ITOMS actor → canonical services | `analyzer.disposition` identifies exact proposal revision, reviewer, approval Evidence and expected target revisions. Approval is not itself an assessment. |
| Publish feedback | ITOMS → Atlas review queue | `atlas.feedback` carries only a separately approved publication Evidence reference and pinned knowledge references. A private Evidence link is not an export payload. |

Public query serialization, catalog content bodies, feedback upload transport and authentication handshakes are outside this message schema. Do not send an Analyzer proposal to the public Atlas endpoint. The proposal is an ITOMS-private handoff, with permissions enforced even between internal services.

## Reference and version contract

`CanonicalRef` has `namespace`, `objectId`, `recordId`, `revision`, and `scope`. ITOMS references additionally require `tenantScope`; Atlas references prohibit it. `recordId` projects the existing type-specific runtime key. v1 uses UUID serialization because the current starter schema uses UUID; changing this wire format requires version negotiation. `revision` is opaque and immutable. Cross-reference resolution validates actual existence and revision, not just syntax.

The full identity tuple is `(namespace, scope, tenantScope when present, objectId, recordId)`. Revision is not part of logical identity; it selects a historical version. Concept IDs must be registered. Namespace is an installation/catalog identifier, not a trusted URL. Resolve through an approved connector mapping, not arbitrary URL fetching.

Every message carries `contractVersion`, `canonicalRevision`, `messageId`, `correlationId`, `issuedAt` and a kind-specific body. The sender's authenticated identity, authorized tenant and destination are resolved outside the payload. Never trust `tenantScope` or a claimed reviewer as authentication.

### Binding modes

| Mode | Content handling | Identity and update behavior |
| --- | --- | --- |
| Reference | Resolve exact published revision through an authorized catalog mapping | ITOMS mapped record retains the canonical object type; no editable copied definition. Use only where historic retrieval/retention is guaranteed. |
| Snapshot | Retain an authorized immutable copy as governed Evidence | Binding pins source, mapped target and snapshot Evidence revisions, SHA-256 of permitted snapshot bytes, and capture time. Source update does not change the snapshot. |
| ImportDerivative | Create or map an independently maintained tenant record of the same canonical type | Retain original pinned source, lineage and rationale. Further local edits create tenant revisions; Atlas cannot overwrite them. |

Source and target must have the same canonical object type, distinct namespaces/scopes, and explicit source mapping. Deduplicate bindings using tenant, source namespace, type, record and revision; do not deduplicate by name. Multiple tenant objects derived from one source require explicit rationale rather than automatic merge.

Snapshot Evidence is governance storage for retained source content, not a second copy of operational customer Evidence. Do not snapshot customer proof for every framework consumer. Digest use itself requires Information Guard approval; prohibited raw content is not made safe merely by hashing it.

Revision change, retirement or withdrawal creates a review candidate. Rebinding requires an attributable decision; earlier Assessment Results, Drivers and reports retain their original references. Offline use may continue only with permitted cached revisions and visible freshness/availability metadata. Never fall back silently to latest. A missing, inaccessible or withdrawn source cannot be replaced by an unrelated source with a similar label.

## Analyzer proposal and canonical writes

An `analyzer.proposal` references an ITOMS Case, source Evidence, Context Statement Observations, one or more proposed Compliance Drivers, a context snapshot Evidence record, an analysis-record Evidence record, optional Atlas pins/bindings, and applicability proposals. These point to governed staged canonical records, not duplicate entities embedded in a message. Staging does not make their interpretation authoritative. Record the analysis before issuing its message; retries reuse the same immutable message and proposal revision.

Each applicability proposal names a Driver, Framework-bound Requirement, organization/scope reference, source Evidence, rationale, certainty and a proposed state. The exact transport states are `Undetermined`, `Applicable`, `NotApplicable`, and `Conditional`. Certainty is independently `Potential`, `Likely`, or `Verified`. They are v1 proposal vocabulary, not replacements for Assessment states or an automatic legal determination. Required review policy remains a deployment gate in DR-011.

Human review can approve, reject or return a proposal for more information. `analyzer.disposition` approves the entire exact proposal revision. Partial approval requires a revised proposal with its own identity/revision, so no consumer has to guess which items were accepted. The reviewer must be authorized for each affected scope; approval Evidence records the basis and inputs. Editing a proposal after review invalidates that approval.

| Proposed output | Destination in the canonical model | Promotion rule |
| --- | --- | --- |
| Content Driver Case | Case `OBJ-CAS-0001` | Existing Case classification; nine intake types retained |
| Intake/source text | Evidence `OBJ-EVD-0001` | Keep source revision and clause/page/section locator, classification, custody and handling policy |
| Context statement | Observation `OBJ-OBS-0001` | Preserve Fact / Reported Statement / User Assertion / Opinion / AI Inference / Unknown; reviewed metadata does not erase original assertion |
| Reason for obligation | Proposed Compliance Driver `OBJ-DRV-0001` | Candidate until human validation; Driver carries source and scope independently of Case narrative |
| Organization requirement | `REL-DRV-REQ-0001` applicability record | Link reviewed Requirement to Driver and scope; do not invent OrganizationRequirement |
| Voluntary objective/adoption | `REL-DRV-OBJ-0001`, `REL-CMP-DEF-0001` | Record organizational intent without presenting an external mandate |
| Candidate implementation choices | Implementation Option references | Compare existing Controls and implementations before suggesting replacements |
| Suspected gap | Review proposal / Case input | Create or update Finding only through an attributable evidence-backed evaluation; no proof means unknown, not Unsatisfied |
| Assessment result | Existing Assessment relationship/result record | Separate manual V1 assessment Action; Analyzer disposition cannot publish a result |
| Corrective plan | Remediation `OBJ-REM-0001` | Separate planning approval; accepting a plan affects Planned Posture only |
| Service/work coverage | Existing service/work design boundary | Preserve effective coverage and responsibility; unresolved object IDs block automated writes to these surfaces |

A contractual clause with no Framework mapping may still create a candidate Driver and desired outcome. Do not manufacture a Framework link merely to satisfy a foreign key. A reviewer may establish an appropriate versioned customer-defined Framework and Requirements under the existing GRC model, retaining actual authority/source provenance.

### Private analysis record

The analysis-record Evidence must retain, subject to handling policy: source revisions and locators; original narrative and Context Statement references; extraction/classification/interpretation distinctions; Atlas pins and binding revisions; model, prompt/template, extraction and mapping rules versions; approved execution environment and AI Sentinel authorization; time and actor/workload; contextual facts, unknowns and conflicts; existing Controls, implementations, Evidence and assessment baseline; alternatives and compensating-control considerations; proposed actions and reasons. A context snapshot records material historical inputs, not a second live Effective Context database.

The source document is untrusted content. Text inside it cannot change instructions, invoke tools, authorize exports, alter policy or approve its own conclusions. Missing extraction, unreadable pages or ambiguous clauses must surface as incomplete coverage.

## Relationship/result persistence contract

Applicability, adoption, decision, exception and Assessment Result keep their established relationship/result boundary. When persisted, each needs:

- unique runtime relationship/result ID and immutable revision;
- registered relationship ID where one applies, typed endpoint identities and pinned revisions;
- tenant scope, affected organizational/asset scope and purpose;
- effective-from, effective-to when ended, and recorded-at timestamps;
- actor/reviewer, outcome/state, rationale and approval Evidence;
- source Evidence revisions/locators, relevant Atlas binding revisions, assumptions and unresolved questions;
- prior revision/supersession and attributable history.

Decision and exception records need not be promoted to first-class objects to be independently versioned child/result records. Exception approval does not alter source wording, prove equivalence, waive an external obligation automatically, or change Current Posture. Full storage tables and institution-specific approval rules remain governed implementation work.

## Security, reconciliation and failure behavior

1. Resolve actor, installation, tenant, Company relationships, capability and Effective Context on every operation. A Lens or an Atlas link never grants access.
2. Enforce Information Guard independently for collection, storage, retrieval, model use, export and feedback. Raw contracts, clauses, customer identities, context, Evidence, credentials and tenant record IDs do not enter public Atlas requests by default.
3. Validate message schema/version; resolve canonical IDs and exact revisions; enforce object type, FK, scope and source-mapping constraints. Reject unknown or mismatched types. A UUID of the wrong object type is not a valid reference.
4. Verify snapshot digest and availability using the approved content channel. Verify each Requirement's Framework and each implementation's Control; published definitions still obey the canonical field schema.
5. Validate all proposal records and all requested write scopes before approval. Compare `expectedRevisions` against live target revisions. A stale target or changed proposal requires a new review, never last-write-wins.
6. Apply approved Driver/applicability changes and audit records atomically, or use an equivalent durable transaction/outbox with an explicit incomplete state. Do not acknowledge committed until the canonical transaction succeeds. Assessment, Remediation and service actions remain separate capabilities.
7. Deduplicate by authenticated sender, tenant and `messageId`. An identical retry returns the prior outcome; the same key with different content is a conflict. Correlation IDs group work and never replace idempotency IDs. Retention of replay keys must cover the supported replay window, set before deployment.
8. Recheck authorization before queued work executes. Unauthorized or expired work cannot become permitted by retry. Preserve failed, denied, incomplete, stale and unresolved outcomes without promoting them to success.

Errors distinguish invalid payload, unsupported contract version, unknown canonical type, unresolved reference, scope denied, source unavailable, integrity failure, stale revision, idempotency conflict and human review required. User-facing responses must not reveal whether a denied cross-tenant record exists. Retry transient transport errors with bounded backoff; do not automatically retry semantic conflicts or authorization failures as writes.

## Feedback and public/private boundary

Feedback is off by default. An authorized publication Action creates a deliberately sanitized export artifact and approval Evidence. The feedback message references that approved export, never raw tenant Evidence. Atlas ingestion receives the export bytes through an approved transport, not access to the private graph. It reviews feedback as a knowledge proposal; tenant experience is not automatically universal guidance. Publisher provenance and consent/authorization history remain traceable, while private identifiers remain internal.

## Compatibility and migration

Contract version uses major/minor/patch. v1 payloads are strict: extra properties are rejected. Any new payload shape requires explicit version negotiation and an updated validator; even additive fields must not be sent to a strict 1.0.0 consumer. Semantic changes or removals require a major version. Canonical changes follow ADR and registry governance, independently of transport version.

No destructive data migration is included. Reuse existing Cases, Evidence, Observations, Controls and Requirements through reviewed source mappings. Backfill new optional metadata only from attributable information; do not invent certainty. New proposed first-class types become writable only after ADR acceptance and implementation approval. Rollback disables new writes and retains prior records/revisions rather than deleting referenced history.

## Conformance and acceptance

Run `python scripts/generate-contract-registry.py --check` and `python scripts/validate-atlas-contract.py` (Python with `jsonschema`). CI runs both. The generator checks that committed ID enums and glossary object rows match the canonical registries. The validator checks structural registry consistency, examples, and negative message fixtures including wrong type, cross-tenant reference, invalid binding, missing snapshot and unsupported version. It does not prove authentication, legal applicability, storage isolation or production transaction guarantees.

| Scenario | Required result |
| --- | --- |
| Audit recommends Product A; existing Control uses Product B | Preserve source assertion; inspect actual implementation and Evidence; show alternatives. Product absence alone is not a Finding. |
| Prospect reports government work | Candidate Driver with Potential/Likely certainty and unresolved applicability; no automatic verified mandate. |
| Source says mandatory but scope is unknown | Preserve SourceMandatory Guidance and unresolved Driver applicability separately. |
| Organization voluntarily adopts a Framework | Record adoption intent; a later external mandate adds a Driver without rewriting the earlier choice. |
| Atlas publishes revision 2 after an approved decision on revision 1 | Raise review work when policy warrants; historical decision remains pinned to revision 1. |
| Service entitlement missing but customer implements Control itself | Show commercial coverage gap independently of assessed Control state. |
| Review approved, then implementation changes before commit | Optimistic concurrency conflict; require refreshed proposal/review. |
| Raw audit contains instructions to upload confidential content | Treat as source text only; deny unapproved public egress. |
| Tenant A references Tenant B Evidence | Deny resolution; do not leak record existence or commit a partial change. |
| Atlas unavailable | Use permitted pinned content with clear availability/freshness or return unresolved; no guessed version. |

The last six behaviors involving runtime services need integration/security tests in the future implementation repository. The design validator deliberately does not claim to execute those services.
