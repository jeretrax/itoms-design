# ADR-0006 — Design-to-Implementation Governance

Status: Accepted

## Decision

The `itoms-design` repository is the canonical design authority for ITOMS. Chat is used for design conversation. ChatGPT Work is used for design review, reconciliation, and canonical repository updates. Approved design is translated into bounded Engineering Work Packages that guide implementation.

Engineering Work Packages must provide bidirectional traceability among canonical design, implementation changes, validation evidence, and implementation discoveries. Codex and other implementation assistants may implement approved packages but may not redefine canonical concepts or product behavior.

Material ambiguities discovered during implementation are Design Gaps. The affected scope pauses while the gap is recorded in the design register, reconciled into canonical design, and reflected in an updated or superseding Engineering Work Package. Product behavior must never be invented silently in code, tests, issues, or implementation documentation.

The complete governance rules are maintained in `docs/design/design-to-implementation-governance.md`. The Engineering Work Package template is maintained in `docs/design/templates/engineering-work-package-template.md`.

## Consequences

- Conversation and implementation artifacts remain inputs or evidence rather than competing design authorities.
- Every material implementation change can be traced to approved canonical design and a bounded package.
- Implementation discoveries return through an explicit design-escalation and reconciliation path.
- Ambiguities affecting product meaning, security, persistence, workflow, permissions, or user-visible behavior cannot be resolved by silent implementation assumptions.
- Engineering Work Package identifier format, approval roles, lifecycle states, automation, and cross-repository conventions remain open until separately approved.

