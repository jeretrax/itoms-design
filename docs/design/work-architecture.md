# ITOMS Work Architecture

**Status:** Proposed

**Purpose:** Define how ITOMS helps people perform, continue, coordinate, and improve real business work without forcing that work into a rigid automation sequence.

## Core principle

ITOMS is organized to help a person accomplish a meaningful body of work, not merely open objects or invoke isolated shortcuts.

Real work, especially in small and midsize organizations, crosses records, people, customers, assets, documents, communications, decisions, and external systems. It may branch, skip optional steps, pause, move backward, require judgment, encounter exceptions, or temporarily leave ITOMS. Work Architecture must preserve that continuity while allowing guidance and selective automation.

**Navigation should be capable of following the work rather than always following the object.**

## Architectural hierarchy

`Work Function → Workflow / Process → Stage → Task → Action`

The hierarchy expresses increasing specificity. It is a composition model, not a requirement that every activity use all five levels or follow one linear path.

### Work Function

A **Work Function** is a meaningful, recurring business responsibility or activity that produces an operational result. It is larger than an individual Task and explains why the work is being performed.

Examples include receiving customer payments, onboarding an employee, setting up a contract, onboarding a customer, conducting an Assessment, processing a purchasing request, and preparing a due-diligence response.

A Work Function may have several accepted ways of being performed. It may be supported by one or more Workflows, performed ad hoc, or coordinated across several systems. Work Function does not mean department, software module, job title, or permission boundary.

The relationship between Work Function and the existing proposed Business Function concept remains subject to canonical terminology review. This document establishes the architectural meaning without prematurely creating a duplicate first-class object.

### Workflow / Process

A **Workflow**, also called a **Process** in business-facing language, is a repeatable sequence or pattern through which a Work Function can be performed. The existing canonical Workflow concept is `OBJ-WFL-0001`; Process remains an alias unless a later decision establishes a distinct boundary.

A Workflow can define states, Stages, Tasks, Actions, roles, inputs, decisions, branches, approvals, exceptions, evidence, and outcomes. It is a navigable graph of possible progression, not necessarily a fixed list.

A Workflow may:

- branch according to circumstances or judgment;
- skip optional or inapplicable work;
- revisit an earlier Stage or Task;
- execute Tasks in parallel or in no prescribed order;
- pause while waiting for a person, vendor, event, or external system;
- include work completed outside ITOMS;
- recommend rather than require the next step;
- combine manual, assisted, and automated Actions.

### Stage

A **Stage** is a meaningful portion of a Workflow that groups related work around an intermediate purpose, condition, or milestone. A Stage may contain Tasks, decisions, gates, entry or exit conditions, and Exceptions.

Stages help people understand progress without implying that every Task inside a Stage is mandatory or sequential. A Workflow may move between Stages nonlinearly when its rules permit.

### Task

A **Task** is a unit of work a person or automation needs to accomplish. It should have a recognizable purpose and completion condition and may require one or more Actions.

A Task can be assigned, accepted, delegated, handed off, deferred, blocked, skipped when permitted, or completed outside ITOMS with an attributable result. Task is not synonymous with Case, Project, Assessment, or other business object.

Whether Task requires promotion to its own canonical first-class object is deferred until its identity, lifecycle, and relationship requirements are specified.

### Action

An **Action** is the atomic operation performed within ITOMS or another system. Examples include creating a record, updating a field, generating a PDF, sending an email, adding an inventory item, saving a document, requesting approval, or recording an external completion.

An Action may be manual, guided, confirmed, delegated to an integration, or automated. Capabilities describe which Actions ITOMS can perform; Permissions determine whether the actor may perform them in the Effective Context. Actions should produce attributable audit or evidence records when material.

## Work Session

**Work Session** (`OBJ-WSS-0001`) is a first-class, tenant-scoped record representing a person's current or resumable period of activity within a Work Function.

A Work Session preserves continuity while the person moves across records, objects, customers, assets, documents, Tasks, and applications. It is distinct from an authentication session, browser session, workspace layout, Workflow definition, or individual Task.

A Work Session may retain or derive:

- the Person and Effective Context under which work is occurring;
- the current Work Function and applicable Workflow or ad-hoc pattern;
- previous, current, and next work items;
- completed and remaining items;
- Exceptions, blockers, and waiting conditions;
- recent Actions and material decisions;
- linked Cases, Projects, Assessments, Topics, assets, companies, documents, and other canonical records;
- the Suggested Next Action and why it was suggested;
- start, pause, resume, handoff, completion, abandonment, and archival history.

