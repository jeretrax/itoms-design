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
- Asset occupies a Location during an occupancy interval.
- Device specializes or references an underlying Asset.
- Evidence supports an Observation, Assessment, Risk, Control, decision, or other object.
- Case belongs to or contributes to a Topic.
- Work Session (`OBJ-WSS-0001`) relates a Person and current Work Function to the canonical records, Tasks, Actions, Exceptions, and outcomes involved during a resumable period of work.
- Work affects one or more supported Business Processes or Business Functions once those concepts are canonically approved.

Relationship definitions promoted to metadata use the `REL-` namespace.
