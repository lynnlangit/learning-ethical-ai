# Audit Logging for Agentic AI: Decision Chain Tracing

Comprehensive audit logging patterns for tracking AI agent decision-making and tool invocations.

## Why Audit Logging for Agents?

**Use Cases**:
- **Incident investigation**: "Why did the AI delete that patient record?"
- **Compliance**: HIPAA, GDPR, FDA requirements for AI traceability
- **Debugging**: Trace multi-step agent reasoning
- **Security**: Detect anomalous behavior
- **Bias detection**: Analyze decision patterns across demographics

## What to Log

### Minimum Required Fields

```python
audit_log_entry = {
    # WHO
    "user_id": "dr_smith_123",
    "agent_id": "clinical_assistant_v2.1",
    "session_id": "sess_abc123",

    # WHAT
    "action": "search_ehr",
    "parameters": {"query": "diabetes", "max_results": 10},
    "result_summary": "10 records returned",

    # WHEN
    "timestamp": "2026-01-08T14:32:15Z",
    "duration_ms": 234,

    # WHY (agent reasoning)
    "agent_reasoning": "User asked about diabetes prevalence, searching EHR for statistics",
    "user_prompt": "How many patients have diabetes?",

    # CONTEXT
    "tool_call_chain": ["analyze_question", "search_ehr", "aggregate_results"],
    "confidence": 0.92,

    # OUTCOME
    "success": True,
    "errors": None
}
```

## Logging Pattern 1: Decision Chain Tracing

```python
class AgentDecisionTracer:
    def __init__(self):
        self.decision_chain = []

    def log_step(self, step_type: str, inputs: dict, outputs: dict, reasoning: str):
        step = {
            "step_number": len(self.decision_chain) + 1,
            "step_type": step_type,  # "reasoning", "tool_call", "final_answer"
            "inputs": inputs,
            "outputs": outputs,
            "reasoning": reasoning,
            "timestamp": datetime.utcnow()
        }
        self.decision_chain.append(step)

    def get_trace(self):
        return {
            "total_steps": len(self.decision_chain),
            "decision_chain": self.decision_chain,
            "duration": self.calculate_total_duration()
        }

# Usage in AI agent
tracer = AgentDecisionTracer()

# Step 1: Understand query
tracer.log_step(
    step_type="reasoning",
    inputs={"user_query": "How many patients have diabetes?"},
    outputs={"intent": "aggregate_statistics", "entity": "diabetes"},
    reasoning="User wants count, not individual records"
)

# Step 2: Search EHR
tracer.log_step(
    step_type="tool_call",
    inputs={"tool": "search_ehr", "query": "diabetes"},
    outputs={"num_results": 10},
    reasoning="Searching EHR for diabetes diagnoses"
)

# Step 3: Provide answer
tracer.log_step(
    step_type="final_answer",
    inputs={"aggregated_count": 10},
    outputs={"response": "We have 10 patients with diabetes in the database."},
    reasoning="Aggregated results into patient-facing summary"
)

# Save complete trace
audit_log.write(tracer.get_trace())
```

## Logging Pattern 2: HIPAA-Compliant Audit Logs

```python
import logging
import json
from typing import Any

class HIPAACompliantLogger:
    """HIPAA-compliant audit logging for healthcare AI"""

    def __init__(self, log_file="/var/log/hipaa_audit.log"):
        self.logger = logging.getLogger("hipaa_audit")
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_phi_access(
        self,
        user_id: str,
        action: str,
        patient_id: str,  # Or MRN
        purpose: str,  # "treatment", "payment", "operations"
        success: bool,
        ip_address: str
    ):
        """Log PHI access (required by HIPAA Security Rule)"""

        log_entry = {
            "event_type": "phi_access",
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": action,
            "patient_identifier": self.hash_identifier(patient_id),  # Don't log actual ID
            "purpose": purpose,
            "success": success,
            "ip_address": ip_address,
            "user_agent": request.headers.get("User-Agent")
        }

        self.logger.info(json.dumps(log_entry))

        # HIPAA requires 6-year retention
        # Implement log retention policy separately

    @staticmethod
    def hash_identifier(identifier: str) -> str:
        """Hash patient ID for privacy (can still match across logs)"""
        return hashlib.sha256(identifier.encode()).hexdigest()

# Usage
hipaa_logger = HIPAACompliantLogger()

@mcp.tool("view_patient_record")
async def view_patient_record(patient_id: str, user_id: str):
    try:
        record = ehr.get_record(patient_id)

        hipaa_logger.log_phi_access(
            user_id=user_id,
            action="view_patient_record",
            patient_id=patient_id,
            purpose="treatment",
            success=True,
            ip_address=request.remote_addr
        )

        return record

    except Exception as e:
        hipaa_logger.log_phi_access(
            user_id=user_id,
            action="view_patient_record",
            patient_id=patient_id,
            purpose="treatment",
            success=False,
            ip_address=request.remote_addr
        )
        raise
```

## Log Analysis Pattern: Anomaly Detection

```python
# Detect unusual agent behavior from logs
import pandas as pd

def detect_anomalies(audit_logs: list[dict]):
    df = pd.DataFrame(audit_logs)

    # Anomaly 1: Excessive data access
    user_record_counts = df.groupby("user_id")["records_accessed"].sum()
    if (user_record_counts > 1000).any():
        alert("User accessed >1000 records in session - potential exfiltration")

    # Anomaly 2: After-hours access
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    after_hours = df[(df["hour"] < 6) | (df["hour"] > 18)]
    if len(after_hours) > 0:
        alert(f"{len(after_hours)} after-hours PHI accesses detected")

    # Anomaly 3: Failed authorization attempts
    failed_auth = df[df["success"] == False]
    if len(failed_auth) > 5:
        alert(f"Multiple failed auth attempts: {failed_auth['user_id'].unique()}")
```

## Resources
- [HIPAA Audit Log Requirements](../04-healthcare/hipaa-ai-checklist.md)
- [MCP Security Threats](./mcp-security-threats.md) - MCP-08: Insufficient Logging
- [Clinical LLM Risks](../04-healthcare/clinical-llm-risks.md) - Regulatory liability

---

**Key Takeaway**: Comprehensive audit logging is essential for debugging, security, compliance, and trust. Log the WHO, WHAT, WHEN, WHY, and HOW of every AI agent decision.
