# ITOMS Design-to-Implementation Governance Handoff

**Status:** Proposed

**Purpose:** Formalize a specification-driven workflow with bidirectional traceability from design to implementation and from implementation discoveries back into canonical design.

## Core rule

The `itoms-design` repository is the canonical design authority for ITOMS. Conversation, review, implementation planning, source code, tests, and generated artifacts may interpret or realize that design, but they do not independently redefine it.

Approved design is translated into bounded Engineering Work Packages. Each package identifies the canonical design it implements, the limits of the authorized work, and the evidence required to show conformance. Implementation discoveries flow back through an explicit design-escalation path before they can change product behavior.

## Authorities and responsibilities

| Surface or artifact | Responsibility | Authority boundary |
| --- | --- | --- |
| Chat | Design conversation, exploration, clarification, examples, and proposed decisions. | Conversation is design input. It is not canonical until reconciled into `itoms-design`. |
| ChatGPT Work | Design review, repository reconciliation, conflict identification, canonical document updates, link validation, and preparation of approved handoff material. | Work applies the repository rules and records decisions. Work does not become a separate design authority. |
| `itoms-design` | Canonical design definitions, permanent identities, design principles, architecture, registries, design notes, and ADRs. | This repository is the authoritative product-design source. Conflicts are resolved according to `REPO_START_HERE.md`, permanent IDs, canonical registries, and applicable ADRs. |
| Engineering Work Package | Bounded translation of approved design into implementable scope, constraints, acceptance criteria, validation, and traceability. | A package may clarify engineering scope but may not invent or override product behavior. |
| Codex and other implementation assistants | Inspect applicable design, implement an approved package, test the result, report evidence, and surface gaps. | An implementation assistant may make ordinary reversible engineering choices inside the package boundary. It must not redefine canonical concepts, permissions, workflows, lifecycle, or intended behavior. |
| Implementation repositories | Source code, migrations, contracts, tests, build configuration, and deployment artifacts that realize the design. | Implementation state is evidence of what was built, not authority for what ITOMS is intended to mean. |

Human approval roles and the final approval mechanism remain design questions. Tool names describe current responsibilities, not permanent product architecture or exclusive vendors.

## Governing principles

### Canonical design authority

Product meaning originates in the canonical design repository. A chat transcript, Work output, Engineering Work Package, code comment, issue, source schema, UI implementation, or test expectation cannot silently supersede canonical design.

When canonical sources appear inconsistent, resolve identity by permanent ID and follow the repository read order. Record the reconciliation in the appropriate canonical document, design note, or ADR before treating an interpretation as approved.

### Bidirectional traceability

Traceability must work in both directions:

`Canonical Design → Engineering Work Package → Implementation Change → Validation Evidence`

`Implementation Discovery → Design Gap → Canonical Design Decision → Updated Engineering Work Package → Implementation Change`

An implementation change must be traceable to the approved design and package that authorized it. A material implementation discovery must be traceable back to the design record that resolved it.

At minimum, traceability should identify:

- applicable canonical document paths, permanent IDs, registry rows, design notes, and ADRs;
- the Engineering Work Package reference and approved scope;
- implementation repository, issue, branch, commit, pull request, migration, or equivalent change reference;
- tests, review results, generated contracts, screenshots, or other validation evidence;
- unresolved gaps, deviations, and the canonical disposition that permits or rejects them.

The final identifier scheme and traceability automation are intentionally unresolved. File paths or tool-local identifiers are not substitutes for permanent canonical IDs where those IDs already exist.

### Escalation of design gaps

A **Design Gap** exists when implementation cannot proceed without selecting product meaning that the canonical design does not define clearly enough, or when applicable canonical sources conflict.

A material ambiguity requires design escalation when it could affect, among other concerns:

- canonical identity, object boundaries, Primary Domain, or relationship meaning;
- ownership, custody, responsibility, provenance, temporal history, or lifecycle;
- user-visible behavior, required outcomes, workflow progression, or exception handling;
- Capabilities, Permissions, tenant boundaries, Effective Context, or administrative authority;
- information collection, retention, disclosure, deletion, AI exposure, auditability, or compliance;
- integration mapping, source authority, reconciliation, or persistence;
- destructive behavior, irreversible migration, compatibility, or acceptance criteria.

The affected portion of implementation must pause at the ambiguity boundary. Unaffected work that remains inside the approved package may continue when it cannot prejudge the decision.

The minimum escalation path is:

1. Describe the ambiguity, conflicting sources, affected scope, and implementation consequence.
2. Link the gap from the Engineering Work Package and record it in [`12-ITOMS_DESIGN_REGISTER.md`](12-ITOMS_DESIGN_REGISTER.md).
3. Reconcile the question against the canonical read order and existing permanent IDs.
4. Update the governing design document, registry, or ADR when a decision is approved.
5. Revise or supersede the affected Engineering Work Package so its scope and acceptance criteria match the approved design.
6. Resume implementation and retain links to the decision and validation evidence.

