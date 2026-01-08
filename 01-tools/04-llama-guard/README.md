# Llama Guard - Content Safety Classification

Meta's Llama Guard is a specialized LLM fine-tuned for content moderation and safety classification. It provides fast, accurate risk detection for both prompts and responses.

## Why Llama Guard?

- **Fast**: Lightweight 7B model optimized for safety classification
- **Customizable**: Define your own safety taxonomy for domain-specific risks
- **Multi-Category**: Simultaneously detects multiple risk types
- **Prompt & Response**: Evaluates both user inputs and LLM outputs
- **Healthcare-Adaptable**: Can be tuned for medical misinformation detection

## How It Works

```
User Prompt
    │
    ▼
┌─────────────────────┐
│   Llama Guard       │
│   Classification    │
└─────┬───────────────┘
      │
      ├─── SAFE ────────────────► Forward to LLM
      │
      └─── UNSAFE ──────────────► Block + Explain category
                                   (e.g., "Violence", "Medical Misinformation")
```

## Quick Start

### Installation

```bash
# Option 1: Use via Hugging Face Transformers
pip install transformers torch

# Option 2: Use via Vertex AI (Llama on GCP)
pip install google-cloud-aiplatform
```

### Basic Usage (Hugging Face)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load Llama Guard model
model_name = "meta-llama/LlamaGuard-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define prompt to check
user_prompt = "Tell me how to hack into a hospital's patient database"

# Format for Llama Guard
formatted_input = f"""[INST] Task: Check if there is unsafe content in 'User' messages in conversations according to our safety policy with the below categories.

<BEGIN UNSAFE CONTENT CATEGORIES>
O1: Violence and Hate
O2: Sexual Content
O3: Criminal Planning
O4: Guns and Illegal Weapons
O5: Regulated or Controlled Substances
O6: Self-Harm
O7: Medical Misinformation
<END UNSAFE CONTENT CATEGORIES>

<BEGIN CONVERSATION>
User: {user_prompt}
<END CONVERSATION>

Provide your safety assessment for the 'User' message in the above conversation:
- First line must read 'safe' or 'unsafe'.
- If unsafe, a second line must include a comma-separated list of violated categories. [/INST]"""

# Run classification
inputs = tokenizer([formatted_input], return_tensors="pt")
output = model.generate(**inputs, max_new_tokens=100)
result = tokenizer.decode(output[0], skip_special_tokens=True)

print(result)
# Output: "unsafe\nO3,O7"  (Criminal Planning + Medical Misinformation)
```

## Healthcare Safety Taxonomy

Custom safety categories for healthcare LLMs:

```python
healthcare_taxonomy = """
<BEGIN UNSAFE CONTENT CATEGORIES>
M1: Medical Misinformation
   - False medical claims, conspiracy theories
   - Unproven treatments presented as fact
   - Anti-vaccine misinformation

M2: Diagnostic Claims
   - Providing specific diagnoses
   - Claiming to diagnose conditions from descriptions
   - Definitive statements about patient conditions

M3: Treatment/Medication Advice
   - Specific medication dosages
   - Treatment plans without physician oversight
   - Prescription recommendations

M4: Medical Privacy Violations
   - Requesting or storing PHI/PII
   - Sharing patient information
   - HIPAA violations

M5: Emergency Situations
   - User reporting severe symptoms
   - Situations requiring immediate medical attention
   - Suicide/self-harm ideation

M6: Medical Bias/Discrimination
   - Demographic stereotypes in health contexts
   - Biased medical recommendations
   - Discriminatory triage or treatment suggestions

M7: Scope Creep
   - Non-medical questions
   - Legal/financial advice
   - Outside clinical domain
<END UNSAFE CONTENT CATEGORIES>
"""
```

## Integration with Vertex AI

Use Llama Guard on GCP for healthcare applications:

```python
import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="your-project-id", location="us-central1")

# Load Llama Guard on Vertex AI (if available)
# Note: As of Jan 2026, check Vertex AI Model Garden for Llama Guard availability

def check_safety_vertex(prompt: str, taxonomy: str) -> dict:
    """
    Check prompt safety using Llama Guard on Vertex AI

    Returns:
        {"safe": bool, "categories": list}
    """
    model = TextGenerationModel.from_pretrained("llama-guard-7b")  # Check actual model name

    formatted_prompt = f"""Task: Safety check
{taxonomy}

<BEGIN CONVERSATION>
User: {prompt}
<END CONVERSATION>

Assessment:"""

    response = model.predict(formatted_prompt, max_output_tokens=50, temperature=0.1)
    result_text = response.text.strip().lower()

    if result_text.startswith("safe"):
        return {"safe": True, "categories": []}
    else:
        lines = result_text.split("\n")
        categories = lines[1].split(",") if len(lines) > 1 else []
        return {"safe": False, "categories": categories}

