# ADR-0005 — System Settings, Information Guard, and AI Sentinel

Status: Accepted

## Decision

System Settings is the configuration and enforcement control plane of an ITOMS installation. It is organized into cross-cutting configuration realms rather than feature modules or canonical Domains.

Information Guard is the core realm governing information collection, Channel policy, classification, handling, minimization, sanitization, retention, AI exposure, exceptions, and auditability. Channel is an identifiable ingestion or interaction boundary for which these policies may differ. Channel complements Connector and does not replace integration configuration.

AI Sentinel is the Information Guard capability that governs whether and how information may be processed by AI. ITOMS uses deterministic processing first and AI where it adds semantic value. AI never becomes the system of record; authorized ITOMS Actions own canonical state changes.

The default posture is restrictive: collect minimally, sanitize early, destroy prohibited values before persistence or AI exposure, retain audit events without prohibited raw values, and allow only narrow purpose- and Capability-scoped exceptions.

The complete definitions are maintained in `docs/design/system-settings-architecture.md`.

## Consequences

- Collection does not imply permission for AI processing.
- Local processing does not grant ownership, custody, confidentiality, or other information rights.
- Connector access does not authorize every technically accessible flow or secondary purpose.
- Policy evaluation considers Channel, ownership, custody, classification, purpose, execution environment, and retention.
- Ambiguous policy fails closed where exposure or execution risk could increase.
- Final taxonomy, precedence, information-rights, regulated-retention, provider-qualification, and administrative-interface boundaries remain documented design questions.
