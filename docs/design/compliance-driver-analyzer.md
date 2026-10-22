# Compliance Driver Analyzer Design Handoff

**Status:** Proposed

**Purpose:** Define the ITOMS Compliance Driver Analyzer as a private-enclave intake, interpretation, communication, and service-coverage capability that discovers why an organization has security obligations, translates those obligations into plain business language, and connects them to actionable requirements, controls, responsibilities, and service coverage.

## Core product decision

The Compliance Driver Analyzer is not a generic compliance score and is not the primary ITOMS security-posture experience.

Its primary question is:

> **Why does this organization need to do these particular security things?**

The Analyzer discovers external and business drivers, interprets them, establishes provenance and certainty, and feeds structured results into the canonical ITOMS GRC graph.

Customer-facing ITOMS can continue to focus on:

- where the organization is now;
- what needs attention;
- what is already being done;
- what should happen next.

The Driver Analyzer supplies the reason behind those recommendations.

## Business role

The capability has three simultaneous roles:

1. **Requirements discovery** — identify obligations or likely obligations arising from contracts, business relationships, audits, insurance, regulation, or business practices.
2. **Translation and communication** — explain source language in terms an ordinary business owner or manager can understand.
3. **Sales and service alignment** — show which requirements are already addressed by the customer's subscribed services, which require additional capabilities, and which remain the customer's or another party's responsibility.

The Analyzer must not manufacture demand or treat every gap as an upsell. Source evidence and applicability drive recommendations.

Possible outcomes include:

- already addressed by the customer's current service;
- requires a capability included in another service tier;
- available as an add-on or project;
- customer organizational responsibility;
- third-party or legal responsibility;
- potential requirement requiring validation;
- insufficient information to determine applicability.

## Content Driver Case and primary case types

Analysis begins with a **Content Driver Case**: the governed container that records why ITOMS is reviewing a situation before individual Sources are analyzed. The Case is distinct from a document. One continuing business situation may accumulate multiple Sources over time.

All case types share a common structure, while case type controls intake questions, source handling, authority assumptions, analysis rules, certainty, and expected outputs.

The nine initial case/intake types are:

1. **Customer / Vendor Contract** — commercial agreements containing security, privacy, confidentiality, insurance, data-handling, technology, or operational obligations.
2. **Partnership / Business Agreement** — partnership, subcontractor, joint-venture, business-associate, data-sharing, mutual restriction/non-compete, or similar relationship agreements.
3. **Employment / Employer Agreement** — agreements imposing obligations involving employee information, confidentiality, access, systems, intellectual property, privacy, or security practices.
4. **Request for Proposal / Bid Requirement** — RFPs, RFQs, procurement requirements, bid packages, prequalification material, and related security questionnaires.
5. **IT / Security Audit or Assessment** — audit reports, customer assessments, penetration-test findings, third-party assessments, assessment responses, or similar findings. Assessment context and possible commercial interests inform scrutiny but do not determine whether an individual finding is valid.
6. **Regulatory / Government Requirement** — regulatory, government, contractual flow-down, or industry obligations. Mention of a framework alone does not prove applicability.
7. **Cyber Insurance Requirement** — applications, renewal questionnaires, underwriting requirements, coverage conditions, exclusions, attestations, and required safeguards.
8. **Questionnaire / Discovery** — structured customer or prospect discovery that can originate potential Drivers when no authoritative source document exists. Self-reported or inferred information retains its lower certainty until validated.
9. **Framework Adoption / Desired Compliance** — an organization voluntarily selects a framework, standard, profile, or security baseline as a target even when no external counterparty currently requires it. The initiating Driver is organizational intent. If a later contract, regulation, insurer, or other authority makes the same outcome mandatory, ITOMS adds the new Driver and authority rather than rewriting the original history.

Additional case types may be added without creating separate compliance silos.

### Case Context

Before Source Analysis, ITOMS performs **Case Framing**. Case Context answers: **What is going on, why are we looking at it, and what decision are we trying to make?**

The common Case Context should capture:

