# ITOMS Local Agent Platform Architecture

**Status:** Proposed

**Purpose:** Define the trusted endpoint and edge presence through which ITOMS identifies Devices, observes local condition, preserves bounded history, supports disconnected operation, performs authorized work, and assists a person even when cloud connectivity is unavailable.

## Core decision

ITOMS will establish a persistent, secure, locally useful layer on every managed Device where the operating platform permits it.

The Local Agent Platform is larger than a conventional RMM agent. It is the endpoint execution and observation boundary for ITOMS, but it is not a second asset directory, an unrestricted remote shell, an EDR replacement, or the canonical system of record.

The architectural unit is one **ITOMS Local Agent Platform** with shared security, identity, communication, policy, telemetry, storage, and job semantics. Windows is the first and deepest implementation. macOS and Linux use platform adapters around the shared core. Android and iOS/iPadOS participate only within their platform restrictions and may continue to depend on MDM or MAM for privileged management.

The preferred native core implementation language is Rust. This is an approved architectural direction, not a requirement that every operation be written in Rust. Native operating-system APIs, approved scripts, external management services, and optional extensions remain valid execution mechanisms when governed by the same security boundary.

## Canonical reconciliation

This decision does not promote Agent, Agent Installation, Support App, Collector, Monitor, Job, or Command into new first-class canonical objects.

- The managed physical or logical endpoint remains Device `OBJ-DEV-0001` and its underlying Asset `OBJ-AST-0001`.
- Agent identity and installation state are operational identities associated with the canonical Device until their independent lifecycle and relationship requirements are approved.
- Agent presence enriches the canonical Device. It never creates a separate RMM endpoint database.
- Agent-reported facts enter as attributable source data, Observations `OBJ-OBS-0001`, or governed Evidence `OBJ-EVD-0001` according to the existing information model.
- Evaluated exceptions use Finding `OBJ-FND-0001`; human interruption uses Attention Item `OBJ-ATT-0001`; investigation uses Case `OBJ-CAS-0001`; resumable work uses Work Session `OBJ-WSS-0001`.
- Authorized endpoint activity is performed as governed Actions within Work Architecture. A device-side job envelope is an execution contract, not automatically a new business object or Workflow.

The boundary may be revisited if agent installations, jobs, or extensions require independent identity, permissions, history, relationships, and lifecycle beyond operational records. Until then, implementation must not invent permanent object IDs.

## Component model

### Device Agent

The **ITOMS Device Agent** is the machine-facing, privileged service. It is responsible for:

- local Device identity and secure enrollment;
- agent lifecycle, startup, health, diagnostics, update, rollback, and recovery;
- hardware, operating-system, network-interface, health, and selected service observation;
- bounded local history and disconnected buffering;
- policy and configuration enforcement within its approved capability set;
- authenticated communication with ITOMS;
- execution of authorized native operations, scripts, packages, and extensions;
- local diagnostic responses for the Support App;
- attributable results, logs, Evidence, and execution status.

The Device Agent must not depend on PowerShell, a cloud connection, or the user-facing Support App for its basic lifecycle, identity, observation, communication, update, or recovery functions.

### Support App

The **ITOMS Support App** is the person-facing endpoint experience. It is responsible for:

- requesting support;
- displaying approved support and contact information;
- showing understandable local Device, network, and service-reachability status;
- offering permitted self-service and troubleshooting guidance;
- exchanging narrowly scoped requests and responses with the local Device Agent.

The Support App is not privileged merely because it is installed beside the Device Agent. Local communication is authenticated, authorized by capability, auditable when material, and incapable of turning an unprivileged process into an arbitrary SYSTEM or root executor.

### Shared core and platform adapters

The shared Rust core should contain as much common behavior as practical:

- cryptography and trust validation;
- enrollment and operational identity;
- message and job contracts;
- policy evaluation hooks;
- communication state and retry behavior;
- local queue and bounded history abstractions;
- configuration validation;
- logging and self-diagnostics;
- update verification and staged activation;
- extension and capability boundaries.

Platform adapters provide Windows, macOS, Linux, or mobile-specific discovery, telemetry, service integration, packaging, update, and management operations. Shared contracts must not assume Windows-specific paths, services, registries, shells, or management APIs.

## Logical communication contract

The Local Agent Platform communicates with ITOMS through a secure logical agent protocol. The final transport, broker, serialization, and connection topology remain open design decisions. The logical contract must work across hosted, federated, self-hosted, and intermittently connected deployments.

