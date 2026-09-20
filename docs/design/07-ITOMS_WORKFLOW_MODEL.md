# ITOMS Workflow Model

**Status:** Proposed  
**Canonical workflow concept:** `OBJ-WFL-0001`

A Workflow, also called a Process in business-facing language, is a versioned definition of states, Stages, Tasks, Actions, decisions, approvals, automation, verification, exceptions, and outcomes associated with a Work Function, object, or business process.

A Workflow is a graph of possible progression, not necessarily a rigid sequence. It may branch, skip optional work, move backward, pause, allow parallel activity, require judgment, or record work performed outside ITOMS. Detailed hierarchy, Work Session, discovery, handoff, and guidance rules are defined in [`work-architecture.md`](work-architecture.md).

## Operational progression

The core sense-making flow is:

`Observation → Case → Topic → Assessment → Decision / Risk / Initiative / Project`

This is not a mandatory conversion pipeline. Items may remain at the lowest useful level, and evidence may support several stages.

Control Monitoring has a separate evaluation flow: `Observation → Control Evaluation → State / Condition → Finding → Alert when warranted → Investigation / Work → Remediation → Verification`. It complements the sense-making flow rather than replacing it. Observation, Finding, Alert, Incident, and Risk are distinct, and no arrow requires automatic promotion. See [`control-monitoring-architecture.md`](control-monitoring-architecture.md).

GRC uses a traceability chain rather than a mandatory Workflow: `Framework → Requirement ↔ Control → Control Implementation → Evidence → Assessment → Finding → Remediation`. Manual assessment and remediation planning may invoke guided Workflows and Work Sessions, but accepting or completing work does not change Current Posture until an authorized reassessment records a supported conclusion. See [`grc-architecture.md`](grc-architecture.md).

## Workflow definition

A workflow should specify:

- workflow ID and version
- applicable object types
- entry criteria and trigger
- states and permitted transitions
- roles, owners, and visibility
- required inputs and evidence
- automation and approval boundaries
- gates, exceptions, and escalation
- completion criteria and outcomes
- history and audit requirements
- suggested next-action rules and explanation
- pause, resume, handoff, and external-work behavior

The customer lifecycle uses this shared model for discovery, onboarding, management, support, review, and offboarding rather than hard-coded page sequences.
