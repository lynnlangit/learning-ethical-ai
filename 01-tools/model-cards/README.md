# Model Cards Toolkit - Model Documentation & Transparency

Google's Model Cards Toolkit provides a framework for creating structured documentation for AI models. Model cards promote transparency, accountability, and responsible AI practices.

## Why Model Cards?

- **Regulatory Compliance**: Required for EU AI Act, helps with FDA submissions
- **Transparency**: Clearly communicate model capabilities and limitations
- **Bias Documentation**: Record demographic performance disparities
- **Reproducibility**: Document training data, parameters, evaluation metrics
- **Trust**: Help users understand when and how to use your model

## What Goes in a Model Card?

```
┌─────────────────────────────────────────────┐
│            MODEL CARD SECTIONS              │
├─────────────────────────────────────────────┤
│ 1. Model Details                            │
│    - Owner, version, architecture           │
│    - Intended use, out-of-scope uses        │
│                                             │
│ 2. Training Data                            │
│    - Dataset description, size, sources     │
│    - Preprocessing, limitations             │
│                                             │
│ 3. Evaluation                               │
│    - Metrics, benchmarks, test data         │
│    - Performance across demographics        │
│                                             │
│ 4. Ethical Considerations                   │
│    - Fairness analysis, bias mitigation     │
│    - Privacy, security considerations       │
│                                             │
│ 5. Recommendations                          │
│    - Ideal use cases, limitations           │
│    - Monitoring guidance                    │
└─────────────────────────────────────────────┘
```

## Quick Start

### Installation

```bash
pip install model-card-toolkit
```

### Basic Model Card Creation

```python
from model_card_toolkit import ModelCardToolkit

# Initialize toolkit
mct = ModelCardToolkit()

# Create model card
model_card = mct.scaffold_assets()

# Fill in details
model_card.model_details.name = "Clinical Chatbot v1.0"
model_card.model_details.overview = "LLM for patient health information"
model_card.model_details.owners = [
    {"name": "Healthcare AI Team", "contact": "ai-team@hospital.org"}
]
model_card.model_details.version.name = "1.0"
model_card.model_details.version.date = "2026-01-08"

# Save
mct.update_model_card(model_card)
mct.export_format()  # Generates HTML and JSON
```

## Healthcare LLM Model Card Example

```python
from model_card_toolkit import ModelCardToolkit
import model_card_toolkit.utils as mct_utils

mct = ModelCardToolkit()
model_card = mct.scaffold_assets()

# ===== MODEL DETAILS =====
model_card.model_details.name = "ClinicalAssist GPT"
model_card.model_details.overview = """
A fine-tuned large language model for providing general clinical information
to patients and healthcare consumers. Built on Gemini 2.0 Flash with
healthcare-specific instruction tuning.
"""

model_card.model_details.owners = [
    {
        "name": "Mayo Clinic AI Lab",
        "contact": "ai-safety@mayoclinic.org"
    }
]

model_card.model_details.version.name = "2.1.0"
model_card.model_details.version.date = "2026-01-08"
model_card.model_details.version.diff = "Added medication safety guardrails"

model_card.model_details.license = "Apache 2.0"
model_card.model_details.references = [
    {
        "reference": "https://docs.giskard.ai/healthcare-llm-testing"
    }
]

# ===== INTENDED USE =====
model_card.model_details.intended_use = """
**Intended Users**: Patients, healthcare consumers, health educators

**Intended Use Cases**:
- Explain medical conditions in plain language
- Provide general wellness and prevention information
- Clarify medical terminology
- Direct users to appropriate healthcare resources

**Out-of-Scope Uses** (DO NOT USE FOR):
- Medical diagnosis or treatment decisions
- Emergency medical situations
- Medication dosing or prescription
- Replacing consultation with healthcare providers
- Clinical decision support without physician oversight
"""

# ===== FACTORS =====
model_card.considerations.factors = [
    {
        "name": "Demographics",
        "description": "Model performance varies across age groups and health literacy levels"
    },
    {
        "name": "Medical Domains",
        "description": "Strongest in cardiology, diabetes, and oncology. Limited in rare diseases."
    },
    {
        "name": "Language",
        "description": "Optimized for English. Medical translation may lose clinical nuance."
    }
]

# ===== METRICS =====
model_card.quantitative_analysis.metrics = [
    {
        "name": "Hallucination Rate",
        "value": "3.2%",
        "description": "Percentage of responses containing medical misinformation (Giskard scan)"
    },
    {
        "name": "Safety Score",
        "value": "0.87/1.0",
        "description": "Overall safety rating from comprehensive Giskard audit"
    },
    {
        "name": "Out-of-Scope Refusal Rate",
        "value": "94%",
        "description": "Correctly declines inappropriate requests (diagnosis, dosing)"
    }
]

# ===== ETHICAL CONSIDERATIONS =====
model_card.considerations.ethical_considerations = [
    {
        "name": "Demographic Bias",
        "mitigation_strategy": "Training data balanced across age, gender, race. Regular fairness audits."
    },
    {
        "name": "Medical Misinformation",
        "mitigation_strategy": "RAG with evidence-based sources. Giskard hallucination detection."
    },
    {
        "name": "Privacy",
        "mitigation_strategy": "PII detection rails. No conversation logging without consent. HIPAA-compliant."
    },
    {
        "name": "Dependency Risk",
        "mitigation_strategy": "Explicit disclaimers. Recommends provider consultation in every response."
    }
]

# ===== LIMITATIONS =====
model_card.considerations.limitations = [
    {
        "description": "Cannot provide personalized medical advice or diagnoses"
    },
    {
        "description": "Knowledge cutoff: January 2025. May not reflect latest guidelines."
    },
    {
        "description": "Limited in rare diseases and cutting-edge treatments"
    },
    {
        "description": "Requires guardrails (NeMo) to prevent scope creep"
    }
]

# ===== USE CASES =====
model_card.considerations.use_cases = [
    {
        "description": "Patient education portal (non-diagnostic)",
        "evaluation": "PASS - Appropriate use with disclaimers"
    },
    {
        "description": "Clinical decision support tool",
        "evaluation": "FAIL - Requires physician oversight, formal FDA clearance"
    },
    {
        "description": "Medical triage chatbot",
        "evaluation": "CAUTION - Only with human escalation for emergencies"
    }
]

# Export
mct.update_model_card(model_card)
mct.export_format("healthcare_model_card.html")
print("✅ Model card generated: healthcare_model_card.html")
```

