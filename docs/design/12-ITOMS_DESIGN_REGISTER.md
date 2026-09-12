# ITOMS Design Register

**Status:** Active  
**Purpose:** Durable inbox and history for ITOMS design ideas, concerns, requirements, unresolved details, and their disposition.

Entries are never deleted. When resolved, an entry is marked Accepted, Deferred, Rejected, Superseded, or Implemented and linked to the canonical documents, specifications, workflows, UI patterns, or ADRs that incorporated the decision.

## Status lifecycle

`Proposed → Under Review → Accepted / Deferred / Rejected → Implemented`

An accepted entry may later become `Superseded`, but its history remains.

## Design Note Template

### DR-XXX — Short Title

**Status:** Proposed  
**Category:**  
**Domain:**  
**Facet:**  
**Related Objects:**  
**Related Workflow:**  
**Date Raised:** YYYY-MM-DD  
**Raised By:**  

#### Design Concern / Idea

Describe the idea, requirement, concern, field, behavior, workflow, interface element, or other design consideration in plain language.

#### Why It Matters

Optional explanation of the business, operational, technical, or user reason behind the note.

#### Design Considerations

Record alternatives, implications, questions, constraints, or related ideas discovered during discussion.

#### Disposition

Pending.

#### Incorporated Into

List the canonical design document(s), functional specification(s), workflow(s), UI pattern(s), or implementation references that ultimately address this note.

---

## Active Design Notes

### DR-006 — Information Guard Policy and Administration Boundaries

**Status:** Proposed

**Category:** System Settings / Information Governance / AI Governance

**Domain:** Cross-domain

**Facet:** Security / Compliance / IT / MSP Service Delivery / Administration

**Related Objects:** Company, Person, Asset, Evidence, Policy, Control, Workflow, Work Session, and future configuration metadata

**Related Workflow:** Policy Definition, Exception Approval, Channel Onboarding, AI Provider Qualification, Configuration Publication

**Date Raised:** 2026-09-12

**Raised By:** Product Owner

#### Design Concern / Idea

System Settings Architecture establishes Information Guard, Channel policy, and AI Sentinel, but several boundaries require deliberate product, security, legal, and implementation decisions before they become canonical behavior.

#### Design Considerations

- **Final Channel taxonomy:** Determine whether email, web forms, APIs, imports, webhooks, browser experiences, individual collectors, and connector subflows require separate canonical Channel types or configured Channel instances.
- **Inheritance and precedence:** Define the exact resolution order across installation, provider, tenant, organization, location, Channel, capability, integration, agent, workflow, classification, purpose, and execution-environment policy. Define conflict behavior, deny precedence, explicit overrides, versioning, and effective dates.
- **Shared and derived information ownership:** Define ownership, custody, stewardship, rights, and authorized purposes when information is submitted by one party, concerns another, combines multiple sources, or is transformed or inferred by ITOMS or AI.
- **Regulated information ITOMS must retain:** Define how minimization and destruction interact with legal holds, security evidence, contractual records, regulated data, audit obligations, and information that ITOMS legitimately must preserve as canonical truth.
- **AI provider qualification:** Define provider, model, region, contract, privacy, security, retention, training-use, isolation, logging, evaluation, incident-response, and subcontractor requirements before an execution environment may be approved.
- **Provider and customer administration boundaries:** Define which System Settings a platform provider, MSP administrator, customer administrator, security officer, compliance role, or delegated operator may view, propose, approve, override, or audit.
- **Configuration user experience:** Define safe editing, inheritance visibility, effective-policy explanation, simulation, change review, staged publication, rollback, exception expiry, and warnings without embedding interface layout into the control-plane model.
- **Prohibited-value audit design:** Determine which metadata, hashes, fingerprints, counts, or category indicators are safe and useful when raw values must be destroyed.

#### Disposition

Pending design review. Until resolved, ambiguous enforcement fails closed when a broader interpretation could increase information exposure, retention, AI processing, or execution authority.

#### Incorporated Into

- `docs/design/system-settings-architecture.md` identifies the boundaries and placeholders but does not invent final behavior.

---

### DR-001 — Bind Inbound Requests and Projects to Supported Business Processes

