# ITOMS GRC Architecture

**Status:** Proposed

**Purpose:** Define the unified Governance, Risk, and Compliance capability by which ITOMS represents obligations, reusable safeguards, scoped implementation, evidence, assessment, gaps, remediation, and progress from current posture toward target posture.

## Core decision

ITOMS uses one canonical GRC graph rather than separate compliance checklists for each framework:

`Framework → Requirement ↔ Control → Control Implementation → Evidence → Assessment → Finding → Remediation`

The chain expresses traceability, not a rigid Workflow. Controls and Requirements have a many-to-many relationship. Evidence may support several implementations, assessments, or Findings. An Assessment may evaluate a Requirement, Control, Control Implementation, or defined scope. A Finding may identify a gap without forcing immediate remediation, and a Remediation may coordinate one or more Tasks or Projects.

Version 1 is manual and progress-focused. It provides structured assessment, evidence attachment, gap identification, proposed remediation, planning, and traceable progress. Automated evidence collection and continuous evaluation may be added later through Control Monitoring, but automation does not replace attributable assessment or canonical state.

## Target product goal

The [GRC Solutions Landscape Summary](mockups/grc-solutions-landscape-summary.html) is the accepted target experience and capability-coverage goal for GRC in ITOMS.

The goal is not merely to reproduce the mockup as one enormous screen. The goal is for ITOMS to make the complete security, risk, governance, compliance, resilience, policy, procedure, control, service, evidence, assessment, remediation, and improvement landscape available through one coherent GRC capability.

The resulting capability must allow an authorized person to understand, in one connected environment:

- what the organization could adopt, configure, subscribe to, document, assess, or improve;
- what is applicable to the organization and why;
- what has been selected, adopted, purchased, assigned, or declined;
- what is currently implemented and operating;
- what is supported by Evidence and what remains unverified;
- what the latest approved Assessment concluded;
- what gaps and Findings remain;
- what Remediations have been proposed, accepted, deferred, rejected, completed, or verified;
- what effort, cost, dependencies, services, Tasks, or Projects are associated with improvement;
- how Current Posture compares with Planned and Target Posture;
- which Framework Requirements and reusable Controls are affected by each decision.

The landscape should be consumable by an ordinary business manager while retaining drill-down for technicians, assessors, auditors, security personnel, service managers, and executives. It should make both existing work and additional available solutions visible without presenting optional services as already included, planned work as verified, or broad visibility as authorization to restricted records.

### Goal versus literal interface

The mockup establishes required breadth, connectedness, visibility, posture comparison, filtering, traceability, and navigation intent. Its exact dimensions, generated sample entries, record counts, percentages, colors, wording, and card layout are illustrative. They are not canonical data, a mandatory final screen layout, or a claim that every solution applies to every organization.

The final interface may provide summary, filtered, role-specific, Work-oriented, Data-oriented, mobile, executive, customer, and detailed views. Those views must all resolve to the same canonical GRC graph and must collectively preserve the whole-landscape goal.

### Capability rather than silo

“GRC module” may be used conversationally for the user-facing capability area. Architecturally, GRC remains a cross-cutting ITOMS Capability and Workspace, not a module-owned data silo. It uses canonical Companies, People, Assets, Applications, Policies, Frameworks, Requirements, Controls, Control Implementations, Evidence, Assessments, Findings, Remediations, Risks, Work Sessions, Tasks, Projects, costs, subscriptions, and relationships.

GRC processes are responsible for progressively turning the possible landscape into attributable organizational decisions, implementation records, Evidence, Assessment Results, Findings, accepted plans, completed work, and verified improvement.

## Standards alignment

