# ITOMS Email & Domain Security Specification

**Status:** Proposed

**Purpose:** Define the first concrete Security Monitoring capability and vertical slice of [Control Monitoring Architecture](../control-monitoring-architecture.md).

**Implementation status:** Design only. This document does not authorize application implementation or substitute for an approved Engineering Work Package.

## Objective

Email & Domain Security continuously monitors, assesses, explains, and helps improve the email-authentication posture of canonical Internet Domain Assets. The initial scope includes DMARC, SPF, DKIM, sending-source discovery, alignment, reporting continuity, DNS change, Findings, remediation, verification, evidence, customer reporting, and self-service enrollment.

The capability is not a DMARC-only dashboard and is not a standalone product architecture. It proves the reusable ITOMS pattern:

`Canonical Asset + Continuous Telemetry + Historical Observation + Control Evaluation + Actionable Finding + Human Work + Remediation + Verification + Evidence + GRC Consumption + Customer Visibility`

## Architectural placement

`ITOMS → Control Monitoring → Security Monitoring → Email & Domain Security`

Email & Domain Security uses canonical object, context, work, integration, evidence, GRC, System Settings, and Information Guard services. It may provide a focused Workspace and capability navigation without creating a module-owned data silo.

## Scope

Initial design scope:

- DNS discovery and change monitoring for mail-related records;
- SPF existence, syntax, technical-limit, dependency, and change evaluation;
- DKIM configuration and selector observations where known or discoverable;
- DMARC existence, syntax, alignment, policy, reporting, override, and enforcement evaluation;
- DMARC aggregate report ingestion and normalized history;
- DMARC forensic or failure report support where available and permitted;
- email Sending Source resolution, classification, authorization, and history;
- explainable posture dimensions and enforcement readiness;
- Finding, alert, investigation, remediation, verification, exception, and evidence handling;
- customer, technician, executive, and MSP fleet views through Effective Context;
- self-service and technician-assisted domain enrollment;
- assessment, reporting, GRC, and customer-education outputs.

The design does not claim to eliminate phishing, guarantee receiver behavior, or depend on forensic reports being available.

## Canonical data and ownership

### Canonical subjects

- Organization and customer identity use Company `OBJ-CMP-0001`.
- People, administrators, owners, contacts, vendors, analysts, and responsible parties use Person `OBJ-PER-0001`, Contact `OBJ-CON-0001`, and relationships.
- Each monitored DNS scope uses Internet Domain `OBJ-IDN-0001`, a technical Asset related to Asset `OBJ-AST-0001`.
- Microsoft 365, Google Workspace, Proofpoint, SendGrid, Mailchimp, Salesforce, line-of-business applications, websites, relays, and other known sources reference canonical Company, Application `OBJ-APP-0001`, Device `OBJ-DEV-0001`, service, subscription, and relationship records as applicable.
- Controls, Policies, Risks, Assessments, Observations, Findings, Attention Items, Cases, Evidence, Workflows, and Work Sessions use their canonical objects.

The capability must not create duplicate organizations, people, Internet Domains, applications, vendors, or services. Security-specific state concerning those objects remains owned by Security Monitoring.

### Security Monitoring records

The capability maintains security-specific observations, normalized report data, evaluation results, posture history, Findings, Attention Items, monitoring exceptions, detection history, remediation state, verification results, and restricted Evidence.

Security ownership of an operational record does not broaden who may see it. Summary posture and sensitive investigation content require separate permissions.

## Internet Domain model

An Internet Domain retains durable identity across monitoring enrollment, DNS-provider changes, mail-provider changes, ownership changes, assessment, ongoing service, and removal from monitoring.

Required relationships may include:

- authoritative Owner under [Asset Architecture](../asset-architecture.md);
- associated Company or Companies and the role of each relationship;
- parent, child, delegated, organizational-domain, or reporting scope when approved;
- mail services, DNS providers, registrars, applications, vendors, and sending sources;
- Policies, Controls, Assessments, Findings, Risks, Evidence, Cases, and Work Sessions;
- monitoring enrollment, coverage, configuration, and historical posture.

`Company.PrimaryInternetDomain` remains a convenience/default reference and must resolve to the canonical Internet Domain when one exists. It must not become a competing domain record.

## Collection sources

### DNS

Initial DNS collection covers:

- MX records;
- SPF TXT records and included dependencies;
- DMARC TXT records;
- DKIM selectors where known or discoverable;
- CNAME dependencies;
- other explicitly approved mail-related records.

