# ITOMS Design Principles

**Status:** Proposed

1. **The customer operations graph is the center.** Capabilities and experiences use shared canonical entities instead of maintaining disconnected copies.
2. **Identity is permanent.** Canonical IDs identify concepts; display names and aliases may evolve.
3. **One Primary Domain, many Facets.** Each first-class object has one owning Domain and may appear through many role-specific lenses.
4. **Work is contextual.** Requests, cases, projects, and recommendations retain the business process, relationship, risk, and outcome they affect.
5. **History is evidence.** Archive rather than delete when historical relationships exist.
6. **Guidance precedes complexity.** Default workspaces lead people through their responsibilities; object tables remain available when needed.
7. **Provenance is visible.** Imported, discovered, submitted, asserted, and verified data remain distinguishable.
8. **Human decisions stay accountable.** Automation may recommend and prepare, but approval and risk acceptance remain attributable.
9. **Security is contextual and least-privileged.** Access follows tenant, role, relationship, data sensitivity, and purpose.
10. **Design decisions are durable.** Material changes are recorded in the design register and promoted into canonical documents or ADRs.
11. **Context never replaces truth.** Organization Profile, Operating Model, Lens, and Permissions shape Effective Context without destroying or duplicating Canonical Data.
12. **Navigation follows the work.** Work Sessions preserve continuity across objects, organizations, documents, and systems rather than forcing every activity into object-centric navigation.
13. **Guidance is not rigidity.** Workflows may guide, branch, pause, reverse, and support judgment; automation remains subordinate to the Work Function and intended outcome.
14. **Ownership is explicit.** Every Asset resolves to an authoritative Owner; custody, location, deployment, management placement, and vendor grouping never substitute for ownership.
15. **Collection is purpose-limited.** Collection does not imply permission for AI processing, and local processing does not grant information rights.
16. **Deterministic first.** Use deterministic processing for known rules and AI for semantic value; AI never becomes the system of record.
17. **Sanitize before exposure.** Collect minimally, sanitize early, and destroy prohibited values before persistence or AI processing while retaining non-sensitive audit evidence.
18. **Canonical design governs implementation.** Conversation, work packages, code, tests, and generated artifacts must trace to and conform with approved design in `itoms-design`.
19. **Traceability runs both ways.** Approved design traces through bounded engineering work to implementation evidence, and material implementation discoveries trace back to canonical design decisions.
20. **Design gaps are escalated.** Implementation pauses at a material ambiguity boundary until the affected product meaning is reconciled and approved in canonical design.
21. **Product behavior is never invented silently.** An implementation convenience cannot create or override product meaning, lifecycle, permissions, persistence, workflow, or user-visible obligations.
22. **Telemetry is not a conclusion.** Collection or Observation does not automatically create a Finding, Alert, Incident, or Risk; promotion remains policy-driven and attributable.
23. **Posture is explainable.** A score or status never replaces the conditions, Controls, Evidence, configuration, exceptions, and history that support it.
24. **Evidence is referenced, not copied.** Operations, GRC, Assessments, reports, and audits reuse governed canonical Evidence subject to context and Permissions.
25. **Planned is not verified.** Accepted Remediation may project Planned Posture, but only an attributable, evidence-backed Assessment changes Current Posture.
26. **Frameworks reuse Controls.** Requirements map many-to-many to reusable Controls and shared Evidence instead of creating framework-specific copies.
27. **The endpoint layer remains locally useful.** A managed Device continues permitted observation, bounded history, diagnostics, and support behavior during cloud or Internet failure.
28. **Endpoint presence is bounded authority.** Installing an agent does not grant the cloud arbitrary SYSTEM or root execution; every operation is authenticated, scoped to an allowed capability, policy-checked, replay-resistant, and attributable.
29. **The Device stays canonical.** Agent, RMM, MDM, directory, and discovery identities enrich or map to one canonical Device and never create a competing endpoint directory by convenience.
30. **Fleet updates are a safety boundary.** Agent signing, staged release, compatibility, rollback, repair, and recovery are architectural requirements, not release-process afterthoughts.
