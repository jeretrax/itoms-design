# ITOMS Control Monitoring Architecture

**Status:** Proposed

**Purpose:** Define the reusable architecture by which ITOMS continuously observes technology and operations, evaluates expected conditions, creates actionable conclusions, guides remediation, verifies results, preserves evidence, and communicates historical posture.

## Core decision

**Control Monitoring** is the architectural family for continuous technical and operational observation and evaluation in ITOMS. It is not a standalone product, data silo, feature module, or replacement for GRC, Work Architecture, or canonical object services.

Control Monitoring contains two major concerns:

- **Security Monitoring:** evaluates security-related state, control performance, exposure, suspicious change, and evidence.
- **Operational Monitoring:** evaluates availability, performance, configuration, service condition, and other operational expectations.

The initial vertical slice is [Email & Domain Security](applications/email-domain-security.md) within Security Monitoring. It establishes reusable patterns for future identity, endpoint, vulnerability, SaaS, network, WAN, infrastructure, and service-availability monitoring without declaring those future capabilities implemented.

[Local Agent Platform Architecture](local-agent-platform-architecture.md) defines the trusted endpoint source for future endpoint and Device-health monitoring. It establishes collection, buffering, identity, and communication behavior, but does not by itself define final endpoint Controls, evaluation rules, Findings, alert thresholds, or assessment outcomes.

Conceptually:

```text
Control Monitoring
├── Security Monitoring
│   └── Email & Domain Security
└── Operational Monitoring
```

The hierarchy describes architectural responsibility and capability grouping. It does not create software modules, navigation ownership, canonical Domains, or permission grants.

## Reusable monitoring pipeline

Control Monitoring uses the following logical pipeline:

`Collector / Data Source → Raw Observation → Normalization → Entity Resolution → Control Evaluation → State / Condition → Finding → Alert when warranted → Investigation / Work → Remediation → Verification → Evidence → Historical Posture`

These steps are logically distinct even when an implementation combines technical processing stages.

| Stage | Architectural meaning |
| --- | --- |
| Collector / Data Source | An integration, agent, API, report receiver, query, probe, import, or user submission that supplies attributable source data. |
| Raw Observation | Source-native data retained or referenced according to provenance, classification, purpose, retention, and Information Guard policy. A raw artifact may be Evidence rather than a separately promoted object. |
| Normalization | Deterministic parsing and mapping into stable values, categories, units, timestamps, and source references without changing the source artifact. |
| Entity Resolution | Links normalized information to canonical objects and relationships, or records an unresolved candidate without creating a duplicate canonical record. |
| Control Evaluation | Compares resolved evidence and state with a canonical Control, policy, expectation, or approved evaluation rule. |
| State / Condition | The current or interval-based result of evaluation. State and Condition are evaluative concepts; their final persistence boundary remains under review. |
| Finding | An evidence-backed conclusion that an expected condition, Control, or operational requirement is not met or requires disposition. Finding is `OBJ-FND-0001`. |
| Alert | A Finding or change elevated for human attention. Alert uses Attention Item `OBJ-ATT-0001`; it is not a duplicate first-class object. |
| Investigation / Work | A Case `OBJ-CAS-0001`, Work Session `OBJ-WSS-0001`, and applicable Workflow coordinate judgment, assignment, remediation, and external activity. An Incident is a security-classified Case unless a later decision establishes a separate boundary. |
| Remediation | Attributable Tasks and Actions intended to correct, mitigate, accept, suppress, or otherwise disposition the Finding. |
| Verification | A new evaluation establishes whether the expected condition is now met. Closure does not erase prior failed state. |
| Evidence | Evidence `OBJ-EVD-0001` supports observations, evaluations, Findings, decisions, remediation, and verification without being copied for every consumer. |
| Historical Posture | Explainable, time-aware representation of condition, Finding, remediation, verification, exceptions, and coverage across a defined scope. |

## Required distinctions

- An **Observation** is not automatically a Finding.
- A **Finding** is not automatically an Alert.
- An **Alert** is not automatically an Incident.
- An **Incident** is not automatically a Risk.
- A failed evaluation does not automatically create a ticket, Case, or human interruption.
- A current posture summary does not replace the observations, rules, evidence, and history that explain it.

