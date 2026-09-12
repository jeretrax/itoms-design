# ITOMS System Settings Architecture

**Status:** Proposed

**Purpose:** Define System Settings as the configuration and enforcement control plane of an ITOMS installation, including the Information Guard realm and its AI Sentinel capability.

## Core rule

System Settings is the control plane that determines how an ITOMS installation is configured, governed, connected, secured, operated, and allowed to act. It supplies policy and configuration to canonical services, Context Architecture, Work Architecture, interfaces, integrations, agents, automation, and platform operations.

System Settings does not become a competing system of record. It controls how canonical information and capabilities may be collected, interpreted, exposed, retained, transmitted, or acted upon. Configuration changes are versioned, attributable, scope-aware, and auditable when material.

## Control plane and operational data

System Settings contains or governs:

- installation, provider, tenant, organization, location, channel, capability, and other scoped configuration;
- policy definitions, defaults, assignments, exceptions, and effective dates;
- configuration validation, publication, enforcement, and rollback state;
- administrative authority and separation of responsibility;
- references to secrets held in an approved secret store;
- audit events explaining material configuration and policy decisions.

System Settings must not absorb ordinary business records merely because those records influence a policy. Canonical Data remains the record of what exists or existed. Effective Context resolves the circumstances in which an actor operates. Work Architecture coordinates what is being performed. System Settings provides the governing configuration used by those architectures.

## Configuration scope

Configuration must be capable of applying at installation, service-provider, tenant, organization, location, Channel, capability, integration, agent, workflow, data class, purpose, execution-environment, or similarly justified scope.

Standard control-plane metadata should include placeholders for:

- stable setting or policy identifier;
- setting version and lifecycle state;
- owning administrative scope;
- applicable scope and target selector;
- effective start and end;
- default or inherited value;
- explicit override or exception;
- source, author, approver, and change reason;
- validation and publication state;
- last evaluation and enforcement result;
- related evidence and audit events.

The final inheritance and precedence algorithm is intentionally not defined here. Until approved, implementations must fail closed where ambiguity could expose restricted information or authorize an action.

## Configuration realms

System Settings is divided into cross-cutting **configuration realms**. A realm groups related controls and administrative responsibilities. It is not a feature module, canonical Domain, Lens, or authorization grant.

### 1. Information Guard

Information governance, Channel policy, classification, handling, retention, AI exposure, exceptions, and enforcement. Information Guard is defined in detail below.

### 2. Identity and access

Authentication methods, identity providers, federation, account lifecycle, roles, group mappings, delegated administration, capability permissions, conditional access inputs, session controls, break-glass access, and privileged-action requirements.

Placeholders should support common provider and customer administrator scopes without predetermining their final boundary.

### 3. Integrations and connections

Connector definitions, authorization grants, external accounts and tenants, supported objects, direction, cadence, webhooks, synchronization scope, source mappings, health, failure behavior, rate limits, and secret references.

Connector configuration describes how ITOMS reaches and exchanges data with a system. Channel configuration describes the policy boundary under which information enters, leaves, or is interacted with. They are related but not interchangeable.

### 4. AI and intelligence infrastructure

Approved AI providers and models, execution environments, routing, semantic services, embeddings, retrieval, prompt and tool boundaries, model availability, evaluation, cost controls, observability, and fallback behavior.

AI provider qualification and final routing rules remain open design decisions. Information Guard and AI Sentinel always constrain this realm.

### 5. Automation and execution

Job runners, schedules, queues, concurrency, retries, timeouts, approval gates, service identities, execution environments, scripts, tool permissions, failure handling, rollback, and change windows.

Automation configuration never creates authority by itself. Each Action remains subject to Capabilities, Permissions, Effective Context, Information Guard, and Work Architecture.

### 6. Work configuration

Work Function availability, Workflow and Process Templates, Stage and Task defaults, Work Session behavior, Suggested Next Action policy, handoffs, exceptions, completion rules, ownership defaults, calendars, service boundaries, and escalation paths.

The definitions and runtime behavior remain governed by [Work Architecture](work-architecture.md); this realm only configures them.

### 7. Canonical data and relationships

Canonical metadata publication, schema extensions, user-defined fields, relationship rules, source authority, reconciliation thresholds, matching policy, lifecycle, archival, retention hooks, temporal behavior, and data-quality requirements.

Configuration may influence validation and applicability but cannot redefine canonical identity or destroy historical truth. See [Context Architecture](context-architecture.md) and [Asset Architecture](asset-architecture.md).

### 8. Communications

Email, SMS, Teams, Slack, WhatsApp, native notification, templates, sender identities, inbound routing, consent, delivery policy, quiet hours, escalation, message retention, and Channel-specific handling.

Communications configuration governs delivery and interaction behavior. Information Guard separately determines which information may be collected, transmitted, retained, or exposed to AI through each communication Channel.

### 9. Agents and edge infrastructure

