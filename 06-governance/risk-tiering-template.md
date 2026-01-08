# AI System Risk Classification Template

Template for classifying your AI system's risk level to determine appropriate governance requirements.

## Risk Tiering Framework

```
Risk Level = f(Impact, Likelihood, Reversibility, Autonomy)
```

### Impact (1-5)
**5 - Critical**: Life/death, permanent harm, irreversible financial loss
**4 - High**: Significant harm, major privacy breach, substantial financial loss
**3 - Medium**: Moderate harm, temporary disruption
**2 - Low**: Minor inconvenience, easily correctable
**1 - Minimal**: No material harm

### Likelihood (1-5)
**5 - Very High**: Error expected >10% of time
**4 - High**: Error expected 1-10% of time
**3 - Medium**: Error expected 0.1-1% of time
**2 - Low**: Error expected <0.1% of time
**1 - Very Low**: Error extremely rare

### Reversibility (1-5)
**5 - Irreversible**: Cannot undo (e.g., incorrect surgery)
**4 - Difficult**: Costly/time-intensive to reverse
**3 - Moderate**: Reversible with effort
**2 - Easy**: Quickly reversible
**1 - Automatic**: Self-correcting

### Autonomy (1-5)
**5 - Fully Autonomous**: No human oversight
**4 - High Autonomy**: Human rarely intervenes
**3 - Collaborative**: Human + AI both active
**2 - Assisted**: Human decides, AI suggests
**1 - Tool**: Human fully controls

## Risk Score Calculation

```python
risk_score = (Impact × 0.4) + (Likelihood × 0.3) + (Reversibility × 0.2) + (Autonomy × 0.1)

if risk_score >= 4.0:
    tier = "Critical Risk"
elif risk_score >= 3.0:
    tier = "High Risk"
elif risk_score >= 2.0:
    tier = "Medium Risk"
else:
    tier = "Low Risk"
```

## Governance by Risk Tier

| Risk Tier | Testing | Approval | Monitoring | Compliance |
|-----------|---------|----------|------------|------------|
| **Critical** | Clinical trials, 3rd-party audit | Board + Regulatory | Real-time + HITL | EU AI Act + FDA |
| **High** | Comprehensive (Giskard), Bias testing | Ethics committee | Daily audits | EU AI Act |
| **Medium** | Standard testing | Technical lead | Weekly audits | Internal policy |
| **Low** | Basic validation | Team lead | Monthly review | Best practices |

## Example: Healthcare AI Risk Assessments

### Example 1: Diagnostic Imaging AI

- **Impact**: 5 (Misdiagnosis → delayed treatment → death)
- **Likelihood**: 2 (5% error rate after validation)
- **Reversibility**: 3 (Diagnosis can be corrected, but delays treatment)
- **Autonomy**: 3 (Radiologist reviews, but relies on AI)

**Risk Score**: (5×0.4) + (2×0.3) + (3×0.2) + (3×0.1) = 3.5 → **HIGH RISK**

**Required Governance**:
- EU AI Act compliance (high-risk healthcare AI)
- Clinical validation studies
- FDA 510(k) clearance (if used in US)
- Radiologist oversight required
- Audit logging of all predictions

### Example 2: Patient Education Chatbot

- **Impact**: 2 (Minor misinformation, user will verify with doctor)
- **Likelihood**: 3 (Hallucinations occur ~1% of time)
- **Reversibility**: 2 (Easy to correct with doctor consult)
- **Autonomy**: 2 (Tool for patient, always disclaims non-medical-advice)

**Risk Score**: (2×0.4) + (3×0.3) + (2×0.2) + (2×0.1) = 2.1 → **MEDIUM RISK**

**Required Governance**:
- Standard Giskard testing
- Clear disclaimers ("Not medical advice")
- Basic guardrails (NeMo)
- Internal review (not regulatory)

### Example 3: Appointment Scheduling AI

- **Impact**: 1 (Worst case: appointment scheduled wrong time)
- **Likelihood**: 2 (Rare errors)
- **Reversibility**: 1 (Easily rescheduled)
- **Autonomy**: 4 (Fully automated)

**Risk Score**: (1×0.4) + (2×0.3) + (1×0.2) + (4×0.1) = 1.4 → **LOW RISK**

**Required Governance**:
- Basic testing
- User feedback monitoring
- No regulatory requirements

## Use This Template

```markdown
# AI System Risk Assessment

**System Name**: [Your AI System]
**Assessment Date**: [Date]
**Assessor**: [Name/Role]

## Risk Factors

| Factor | Score (1-5) | Justification |
|--------|-------------|---------------|
| Impact | [ ] | [Why this score?] |
| Likelihood | [ ] | [Why this score?] |
| Reversibility | [ ] | [Why this score?] |
| Autonomy | [ ] | [Why this score?] |

## Risk Calculation

**Risk Score**: `(___×0.4) + (___×0.3) + (___×0.2) + (___×0.1) = ___`

**Risk Tier**: [Critical / High / Medium / Low]

## Required Governance

- [ ] [List governance requirements based on tier]
- [ ] [Testing requirements]
- [ ] [Approval requirements]
- [ ] [Monitoring requirements]
- [ ] [Compliance requirements]

## Sign-off

**Approved By**: [Name, Title]
**Date**: [Date]
```

## Resources
- [EU AI Act](./eu-ai-act-checklist.md) - High-risk AI requirements
- [NIST AI RMF](./nist-ai-600-1-summary.md) - Risk management framework
- [WHO LMM Guidelines](../04-healthcare/who-lmm-guidelines.md) - Healthcare AI standards