**Status:** Proposed  
**Category:** Workflow / Functional Design  
**Domain:** Operations  
**Facet:** IT / Business Management  
**Related Objects:** Request, Ticket, Project, Business Process, Business Function  
**Related Workflow:** Request Capture / Project Intake  
**Date Raised:** 2026-09-06  
**Raised By:** Product Owner

#### Design Concern / Idea

When capturing the detail of an inbound request, ticket, or project, ITOMS should provide a way to associate that work with the supported business process or business function that the request affects.

The intent is to avoid treating incoming work as an isolated technical ticket. ITOMS should retain the business context of why the work exists and what organizational function depends upon it.

#### Why It Matters

This relationship can help ITOMS understand operational impact, prioritize work in business context, identify recurring problems affecting the same business function, and improve reporting and decision-making.

#### Design Considerations

To be determined, including:

- whether Business Process and Business Function are separate first-class objects
- whether the relationship is required or optional
- how the association is captured during intake
- whether ITOMS can suggest the relationship automatically
- whether multiple processes/functions may be associated with one request
- how the relationship appears in workflow and UI
- how this information contributes to Topics, Risks, Assessments, and QBR/TBR reporting

#### Disposition

Pending design review.

#### Incorporated Into

Not yet incorporated.

---

## Resolved / Integrated Design Notes

Move entries here only for organizational convenience. Do not delete their history.

### DR-005 — System Settings, Information Guard, Channels, and AI Sentinel

**Status:** Implemented

**Category:** Architecture / System Configuration / Information Governance

**Domain:** Cross-domain

**Facet:** All

**Related Objects:** Policy, Control, Evidence, Company, Person, Asset, Workflow, Work Session, and connector source mappings

**Related Workflow:** Configuration Management, Channel Onboarding, Information Handling, AI Invocation, Policy Exception

**Date Raised:** 2026-09-12

**Raised By:** Product Owner

#### Design Concern / Idea

ITOMS needs an installation-wide configuration and enforcement control plane that spans security, integrations, AI, automation, work, communications, agents, evidence, compliance, and platform operation without reverting to isolated modules or allowing AI and integrations to redefine canonical truth.

#### Why It Matters

Different ingestion and interaction Channels carry different information rights and handling risks. Technical access, collection, local execution, or connector authorization does not automatically permit persistence, secondary use, disclosure, or AI processing.

#### Disposition

Accepted. System Settings is the ITOMS installation control plane. Information Guard governs collection, Channel policy, classification, handling, retention, AI exposure, exceptions, and auditability. AI Sentinel governs AI processing within Information Guard. Policy is restrictive by default, and AI remains subordinate to deterministic rules and canonical ITOMS state.

#### Incorporated Into

- `docs/design/system-settings-architecture.md`
- `docs/design/02-ITOMS_DESIGN_PRINCIPLES.md`
- `docs/design/09-ITOMS_APPLICATION_ARCHITECTURE.md`
- `docs/design/11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md`
- `adr/ADR-0005-system-settings-information-guard-and-ai-sentinel.md`

### DR-004 — Explicit Asset Ownership and Provider-Deployed Hardware

**Status:** Implemented

**Category:** Architecture / Asset Management / Integration

**Domain:** Inventory & Asset Lifecycle

**Facet:** IT / Finance / Executive / Inventory Control / MSP Service Delivery

**Related Objects:** Asset (`OBJ-AST-0001`), Device (`OBJ-DEV-0001`), Server (`OBJ-SRV-0001`), Company, Person, Location, Work Session

**Related Workflow:** Asset Registration, Ownership Reconciliation, Provider Hardware Deployment, Maintenance, Recovery, Return, Ownership Transfer

**Date Raised:** 2026-09-12

**Raised By:** Product Owner

#### Design Concern / Idea

An Asset needs a true authoritative Owner even when it is deployed at another organization's site or appears inside that organization's RMM, remote-control, endpoint-management, PSA, or documentation hierarchy. Deployment custody and operational placement must not be mistaken for ownership.

#### Why It Matters

Provider-owned service equipment such as the Site Admin Box must remain visible and manageable in customer operations while being correctly excluded from customer-owned property, acquisition, transfer, and audit schedules. Inferring ownership from tool or site placement would corrupt canonical truth and historical reporting.