For example, in a **Receive Payments** Work Session, the company-wide payment activity remains primary. Moving from one customer payment to another does not force the person back into customer-centric navigation or discard the payment-receipt context.

Work Session state is canonical operational data and follows Canonical Persistence. Closing a browser, changing Lens, switching interface mode, or leaving a Workspace must not silently destroy a resumable session or its material history.

## Workspace

A **Workspace** is the interface assembled for a person performing work. It presents the permitted records, guidance, tools, and Actions relevant to the current Work Function and Work Session.

Workspace is not Work Session. The Work Session is persistent operational context; the Workspace is a presentation generated from that context. A person may reopen the same Work Session in a differently composed Workspace, and two people may receive different Workspaces for related work.

Conceptually:

`Canonical Data → Context Architecture → Effective Context → Work Architecture → Current Work Function + Work Session → Workspace / Interface`

The same Work Function may therefore produce different Workspaces for different organizations, people, roles, relationships, Lenses, Capabilities, Permissions, engagements, or temporal circumstances while operating on the same canonical information.

## Suggested Next Action

A **Suggested Next Action** is an explainable recommendation for the most useful permitted Action, Task, or navigation step in the current Work Session. It is derived from Workflow guidance, incomplete work, priority, dependencies, deadlines, Exceptions, Effective Context, and observed work patterns.

A suggestion is not automatically a requirement. ITOMS should distinguish required, recommended, optional, blocked, and automated progression. The user may accept, defer, choose another permitted action, or explain a deviation. High-impact Actions still require the applicable permission, judgment, and approval.

## Workflow / Process Template

A **Workflow/Process Template** is a versioned reusable definition used to guide future instances of work. It may define applicable Work Functions, Stages, Tasks, Actions, roles, decision points, optional paths, handoffs, exceptions, evidence requirements, and completion outcomes.

Starting or updating work from a Template must preserve the version used. Changing a Template affects future use unless an authorized migration explicitly updates active work. A Template is guidance and structure, not a separate copy of the canonical business records it references.

## Ad-hoc and discovered workflow

An **ad-hoc workflow** is work performed without a previously approved Template. It may still have a Work Function, Work Session, Tasks, Actions, relationships, and outcome.

A **discovered workflow** is a candidate pattern inferred from repeated, attributable activity. ITOMS may recognize recurrence and offer to convert it into reusable guidance, but it must not silently declare correlation to be an approved business process.

The discovery progression is:

`Observed Work → Recognized Pattern → Suggested Workflow → User-Defined Workflow → Guided Work → Selective Automation`

For example, ITOMS may observe that a user repeatedly creates a customer record, adds an inventory item, generates a PDF, emails the customer, saves a copy to shared storage, and records completion. It may then ask whether this should become a reusable Workflow.

The user must be able to accept, edit, reject, defer, version, or later improve the suggestion. Pattern detection must respect tenant boundaries, Permissions, data classification, purpose, provenance, and privacy. The evidence supporting a suggestion should remain explainable.

## Handoff

A **Handoff** transfers or requests responsibility for a Task, Stage, Work Session, Exception, or other defined scope from one person, team, provider, or external party to another.

A Handoff records the sender, intended recipient, scope, reason, status, time, required context, and acceptance when applicable. It does not erase prior ownership or presume that responsibility transferred successfully. The receiving party must receive only the context and Actions permitted to it.

## Exception

An **Exception** is a condition in which expected work cannot, should not, or did not proceed according to the current guidance. Examples include missing information, an unavailable system, a rejected approval, an unusual customer condition, or a deliberate deviation.

An Exception may change the Suggested Next Action, create additional Tasks, invoke a Handoff, pause work, or require approval. It should capture cause, impact, disposition, owner, evidence, and resolution when material. An Exception is part of real work, not merely a workflow-engine failure.

## Completion and outcome

**Completion** records that the defined completion criteria for a Task, Stage, Workflow, or Work Session have been satisfied, waived, or otherwise dispositioned.

An **Outcome** records the operational result produced, such as payment recorded, employee onboarded, request declined, assessment delivered, contract activated, or due-diligence response submitted. Completion and outcome are related but distinct: work can end unsuccessfully, partially, by cancellation, or by accepted exception and still require an attributable outcome.