Communication is separated by purpose even if an implementation multiplexes it over one connection:

| Flow | Direction | Purpose | Required properties |
| --- | --- | --- | --- |
| Enrollment and trust | Bidirectional | Establish agent identity, tenant and Device association, approved scope, and operational credentials. | Explicit authorization, short-lived bootstrap material where practical, tenant validation, replay resistance, revocation, and attributable result. |
| Heartbeat and agent health | Agent to ITOMS | Report reachability, version, configuration state, queue condition, last observation time, update state, and self-diagnostic status. | Small, idempotent, tolerant of duplication and delayed delivery. |
| Inventory and identity observations | Agent to ITOMS | Report hardware, operating system, firmware, interfaces, identifiers, and identity candidates used for Device reconciliation. | Source and capture time, provenance, confidence, change awareness, and no silent canonical overwrite. |
| Telemetry and events | Agent to ITOMS | Send bounded health, performance, network, boot, shutdown, local event, and service-reachability observations. | Policy-scoped minimization, batching, priority, compression where appropriate, ordering metadata, gap visibility, and retention controls. |
| Policy and configuration | ITOMS to Agent | Deliver versioned monitoring, retention, destination, capability, job, update-ring, Information Guard, and support configuration. | Signed or equivalently authenticated, scope-bound, versioned, validated before activation, and capable of safe rollback. |
| Authorized job delivery | ITOMS to Agent | Request an approved native operation, script, package, diagnostic, repair, or extension capability. | Unique job identity, tenant and Device scope, capability authorization, provenance, expiry, replay protection, timeout, resource limits, cancellation or revocation where supported, and audit correlation. |
| Job status and result | Agent to ITOMS | Acknowledge, start, progress, complete, fail, reject, expire, or roll back a requested job and return permitted output. | Idempotent correlation, bounded output, redaction, exit/result semantics, evidence references, and distinction between execution and business outcome. |
| Update and recovery | Bidirectional | Discover, stage, verify, activate, assess, roll back, repair, and report agent releases. | Publisher verification, artifact integrity, compatibility gates, rings/canaries, interrupted-update recovery, last-known-good behavior, and out-of-band recovery path. |
| Support interaction | Bidirectional through local and cloud boundaries | Submit a support request, share permitted diagnostics, return guidance, and expose locally available status. | Separate person and workload identity, consent or notice where required, minimum disclosure, offline usefulness, and no privilege escalation through the Support App. |

Each message or operation should carry or resolve sufficient metadata to establish tenant, agent identity, canonical Device candidate, configuration or contract version, capture or issue time, correlation, purpose, classification, and applicable policy. The precise envelope is deferred.

### Agent-to-platform path

Agent-originated information follows the established monitoring and canonical-data path:

`Device Agent → Agent ingress → Information Guard enforcement → Source validation → Normalization → Device identity reconciliation → Observation / Evidence → Control evaluation → Finding when warranted → Attention / Work when warranted → Historical posture`

The Device Agent may perform deterministic local filtering, aggregation, thresholding, or urgent detection when configured. A local result remains an attributable source assertion until the platform validates, normalizes, resolves, and persists the applicable canonical state. Local detection does not silently create approved GRC Assessment Results or make the agent the system of record.

### Platform-to-agent path

Platform-originated operations follow the governed work and execution path:

`Work Function / approved automation → Effective Context → Capability and Permission check → Information Guard and execution policy → authorized job envelope → Device Agent validation → bounded execution → result / Evidence → Work Session and canonical state transition`

ITOMS may request only operations permitted by agent policy and the resolved context. Possession of cloud-side service credentials does not imply unrestricted SYSTEM or root authority. The agent independently validates job authenticity, intended tenant and Device, capability, expiry, replay state, local policy, and supported execution boundary before acting.

Completing a device-side job does not automatically complete the business Task, close a Finding, prove a Control, or change Current Posture. Those transitions remain governed by Work, Monitoring, and GRC Architecture.

## Local identity and Device reconciliation

Enrollment must associate an agent operational identity with one canonical Device or an explicit unresolved Device candidate. Matching may consider:

- existing ITOMS Device and Asset identifiers;
- agent enrollment identity;
- RMM or MDM identifiers;
- Intune or Entra Device identifiers;
- serial number and firmware identifiers;
- operating-system identifiers;
- hostname history;
- network adapters and MAC addresses;
- Site Admin Box or network-discovery observations.

