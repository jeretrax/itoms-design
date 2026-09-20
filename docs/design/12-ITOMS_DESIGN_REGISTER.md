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

### DR-009 — Unified GRC Scoring, Applicability, and Lifecycle Boundaries

**Status:** Proposed

**Category:** GRC / Assessment / Posture / Remediation

**Domain:** Governance, Risk & Compliance

**Facet:** GRC / Security / IT / Executive / MSP Service Delivery / Customer

**Related Objects:** Framework, Requirement, Control, Control Implementation, Evidence, Assessment, Finding, Remediation, Risk, Policy, Workflow, Work Session

**Related Workflow:** Manual Assessment, Evidence Review, Gap Analysis, Remediation Planning, Verification, Reassessment, Progress Reporting

**Date Raised:** 2026-09-20

**Raised By:** Product Owner

#### Design Concern / Idea

Unified GRC Architecture establishes the canonical Framework-to-Remediation graph, manual V1 assessment states, and distinct Current, Planned, and Target Posture. The following details require deliberate approval before an affected Engineering Work Package is authorized.

#### Design Considerations

- **Posture formula:** Define treatment of Partial and Not Assessed results, weights, denominators, exclusions, rounding, confidence, stale assessments, and aggregation across scopes.
- **Applicability:** Define applicable, not applicable, inherited, alternative, compensating, shared, and customer-responsibility decisions, including approval and Evidence requirements.
- **Target baseline:** Define who can establish or change Target Posture, effective dates, target state granularity, due dates, and historical reconstruction.
- **Assessment Results:** Finalize the relationship/result schema, assessor qualification, review and approval, supersession, challenge, sampling, expiration, and reassessment rules.
- **Control mappings:** Define mapping type, coverage strength, rationale, provenance, versioning, crosswalk governance, and whether a mapping may be tenant-specific.
- **Control Domain taxonomy:** Decide the governed classification used for cross-framework scorecard rows and whether it requires promotion beyond classification metadata. It must remain distinct from ITOMS Primary Domain.
- **Control Implementation lifecycle:** Define actual, planned, inherited, shared, compensating, not implemented, and retired semantics without confusing implementation state with Assessment state.
- **Remediation lifecycle:** Define proposed, accepted, deferred, rejected, scheduled, in progress, blocked, completed, verified, ineffective, superseded, and closed behavior, including reopening and split/merge rules.
- **Effort and cost estimates:** Define units, currency, ranges, confidence, estimate basis, internal versus customer cost, recurring cost, and authorization to view or approve financial detail.
- **Finding relationship:** Define when a posture gap must create a Finding, when one Finding may span several results, and how duplicate or recurring Findings are handled.
- **Evidence sufficiency:** Define evidence freshness, coverage, sampling, integrity, validation, expiration, supersession, restricted access, and minimum metadata by evidence type.
- **Framework content:** Define licensing, source import, update, local extension, deprecation, cross-version migration, and customer-defined Framework rules.
- **Certification language:** Define when ITOMS may state readiness, conformity, compliance, attestation, or certification and what authority and Evidence each claim requires.
- **Task and Project boundary:** Finalize canonical Task and Project objects before implementation relies on durable direct references from Remediation.
- **Risk and exception interaction:** Define when a gap becomes a Risk, how risk acceptance differs from remediation deferral, and how exceptions affect Current, Planned, and Target Posture.

#### Disposition

Pending design review for the detailed boundaries above. The GRC Solutions Landscape Summary is accepted as the target experience and capability-coverage goal, while its exact taxonomy, generated catalog entries, dimensions, and visual layout remain illustrative. V1 remains manual and progress-focused. Every displayed percentage must disclose its calculation policy and scope, and Planned Posture must remain visibly projected rather than verified.

#### Incorporated Into

- `docs/design/grc-architecture.md`
- `adr/ADR-0008-unified-grc-posture-and-remediation.md`

---

### DR-008 — Control Monitoring and Email & Domain Security Open Boundaries

**Status:** Proposed

**Category:** Control Monitoring / Security Monitoring / Email & Domain Security

**Domain:** Cross-domain; Inventory & Asset Lifecycle; Operations & Work Management; Governance, Risk & Compliance

**Facet:** Security / IT / MSP Service Delivery / Customer / Executive / GRC

**Related Objects:** Internet Domain, Asset, Company, Application, Device, Observation, Finding, Attention Item, Case, Control, Policy, Evidence, Assessment, Risk, Workflow, Work Session

**Related Workflow:** Domain Enrollment, Sending Source Review, Finding Investigation, Remediation, Verification, Exception Review

**Date Raised:** 2026-09-17

**Raised By:** Product Owner

#### Design Concern / Idea

Control Monitoring and the initial Email & Domain Security vertical slice establish a canonical monitoring pipeline and promote Internet Domain `OBJ-IDN-0001` and Finding `OBJ-FND-0001`. The following boundaries need deliberate design decisions before an affected Engineering Work Package is approved.

#### Design Considerations

