# ITOMS Experience and UI Model

**Status:** Proposed

ITOMS navigation is centered on the user's role, current position, responsibilities, and next meaningful action. Object-centric lists remain available without becoming the whole application.

## Experience structure

- A persistent application shell supports tenant and workspace context.
- A Workspace presents the current Work Function and resumable Work Session without becoming the canonical Work Session record.
- Each workspace or capability area may provide contextual sub-navigation without becoming a separate data silo.
- Journey or workflow banners show current stage, blockers, ownership, and next steps.
- Navigation may follow work across objects, organizations, documents, and applications while preserving previous, current, and next work items.
- Role-specific Facets present the same canonical truth differently for end users, IT staff, department managers, executives, and MSP personnel.
- Dense operational tables provide saved views, filters, sorting, grouping, and a Datto RMM-style field chooser.

## Standard views

- guided workspace
- list and inventory
- detail and relationship view
- timeline and history
- task or required step
- report and assessment
- training and knowledge
- evidence and verification

Customer-facing views explain what is happening, why it matters, what is needed from the customer, and what happens next while keeping credentials and technician-only details hidden.

Detailed visual behavior remains an Interface Architecture concern. Work requirements and terminology are defined in [`work-architecture.md`](work-architecture.md).