Observed DNS state is distinct from desired configuration. Generating or recommending a record does not prove that a DNS provider contains it; independent observation verifies deployment.

### DMARC aggregate reports

Aggregate reports are the primary operational source for sending-source discovery and authentication behavior. The parser should preserve or normalize, when supplied:

- reporting organization, report ID, and reporting interval;
- source IP and message count;
- header From and envelope or MailFrom domain;
- SPF and DKIM result;
- SPF and DKIM alignment;
- DMARC disposition and policy applied;
- policy overrides and supplied failure reasons.

Aggregate reports support volume, authentication, alignment, source discovery, enforcement readiness, reporting continuity, change detection, Findings, trends, and historical posture.

### DMARC forensic or failure reports

Forensic or failure reports are supplemental investigation Evidence. They are not universally provided and must not be required for a domain to be considered monitored.

Because they may contain sensitive message-related information, their collection, visibility, storage, transformation, AI exposure, export, and retention require separately resolved Information Guard policy. Absence of forensic reports is not itself a monitoring failure unless a specific contractual or Policy requirement says otherwise.

### Future sources

Potential future sources include Microsoft 365, Exchange Online, Defender for Office 365, Google Workspace, Proofpoint, Inky, Mimecast, transactional email providers, marketing platforms, CRM systems, website hosting, SMTP relays, SIEM systems, DNS providers, and threat-intelligence providers.

A future source is not approved merely because it is listed. Each connector must declare purpose, permissions, supported objects, direction, cadence, failure behavior, source mapping, and Channel policy.

## Sending Source model

An **Email Sending Source** is the contextual identity or role of a system, service, device, vendor, or unresolved origin observed sending for an Internet Domain.

Where possible, it resolves to a canonical Application, Device, Company, or approved service relationship. An unknown source remains an unresolved candidate linked to its observations and Evidence; ITOMS must not guess a canonical match.

Security-specific properties may include:

- authorized, unauthorized, unknown, under-investigation, or retired classification;
- expected SPF, DKIM, and alignment behavior;
- known IP or network ranges and provider identifiers;
- first seen, last seen, volume, and affected Internet Domains;
- responsible party and verification state;
- effective dates and the basis for authorization or retirement.

Authorization is temporal. A source's current authorization must not be used to rewrite whether it was authorized at the time of historical activity.

## Monitoring conditions

The capability may evaluate conditions including:

- DMARC, SPF, DKIM, MX, CNAME, or mail-infrastructure configuration change;
- missing, invalid, weakened, strengthened, or unexpectedly changed policy;
- SPF technical-limit or dependency failure;
- authorized sender authentication or alignment regression;
- new IP, provider, or Sending Source;
- unknown, dormant, or unexpected source activity;
- material volume or failure-rate change;
- legitimate traffic receiving quarantine or reject disposition;
- unexpected policy override;
- aggregate-report interruption or historically active reporter silence;
- enforcement readiness, progression, or regression;
- recurrence of a previously remediated Finding.

Expected changes may remain observations. A Condition becomes a Finding only when evaluation rules and evidence support a conclusion requiring disposition.

## Initial Controls

The capability should support reusable Controls such as:

- DMARC record exists and is syntactically valid.
- DMARC aggregate reporting is configured and actively received.
- SPF exists, is valid, and remains within applicable technical limits.
- Required sending services use DKIM.
- Known Sending Sources authenticate and align according to approved expectations.
- Unknown Sending Sources are investigated and dispositioned.
- DMARC enforcement meets approved organizational Policy.
- DNS and authentication changes are monitored.
- Authentication regressions are remediated and verified.
- Exceptions are documented, approved, scoped, and reviewed.

Controls remain canonical GRC objects. Email-specific evaluation logic references them and produces Evidence; it does not duplicate the Control for each report, dashboard, Assessment, or framework.

## Posture model

Posture is expressed through explainable dimensions rather than only an opaque score:

- DMARC deployment;
- DMARC enforcement;
- SPF health;
- DKIM health;
- authentication alignment;
- authorized-source coverage;
- unknown-source exposure;
- monitoring coverage;
- reporting continuity;
- configuration stability;
- remediation status.

A future score, grade, or certificate may summarize these dimensions only when its formula, evidence, scope, and evaluation time are explainable.

