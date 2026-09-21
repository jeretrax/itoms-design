# ITOMS Application Architecture

**Status:** Proposed

ITOMS is a multi-tenant platform built around shared canonical services rather than isolated feature modules.

## Logical components

- Role-specific workspaces and contextual capability navigation
- Effective Context resolution across Organization Profile, Operating Model, Lens, Capabilities, Permissions, and current scope
- Canonical object and relationship services
- Workflow and orchestration engine
- Work Session continuity and next-action guidance services
- Workflow pattern observation and suggestion services
- Ingestion, normalization, and reconciliation services
- Search, reporting, and timeline services
- Evidence and knowledge services
- Policy, risk, control, and assessment services
- Framework, Requirement, Control mapping, Control Implementation, Remediation, and posture projection services
- GRC scorecard, manual assessment, evidence traceability, and progress reporting services
- Integration and connector framework
- Authorization, audit, and tenant-boundary services
- System Settings control-plane and Information Guard policy enforcement
- Channel policy resolution and AI Sentinel decision service
- Control Monitoring collection, normalization, entity-resolution, evaluation, Finding, verification, and posture services
- Monitoring health, evidence reuse, and customer/MSP reporting services
- Agent ingress, trust, heartbeat, configuration, queue acknowledgement, and Device reconciliation services
- Authorized job policy, dispatch, result correlation, revocation, and audit services
- Agent release, update-ring, compatibility, rollback, and recovery services
- Shared Local Agent core, platform adapters, and separate person-facing Support App

## Deployment shapes

- Hosted SaaS
- MSP and co-managed multi-tenant operation
- Federated or secure enclave deployment
- Self-hosted operation for regulated or local-storage-only requirements

Implementation technology choices must preserve the same contracts, canonical identity, tenant isolation, and audit behavior across deployment shapes. Durable architecture choices belong in `/adr`.

The monitoring responsibilities are logical boundaries, not prescribed deployable services. Their reusable contract is defined in [`control-monitoring-architecture.md`](control-monitoring-architecture.md); the first vertical slice is [Email & Domain Security](applications/email-domain-security.md).

The endpoint and edge responsibilities are likewise logical boundaries. Their communication contract, offline behavior, execution boundary, and relationship to canonical Device identity are defined in [`local-agent-platform-architecture.md`](local-agent-platform-architecture.md). A deployment may combine or separate ingress, queueing, job dispatch, update, and monitoring services, but it must preserve purpose-specific policy enforcement and audit correlation.

The unified GRC contract is defined in [`grc-architecture.md`](grc-architecture.md). Its V1 service boundaries must support manual operation without requiring monitoring or AI services.
