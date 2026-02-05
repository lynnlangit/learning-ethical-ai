# Learning Ethical AI

![Ethical AI Repository](https://github.com/lynnlangit/learning-ethical-ai/blob/main/images/ethical-ai-repo.jpeg)

[![Last Updated](https://img.shields.io/badge/Last%20Updated-February%202026-blue)](https://github.com/lynnlangit/learning-ethical-ai)
[![Python](https://img.shields.io/badge/Python-3.11+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![GCP](https://img.shields.io/badge/Cloud-GCP%20Vertex%20AI-orange)](https://cloud.google.com/vertex-ai)

---

## 🛡️ Ethical AI: The 2026 Resource Guide

This guide provides essential technical and regulatory updates for developers and AI practitioners building in the **Generative & Agentic Era (2024–2026)**.

> [!IMPORTANT]
> **New for February 2026**: The [2026 International AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) highlights rapid advancements in AI capabilities and the rising threat of deepfakes.

## 📂 Repository Structure

```
learning-ethical-ai/
│
├── 01-tools/                    # AI safety and ethics tools
│   ├── README.md                  # Tool comparison matrix, quick start
│   ├── 01-giskard/                   # LLM testing & vulnerability scanning
│   │   ├── README.md
│   │   ├── config_vertexai.py     # GCP Vertex AI configuration
│   │   └── healthcare_scan.py     # Working healthcare LLM audit
│   ├── 02-nemo-guardrails/          # Runtime safety controls
│   │   ├── README.md
│   │   └── healthcare_rails/      # Production-ready clinical guardrails
│   ├── 03-model-cards/              # Model documentation & transparency
│   │   └── README.md
│   └── 04-llama-guard/              # Content safety classification
│       └── README.md
│
├── 02-examples/                 # Jupyter notebooks (6 complete examples)
│   ├── README.md
│   ├── requirements.txt
│   ├── 01-giskard-quickstart.ipynb
│   ├── 02-llm-hallucination-detection.ipynb
│   ├── 03-healthcare-llm-safety.ipynb
│   ├── 04-clinical-guardrails.ipynb
│   ├── 05-mcp-security-audit.ipynb
│   └── 06-agent-ethics-patterns.ipynb
│
├── 04-healthcare/               # Healthcare-specific AI ethics
│   ├── clinical-llm-risks.md      # EHR integration risks, hallucinations
│   ├── hipaa-ai-checklist.md      # HIPAA compliance for AI
│   ├── genomics-ethics.md         # Ethical AI in genetic analysis
│   ├── who-lmm-guidelines.md      # WHO 2025 LMM guidance summary
│   └── synthetic-patient-data.md  # Safe synthetic data generation
│
├── 05-agentic-safety/           # MCP and agentic AI security
│   ├── mcp-security-threats.md    # OWASP-style MCP threat taxonomy
│   ├── safe-mcp-patterns.md       # OpenSSF Safe-MCP security patterns
│   ├── human-in-loop-agents.md    # HITL design for high-risk actions
│   ├── tool-poisoning-defense.md  # Defense strategies
│   └── audit-logging-agents.md    # Agent decision chain tracing
│
├── 06-governance/               # Regulatory compliance resources
│   ├── eu-ai-act-checklist.md     # High-risk system requirements
│   ├── nist-ai-600-1-summary.md   # GenAI risk profile summary
│   └── risk-tiering-template.md   # AI system risk classification
│
└── README.md                    # This file
```

---

## 🚀 Quick Start

### Install Dependencies

```bash
# Clone repository
git clone https://github.com/lynnlangit/learning-ethical-ai.git
cd learning-ethical-ai

# Install tools
pip install giskard nemoguardrails model-card-toolkit

# Configure GCP (required for examples)
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1"
```

### Run Your First Safety Scan

```bash
cd 01-tools/giskard
python healthcare_scan.py
# Opens HTML report with safety analysis
```

### Explore Jupyter Notebooks

```bash
cd 02-examples
pip install -r requirements.txt
jupyter notebook
# Start with 01-giskard-quickstart.ipynb
```

---

---

## 📚 Documentation Index

| Topic | Description | Link |
|-------|-------------|------|
| **🎓 Learning Paths** | Step-by-step guides for different roles (Beginner, Dev, Security, Compliance) | [Start Learning →](LEARNING_PATHS.md) |
| **🧪 Tools** | Giskard, NeMo Guardrails, Wallarm, Model Cards setup | [View Tools →](01-tools/README.md) |
| **🧬 Healthcare** | WHO guidelines, HIPAA, Genomics, Clinical Risks | [View Healthcare →](04-healthcare/README.md) |
| **🤖 Agentic Safety** | MCP Security, Threats, HITL, Tool Poisoning | [View Agent Security →](05-agentic-safety/README.md) |
| **🏛️ Governance** | EU AI Act, NIST, US Courts, State Laws | [View Governance →](06-governance/README.md) |

---

## ✅ Developer "Ethics-by-Design" Checklist

Before deploying your AI system:

- [ ] **Risk Tiering**: Classify your system using [06-governance/risk-tiering-template.md](06-governance/risk-tiering-template.md)
- [ ] **Safety Testing**: Run Giskard comprehensive scan (see [01-tools/01-giskard/](01-tools/01-giskard/))
- [ ] **Guardrails**: Implement NeMo Guardrails for runtime safety (see [01-tools/02-nemo-guardrails/](01-tools/02-nemo-guardrails/))
- [ ] **Compliance**: Review EU AI Act requirements if deploying in EU (see [06-governance/eu-ai-act-checklist.md](06-governance/eu-ai-act-checklist.md))
- [ ] **Legal/Courts**: Check US Court AI Rules if building legal tech (see [06-governance/us-court-ai-justice.md](06-governance/us-court-ai-justice.md))
- [ ] **Healthcare**: If clinical use, check HIPAA compliance (see [04-healthcare/hipaa-ai-checklist.md](04-healthcare/hipaa-ai-checklist.md))
- [ ] **Agentic**: If using MCP, audit security (see [05-agentic-safety/mcp-security-threats.md](05-agentic-safety/mcp-security-threats.md))
- [ ] **Human Oversight**: Implement HITL for high-risk actions (see [05-agentic-safety/human-in-loop-agents.md](05-agentic-safety/human-in-loop-agents.md))
- [ ] **Documentation**: Create Model Card (see [01-tools/03-model-cards/](01-tools/03-model-cards/))
- [ ] **Audit Logging**: Enable comprehensive logging (see [05-agentic-safety/audit-logging-agents.md](05-agentic-safety/audit-logging-agents.md))

---

## 🔗 Key Resources

### Official Guidelines
- [EU AI Act](https://artificialintelligenceact.eu/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [WHO LMM Guidance](https://www.who.int/publications/i/item/9789240084759)
- [OECD AI Principles](https://oecd.ai/en/dashboards/ai-principles)

### Tools & Frameworks
- [Giskard](https://github.com/Giskard-AI/giskard) - LLM testing
- [NeMo Guardrails](https://docs.nvidia.com/nemo-guardrails/) - Runtime safety
- [OpenSSF Safe-MCP](https://github.com/openssf/safe-mcp) - MCP security
- [Model Cards Toolkit](https://github.com/tensorflow/model-card-toolkit)

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**Lynn Langit**
- Background: Mayo Clinic / Genomics
- Focus: Healthcare AI ethics, cloud architecture, precision medicine
- GitHub: [@lynnlangit](https://github.com/lynnlangit)

---

## 💬 Chat with this Repo (NotebookLM)

You can use Google's **NotebookLM** to turn this repository into an interactive expert that answers your questions.

1.  Go to [NotebookLM](https://notebooklm.google.com/).
2.  Create a new notebook.
3.  Click **Add Source** > **GitHub** (or paste the repo URL: `https://github.com/lynnlangit/learning-ethical-ai`).
4.  Select this repository.

**Try asking:**
- *"What are the new HIPAA requirements for AI?"*
- *"Summarize the MCP security threats."*
- *"Create a checklist for EU AI Act compliance."*
- *"Listen to the Audio Overview for a podcast-style summary."*

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

For major changes, please open an issue first to discuss proposed changes.

---

**Last Updated**: January 2026
**Status**: Active development - Repository reflects current 2026 standards for ethical AI