The system must answer why a status exists, what caused it, which Evidence supports it, what must change, who is responsible, when it began, and when it was last verified.

## Hygiene and enforcement progression

The conceptual progression is:

`Discovered → Monitoring Established → Sending Sources Identified → Authentication Baseline Established → Legitimate Sources Corrected → DMARC Enforcement Ready → Quarantine Enforcement → Reject Enforcement → Continuously Verified`

This is guidance, not a rigid universal Workflow. Stages may overlap, repeat, pause, or be inapplicable. `p=reject` alone does not prove strong hygiene; authorization coverage, alignment, reporting continuity, change detection, exceptions, remediation, and historical Evidence remain relevant.

## Enrollment Work Function

Domain enrollment is a guided Work Function:

`Add Domain → Discover Public DNS → Create or Link Internet Domain → Initial Assessment → Determine Reporting Configuration → Propose DNS Change → Verify Observed DNS → Begin Ingestion → Observe Sources → Classify Sources → Generate Findings → Develop Enforcement Plan → Continuous Monitoring`

The progression may branch or pause for ownership verification, customer approval, DNS-provider access, third-party authorization, Information Guard review, missing reports, or unsupported configuration.

The capability may prepare recommended DMARC parameters such as `rua`, `ruf`, `fo`, `pct`, `aspf`, `adkim`, `p`, and `sp`. Recommendations are desired state; separately collected DNS is observed state.

## Finding, alert, Incident, and remediation

A failed or degraded Control evaluation may create Finding `OBJ-FND-0001`. A Finding should reference the Company, Internet Domain, Sending Source, Control, supporting Observations and Evidence, first and last seen times, severity, lifecycle, responsible party, recommended remediation, exceptions, verification, and recurrence as applicable.

A practical Finding workflow may include detection, triage, confirmation, assignment, remediation planning, work in progress, verification, and resolution, while also supporting accepted risk, false positive, expected behavior, granted exception, waiting, and suppression dispositions. The final state machine is not canonically approved and remains a design question.

Alerting uses Attention Item `OBJ-ATT-0001`. Routine aggregate processing should not alert. An alert is created when policy determines that human attention is warranted based on severity, confidence, scope, materiality, change, business importance, and suppression or exception state.

Severity thresholds are configurable rather than permanently hard-coded. Candidate categories include:

- **Critical/Urgent:** unexpected loss of enforcement, major authentication tampering, significant legitimate-mail rejection, or strong evidence of active abuse.
- **High:** high-volume unknown sender, major regression, business-critical sender failure, or major unexpected infrastructure change.
- **Medium:** low-volume unknown sender, recurring failure, degraded configuration, readiness problem, or monitoring interruption.
- **Informational:** expected change, new report provider, small anomaly, or source awaiting classification.

An Incident is a Case `OBJ-CAS-0001` created or classified for security response when circumstances warrant investigation. Incident details remain inside the appropriate security permission boundary. A Finding, Alert, Incident, and Risk remain distinct and linkable.

## Evidence and history

Monitoring must demonstrate that it occurred. Evidence and history may include:

- monitoring start and coverage intervals;
- last successful collection and ingestion history;
- report and DNS observation history;
- configuration and policy changes;
- Control evaluation history;
- Finding, alert, remediation, verification, exception, and approval history;
- enforcement progression and regression;
- source authorization state at the time of activity.

Raw report retention may differ from normalized history and audit evidence. Retention must be policy-driven, particularly for forensic reports. Prohibited values must not be retained merely to prove enforcement.

## Context, permissions, and presentation

The same canonical information may produce different Workspaces through Effective Context.

- A customer executive may see protection status, monitoring coverage, meaningful Findings, remediation progress, and an evidence-backed summary.
- A customer administrator may see authorized sources, required DNS changes, and assigned work permitted to that role.
- A technician may see source resolution, evaluation detail, remediation steps, and external-system links.
- A security analyst may see restricted Evidence, investigation material, and Incident context when authorized.
- An MSP operator may see fleet posture across customers while tenant isolation remains enforced.

A broadly visible Internet Domain may show Security Status, active Finding count, Incident indicator, last review, and monitoring status without revealing restricted forensic reports, message-related data, analyst notes, indicators, or investigation records.

## Work-first and administrative experiences

The primary experience presents meaningful work such as:

