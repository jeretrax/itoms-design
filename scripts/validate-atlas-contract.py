#!/usr/bin/env python3
"""Design conformance checks. Does not simulate authorization or a database."""
import copy
import csv
import json
import re
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rows(name):
    with (ROOT / name).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def check_registries():
    objects = rows("itoms_objects.csv")
    domains = rows("itoms_domains.csv")
    fields = rows("itoms_schema.csv")
    relations = rows("itoms_relationships.csv")
    od = {o["ObjectID"]: o for o in objects}
    dd = {d["DomainID"]: d for d in domains}
    require(len(od) == len(objects), "Duplicate ObjectID")
    require(len(dd) == len(domains), "Duplicate DomainID")
    require(len({r["RelationshipID"] for r in relations}) == len(relations), "Duplicate relationship ID")
    require(len({(f["ObjectID"], f["Field"]) for f in fields}) == len(fields), "Duplicate field")
    for o in objects:
        require(o["PrimaryDomainID"] in dd, "Unknown primary domain")
        require(dd[o["PrimaryDomainID"]]["DomainTag"] == o["DomainTag"], "Mismatched domain tag")
        require(all(o.values()), "Incomplete canonical object metadata")
        require(any(f["ObjectID"] == o["ObjectID"] and f["Required"] == "Yes" and "Runtime primary key" in f["Relationship_or_Rule"] for f in fields), "Missing runtime key")
    for f in fields:
        require(f["ObjectID"] in od, "Unknown schema object")
        o = od[f["ObjectID"]]
        require(f["PrimaryDomainID"] == o["PrimaryDomainID"] and f["DomainTag"] == o["DomainTag"], "Schema domain drift")
    for edge in relations:
        for side in ("FromObjectIDs", "ToObjectIDs"):
            require(all(v == "*" or v in od for v in edge[side].split(";")), "Unregistered relationship endpoint")
    requirement_fk = next(f for f in fields if f["ObjectID"] == "OBJ-REQ-0001" and f["Field"] == "FrameworkID")
    require(requirement_fk["Required"] == "Yes", "Requirement must remain Framework-bound")
    require(od["OBJ-FND-0001"]["DomainTag"] == "OPS", "Finding domain changed")
    require(od["OBJ-EVD-0001"]["DomainTag"] == "KNO", "Evidence domain changed")
    return len(objects), len(fields), len(relations)


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


ATLAS_TYPES = {
    "OBJ-CMP-0001", "OBJ-PER-0001", "OBJ-FWK-0001", "OBJ-REQ-0001",
    "OBJ-POL-0001", "OBJ-CTL-0001", "OBJ-EVD-0001", "OBJ-WFL-0001",
    "OBJ-GDN-0001", "OBJ-OBJ-0001", "OBJ-IOP-0001",
}


def validate_semantics(message):
    """Cross-field checks beyond JSON Schema. Resolvers must check live records."""
    refs = [v for v in walk(message) if "objectId" in v and "recordId" in v]
    tenant_scopes = {(v["namespace"], v["tenantScope"]) for v in refs if v["scope"] == "itoms"}
    require(len(tenant_scopes) == 1, "A private handoff must resolve exactly one installation/tenant scope")
    for v in refs:
        require(v["scope"] != "atlas" or v["objectId"] in ATLAS_TYPES, "Atlas cannot publish tenant operational state")
    for binding in (v for v in walk(message) if "bindingId" in v):
        require(binding["source"]["objectId"] == binding["target"]["objectId"], "Binding canonical type mismatch")
        require(binding["source"]["namespace"] != binding["target"]["namespace"], "Binding namespaces must differ")
    if message["kind"] == "analyzer.proposal":
        body = message["body"]
        for binding in body["bindings"]:
            require(binding["source"] in body["atlasPins"], "Binding source is not pinned in proposal")
        for applicability in body["applicability"]:
            require(applicability["driverRef"] in body["driverRefs"], "Applicability Driver not in proposal")
            require(all(r in body["sourceEvidenceRefs"] for r in applicability["sourceEvidenceRefs"]), "Applicability source not in proposal")
        require(body["caseRef"] in body["expectedRevisions"], "Case revision not guarded")
        require(all(d in body["expectedRevisions"] for d in body["driverRefs"]), "Driver revision not guarded")


