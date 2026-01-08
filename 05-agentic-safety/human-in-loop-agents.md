# Human-in-the-Loop (HITL) Patterns for Agentic AI

Design patterns for integrating human oversight into autonomous AI agents, particularly for high-risk healthcare and enterprise applications.

## When HITL is Required

**High-Risk Actions** (always require human approval):
- Clinical decisions (diagnosis, treatment, medication)
- Data deletion or modification
- Financial transactions > threshold
- Policy/configuration changes
- Communications to external parties

**Decision Framework**:
```
Risk = Impact × Irreversibility × Uncertainty

If Risk > Threshold → Require HITL
```

## HITL Pattern 1: Approval Gates

```python
class ApprovalGate:
    async def request_approval(self, action: dict, approvers: list[str]):
        request = {
            "action": action,
            "reason": action.get("justification"),
            "requested_at": datetime.utcnow(),
            "timeout": 300  # 5 minutes
        }

        # Send to Slack, email, etc.
        notification_id = await self.notify_approvers(approvers, request)

        # Wait for response
        response = await self.wait_for_decision(notification_id, timeout=300)

        return response.approved

# Usage
@mcp.tool("prescribe_medication")
async def prescribe_medication(patient_id: str, medication: str, dosage: str):
    # AI proposes action
    proposal = {
        "tool": "prescribe_medication",
        "patient_id": patient_id,
        "medication": medication,
        "dosage": dosage,
        "justification": "Patient has confirmed diagnosis, standard treatment"
    }

    # Require physician approval
    approved = await approval_gate.request_approval(
        action=proposal,
        approvers=["physician_on_call"]
    )

    if not approved:
        raise OperationDeniedError("Physician denied prescription")

    # Execute with human approval
    return ehr_system.prescribe(patient_id, medication, dosage)
```

## HITL Pattern 2: Confidence Thresholds

```python
class ConfidenceGate:
    def __init__(self, auto_approve_threshold=0.95):
        self.threshold = auto_approve_threshold

    async def check(self, action: str, confidence: float):
        if confidence >= self.threshold:
            return True  # Auto-approve high-confidence

        # Low confidence → human review
        return await self.request_human_review(action, confidence)

# Usage in diagnostic AI
result = diagnostic_model.predict(patient_data)

if result.confidence < 0.95:
    # Flag for physician review
    flagged_for_review(patient_id, result.diagnosis, result.confidence)
else:
    # High confidence, but still show to physician
    suggest_to_physician(result.diagnosis, note="AI high-confidence suggestion")
```

## HITL Pattern 3: Audit Trail with Human Annotations

```python
def log_with_human_context(action: dict, human_reviewer: str, decision: str, notes: str):
    audit_entry = {
        "action": action,
        "ai_recommendation": action.get("ai_suggestion"),
        "human_reviewer": human_reviewer,
        "human_decision": decision,  # "approved", "modified", "rejected"
        "human_notes": notes,
        "timestamp": datetime.utcnow()
    }
    audit_log.write(audit_entry)

    # Learn from human feedback
    if decision == "modified":
        feedback_loop.record_correction(
            ai_output=action.get("ai_suggestion"),
            human_correction=notes
        )
```

## Resources
- [MCP Security Threats](./mcp-security-threats.md)
- [Safe MCP Patterns](./safe-mcp-patterns.md)
- [WHO LMM Guidelines](../04-healthcare/who-lmm-guidelines.md) - Human oversight requirements
