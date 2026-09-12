# ITOMS Asset Architecture

**Status:** Proposed

**Purpose:** Define durable asset identity, authoritative ownership, custody, deployment, service purpose, external-system placement, and reporting scope without allowing one concern to redefine another.

## Core rule

An Asset is the durable canonical entity. Ownership, custody, assignment, location, deployment, management coverage, and service purpose describe different relationships to that Asset.

**Every Asset must have an explicit authoritative owner. External-system placement, discovery source, management group, customer site, custodian, or current user never determines or overrides ownership.**

## Asset identity

Asset (`OBJ-AST-0001`) represents a tracked item of operational, technical, financial, compliance, or custodial value. Device (`OBJ-DEV-0001`) specializes or references an Asset with technical functionality. Server (`OBJ-SRV-0001`) specializes Device.

An Asset keeps the same runtime `AssetID` throughout moves, deployments, custody changes, service changes, tool enrollment changes, and ownership transfers. Those events modify relationships or effective-dated state; they do not create a new Asset merely because the operational context changed.

## Authoritative ownership

**Owner** is the Person or Company with the authoritative property interest in an Asset for a defined time interval.

Ownership is explicit, direct, effective-dated, attributable, and independently verifiable. At any effective time, an Asset must resolve to exactly one current authoritative Owner unless it is in a documented ownership-reconciliation state.

Ownership records should retain:

- Asset identifier;
- Owner type and runtime identifier;
- effective start and end;
- acquisition or transfer basis when known;
- verification state, source, evidence, and verifier;
- commercial conditions that affect title, such as lease, rental, loan, consignment, or transfer agreement;
- superseded ownership history.

The authoritative Owner is not necessarily the purchaser, payer, user, custodian, customer, service recipient, site operator, or organization whose management portal displays the Asset. A later ownership transfer closes the previous ownership interval and creates a new one; it does not overwrite history.

## Custody and assignment

**Custody** identifies the Person or Company currently responsible for the physical care, possession, or safekeeping of an Asset. Custody is separate from legal or authoritative ownership.

**Assignment** associates an Asset with a Person, team, department, role, Work Function, or other operational purpose. Assignment expresses intended use or responsibility. It does not establish ownership and does not necessarily establish physical possession.

Custody and assignment may be effective-dated, may differ from one another, and may be absent or disputed. Convenience fields for current custodian or assignee are derived from active relationships and must not replace relationship history.

## Location and deployment

**Location** answers where an Asset physically or logically exists during an interval. A customer Location does not imply customer ownership.

**Deployment** records that an Asset has been intentionally placed into an operating environment for a defined purpose, service, or engagement. Deployment may relate the Asset to a Location, service-recipient Company, deploying provider, contract, subscription, service, engagement, or Work Function. It retains its purpose, service role, responsibility boundaries, status, and effective dates.

Deployment is not ownership. Moving provider-owned equipment to a customer site changes deployment and possibly custody, but not Owner.

## Required relationship records

The implementation should maintain separate effective-dated records rather than combine these meanings into one customer, site, or device-group field:

| Record | Minimum relationship and purpose |
| --- | --- |
| Ownership | Asset to Owner Person or Company; effective interval, state, source, verification, evidence, and transfer basis. Exactly one current authoritative relationship unless reconciling. |
| Custody | Asset to custodial Person or Company; effective interval, acceptance, responsibility, and return condition. |
| Assignment | Asset to Person, team, organizational unit, role, or Work Function; intended use and effective interval. |
| Location occupancy | Asset to Location; effective interval and placement confidence or verification. |
| Deployment | Asset to service-recipient Company and Location, with provider, service role, agreement or engagement, status, and effective interval. |
| Management coverage | Asset or Device to responsible provider/team and managed capability; coverage scope and effective interval. |
| External-system placement | Asset or Device to source system, tenant/account, site/group/folder, external record ID, synchronization state, and effective interval. |

Current Owner, custodian, location, deployment, and management summaries may be cached on the Asset for performance. They are derived projections of these records and are not independent competing truth.

## Provider-deployed service hardware

**Provider-deployed service hardware** is an Asset owned by a service provider and deployed into another organization's environment to deliver, support, monitor, secure, administer, connect, or recover a service.

Provider-deployed service hardware is a service role and relationship pattern, not a duplicate Asset class and not customer inventory. The underlying item remains the appropriate Asset, Device, or Server type.

The model must preserve at least:

- provider as authoritative Owner;
- service-recipient Company and deployed Location;
- current custodian or site contact where applicable;
- service role and related agreement or engagement;
- management and security responsibility;
- tool coverage and external identifiers;
- installation, maintenance, recovery, replacement, and return history;
- reporting classification that distinguishes provider-owned deployed equipment from customer-owned Assets.

Commercial arrangements such as included service equipment, rental, lease, loan, or recoverable provider equipment may change billing and return obligations. They do not change ownership unless an explicit ownership transfer takes effect.

## External-system placement

Datto RMM sites and groups, TeamViewer groups, Intune tenants and groups, PSA configurations, documentation platforms, monitoring portals, backup consoles, and similar systems are operational placements or source mappings.

External-system placement may indicate administration location, policy scope, automation scope, service coverage, management responsibility, discovery provenance, or external identifiers. It must never be interpreted as proof of ownership.

