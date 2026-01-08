# 📓 Ethical AI Examples

Hands-on Jupyter notebooks demonstrating practical ethical AI testing, evaluation, and safety practices. All examples are designed for **developers and AI practitioners** building production systems.

---

## 🎯 Learning Paths

| Path | Focus | Time | Prerequisites |
|------|-------|------|---------------|
| **Beginner** | Start with `01-giskard-quickstart.ipynb` → `02-llm-hallucination-detection.ipynb` | ~2 hours | Python, basic LLM concepts |
| **Healthcare** | `03-healthcare-llm-safety.ipynb` → `04-clinical-guardrails.ipynb` | ~3 hours | Beginner path, HIPAA awareness |
| **Agentic AI** | `05-mcp-security-audit.ipynb` → `06-agent-ethics-patterns.ipynb` | ~2 hours | MCP basics, agentic AI concepts |
| **Full Suite** | All notebooks in order | ~8 hours | All prerequisites |

---

## 📂 Notebook Index

| # | Notebook | Description | Tools Used | Difficulty |
|---|----------|-------------|------------|------------|
| 01 | `01-giskard-quickstart.ipynb` | Introduction to Giskard for LLM testing | Giskard, Vertex AI | ⭐ Beginner |
| 02 | `02-llm-hallucination-detection.ipynb` | Detect factual errors and sycophancy in LLMs | Giskard, RAG | ⭐⭐ Intermediate |
| 03 | `03-healthcare-llm-safety.ipynb` | Healthcare-specific LLM safety testing | Giskard, Clinical prompts | ⭐⭐ Intermediate |
| 04 | `04-clinical-guardrails.ipynb` | Implement guardrails for clinical AI assistants | NeMo Guardrails, Vertex AI | ⭐⭐⭐ Advanced |
| 05 | `05-mcp-security-audit.ipynb` | Audit MCP servers for security vulnerabilities | Safe-MCP patterns | ⭐⭐ Intermediate |
| 06 | `06-agent-ethics-patterns.ipynb` | Ethical patterns for agentic AI systems | MCP, HITL design | ⭐⭐⭐ Advanced |

---

## 🔧 Environment Setup

### Prerequisites

```bash
# Python 3.10+ required
python --version

# Google Cloud SDK (for Vertex AI examples)
gcloud --version
```

### Installation

```bash
# Create virtual environment
python -m venv ethical-ai-env
source ethical-ai-env/bin/activate  # Linux/Mac
# ethical-ai-env\Scripts\activate   # Windows

# Install core dependencies
pip install giskard[llm] langchain langchain-google-vertexai pandas jupyter

# For healthcare examples
pip install nemoguardrails

# For MCP examples  
pip install mcp
```

### Google Cloud Setup (for GCP-based examples)

```bash
# Authenticate
gcloud auth application-default login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```

---

## 🏥 Healthcare-Specific Notes

The healthcare examples (`03-*`, `04-*`) are designed with clinical AI safety in mind:

- **HIPAA Considerations**: All examples use synthetic/public data only
- **Clinical Accuracy**: Examples demonstrate testing for medical misinformation
- **Patient Safety**: Guardrail examples focus on preventing harmful medical advice
- **Regulatory Awareness**: References to WHO and NIH AI guidelines included

---

## 🤖 Agentic AI & MCP Notes

The agentic examples (`05-*`, `06-*`) reference the [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) project:

- **Tool Poisoning Defense**: Patterns to prevent malicious tool injection
- **Human-in-the-Loop (HITL)**: When to require human approval for agent actions
- **Audit Logging**: Tracing agent decision chains for accountability
- **Safe-MCP Patterns**: OpenSSF-aligned security configurations

---

## 📚 Additional Resources

| Resource | Description |
|----------|-------------|
| [Giskard Documentation](https://docs.giskard.ai/) | Official Giskard docs |
| [Vertex AI Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs/models) | Google's LLM models |
| [Safe-MCP Project](https://github.com/openssf/safe-mcp) | OpenSSF MCP security framework |
| [NIST AI 600-1](https://www.nist.gov/itl/ai-risk-management-framework) | GenAI risk profile |
| [EU AI Act](https://artificialintelligenceact.eu/) | Regulatory compliance |

---

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on adding new examples.

**Good example contributions include:**
- New vulnerability detection patterns
- Domain-specific testing scenarios (finance, legal, etc.)
- Integration with additional tools (PyRIT, Llama Guard, etc.)
- Multi-language support examples

---

## 📄 License

Apache 2.0 - See [LICENSE](../LICENSE)