def validator():
    schema = json.loads((ROOT / "contracts/atlas-itoms-v1.schema.json").read_text())
    ids = json.loads((ROOT / "contracts/canonical-ids.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    Draft202012Validator.check_schema(ids)
    object_ids = set(ids["$defs"]["ObjectID"]["enum"])
    relationship_ids = set(ids["$defs"]["RelationshipID"]["enum"])
    require(ATLAS_TYPES <= object_ids, "Atlas publication allowlist contains an unknown type")
    for node in walk(schema):
        constant = node.get("const")
        if isinstance(constant, str) and constant.startswith("OBJ-"):
            require(constant in object_ids, "Contract contains an unregistered object constant")
        if isinstance(constant, str) and constant.startswith("REL-"):
            require(constant in relationship_ids, "Contract contains an unregistered relationship constant")
    resources = Registry().with_resource(ids["$id"], Resource.from_contents(ids))
    formats = FormatChecker()

    @formats.checks("date-time", raises=ValueError)
    def check_timestamp(value):
        if not isinstance(value, str):
            return True
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value):
            return False
        return datetime.fromisoformat(value.replace("Z", "+00:00")).tzinfo is not None

    return Draft202012Validator(schema, registry=resources, format_checker=formats)


def main():
    counts = check_registries()
    v = validator()

    def validate(message):
        v.validate(message)
        validate_semantics(message)

    examples = {p.stem: json.loads(p.read_text()) for p in (ROOT / "contracts/examples").glob("*.json")}
    require(len(examples) == 4, "Expected four contract examples")
    for message in examples.values():
        validate(message)
    binding = copy.deepcopy(examples["snapshot-binding"])
    del binding["body"]["snapshot"]
    binding["body"]["mode"] = "Reference"
    validate(binding)
    binding["body"]["mode"] = "ImportDerivative"
    binding["body"]["derivationRationale"] = "Synthetic local variation with retained source lineage."
    validate(binding)

    negatives = []

    def bad(base, label, mutate):
        example = copy.deepcopy(examples[base])
        mutate(example)
        negatives.append((label, example))

    bad("analyzer-proposal", "unregistered object", lambda m: m["body"]["caseRef"].update(objectId="OBJ-FAKE-0001"))
    bad("analyzer-proposal", "wrong Case type", lambda m: m["body"]["caseRef"].update(objectId="OBJ-CMP-0001"))
    bad("analyzer-proposal", "cross tenant", lambda m: m["body"]["contextSnapshotRef"].update(tenantScope="other-tenant"))
    bad("snapshot-binding", "mismatched binding type", lambda m: m["body"]["target"].update(objectId="OBJ-CTL-0001"))
    bad("snapshot-binding", "missing snapshot", lambda m: m["body"].pop("snapshot"))
    bad("snapshot-binding", "snapshot in reference mode", lambda m: m["body"].update(mode="Reference"))
    bad("snapshot-binding", "tenant leak in Atlas reference", lambda m: m["body"]["source"].update(tenantScope="private"))
    bad("snapshot-binding", "invalid digest", lambda m: m["body"]["snapshot"].update(sha256="invalid"))
    bad("snapshot-binding", "unpinned content", lambda m: m["body"]["source"].pop("revision"))
    bad("snapshot-binding", "operational Atlas state", lambda m: (m["body"]["source"].update(objectId="OBJ-CIM-0001"), m["body"]["target"].update(objectId="OBJ-CIM-0001")))
    bad("analyzer-proposal", "unsupported version", lambda m: m.update(contractVersion="2.0.0"))
    bad("analyzer-proposal", "extra raw document payload", lambda m: m["body"].update(rawDocument="private text"))
    bad("analyzer-proposal", "assessment state as applicability", lambda m: m["body"]["applicability"][0].update(proposedState="Satisfied"))
    bad("analyzer-proposal", "unlisted Driver", lambda m: m["body"]["applicability"][0]["driverRef"].update(recordId="00000000-0000-0000-0000-000000000099"))
    bad("analyzer-proposal", "unlisted pin", lambda m: m["body"].update(atlasPins=[]))
    bad("analyzer-proposal", "missing concurrency guards", lambda m: m["body"].update(expectedRevisions=[m["body"]["caseRef"]]))
    bad("analyzer-disposition", "unsupported partial approval", lambda m: m["body"].update(outcome="PartiallyApproved"))
    bad("analyzer-disposition", "unattributed review", lambda m: m["body"].pop("approvalEvidenceRef"))
    bad("analyzer-proposal", "invalid timestamp", lambda m: m.update(issuedAt="yesterday"))
    for label, message in negatives:
        try:
            validate(message)
        except (ValueError, __import__("jsonschema").ValidationError):
            continue
        raise ValueError("Negative fixture unexpectedly passed: " + label)
    print(f"PASS: {counts[0]} objects, {counts[1]} fields, {counts[2]} relationships; 6 valid payloads; {len(negatives)} rejected invalid payloads.")
    print("Runtime authentication, source availability, FK existence, approval policy, transactions and replay behavior require implementation tests.")


if __name__ == "__main__":
    main()