Collectors, endpoint applications, Site Admin Boxes, gateways, relays, local processing, enrollment, certificates, update rings, health, buffering, offline behavior, command authority, telemetry, and data-forwarding constraints.

Agent or edge placement does not create ownership or information rights. Asset ownership and deployment follow [Asset Architecture](asset-architecture.md).

### 10. Audit, evidence, and compliance

Audit-event policy, evidence capture, integrity, timestamps, actor attribution, retention, legal hold, export, review, framework mappings, control verification, exception evidence, and reporting scope.

Auditability does not justify retaining prohibited raw values. Information Guard may require an audit event that records the policy decision, category, time, Channel, actor or workload, and disposition without storing the prohibited content.

### 11. Platform operations

Tenant provisioning, regions, residency, storage, encryption, keys, backups, recovery, availability, monitoring, capacity, quotas, licensing, feature release, maintenance windows, support access, import/export, deletion workflows, and installation health.

Defaults should follow common secure operating practice, but product-specific values remain placeholders until implementation requirements are approved.

## Information Guard

**Information Guard** is the core configuration and enforcement realm governing how information may be collected, classified, handled, transformed, retained, transmitted, disclosed, processed by AI, excepted, and audited.

Information Guard applies across native interfaces, integrations, communications, agents, collectors, automation, AI execution, imports, exports, evidence, and administrative tools. It is not limited to AI and is not merely a DLP feature.

### Information Guard policy concerns

An Information Guard policy may address:

- Channel and direction of information flow;
- information owner, custodian, source, and affected organization;
- classification and detected information category;
- collection purpose and permitted secondary purposes;
- allowed canonical destination or prohibition on persistence;
- sanitization, minimization, redaction, tokenization, masking, or destruction;
- retention period, legal hold, export, and deletion requirements;
- AI eligibility, approved execution environment, provider, model class, and transformation;
- human review, approval, exception, and escalation;
- audit event and evidence requirements.

Policy evaluation must consider, at minimum, Channel, ownership, custody, classification, purpose, execution environment, and retention. Effective Context, Capability, Permission, tenant boundary, and applicable regulatory or contractual conditions are additional inputs where relevant.

### Restrictive default posture

Information Guard is deny-safe and purpose-limited:

1. Collect only the minimum information required for an approved purpose.
2. Sanitize as early as practical, preferably at the Channel or trusted edge.
3. Destroy prohibited values before persistence or AI exposure.
4. Do not reuse collected information for a new purpose without an applicable policy basis.
5. Retain audit events about enforcement without retaining prohibited raw values.
6. Permit exceptions only when they are narrow, scoped, attributable, time-bound where appropriate, and tied to a defined purpose and Capability.
7. Treat missing, conflicting, or indeterminate policy as denial when disclosure, persistence, or execution could increase risk.

Broad installation-wide “allow AI” or “allow collection” switches are insufficient authorization. More permissive policy must be explicitly scoped.

## Channel

A **Channel** is an identifiable ingestion or interaction boundary for which collection, handling, retention, transmission, and AI-processing policy may differ.

A Channel is defined by the meaningful policy boundary, not merely by brand name or transport protocol. One application may expose several Channels when its flows have materially different purposes or handling requirements. Several technical transports may share a Channel only when their effective policy is intentionally identical.

Current Channel candidates include:

| Channel | Boundary and policy concern |
| --- | --- |
| ITOMS backend AI invocation | Server-side request to an AI execution environment, including prompts, retrieved context, tool results, and model output. |
| ITOMS mobile app submission | User-submitted voice, text, photo, video, document, metadata, or form content entering through the mobile application. |
| Windows endpoint app | Endpoint capture, interaction, telemetry, support request, local processing, and device-originated submission. |
| ITOMS native chat | Conversation and attachments handled inside the ITOMS experience. |
| SMS | External messaging with carrier and provider handling, sender identity, consent, and message-retention implications. |
| Microsoft Teams | External collaboration messages, files, threads, identities, tenant boundaries, and app permissions. |
| Slack | External collaboration messages, files, threads, workspace boundaries, and app permissions. |
| WhatsApp | External messaging with provider, identity, consent, media, and retention implications. |
| Technical collector | Network, endpoint, security, backup, inventory, or other collector output where source, sensitivity, local filtering, or execution policy warrants a distinct boundary. |

This list is a working taxonomy, not a final closed enumeration. Email, API clients, web forms, file imports, webhooks, and other interfaces may require distinct Channels after design review.

### Channel and Connector reconciliation

A **Connector** is the configured technical integration with an external system. It declares purpose, permissions, supported objects, direction, cadence, failure behavior, source mappings, and health according to the existing integration model.

A **Channel** is the Information Guard policy boundary through which an interaction or information flow occurs.

- A Connector may expose multiple Channels, such as inbound messages, outbound notifications, file retrieval, directory synchronization, and AI-assisted interpretation.
- A Channel may use one or more Connectors or native services.
- Connector authorization does not imply permission to persist, disclose, or process all accessible information.
- Channel policy does not replace connector authentication, synchronization, mapping, or health configuration.
- Every ingestion or interaction path must resolve to a Channel policy before prohibited values are persisted or exposed to AI.

