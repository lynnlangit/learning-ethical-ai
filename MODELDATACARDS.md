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

## 📚 Resources & Tools

* **[Hugging Face Model Card Creator](https://huggingface.co/docs/hub/model-card-guidebook):** The industry standard for open-source model documentation.
* **[Google Data Cards Playbook](https://sites.research.google/datacardsplaybook/):** A toolkit for transparency in dataset documentation.
* **[NIST AI RMF Playbook (2025)](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook):** Practical suggestions for achieving the "Measure" and "Manage" functions.

---

### Next Step

Would you like me to create a **Python script** that automatically generates a skeleton `MODELDATACARD.md` for a user based on a series of interactive terminal prompts?
