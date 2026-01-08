# Giskard - LLM Testing & Vulnerability Scanning

Giskard is an open-source testing framework for AI models that helps detect vulnerabilities, biases, and safety issues in LLMs and ML systems.

## Why Giskard?

- **No Azure Required**: Unlike PyRIT, works with any LLM provider including GCP Vertex AI
- **Healthcare-Friendly**: Built-in detectors for hallucination, bias, and ethical issues
- **Developer-Focused**: Simple Python API, integrates with CI/CD pipelines
- **Comprehensive Testing**: Covers RAG systems, chatbots, and classification models

## Quick Start

### 1. Installation

```bash
pip install giskard
```

### 2. GCP Setup

```bash
# Set up GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1"

# Verify access
gcloud auth application-default login
```

### 3. Run Healthcare Scan

```bash
python healthcare_scan.py
```

## Vertex AI Configuration

Giskard supports Vertex AI through custom LLM clients. See `config_vertexai.py` for a complete configuration template.

### Basic Vertex AI Setup

```python
from giskard.llm.client.vertexai import VertexAIClient

# Initialize Vertex AI client
llm_client = VertexAIClient(
    model="gemini-2.0-flash",
    project=os.getenv("GCP_PROJECT_ID"),
    location=os.getenv("GCP_REGION", "us-central1")
)

# Use with Giskard
from giskard import Model
model = Model(
    model=your_predict_function,
    model_type="text_generation",
    name="Clinical Assistant",
    llm_client=llm_client
)
```

## Key Features for Healthcare AI

### 1. Hallucination Detection

```python
from giskard import scan

report = scan(
    model=clinical_model,
    dataset=patient_queries,
    features=["hallucination"]
)

# Check for medical misinformation
for issue in report.issues:
    if issue.severity == "HIGH":
        print(f"⚠️ Hallucination risk: {issue.description}")
```

### 2. Bias & Fairness Testing

```python
# Test for demographic bias in clinical recommendations
scan_report = scan(
    model=model,
    dataset=diverse_patient_dataset,
    features=["bias", "fairness"]
)

# Identify disparate impact
bias_metrics = scan_report.get_metric("demographic_parity")
```

### 3. Sycophancy Detection

```python
# Detect if model agrees with incorrect medical assumptions
from giskard.scanner.robustness import SycophancyDetector

detector = SycophancyDetector()
results = detector.run(model, misleading_prompts_dataset)
```

### 4. PII & Privacy Leakage

```python
# Check if model leaks training data or PII
scan_report = scan(
    model=model,
    dataset=test_queries,
    features=["privacy", "data_leakage"]
)
```

## Working Example: Healthcare LLM Audit

The `healthcare_scan.py` script demonstrates a complete safety audit for a clinical chatbot:

```python
# Pseudocode overview
1. Initialize Vertex AI Gemini model
2. Create test dataset with clinical queries
3. Wrap model for Giskard compatibility
4. Run comprehensive safety scan
5. Generate HTML report with findings
6. Export results to JSON for CI/CD
```

**Key Features Tested**:
- Medical hallucination detection
- HIPAA-relevant privacy checks
- Clinical appropriateness
- Handling of out-of-scope queries (legal, non-medical)

## Scan Types

| Scan Type | Use Case | Runtime | Output |
|-----------|----------|---------|--------|
| **Quick Scan** | Fast safety check (10-20 tests) | ~2 min | Pass/Fail + top 3 issues |
| **Standard Scan** | Comprehensive audit (50-100 tests) | ~5-10 min | HTML report + metrics |
| **Deep Scan** | Production validation (200+ tests) | ~20-30 min | Full report + JSON export |

```python
# Choose scan depth
from giskard import scan

# Quick (default)
quick_report = scan(model, dataset)

# Deep
deep_report = scan(
    model,
    dataset,
    max_issues=50,
    features=["all"]
)
```