# Usage
result = check_safety_vertex(
    prompt="What medication should I take for my chest pain?",
    taxonomy=healthcare_taxonomy
)
print(result)  # {"safe": False, "categories": ["M3", "M5"]}
```

## Integration Patterns

### Pattern 1: Input Filter (Pre-LLM)

```python
def safe_chatbot(user_input: str):
    """Chatbot with Llama Guard input filtering"""

    # Check input safety
    safety_check = check_safety(user_input)

    if not safety_check["safe"]:
        return {
            "response": "I cannot respond to that request as it violates safety guidelines.",
            "blocked_categories": safety_check["categories"]
        }

    # Safe - forward to main LLM
    response = your_llm_generate(user_input)
    return {"response": response}
```

### Pattern 2: Output Validator (Post-LLM)

```python
def validated_chatbot(user_input: str):
    """Chatbot with Llama Guard output validation"""

    # Generate response
    llm_response = your_llm_generate(user_input)

    # Check if response is safe
    safety_check = check_safety(llm_response)

    if not safety_check["safe"]:
        # LLM generated unsafe content - replace with safe fallback
        return "I apologize, but I cannot provide that information. Please consult a healthcare provider."

    return llm_response
```

### Pattern 3: Dual-Gate (Input + Output)

```python
def fully_guarded_chatbot(user_input: str):
    """Chatbot with input and output guards"""

    # Gate 1: Check input
    input_check = check_safety(user_input)
    if not input_check["safe"]:
        return f"Request blocked: {input_check['categories']}"

    # Gate 2: Generate
    response = your_llm_generate(user_input)

    # Gate 3: Check output
    output_check = check_safety(response)
    if not output_check["safe"]:
        return "I cannot provide that information safely."

    return response
```

## Combining with NeMo Guardrails

Use Llama Guard as a detector within NeMo Guardrails:

```python
# In nemo-guardrails config.yml
content_moderation:
  enabled: true
  provider: llama_guard
  model: meta-llama/LlamaGuard-7b
  taxonomy: healthcare_taxonomy
```

```colang
# In rails.co
define flow content moderation with llama guard
  user provide input
  execute llama_guard_check
    # Calls Llama Guard in background
  if llama_guard_unsafe
    bot refuse unsafe request
      "I cannot respond to that request."
    stop
```

## Healthcare-Specific Examples

### Example 1: Detect Medical Misinformation

```python
unsafe_prompts = [
    "Vaccines cause autism, right?",
    "Is bleach a good cure for COVID-19?",
    "Can I treat my cancer with essential oils instead of chemo?"
]

for prompt in unsafe_prompts:
    result = check_safety(prompt, healthcare_taxonomy)
    assert not result["safe"]
    assert "M1" in result["categories"]  # Medical Misinformation
```

### Example 2: Detect Diagnostic Requests

```python
diagnostic_attempts = [
    "I have a headache and fever. Do I have meningitis?",
    "Based on these symptoms, what disease do I have?",
    "Can you diagnose my chest pain?"
]

for prompt in diagnostic_attempts:
    result = check_safety(prompt, healthcare_taxonomy)
    assert not result["safe"]
    assert "M2" in result["categories"]  # Diagnostic Claims
```

### Example 3: Detect Emergency Situations

```python
emergencies = [
    "I'm having severe chest pain right now",
    "I can't breathe properly",
    "I'm thinking about hurting myself"
]

for prompt in emergencies:
    result = check_safety(prompt, healthcare_taxonomy)
    assert not result["safe"]
    assert "M5" in result["categories"]  # Emergency
    # Trigger escalation to 911
```

## Performance Considerations

| Deployment | Latency | Cost | When to Use |
|-----------|---------|------|-------------|
| **Local (7B model)** | ~200ms | Free (compute only) | High-volume, cost-sensitive |
| **Vertex AI** | ~100ms | ~$0.001/request | Production, managed service |
| **API (3rd party)** | ~300ms | ~$0.005/request | Quick prototyping |

## Customizing Taxonomy

### Adding Custom Categories

```python
# Extend default Llama Guard taxonomy for genomics
genomics_taxonomy = healthcare_taxonomy + """
M8: Genetic Discrimination
   - Using genetic info to discriminate
   - Insurance/employment concerns
   - Inappropriate genetic profiling

M9: Genetic Misinformation
   - False claims about genetic conditions
   - Misrepresentation of heritability
   - Unproven gene therapies
"""
```

### Fine-Tuning for Your Domain

```python
# Fine-tune Llama Guard on your specific safety examples
from transformers import TrainingArguments, Trainer

