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
