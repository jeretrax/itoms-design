# Canonical Ontology v1: IT Visualized, IT Atlas, and ITOMS

**Status:** Proposed v1.0.0, for review under ADR-0010. Not an implementation approval.

**Reviewed baseline:** `jeretrax/itoms-design` commit `7ec850392ea6004693c042b30e8859d4dc45fc28` (2026-10-01). Prepared 2026-10-03.

## Authority and purpose

This ontology is an extension and interpretation of the existing ITOMS canonical model. The authoritative object definitions remain in [itoms_objects.csv](../../itoms_objects.csv), fields in [itoms_schema.csv](../../itoms_schema.csv), and domains in [itoms_domains.csv](../../itoms_domains.csv). The new [relationship registry](../../itoms_relationships.csv) promotes selected relationships into the already reserved `REL-` namespace. There is no Atlas-owned replacement for those registries.

IT Visualized is the body of knowledge. IT Atlas is its navigable, source-aware map. ITOMS holds an organization's operational position, context, decisions, implementation, evidence, and history. A human or AI-assisted vCIO can navigate these records; neither a navigator nor a Lens owns a separate truth.

The distinction is between reusable definitions and contextual records, not between two incompatible meanings of Control or Requirement. Atlas is authoritative for the content revisions it publishes. ITOMS is authoritative for tenant state and local derivatives. Architectural Primary Domain remains the owner of each concept's meaning in this repository; it is independent of which product publishes a record.

## Baseline review and reconciliation

The review covered the mandatory read order in [REPO_START_HERE.md](../../REPO_START_HERE.md), canonical rules, the object/domain/field registries and glossary, Context, Work, Asset, System Settings, Local Agent, Monitoring and GRC architectures, the relationship/data/security models, the Compliance Driver Analyzer, and the design register.

| Existing constraint or gap | v1 disposition |
| --- | --- |
| There are 27 registered object types at the reviewed baseline. | Preserve all 27 IDs, definitions, domains, fields and lifecycle policies. Add four proposed types in those same registries. |
| Requirement requires `FrameworkID`; it is not a free-standing organization obligation. | Organization requirement is a scoped applicability/adoption relationship to a Requirement. An unmapped contract clause remains Driver source text until a reviewed Framework/Requirement mapping exists. |
| Content Driver Case is described but lacks a distinct registered ID. | Use Case `OBJ-CAS-0001` with a Content Driver classification and the nine intake types already described. Do not mint a second Case object. |
| Source Document and Case Context Statement boundaries were open. | Source uses Evidence `OBJ-EVD-0001`; attributable Context Statement uses Observation `OBJ-OBS-0001` plus statement classification and validation metadata. An assertion is not automatically a fact. |
| Compliance Driver has independent provenance, scope, review, and history but no registered type. | Propose Compliance Driver `OBJ-DRV-0001` in the existing GRC domain. |
| Guidance, Objective, and reusable implementation options have no registered equivalent. | Propose Guidance `OBJ-GDN-0001`, Objective `OBJ-OBJ-0001`, and Implementation Option `OBJ-IOP-0001` in the existing Knowledge & Evidence domain. |
| Decision, adoption, applicability, exception and Assessment Result are not registered standalone types. | Preserve them as attributable relationship/result records. Use canonical endpoints, record identity, revision, effective time, actor and Evidence; no invented object IDs. |
| Service Capability, Entitlement, Package, Task and Project boundaries remain open. | Keep service/work integration behind the existing design gaps. Subscription is not silently renamed to Service Capability. |
| Glossary's object table omitted four objects already in the CSV. | Regenerate that table from the object registry; preserve the surrounding explanatory glossary. |

The proposed additions are reviewable design, not a claim that pending decisions were previously accepted. [ADR-0010](../../adr/ADR-0010-canonical-ontology-and-atlas-contract.md) records the exact extension boundary. DR-011 records remaining implementation gates.

## Shared vocabulary and ownership

