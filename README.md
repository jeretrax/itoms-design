# ITOMS Documentation / Repository Bootstrap Sample

This sample is intended to become the root documentation contract for an ITOMS source repository.

## Start here

Read `REPO_START_HERE.md` first. It defines the mandatory read order and the rule that canonical IDs, not names, establish identity.

## Files

- `REPO_START_HERE.md` — mandatory repository read order and non-negotiable rules.
- `docs/design/README.md` — index and reading order for the ITOMS master design.
- `docs/design/context-architecture.md` — context layers and Canonical Persistence rules.
- `docs/design/work-architecture.md` — work hierarchy, Work Session continuity, guidance, workflow discovery, and selective automation.
- `docs/design/asset-architecture.md` — explicit ownership, separate custody and deployment, provider service hardware, and inventory-scope rules.
- `ITOMS_CANONICAL_RULES.md` — detailed Object ID, Domain, DomainTag, Facet, relationship, and naming rules.
- `itoms_domains.csv` — canonical Domain registry.
- `itoms_objects.csv` — canonical first-class Object registry.
- `itoms_glossary.html` — human-readable master glossary/object library with VB6-style forms and ribbon.
- `itoms_vb6.css` — intentionally plain classic-Windows presentation.
- `itoms_schema.csv` — field-level starter schema/data dictionary with canonical Object and Domain metadata.
- `AGENTS.md` — repo-aware agent entry point.
- `CLAUDE.md` — Claude repository entry point.
- `.github/copilot-instructions.md` — GitHub Copilot repository instructions.

## Core identity model

A first-class concept has a permanent canonical ID, for example `OBJ-AST-0001` for **Asset**. A tenant's individual asset record separately has a runtime `AssetID`, typically UUID/ULID-capable. Renaming the concept never changes its canonical Object ID.

Every first-class object has exactly one `PrimaryDomainID` and a readable `DomainTag`. Domains define canonical ownership. Facets define how the same object is viewed by HR, IT, Finance, Security, Executive, DR, Inventory Control, and other audiences.

Company Internet/DNS names use `PrimaryInternetDomain`; they are unrelated to the architectural `PrimaryDomainID` field.
