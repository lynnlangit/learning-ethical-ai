# Safe MCP Patterns: OpenSSF Security Guidelines

Security patterns and best practices for building safe Model Context Protocol (MCP) servers, aligned with OpenSSF (Open Source Security Foundation) principles.

## Reference: OpenSSF Safe-MCP Initiative

The OpenSSF Safe-MCP project provides security guidelines for MCP server development:
- **GitHub**: [github.com/openssf/safe-mcp](https://github.com/openssf/safe-mcp)
- **Goal**: Establish security baseline for agentic AI tool integration
- **Status**: Active development (as of January 2026)

**Related Example**: See [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) for geospatial MCP server implementing these patterns.

## Core Safe-MCP Principles

### 1. Principle of Least Privilege

**Pattern**: Every MCP tool should have the minimum permissions necessary.

```python
# ✅ GOOD: Granular permissions
@mcp.tool("read_patient_summary")
@requires_permission("ehr.read.summary")  # Narrow scope
async def read_patient_summary(patient_id: str):
    return ehr.get_summary(patient_id)

@mcp.tool("read_patient_full_record")
@requires_permission("ehr.read.full")  # Broader scope, stricter control
async def read_patient_full_record(patient_id: str):
    return ehr.get_full_record(patient_id)

# ❌ BAD: Overly broad permissions
@mcp.tool("read_patient_data")
@requires_permission("ehr.admin")  # Unnecessary admin rights
async def read_patient_data(patient_id: str):
    return ehr.get_summary(patient_id)
```

### 2. Defense in Depth

**Pattern**: Multiple security layers, so single failure doesn't compromise system.

```
┌────────────────────────────────────────────┐
│         DEFENSE-IN-DEPTH LAYERS            │
├────────────────────────────────────────────┤
│                                            │
│  Layer 1: Input Validation                 │
│    - Schema validation, type checking      │
│    - Sanitization, whitelist filtering     │
│                                            │
│  Layer 2: Authentication                   │
│    - API keys, OAuth tokens                │
│    - User identity verification            │
│                                            │
│  Layer 3: Authorization                    │
│    - RBAC (Role-Based Access Control)      │
│    - Resource-level permissions            │
│                                            │
│  Layer 4: Rate Limiting                    │
│    - Per-user, per-tool quotas             │
│    - Prevent abuse/DoS                     │
│                                            │
│  Layer 5: Audit Logging                    │
│    - Record all actions                    │
│    - Detect anomalies                      │
│                                            │
│  Layer 6: Monitoring & Alerts              │
│    - Real-time threat detection            │
│    - Incident response                     │
│                                            │
└────────────────────────────────────────────┘
```

### 3. Secure by Default

**Pattern**: MCP tools should be restrictive by default, permissive only when explicitly configured.

```python
# ✅ GOOD: Secure defaults
class MCPTool:
    def __init__(
        self,
        name: str,
        requires_auth: bool = True,  # Auth required by default
        max_calls_per_minute: int = 10,  # Conservative rate limit
        log_all_calls: bool = True,  # Audit by default
        allowed_roles: list = ["admin"]  # Restrictive by default
    ):
        self.name = name
        self.requires_auth = requires_auth
        # ...

# ❌ BAD: Insecure defaults
class MCPTool:
    def __init__(
        self,
        name: str,
        requires_auth: bool = False,  # Open by default!
        max_calls_per_minute: int = 1000,  # Unlimited
        log_all_calls: bool = False  # No audit trail
    ):
        # ...
```

## Safe-MCP Implementation Patterns

### Pattern 1: Input Validation Schema

```python
from pydantic import BaseModel, Field, validator

class SearchEHRInput(BaseModel):
    """Validated input schema for EHR search"""

    query: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Search term (3-100 characters)"
    )

    max_results: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Max results (1-100)"
    )

    @validator('query')
    def validate_query(cls, v):
        # Block SQL injection attempts
        dangerous_keywords = ['DROP', 'DELETE', 'UPDATE', 'INSERT', '--', ';']
        if any(keyword in v.upper() for keyword in dangerous_keywords):
            raise ValueError(f"Query contains dangerous keyword")

        # Block wildcards
        if v in ['*', '%']:
            raise ValueError("Wildcard queries not allowed")

        return v

@mcp.tool("search_ehr")
async def search_ehr(input: SearchEHRInput):
    # Input is pre-validated by Pydantic
    return database.search(input.query, limit=input.max_results)
```

### Pattern 2: Capability-Based Security

```python
# Grant capabilities, not broad permissions
class MCPCapability:
    """Specific, time-limited capability to perform an action"""

    def __init__(self, action: str, resource: str, expires_at: datetime):
        self.action = action  # e.g., "read"
        self.resource = resource  # e.g., "patient/12345"
        self.expires_at = expires_at

    def is_valid(self) -> bool:
        return datetime.utcnow() < self.expires_at

# Issue capability token
def issue_capability(user_id: str, action: str, resource: str, duration_minutes: int = 15):
    """Issue time-limited capability token"""
    capability = MCPCapability(
        action=action,
        resource=resource,
        expires_at=datetime.utcnow() + timedelta(minutes=duration_minutes)
    )
    return jwt.encode(capability.__dict__, SECRET_KEY)

# Use capability
@mcp.tool("read_patient_record")
async def read_patient_record(patient_id: str, capability_token: str):
    capability = jwt.decode(capability_token, SECRET_KEY)

    # Verify capability is valid and matches request
    if not capability.is_valid():
        raise AuthorizationError("Capability expired")
    if capability.action != "read" or capability.resource != f"patient/{patient_id}":
        raise AuthorizationError("Capability mismatch")

    return ehr.get_record(patient_id)
```

### Pattern 3: Tool Call Chain Monitoring

```python
class ToolCallMonitor:
    """Monitor for suspicious tool call patterns"""

    def __init__(self):
        self.call_graph = nx.DiGraph()  # NetworkX graph
        self.suspicious_patterns = self.load_attack_patterns()

    def record_call(self, from_tool: str, to_tool: str, user_id: str):
        self.call_graph.add_edge(from_tool, to_tool, user=user_id, timestamp=datetime.utcnow())

    def detect_suspicious_chain(self, user_id: str) -> bool:
        """Detect if recent call chain matches known attack patterns"""

        user_subgraph = self.get_user_subgraph(user_id, last_n_calls=10)

        for attack_pattern in self.suspicious_patterns:
            if nx.is_subgraph_isomorphic(user_subgraph, attack_pattern):
                return True

        return False

# Suspicious patterns (from threat intelligence)
monitor = ToolCallMonitor()
monitor.suspicious_patterns = [
    # Pattern: enumerate → exfiltrate → transmit
    nx.DiGraph([("list_patients", "export_data"), ("export_data", "send_email")]),

    # Pattern: privilege escalation chain
    nx.DiGraph([("read_config", "modify_permissions"), ("modify_permissions", "admin_action")]),
]
```

### Pattern 4: Human-in-the-Loop (HITL) for High-Risk Actions

```python
# See human-in-loop-agents.md for full implementation

class HITLGate:
    """Require human approval for high-risk MCP tool calls"""

    HIGH_RISK_TOOLS = [
        "delete_patient_record",
        "export_large_dataset",
        "modify_treatment_plan",
        "prescribe_medication"
    ]

    @staticmethod
    async def require_approval(tool_name: str, parameters: dict) -> bool:
        if tool_name not in HITLGate.HIGH_RISK_TOOLS:
            return True  # Low-risk, auto-approve

        # Send approval request to human
        approval_request = {
            "tool": tool_name,
            "parameters": parameters,
            "requester": get_current_user(),
            "timestamp": datetime.utcnow().isoformat()
        }

        approval_id = await send_approval_request(approval_request)

        # Wait for human decision (with timeout)
        decision = await wait_for_approval(approval_id, timeout_seconds=300)

        return decision == "approved"

@mcp.tool("delete_patient_record")
async def delete_patient_record(patient_id: str):
    # Require human approval before execution
    approved = await HITLGate.require_approval("delete_patient_record", {"patient_id": patient_id})

    if not approved:
        raise OperationDeniedError("Human reviewer denied deletion request")

    database.delete(patient_id)
    return {"status": "deleted"}
```

### Pattern 5: Sandboxed Execution

```python
# Run MCP tools in isolated sandbox

# Docker-based sandboxing
FROM python:3.11-slim

# Non-root user
RUN useradd -m -u 1000 mcpuser
USER mcpuser

# Restricted filesystem
VOLUME /app/allowed_files
WORKDIR /app

# No outbound network by default
# (Add specific allowlist in docker-compose)

# Resource limits
CMD ["python", "-m", "mcp_server", "--max-memory=512M", "--max-cpu=0.5"]
```

```yaml
# docker-compose.yml with security constraints
version: '3.8'
services:
  mcp-server:
    build: .
    security_opt:
      - no-new-privileges:true
      - seccomp:unconfined
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE  # Only allow binding to ports
    read_only: true  # Read-only root filesystem
    networks:
      - restricted_network

networks:
  restricted_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
```

## Safe-MCP Testing Checklist

### Security Testing Requirements

- [ ] **Input Validation**: Fuzz test all tool parameters
- [ ] **Authentication Bypass**: Test with missing/invalid credentials
- [ ] **Authorization Bypass**: Test privilege escalation attempts
- [ ] **Rate Limiting**: Test DoS resistance (burst requests)
- [ ] **Path Traversal**: Test file operations with `../../` payloads
- [ ] **SQL Injection**: Test database queries with malicious inputs
- [ ] **Tool Chain Abuse**: Test suspicious multi-tool patterns
- [ ] **Logging Verification**: Confirm all high-risk actions logged
- [ ] **Secrets Exposure**: Scan for hardcoded credentials in code/logs
- [ ] **Dependency Vulnerabilities**: Run `npm audit` or `pip-audit`

### Example: Automated Security Tests

```python
# test_mcp_security.py
import pytest

class TestMCPSecurity:
    def test_sql_injection_blocked(self):
        """Verify SQL injection attempts are rejected"""
        malicious_queries = [
            "'; DROP TABLE patients; --",
            "1' OR '1'='1",
            "admin'--"
        ]
        for query in malicious_queries:
            with pytest.raises(ValidationError):
                search_ehr(query=query)

    def test_path_traversal_blocked(self):
        """Verify path traversal attempts are rejected"""
        malicious_paths = [
            "../../../../etc/passwd",
            "/etc/shadow",
            "..\\..\\..\\windows\\system32\\config\\sam"
        ]
        for path in malicious_paths:
            with pytest.raises(SecurityError):
                read_file(filename=path)

    def test_rate_limiting_enforced(self):
        """Verify rate limiting prevents DoS"""
        # Attempt 100 rapid calls (exceeds limit of 60/min)
        with pytest.raises(RateLimitExceededError):
            for _ in range(100):
                search_ehr(query="test")

    def test_unauthorized_access_blocked(self):
        """Verify unauthenticated requests are rejected"""
        with pytest.raises(AuthenticationError):
            delete_patient_record(patient_id="12345", auth_token=None)

    def test_tool_chain_detection(self):
        """Verify suspicious tool chains are detected"""
        # Simulate attack chain
        list_patients()
        export_data(all_patient_ids)

        # Should trigger alert
        assert monitor.detect_suspicious_chain(user_id=current_user)
```

## Safe-MCP Deployment Patterns

### Pattern 1: Blue-Green Deployment with Canary Testing

```bash
# Deploy new MCP server version to canary (10% traffic)
kubectl apply -f mcp-server-v2-canary.yaml

# Monitor canary for security issues
monitor_security_metrics --version=v2 --duration=1h

# If safe, promote to production
kubectl apply -f mcp-server-v2-production.yaml

# If issues detected, rollback immediately
kubectl rollback deployment/mcp-server
```

### Pattern 2: Network Segmentation

```
┌──────────────────────────────────────────────┐
│        NETWORK SEGMENTATION                  │
├──────────────────────────────────────────────┤
│                                              │
│  DMZ (Public-facing)                         │
│    └─ AI Agent (Claude, etc.)                │
│          │                                   │
│          ▼ (Restricted API access)           │
│  Application Layer                           │
│    └─ MCP Server (sandboxed)                 │
│          │                                   │
│          ▼ (Database-specific network)       │
│  Data Layer                                  │
│    └─ EHR Database (no internet access)      │
│                                              │
└──────────────────────────────────────────────┘

# Firewall rules
- AI Agent → MCP Server: Port 443 only (HTTPS)
- MCP Server → Database: Port 5432 only (PostgreSQL)
- Database → Internet: BLOCKED
```

## Resources

### OpenSSF Safe-MCP
- [Safe-MCP GitHub](https://github.com/openssf/safe-mcp) - Official guidelines
- [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/)

### Reference Implementations
- [spatial-mcp](https://github.com/lynnlangit/spatial-mcp) - Secure geospatial MCP server
- [MCP Security Audit Notebook](../02-examples/05-mcp-security-audit.ipynb)

### Related Guides
- [MCP Security Threats](./mcp-security-threats.md) - OWASP-style threat taxonomy
- [Human-in-the-Loop Agents](./human-in-loop-agents.md) - HITL patterns
- [Tool Poisoning Defense](./tool-poisoning-defense.md) - Supply chain security
- [Audit Logging](./audit-logging-agents.md) - Comprehensive logging patterns

---

**Key Takeaway**: Safe MCP development requires security thinking at every layer: input validation, authentication, authorization, rate limiting, sandboxing, monitoring, and incident response. Use these patterns as a baseline, not a ceiling.
