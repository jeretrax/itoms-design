# ITOMS Context Architecture

**Status:** Proposed

**Purpose:** Define how ITOMS presents and governs one persistent canonical operational model across different organizations, service arrangements, users, and work situations.

## Core rule

ITOMS has one Canonical Data layer. Organization Profile, Operating Model, Lens, and Permissions are context layers applied to that data. Their evaluated combination is the Effective Context for a request or session.

Context may change what is enabled, required, editable, emphasized, hidden, or named in the interface. Context does not create a separate truth and does not change the canonical identity of an object.

## Canonical Data

**Canonical Data** is the durable, tenant-scoped operational truth managed through the canonical object, relationship, workflow, and information models. It includes current and historical records, canonical identities, relationships, provenance, evidence, lifecycle state, and source mappings.

Canonical Data is independent of how the organization is classified, how IT responsibility is divided, which workspace is open, or who is viewing it. Vendor records may be mapped to Canonical Data, but a vendor identifier never replaces canonical identity.

Canonical metadata, such as Domain and Object definitions, is distinct from tenant record instances. Both retain stable identity according to their respective identity rules.

## Organization Profile

**Organization Profile** describes durable characteristics of the organization that affect defaults and applicability. Examples include organization type, size, industry, regulatory obligations, geographic scope, operational maturity, location pattern, and internal IT capacity.

The profile may:

- select recommended policies, controls, workflows, terminology, and workspace defaults;
- determine which questions, guidance, or maturity expectations are relevant;
- set default limits or configuration recommendations where commercial policy permits.

The profile does not grant access by itself and does not own Canonical Data. A profile change recalculates applicable defaults and recommendations without deleting records created under the previous profile.

## Operating Model

**Operating Model** describes how responsibility, authority, and service delivery are divided for an organization or defined scope. Supported examples include internal IT, MSP-managed, co-managed, customer-managed with advisory support, federated, and secure self-hosted operation.

An Operating Model may apply at organization level and may be narrowed by service, location, engagement, or time interval when responsibility differs. It may influence:

- available capabilities and workflows;
- default ownership, routing, approval, and escalation;
- provider and customer responsibilities;
- workspace composition and operational terminology;
- service-boundary and responsibility reporting.

Changing Operating Model changes responsibility and behavior, not canonical identity or history. Moving from internal IT to MSP-managed or co-managed operation must retain all people, assets, identities, contracts, evidence, work, relationships, and prior responsibility intervals.

## Lens

**Lens** is the presentation and task-orientation applied to Canonical Data for a user, role, or purpose. A Lens controls emphasis, navigation, fields, summaries, terminology, and available actions after Permissions are evaluated.

Examples include Executive, Finance, Human Resources, IT Operations, Security, Disaster Recovery, Inventory Control, End User, and MSP Service Delivery lenses.

A Lens:

- presents the same object differently for a particular responsibility or decision;
- may filter or summarize information without creating a duplicate object;
- may provide saved views, dashboards, guided work, and contextual navigation;
- never grants permission and never overrides a denial.

Existing design references to a **Facet** remain valid. A Facet is a reusable, named role- or use-case-oriented Lens definition. At runtime, the selected Facet contributes its Lens configuration to Effective Context. Facet and Lens are not Domains, departments, feature modules, or security roles.

## Permissions

**Permissions** determine whether an actor may discover, view, create, change, approve, export, administer, or otherwise act on data or a capability. Authorization is evaluated independently from presentation.

Permissions consider, as applicable:

- tenant and provider boundary;
- authenticated actor and delegated authority;
- role and group membership;
- relationship to the affected organization, object, engagement, or responsibility scope;
- capability and requested action;
- data classification, purpose, location, and time;
- policy conditions and explicit restrictions.

Permissions are deny-safe. A Lens can hide an allowed action for simplicity, but it cannot reveal or authorize a denied action. Operating Model and Organization Profile may supply authorization inputs or defaults, but neither is itself a permission grant.

## Effective Context

**Effective Context** is the resolved, request-scoped result of applying organization, operating, presentation, authorization, and immediate work context to Canonical Data.

Conceptually:

`Effective Context = Canonical Data + Organization Profile + Operating Model + Lens + Permissions + Current Scope`

`Current Scope` includes the active tenant, provider/customer relationship, user, workspace, engagement or workflow, selected object, location, and effective time where relevant.

Effective Context determines:

- which canonical records and relationships are discoverable;
- which capabilities and actions are available;
- which fields are visible, editable, required, or masked;
- which workflow, ownership, routing, and approval defaults apply;
- which terminology, summaries, and navigation are presented;
- which policy warnings, guidance, and recommendations are relevant.

Effective Context is computed, not persisted as a competing copy of the underlying records. Material inputs and authorization decisions should be auditable when needed to explain past visibility or action.

## Resolution rules

When context inputs disagree, ITOMS resolves them in this order:

1. Tenant isolation and explicit security restrictions.
2. Data classification, legal, regulatory, residency, and retention requirements.
3. Explicit Permissions and delegated authority.
4. Contractual scope and active Operating Model responsibility.
5. Workflow, engagement, location, and time-specific context.
6. Organization Profile defaults.
7. Lens presentation preferences.

A lower item cannot override a restriction established by a higher item. Explicit scoped configuration overrides a default at the same level. All resolutions continue to reference the same canonical records.

## Canonical Persistence

**Canonical Persistence** is the invariant that context changes never destroy operational truth.

- Changing Organization Profile, Operating Model, Lens, service tier, workspace, or responsible party never deletes or recreates Canonical Data.
- Context changes may hide data from a particular view, disable behavior, close a responsibility interval, or change future defaults. They must not erase history.
- Records that are no longer active are archived, ended, or made inactive according to lifecycle and retention policy.
- Relationships with temporal meaning retain effective dates so responsibility and state can be reconstructed.
- Re-enabling a prior mode or Lens reveals the same permitted canonical records, including retained history; it does not initialize an empty parallel dataset.
- Export, migration, federation, and self-hosted deployment preserve canonical IDs, tenant record identities, provenance, relationships, and audit history.
- Deletion occurs only through an explicit authorized lifecycle action governed by retention and evidence rules, never as a side effect of a mode or profile change.

## Architectural consequences

- Context configuration is stored separately from canonical operational records.
- UI routes and capability packages query canonical services through Effective Context rather than maintaining module-owned copies.
- Operating-model changes are represented as configuration and, where responsibility is temporal, effective-dated relationships.
- Authorization is enforced by services and data access boundaries, not solely by hidden controls in the interface.
- Derived context caches are disposable and reproducible; Canonical Data remains authoritative.
- Reports and audit records identify the context and effective time used when their interpretation depends on it.
- New features must declare the canonical objects they use, the capabilities they expose, the context inputs they honor, and their archival behavior.

## Validation questions

Before approving a context-dependent feature, verify:

1. Does it use existing canonical objects and relationships rather than create a mode-specific copy?
2. Which Organization Profile attributes affect applicability or defaults?
3. Which Operating Model responsibilities affect routing, ownership, or capability availability?
4. Which Lens presentation changes are useful, and are they separate from Permissions?
5. What is the Effective Context and resolution order for the action?
6. What remains visible or recoverable after the profile, mode, Lens, or responsible party changes?
7. Can the system explain the authorization and context used for a material historical action?