#### Disposition

Accepted. Ownership is explicit and effective-dated. Custody, assignment, location, deployment, service role, management coverage, and external-system placement are separate. Provider-deployed service hardware remains the appropriate Asset, Device, or Server type and uses the Site Admin Box as its reference pattern.

#### Incorporated Into

- `docs/design/asset-architecture.md`
- `docs/design/work-architecture.md`
- `docs/design/02-ITOMS_DESIGN_PRINCIPLES.md`
- `docs/design/06-ITOMS_RELATIONSHIP_MODEL.md`
- `docs/design/08-ITOMS_INFORMATION_AND_DATA_MODEL.md`
- `docs/design/11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md`
- `adr/ADR-0004-explicit-asset-ownership-and-deployment.md`

### DR-003 — Work Architecture and Persistent Work Sessions

**Status:** Implemented

**Category:** Architecture / Work Management / Experience

**Domain:** Operations

**Facet:** All

**Related Objects:** Workflow (`OBJ-WFL-0001`), Work Session (`OBJ-WSS-0001`), Case, Assessment, Topic, and proposed work objects

**Related Workflow:** All guided and ad-hoc work

**Date Raised:** 2026-09-10

**Raised By:** Product Owner

#### Design Concern / Idea

ITOMS must help people perform recurring business functions across tasks, decisions, exceptions, records, communications, documents, and external systems. Object-centric navigation and rigid automation sequences do not preserve the user's real work context.

#### Why It Matters

People need persistent, resumable continuity and useful next-action guidance while moving across many objects and systems. The system should learn repeatable patterns and offer guidance or selective automation without forcing the organization to redesign work around an inflexible engine.

#### Disposition

Accepted. ITOMS uses the hierarchy Work Function, Workflow/Process, Stage, Task, and Action. Workflow progression may branch, skip, reverse, pause, involve judgment, or leave ITOMS. Work Session is promoted as first-class object `OBJ-WSS-0001`; Workspace remains presentation. Automation is subordinate to work purpose and outcome.

#### Incorporated Into

- `docs/design/work-architecture.md`
- `docs/design/02-ITOMS_DESIGN_PRINCIPLES.md`
- `docs/design/07-ITOMS_WORKFLOW_MODEL.md`
- `docs/design/09-ITOMS_APPLICATION_ARCHITECTURE.md`
- `docs/design/10-ITOMS_EXPERIENCE_AND_UI_MODEL.md`
- `adr/ADR-0003-work-architecture-and-work-session.md`

### DR-002 — Context Layers and Canonical Persistence

**Status:** Implemented

**Category:** Architecture / Information Model / Authorization

**Domain:** Cross-domain

**Facet:** All

**Related Objects:** All canonical objects

**Related Workflow:** All context-dependent workflows

**Date Raised:** 2026-09-10

**Raised By:** Product Owner

#### Design Concern / Idea

ITOMS must support internal IT, MSP-managed, co-managed, and other operating arrangements without maintaining competing datasets or losing information when the organization changes mode. Organization characteristics, responsibility boundaries, presentation, and authorization need distinct definitions and a deterministic runtime composition.

#### Why It Matters

The platform must preserve one durable operational history while allowing different organizations and roles to experience and operate the system appropriately. A profile or mode change must never erase assets, people, identities, contracts, evidence, work, relationships, or prior responsibility.

#### Disposition

Accepted. ITOMS uses Canonical Data with Organization Profile, Operating Model, Lens, Capabilities, Permissions, and Current Scope to compute Effective Context. Capabilities identify available functions while Permissions authorize their use for an actor and scope. Canonical Persistence prohibits context changes from deleting or recreating canonical records.

#### Incorporated Into

- `docs/design/context-architecture.md`
- `docs/design/02-ITOMS_DESIGN_PRINCIPLES.md`
- `docs/design/09-ITOMS_APPLICATION_ARCHITECTURE.md`
- `docs/design/10-ITOMS_EXPERIENCE_AND_UI_MODEL.md`
- `docs/design/11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md`
- `adr/ADR-0002-context-layers-and-canonical-persistence.md`