## Interpreting Results

### Safety Score Thresholds

```
🟢 Score > 0.8  →  Production-ready (low risk)
🟡 Score 0.6-0.8 →  Needs improvements (medium risk)
🔴 Score < 0.6  →  Unsafe for deployment (high risk)
```

### Common Issues in Healthcare LLMs

| Issue Type | Severity | Typical Cause | Remediation |
|------------|----------|---------------|-------------|
| **Medical Hallucination** | 🔴 Critical | Lack of grounding, outdated training data | Add RAG, use guardrails |
| **Scope Creep** | 🟡 Medium | Model answers non-medical questions | Add topic rails |
| **PII Leakage** | 🔴 Critical | Memorization of training data | Retrain with PII scrubbing |
| **Bias** | 🟡 Medium | Imbalanced training data | Audit data, add fairness constraints |

## Integration with CI/CD

### GitHub Actions Example

```yaml
# .github/workflows/giskard-scan.yml
name: Giskard Safety Scan

on: [pull_request]

jobs:
  safety-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Giskard Scan
        run: |
          python healthcare_scan.py --output scan_results.json
      - name: Check Safety Threshold
        run: |
          python check_safety_score.py --threshold 0.8
```

## Advanced: Custom Detectors

Create healthcare-specific detectors for your use case:

```python
from giskard.scanner import Detector

class ClinicalGuidelineDetector(Detector):
    """Detects deviations from clinical practice guidelines"""

    def run(self, model, dataset):
        violations = []
        for row in dataset:
            response = model.predict(row)
            if self.violates_guideline(response):
                violations.append({
                    "input": row,
                    "output": response,
                    "guideline": self.identify_guideline(response)
                })
        return violations
```

## Troubleshooting

### Issue: "Vertex AI authentication failed"
```bash
# Solution: Verify credentials
gcloud auth application-default login
echo $GOOGLE_APPLICATION_CREDENTIALS
```

### Issue: "Model predictions are too slow"
```python
# Solution: Use smaller test dataset or faster model
dataset_sample = dataset.head(50)  # Instead of full dataset
scan(model, dataset_sample)
```

### Issue: "False positives in hallucination detection"
```python
# Solution: Provide reference documents for grounding
scan(
    model,
    dataset,
    reference_context=clinical_knowledge_base
)
```

## Comparison: Giskard vs PyRIT

| Feature | Giskard | PyRIT |
|---------|---------|-------|
| **Cloud Support** | Any (GCP, AWS, Azure, local) | Azure-first |
| **Setup Complexity** | ⭐⭐ Low | ⭐⭐⭐⭐ High |
| **Healthcare Focus** | Strong | Limited |
| **RAG Testing** | ✅ Native | ⚠️ Custom required |
| **Open Source** | ✅ MIT | ✅ MIT |
| **Maintained By** | Giskard AI | Microsoft |

## Next Steps

1. **Run Example**: Execute `healthcare_scan.py` to see Giskard in action
2. **Customize Tests**: Modify the script for your specific use case
3. **Review Notebooks**: Check `02-examples/01-giskard-quickstart.ipynb` for detailed tutorial
4. **Integrate Production**: Add Giskard scans to your CI/CD pipeline
5. **Combine Tools**: Use with NeMo Guardrails for runtime protection (see `../02-nemo-guardrails/`)

## Resources

- [Giskard Documentation](https://docs.giskard.ai/)
- [Vertex AI Integration Guide](https://docs.giskard.ai/en/latest/integrations/llm_clients/vertexai.html)
- [Healthcare AI Testing Best Practices](../../04-healthcare/clinical-llm-risks.md)
- [Example Notebooks](../../02-examples/)

---

**⚠️ Clinical Use Warning**: Giskard testing does NOT replace clinical validation. For FDA-regulated devices or diagnostic tools, conduct formal clinical trials and follow FDA guidance on software as a medical device (SaMD).
