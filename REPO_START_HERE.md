# ITOMS Repository Start Here

## Mandatory read order

Any developer, AI coding assistant, agent, automation, or reviewer working in this repository MUST read these files before creating or changing ITOMS concepts, schema, UI, workflows, or documentation:

1. `REPO_START_HERE.md` — repository operating rules.
2. `ITOMS_CANONICAL_RULES.md` — identity, domain, naming, and relationship rules.
3. `docs/design/README.md` — master design index and reading structure.
4. `docs/design/context-architecture.md` — rules for Canonical Data, profiles, operating models, lenses, capabilities, permissions, and Effective Context.
5. `docs/design/work-architecture.md` — rules for Work Functions, flexible Workflows, Work Sessions, guidance, handoffs, exceptions, and outcomes.
6. `docs/design/asset-architecture.md` — rules for explicit ownership, custody, assignment, deployment, provider service hardware, and external-system placement.
7. `docs/design/system-settings-architecture.md` — control-plane configuration, Information Guard, Channels, AI Sentinel, and enforcement rules.
8. `itoms_domains.csv` — canonical Domain registry.
9. `itoms_objects.csv` — canonical Object registry.
10. `itoms_glossary.html` — authoritative human-readable glossary and object library.
11. `itoms_schema.csv` — field-level starter schema/data dictionary.

If two files appear to disagree, stop treating the names as authority. Resolve the concept by its permanent ID and update the inconsistent documentation. Permanent IDs are the identity of a concept; display names are labels.

## Non-negotiable rules

- Every first-class ITOMS concept receives a permanent canonical ID.
- A canonical ID is never reused and never changes because a concept is renamed.
- Every first-class object belongs to exactly one **Primary Domain**.
- The Primary Domain is referenced by `PrimaryDomainID`, not by free text.
- `DomainTag` is a stable, compact human-readable label for the domain and is useful in UI, exports, logs, search, and code generation. The ID remains authoritative.
- Cross-object relationships reference canonical IDs, not display names.
- Aliases, former names, UI captions, abbreviations, and vendor-specific names may change without changing canonical identity.
- Archive rather than delete when historical references exist.
- Organization Profile, Operating Model, or Lens changes never delete, replace, or redefine Canonical Data. They may change behavior, visibility, defaults, and presentation only.
- Workflows guide possible progression and must not be assumed to be rigid sequences. Work Session preserves resumable work context independently of Workspace presentation.
- Every Asset has an explicit authoritative Owner. Custody, assignment, location, deployment, service role, management coverage, and external-system placement never implicitly define or change ownership.
- Collection does not imply permission for AI processing, and local processing does not grant information rights. Information Guard policies are restrictive by default.
- Material changes to definitions, ownership, or architecture should be recorded as an ADR/decision record.

## Reserved ID namespaces

| Prefix | Concept class | Example |
|---|---|---|
| `DOM-` | Domain | `DOM-INV-0001` |
| `OBJ-` | Canonical first-class object | `OBJ-AST-0001` |
| `WF-` | Workflow | `WF-AST-0001` |
| `UI-` | UI definition/view | `UI-AST-NEW-0001` |
| `ADR-` | Architecture/decision record | `ADR-0001` |
| `FLD-` | Canonical schema field, when field-level IDs are required | `FLD-AST-0001` |
| `REL-` | Canonical relationship definition, when promoted to metadata | `REL-AST-LOC-0001` |

Prefixes identify the metadata namespace. Runtime database record IDs are separate instance identifiers and may use UUID/ULID keys.

## What counts as a first-class object?

A concept should normally become a first-class object when ITOMS needs to independently identify it, relate other things to it, apply lifecycle/history to it, assign ownership or permissions to it, assess it, attach evidence to it, or refer to it consistently across multiple domains/facets.

Before adding a new object, search `itoms_objects.csv` and the glossary for an existing concept or alias. Do not create a near-duplicate merely because a vendor or screen uses a different name.

## Repository intent

The repository is the canonical machine- and human-readable definition of ITOMS. Code, database migrations, API contracts, UI forms, documentation, AI instructions, test fixtures, and generated artifacts should converge on the same canonical object metadata rather than independently redefining terminology.

The foundational design set is indexed in `docs/design/README.md`. New design documents should be placed according to that index instead of introducing a competing root-level naming pattern.