- case identity, organization, case type, status, owner, initiator, sensitivity, and important dates;
- purpose, trigger/event, why the review is occurring now, and the **Decision Sought**;
- parties and their roles and relationships to the organization;
- relationship context, including current/proposed/renewing/terminating/disputed status and known commercial interests or incentives when relevant;
- the original human narrative and subsequent attributable additions or corrections;
- structured Context Statements classified as **Fact**, **Reported Statement**, **User Assertion**, **Opinion / Concern**, **AI Inference**, or **Unknown**;
- attribution, provenance, confidence, validation state, effective dates, and history for each material Context Statement;
- goals, concerns, perceived consequences, constraints, deadlines, dependencies, and handling restrictions;
- questions and unknowns discovered during intake or analysis;
- linked Sources and source classifications;
- confidentiality, access, retention, and AI-processing restrictions;
- a versioned AI-generated Case Context Summary derived from the underlying structured context.

The original narrative is preserved. The AI summary is a derived human-readable view, not the database truth. AI may extract and maintain structured Context Statements, but inference must not silently become fact.

Core rule:

> **Case Context informs analysis. Source Evidence establishes what the Sources say. Neither is allowed to overwrite the other.**

Conceptually:

`Human Narrative → AI Context Extraction → Structured Context Statements → Case Context Summary`

followed by:

`Case Context + Sources → Analysis → Drivers → Required Outcomes / Requirements → Controls → Control Implementations → Service Linkage`

Drivers, Controls, Findings, Service Linkages, and work are related downstream objects; they are not embedded fields inside Case Context.

### Source handling

A Source is evidence or input attached to the Case, such as a contract, audit, insurance policy, questionnaire, email, meeting note, verbal statement, or authoritative reference. Multiple Sources may attach to one Case, and a customer may have multiple Cases whose Drivers converge on the same Required Outcome or Control.

Raw confidential Sources remain subject to the private-enclave boundary and role-based access. Derived Context Statements and Drivers retain provenance pointers rather than requiring unrestricted copies of source material.

### No-document intake

When no authoritative document is available, ITOMS uses questionnaire-driven discovery. Two separate questionnaire experiences feed the same Driver Analyzer but have different language, workflows, and certainty rules.

## Questionnaire instance 1: Customer Requirements Discovery

**Audience:** Existing customer.

**Purpose:** Directly identify, validate, and maintain known or suspected requirements for an organization with an established ITOMS/customer relationship.

Because a trusted relationship already exists, questions may explicitly reference contracts, audits, cyber insurance, regulatory requirements, frameworks, customer questionnaires, CMMC, DFARS, HIPAA, PCI, and other known terminology when useful.

### Workflow

`Known Customer → Direct Requirements Questionnaire → Identify Drivers → Validate Evidence → Map Requirements → Compare Against Current Services → Identify Gaps → Customer Review → Action Plan`

### Expected question areas

- contractual cybersecurity or technology requirements;
- customer or vendor security questionnaires;
- government or subcontract work;
- regulated or sensitive data;
- known frameworks or standards;
- prior audits and findings;
- cyber-insurance applications and control requirements;
- legal or contractual review findings;
- customer portals and data exchange;
- existing attestations or representations;
- current and planned business relationships that may introduce new obligations.

### Existing-customer advantage

This workflow can compare discovered requirements against known ITOMS context, including subscribed services, existing controls, implementations, evidence, findings, projects, and planned work.

A result can therefore distinguish:

- requirement already addressed through IT Essentials;
- requirement addressed through another current service;
- capability not included in the current subscription;
- capability available through IT Advanced or another defined offering;
- organizational/process responsibility outside the MSP service;
- requirement requiring evidence or reassessment;
- requirement whose applicability remains unresolved.

## Questionnaire instance 2: Business Security Requirements Discovery

**Audience:** General prospect, business owner, manager, or other nontechnical participant.

**Purpose:** Discover likely security and business requirements without expecting the participant to understand compliance terminology.

This is both a lead-generation/customer-education experience and an input to service-package guidance.

### Language rule

The participant answers questions about **how the business operates**. The Analyzer determines which compliance, contractual, regulatory, insurance, and security questions those answers imply.

Avoid requiring the prospect to understand terms such as DFARS, CMMC, NIST, control families, or regulatory citations.

Questions should sound like a knowledgeable business advisor, for example:

