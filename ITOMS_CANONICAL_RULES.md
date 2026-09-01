# ITOMS Canonical Identity and Domain Rules

## 1. Canonical identity

Every first-class ITOMS concept has a permanent `CanonicalID`. For top-level objects this is called `ObjectID`; for Domains it is `DomainID`; workflows use `WorkflowID`; UI definitions use `UIID`; architecture decisions use `ADRID`.

A canonical ID identifies the **type/concept**, not a customer record instance. For example:

- `OBJ-PER-0001` = the canonical ITOMS concept **Person**.
- A specific person record in a tenant has its own runtime `PersonID` such as a UUID/ULID.

Renaming `Person` to `Individual` in the future would not change `OBJ-PER-0001`.

## 2. Primary Domain

Every first-class object belongs to exactly one Primary Domain. Primary Domain answers: **Which architectural/business domain owns the canonical definition and lifecycle of this object?**

Store this as:

- `PrimaryDomainID` — authoritative relationship to a row in `itoms_domains.csv`.
- `DomainTag` — stable short label copied/denormalized where useful for readability and tooling.

An object may be visible through many **Facets** without changing Primary Domain. Facets are lenses such as IT, HR, Finance, Security, Executive, DR, or Inventory Control. Domain determines canonical ownership; Facet determines how the same object is viewed or used.

## 3. DomainTag

`DomainTag` is not a replacement for `DomainID`. It is a compact semantic label intended for humans and tooling, for example:

- `ORG` — Organization & People
- `INV` — Inventory & Asset Lifecycle
- `IAM` — Identity & Access
- `APP` — Applications & Services
- `GRC` — Governance, Risk & Compliance
- `OPS` — Operations & Work Management
- `KNO` — Knowledge & Evidence
- `FIN` — Financial & Commercial
- `LOC` — Location & Physical Context

Tags should be short, stable, unique, uppercase, and never repurposed. If a domain's display name changes, the existing tag should normally remain.

## 4. Internet domain naming

Do not use `PrimaryDomain` for a DNS/Internet domain. For Company records use `PrimaryInternetDomain` (for example, `contoso.com`). `PrimaryDomainID` is reserved for the ITOMS architectural domain relationship.

## 5. Relationships

Canonical metadata relationships are by ID. A relationship definition should identify both endpoint object IDs when practical:

`OBJ-AST-0001 (Asset) --located_at--> OBJ-LOC-0001 (Location)`

Runtime records then point to the tenant record identifiers of those object types.

Display names may be stored or cached for convenience but are never the referential key.

## 6. Aliases and vendor vocabulary

Aliases are allowed and encouraged. Examples:

- Person: employee, user, staff member, worker, contact person.
- Device: endpoint, workstation, node, managed device.

An alias does not create a second canonical object. Vendor-specific identifiers map to canonical objects through source mappings.

## 7. Changes and ADRs

Create an ADR when a change affects canonical identity, domain ownership, object boundaries, lifecycle semantics, or a durable repository convention. An ADR should include the affected IDs so the decision remains traceable even if labels change.

## 8. Required metadata for first-class objects

At minimum:

- `ObjectID`
- `ObjectName`
- `PrimaryDomainID`
- `DomainTag`
- `Definition`
- `Status`
- `Aliases`
- `LifecyclePolicy`

Recommended:

- `ParentObjectID` or specialization relationship where applicable
- supported facets
- owner/steward
- relationship definitions
- list/detail/new UI IDs
- workflow IDs
- schema/table/API mapping
- source-system mappings
- creation ADR and subsequent decision references