## AI Sentinel

**AI Sentinel** is the Information Guard capability that governs whether and how information may be processed by AI.

AI Sentinel evaluates the proposed AI operation against Information Guard policy and the resolved inputs, including Channel, information ownership and custody, classification, purpose, requested Capability, execution environment, retention, and applicable Effective Context.

AI Sentinel may:

- deny AI processing;
- allow only deterministic processing;
- require minimization, redaction, masking, tokenization, or local preprocessing;
- restrict execution to an approved environment, provider, model class, region, or retention posture;
- limit retrieved context, tools, output destinations, or follow-on Actions;
- require human approval or a narrow exception;
- record an auditable decision without retaining prohibited content.

AI Sentinel does not own canonical data, determine business truth, or replace Permissions. It enforces the AI-processing portion of Information Guard.

## AI execution principle

**Deterministic first, AI where it adds semantic value, and never let AI become the system of record.**

Deterministic logic should perform known validation, parsing, filtering, routing, policy evaluation, exact transformation, and state changes when rules can reliably express the requirement. AI may summarize, classify, extract, interpret, correlate, explain, draft, or recommend when semantic reasoning materially improves the result.

AI output remains an assertion, proposal, observation, or derived result until the appropriate deterministic validation, user decision, Workflow Action, or authorized service writes canonical state. ITOMS owns canonical identity, relationships, lifecycle, provenance, and history.

## Exceptions

An Information Guard exception must be narrower than the rule it changes. It should identify the purpose, Capability, information category, Channel, actor or workload, organization or tenant, execution environment, permitted handling, expiration or review condition, approver, reason, and required audit evidence.

An exception must not silently create a general allow rule, override tenant isolation, transfer information rights, or erase the underlying policy decision. Emergency use must remain attributable and reviewable.

## Auditability without prohibited retention

Enforcement records should capture enough information to explain what occurred without reproducing prohibited content. A standard audit-event placeholder may include:

- policy and version;
- Channel and direction;
- actor, agent, integration, or workload identity;
- tenant and applicable scope;
- detected category or classification, not the prohibited value;
- purpose and requested Capability;
- decision and transformations applied;
- execution environment class;
- timestamp, correlation identifier, and outcome;
- exception reference when used.

Hashes, fingerprints, excerpts, or reversible tokens are not automatically safe substitutes. Their use requires policy approval based on the information and threat model.

## Design philosophy additions

- **Collection does not imply permission for AI processing.** Access to or ingestion of information authorizes only the approved collection purpose and handling policy.
- **Local processing does not grant information rights.** Running on an endpoint, Site Admin Box, customer network, private tenant, or self-hosted installation does not change ownership, custody, confidentiality, purpose limitation, or authorization.
- **AI is not canonical truth.** AI can interpret and recommend; canonical state changes occur through attributable, governed Actions.
- **Sanitize before expansion.** Minimize and remove prohibited content before persistence, transmission, indexing, retrieval, logging, or AI exposure whenever practical.
- **Exceptions are narrow.** Purpose- and Capability-scoped exceptions are preferable to broad allow switches.
- **Audit the decision, not the prohibited secret.** Preserve proof of enforcement without retaining raw values that policy requires destroyed.

## Cross-architecture boundaries

- [Context Architecture](context-architecture.md) resolves the actor, organization, relationships, roles, Lens, Capabilities, Permissions, engagement, time, and other circumstances. System Settings supplies applicable policy but does not redefine Effective Context.
- [Work Architecture](work-architecture.md) determines the Work Function, Work Session, progression, handoffs, exceptions, and outcomes. System Settings constrains Actions and automation but does not redefine work semantics.
- [Asset Architecture](asset-architecture.md) determines Asset ownership, custody, deployment, and management placement. Agent location or local execution does not create information rights.
- [Integration, Security, and Governance](11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md) defines connector and governance rules. Channel policy complements rather than replaces Connector configuration.
- [Information and Data Model](08-ITOMS_INFORMATION_AND_DATA_MODEL.md) defines canonical, tenant, evidence, and derived data layers. AI output does not become a separate canonical layer.

## Validation questions

1. Which configuration realm owns the setting, and at what scope does it apply?
2. Through which Channel does the information enter, leave, or become interactive?
3. What is the approved collection purpose, and what minimum information is required?
4. Who owns and holds custody of the information, and is that determination resolved?
5. What classification, retention, execution-environment, and AI-exposure policy applies?
6. Can prohibited values be destroyed before persistence, logging, retrieval, or AI exposure?
7. Does the audit event explain enforcement without storing the prohibited raw value?
8. Is an exception narrow, attributable, reviewable, and scoped by purpose and Capability?
9. Does deterministic logic perform the work when semantic AI processing is unnecessary?
10. Can any configuration ambiguity accidentally broaden collection, disclosure, AI exposure, or execution authority?