| Concept | Canonical interpretation | Atlas content / ITOMS responsibility |
| --- | --- | --- |
| Company, Person, Contact | `OBJ-CMP-0001`, `OBJ-PER-0001`, `OBJ-CON-0001` | Atlas may identify public publishers using Company and public authors using Person. ITOMS customer/provider/employee records remain private and separately scoped. A shared name is not a match. |
| Location | `OBJ-LOC-0001` | ITOMS operational scope; Atlas applicability may describe geography without creating customer Locations. |
| Asset, Device, Server, Internet Domain | `OBJ-AST-0001`, `OBJ-DEV-0001`, `OBJ-SRV-0001`, `OBJ-IDN-0001` | ITOMS instances, ownership and history. Atlas describes patterns/options without manufacturing inventory. |
| Application, Subscription, Security Group | `OBJ-APP-0001`, `OBJ-SUB-0001`, `OBJ-SGR-0001` | ITOMS use, entitlements and access records. A vendor offering in Atlas is explanatory option content, not proof of subscription or deployment. |
| Framework | `OBJ-FWK-0001` | Atlas publishes source/version metadata; ITOMS resolves a source mapping, pinned snapshot, or explicitly local Framework. |
| Requirement | `OBJ-REQ-0001` | Always belongs to a versioned Framework. Customer-defined frameworks are permitted by existing GRC design, but a contractual clause must not be disguised as a requirement issued by a different authority. |
| Control / Practice | `OBJ-CTL-0001` | Reusable safeguard, mapped many-to-many to Requirements. Atlas publication and ITOMS use retain that same meaning. |
| Policy | `OBJ-POL-0001` | Atlas may publish reference statements/templates; ITOMS adoption creates or binds the organization's versioned Policy with explicit lineage. Template presence is not adoption. |
| Control Implementation | `OBJ-CIM-0001` | ITOMS scoped realization of a Control. Atlas contains options, never a claim that a customer implemented them. |
| Evidence / Source | `OBJ-EVD-0001` | Atlas public provenance and ITOMS private artifacts use one concept with separate namespaces and permissions. Public source text and customer proof have different roles. |
| Observation / Context Statement | `OBJ-OBS-0001` | Attributable source assertion or observation. Fact, Reported Statement, User Assertion, Opinion / Concern, AI Inference and Unknown remain distinguishable. |
| Assessment / Finding / Remediation | `OBJ-ASM-0001`, `OBJ-FND-0001`, `OBJ-REM-0001` | ITOMS evaluation, conclusion, and plan. Atlas route suggestions do not instantiate approved results. Finding stays in OPS and Evidence stays in KNO. |
| Risk / Residual Risk | `OBJ-RSK-0001` | Tenant exposure and remaining exposure after a stated treatment. Residual risk is contextual evaluated state of a Risk, not a second object. Atlas risk explanations are Guidance, not customer Risk entries. |
| Case / Topic | `OBJ-CAS-0001`, `OBJ-TOP-0001` | ITOMS investigation and continuing subject. Content Driver Case is a Case classification. |
| Workflow / Procedure / Work Session | `OBJ-WFL-0001`, `OBJ-WSS-0001` | Executable or guided process definitions use Workflow. Narrative procedural knowledge can be Guidance linked to a Workflow; procedure is not automatically a new object. Work Session belongs to ITOMS. |
| Attention / Alert | `OBJ-ATT-0001` | Existing attention concept. A changed Atlas reference may warrant attention under ITOMS policy, not an automatic incident. |
| Authority | Role of Company or Person where resolved | Preserve Framework.Authority text for compatibility; source-backed authority relationships are explicit. An unresolved issuer remains unresolved, not a fabricated Company. Authority is not a new party type. |
| Guidance | Proposed `OBJ-GDN-0001` | Sourced claim, recommendation, interpretation, procedure or risk explanation with basis, strength, applicability conditions, alternatives and conflicts. |
| Objective | Proposed `OBJ-OBJ-0001` | Reusable desired outcome with success criteria. ITOMS goal/target is a scoped adoption and desired-state decision, not a mutation of the Atlas Objective. |
| Implementation Option | Proposed `OBJ-IOP-0001` | Reusable approach to realizing Controls, with assumptions, dependencies, cost/disruption ranges and limitations. A selected option does not prove implementation. |
| Compliance Driver | Proposed `OBJ-DRV-0001` | Organization-scoped reason to investigate or adopt obligations, with Case, source, scope, basis and review history. Atlas offers reusable guidance about potential drivers; the actual Driver belongs to ITOMS. |
| Applicability / Adoption / Decision / Exception | Versioned relationship/result records | ITOMS stores who decided what, why, for which scope/period, using which content versions and Evidence. No parallel OrganizationRequirement or AtlasDecision object. |
| Outcome / Lens / Route | Result, presentation configuration, derived comparison | Work Outcome remains the existing result concept. Lens weights change emphasis or route ranking, never authority, facts, applicability approval or access. |

