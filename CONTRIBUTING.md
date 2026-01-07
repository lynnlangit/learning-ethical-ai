# 🤝 Contributing to Learning Ethical AI

Thank you for your interest in contributing! As we navigate the **Generative & Agentic Era**, your contributions help ensure that AI systems remain safe, transparent, and aligned with human values.

By contributing to this project, you agree to abide by our [Code of Conduct](https://www.google.com/search?q=CODE_OF_CONDUCT.md) and the following guidelines.

---

## 🏗️ How to Contribute

We welcome contributions in several areas:

* **Code:** Implementing safety filters, red-teaming scripts, or agentic guardrails.
* **Research:** Adding summaries of new 2026 regulations (e.g., updates to the EU AI Act).
* **Data:** Contributing anonymized or synthetic datasets for bias testing.
* **Documentation:** Improving clarity on how to use ethical AI tools like Giskard or PyRIT.

---

## 🤖 AI-Assisted Contributions (Provenance)

In alignment with 2026 open-source standards, we support the use of AI tools (Gemini, GitHub Copilot) to assist your work, but we require transparency:

1. **Marking:** If more than 20% of your contribution is AI-generated, please add a trailer to your commit message:
`Assisted-by: [AI Model Name]` or `Generated-by: [AI Model Name]`
2. **Validation:** You are responsible for the accuracy and safety of AI-generated code. AI-generated contributions must pass all manual red-teaming checks.

---

## 🛡️ Safety & Bias Reporting

If you are contributing a new model or dataset, you must include a **Safety Brief** in your Pull Request:

* **[ ] Bias Analysis:** Did you test the contribution for demographic skew (Race, Gender, Age, Disability)?
* **[ ] Hallucination Rate:** For GenAI contributions, what is the observed "confabulation" rate?
* **[ ] PII/PHI Check:** Does this contribution contain any Personally Identifiable Information or Protected Health Information? (Strictly prohibited for this repo).

---

## 🧬 Special Guidelines for Bioinformatics (Agentic AI)

Given the repository's focus on projects like `precision-medicine-mcp`, all contributions involving clinical agents must:

1. Include a **Human-in-the-Loop (HITL)** trigger for any tool call that suggests medical intervention.
2. Adhere to the **2025 WHO Guidance on Large Multi-Modal Models for Health**.

---

## 🛠️ Pull Request Process

1. **Open an Issue:** Before making a major change, open an issue to discuss your proposal.
2. **Branching:** Use descriptive branch names (e.g., `feature/nist-600-1-compliance`).
3. **Tests:** Ensure your code passes all existing safety benchmarks.
4. **Review:** All PRs require at least one maintainer review. We look specifically for "Safety-by-Design" principles.

---

## 🎓 Recognition

All contributors will be featured in our `CONTRIBUTORS.md` file. For significant research contributions, we are happy to provide citations in a Digital Object Identifier (DOI) format for your academic portfolio.