An Asset appearing under a customer's Datto RMM site, TeamViewer group, Intune tenant, or physical Location remains provider-owned when its authoritative ownership relationship says so.

Connector ingestion must map external records to the canonical Asset and retain source placement separately. A source-system move updates that mapping or placement. It must not silently transfer ownership, duplicate the Asset, or alter historical truth.

## Inventory and reporting scope

Inventory scope is an explicit query or report purpose, not an inherent consequence of where an Asset is found.

- **Customer-owned asset schedule:** Assets whose current authoritative Owner is the customer.
- **Assets deployed at customer:** All Assets at customer Locations, including customer-, provider-, employee-, lessor-, and third-party-owned equipment, grouped by Owner.
- **Provider service-hardware schedule:** Provider-owned Assets currently deployed to customers.
- **Managed-device view:** Devices under an active management relationship, regardless of Owner.
- **Acquisition or audit schedule:** Assets included according to the stated transaction or audit scope, with exclusions and ownership evidence visible.

Provider-owned equipment must remain operationally visible in the customer's technical context when permitted, while being excluded from a customer-owned asset transfer or ownership schedule. Reports must state their scope and must not use tool placement or site membership as an ownership proxy.

Unknown, disputed, or conflicting ownership creates a reconciliation item. ITOMS must not guess ownership from the easiest available source.

## Site Admin Box example

A **Site Admin Box** is a provider-deployed Device or Server used for monitoring, administration, backup, recovery, tooling, or other managed services at a customer site.

For a Traxler Consulting Site Admin Box deployed at a customer:

| Concern | Canonical interpretation |
| --- | --- |
| Asset identity | One durable Asset, with Device or Server specialization as appropriate. |
| Owner | Traxler Consulting, explicitly recorded and verified. |
| Deployment | Deployed to the customer's Company and Location for a defined managed-service purpose. |
| Custody | Current physical custodian or responsible party, which may be Traxler Consulting, a named technician, or the customer site contact according to the agreement. |
| Assignment/service role | Site administration, monitoring, backup, recovery, or another documented provider service role. |
| Datto RMM / TeamViewer | Managed in the appropriate operational site or group; those placements do not define Owner. |
| Intune | Enrollment follows security and management requirements, not ownership inference. Customer-tenant enrollment does not change Traxler Consulting ownership. |
| Customer inventory | Visible as equipment deployed at the customer, but excluded from customer-owned asset and acquisition schedules. |
| Provider inventory | Included as provider-owned equipment deployed externally, with return or recovery obligations where applicable. |

This same model applies to provider-owned backup appliances, monitoring collectors, managed routers, loaner equipment, temporary migration devices, cellular gateways, and similar service hardware.

## Relationship to Context Architecture

Owner is canonical Asset truth. Effective Context determines whether an actor can discover or act on ownership, custody, deployment, tool placement, commercial terms, or sensitive configuration.

Lens and Workspace may emphasize different relationships. A customer executive may see that provider equipment is excluded from owned assets; a technician may see management placement and service role; Finance may see acquisition basis and rental terms. These views operate on the same Asset and cannot redefine Owner.

Organization Profile and Operating Model may influence default responsibilities or reporting, but changing from MSP-managed to co-managed or internal IT must not alter ownership unless a separate authorized ownership-transfer event occurs.

## Relationship to Work Architecture

Asset ownership and deployment create and guide work without becoming Workflows themselves. Relevant Work Functions include acquiring and registering an Asset, verifying ownership, deploying provider service hardware, enrolling management tools, maintaining or recovering deployed hardware, returning equipment, transferring ownership, and preparing inventory schedules.

A Work Session retains the Site Admin Box as the same Asset while a technician moves across procurement records, configuration Tasks, Datto RMM, TeamViewer, Intune, backup software, documentation, deployment evidence, and customer communication.

Suggested Next Actions may identify missing Owner verification, conflicting external records, an unaccepted custody handoff, required enrollment, overdue maintenance, or a return obligation. Completing an external-system placement Action must never implicitly complete an ownership-transfer Task.

## Architectural consequences

- Asset creation requires an explicit Owner or a visible ownership-reconciliation state that blocks ownership-dependent completion.
- Ownership, custody, assignment, location, deployment, management coverage, and external-system placement use separate relationships or records.
- Current-state convenience fields are derived and cannot silently overwrite relationship history.
- Asset lists and reports declare their purpose and inclusion rule.
- External connectors preserve source identifiers and placement without treating vendor hierarchy as canonical ownership.
- Ownership transfers are explicit authorized lifecycle events with evidence and effective dates.
- Provider-deployed hardware remains visible in service operations and separable in customer ownership, audit, and transaction reporting.

## Validation questions

1. Does every Asset resolve to an explicit authoritative Owner or documented reconciliation state?
2. Are ownership, custody, assignment, location, deployment, service role, and management placement represented separately?
3. Could an external group, tenant, site, or portal move accidentally alter Owner?
4. Can the system reconstruct who owned and held the Asset at a prior date?
5. Can provider-deployed equipment remain operationally visible without appearing as customer-owned property?
6. Does every inventory or audit report state the rule by which Assets are included?
7. Does the related Work Session preserve Asset identity across internal and external Actions?
8. Is an ownership change an explicit authorized event rather than an inference?