Routine telemetry should normally update observations, evaluation state, and posture without demanding human attention. Promotion decisions are attributable, policy-driven, and explainable.

## Canonical object reconciliation

### Existing objects reused

| Concept | Canonical use in monitoring |
| --- | --- |
| Company `OBJ-CMP-0001` | Organization, customer, provider, vendor, reporting organization, service provider, or other party. |
| Person `OBJ-PER-0001` and Contact `OBJ-CON-0001` | Owners, administrators, reviewers, responsible parties, approvers, customer contacts, and analysts. |
| Asset `OBJ-AST-0001` | Durable technical or operational thing being monitored. |
| Application `OBJ-APP-0001` | Software, SaaS, workload, sending application, monitoring service, or other application identity. |
| Policy `OBJ-POL-0001` and Control `OBJ-CTL-0001` | Expected behavior and measurable evaluation criteria. |
| Observation `OBJ-OBS-0001` | Attributable factual information that was seen, measured, discovered, or asserted. |
| Assessment `OBJ-ASM-0001` | Structured point-in-time or scoped evaluation that may consume monitoring state. |
| Attention Item `OBJ-ATT-0001` | Alert or attention signal requiring human awareness or action. |
| Case `OBJ-CAS-0001` | Investigation, Incident, question, or decision thread arising from monitoring. |
| Risk `OBJ-RSK-0001` | Business exposure separately evaluated or accepted from one or more Findings. |
| Evidence `OBJ-EVD-0001` | Source artifact, report, measurement, evaluation result, approval, or proof. |
| Workflow `OBJ-WFL-0001` and Work Session `OBJ-WSS-0001` | Guided, resumable investigation, remediation, verification, and exception work. |

### New canonical objects

**Internet Domain** (`OBJ-IDN-0001`) is a technical Asset with durable identity, ownership, relationships, configuration, and history independent of a single Company field or monitoring application. It may represent a registered organizational domain, delegated subdomain, or another monitored DNS scope when that scope is explicitly identified. The exact normalization and scope rules remain open design questions.

**Finding** (`OBJ-FND-0001`) is an evaluated, evidence-backed conclusion that an expected condition, Control, or operational requirement is not met or requires disposition. It preserves subject, rule or Control, severity, lifecycle, provenance, first and last seen time, responsibility, evidence, exceptions, remediation, and verification as applicable.

### Concepts not promoted by this decision

- **Alert** is an Attention Item role or type.
- **Incident** is a Case classification with additional security context and permissions.
- **Sending Source** is a contextual role and resolution construct relating an Internet Domain to a canonical Application, Device, Company, service relationship, or unresolved candidate.
- **Control Evaluation**, **State**, **Condition**, **Collector**, and **Monitor** remain evaluation, configuration, or runtime concepts until their independent identity and lifecycle requirements are approved.

## Data ownership and source authority

Monitoring consumes canonical objects. It must not create separate customer, Person, Application, Device, vendor, service, or Internet Domain directories.

The monitoring capability owns its operational monitoring records, including attributable observations, evaluation results, Findings, alert decisions, monitoring exceptions, posture history, detection history, and security-specific evidence. Ownership of those records does not transfer ownership of the canonical subject being monitored.

Entity resolution follows these rules:

1. Resolve to an existing canonical object when evidence supports the match.
2. Preserve source identifiers and source placement separately from canonical identity.
3. Represent an unresolved candidate explicitly rather than inventing a canonical match.
4. Reconciliation changes the mapping and confidence, not the historical source artifact.
5. A monitoring application never becomes authoritative for unrelated organizational or asset data merely because it observed it.

## Control evaluation and GRC

Control Monitoring performs operational evaluation. GRC defines and governs Policies, Controls, frameworks, Assessments, Risks, and acceptance.

The reusable relationship is:

`Operations generates attributable Evidence → Control Monitoring evaluates current conditions → GRC consumes the same Evidence and evaluation history`

Monitoring must not create separate copies of Evidence for dashboards, customer reports, Assessments, audits, or framework mappings. Each consumer references the canonical Evidence and receives only the details allowed by Effective Context and Permissions.