An issue, comment, or local workaround does not close a material Design Gap unless the canonical design disposition is recorded.

### No silent invention of product behavior

Implementation must not silently introduce a new product concept, default, state, transition, permission, destructive effect, data interpretation, workflow requirement, or user-facing rule merely because the code requires a choice.

An ordinary engineering choice may be made within an approved package only when it does not alter canonical meaning or observable product obligations, remains consistent with all applicable constraints, and is recorded where future maintainers need it. If that test is uncertain, treat the choice as a Design Gap.

## Engineering Work Packages

An **Engineering Work Package** is a bounded, reviewable handoff artifact that translates approved canonical design into a specific implementation objective. It is not a Workflow, Work Session, Project, Case, Scenario, canonical object, or substitute design specification.

Each package must:

- state its objective and explicit in-scope and out-of-scope boundaries;
- cite the exact approved canonical design sources it implements;
- identify affected canonical objects and permanent IDs where applicable;
- state required behavior, constraints, acceptance criteria, and validation evidence;
- identify affected implementation surfaces without presuming unapproved architecture;
- record dependencies, risks, assumptions requiring confirmation, and known Design Gaps;
- define how discoveries and deviations return to design review;
- identify the resulting implementation and validation references after completion.

Packages should be small enough that approval does not authorize unrelated product decisions. A package may coordinate several implementation changes when they share one coherent objective and design boundary.

The placeholder-only template is maintained at [`templates/engineering-work-package-template.md`](templates/engineering-work-package-template.md).

## Specification-driven workflow

### 1. Design conversation

Chat develops the problem statement, desired outcome, examples, constraints, alternatives, and questions. Proposed language remains non-canonical at this stage.

### 2. Design review and reconciliation

Work reads the current canonical repository, compares the proposal with existing definitions and decisions, preserves prior intent, identifies conflicts, and records unresolved questions in the design register. Material durable decisions receive an ADR when required by repository rules.

### 3. Canonical design approval

Approved changes are committed to `itoms-design`. The applicable commit and canonical paths establish the design baseline for an Engineering Work Package. Merely drafting or discussing a change does not authorize implementation as settled behavior.

### 4. Engineering Work Package preparation

The approved design is translated into a bounded package using the repository template. The package references design rather than copying and subtly rewriting it. Any necessary interpretation is explicit and reviewable.

### 5. Implementation

Codex or another implementer reads the package and every cited canonical source before changing code. Implementation stays within the package boundary, preserves canonical IDs and contracts, and produces the required tests and evidence.

### 6. Gap handling and feedback

Implementation findings are classified as conforming engineering detail, nonconformance, or potential Design Gap. Material ambiguities follow the escalation path. The implementation is not used as the reason to retroactively declare unreviewed behavior canonical.

### 7. Completion and reconciliation

Completion records implementation references, validation evidence, deviations, and remaining questions. When implementation reveals a durable truth or approved design change, that information is reconciled back into `itoms-design` and linked bidirectionally.

## Relationship to existing architecture

- [Context Architecture](context-architecture.md) determines Effective Context and separates canonical truth, context, authorization, and presentation. An Engineering Work Package must cite rather than reinterpret those boundaries.
- [Work Architecture](work-architecture.md) defines Work Functions, Workflows, Stages, Tasks, Actions, Work Sessions, and outcomes. The engineering handoff process may use work-management tools, but an Engineering Work Package is not automatically one of those product concepts.
- [Asset Architecture](asset-architecture.md) governs Asset ownership, custody, deployment, and external placement. Implementation convenience cannot collapse those relationships.
- [System Settings Architecture](system-settings-architecture.md) governs installation configuration and enforcement. Work-package scope cannot create authority or relax Information Guard.
- [Application Architecture](09-ITOMS_APPLICATION_ARCHITECTURE.md) defines logical services and deployment expectations. Technology choices must remain consistent with its contracts and deployment shapes.
- [Design Register](12-ITOMS_DESIGN_REGISTER.md) records unresolved gaps and their disposition.
- [`ITOMS_CANONICAL_RULES.md`](../../ITOMS_CANONICAL_RULES.md) governs permanent identity, Primary Domain, relationships, aliases, and required ADRs.

## Required handoff checks

Before approving an Engineering Work Package, verify:

1. Does it cite the current canonical design baseline and every applicable permanent ID?
2. Is the objective bounded, with explicit exclusions and dependencies?
3. Are product behavior and acceptance criteria supported by canonical design rather than inferred from implementation convenience?
4. Are Context, Work, Asset, System Settings, information-governance, and permission boundaries preserved where applicable?
5. Are material ambiguities recorded and escalated instead of hidden as assumptions?
6. Can each implementation change and validation result be traced back to the package?
7. Can every material implementation discovery be traced to a canonical disposition?
8. Does completion update both sides of the traceability chain without treating code as the design authority?