## Integration with Giskard

Automatically populate model card metrics from Giskard scans:

```python
from giskard import scan
from model_card_toolkit import ModelCardToolkit

# Run Giskard scan
scan_report = scan(model, dataset)

# Extract metrics
mct = ModelCardToolkit()
model_card = mct.scaffold_assets()

# Auto-populate from scan results
model_card.quantitative_analysis.metrics = [
    {
        "name": "Hallucination Rate",
        "value": f"{scan_report.get_metric('hallucination_rate'):.1%}",
        "description": "From Giskard automated testing"
    },
    {
        "name": "Bias Score",
        "value": f"{scan_report.get_metric('bias_score'):.2f}",
        "description": "Fairness across demographics (0=biased, 1=fair)"
    }
]

mct.update_model_card(model_card)
mct.export_format()
```

## Healthcare-Specific Sections

### Clinical Validation

```python
model_card.considerations.ethical_considerations.append({
    "name": "Clinical Validation",
    "mitigation_strategy": """
    - Reviewed by board-certified physicians (3 specialties)
    - 500 clinical vignettes tested (accuracy: 89%)
    - Ongoing monitoring with physician feedback loop
    - NOT FDA-approved as medical device
    """
})
```

### HIPAA Compliance

```python
model_card.considerations.ethical_considerations.append({
    "name": "HIPAA Compliance",
    "mitigation_strategy": """
    - No PHI (Protected Health Information) in training data
    - PII detection and removal in user inputs
    - Encrypted storage of conversation logs
    - Business Associate Agreement (BAA) required for deployment
    - See: 04-healthcare/hipaa-ai-checklist.md
    """
})
```

### Adverse Event Reporting

```python
model_card.model_details.additional_info = """
**Adverse Event Reporting**:
If the model provides harmful medical misinformation, report to:
- Internal: ai-safety@hospital.org
- FDA MedWatch (if patient harm): https://www.fda.gov/medwatch
"""
```

## Regulatory Use Cases

### EU AI Act Compliance

Model cards help satisfy transparency requirements for high-risk AI systems:

```python
# Required for EU AI Act Article 13 (Transparency)
model_card.model_details.eu_ai_act_compliance = {
    "risk_level": "High-risk (Annex III, healthcare category)",
    "conformity_assessment": "Third-party audited (Notified Body)",
    "ce_marking": "Applied for",
    "documentation_link": "https://compliance.hospital.org/eu-ai-act/clinical-assist"
}
```

