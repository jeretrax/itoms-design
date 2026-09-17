# ADR-0007 — Control Monitoring and Email & Domain Security

Status: Accepted

## Decision

ITOMS adopts Control Monitoring as the reusable architectural family for continuous collection, normalization, entity resolution, Control evaluation, condition, Finding, attention, investigation, remediation, verification, Evidence, and historical posture. Security Monitoring and Operational Monitoring are major concerns within that family, not isolated modules or canonical Domains.

Email & Domain Security is the first concrete Security Monitoring vertical slice. It consumes shared canonical objects and establishes patterns reusable by later identity, endpoint, vulnerability, SaaS, network, WAN, infrastructure, and availability monitoring.

Internet Domain is promoted as first-class technical Asset `OBJ-IDN-0001` in `DOM-INV-0001`. Finding is promoted as first-class operational object `OBJ-FND-0001` in `DOM-OPS-0001`. Alert reuses Attention Item `OBJ-ATT-0001`; Incident reuses Case `OBJ-CAS-0001` with appropriate classification and security context. Email Sending Source remains a contextual role and resolution construct rather than a duplicate application, device, vendor, or service directory.

The complete architecture and initial specification are maintained in `docs/design/control-monitoring-architecture.md` and `docs/design/applications/email-domain-security.md`.

## Consequences

- Observation, Finding, Alert, Incident, and Risk remain distinct.
- Monitoring does not duplicate Companies, People, Assets, Applications, Controls, Evidence, or work objects.
- Operations produces reusable Evidence; GRC references that Evidence rather than copying it.
- Posture remains explainable and historical rather than depending solely on an opaque score.
- Monitoring configuration and collection remain constrained by System Settings, Effective Context, Permissions, Information Guard, and Channel policy.
- Exact domain normalization, Sending Source persistence, Condition and Control Evaluation boundaries, Finding lifecycle, severity thresholds, forensic-report policy, and final interface behavior remain documented design questions.
