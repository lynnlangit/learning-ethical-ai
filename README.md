# Learning Ethical AI


This guide pivots from ["Classical ML Fairness" (detecting bias in tables)](https://github.com/lynnlangit/learning-ethical-ai/blob/main/Background.md) to **Generative and Agentic Ethics** (securing autonomous reasoning and healthcare deployments).

---

# 🛡️ Ethical AI: The 2026 Resource Guide

This guide provides the essential technical and regulatory updates for developers and architects building in the **Generative & Agentic Era (2024–2026)**.

---

## 🏛️ 1. Global Governance & Compliance

By 2026, AI ethics has transitioned from voluntary principles to enforceable law.

* **EU AI Act (Full Enforcement August 2026):** The definitive global benchmark for risk-based AI regulation. It categorizes systems into Unacceptable, High, Limited, and Minimal risk.
* [Official EU AI Act Compliance Tracker](https://artificialintelligenceact.eu/)
* **Actionable for Devs:** Check the [GPAI Code of Practice](https://artificialintelligenceact.eu/high-level-summary/) released in 2025 for General Purpose AI models.


* **NIST AI 600-1: Generative AI Profile (2025):** A specialized extension of the NIST Risk Management Framework (RMF). It provides 12 high-level risks, including "Confabulation" (Hallucination) and "CBRN" (Chemical/Biological risk) information access.
* [NIST AI RMF Resource Center](https://www.nist.gov/itl/ai-risk-management-framework)



---

## 🤖 2. Agentic Safety & Security

With the rise of the **Model Context Protocol (MCP)** and multi-agent systems, "ethics" now includes preventing autonomous loop failures and unauthorized tool use.

* **Frontier Safety Framework (2025):** The shared safety protocols used by major labs (Google, Anthropic) to mitigate risks in models with high autonomous capabilities.
* [Google AI Responsibility Reports](https://www.google.com/search?q=https://ai.google/responsibility/reports/)


* **Agentic Loop Monitoring:** Best practices for 2026 focus on "Explainability-by-Design" in agent reasoning steps (Chain-of-Thought) and tool-calling logs.
* [OECD AI Principles - 2024/2025 Update](https://oecd.ai/en/dashboards/ai-principles/P7)



---

## 🧬 3. Bio-Ethics & Precision Medicine

For computational bioinformaticians, ethical AI involves the safe orchestration of synthetic patient data and omics.

* **WHO Guidance on Large Multi-Modal Models (LMMs) for Health (March 2025):** New standards for transparency and accountability when using Generative AI for disease detection and treatment.
* [WHO Health AI Ethics Portal](https://www.google.com/search?q=https://www.who.int/news/item/18-01-2024-who-releases-guidance-on-ai-for-health)


* **NIH Ethical AI in Medical Research:** Guidelines for handling privacy in the age of AI-driven genomic analysis.
* [NIH AI Guidelines](https://pmc.ncbi.nlm.nih.gov/articles/PMC12772196/)



---

## 🛠️ 4. The 2026 Ethical AI Toolkit

Modern alternatives to classical fairness tools, focusing on **Red Teaming** and **Safety Evaluators**.

| Tool | Primary Use | Why it's in the 2026 Stack |
| --- | --- | --- |
| **Giskard** | Automated Red Teaming | Best for dynamic, multi-turn stress tests for AI Agents. |
| **Microsoft PyRIT** | Risk Identification | An open-source Python framework for proactive red-teaming of LLMs. |
| **Vera (WhyLabs)** | Production Guardrails | Real-time monitoring for hallucinations and safety breaches in clinical apps. |
| **C2PA / Content Auth** | Content Provenance | The 2026 standard for watermarking and certifying AI-generated media. |

* **Source Links:**
* [Giskard GitHub](https://www.google.com/search?q=https://github.com/Giskard-AI/giskard)
* [PyRIT GitHub](https://github.com/Azure/PyRIT)
* [C2PA Standard](https://c2pa.org/)



---

## ✅ Developer "Ethics-by-Design" Checklist

* [ ] **Risk Tiering:** Identify if your app falls under the "High-Risk" category of the EU AI Act (e.g., healthcare diagnostics).
* [ ] **Prompt Injection Shielding:** Implement safety filters at the system prompt level (NIST AI 600-1).
* [ ] **Agentic Permissioning:** For MCP tools, require Human-in-the-Loop (HITL) for any "Yellow-Light" actions (e.g., modifying patient records).
* [ ] **Output Watermarking:** Use C2PA standards if your AI generates patient-facing reports or educational images.

---

**Next Step:** Would you like me to generate a specific Python script that you can add to your repo as a "Hands-On" example, showing how to implement these 2026 safety filters using the Google Gen AI SDK?
