# 🎓 Learning Paths

Choose the path that matches your role and goals.

## Path 1: AI Safety Beginner (Start Here!)
**Goal**: Understand GenAI safety risks and run basic tests

1. **Read**: `04-healthcare/clinical-llm-risks.md` - Understand healthcare AI risks
2. **Practice**: `02-examples/01-giskard-quickstart.ipynb` - Run your first safety scan
3. **Deploy**: `01-tools/01-giskard/healthcare_scan.py` - Audit a clinical LLM
4. **Learn**: `01-tools/02-nemo-guardrails/README.md` - Understand runtime safety

**Time**: 4-6 hours | **Prerequisites**: Basic Python, cloud familiarity

---

## Path 2: Healthcare AI Developer (Clinical Focus)
**Goal**: Build HIPAA-compliant, safe healthcare AI systems

1. **Compliance**: `04-healthcare/hipaa-ai-checklist.md` - HIPAA requirements
2. **Testing**: `02-examples/03-healthcare-llm-safety.ipynb` - Healthcare-specific tests
3. **Guardrails**: `02-examples/04-clinical-guardrails.ipynb` - Deploy clinical safety rails
4. **Genomics**: `04-healthcare/genomics-ethics.md` - Genetic AI ethics (if applicable)
5. **Governance**: `04-healthcare/who-lmm-guidelines.md` - WHO standards
6. **Documentation**: `01-tools/03-model-cards/README.md` - Create compliant model cards

**Time**: 12-16 hours | **Prerequisites**: Healthcare domain knowledge, Python

---

## Path 3: Agentic AI Security Engineer (MCP Focus)
**Goal**: Secure autonomous AI agents and MCP servers

1. **Threats**: `05-agentic-safety/mcp-security-threats.md` - OWASP-style threat taxonomy
2. **Patterns**: `05-agentic-safety/safe-mcp-patterns.md` - Secure MCP development
3. **Practice**: `02-examples/05-mcp-security-audit.ipynb` - Audit an MCP server
4. **Reference**: [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) - Secure geospatial MCP implementation
5. **HITL**: `05-agentic-safety/human-in-loop-agents.md` - Human oversight patterns
6. **Logging**: `05-agentic-safety/audit-logging-agents.md` - Decision chain tracing

**Time**: 10-14 hours | **Prerequisites**: Security fundamentals, agentic AI familiarity

---

## Path 4: AI Compliance Officer (Regulatory Focus)
**Goal**: Navigate EU AI Act, NIST, FDA regulations for AI systems

1. **Risk Assessment**: `06-governance/risk-tiering-template.md` - Classify your AI system
2. **EU AI Act**: `06-governance/eu-ai-act-checklist.md` - High-risk system requirements
3. **NIST Framework**: `06-governance/nist-ai-600-1-summary.md` - GenAI risk management
4. **Healthcare**: `04-healthcare/who-lmm-guidelines.md` - WHO LMM standards
5. **Documentation**: `01-tools/03-model-cards/README.md` - Required transparency docs
6. **Testing**: `01-tools/01-giskard/README.md` - Pre-deployment validation

**Time**: 8-12 hours | **Prerequisites**: Regulatory/compliance background

---

## Path 5: Advanced - Multi-Agent Ethics Patterns
**Goal**: Design ethical multi-agent systems with complex tool interactions

1. **Foundation**: Complete Path 3 (Agentic AI Security)
2. **Multi-Agent**: `02-examples/06-agent-ethics-patterns.ipynb` - Multi-agent patterns
3. **Tool Poisoning**: `05-agentic-safety/tool-poisoning-defense.md` - Supply chain security
4. **Testing**: `04-healthcare/synthetic-patient-data.md` - Safe testing data generation
5. **Project**: Build a multi-agent healthcare system with full compliance

**Time**: 20+ hours | **Prerequisites**: All previous paths
