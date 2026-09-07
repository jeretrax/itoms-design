# ITOMS Domain Model

**Status:** Proposed  
**Authoritative registry:** `/itoms_domains.csv`

Domains establish canonical ownership of definitions and lifecycles. They are not navigation menus, departments, or DNS domains.

| Domain ID | Tag | Domain |
|---|---|---|
| `DOM-ORG-0001` | ORG | Organization & People |
| `DOM-LOC-0001` | LOC | Location & Physical Context |
| `DOM-INV-0001` | INV | Inventory & Asset Lifecycle |
| `DOM-APP-0001` | APP | Applications & Services |
| `DOM-IAM-0001` | IAM | Identity & Access |
| `DOM-GRC-0001` | GRC | Governance, Risk & Compliance |
| `DOM-OPS-0001` | OPS | Operations & Work Management |
| `DOM-KNO-0001` | KNO | Knowledge & Evidence |
| `DOM-FIN-0001` | FIN | Financial & Commercial |

## Ownership rule

Every first-class object belongs to exactly one Primary Domain. Cross-domain use is expressed through relationships and Facets. Changing Primary Domain is a material architectural decision and requires an ADR.

## Domain review questions

- Which Domain owns the definition and lifecycle?
- Which other Domains consume or relate to it?
- Which Facets expose it to specific audiences?
- What evidence and history must survive archival?

