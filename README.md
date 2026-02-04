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
> **New for February 2026**: The [2026 International AI Safety Report](https://www.gov.uk/government/publications/international-scientific-report-on-the-safety-of-advanced-ai-interim-report) highlights rapid advancements in AI capabilities and the rising threat of deepfakes.

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

## 🎓 Learning Paths

### Path 1: AI Safety Beginner (Start Here!)

**Goal**: Understand GenAI safety risks and run basic tests

1. **Read**: `04-healthcare/clinical-llm-risks.md` - Understand healthcare AI risks
2. **Practice**: `02-examples/01-giskard-quickstart.ipynb` - Run your first safety scan
3. **Deploy**: `01-tools/01-giskard/healthcare_scan.py` - Audit a clinical LLM
4. **Learn**: `01-tools/02-nemo-guardrails/README.md` - Understand runtime safety

**Time**: 4-6 hours | **Prerequisites**: Basic Python, cloud familiarity

---

### Path 2: Healthcare AI Developer (Clinical Focus)

**Goal**: Build HIPAA-compliant, safe healthcare AI systems

1. **Compliance**: `04-healthcare/hipaa-ai-checklist.md` - HIPAA requirements
2. **Testing**: `02-examples/03-healthcare-llm-safety.ipynb` - Healthcare-specific tests
3. **Guardrails**: `02-examples/04-clinical-guardrails.ipynb` - Deploy clinical safety rails
4. **Genomics**: `04-healthcare/genomics-ethics.md` - Genetic AI ethics (if applicable)
5. **Governance**: `04-healthcare/who-lmm-guidelines.md` - WHO standards
6. **Documentation**: `01-tools/03-model-cards/README.md` - Create compliant model cards

**Time**: 12-16 hours | **Prerequisites**: Healthcare domain knowledge, Python

---

### Path 3: Agentic AI Security Engineer (MCP Focus)

**Goal**: Secure autonomous AI agents and MCP servers

1. **Threats**: `05-agentic-safety/mcp-security-threats.md` - OWASP-style threat taxonomy
2. **Patterns**: `05-agentic-safety/safe-mcp-patterns.md` - Secure MCP development
3. **Practice**: `02-examples/05-mcp-security-audit.ipynb` - Audit an MCP server
4. **Reference**: [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) - Secure MCP implementation
5. **HITL**: `05-agentic-safety/human-in-loop-agents.md` - Human oversight patterns
6. **Logging**: `05-agentic-safety/audit-logging-agents.md` - Decision chain tracing

**Time**: 10-14 hours | **Prerequisites**: Security fundamentals, agentic AI familiarity

---

### Path 4: AI Compliance Officer (Regulatory Focus)

**Goal**: Navigate EU AI Act, NIST, FDA regulations for AI systems

1. **Risk Assessment**: `06-governance/risk-tiering-template.md` - Classify your AI system
2. **EU AI Act**: `06-governance/eu-ai-act-checklist.md` - High-risk system requirements
3. **NIST Framework**: `06-governance/nist-ai-600-1-summary.md` - GenAI risk management
4. **Healthcare**: `04-healthcare/who-lmm-guidelines.md` - WHO LMM standards
5. **Documentation**: `01-tools/03-model-cards/README.md` - Required transparency docs
6. **Testing**: `01-tools/01-giskard/README.md` - Pre-deployment validation

**Time**: 8-12 hours | **Prerequisites**: Regulatory/compliance background

---

### Path 5: Advanced - Multi-Agent Ethics Patterns

**Goal**: Design ethical multi-agent systems with complex tool interactions

1. **Foundation**: Complete Path 3 (Agentic AI Security)
2. **Multi-Agent**: `02-examples/06-agent-ethics-patterns.ipynb` - Multi-agent patterns
3. **Tool Poisoning**: `05-agentic-safety/tool-poisoning-defense.md` - Supply chain security
4. **Testing**: `04-healthcare/synthetic-patient-data.md` - Safe testing data generation
5. **Project**: Build a multi-agent healthcare system with full compliance

**Time**: 20+ hours | **Prerequisites**: All previous paths

---

## 🛠️ Tool Comparison Matrix

| Tool | Primary Use Case | Best For | Setup | Healthcare Support | Getting Started |
|------|-----------------|----------|-------|-------------------|-----------------|
| **Giskard** | LLM testing & vulnerability scanning | Quick safety audits, RAG evaluation, hallucination detection | ⭐⭐ Low | ✅ Excellent | [Guide](01-tools/01-giskard/README.md) |
| **NeMo Guardrails** | Runtime safety controls | Production guardrails, input/output filtering, topic control | ⭐⭐⭐ Medium | ✅ Strong | [Guide](01-tools/02-nemo-guardrails/README.md) |
| **Model Cards Toolkit** | Model documentation & transparency | Compliance documentation, model governance | ⭐ Very Low | ✅ Good | [Guide](01-tools/03-model-cards/README.md) |
| **Llama Guard** | Content moderation | Toxicity filtering, safety classification | ⭐⭐ Low | ⚠️ Limited | [Guide](01-tools/04-llama-guard/README.md) |
| **OpenAI Model Spec** | Behavioral guidelines | Defining intended model behavior | ⭐ Low | ⚠️ Limited | [Spec](https://openai.com/index/model-spec/) |
| **Wallarm for LLMs** | Security & defense | Protecting agents from prompt injection/jailbreaks | ⭐⭐ Low | ✅ Good | [Tool](https://www.wallarm.com/) |

---

## 🏛️ Global Governance & Compliance (2026 Update)

By 2026, AI ethics has transitioned from voluntary principles to enforceable law.

### EU AI Act (Full Enforcement August 2026)

The definitive global benchmark for risk-based AI regulation. It categorizes systems into Unacceptable, High, Limited, and Minimal risk.

- **Official**: [EU AI Act Compliance Tracker](https://artificialintelligenceact.eu/)
- **Implementation Guide**: [06-governance/eu-ai-act-checklist.md](06-governance/eu-ai-act-checklist.md)
- **Actionable for Devs**: Check the [GPAI Code of Practice](https://artificialintelligenceact.eu/high-level-summary/)

### NIST AI 600-1: Generative AI Profile (2025)

A specialized extension of the NIST Risk Management Framework (RMF). It provides 12 high-level risks, including "Confabulation" (Hallucination) and "CBRN" information access.

- **Official**: [NIST AI RMF Resource Center](https://www.nist.gov/itl/ai-risk-management-framework)
- **Summary**: [06-governance/nist-ai-600-1-summary.md](06-governance/nist-ai-600-1-summary.md)

---

## 🤖 Agentic Safety & Security

With the rise of the **Model Context Protocol (MCP)** and multi-agent systems, "ethics" now includes preventing autonomous loop failures and unauthorized tool use.

### MCP Security Resources

- **Threat Taxonomy**: [05-agentic-safety/mcp-security-threats.md](05-agentic-safety/mcp-security-threats.md) - OWASP-style threat model
- **Secure Patterns**: [05-agentic-safety/safe-mcp-patterns.md](05-agentic-safety/safe-mcp-patterns.md) - OpenSSF guidelines
- **Reference Implementation**: [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) - Secure geospatial MCP server
- **Security Audit**: [02-examples/05-mcp-security-audit.ipynb](02-examples/05-mcp-security-audit.ipynb)

### Human-in-the-Loop Best Practices

- **HITL Patterns**: [05-agentic-safety/human-in-loop-agents.md](05-agentic-safety/human-in-loop-agents.md)
- **OECD AI Principles**: [2024/2025 Update](https://oecd.ai/en/dashboards/ai-principles/P7)

---

## 🧬 Bio-Ethics & Precision Medicine

For computational bioinformaticians and healthcare AI developers, ethical AI involves the safe orchestration of synthetic patient data and genomics.

### WHO Guidance on Large Multi-Modal Models (LMMs) for Health (2025)

New standards for transparency and accountability when using Generative AI for disease detection and treatment.

- **Official**: [WHO Health AI Ethics Portal](https://www.who.int/news/item/18-01-2024-who-releases-guidance-on-ai-for-health)
- **Summary**: [04-healthcare/who-lmm-guidelines.md](04-healthcare/who-lmm-guidelines.md)

### Healthcare AI Resources

- **Clinical Risks**: [04-healthcare/clinical-llm-risks.md](04-healthcare/clinical-llm-risks.md) - EHR integration, hallucinations
- **HIPAA Compliance**: [04-healthcare/hipaa-ai-checklist.md](04-healthcare/hipaa-ai-checklist.md)
- **Genomics Ethics**: [04-healthcare/genomics-ethics.md](04-healthcare/genomics-ethics.md) - AI in genetic analysis
- **Synthetic Data**: [04-healthcare/synthetic-patient-data.md](04-healthcare/synthetic-patient-data.md)
- **NIH Guidelines**: [NIH AI Guidelines](https://pmc.ncbi.nlm.nih.gov/articles/PMC12772196/)

---

## ✅ Developer "Ethics-by-Design" Checklist

Before deploying your AI system:

- [ ] **Risk Tiering**: Classify your system using [06-governance/risk-tiering-template.md](06-governance/risk-tiering-template.md)
- [ ] **Safety Testing**: Run Giskard comprehensive scan (see [01-tools/01-giskard/](01-tools/01-giskard/))
- [ ] **Guardrails**: Implement NeMo Guardrails for runtime safety (see [01-tools/02-nemo-guardrails/](01-tools/02-nemo-guardrails/))
- [ ] **Compliance**: Review EU AI Act requirements if deploying in EU (see [06-governance/eu-ai-act-checklist.md](06-governance/eu-ai-act-checklist.md))
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

### Related Projects
- [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) - Secure geospatial MCP server reference

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
