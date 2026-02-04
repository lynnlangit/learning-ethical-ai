# NIST AI 600-1: Generative AI Risk Profile (Summary)

Summary of NIST's risk framework for generative AI systems (NIST AI 600-1, July 2024 + 2025 updates).

## Overview

**Full Title**: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile
**Published**: July 2024, Updated January 2025
**Purpose**: Extend NIST AI RMF (AI 100-1) specifically for GenAI/LLM risks

## GenAI-Specific Risks (Beyond Traditional AI)

### 1. CBRN Information (Chemical, Biological, Radiological, Nuclear)
**Risk**: LLMs provide dangerous knowledge for bioweapons, explosives, etc.

**Mitigation**:
- Content filtering for CBRN requests
- Human review for suspicious queries
- Collaboration with law enforcement

### 2. Confabulation (Hallucination)
**Risk**: LLMs generate plausible-sounding but false information

**Healthcare Impact**: Medical misinformation, fake citations, invented drug interactions

**Mitigation**:
- RAG with authoritative sources
- Confidence scoring
- Citation verification
- See `../01-tools/01-giskard/` for hallucination testing

### 3. Dangerous or Violent Recommendations
**Risk**: LLMs suggest harmful actions (self-harm, violence)

**Mitigation**:
- Safety classifiers (Llama Guard - see `../01-tools/04-llama-guard/`)
- Input/output filtering (NeMo Guardrails - see `../01-tools/02-nemo-guardrails/`)

### 4. Data Privacy
**Risk**: LLMs leak training data containing PII/PHI

**Mitigation**:
- De-identify training data
- Differential privacy
- Output PII detection
- See `../04-healthcare/hipaa-ai-checklist.md`

### 5. Environmental Impacts
**Risk**: Large-scale LLM training consumes massive energy

**Mitigation**:
- Use smaller, efficient models where possible
- Carbon-aware computing
- Report environmental impact in Model Cards

### 6. Human-AI Configuration
**Risk**: Over-reliance on AI, automation bias

**Mitigation**:
- Human-in-the-loop for high-stakes decisions
- Transparency about AI limitations
- See `../05-agentic-safety/human-in-loop-agents.md`

### 7. Information Integrity
**Risk**: AI-generated misinformation, deepfakes

**Healthcare Impact**: False health claims, fake medical credentials

**Mitigation**:
- Watermarking AI-generated content
- Source attribution
- Fact-checking against authoritative databases

### 8. Information Security
**Risk**: Prompt injection, jailbreaks, adversarial attacks

**Mitigation**:
- Input validation
- Guardrails (see `../01-tools/02-nemo-guardrails/`)
- Security testing (see `../01-tools/01-giskard/`)

### 9. Intellectual Property
**Risk**: LLMs reproduce copyrighted content

**Mitigation**:
- Training data licensing review
- Output filtering for copyrighted material
- Attribution when using protected works

### 10. Obscene, Degrading, Abusive Content
**Risk**: LLMs generate offensive or harmful content

**Mitigation**:
- Content moderation (Llama Guard)
- User reporting mechanisms
- Regular safety audits

### 11. Toxicity, Bias, Homogenization
**Risk**: LLMs perpetuate stereotypes, generate biased outputs

**Healthcare Impact**: Disparate treatment recommendations, demographic bias

**Mitigation**:
- Bias testing across demographics
- Diverse training data
- Fairness metrics in Model Cards
- See `../04-healthcare/clinical-llm-risks.md` - Bias section

### 12. Value Chain & Component Integration
**Risk**: Third-party LLM APIs, compromised components

**Mitigation**:
- Vendor risk assessment (BAAs for HIPAA)
- Dependency scanning
- See `../05-agentic-safety/tool-poisoning-defense.md`

## NIST AI RMF Core Functions

### 1. GOVERN
Establish AI governance structure

**Actions**:
- Assign AI accountability roles
- Create AI ethics committee
- Document AI policies

### 2. MAP
Understand AI context and risks

**Actions**:
- Identify AI use cases
- Assess potential harms
- Document stakeholders

### 3. MEASURE
Quantify AI risks and performance

**Actions**:
- Run Giskard safety scans
- Measure demographic performance disparities
- Track hallucination rates

### 4. MANAGE
Mitigate identified risks

**Actions**:
- Implement guardrails
- Add human oversight
- Deploy monitoring

## Quick Compliance Checklist

**For Healthcare GenAI**:
- [ ] Confabulation testing (hallucination detection)
- [ ] Bias analysis across patient demographics
- [ ] HIPAA compliance (PHI protection)
- [ ] Human oversight for clinical decisions
- [ ] Audit logging (decision traceability)
- [ ] Regular safety audits (quarterly Giskard scans)
- [ ] Incident response plan

## Resources
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1 (GenAI Profile)](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST SP 800-53 Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) - August 2025 update with AI controls.
- [Implementation Tools](../01-tools/) - Giskard, NeMo Guardrails
