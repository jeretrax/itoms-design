# ADR-0008 — Unified GRC Posture and Remediation

Status: Accepted

## Decision

ITOMS adopts a unified GRC graph: `Framework → Requirement ↔ Control → Control Implementation → Evidence → Assessment → Finding → Remediation`.

Framework `OBJ-FWK-0001`, Requirement `OBJ-REQ-0001`, Control Implementation `OBJ-CIM-0001`, and Remediation `OBJ-REM-0001` are promoted as first-class objects in `DOM-GRC-0001`. Existing Control `OBJ-CTL-0001`, Assessment `OBJ-ASM-0001`, Finding `OBJ-FND-0001`, and Evidence `OBJ-EVD-0001` remain canonical and are reused across their existing Primary Domains.

Controls and Requirements relate many-to-many. Current Posture is assessment-backed truth, Planned Posture is the labeled projection produced by accepted Remediations, and Target Posture is the approved desired baseline. Accepting or completing remediation work does not change Current Posture until an authorized reassessment records a supported result.

V1 is manual and progress-focused. Its assessment states are Satisfied, Partial, Unsatisfied, and Not Assessed. Automation may later supply observations or suggested Evidence through Control Monitoring but cannot silently approve assessment conclusions or become canonical truth.

The complete architecture is maintained in `docs/design/grc-architecture.md`.

The GRC Solutions Landscape Summary at `docs/design/mockups/grc-solutions-landscape-summary.html` is accepted as the target experience and capability-coverage goal. Its breadth, connectedness, posture comparison, solution visibility, and drill-down intent are requirements. Its exact dimensions, generated sample catalog, visual treatment, and layout are illustrative and may evolve through Interface Architecture.

## Consequences

- Framework-specific checklists do not duplicate reusable Controls or Evidence.
- Control Implementation is distinct from both the reusable Control and implementation of ITOMS software.
- Finding remains cross-domain in Operations and Work Management; Evidence remains in Knowledge and Evidence.
- Remediation is a GRC plan linked to, but not synonymous with, a Task or Project.
- Scorecards must expose Current, Planned, and Target values with traceable scope and calculation policy.
- GRC processes and experiences must collectively make the full available, applicable, adopted, implemented, evidenced, assessed, planned, and verified solution landscape understandable without creating a module-owned data silo.
- Final scoring weights, applicability rules, Control Domain taxonomy, lifecycle details, imports, and certification claims remain open design questions.
