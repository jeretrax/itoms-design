# ITOMS Master Design Index

**Status:** Active

**Purpose:** Define the reading order and stable structure of the ITOMS master design.

Read `REPO_START_HERE.md` before this directory. Root registries and canonical rules remain authoritative where noted by individual documents.

## Foundational set

1. [`01-ITOMS_VISION.md`](01-ITOMS_VISION.md) — enduring product direction and boundary.
2. [`02-ITOMS_DESIGN_PRINCIPLES.md`](02-ITOMS_DESIGN_PRINCIPLES.md) — non-negotiable design principles.
3. [`context-architecture.md`](context-architecture.md) — Canonical Data, Organization Profile, Operating Model, Lens, Capabilities, Permissions, Effective Context, and Canonical Persistence.
4. [`work-architecture.md`](work-architecture.md) — Work Functions, flexible Workflows, Work Sessions, guidance, handoffs, exceptions, outcomes, and selective automation.
5. [`03-ITOMS_GLOSSARY_MODEL.md`](03-ITOMS_GLOSSARY_MODEL.md) — terminology governance.
6. [`04-ITOMS_DOMAIN_MODEL.md`](04-ITOMS_DOMAIN_MODEL.md) — canonical ownership boundaries.
7. [`05-ITOMS_OBJECT_MODEL.md`](05-ITOMS_OBJECT_MODEL.md) — first-class concept rules.
8. [`06-ITOMS_RELATIONSHIP_MODEL.md`](06-ITOMS_RELATIONSHIP_MODEL.md) — graph and historical relationship rules.
9. [`07-ITOMS_WORKFLOW_MODEL.md`](07-ITOMS_WORKFLOW_MODEL.md) — versioned work progression.
10. [`08-ITOMS_INFORMATION_AND_DATA_MODEL.md`](08-ITOMS_INFORMATION_AND_DATA_MODEL.md) — information layers, provenance, and history.
11. [`09-ITOMS_APPLICATION_ARCHITECTURE.md`](09-ITOMS_APPLICATION_ARCHITECTURE.md) — logical services and deployment shapes.
12. [`10-ITOMS_EXPERIENCE_AND_UI_MODEL.md`](10-ITOMS_EXPERIENCE_AND_UI_MODEL.md) — role-centered interaction model.
13. [`11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md`](11-ITOMS_INTEGRATION_SECURITY_AND_GOVERNANCE.md) — connectors, security, and governance.
14. [`12-ITOMS_DESIGN_REGISTER.md`](12-ITOMS_DESIGN_REGISTER.md) — durable design inbox and decision history.

## Naming and structure

- Existing numbered foundational filenames are stable compatibility names and should not be renamed merely for stylistic consistency.
- New cross-cutting architecture documents use lowercase kebab-case descriptive names, as established by `context-architecture.md`.
- Detailed future specifications should live in a purpose-named subdirectory rather than expanding the foundational set without design review.
- Material architectural changes require a design-register entry and, when durable boundaries change, an ADR in `/adr`.
- References should use repository-relative Markdown links and preserve filename case.

## Conceptual dependency

The Vision and Design Principles establish intent. Context Architecture determines the Effective Context in which a person operates. Work Architecture determines the Work Function being performed, its possible progression, and continuity through a Work Session. Domain, Object, Relationship, Workflow, and Data models define persistent truth and reusable definitions. Application, Experience, Integration, Security, and Governance documents define how they are delivered and controlled.
