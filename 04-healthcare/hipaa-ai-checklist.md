# HIPAA Compliance Checklist for AI Applications

A practical checklist for ensuring your AI/LLM application complies with the Health Insurance Portability and Accountability Act (HIPAA) when handling Protected Health Information (PHI).

## Quick Reference: Is Your AI Subject to HIPAA?

```
┌──────────────────────────────────────────────────────┐
│         HIPAA APPLICABILITY DECISION TREE            │
└──────────────────────────────────────────────────────┘

Does your AI process, store, or transmit health information?
    │
    ├─ NO ──> HIPAA likely doesn't apply
    │
    └─ YES
        │
        └─ Is the information about identifiable individuals?
            │
            ├─ NO (de-identified/anonymized) ──> HIPAA doesn't apply
            │
            └─ YES (contains any of 18 HIPAA identifiers)
                │
                └─ Are you a Covered Entity or Business Associate?
                    │
                    ├─ NO ──> HIPAA may not legally apply BUT still best practice
                    │
                    └─ YES ──> ✅ HIPAA COMPLIANCE REQUIRED
```

## The 18 HIPAA Identifiers (Must Protect)

Your AI must NOT expose these identifiers without proper authorization:

| Category | Examples | Common AI Risks |
|----------|----------|-----------------|
| **1. Names** | Full name, maiden name | LLM memorization, training data leakage |
| **2. Geographic identifiers** | Street address, zip code (if <20k people) | Location-based queries revealing identity |
| **3. Dates** | Birth date, admission date, death date | Age inference, timeline reconstruction |
| **4. Phone numbers** | All phone/fax numbers | Contact info in training data |
| **5. Email addresses** | Any email | Training data contamination |
| **6. SSN** | Social Security Numbers | Accidental inclusion in prompts/responses |
| **7. MRN** | Medical Record Numbers | EHR integration leakage |
| **8. Account numbers** | Health plan, billing accounts | Financial data in medical context |
| **9. Certificate/license numbers** | Professional licenses | Provider identification |
| **10. Vehicle identifiers** | License plates, VINs | Transportation/injury cases |
| **11. Device identifiers** | Serial numbers, IP addresses | IoT medical devices, telehealth |
| **12. URLs** | Web addresses containing PHI | Logging, analytics |
| **13. Biometric identifiers** | Fingerprints, retinal scans, voice | Biometric authentication systems |
| **14. Photos** | Full-face photos, comparable images | Medical imaging with faces |
| **15. Other unique identifiers** | Any unique identifying number/code | Custom patient IDs |

**Plus**: Any other characteristic that could be used to identify an individual.

## HIPAA Compliance Checklist for AI/LLM Applications

### Phase 1: Data Collection & Training

#### ✅ Training Data Protection

- [ ] **Audit training data for PHI**
  - Scan all training datasets for 18 HIPAA identifiers
  - Use automated PII detection tools (e.g., Google Cloud DLP, Presidio)
  - Manual review of sample records

- [ ] **De-identify or obtain authorization**
  - Option 1: Remove all 18 identifiers (Safe Harbor method)
  - Option 2: Statistical de-identification (Expert Determination method)
  - Option 3: Obtain patient authorization for each individual's data use

- [ ] **Secure data storage during training**
  - Encrypt data at rest (AES-256 or equivalent)
  - Encrypt data in transit (TLS 1.2+)
  - Restrict access to authorized personnel only (RBAC)
  - Log all access to PHI

- [ ] **Vendor compliance (if using third-party training services)**
  - Obtain signed Business Associate Agreement (BAA)
  - Verify vendor's HIPAA compliance certifications
  - Ensure vendor deletes PHI after training completion

**Tools**:
```python
# Example: De-identify before training
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def de_identify_text(text):
    results = analyzer.analyze(text=text, language='en')
    anonymized = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized.text

# Apply to all training data
train_data_deidentified = [de_identify_text(doc) for doc in train_data]
```

### Phase 2: Model Development & Testing

#### ✅ Privacy-Preserving Model Design

- [ ] **Implement differential privacy**
  - Add noise during training to prevent memorization
  - Use frameworks like TensorFlow Privacy or Opacus
  - Target ε < 10 for reasonable privacy guarantee

- [ ] **Test for memorization**
  - Verify model doesn't regurgitate training examples containing PHI
  - Use membership inference attacks to test
  - See `synthetic-patient-data.md` for testing protocols

- [ ] **Minimize PHI in prompts**
  - Design prompts to work without requiring PHI
  - Use synthetic examples in system prompts
  - Implement PII detection on user inputs (NeMo Guardrails)

**Example**: Testing for memorization
```python
# Test if model memorizes PHI from training data
test_prompts = [
    "Complete this medical record: Patient John Smith, MRN ",
    "What do you know about patient with SSN 123-45-",
]

for prompt in test_prompts:
    response = model.generate(prompt)
    assert not contains_phi(response), f"PHI leak detected: {response}"
```