The terminology and separation align conceptually with the [NIST Open Security Controls Assessment Language layers and models](https://pages.nist.gov/OSCAL/learn/concepts/layer/): control catalogs, profiles and mappings; system and component implementation; assessment plans and results; Findings with supporting Evidence; and Plan of Action and Milestones remediation. ITOMS uses broader cross-framework business terms and does not claim OSCAL serialization or conformance in V1. Future import or export must map explicitly and preserve canonical IDs, source versions, and provenance.

## Canonical concepts

### Framework

A **Framework** (`OBJ-FWK-0001`) is a named, versioned body of governance, risk, compliance, security, privacy, contractual, or operational guidance issued or maintained by an identifiable authority. Examples may include CMMC, NIST CSF, CIS Controls, or a customer-defined framework.

A Framework provides structure and provenance. It does not create duplicate Controls for every framework version.

### Requirement

A **Requirement** (`OBJ-REQ-0001`) is a versioned statement within a Framework that expresses an obligation, expected outcome, practice, criterion, or condition that can be evaluated.

Requirement identity preserves the source framework, source identifier, version, text, applicability, and effective period. A Requirement is not the same as a Control: it states what must be achieved, while a Control describes a reusable safeguard or practice used to meet one or more Requirements.

### Control

A **Control** (`OBJ-CTL-0001`) is a reusable, measurable safeguard or practice. Controls relate many-to-many with Requirements so the same implementation and Evidence can support several frameworks without duplication.

The mapping must retain mapping type, rationale, provenance, effective version, and coverage characterization when material. A mapping does not by itself prove that the Requirement is satisfied.

### Control Implementation

A **Control Implementation** (`OBJ-CIM-0001`) describes how a Control is implemented, planned, inherited, shared, or intentionally not implemented for a defined organization, system, service, Asset, Location, engagement, or other scope.

It provides the implementation narrative, scope, responsible party, operating frequency, implementation status, applicable dates, and relationships to Evidence and work. The Control remains the reusable definition; the Control Implementation is the contextual realization.

### Evidence

**Evidence** (`OBJ-EVD-0001`) is the governed artifact, assertion, record, measurement, document, screenshot, configuration result, approval, interview result, or other support used to substantiate an implementation, assessment result, Finding, remediation, exception, or decision.

Evidence is referenced rather than copied for each framework. Evidence attachment must support metadata including:

- evidence type, title, description, and source;
- owner, custodian, submitter, and verifier where applicable;
- collection or creation time and relevant coverage period;
- related canonical objects, scope, Requirements, Controls, implementations, Assessments, and Findings;
- provenance, verification state, integrity reference, and source-system identifier;
- classification, handling, retention, expiration, review date, and access restrictions;
- version, supersession, and historical validity.

An attachment proves only what its scope, period, provenance, and assessment support. Presence of a file does not automatically satisfy a Control.

### Assessment

An **Assessment** (`OBJ-ASM-0001`) is an attributable, scoped evaluation against a defined Framework, Requirement set, Control set, implementation set, or target baseline at a point in time or over a stated period.

V1 Assessments are manual. A qualified actor reviews the applicable Requirement, Control, Control Implementation, and Evidence and records an assessment result with rationale. Imported or automated observations may be presented later as inputs, but they remain distinguishable from the assessor's conclusion.

An **Assessment Result** is the versioned relationship/result record that connects an Assessment to its evaluated subject and records state, rationale, assessor, time, Evidence, exceptions, and review status. It is not promoted as a separate first-class object in this decision.

### Finding

A **Finding** (`OBJ-FND-0001`) is the existing cross-domain, evidence-backed conclusion that an expected condition, Control, or Requirement is not met or requires disposition. GRC reuses Finding rather than creating a separate compliance-gap object.

A posture gap may create or relate to a Finding when an attributable conclusion and lifecycle are needed. A calculated difference between current and target posture is not automatically a Finding.

### Remediation

A **Remediation** (`OBJ-REM-0001`) is a proposed or accepted plan for correcting, mitigating, compensating for, or otherwise addressing one or more Findings or posture gaps.

A Remediation records scope, intended outcome, proposed approach, responsible party, dependencies, estimated effort, estimated cost, timing, priority, acceptance decision, target effect, and relationships to Tasks, Projects, Evidence, and verification. It is not itself a Task or Project. Work Architecture coordinates execution.

## Assessment states

The canonical V1 assessment states are:

| State | Meaning |
| --- | --- |
| **Satisfied** | Available Evidence and assessor rationale support that the evaluated expectation is met for the stated scope and period. |
| **Partial** | The expectation is met only in part, only for part of the scope, or with material limitations that prevent a Satisfied conclusion. |
| **Unsatisfied** | Available Evidence and assessor rationale support that the expectation is not met for the stated scope and period. |
| **Not Assessed** | No approved conclusion exists for the stated scope and assessment baseline. This is not equivalent to Satisfied or Unsatisfied. |

These are assessment conclusions, not Workflow statuses, implementation lifecycle states, risk decisions, or remediation states. A state change creates assessment history; it does not rewrite the prior conclusion.

## Current, planned, and target posture

### Current Posture

**Current Posture** is the latest approved, attributable assessment state for the applicable scope and baseline. It represents assessed truth, including its assessment date, Evidence coverage, exceptions, and confidence or review status where applicable.

Completing a Task, uploading Evidence, editing an implementation narrative, or accepting a Remediation does not by itself change Current Posture. Current Posture changes when an authorized Assessment concludes and records a new supported state.

### Planned Posture

**Planned Posture** is a projection of the posture expected if accepted Remediations achieve their explicitly stated target effects. Accepting a proposed Remediation includes it in Planned Posture. Rejecting, deferring, or merely drafting it does not.

Planned Posture is not verified compliance and must always be labeled as projected. It retains the Remediation assumptions, effort, cost, dependencies, target date, and affected Requirements, Controls, and implementations.

### Target Posture

**Target Posture** is the approved desired state for a defined organization, system, service, Framework, Control Domain, or other scope and target date. It expresses the baseline the organization intends or is obligated to reach.

Target selection does not alter Current Posture. A target can be changed prospectively with approval and history, but it must not be used to rewrite prior obligations or assessment results.

### Percentages and score interpretation

Scorecards show Current, Planned, and Target percentages with the underlying counts and status distribution. Each percentage must identify its scope, baseline or Framework version, as-of or target date, calculation policy, exclusions, treatment of Not Assessed items, and treatment of Partial items.

The final weighting formula, cross-framework aggregation policy, and treatment of alternative or compensating Controls remain open design decisions. V1 must not present a percentage as an external certification or compliance determination unless the applicable methodology and authority support that claim.

## Scorecard and drill-down requirements

The GRC Scorecard presents two coordinated views of the same canonical graph:

- **Control Domain view:** posture grouped by a governed control category such as Identity and Access, Asset Management, Data Protection, or Incident Response.
- **Framework view:** posture grouped by Framework and Requirement hierarchy.

“Control Domain” in this context is a classification or reporting taxonomy. It must not be confused with an ITOMS Primary Domain or `PrimaryDomainID`. Its final canonical taxonomy and promotion boundary remain under review.

For each supported row or group, the Scorecard shows Current, Planned, and Target posture side by side, including state counts and progress toward the target. A user with the appropriate Permissions can drill through:

`Scorecard → Framework / Control Domain → Requirement → mapped Control → Control Implementation → Evidence / Assessment Result → Finding → Remediation → Task or Project`

The interface must explain why a value exists and must preserve scope while moving between framework and control-oriented views. It must not duplicate the underlying records to produce each view.

## Gaps and remediation planning

A **gap** is the explainable difference between Current Posture and Target Posture for a defined scope. It is derived from approved target and assessment records and is not independently promoted as a canonical object in V1.

A gap may produce one or more proposed Remediations. A proposed Remediation includes:

- affected Requirement, Control, Control Implementation, Finding, and scope;
- intended target effect and expected posture change;
- effort estimate and estimating basis;
- cost estimate, currency, range or confidence, and estimating basis;
- dependencies, assumptions, constraints, priority, and target timing;
- proposed responsible party and approval requirements;
- related Task, Project, Workflow, or external work when accepted.

Acceptance is an attributable planning decision. It updates Planned Posture, not Current Posture. Completion must be followed by Evidence and reassessment before the verified posture changes.

## Manual V1 Work Function

The initial Work Function is:

`Select Scope and Target → Map Applicable Requirements and Controls → Document Control Implementations → Attach or Reference Evidence → Perform Manual Assessment → Record Findings → Propose Remediations → Estimate Effort and Cost → Accept / Defer / Reject → Coordinate Tasks or Projects → Verify Evidence → Reassess → Report Progress`

This is guided work, not a rigid sequence. Users may assess incrementally, revisit conclusions, attach Evidence later, split remediation work, record exceptions, or defer a decision. Work Sessions preserve context across Frameworks, Requirements, Controls, Evidence, Findings, Remediations, Tasks, and Projects.

## Relationship to Control Monitoring

GRC defines obligations, reusable Controls, scoped implementations, manual assessment, target posture, Findings, and remediation governance. [Control Monitoring](control-monitoring-architecture.md) observes and evaluates operational conditions.

Future automation may suggest Evidence, prepopulate assessment inputs, or continuously evaluate a Control. It must preserve source provenance and cannot silently convert an Observation into an approved Assessment Result. Operations and GRC reference the same canonical Evidence rather than copying it.

## Context, permissions, and history

Effective Context determines which organizations, scopes, Frameworks, implementations, Evidence, Findings, costs, and work a person may discover or act upon. Lens and scorecard presentation never grant access.

The architecture must preserve:

- Framework and Requirement versions;
- effective-dated mappings and applicability decisions;
- Control Implementation history and responsible parties;
- Assessment scope, baseline, result, rationale, assessor, and approval;
- Evidence version, period, provenance, classification, and retention;
- Finding and Remediation decisions, estimates, approvals, and state changes;
- the calculation policy behind every historical posture value;
- Current, Planned, and Target posture as distinct historical views.

## V1 boundary

V1 includes manual Framework and Requirement setup or import, many-to-many Control mapping, scoped Control Implementations, Evidence attachment and metadata, manual Assessments using the four canonical states, Findings, proposed Remediations with effort and cost estimates, acceptance-driven Planned Posture, progress scorecards, and drill-down to work.

V1 does not require automated evidence collection, continuous control monitoring, AI assessment, automatic remediation, certification issuance, or a universal scoring formula. Those capabilities require separately approved design and Engineering Work Packages.

## Validation questions

1. Can every score be traced to versioned Requirements, Controls, implementations, Assessments, and Evidence?
2. Are Requirements and Controls many-to-many without duplicated safeguards?
3. Is the scoped Control Implementation distinct from the reusable Control?
4. Are Current, Planned, and Target Posture visibly different and historically reconstructable?
5. Does accepting a Remediation change only Planned Posture until reassessment verifies the outcome?
6. Are Not Assessed and Unsatisfied kept distinct?
7. Can Evidence be reused without losing scope, provenance, classification, or access control?
8. Can users drill from posture to Requirement, Control, Evidence, Finding, Remediation, and work?
9. Does V1 remain useful when every assessment and evidence decision is manual?
10. Are formula, weighting, applicability, exception, and certification claims explicit rather than implied?
