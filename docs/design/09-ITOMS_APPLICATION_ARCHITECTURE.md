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
- Integration and connector framework
- Authorization, audit, and tenant-boundary services

## Deployment shapes

- Hosted SaaS
- MSP and co-managed multi-tenant operation
- Federated or secure enclave deployment
- Self-hosted operation for regulated or local-storage-only requirements

Implementation technology choices must preserve the same contracts, canonical identity, tenant isolation, and audit behavior across deployment shapes. Durable architecture choices belong in `/adr`.