### Phase 3: Deployment & Runtime

#### ✅ Access Controls

- [ ] **Implement authentication**
  - Multi-factor authentication (MFA) for all users
  - Unique user IDs (no shared accounts)
  - Password complexity requirements (NIST 800-63B)

- [ ] **Role-Based Access Control (RBAC)**
  - Minimum necessary access principle
  - Separate roles: admin, clinician, patient, etc.
  - Document access policies

- [ ] **Session management**
  - Automatic logout after inactivity (15 minutes recommended)
  - Encrypted sessions (HTTPS only)
  - Session token rotation

#### ✅ Data Protection in Production

- [ ] **Encryption**
  - PHI encrypted at rest (AES-256)
  - PHI encrypted in transit (TLS 1.2+)
  - Encryption key management (rotate keys annually)

- [ ] **Input/Output filtering**
  - PII detection on user inputs (block before processing)
  - PII detection on model outputs (scrub before display)
  - Use NeMo Guardrails for runtime protection

**Example**: Runtime PII protection
```python
from nemoguardrails import RailsConfig, LLMRails

# Configure guardrails with PII blocking
config = RailsConfig.from_path("./healthcare_rails")
rails = LLMRails(config)

def safe_generate(user_input):
    # Guardrails automatically block PII in input/output
    response = rails.generate(messages=[{"role": "user", "content": user_input}])

    # Additional PII check
    if contains_phi(response):
        return "I cannot provide information containing personal health data."

    return response
```

- [ ] **Audit logging**
  - Log all PHI access (who, what, when, why)
  - Tamper-proof logs (write-once storage)
  - Retain logs for 6 years (HIPAA requirement)
  - Monitor for unusual access patterns

**Example**: HIPAA audit log
```python
import logging
import json

def hipaa_audit_log(user_id, action, phi_accessed, purpose):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "action": action,
        "phi_accessed": phi_accessed,  # Don't log actual PHI!
        "purpose": purpose,
        "ip_address": request.remote_addr
    }

    logging.info(json.dumps(log_entry))

# Usage
hipaa_audit_log(
    user_id="dr_smith_123",
    action="VIEW_PATIENT_SUMMARY",
    phi_accessed="MRN_998877",
    purpose="Treatment"
)
```

### Phase 4: Vendor Management (Cloud Providers, LLM APIs)

#### ✅ Business Associate Agreements (BAAs)

- [ ] **Obtain signed BAA from all vendors handling PHI**
  - Google Cloud (for Vertex AI): ✅ Provides BAA
  - OpenAI: ⚠️ Check current BAA status
  - Anthropic (Claude): ⚠️ Check current BAA status
  - Azure OpenAI: ✅ Provides BAA

- [ ] **BAA must include**:
  - Vendor's obligations to safeguard PHI
  - Permitted uses of PHI
  - Data breach notification requirements
  - Data return/destruction upon termination

- [ ] **Verify vendor security**
  - HITRUST certification (gold standard for healthcare)
  - SOC 2 Type II audit
  - ISO 27001 certification
  - Regular third-party security assessments

**GCP Vertex AI Example**:
```bash
# Configure Vertex AI with HIPAA-compliant settings
gcloud config set project hipaa-compliant-project

# Ensure data location is HIPAA-eligible region
gcloud ai models deploy MODEL_ID \
  --region=us-central1 \  # HIPAA-eligible region
  --encryption-key=projects/KMS_PROJECT/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY

# Enable audit logging
gcloud logging write hipaa-audit-log "PHI accessed via Vertex AI" --severity=INFO
```

### Phase 5: Incident Response & Breach Management

#### ✅ Breach Response Plan

- [ ] **Define breach criteria**
  - Unauthorized access to PHI
  - PHI disclosed without authorization
  - PHI lost or stolen

- [ ] **Breach response steps**
  1. Contain the breach (e.g., disable compromised account)
  2. Assess the scope (how much PHI, how many individuals)
  3. Notify affected individuals (within 60 days if >500 individuals)
  4. Notify HHS (within 60 days if >500 individuals)
  5. Notify media (if >500 individuals in same state/jurisdiction)
  6. Document the breach and response

- [ ] **Test incident response plan**
  - Conduct tabletop exercises (annually)
  - Document lessons learned
  - Update plan based on findings

**Example**: Breach detection for AI/LLM
```python
# Monitor for potential PHI leakage in model outputs
def detect_breach(user_query, model_response):
    phi_detected = []

    # Check for 18 HIPAA identifiers
    if contains_ssn(model_response):
        phi_detected.append("SSN")
    if contains_mrn(model_response):
        phi_detected.append("MRN")
    if contains_name(model_response) and contains_health_data(model_response):
        phi_detected.append("Name + Health Info")

    if phi_detected:
        trigger_breach_protocol(
            user_id=current_user.id,
            query=user_query,
            response=model_response,
            phi_types=phi_detected
        )
        return "RESPONSE BLOCKED: Potential PHI disclosure detected."

    return model_response
```

