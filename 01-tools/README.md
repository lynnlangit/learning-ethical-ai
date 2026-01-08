# AI Safety & Ethics Tools

This folder contains setup guides, configuration templates, and working examples for key AI safety and ethics tools. All examples are configured for **GCP Vertex AI** by default.

## Quick Start Guide

```bash
# Install core dependencies
pip install giskard nemoguardrails model-card-toolkit

# Configure GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1"
```

## Tool Comparison Matrix

| Tool | Primary Use Case | Best For | Setup Complexity | Healthcare Support |
|------|-----------------|----------|------------------|-------------------|
| **Giskard** | LLM testing & vulnerability scanning | Quick safety audits, RAG evaluation, hallucination detection | ⭐⭐ Low | ✅ Excellent |
| **NeMo Guardrails** | Runtime safety controls | Production guardrails, input/output filtering, topic control | ⭐⭐⭐ Medium | ✅ Strong |
| **Model Cards Toolkit** | Model documentation & transparency | Compliance documentation, model governance | ⭐ Very Low | ✅ Good |
| **Llama Guard** | Content moderation | Toxicity filtering, safety classification | ⭐⭐ Low | ⚠️ Limited |

## Getting Started Paths

### Path 1: Safety Testing (Beginners)
1. Start with **Giskard** → `01-giskard/README.md`
2. Run the healthcare scan example
3. Review results and interpret safety scores

### Path 2: Production Guardrails (Intermediate)
1. Learn **NeMo Guardrails** basics → `02-nemo-guardrails/README.md`
2. Deploy the healthcare rails example
3. Customize rails for your use case

### Path 3: Compliance & Documentation (All Levels)
1. Use **Model Cards Toolkit** → `03-model-cards/README.md`
2. Generate model cards for existing models
3. Integrate into CI/CD pipeline

### Path 4: Content Moderation (Intermediate)
1. Deploy **Llama Guard** → `04-llama-guard/README.md`
2. Test with healthcare-specific taxonomy
3. Combine with Giskard for comprehensive testing

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Application Layer                     │
│                  (Your LLM Application)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
┌───────▼──────┐ ┌──▼─────────┐ ┌▼────────────┐
│  Pre-Deploy  │ │  Runtime   │ │Post-Deploy  │
│   Testing    │ │ Guardrails │ │Monitoring   │
└───────┬──────┘ └──┬─────────┘ └┬────────────┘
        │           │             │
  ┌─────▼─────┐ ┌──▼──────────┐  │
  │ Giskard   │ │NeMo Rails   │  │
  │ Scanning  │ │Input/Output │  │
  └───────────┘ │Filtering    │  │
                └─────────────┘  │
  ┌─────────────────────────────▼┐
  │   Model Cards Documentation   │
  │   (Compliance & Governance)   │
  └───────────────────────────────┘
```

## Tool Deep Dives

### [Giskard](./01-giskard/) - LLM Testing & Vulnerability Scanning
- **What**: Automated testing framework for LLMs and ML models
- **Why**: Detect hallucinations, biases, and safety vulnerabilities before deployment
- **Healthcare Strengths**: Clinical context understanding, HIPAA-aware testing scenarios
- **GCP Integration**: Native Vertex AI support via `giskard.llm.VertexAIClient`

**Working Example**: `01-giskard/healthcare_scan.py` - Complete healthcare LLM safety audit

### [NeMo Guardrails](./02-nemo-guardrails/) - Runtime Safety Controls
- **What**: NVIDIA's framework for controlling LLM behavior with programmable rails
- **Why**: Enforce safety policies, prevent jailbreaks, control output boundaries
- **Healthcare Strengths**: Clinical appropriateness checks, PII prevention, scope limiting
- **Language**: Colang (declarative safety rules)

**Working Example**: `02-nemo-guardrails/healthcare_rails/` - Production-ready clinical guardrails

### [Model Cards Toolkit](./03-model-cards/) - Model Documentation
- **What**: Google's framework for structured model documentation
- **Why**: Regulatory compliance, transparency, bias disclosure
- **Healthcare Strengths**: Maps to FDA guidance, supports clinical validation docs

**Working Example**: Linked in README - Gemini model card generation

### [Llama Guard](./04-llama-guard/) - Content Safety Classification
- **What**: Meta's safety classifier for prompt/response filtering
- **Why**: Fast content moderation, multi-category risk detection
- **Healthcare Strengths**: Customizable taxonomy for medical misinformation

**Working Example**: Linked in README - Healthcare taxonomy setup

## Integration Patterns

### Pattern 1: Pre-Deployment Testing Pipeline
```python
# 1. Test with Giskard
from giskard import scan
report = scan(model, dataset, features=["hallucination", "ethics"])

# 2. Generate Model Card
from model_card_toolkit import ModelCardToolkit
mct = ModelCardToolkit()
mct.update_model_card_json(test_results=report)

# 3. Deploy with Guardrails
# (See 02-nemo-guardrails/healthcare_rails/)
```

### Pattern 2: Runtime Protection Stack
```python
# Input → Llama Guard → NeMo Rails → LLM → NeMo Rails → Output
from nemoguardrails import RailsConfig, LLMRails

rails = LLMRails(RailsConfig.from_path("./healthcare_rails"))
response = rails.generate(user_input)  # Auto-filtered
```

### Pattern 3: Continuous Monitoring
```python
# Log all interactions for periodic Giskard re-scanning
import giskard
dataset = giskard.Dataset.from_production_logs("logs/")
scan(model, dataset).to_wandb()  # Track safety metrics over time
```

## Cloud Cost Considerations

| Tool | Vertex AI Calls | Est. Cost (per 1000 tests) |
|------|----------------|---------------------------|
| Giskard | ~50-200 LLM calls | $0.10 - $2.00 |
| NeMo Guardrails | +1 call per user interaction | +$0.001 - $0.01 per user |
| Model Cards | 0 (metadata only) | $0.00 |
| Llama Guard | ~1 classifier call | ~$0.05 |

*Based on Gemini 2.0 Flash pricing (January 2026)*

## Next Steps

1. **Explore Tools**: Browse subfolders for detailed setup guides
2. **Run Examples**: Execute working scripts in each tool directory
3. **Check Notebooks**: See `02-examples/` for end-to-end tutorials
4. **Understand Healthcare Context**: Review `04-healthcare/` for clinical AI risks
5. **Learn Governance**: Check `06-governance/` for regulatory requirements

## Additional Resources

- [Giskard Documentation](https://docs.giskard.ai/)
- [NeMo Guardrails Guide](https://docs.nvidia.com/nemo-guardrails/)
- [Model Cards Paper (Mitchell et al.)](https://arxiv.org/abs/1810.03993)
- [Llama Guard Model Card](https://huggingface.co/meta-llama/LlamaGuard-7b)
- [Vertex AI Safety Guidance](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/responsible-ai)

---

**⚠️ Healthcare Note**: All tools in this folder have been configured with healthcare-specific examples. If you're building clinical AI systems, review `04-healthcare/` for HIPAA compliance considerations before deployment.
