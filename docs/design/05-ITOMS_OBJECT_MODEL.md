# ITOMS Object Model

**Status:** Proposed  
**Authoritative registry:** `/itoms_objects.csv`

An object becomes first-class when ITOMS must independently identify it, relate it, manage its lifecycle, assign responsibility or permissions, assess it, attach evidence, or reference it consistently across domains.

## Required concept metadata

- `ObjectID`
- `ObjectName`
- `PrimaryDomainID`
- `DomainTag`
- Definition
- Status
- Aliases
- Lifecycle policy

## Runtime distinction

Canonical IDs identify object types, such as `OBJ-AST-0001` for Asset. Tenant records use separate runtime identifiers, such as `AssetID` represented by a UUID or ULID.

## Promotion test

Before promoting a concept:

1. Search the object registry and glossary for an existing concept or alias.
2. Confirm that independent identity and lifecycle are necessary.
3. Assign exactly one Primary Domain.
4. Define relationships by canonical endpoint IDs.
5. Define archive, retention, and evidence behavior.
6. Record material boundary decisions in an ADR.