### Phase 6: Ongoing Compliance

#### ✅ Regular Security Assessments

- [ ] **Annual HIPAA Security Risk Assessment**
  - Identify threats to PHI (including AI-specific risks)
  - Assess current safeguards
  - Document vulnerabilities
  - Remediation plan with timelines

- [ ] **Periodic penetration testing**
  - Test for prompt injection attacks
  - Test for PII extraction via adversarial prompts
  - Test access controls

- [ ] **Regular model audits**
  - Re-run Giskard scans quarterly
  - Test for new jailbreak techniques
  - Verify PII detection still works

#### ✅ Training & Awareness

- [ ] **HIPAA training for all workforce members**
  - Initial training for new employees
  - Annual refresher training
  - Document completion (signatures, certificates)

- [ ] **AI-specific training**
  - How to use the AI tool appropriately
  - When NOT to input PHI into AI
  - Recognizing and reporting AI-generated PHI leaks

#### ✅ Policies & Procedures

- [ ] **Document HIPAA policies**
  - Privacy Policy (how PHI is used)
  - Security Policy (how PHI is protected)
  - Breach Notification Policy
  - AI Usage Policy (specific to LLM tools)

- [ ] **Sanction policy**
  - Consequences for HIPAA violations
  - Disciplinary actions
  - Document enforcement

## AI-Specific HIPAA Risks & Mitigations

| Risk | Example | Mitigation |
|------|---------|------------|
| **Training data contamination** | PHI accidentally included in training set | De-identify all training data, audit datasets |
| **Model memorization** | LLM outputs patient names from training data | Differential privacy, memorization testing |
| **Prompt injection** | User tricks LLM into revealing others' PHI | Input validation, NeMo Guardrails |
| **Logging PHI** | User inputs containing PHI logged for debugging | Scrub logs, PII detection before logging |
| **Third-party LLM APIs** | Sending PHI to OpenAI without BAA | Only use BAA-covered vendors (GCP, Azure) |
| **RAG database leakage** | Vector DB contains unsecured PHI | Encrypt vector stores, access controls |
| **Insecure fine-tuning** | Fine-tuning with PHI on non-compliant infrastructure | Use HIPAA-compliant cloud (GCP, Azure with BAA) |

## HIPAA Penalties (Why This Matters)

| Violation Tier | Description | Penalty Range |
|---------------|-------------|---------------|
| **Tier 1** | Unknowing violation | $100 - $50,000 per violation |
| **Tier 2** | Reasonable cause | $1,000 - $50,000 per violation |
| **Tier 3** | Willful neglect (corrected) | $10,000 - $50,000 per violation |
| **Tier 4** | Willful neglect (not corrected) | $50,000 per violation |

**Maximum annual penalty**: $1.5 million per violation category

**Criminal penalties**: Up to $250,000 fine + 10 years in prison for knowingly misusing PHI.

## Quick Start: Minimum Viable HIPAA Compliance

If you're deploying an AI/LLM tool quickly, start with these essentials:

1. ✅ **De-identify all training data** (remove 18 identifiers)
2. ✅ **Use HIPAA-compliant cloud** (GCP, Azure with signed BAA)
3. ✅ **Implement PII detection** (NeMo Guardrails on inputs/outputs)
4. ✅ **Encrypt everything** (at rest, in transit)
5. ✅ **Enable audit logging** (who accessed what, when)
6. ✅ **Test for memorization** (verify model doesn't leak PHI)
7. ✅ **Document everything** (policies, training, risk assessments)

## Resources

### Official Guidance
- [HHS HIPAA for Professionals](https://www.hhs.gov/hipaa/for-professionals/index.html)
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) (learn from others' breaches)

### Tools & Frameworks
- [Google Cloud DLP API](https://cloud.google.com/dlp) - Automated PII/PHI detection
- [Microsoft Presidio](https://github.com/microsoft/presidio) - Open-source PII anonymization
- [NeMo Guardrails](../01-tools/02-nemo-guardrails/) - Runtime PII blocking
- [Giskard Privacy Scanning](../01-tools/01-giskard/) - Test for data leakage

### Related Guides
- [Clinical LLM Risks](./clinical-llm-risks.md) - Healthcare-specific AI risks
- [WHO LMM Guidelines](./who-lmm-guidelines.md) - International healthcare AI guidance
- [Synthetic Patient Data](./synthetic-patient-data.md) - Safe data generation for testing

---

**Disclaimer**: This checklist provides practical guidance but is not legal advice. Consult with a qualified HIPAA attorney and your organization's compliance officer for definitive guidance on your specific situation.

**Last Updated**: January 2026 (HIPAA rules as of 2026)
