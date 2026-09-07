# ITOMS Glossary Model

**Status:** Proposed  
**Authoritative glossary:** `/itoms_glossary.html`

This document defines how ITOMS terminology is governed. It does not duplicate the full glossary.

## Rules

- Every first-class concept must be checked against `/itoms_objects.csv` before it is introduced.
- A concept's canonical ID is authoritative; its display name is a mutable label.
- Aliases and vendor terms map to canonical concepts rather than creating duplicates.
- Every first-class object has exactly one `PrimaryDomainID` from `/itoms_domains.csv`.
- `DomainTag` is a stable readable label, not the referential key.
- A Facet is a role or use-case lens and does not change canonical ownership.
- Company DNS names use `PrimaryInternetDomain`, never `PrimaryDomainID`.

## Change process

Proposed terms begin in `12-ITOMS_DESIGN_REGISTER.md`. Accepted first-class concepts are added to the object registry, glossary, schema where applicable, and an ADR when the change affects object boundaries or ownership.