No single vendor identifier, hostname, MAC address, IP address, customer site, or management group is automatically authoritative. Conflicts produce reconciliation work rather than silent duplication or overwrite. A reinstall, re-enrollment, operating-system replacement, cloned image, or hardware replacement must not be assumed to mean either “same Device” or “new Device” until the identity rules are approved.

## Observation and bounded local history

The Device Agent continues observation without cloud availability and retains a bounded, resource-conscious local history sufficient to explain recent failure conditions.

Initial categories include:

- Device identity and hardware configuration;
- CPU, memory, storage, thermal, battery, uptime, boot, restart, and critical local condition;
- network adapters, link state and speed, addressing, gateway, DNS, local connectivity, Internet connectivity, latency, packet loss where practical, and connectivity history;
- configurable reachability to ITOMS, customer, MSP, Internet-reference, and test or monitoring destinations.

The model keeps **Device Health**, **Network Health**, and **Service Reachability** distinct. A reachable gateway does not prove Internet or application availability, and inability to contact ITOMS does not prove the Device failed.

Local history is not permanent logging. Retention, sampling, event priority, storage limits, summarization, deletion, and upload policy are governed through System Settings and Information Guard. Sensitive or prohibited values are minimized or destroyed as early as practical.

## Disconnected operation and store-and-forward

When the platform is unavailable:

1. permitted local observation and local Support App functions continue;
2. important events and telemetry are queued according to policy and priority;
3. queue limits prevent unbounded disk consumption;
4. the agent retries without creating a synchronized outage or retry storm;
5. data expiry and retention policy continue to apply while disconnected;
6. reconnection resumes from acknowledged state where the selected protocol permits;
7. ITOMS receives enough ordering, capture-time, gap, and loss metadata to distinguish delayed information from current state.

The platform must be able to reason separately about Device failure, local-network failure, Internet failure, ITOMS service failure, and agent failure. Queue overflow, expired data, corrupted local storage, and lost intervals are reported as collection gaps rather than hidden.

## Secure execution boundary

The agent is a security boundary, not a standing promise of arbitrary remote execution.

Every executable request must resolve to an allowed capability. The contract supports:

- authenticated and integrity-protected job origin;
- unique job and correlation identity;
- tenant, Device, purpose, and capability scope;
- issue time, expiry, nonce or equivalent replay defense;
- applicable configuration and policy version;
- approval or Work Session reference when required;
- execution timeout and resource constraints;
- allowed interpreter, native operation, package, or extension;
- script or artifact provenance and integrity;
- bounded, classified, and redacted output;
- emergency revocation and release rollback;
- attributable audit events on both platform and Device sides.

PowerShell is an approved Windows automation capability, not the foundation of agent operation. Routine heartbeat, identity, inventory, health, connectivity, update, and repair behavior should use the native core and operating-system APIs where practical. Similar rules apply to shells and interpreters on other platforms.

## Lifecycle, updates, and survivability

Agent lifecycle includes installation, registration, enrollment, startup, heartbeat, configuration validation, diagnostics, update discovery, staged update, verification, activation, rollback, repair, recovery reporting, revocation, unenrollment, and removal.

The release system is designed for fleet-scale failure containment. It must support:

- stable publisher identity and strong code signing;
- secured build and release provenance;
- staged rings and canary deployment;
- compatibility testing against supported operating systems and security products;
- interrupted-upgrade and unexpected-reboot recovery;
- last-known-good or equivalent rollback behavior;
- detection of quarantine, corruption, partial installation, expired credentials, and invalid configuration;
- an independent recovery path whose final mechanism remains open;
- vendor false-positive reporting and resolution;
- EDR compatibility as a future formal release gate.

Broad antivirus folder exclusions are not the normal survivability mechanism. Predictable behavior, trust reputation, secure release practice, and recovery are required architectural concerns.

## Device management classification and discovery

Discovery and management are separate concerns. A Device may be:

- Agent Managed;
- Infrastructure/API Managed;
- Known / Documented;
- BYOD;
- Guest;
- Discovered / Unclassified;
- Unknown / Unauthorized.

This list is a candidate classification, not a finalized canonical state model.

Discovery does not imply agent enrollment, management authority, customer ownership, or consumption of an OEM RMM license. Only intentionally enrolled endpoints should reach a metered OEM endpoint layer where technically possible.

