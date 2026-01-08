# EU AI Act Compliance Checklist (2026)

Practical checklist for healthcare AI systems under the European Union's AI Act.

## Overview

**Status**: Entered into force August 2024, phased implementation through 2027
**Scope**: AI systems placed on EU market or affecting EU persons

## AI Risk Classification

### High-Risk AI Systems (Annex III: Healthcare)

**Your AI is HIGH-RISK if it**:
- ✅ Used for diagnosis, treatment decisions, or triage
- ✅ Determines access to healthcare services
- ✅ Prioritizes patients for treatment
- ✅ Interprets medical imaging for diagnostic purposes

**Required Actions for High-Risk Systems**:

#### 1. Risk Management System
- [ ] Documented risk assessment (technical & clinical risks)
- [ ] Risk mitigation measures implemented
- [ ] Post-market monitoring plan
- [ ] Incident reporting process

#### 2. Data Governance
- [ ] Training data representative of target population
- [ ] Bias testing across demographics
- [ ] Data quality assurance process
- [ ] Documentation of data provenance

#### 3. Technical Documentation
- [ ] Detailed system description
- [ ] Model Card (see `../01-tools/model-cards/`)
- [ ] Training methodology documented
- [ ] Performance metrics (overall + subgroups)

#### 4. Record-Keeping
- [ ] Automatic logging of AI decisions (6+ years retention)
- [ ] Audit trail of training data versions
- [ ] Model version control
- [ ] Update history documented

#### 5. Transparency
- [ ] Users informed AI is being used
- [ ] Capabilities and limitations explained
- [ ] Human oversight mechanisms visible
- [ ] Instructions for use provided

#### 6. Human Oversight
- [ ] Human-in-the-loop for critical decisions
- [ ] Override capability for human operators
- [ ] Stop button / emergency shutdown
- [ ] Ongoing human monitoring

#### 7. Accuracy, Robustness, Cybersecurity
- [ ] Minimum accuracy thresholds defined and met
- [ ] Tested against adversarial attacks
- [ ] Cybersecurity measures (encryption, access control)
- [ ] Resilience to errors and anomalies

#### 8. Conformity Assessment
- [ ] Third-party audit (Notified Body) completed
- [ ] CE marking obtained
- [ ] EU Declaration of Conformity signed
- [ ] Registered in EU AI database

## Prohibited AI Practices (Article 5)

**DO NOT** deploy AI that:
- ❌ Manipulates behavior causing psychological/physical harm
- ❌ Exploits vulnerable groups (children, disabled)
- ❌ Social scoring by public authorities
- ❌ Real-time biometric identification in public spaces (with exceptions)

## Limited-Risk AI (Transparency Only)

**Your AI is LIMITED-RISK if it**:
- Chatbots / AI assistants (general health info)
- Content generation (health education materials)
- Emotion recognition

**Required Actions**:
- [ ] Disclose to users they're interacting with AI
- [ ] Make disclosure clear and intelligible

## Minimal-Risk AI (No Requirements)

- Spam filters
- Inventory management
- AI-enabled search (non-diagnostic)

## Penalties

| Violation | Fine (Up To) |
|-----------|--------------|
| Prohibited AI practices | €35M or 7% global annual turnover |
| Non-compliance (high-risk) | €15M or 3% global annual turnover |
| Incorrect information to authorities | €7.5M or 1.5% global annual turnover |

## Quick Start: Minimum Viable Compliance

**For Healthcare High-Risk AI**:
1. Conduct risk assessment
2. Test for bias across demographics
3. Create Model Card (see `../01-tools/model-cards/`)
4. Implement human oversight (see `../05-agentic-safety/human-in-loop-agents.md`)
5. Enable audit logging (see `../05-agentic-safety/audit-logging-agents.md`)
6. Schedule third-party audit

## Resources
- [EU AI Act Full Text](https://artificialintelligenceact.eu/)
- [WHO LMM Guidelines](../04-healthcare/who-lmm-guidelines.md) - Aligned with EU AI Act
- [Model Cards Toolkit](../01-tools/model-cards/) - Required documentation
