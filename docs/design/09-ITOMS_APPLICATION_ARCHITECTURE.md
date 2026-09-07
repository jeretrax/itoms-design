# ITOMS Application Architecture

**Status:** Proposed

ITOMS is a multi-tenant platform built around shared canonical services rather than isolated feature modules.

## Logical components

- Role-specific workspaces and module navigation
- Canonical object and relationship services
- Workflow and orchestration engine
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

