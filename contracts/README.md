# Atlas–ITOMS v1 design contracts

Status: Proposed. These are transport/binding contracts under ADR-0010, not a replacement canonical entity schema or a deployed API.

- Canonical object/field authority: root `itoms_objects.csv` and `itoms_schema.csv`.
- Canonical relationship metadata: root `itoms_relationships.csv`.
- Meaning and ownership: [Canonical Ontology v1](../docs/design/canonical-ontology-v1.md).
- Operations and runtime guarantees: [schema contract](../docs/design/atlas-itoms-schema-contract-v1.md).
- `canonical-ids.schema.json` is generated from those registries.
- `.invalid` schema identifiers are identifiers only, not hosted endpoints.
- All examples use synthetic IDs, tenants and content. Their `canonicalRevision` identifies the reviewed baseline plus this proposed extension; a released implementation must replace it with the actual accepted registry commit and advertise supported revisions.
- Example snapshot digests are placeholders, not hashes of real files. Format checks do not establish integrity or reference existence.
- `atlas.feedback` is an internal publication handoff. Its private export/approval references are resolved by ITOMS; the public Atlas receives only separately authorized export content.

Run from the repository root:

```sh
python -m pip install -r contracts/requirements-validation.txt
python scripts/generate-contract-registry.py --check
python scripts/validate-atlas-contract.py
```

After changing canonical registries, run the generator without `--check`, review the generated diff, and run validation again. Entity schemas and migrations belong to approved implementation work; do not hand-maintain competing Atlas entity definitions here.