- **Internet Domain identity:** Define normalization, uniqueness, tenancy, public-suffix handling, registered-domain versus subdomain scope, delegated zones, internationalized names, aliases, and lifecycle.
- **Finding lifecycle:** Define creation, recurrence, deduplication, grouping, suppression, acceptance, remediation, verification, reopening, closure, and retention semantics.
- **Evaluation persistence:** Decide when Control Evaluation, State, and Condition require independent persisted identities rather than versioned records or derived state.
- **Sending Source resolution:** Define candidate, resolved, approved, unauthorized, expected, retired, and shared-source relationships without creating duplicate Companies, Applications, Devices, services, or vendors.
- **Policy inheritance:** Define baseline, severity, alert, routing, suppression, and exception inheritance and precedence across provider, tenant, organization, Internet Domain, source, Control, and engagement scopes.
- **DMARC information handling:** Define aggregate-report raw and normalized retention, forensic-report availability and necessity, classification, redaction, destruction, AI exposure, and customer-visible detail.
- **Report delegation and tenancy:** Define authorization and isolation for cross-domain report destinations, provider-operated receivers, shared providers, and multi-customer report streams.
- **Incident boundary:** Define the Case classification, lifecycle, escalation, evidence, notification, and permission rules that make a Case an Incident without prematurely creating a separate canonical object.
- **Interface terminology:** Decide final Work Mode and Data Mode labels, navigation, permission boundaries, and customer/MSP transitions in future Interface Architecture.
- **Assessment boundary:** Define how a future Lookout capability, if canonically approved, invokes assessment and continuous monitoring without duplicating Internet Domains, Findings, or Evidence.
- **DKIM discovery:** Define selector discovery, collection methods, authorization, false-negative handling, and key-rotation history.
- **Posture representation:** Define dimensions, maturity levels, grade or score formulas, enforcement-readiness criteria, attestation language, and the evidence required to support claims.
- **Control mappings:** Approve the initial canonical Controls, evaluation rules, framework mappings, and evidence intervals for email and domain security.

#### Disposition

Pending design review. The architecture records explicit boundaries and conservative placeholders; it does not invent final lifecycle, policy, scoring, interface, or provider behavior.

#### Incorporated Into

- `docs/design/control-monitoring-architecture.md`
- `docs/design/applications/email-domain-security.md`
- `adr/ADR-0007-control-monitoring-and-email-domain-security.md`

---

### DR-007 — Engineering Work Package Governance Details

**Status:** Proposed

**Category:** Design Governance / Engineering Handoff / Traceability

**Domain:** Cross-domain

**Facet:** Product / Architecture / Engineering / Quality / Security

**Related Objects:** All canonical objects affected by implementation

**Related Workflow:** Design Review, Engineering Handoff, Implementation, Validation, Design Gap Escalation

**Date Raised:** 2026-09-12

**Raised By:** Product Owner

#### Design Concern / Idea

Design-to-Implementation Governance establishes canonical authority, bounded Engineering Work Packages, bidirectional traceability, and mandatory escalation of material Design Gaps. Several operational details require deliberate approval before they become repository or engineering behavior.

#### Design Considerations

- **Identifier convention:** Decide whether Engineering Work Packages need a repository-wide permanent namespace, a repository-scoped sequence, or references supplied by the implementation work-management system.
- **Approval authority:** Define who may approve design baselines, Engineering Work Packages, revisions, deviations, and completion for product, architecture, security, data, and user-experience concerns.
- **Lifecycle and status model:** Define draft, review, approval, implementation, blocked, superseded, completed, rejected, and reopened semantics without confusing package state with product Workflow state.
- **Package size and decomposition:** Define practical boundaries for splitting work while retaining one coherent objective and complete acceptance criteria.
- **Traceability storage:** Decide which links belong in `itoms-design`, implementation repositories, issues, pull requests, build records, release records, or a future traceability service.
- **Multiple implementation repositories:** Define how one package targets several services, clients, deployment shapes, branches, or version lines without losing atomic review or compatibility expectations.
- **Design baseline selection:** Define how packages reference commits, releases, ADR status, proposed documents, and later canonical corrections.
- **Automation and generated artifacts:** Define validation rules for generated schemas, API contracts, migrations, tests, and documentation, including how drift is detected without treating generated output as design authority.
- **Emergency and defect work:** Define when an urgent security or operational correction may proceed before full design reconciliation and what retrospective evidence and approval are mandatory.
- **Deviation handling:** Define when a deviation requires package revision, a new package, a design note, or an ADR, and who may accept temporary nonconformance.
- **Implementation feedback classification:** Define the boundary among ordinary engineering detail, defect, nonconformance, optimization, and material Design Gap.

#### Disposition

Pending design review. Until resolved, use the placeholder-only template, record explicit references available in the participating repositories or tools, and escalate any uncertainty that could change product meaning or obligations.

#### Incorporated Into

- `docs/design/design-to-implementation-governance.md` establishes the governing boundaries without inventing the unresolved operating details.
- `docs/design/templates/engineering-work-package-template.md` provides placeholders only.

---

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