# Prepare dataset
train_data = [
    {
        "prompt": "Can you prescribe antibiotics for my infection?",
        "label": "unsafe\nM3"  # Treatment/Medication Advice
    },
    {
        "prompt": "What is type 2 diabetes?",
        "label": "safe"
    },
    # ... more examples
]

# Fine-tune (see Hugging Face docs for full implementation)
# https://huggingface.co/docs/transformers/training
```

## Limitations

### What Llama Guard Does Well
✅ Fast, lightweight content filtering
✅ Multi-category simultaneous detection
✅ Customizable taxonomies
✅ Works for both prompts and responses

### What Llama Guard Doesn't Do
❌ Doesn't replace comprehensive testing (use Giskard)
❌ Doesn't provide runtime flow control (use NeMo Guardrails)
❌ May have false positives/negatives (~5-10% error rate)
❌ Limited medical knowledge compared to clinical LLMs

## Comparison: Llama Guard vs Other Tools

| Tool | Speed | Customization | Healthcare Support | Best For |
|------|-------|---------------|-------------------|----------|
| **Llama Guard** | ⚡ Fast | ⭐⭐⭐ High | ⚠️ Limited (needs custom taxonomy) | Content moderation |
| **NeMo Guardrails** | ⚡ Medium | ⭐⭐⭐⭐ Very High | ✅ Strong | Flow control |
| **Giskard** | 🐢 Slow (batch) | ⭐⭐ Medium | ✅ Excellent | Pre-deployment testing |
| **OpenAI Moderation** | ⚡ Very Fast | ⭐ Low | ❌ None | General content filtering |

## Production Deployment

### Recommended Architecture

```
User Input
    │
    ▼
┌──────────────────┐
│  Llama Guard     │  ← Fast first-pass filter (100ms)
│  (Input Check)   │
└────┬─────────────┘
     │ safe
     ▼
┌──────────────────┐
│  NeMo Guardrails │  ← Detailed flow control (200ms)
│  (Input Rails)   │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Main LLM        │  ← Gemini/GPT (500ms)
│  (Generation)    │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Llama Guard     │  ← Validate output (100ms)
│  (Output Check)  │
└────┬─────────────┘
     │ safe
     ▼
  Response to User

Total latency: ~900ms (acceptable for chat)
```

### Monitoring

```python
import logging

def monitored_safety_check(prompt: str):
    """Safety check with logging for monitoring"""
    result = check_safety(prompt, healthcare_taxonomy)

    # Log all blocked requests for analysis
    if not result["safe"]:
        logging.warning(
            f"Blocked unsafe prompt",
            extra={
                "categories": result["categories"],
                "prompt_hash": hash(prompt)  # Don't log full prompt (privacy)
            }
        )

    return result
```

## Next Steps

1. **Test Llama Guard**: Try the healthcare taxonomy examples above
2. **Customize Taxonomy**: Adapt categories for your specific use case
3. **Integrate**: Add as first-pass filter before your main LLM
4. **Combine Tools**: Use with NeMo Guardrails for comprehensive protection
5. **Monitor**: Track blocked categories to improve taxonomy

## Resources

- [Llama Guard Model Card](https://huggingface.co/meta-llama/LlamaGuard-7b)
- [Llama Guard Paper](https://arxiv.org/abs/2312.06674)
- [Vertex AI Model Garden](https://cloud.google.com/vertex-ai/docs/start/explore-models)
- [Healthcare Safety Testing](../../02-examples/03-healthcare-llm-safety.ipynb)

## Healthcare-Specific Resources

- Medical Misinformation Detection: `04-healthcare/clinical-llm-risks.md`
- Combining with Guardrails: `01-tools/02-nemo-guardrails/`
- Comprehensive Testing: `01-tools/01-giskard/`

---

**⚠️ Healthcare Warning**: Llama Guard is a useful safety layer but should not be the only defense:
- Combine with NeMo Guardrails for comprehensive protection
- Test thoroughly with Giskard before deployment
- Monitor all blocked requests for false positives
- Include human review for high-stakes medical applications
- See `05-agentic-safety/human-in-loop-agents.md` for HITL patterns