### FDA SaMD (Software as Medical Device)

For diagnostic/treatment models requiring FDA clearance:

```python
model_card.model_details.regulatory_status = {
    "fda_classification": "Not a medical device (informational only)",
    "intended_use_statement": "General health education, not for diagnosis or treatment",
    "clinical_validation": "Physician-reviewed, not clinically validated for diagnosis"
}
```

## Model Card Templates

### Template 1: Healthcare Chatbot
- General patient information
- No diagnosis/treatment
- Consumer-facing

### Template 2: Clinical Decision Support
- Physician-facing
- Requires FDA clearance
- High-risk category

### Template 3: Healthcare RAG System
- Evidence retrieval only
- Documents sources
- Cites clinical guidelines

See `02-examples/` for notebook implementations.

## Best Practices

### 1. Update Regularly

```python
# Version your model cards
model_card.model_details.version.name = "2.1.0"
model_card.model_details.version.date = "2026-01-08"
model_card.model_details.version.diff = "Updated for Gemini 2.0 Flash, added medication rails"
```

### 2. Include Real Performance Data

```python
# Not just benchmarks - real-world metrics
model_card.quantitative_analysis.metrics.append({
    "name": "Production Hallucination Rate (30 days)",
    "value": "2.8%",
    "description": "From 10,000 logged conversations with physician review"
})
```

### 3. Document Failure Modes

```python
model_card.considerations.limitations.append({
    "description": "Known failure: Confuses brand names with generic medication names ~5% of time"
})
```

### 4. Include Demographic Breakdowns

```python
# Performance by subgroup
model_card.quantitative_analysis.disaggregated_metrics = [
    {"subgroup": "Age 18-40", "accuracy": "0.91"},
    {"subgroup": "Age 40-65", "accuracy": "0.89"},
    {"subgroup": "Age 65+", "accuracy": "0.84"},  # Lower - flag for improvement
]
```

## Exporting Formats

```python
# HTML (human-readable)
mct.export_format("model_card.html", "html")

# JSON (machine-readable, for compliance)
mct.export_format("model_card.json", "json")

# Markdown (for GitHub/docs)
mct.export_format("model_card.md", "markdown")
```

## Comparison: Model Cards vs Other Documentation

| Tool | Purpose | Audience | When |
|------|---------|----------|------|
| **Model Card** | Transparency & compliance | Stakeholders, regulators | Every model |
| **Datasheets** | Dataset documentation | ML engineers | Every dataset |
| **FactSheets** | System-level docs | Auditors | Production systems |
| **Technical Docs** | Implementation details | Developers | Development |

**Use all for complete documentation!**

## Example: Real-World Model Cards

- [Gemini Model Card](https://ai.google.dev/gemini-api/docs/model-card)
- [GPT-4 System Card](https://openai.com/research/gpt-4-system-card)
- [Llama Guard Model Card](https://huggingface.co/meta-llama/LlamaGuard-7b)

## Next Steps

1. **Create Your First Card**: Run the healthcare example above
2. **Integrate with Giskard**: Auto-populate metrics from safety scans
3. **Version Control**: Store model cards in Git alongside model code
4. **Publish**: Share model cards with users, regulators, stakeholders
5. **Update Regularly**: Treat model cards as living documents

## Resources

- [Model Cards Paper (Mitchell et al., 2019)](https://arxiv.org/abs/1810.03993)
- [Model Cards Toolkit Docs](https://github.com/tensorflow/model-card-toolkit)
- [EU AI Act Transparency Requirements](https://artificialintelligenceact.eu/article/13/)
- [FDA SaMD Guidance](https://www.fda.gov/medical-devices/software-medical-device-samd)

## Healthcare-Specific Resources

- WHO LMM Guidance: See `04-healthcare/who-lmm-guidelines.md`
- HIPAA Compliance: See `04-healthcare/hipaa-ai-checklist.md`
- EU AI Act Summary: See `06-governance/eu-ai-act-checklist.md`

---

**⚠️ Compliance Note**: Model cards are increasingly **required** for:
- EU AI Act (high-risk systems)
- FDA SaMD submissions (documentation requirement)
- Healthcare system procurement (transparency requirement)
- Insurance coverage (validation requirement)

Create model cards early and update them continuously.
