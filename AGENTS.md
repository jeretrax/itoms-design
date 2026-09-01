# ITOMS Agent Instructions

Before planning, coding, changing schema, creating UI, adding documentation, or inventing terminology, read `REPO_START_HERE.md` and follow its read order.

Do not create a first-class object without checking `itoms_objects.csv`. Do not identify canonical concepts by display name when a canonical ID exists. Every first-class object must have exactly one `PrimaryDomainID`. Treat `DomainTag` as a readable stable label, not the authoritative key. Record durable architectural changes in an ADR.