Discovered Devices still contribute to environment complexity, exposure, investigation, documentation, and service effort. The pricing and service-effort model may count visibility and complexity independently from third-party licensing. Exact states, time windows, deduplication, and weights remain open.

## Site Admin Box relationship

The Device Agent and Site Admin Box provide complementary observation:

- **Device Agent:** what is happening inside this Device;
- **Site Admin Box:** what is happening across this Location or network;
- **ITOMS control plane:** what those observations mean for the organization, services, Controls, work, and posture.

The Site Admin Box remains provider-deployed service hardware under [Asset Architecture](asset-architecture.md). It may host collectors, relays, local probes, update caches, support services, or recovery functions when separately authorized. Its deployment does not make it the owner of endpoint data, grant unrestricted agent authority, or alter Device ownership.

Agent and Site Admin Box observations can corroborate or conflict. ITOMS preserves both sources, capture times, and confidence and resolves identity or state explicitly.

## Information Guard and Channel boundaries

Agent collection, local processing, Support App interaction, telemetry upload, remote job execution, and diagnostic output are subject to Information Guard.

The final Channel taxonomy is unresolved. The architecture nevertheless requires these policy-distinct flows to remain distinguishable:

- agent enrollment and trust;
- endpoint telemetry and event submission;
- platform control and configuration delivery;
- job request and job result;
- software/update artifact delivery;
- local Support App interaction;
- cloud support request and diagnostic submission.

An implementation may multiplex them over one technical connection only if policy, authorization, auditing, prioritization, retention, and failure handling remain independently enforceable. Collection does not permit AI processing, and local execution does not grant information rights.

## Work Architecture relationship

Agent activity participates in, but does not replace, Work Architecture.

- A Work Function explains why endpoint work is being performed.
- A Workflow may guide deployment, diagnosis, remediation, software installation, repair, recovery, or support.
- A Work Session preserves the Device, Person, Case, Finding, policy, requested job, results, Evidence, external systems, and next action.
- A Task describes the unit of work; the agent executes only the authorized Action within it.
- A job status reports technical execution. It does not determine the business outcome by itself.
- Exceptions such as offline Device, denied local policy, expired job, failed script, update rollback, insufficient evidence, or customer dependency return to the Work Session as explainable conditions.

Automation remains selective. High-impact or destructive Actions require the applicable approval and permission even when technically easy for the agent to execute.

## Capability sequence

The following sequence expresses implementation priority, not permanent canonical identifiers:

1. Agent lifecycle, health, and recovery.
2. Secure identity, enrollment, and communications.
3. Local observation and historical telemetry.
4. Store-and-forward and offline operation.
5. Secure job and command execution.
6. Native operating-system management operations.
7. Controlled script and automation execution.
8. Software deployment and package operations.
9. Monitoring and alert evaluation.
10. Local Support App.
11. Remote-support integration.
12. Extension and capability framework.

No Engineering Work Package should treat these ordinal labels as canonical IDs until the capability registry and identifier convention are approved.

## Initial non-goals

The initial implementation does not attempt to reproduce every mature RMM function. Specifically, it does not require:

- complete patch-management replacement;
- EDR or antivirus replacement;
- a complete native remote-desktop stack;
- MDM replacement;
- hundreds of native management actions;
- unrestricted remote shell access;
- permanent retention of all raw endpoint telemetry.

The first implementation objective is a trustworthy identity, lifecycle, observation, offline, communication, and bounded-execution foundation upon which later capabilities can be approved.

## Validation questions

1. Does the agent enrich the canonical Device instead of creating a duplicate endpoint record?
2. Can every agent message and job resolve tenant, Device, purpose, policy, time, and provenance?
3. Are Device Health, Network Health, Service Reachability, agent health, and platform reachability distinguishable?
4. Does disconnected operation remain bounded, policy-compliant, and honest about collection gaps?
5. Can a compromised platform credential authorize only scoped capabilities rather than arbitrary SYSTEM or root execution?
6. Are the Support App and privileged Device Agent separated by authenticated local authorization?
7. Can an update fail, roll back, repair, or be recovered without disabling the entire fleet?
8. Do agent observations remain distinguishable from Findings, Alerts, Incidents, Risks, and approved GRC Assessment Results?
9. Does discovery remain separate from management, ownership, and OEM licensing?
10. Are open transport, identity, storage, installer, IPC, retention, and extension decisions escalated instead of silently implemented?
