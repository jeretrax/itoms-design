# ITOMS Service Management and GRC Separation

## Design decision

IT Service Management and Governance, Risk & Compliance are separate management functions in ITOMS.

They share canonical organizational data and may link to one another, but neither is a status projection of the other.

## IT Service Management

Primary question:

> What IT services does the organization have, purchase, receive, or provide; who is responsible; and is delivery occurring as agreed?

Core chain:

Agreement / Plan → Service → Service Commitment → Responsibility → Lifecycle Stage → Procedure / Schedule → Work / Delivery Record → Deliverable / Service Evidence

Service-management state includes:
- catalog availability
- selected / subscribed / assigned
- provider
- agreement and scope
- commercial treatment or internal resource allocation
- onboarding prerequisites
- operationalization
- recurring obligations
- SLA / service expectation
- delivery health
- customer dependencies
- changes and offboarding

A service can exist without a GRC relationship.

## GRC

Primary question:

> What should be true, what is actually true, what has been agreed upon, and what can be proven?

Canonical chain:

Framework → Requirement → Control → Implementation → Evidence → Assessment → Finding → Remediation

GRC state includes:
- applicability
- desired / target state
- current assessed state
- planned state
- evidence
- assessment result
- gaps and findings
- remediation
- risk acceptance
- business ownership

A GRC control can exist without a supporting managed service.

## Hard boundary

Purchasing, subscribing to, assigning, or delivering an IT service does not establish that a GRC control is satisfied.

Likewise, a GRC gap does not automatically create MSP scope.

The connection is explicit:

Service / Responsibility → supports → Control Implementation

Evidence generated during service delivery may be attached to or referenced by a GRC implementation or assessment, but the assessment determines posture.

## Ownership

Risk remains a business responsibility by default. Technical or service providers may own implementation responsibilities without becoming the owner of the underlying business risk.

Every applicable gap should be capable of showing:
- business owner
- implementation owner
- existing supporting service, if any
- whether work is included in current scope
- customer responsibility
- third-party responsibility
- proposed new service or project
- accepted risk / deferred decision

## Reference customer: PICCO Coatings

PICCO is the initial design fixture.

The IT Essentials agreement instantiates the purchased service set. The Traxler **Our Managed Services Explained** catalog is the source catalog for service definitions.

Examples from the source catalog include:
- Employee Onboarding & Offboarding
- User Management
- Email Spam Filtering
- 2FA / MFA
- User Training
- Phishing Simulation
- M365 / Google Workspace Support
- Endpoint Protection
- Software Patch Management
- MDR / SOC
- Data Loss Prevention
- Backup services
- Firewall / IDP / IPS
- Network Monitoring
- Governance, Risk & Compliance Center
- Written Policies
- Plan of Action & Milestones
- Compliance reporting
- Disaster Recovery Plan / Testing
- Vulnerability Scanning
- System Security Plan
- Mobile / Tablet Device Management

The source catalog currently contains 113 numbered offerings and mixes true managed services, service guarantees, delivery channels, recurring deliverables, projects, technical capabilities, and GRC activities. ITOMS should preserve source lineage while normalizing each item into the appropriate canonical type.

## UI consequence

ITOMS should expose at least two separate customer management dashboards:

### IT Services Management Dashboard
Optimized for:
- what the customer has
- what is included
- who provides it
- what Traxler is responsible for
- what the customer is responsible for
- onboarding / operational state
- recurring work and deliverables
- service health
- cost / agreement context
- recommendations outside scope

### GRC Posture Dashboard
Optimized for:
- desired state
- actual state
- planned state
- applicable requirements
- controls
- implementations
- evidence
- assessments
- findings
- remediation and accepted risk

The existing massive GRC Solutions Landscape is the expanded GRC universe. The abridged GRC dashboard is the normal management view.

## Cross-navigation

From a Service:
- show GRC implementations supported by this service
- show evidence generated that is reusable by GRC
- never label a control compliant solely from service status

From a Control / Implementation:
- show supporting services
- show implementation owner
- show whether supporting work is in scope
- show unsupported gaps
- allow creation of recommendation, project, responsibility, or service proposal

## Initial mockups

- `docs/design/mockups/it-service-management-dashboard.html`
- `docs/design/mockups/grc-posture-dashboard-abridged.html`
- `docs/design/mockups/grc-solutions-landscape-summary.html` (existing expanded landscape)

These are conceptual mockups. Numeric PICCO posture and delivery values in the HTML examples are illustrative and must not be treated as assessed customer facts.
