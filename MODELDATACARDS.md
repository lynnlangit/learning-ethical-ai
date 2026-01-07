# 📑 Model & Data Cards: The "AI Nutrition Label"

In the **Generative & Agentic Era**, transparency is not just an ethical goal—it is a regulatory requirement under the **EU AI Act** and **NIST AI RMF 1.0/2025**. This page provides templates for documenting the "what," "how," and "why" of your AI systems.

---

## 🏗️ 1. The Model Card (Architecture & Safety)

A Model Card provides a standardized overview of a model's design, intended use, and known safety limitations.

### Template: Agentic Bioinformatics Model

> **Use Case Example:** `precision-medicine-mcp` Orchestrator

| Section | Description | 2026 Best Practice |
| --- | --- | --- |
| **Model Details** | Basic metadata (Model name, version, architecture). | Include **MCP Protocol** compatibility. |
| **Intended Use** | What the model *should* and *should not* do. | Specify "Non-clinical use" if not FDA/EMA cleared. |
| **Training Domain** | The specific data distribution used. | Note if the model was fine-tuned on **Genomic/Omic** data. |
| **Safety Guardrails** | Configured thresholds (e.g., Vertex AI Safety). | Document **Jailbreak/Prompt Injection** resilience. |
| **Explainability** | How the model reaches its conclusions. | Link to **Chain-of-Thought (CoT)** reasoning logs. |

---

## 🧬 2. The Data Card (Provenance & Privacy)

A Data Card is essential when handling sensitive biological or synthetic patient data. It documents the "life of the data" before it ever hits a model.

### Template: Synthetic Patient Genomic Data

> **Use Case Example:** Synthetic datasets for `PatientOne` POC

* **Dataset Overview:** Description of the synthetic cohort (e.g., "5,000 synthetic stage-IV oncology records").
* **Provenance:** How was this data generated? (e.g., "Generative Adversarial Network trained on anonymized NIH dataset").
* **Privacy Preservation:**
* **K-Anonymity:** Specify the  value.
* **Differential Privacy:** Note the  (epsilon) budget used during generation.


* **Representativeness:** Does the data contain a balanced distribution of race, age, and gender to prevent "Medical Bias"?
* **Human Review:** Was the synthetic data validated by a certified bioinformatician?

---

## 🛠️ Implementation Guide: "Self-Auditing"

To improve the quality of your builds, we recommend a **Three-Step Audit** for every new feature:

1. **Map:** Use the Data Card to map where the information came from.
2. **Measure:** Use the Model Card to measure performance against **NIST AI 600-1** safety categories.
3. **Manage:** Implement "Human-in-the-loop" triggers for any high-confidence/high-impact clinical suggestions.

---

## Script Example

```
"""
Model & Data Card Generator (2026 Edition)
This script interactively generates a 'MODELDATACARD.md' file.
Standardized for NIST AI 600-1 and EU AI Act compliance.
"""

import datetime

def get_input(prompt, default="No information provided"):
    user_val = input(f"{prompt} [{default}]: ").strip()
    return user_val if user_val else default

def generate_card():
    print("--- 🛡️ Ethical AI Documentation Generator ---")
    
    # 1. Model Metadata
    model_name = get_input("Model/Agent Name", "precision-medicine-mcp")
    version = get_input("Version", "1.0.0")
    risk_tier = get_input("EU AI Act Risk Tier (Unacceptable, High, Limited, Minimal)", "High")
    
    # 2. Safety & Governance
    safety_threshold = get_input("NIST AI 600-1 Safety Category (e.g., Dangerous Content)", "Dangerous Content")
    jailbreak_resilience = get_input("Jailbreak Protection Level (Low, Med, High)", "High")
    
    # 3. Data Provenance
    data_source = get_input("Data Source (Synthetic/Real/Mixed)", "Synthetic")
    privacy_tech = get_input("Privacy Protection (Differential Privacy/K-Anonymity)", "Differential Privacy")
    
    # Markdown Template
    markdown_content = f"""# 📑 Model & Data Card: {model_name}
*Generated on: {datetime.date.today()}*

---

## 🏛️ Governance & Risk
| Attribute | Value |
| :--- | :--- |
| **Version** | {version} |
| **Risk Tier** | {risk_tier} |
| **Safety Standard** | NIST AI 600-1 |

## 🛡️ Model Safety Features
- **Primary Safety Category:** {safety_threshold}
- **Jailbreak Resilience:** {jailbreak_resilience}
- **Agentic Loop Protection:** Enabled (Human-in-the-Loop required for tool execution)

## 🧬 Data Provenance & Ethics
- **Source Type:** {data_source}
- **Privacy Methodology:** {privacy_tech}
- **Bias Mitigation:** disaggregated evaluation across 5 demographic variables.

---
*This document is a requirement for compliance with the Learning Ethical AI framework (2026).*
"""

    with open("MODELDATACARD_DEMO.md", "w") as f:
        f.write(markdown_content)
    
    print("\n✅ Success! 'MODELDATACARD_DEMO.md' has been generated in your directory.")

if __name__ == "__main__":
    generate_card()
```
----

## 📚 Resources & Tools

* **[Hugging Face Model Card Creator](https://huggingface.co/docs/hub/model-card-guidebook):** The industry standard for open-source model documentation.
* **[Google Data Cards Playbook](https://sites.research.google/datacardsplaybook/):** A toolkit for transparency in dataset documentation.
* **[NIST AI RMF Playbook (2025)](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook):** Practical suggestions for achieving the "Measure" and "Manage" functions.

---


Would you like me to create a **Python script** that automatically generates a skeleton `MODELDATACARD.md` for a user based on a series of interactive terminal prompts?
