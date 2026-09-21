# ADR-0009: Local Agent Platform and Secure Device Communication

**Status:** Accepted

**Date:** 2026-09-21

## Context

ITOMS needs a persistent endpoint presence that provides Device identity, local observation, bounded history, disconnected operation, support, recovery, and controlled execution. Existing design defines canonical Device and Asset identity, Control Monitoring, Work Sessions, Information Guard, Channels, and Site Admin Box deployment, but it does not define how a local endpoint component participates in those architectures or communicates with the platform.

A conventional cloud-dependent RMM agent model is insufficient because ITOMS must remain locally useful during outages and must not equate cloud access with unrestricted SYSTEM or root execution.

## Decision

ITOMS will use one cross-platform Local Agent Platform with a shared native core and platform adapters. Rust is the preferred shared-core implementation language. Windows is the first and deepest implementation, without placing Windows-only assumptions in shared contracts.

The Local Agent Platform contains a privileged machine-facing Device Agent and a separate person-facing Support App. Their local communication is authenticated, capability-scoped, and unable to provide arbitrary privileged execution.

Agent-to-platform communication is a logical secure protocol with purpose-separated flows for enrollment, health, inventory, telemetry, policy/configuration, authorized jobs, results, updates/recovery, and support interaction. The final transport, broker, serialization, certificate architecture, local IPC, and storage technologies remain open.

Platform-to-agent execution uses signed or equivalently authenticated, tenant- and Device-scoped, expiring, replay-resistant job envelopes. The Device Agent independently validates authority and local policy. Cloud compromise or possession of service credentials must not automatically provide unrestricted fleet execution.

Agent-reported information enters the existing Information Guard and Control Monitoring path. The canonical Device remains `OBJ-DEV-0001`; the agent enriches that Device rather than creating a duplicate endpoint directory. Agent jobs and installation records remain operational concepts until their first-class lifecycle requirements are approved.

The Device Agent continues permitted observation while disconnected, retains bounded local history and queues, and reports delayed information and collection gaps honestly after reconnection. The Support App remains useful locally when cloud or Internet services are unavailable.

Discovery, agent management, Asset ownership, service effort, and OEM licensing remain separate classifications. The Device Agent observes inside a Device, the Site Admin Box observes across a Location or network, and the ITOMS control plane interprets both.

## Consequences

- Local Agent Platform becomes a foundational architecture document and an input to future Engineering Work Packages.
- No new canonical Object ID is created by this decision.
- System Settings must govern enrollment, agent policy, update rings, buffering, retention, execution capabilities, and recovery configuration.
- Information Guard must distinguish policy-relevant agent flows even if a future protocol multiplexes them.
- Work Architecture remains authoritative for why an operation occurs and whether its technical result completes business work.
- Control Monitoring remains authoritative for normalization, evaluation, Finding, alerting, Evidence, and historical posture.
- Agent updates require fleet-scale containment, rollback, recovery, signing, and future EDR compatibility gates.
- Material gaps in transport, identity, IPC, storage, packaging, lifecycle, retention, or extension behavior must be resolved in canonical design before implementation selects product behavior.

## Related canonical concepts

- Asset `OBJ-AST-0001`
- Device `OBJ-DEV-0001`
- Observation `OBJ-OBS-0001`
- Finding `OBJ-FND-0001`
- Attention Item `OBJ-ATT-0001`
- Case `OBJ-CAS-0001`
- Work Session `OBJ-WSS-0001`
- Evidence `OBJ-EVD-0001`

## References

- [`../docs/design/local-agent-platform-architecture.md`](../docs/design/local-agent-platform-architecture.md)
- [`../docs/design/asset-architecture.md`](../docs/design/asset-architecture.md)
- [`../docs/design/system-settings-architecture.md`](../docs/design/system-settings-architecture.md)
- [`../docs/design/control-monitoring-architecture.md`](../docs/design/control-monitoring-architecture.md)
- [`../docs/design/work-architecture.md`](../docs/design/work-architecture.md)
