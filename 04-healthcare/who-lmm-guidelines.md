# WHO Guidance on Large Multi-Modal Models (LMMs) for Healthcare (2025)

Summary of the World Health Organization's guidance on deploying Large Multi-Modal Models in health applications, published January 2025.

## Document Overview

**Official Title**: "Ethics and Governance of Large Multimodal Models (LMMs) in Health"
**Published**: January 2025
**Full Document**: [WHO Website](https://www.who.int/publications/i/item/9789240084759)

**Scope**: Covers LLMs, vision-language models, and multimodal AI in clinical, public health, and health systems applications.

## Key Definitions

```
┌──────────────────────────────────────────────────────┐
│   WHO LMM TERMINOLOGY FOR HEALTHCARE AI              │
├──────────────────────────────────────────────────────┤
│                                                      │
│  LMM: Large Multimodal Model                         │
│  - Processes text, images, audio, other modalities   │
│  - Examples: GPT-4V, Gemini, Med-PaLM 2              │
│                                                      │
│  LLM: Large Language Model                           │
│  - Text-only subset of LMMs                          │
│  - Examples: GPT-4, Gemini, Claude                   │
│                                                      │
│  Healthcare LMM: LMM designed/deployed for health    │
│  - Clinical decision support, medical imaging,       │
│    patient communication, drug discovery             │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## Six Core Ethical Principles for Healthcare LMMs

### 1. Protect Human Autonomy

**Principle**: LMMs should **augment**, not replace, human decision-making in healthcare.

**WHO Recommendations**:
- ✅ **Human oversight**: Require clinician review of all LMM outputs before clinical action
- ✅ **Explainability**: LMMs must explain reasoning in clinically interpretable terms
- ✅ **Patient consent**: Patients must know when LMMs are used in their care
- ❌ **No autonomous diagnosis**: LMMs should not make final diagnostic decisions without human validation

**Implementation Checklist**:
- [ ] LMM suggestions labeled as "suggestions," not "decisions"
- [ ] Clinician can override LMM recommendations
- [ ] Audit trail shows human approval for all clinical actions
- [ ] Patient informed consent for LMM use in treatment planning

**Example Violation**:
```
❌ BAD: LMM autonomously orders MRI based on symptoms
✅ GOOD: LMM suggests "Consider MRI for further evaluation" → physician decides
```

### 2. Promote Human Well-Being and Safety

**Principle**: LMMs must demonstrably improve health outcomes and minimize harm.

**WHO Recommendations**:
- **Clinical validation**: Prospective trials required before deployment in clinical pathways
- **Post-market surveillance**: Continuous monitoring for adverse events
- **Safety thresholds**: Establish minimum performance criteria before deployment
  - Diagnostic accuracy ≥ human expert performance
  - Sensitivity for critical conditions (e.g., cancer) > 95%
  - False positive rate acceptable for clinical workflow

**WHO Risk Categories for Healthcare LMMs**:

| Risk Level | Examples | Required Evidence |
|-----------|----------|------------------|
| **High** | Diagnostic imaging interpretation, treatment planning | Randomized controlled trials |
| **Medium** | Patient triage, medication adherence reminders | Prospective observational studies |
| **Low** | General health education, appointment scheduling | Usability testing, user feedback |

**Deployment Criterion**: Benefits must **clearly outweigh** risks.

### 3. Ensure Transparency and Explainability

**Principle**: How LMMs work and make decisions must be understandable to clinicians and patients.

**WHO Requirements**:

#### For Clinicians:
- Model architecture and training data described
- Decision rationale provided for each output (e.g., "Based on symptoms X, Y, Z")
- Confidence scores displayed (e.g., "80% confidence in this diagnosis")
- Limitations clearly stated (e.g., "Not validated for pediatric patients")

#### For Patients:
- Plain-language explanation that LMM was involved in their care
- What data was used (e.g., "analyzed your medical records and lab results")
- How it influenced care decisions (e.g., "suggested additional tests your doctor ordered")

**Model Card Requirement**: Every healthcare LMM must have a **Model Card** documenting:
- Intended use and out-of-scope uses
- Training data characteristics
- Performance metrics (overall and by demographic subgroups)
- Known limitations and failure modes

See `../01-tools/03-model-cards/` for implementation guide.

### 4. Foster Accountability and Responsibility

**Principle**: Clear lines of responsibility when LMMs are involved in patient care.

**WHO Liability Framework**:

```
┌─────────────────────────────────────────────────┐
│      LMM HARM LIABILITY (WHO Recommendation)    │
├─────────────────────────────────────────────────┤
│                                                 │
│  If LMM causes patient harm, WHO recommends:    │
│                                                 │
│  1. Healthcare Provider                         │
│     Primary responsibility (used the tool)      │
│                                                 │
│  2. Healthcare Institution                      │
│     Institutional responsibility (deployed it)  │
│                                                 │
│  3. LMM Developer                               │
│     If defect/undisclosed limitation            │
│                                                 │
│  4. Regulatory Agencies                         │
│     If approved despite known risks             │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Required Safeguards**:
- **Incident reporting**: Adverse events logged and reported to regulatory bodies
- **Audit trails**: All LMM interactions logged for accountability
- **Professional standards**: Healthcare professional's duty to verify LMM outputs
- **Insurance**: Malpractice insurance must cover LMM-assisted care

### 5. Ensure Inclusiveness and Equity

**Principle**: LMMs must work equitably across all populations, not exacerbate health disparities.

**WHO Equity Requirements**:

#### Training Data Diversity
- [ ] Training data includes diverse populations (race, ethnicity, age, sex, geography)
- [ ] Underrepresented groups not excluded due to data scarcity
- [ ] Synthetic data used to balance representation where needed

#### Performance Equity
- [ ] Model performance tested across demographic subgroups
- [ ] Performance disparities documented and mitigated
- [ ] Acceptable disparity threshold: <5% difference in accuracy between groups

#### Access Equity
- [ ] LMM benefits available to low-resource settings, not just wealthy countries
- [ ] Multilingual support for diverse patient populations
- [ ] Affordable deployment models (not just premium healthcare systems)

**Example: WHO Equity Metric**
```python
# Test diagnostic LMM across demographic groups
subgroups = {
    "Women 18-40": 0.89,      # Sensitivity (cancer detection)
    "Men 18-40": 0.91,        # 2% difference (acceptable)
    "Women 65+": 0.87,        # 4% difference (acceptable)
    "Low-resource setting": 0.76,  # ⚠️ 13% difference (UNACCEPTABLE)
}

# WHO recommendation: Do not deploy if any subgroup >5% below best-performing group
max_disparity = max(subgroups.values()) - min(subgroups.values())
if max_disparity > 0.05:
    print("⚠️ Equity violation: Address low-resource setting performance before deployment")
```

### 6. Promote Responsive and Sustainable AI

**Principle**: LMMs should be environmentally sustainable and responsive to evolving health needs.

**WHO Recommendations**:

#### Environmental Sustainability
- Report carbon footprint of model training and inference
- Optimize model efficiency (smaller models where appropriate)
- Consider environmental impact in deployment decisions

#### Responsiveness
- **Continuous learning**: Update LMMs with new medical evidence
- **Adaptability**: Localize models for different healthcare systems and cultures
- **Feedback loops**: Incorporate clinician and patient feedback for improvement

**Example: Medical Guideline Updates**
```
Scenario: New hypertension guidelines released (2025)
Old guidelines: Target BP <140/90 for most adults
New guidelines: Target BP <130/80 for high-risk patients

LMM Update Required:
- Retrain or fine-tune with new guidelines
- Notify all deployed systems
- Audit past recommendations for affected patients
- Document update in Model Card version history
```

## Healthcare-Specific WHO Recommendations

### Clinical Decision Support

**Appropriate Uses**:
- Differential diagnosis suggestions (not final diagnosis)
- Flagging abnormal lab values or imaging findings
- Medication interaction checking
- Evidence-based treatment option summaries

**Inappropriate Uses**:
- Autonomous diagnosis without clinician review
- Treatment decisions without physician oversight
- Triage decisions in emergencies without human validation
- Replacing specialist consultation

### Medical Imaging

**WHO Standards for LMMs in Radiology/Pathology**:
- [ ] Sensitivity ≥95% for cancer detection (high-stakes diagnoses)
- [ ] Specificity sufficient to avoid excessive false positives (workflow burden)
- [ ] Performance validated on multi-site, diverse datasets
- [ ] Radiologist/pathologist review required (LMM is "second reader," not sole reader)

**Example: Mammography AI**
```
Standalone Radiologist: 85% cancer detection rate
Radiologist + LMM: 92% cancer detection rate (✅ benefit demonstrated)

BUT:
LMM Alone: 88% cancer detection rate (❌ not sufficient to replace human)
```

### Patient-Facing LMMs (Chatbots, Symptom Checkers)

**WHO Safety Requirements**:
- Clear disclaimer: "This is not medical advice. Consult healthcare provider."
- Emergency escalation: Detect urgent symptoms, direct to emergency services
- PII protection: GDPR/HIPAA compliant data handling
- No specific medical advice: No dosing recommendations, diagnoses, or treatment plans

**Example Guardrails** (from WHO guidance):
```colang
# Implement using NeMo Guardrails (see 01-tools/02-nemo-guardrails/)
define user report emergency symptom
  "chest pain"
  "difficulty breathing"
  "severe bleeding"

define bot escalate to emergency
  "These symptoms require immediate medical attention. Call emergency services or go to the nearest emergency room now."

define flow emergency detection
  priority 100  # Highest priority
  user report emergency symptom
  bot escalate to emergency
  stop  # Don't provide chatbot advice for emergencies
```

## Governance Recommendations

### National-Level Governance

WHO recommends each country establish:

1. **Regulatory Framework**
   - Classify healthcare LMMs by risk level
   - Require pre-market approval for high-risk applications
   - Post-market surveillance for adverse events

2. **Multi-Stakeholder Oversight**
   - Include clinicians, patients, ethicists, technologists
   - Regular review of LMM deployment practices
   - Public reporting of safety incidents

3. **Professional Guidelines**
   - Medical societies define standards of care for LMM use
   - Continuing education for healthcare professionals
   - Competency requirements for LMM-assisted practice

### Institutional-Level Governance

Hospitals/health systems deploying LMMs should:

- [ ] **Ethics Review**: Institutional review board (IRB) or ethics committee approval
- [ ] **Clinical Validation**: Local validation in institution's patient population
- [ ] **Monitoring**: Continuous performance monitoring and incident tracking
- [ ] **Training**: Staff training on appropriate LMM use and limitations
- [ ] **Patient Communication**: Clear policies on informing patients about LMM use

## WHO Implementation Roadmap

### Phase 1: Assessment (Months 1-3)
- Identify healthcare processes where LMMs could be beneficial
- Conduct needs assessment and stakeholder consultation
- Review existing evidence on LMM performance and safety

### Phase 2: Pilot (Months 4-9)
- Deploy LMM in controlled pilot setting
- Rigorous evaluation with control group
- Collect safety and efficacy data
- Refine based on feedback

### Phase 3: Scale (Months 10-18)
- Gradual expansion to additional clinical areas
- Continuous monitoring and adaptation
- Publish results for transparency

### Phase 4: Sustain (Ongoing)
- Regular updates with new medical evidence
- Long-term outcome tracking
- Equity audits across patient populations

## Alignment with Other Frameworks

| Framework | Focus | Overlap with WHO LMM Guidance |
|-----------|-------|------------------------------|
| **EU AI Act** | Regulatory compliance | High-risk healthcare AI classification |
| **FDA SaMD Guidance** | Medical device regulation | Clinical validation requirements |
| **NIST AI RMF** | Risk management | Trustworthy AI principles |
| **OECD AI Principles** | Responsible AI governance | Human oversight, transparency |

See `../06-governance/` for detailed implementation of these frameworks.

## Quick Start: WHO-Compliant Healthcare LMM

**Minimum checklist for WHO alignment**:

- [ ] **Autonomy**: Human oversight required for all clinical decisions
- [ ] **Safety**: Clinical validation study completed, performance documented
- [ ] **Transparency**: Model Card published, limitations clearly stated
- [ ] **Accountability**: Incident reporting system in place, audit trails enabled
- [ ] **Equity**: Performance tested across demographic groups, disparities <5%
- [ ] **Sustainability**: Model update plan for new medical evidence

**Tools to implement WHO guidance**:
- Pre-deployment testing: `../01-tools/01-giskard/` (safety scanning)
- Runtime safety: `../01-tools/02-nemo-guardrails/` (clinical guardrails)
- Documentation: `../01-tools/03-model-cards/` (transparency)
- Compliance: `./hipaa-ai-checklist.md` (privacy), `../06-governance/` (regulation)

## Resources

### WHO Official Materials
- [Full Guidance Document](https://www.who.int/publications/i/item/9789240084759)
- [WHO AI for Health Initiative](https://www.who.int/teams/digital-health-and-innovation/ai-for-health)

### Implementation Guides
- [Clinical LLM Risks](./clinical-llm-risks.md) - Practical deployment risks
- [HIPAA Compliance](./hipaa-ai-checklist.md) - Privacy protection
- [Genomics Ethics](./genomics-ethics.md) - Genetic AI applications

### Regulatory Context
- [EU AI Act Summary](../06-governance/eu-ai-act-checklist.md)
- [NIST AI RMF](../06-governance/nist-ai-600-1-summary.md)

---

**Key Takeaway**: The WHO guidance emphasizes that healthcare LMMs are **tools to assist** clinicians, not autonomous agents. Human oversight, clinical validation, and equity are non-negotiable requirements for responsible deployment.

**Last Updated**: January 2026 (reflects WHO January 2025 guidance)
