# ITOMS Relationship Model

**Status:** Proposed

Relationships make the customer operations graph useful. They preserve why objects matter to one another across time, tenants, roles, and source systems.

## Rules

- Canonical relationship definitions identify endpoint concepts by `ObjectID`.
- Runtime relationships reference tenant-scoped instance IDs.
- Relationship roles, effective dates, confidence, provenance, verification, and lifecycle should be retained when material.
- Many-to-many relationships are modeled explicitly when they carry business meaning.
- Historical relationships are ended or archived, not silently overwritten.

## Representative relationships

- Person relates to one or more Companies through contextual roles.
- Asset has exactly one authoritative Owner for an effective interval, or a documented ownership-reconciliation state.
- Asset occupies a Location, is held in Custody, receives Assignments, and participates in Deployments through separate effective-dated relationships.
- External-system placement and management coverage relate to an Asset without defining its Owner.
- Device specializes or references an underlying Asset.
- Internet Domain (`OBJ-IDN-0001`) is a technical Asset related to its authoritative Owner, Companies that use it, applications and services that operate through it, and the observations and history that describe it. A Company's primary-domain relationship does not make Company a duplicate domain registry.
- Evidence supports an Observation, Assessment, Risk, Control, decision, or other object.
- A Finding (`OBJ-FND-0001`) relates an evaluated subject, applicable Control or expectation, supporting Observations and Evidence, current disposition, and historical evaluations. An Alert is an Attention Item related to a Finding or material change; an Incident is a security-classified Case when investigation is warranted.
- A Sending Source is a contextual role that relates an Internet Domain and observed mail activity to a resolved Company, Application, Device, service, or provider. Unresolved candidates retain provenance without inventing a canonical object.
- Case belongs to or contributes to a Topic.
- Work Session (`OBJ-WSS-0001`) relates a Person and current Work Function to the canonical records, Tasks, Actions, Exceptions, and outcomes involved during a resumable period of work.
- Work affects one or more supported Business Processes or Business Functions once those concepts are canonically approved.

Relationship definitions promoted to metadata use the `REL-` namespace.

Monitoring relationships are defined further in [`control-monitoring-architecture.md`](control-monitoring-architecture.md) and the initial [Email & Domain Security specification](applications/email-domain-security.md).