- What does your company do and who do you primarily do business with?
- Do you work with hospitals, doctors, clinics, pharmacies, or healthcare organizations?
- Do you perform work for federal, state, or local government, directly or through another contractor?
- Do customers send contracts containing requirements about computers, security, confidentiality, or protecting information?
- Do customers ask you to complete security questionnaires?
- Do employees use customer portals to upload or download files?
- Do customers give you information they consider confidential?
- Do you handle employee records, Social Security numbers, financial information, medical information, drawings, designs, or other sensitive information?
- Do you accept or process credit-card payments?
- Have you participated in an IT, security, customer, financial, or insurance audit?
- Has a customer required an IT or security change before doing business with you?
- Does the word “compliance” come up with customers, vendors, insurers, auditors, or attorneys even if you are unsure what it means?
- Do you carry cybersecurity insurance?
- Does your insurer ask about MFA, backups, training, antivirus, monitoring, or other IT practices?
- Do you have legal counsel who reviews business contracts?
- Has legal counsel raised concerns involving technology, privacy, cybersecurity, or customer information?
- Have you signed technology or security requirements you were not completely sure the business was meeting?

### Conditional branching

Follow-up questions should be driven by prior answers.

Example:

`Government work = Yes → Prime or subcontractor? → Receives technical files/drawings/specifications? → How are those files received/stored/shared? → Internal applicability investigation`

The prospect should not need to know whether DFARS or CMMC applies. ITOMS should use their business facts to identify that these may be relevant and require validation.

### Workflow

`Prospect → Business-Language Questionnaire → Discover Potential Drivers → Conditional Follow-ups → Infer Likely Requirements → Map Likely Service Coverage → Prospect Report → Sales Follow-up`

### Marketing role

Possible public-facing positioning includes:

- **What security requirements apply to your business?**
- **Do your customers expect more from your IT than you realize?**
- **Find out what your customers, contracts, and insurance may require from your IT.**

The experience should provide value before a sales conversation. It may summarize potential drivers, likely security needs, unresolved questions, and service coverage that could address them.

## Certainty and applicability model

The two questionnaire instances must not overstate certainty.

### Existing customer / verified source

When authoritative source material or validated evidence establishes applicability, ITOMS may use language such as:

- Required
- Applicable
- Contractually required
- Verified requirement

### Prospect / inferred source

Questionnaire inference should use language such as:

- Likely requirement
- Potential requirement
- May apply
- Needs confirmation
- Additional information required

An inferred requirement must not silently become a verified obligation.

Applicability, provenance, source, interpretation, and validation state must remain traceable.

## Analyzer pipeline

Document and questionnaire intake converge into a common conceptual pipeline:

`Content Driver Case → Case Framing / Context → Sources / Questionnaire → Driver Analysis → Applicability & Certainty → Plain-Language Interpretation → Required Outcome / Requirement Mapping → Control Mapping → Coverage / Gap Analysis → Responsibility & Service Mapping → Customer-Facing Output → Work`

For document-driven analysis:

`Contract / RFP / Audit / Insurance Source → Analyzer → Drivers → Requirements / Controls → Current ITOMS Posture → Gaps / Actions`

For questionnaire-driven analysis:

`Questionnaire → Analyzer → Potential or Confirmed Drivers → Requirements / Controls → Current or Prospect Coverage → Gaps / Actions`

## Customer-facing requirement record

The customer communication experience should be able to present each material item as:

- **Required by / Driven by:** source and location when available;
- **What it means:** plain-business-language interpretation;
- **Why it applies:** applicability rationale;
- **Certainty:** verified, likely, potential, unresolved, etc.;
- **Current status:** addressed, partial, missing, not assessed, or unresolved as appropriate;
- **What you already have:** current service/control coverage;
- **What is needed:** capability, process, evidence, decision, or implementation;
- **Responsibility:** MSP, customer, shared, third party, legal, assessor, or unresolved;
- **Available through:** current service, higher service tier, add-on/project, customer action, or external provider;
- **Next action:** review, validate, subscribe, implement, document, assess, or otherwise disposition.

A useful customer communication pattern is:

`Source says → Plain English → Current coverage → Gap → Required action → Service / responsibility that addresses it`

## Service linkage and service-package mapping