Completion should record who or what concluded the work, when, against which criteria or Template version, with what evidence, and with what unresolved Exceptions or follow-up commitments.

## Guidance and automation

The goal of Work Architecture is productive work, not automation for its own sake. ITOMS combines persistent context, guidance, suggested Actions, shortcuts, reusable processes, coordination, and selective automation.

- Some Actions may be fully automated when authority and reliability permit.
- Some Actions may be prepared automatically but require confirmation.
- Some Tasks may receive guidance while remaining judgment-driven.
- Some work may remain manual or occur outside ITOMS and be recorded afterward.

Automation is subordinate to the Work Function, Effective Context, Permissions, human accountability, and intended outcome. Automating an Action does not redefine the Workflow or the canonical objects involved.

## Relationship to other ITOMS work objects

Work Architecture orchestrates work involving canonical and proposed objects; it does not redefine every work-related object as a Workflow.

| Concept | Relationship to Work Architecture |
| --- | --- |
| Case | A specific investigation, question, incident, decision thread, or problem that may initiate, participate in, or result from work. A Case is not itself a Workflow. |
| Project | A bounded coordinated undertaking that may contain several Work Functions, Workflows, Work Sessions, deliverables, and outcomes. Its canonical boundary remains pending. |
| Scenario | A reusable business-demand or situational description that may identify applicable Work Functions, Templates, capabilities, reports, and roles. It is not a running Workflow unless instantiated as one. Its canonical boundary remains pending. |
| Engagement | A responsibility-bearing relationship or scope connecting people and organizations to a Case, Project, Assessment, or other work. It contributes to Effective Context and handoffs; it is not automatically a Workflow. |
| Assessment | A structured evaluation (`OBJ-ASM-0001`) that may be the subject or outcome of a Work Function and may use one or more Workflows. |
| Task | A unit of work inside or alongside guided progression. It is not a synonym for the object being worked on. Its canonical promotion remains pending. |
| Topic | An enduring subject (`OBJ-TOP-0001`) that can accumulate Cases, work, evidence, decisions, risks, and initiatives across many sessions. |
| Business Initiative | A strategic or operational change effort that may sponsor Projects and Work Functions. Its canonical boundary remains pending. |

## Architectural separation

1. **Canonical Data Architecture** determines what information exists or existed and what persists.
2. **Context Architecture** resolves the circumstances, relationships, roles, Lens, Capabilities, Permissions, engagement, and time under which the actor operates.
3. **Work Architecture** determines what Work Function is being performed, how it may progress, and how continuity, guidance, handoffs, exceptions, and outcomes are maintained.
4. **Interface Architecture** determines how resolved context and work are presented and manipulated.

No Workspace layout, navigation pattern, or screen control should redefine canonical data or Workflow semantics. Conversely, Work Session continuity must survive changes in presentation.

## Interface requirements, not interface design

Future Interface Architecture must support:

- persistent indication of the current Work Function and Work Session;
- previous, current, next, completed, and remaining work items;
- explainable Suggested Next Actions and their status;
- pause, resume, and handoff of Work Sessions;
- cross-object and cross-organization traversal without losing work context;
- appropriate Workflow shortcuts from home and Workspace views;
- user-created, organization-defined, and system-suggested Workflows;
- visible Exceptions, blockers, waiting conditions, recent Actions, and outcomes;
- object-centric views when useful without making them the only navigation model.

Specific layouts, ribbons, panels, device behavior, and visual treatments belong in future Interface Architecture specifications.

## Validation questions

Before approving a work-oriented feature, verify:

1. What Work Function is the person trying to accomplish?
2. Is the progression guidance, a requirement, or an automation, and is that distinction visible?
3. Can the work branch, skip, reverse, pause, leave ITOMS, or encounter an Exception safely?
4. Does the Work Session retain continuity across all relevant objects and systems?
5. Is the Suggested Next Action permitted and explainable in the Effective Context?
6. Are handoffs, decisions, exceptions, completion, and outcomes attributable?
7. Does the Workspace present the work without becoming its canonical data model?
8. Are existing Cases, Projects, Scenarios, Engagements, Assessments, Tasks, Topics, and Initiatives orchestrated rather than unnecessarily redefined?