## Definition, instance and identifier layers

1. **Canonical concept ID:** e.g. `OBJ-CTL-0001`. Permanent metadata identity, shared by both products.
2. **Published record identity:** Atlas namespace plus a runtime UUID, canonical object type and immutable revision. A particular safeguard is a Control record, not a new `OBJ-*` type.
3. **Tenant record identity:** ITOMS installation namespace, tenant security scope and runtime UUID. Existing fields such as `ControlID` and `CompanyID` retain their meanings.
4. **Source mapping / binding:** Connects a published record revision with an existing or newly authorized ITOMS record. Matching is explicit; labels and vendors' identifiers never replace canonical identity.

Wire `recordId` is a transport projection of the existing type-specific runtime key. It does not add a new primary key column. Wire `tenantScope` is an opaque security boundary resolved by the installation, not a new Tenant object and not implicitly CompanyID. A provider may serve multiple Company records and customer scopes without obtaining authority over all of them.

Atlas content is separately published shared reference data. The existing ITOMS canonical metadata, tenant records, evidence/observations, and derived-state layers remain intact. Import/snapshot mappings permit consumption of shared references without turning Atlas into a tenant record store.

## Relationships and reasoning

The selected typed relationships are registered in [itoms_relationships.csv](../../itoms_relationships.csv). That file is an additive canonical relationship registry, not a second object or field registry. Existing representative relationships outside the Atlas boundary remain valid; v1 does not claim to inventory every operational edge.

All runtime edges identify the registered relationship type and typed endpoint records. Where an endpoint set is polymorphic, `*` means any registered object type, never an unknown type. Relationship instances retain independent runtime identity, version, source Evidence, rationale, actor, effective interval, recorded time, and supersession as applicable. Cardinality describes the active conceptual association, not how many historical revisions may be retained.

The explanatory reasoning path is:

`Authority → Guidance → Objective → Risk explanation → Control → Implementation Option`

The operational path adds:

`Case + Evidence + Context → Compliance Driver → Applicability → Requirement ↔ Control → Control Implementation → Evidence → Assessment → Finding → Remediation → Reassessment`

These are traceability paths, not mandatory one-to-one links or a rigid workflow. A Guidance item can disagree with another. An Option may be an alternative or proposed compensating approach. Neither edge means equivalent coverage. Coverage requires mapping rationale, source, scope, version and qualified review. An accepted risk or commercial entitlement does not satisfy a Requirement.

## Knowledge semantics

Guidance separates its content kind from normative strength. A quoted source's mandatory wording is not proof that it binds every organization. Each material recommendation carries authority/source, publication and retrieval time, objective, conditions of applicability, addressed risk explanation, strength of the claim, alternatives, conflicts, assumptions, limitations, and review status.

Cost and disruption are estimates with units, currency where monetary, range, period, basis and date. Unknown is represented explicitly, never as zero cost or zero risk. Competing advice is retained with contextual disagreement and provenance rather than collapsed into an unexplained universal score.

Candidate routes combine permitted context, goals, constraints, Lens weights, current position and pinned guidance relationships. The compared inputs, weights/rules and option versions must be retained when a route contributes to a material decision. Route ranking is advisory; Atlas neutrality requires distinguishing source obligations from vendor preferences or package sales.

## Temporal and lifecycle rules

Published versions and relied-on bindings are immutable. A correction publishes a new revision and a supersession relationship. Archived, withdrawn or superseded content remains resolvable for authorized historical purposes. Legal retention/deletion constraints still apply; when content cannot be retained, record the lawful disposition and make incomplete reconstruction explicit.

Effective time describes when a claim, mapping, obligation or decision applies. Recorded time describes when the system learned or stored it. Do not backdate knowledge or silently replace a decision's original inputs with today's Atlas. Existing organizational implementations and decisions retain history after a source update, customer conversion, service-package change, Lens change or Operating Model change.

## v1 completion boundary

This package establishes vocabulary, canonical extensions, relationship semantics, versioned reference/binding and Analyzer handoff contracts, review gates, and conformance checks. It does not build a public Atlas application, an operational API, a compliance scoring formula, a legal applicability engine, service entitlement schema, or production enclave. Those require bounded Engineering Work Packages and the unresolved decisions in DR-011 and DR-009.

See the [Atlas ↔ ITOMS schema contract](atlas-itoms-schema-contract-v1.md) for executable contract artifacts, transaction behavior, examples, and acceptance scenarios.