Service linkage is a durable, bidirectional explanatory relationship connecting the customer's requirements graph to the services that implement it. It is not proof of compliance.

The working chain is:

`Case → Source → Driver → Required Outcome / Requirement → Control → Control Implementation → Service Capability → Customer Service Entitlement → Service Package`

Evidence and Assessment remain attached to the applicable Control Implementation and assessment scope. A subscription or package assignment never substitutes for implementation Evidence or an approved Assessment.

The linkage must support both directions:

- **Why is this service needed?** Trace from a Service Capability backward through the Control Implementation, Control, Required Outcome / Requirement, Driver, Case, and authorized source provenance.
- **How is this requirement being addressed?** Trace from a Driver or Required Outcome forward through the Control and Control Implementation to the Service Capability and the customer's current entitlement.
- **What is not covered?** Identify required capabilities with no current customer entitlement, without treating that gap as proof that a Control is unsatisfied until implementation and Evidence are assessed.

Service Capability is the stable delivery concept. Service Package is a commercial grouping or entitlement mechanism and may change over time. Therefore, package membership must not be embedded as permanent truth on a Control or Driver.

Service Linkage relationships must be effective-dated and historically reconstructable. At minimum they must preserve the customer/scope, linked Control Implementation, Service Capability, entitlement/package through which it was delivered, provider/responsible party, relationship status, effective period, provenance, and change history. Moving a capability between IT Essentials, IT Advanced, an add-on, or another offering must not rewrite what service coverage existed at an earlier date.

The Analyzer may show that a capability required to address a driver is:

- included in IT Essentials;
- included in IT Advanced;
- included in another defined service package;
- separately purchasable;
- project-based;
- not provided by the MSP;
- an internal customer responsibility.

The design must prevent optional services from appearing already included and prevent subscription status from being treated as evidence that a requirement is satisfied.

The strongest sales communication is source-driven:

> The customer's business obligation creates the need. The service recommendation explains how that need can be addressed.

## Prospect service guidance

The external questionnaire may function as a service-package configurator, but recommendations must remain explainable at the capability level.

Example output pattern:

> Your business profile suggests 11 security needs. Six appear covered by IT Essentials, four require capabilities available in IT Advanced, and one requires additional review because it may be a contractual obligation.

Counts and package names are dynamic examples, not fixed product claims.

The report should allow the prospect to understand **why** a package is suggested rather than simply producing a package score.

## Private-enclave boundary

Document analysis should operate inside a dedicated private analysis enclave.

Raw contracts, RFPs, audit material, insurance documents, and potentially sensitive questionnaire responses should not automatically become broadly available ITOMS records.

The enclave should:

- receive and process source material;
- preserve source provenance and controlled access;
- extract candidate drivers and requirement statements;
- produce plain-language interpretations;
- identify applicability questions and confidence/certainty;
- allow human validation where required;
- emit only governed structured findings and references needed by the broader ITOMS graph.

The main ITOMS environment should consume structured Driver/Requirement relationships, provenance references, applicability state, and approved interpretations without requiring unrestricted replication of source documents.

Final retention, encryption, key-management, isolation, deletion, model-processing, and source-document access policies require a dedicated security design before implementation.

## Relationship to canonical GRC architecture

The Driver Analyzer extends, rather than replaces, the existing GRC chain:

`Framework → Requirement ↔ Control → Control Implementation → Evidence → Assessment → Finding → Remediation`

It introduces an upstream discovery and applicability concern:

`Business / External Driver → Applicability → Framework and/or Requirement → Control ...`

A Driver may originate from a contract, RFP, business relationship, audit, insurer, regulation, customer expectation, questionnaire inference, or an organization's voluntary Framework Adoption / Desired Compliance decision.

A Driver does not prove that a Control is implemented or that a Requirement is satisfied.

The final canonical object/relationship decision for Driver, Source Document, Applicability Decision, and Service Coverage Mapping must be reconciled with `ITOMS_CANONICAL_RULES.md`, `itoms_objects.csv`, and `itoms_schema.csv` before engineering implementation.

## Relationship to Work Architecture

Analyzer findings should be actionable without collapsing analysis into Tasks.

Possible transitions include:

- request missing source material;
- obtain legal/customer clarification;
- validate applicability;
- review interpretation;
- map or confirm a Control;
- gather Evidence;
- perform an Assessment;
- propose a Remediation;
- recommend a service change;
- create a Project;
- create or coordinate Tasks;
- record customer acceptance, deferral, rejection, or alternative treatment.

Work Sessions preserve the business reason and source provenance as the item moves from discovery through decision and implementation.

## Separation of concerns

The implementation should preserve three distinguishable capabilities:

### 1. Driver Analyzer

Discovers and interprets the external or business reason for a requirement.

### 2. Coverage / Gap Engine

Compares applicable requirements and needed capabilities with the organization's actual controls, evidence, posture, responsibilities, and subscribed services.

### 3. Driver Report / Customer Communication

Explains why something is required, what it means, where the organization stands, who is responsible, and what action or service can address it.

These may share UI and data but should not be collapsed into one opaque scoring mechanism.

## Initial implementation boundary

A first implementation should support:

- source-type selection;
- secure source-document intake;
- two questionnaire instances with independent workflows;
- conditional question branching;
- driver extraction;
- plain-language interpretation;
- applicability and certainty states;
- human validation;
- requirement/control mapping;
- service-package and responsibility mapping;
- current-service comparison for known customers;
- prospect-oriented service guidance;
- customer/prospect Driver Report;
- transition to GRC assessment/remediation/work;
- provenance and audit history.

Automatic legal conclusions, automatic certification claims, and automatic conversion of inferred prospect requirements into verified obligations are explicitly out of scope.

## Open design decisions

The proposed [Canonical Ontology v1](canonical-ontology-v1.md) and [Atlas ↔ ITOMS contract](atlas-itoms-schema-contract-v1.md), under [ADR-0010](../../adr/ADR-0010-canonical-ontology-and-atlas-contract.md), reconcile Content Driver Case to Case `OBJ-CAS-0001`, Source to Evidence `OBJ-EVD-0001`, and Case Context Statement to Observation `OBJ-OBS-0001`. They propose Compliance Driver `OBJ-DRV-0001` in the existing registries, with applicability/adoption represented as versioned relationship/result records. These decisions remain proposed until review; they do not silently close the other questions below. DR-011 tracks implementation gates, including service/work identities, review policy, and enclave security. Atlas supplies pinned reusable knowledge to the private Analyzer; it does not receive raw Case context or approve tenant obligations.

1. What canonical object and relationship IDs represent **Content Driver Case**, **Case Context Statement**, **Driver**, and their effective-dated provenance in `itoms_objects.csv` and `itoms_schema.csv`?
2. What canonical object represents a source contract/RFP when the raw document remains enclave-restricted?
3. What certainty/applicability states should be canonical?
4. How are interpretations approved, superseded, and historically reconstructed?
5. What canonical objects and relationship IDs represent Service Capability, Customer Service Entitlement, and effective-dated Service Linkage in `itoms_objects.csv` and `itoms_schema.csv`?
6. Which prospect questionnaire answers may be retained after conversion to a customer?
7. What is the handoff process from marketing lead to customer onboarding without overstating inferred obligations?
8. What human review is mandatory before a document-derived requirement becomes authoritative?
9. What security and retention controls govern enclave source material?
10. Which Driver Report elements are visible to customer users versus MSP/internal roles?
11. What controlled vocabulary and lifecycle should govern the nine initial Content Driver Case types?
12. Which Case Context classifications require human validation before they may influence authoritative analysis?

## Validation questions

1. Can every recommendation explain the business or external driver that caused it?
2. Can the customer see what a source requirement means without reading compliance jargon?
3. Can ITOMS distinguish verified requirements from inferred prospect requirements?
4. Can a capability be shown as available in IT Advanced without implying that the customer already receives it?
5. Can a requirement be assigned to the customer or a third party rather than automatically becoming an MSP sales item?
6. Can the same underlying engine support both direct customer discovery and nontechnical prospect discovery?
7. Can source documents remain restricted while structured, approved findings participate in the wider ITOMS graph?
8. Can service-package or entitlement changes occur without destroying historical Service Linkage or changing prior assessment truth?
9. Can a prospect understand why a service package is suggested?
10. Can an identified driver transition cleanly into assessment, remediation, Projects, and Tasks while preserving provenance?
