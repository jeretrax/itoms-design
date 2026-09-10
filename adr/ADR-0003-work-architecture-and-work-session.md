# ADR-0003 — Work Architecture and Work Session

Status: Accepted

## Decision

ITOMS adopts Work Architecture as a foundational layer alongside Context Architecture. Work is described through the hierarchy `Work Function → Workflow / Process → Stage → Task → Action`, while allowing branching, optional paths, reversal, exceptions, external activity, judgment, and selective automation.

Work Session is promoted as first-class object `OBJ-WSS-0001` in `DOM-OPS-0001`. It preserves a person's resumable work context across canonical records, work items, organizations, documents, and applications. Workspace remains a presentation generated from Effective Context and Work Session, not a synonym for the persistent Work Session record.

The complete definitions are maintained in `docs/design/work-architecture.md`.

## Consequences

- Navigation may follow a Work Function across objects rather than always returning to object-centric navigation.
- Workflow is a flexible graph of guidance and possible progression, not necessarily a rigid sequence.
- Automation remains subordinate to work purpose, Effective Context, Permissions, judgment, and outcome.
- Cases, Projects, Scenarios, Engagements, Assessments, Topics, Tasks, and Initiatives are orchestrated by Work Architecture rather than automatically reclassified as Workflows.
- Work Session identity and material history survive browser, Lens, Workspace, and interface-mode changes.
- The canonical boundary between Work Function and Business Function, and promotion of Task and other proposed work concepts, remain future decisions.