A Control may be evaluated continuously, periodically, on change, on demand, or as part of an Assessment. Evaluation cadence does not change Control identity.

The unified Framework, Requirement, Control Implementation, manual Assessment, Finding, Remediation, and posture semantics are defined in [`grc-architecture.md`](grc-architecture.md). A monitoring evaluation may supply attributable Evidence or an assessment input, but it does not silently approve a GRC Assessment Result or change Current Posture.

## Temporal and historical requirements

Control Monitoring preserves meaningful time and does not overwrite material state. At minimum, the architecture must support:

- source capture and reporting intervals;
- first seen, last seen, and recurrence;
- current and prior evaluated condition;
- configuration and policy changes;
- Finding creation, transition, suppression, acceptance, remediation, verification, recurrence, and closure;
- collection continuity and gaps;
- the rule, Control, threshold, exception, and configuration version used for a historical decision;
- the identity and authorization state of a related source at the time of the observed activity.

Derived current posture is reproducible from retained canonical records and approved rules. Retention policy may summarize or expire raw data, but it must preserve the evidence and auditability required by the applicable purpose, contract, regulation, and Control.

## Permissions and information boundaries

Monitoring summaries and restricted investigative detail are separate authorization scopes.

A permitted user may see a canonical subject's monitoring status, active Finding count, monitoring coverage, or last review without gaining access to restricted evidence, analyst notes, message-related information, indicators, or Incident details.

Effective Context and Permissions govern discovery and action. Information Guard governs collection, persistence, transformation, retention, disclosure, and AI exposure for each Channel. A link from a broadly visible Asset to a restricted Finding never grants access to the Finding or its Evidence.

## Work Architecture

Control Monitoring identifies meaningful work; it does not become a rigid ticket generator.

Findings may produce Suggested Next Actions, Attention Items, Cases, Work Sessions, handoffs, exceptions, remediation Tasks, approvals, and verification. Workflows may branch, pause, wait for a customer or vendor, accept risk, document expected behavior, or close as a false positive.

Navigation should follow the monitoring Work Function across the canonical subject, source data, Control, Finding, evidence, external system, remediation, and verification without losing Work Session context.

## System Settings and integrations

System Settings governs monitoring configuration, including collectors, credentials and secret references, schedules, evaluation cadence, thresholds, baselines, routing, suppression, exceptions, retention, and health. Configuration creates no authority by itself.

Each collection or interaction path resolves to an Information Guard Channel. Connectors provide technical access and source mappings; Channels provide collection and handling policy. Collector access does not imply permission to retain, disclose, or submit all accessible data to AI.

Device Agent observations retain capture time, source identity, configuration version, delivery time, and collection-gap information so delayed store-and-forward data is not mistaken for current state. Local thresholding or detection remains a source assertion until platform normalization, entity resolution, and evaluation determine the applicable Observation, Evidence, State, or Finding.

## Experience requirements

The primary experience is work-first. People should review meaningful changes, investigate Findings, perform remediation, and verify results rather than watch raw telemetry tables.

Appropriately authorized administrative views may expose observations, evaluation state, controls, Findings, evidence, collection health, and history. Exact screen layout and the final labels for Work Mode and Data Mode remain Interface Architecture decisions.

Posture summaries must remain explainable. A user must be able to determine what condition caused the status, which evidence supports it, what must change, who is responsible, when it began, and when it was last verified.

## Validation questions

1. Does the monitor reference canonical subjects rather than create a duplicate directory?
2. Can raw and normalized observations be traced to source, time, and policy?
3. Is entity resolution explicit, confidence-aware, and reversible?
4. Are Observation, Finding, Alert, Incident, and Risk kept distinct?
5. Is the evaluation rule, Control, threshold, exception, and configuration version explainable?
6. Can routine data update posture without generating unnecessary human alerts?
7. Does remediation occur through Work Architecture with attributable completion and verification?
8. Is monitoring Evidence reusable by GRC and reporting without duplication?
9. Are restricted investigation details protected independently from summary posture?
10. Can the system reconstruct posture and collection coverage for a prior time?