- review or approve a new Sending Source;
- investigate authentication regression or DNS change;
- correct SPF or configure and verify DKIM;
- prepare a domain for enforcement;
- review enforcement readiness or stale reporting;
- remediate and verify a domain-security Finding.

Appropriately authorized object-centric views may expose Internet Domains, observations, Controls, evaluation state, Findings, aggregate reports, evidence, and configuration. The final Work Mode and Data Mode labels and access rules require future Interface Architecture approval.

Conceptual views include Security Monitoring Overview, Email & Domain Security Dashboard, Domain List and Detail, Authentication Overview, Sending Sources, DMARC Reporting, SPF Analysis, DKIM Analysis, DNS Change History, Observations, Findings, Alerts, Incidents, Evidence, Exceptions, Monitoring Configuration, Domain Enrollment, MSP Fleet View, Executive Summary, Enforcement Readiness, and Historical Timeline.

These are view requirements, not a final navigation tree or screen layout.

## MSP and customer reporting

MSP fleet views may summarize monitored and unmonitored domains, missing DMARC, enforcement policy, authentication failures, unknown sources, active Findings, stale reporting, enforcement readiness, and regressions. Drill-down follows Effective Context from provider to customer to Internet Domain to Sending Source to Observation, Finding, or Evidence.

Customer and educational outputs may include Email Domain Health Check, Email Authentication Assessment, Domain Security Report, monthly or executive summary, enforcement-readiness report, Sending Source inventory, and an evidence-backed attestation-style summary.

Claims must be supported by measurable operational facts. The capability must not claim that DMARC eliminates phishing or offer a certificate whose scope and evidence cannot be explained.

## Assessment and GRC consumption

An assessment experience, including a future Lookout capability if canonically approved, may discover an Internet Domain, run an initial Assessment, create Findings, and transition the same canonical records into ongoing monitoring. It must not create separate Lookout versions of domains, SPF, DKIM, DMARC, sources, Findings, or Evidence.

GRC references operational Evidence and evaluation history. For example, a Control requiring active DMARC aggregate monitoring may be verified by continuous report receipt over an approved interval. The same Evidence supports operations, customer reporting, Assessment, audit, and compliance uses subject to Permissions.

## Knowledge-base content plan

The Knowledge Base should use the same canonical concepts, Controls, and terminology. Planned topics include:

- SPF, DKIM, DMARC, and why SPF alone does not stop spoofing;
- alignment and DMARC policies `none`, `quarantine`, and `reject`;
- aggregate and forensic reports, RUA versus RUF, and reporting configuration;
- reading aggregate XML and identifying legitimate Sending Sources;
- unknown sources, third-party providers, and safely onboarding or retiring a sender;
- SPF DNS lookup limits and forwarding limitations;
- DKIM selectors and key rotation;
- enforcement progression and why `p=reject` is not the entire objective;
- DNS and authentication change monitoring;
- investigating failures and responding to an email-domain security Incident;
- continuous monitoring, historical Evidence, and executive explanation.

## Logical service responsibilities

Implementation architecture should preserve separable responsibilities for:

- enrollment and canonical subject resolution;
- DNS collection and change observation;
- aggregate and approved forensic-report receipt;
- deterministic parsing, normalization, and provenance;
- source and entity resolution;
- Control evaluation, condition, and posture history;
- Finding and Attention Item decisions;
- Work Session, remediation, exception, and verification orchestration;
- Evidence, reporting, and GRC reference;
- System Settings, collection health, Information Guard, and audit.

These are logical responsibilities, not prescribed deployment services or technology choices.

## Cross-references

- [Context Architecture](../context-architecture.md)
- [Work Architecture](../work-architecture.md)
- [Asset Architecture](../asset-architecture.md)
- [System Settings Architecture](../system-settings-architecture.md)
- [Information and Data Model](../08-ITOMS_INFORMATION_AND_DATA_MODEL.md)
- [Workflow Model](../07-ITOMS_WORKFLOW_MODEL.md)
- [Integration, Security, and Governance](../11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md)
- [Design-to-Implementation Governance](../design-to-implementation-governance.md)
- [Design Register](../12-ITOMS_DESIGN_REGISTER.md)

## Design-readiness boundary

An Engineering Work Package must not be approved until the open monitoring questions in the Design Register that affect its scope have been resolved or explicitly excluded. At minimum, an implementation package must cite the canonical data boundary, retention and Information Guard policy, evaluation rules, Finding lifecycle, authorization boundary, and acceptance evidence it implements.
