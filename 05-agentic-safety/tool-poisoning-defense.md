# Tool Poisoning Defense: Supply Chain Security for MCP

Defense strategies against compromised MCP server code and poisoned tool dependencies.

## Threat: Supply Chain Attacks on MCP Servers

**Attack Vectors**:
1. **Compromised npm/PyPI packages** (typosquatting, account takeover)
2. **Malicious pull requests** to open-source MCP tools
3. **Insider threats** (malicious code in internal tools)
4. **Dependency confusion** (internal vs. public package names)

## Defense Strategy 1: Dependency Integrity Verification

```json
// package-lock.json with integrity hashes
{
  "dependencies": {
    "@modelcontextprotocol/server": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/@modelcontextprotocol/server/-/server-1.0.5.tgz",
      "integrity": "sha512-abc123...",  // Verify hash
      "requires": {}
    }
  }
}
```

```bash
# Verify integrity before deployment
npm ci --ignore-scripts  # No post-install scripts
npm audit  # Check for vulnerabilities
```

## Defense Strategy 2: Code Signing & Verification

```python
# Sign MCP tool code
import hashlib
import hmac

def sign_tool_code(code: str, private_key: str) -> str:
    """Sign MCP tool code with private key"""
    code_hash = hashlib.sha256(code.encode()).digest()
    signature = hmac.new(private_key.encode(), code_hash, hashlib.sha256).hexdigest()
    return signature

def verify_tool_signature(code: str, signature: str, public_key: str) -> bool:
    """Verify tool code hasn't been tampered with"""
    expected_sig = sign_tool_code(code, public_key)
    return hmac.compare_digest(signature, expected_sig)
```

## Defense Strategy 3: Runtime Sandboxing

```dockerfile
# MCP server in locked-down container
FROM python:3.11-slim

# Read-only filesystem
RUN chmod 555 /app
COPY --chmod=444 mcp_server.py /app/

# Drop all capabilities
USER nobody

# No network (except specific allowed domains)
# Enforced by docker-compose network policies
```

## Defense Strategy 4: Behavior Monitoring

```python
# Monitor for suspicious tool behavior
class ToolBehaviorMonitor:
    ALLOWED_OUTBOUND_DOMAINS = ["api.weather.com", "maps.googleapis.com"]

    def monitor_network_call(self, domain: str):
        if domain not in self.ALLOWED_OUTBOUND_DOMAINS:
            raise SecurityError(f"Tool attempted unauthorized outbound connection: {domain}")
            # Alert security team
            alert_security_team(f"Tool poisoning suspected: {domain}")
```

## Resources
- [Safe MCP Patterns](./safe-mcp-patterns.md)
- [MCP Security Threats](./mcp-security-threats.md) - MCP-02: Tool Poisoning
- [OpenSSF Scorecard](https://github.com/ossf/scorecard) - Automated security checks
