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
