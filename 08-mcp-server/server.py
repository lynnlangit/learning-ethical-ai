# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastmcp==2.13.0",
#     "httpx",
#     "mcp",
# ]
# ///

import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import logging
import sys

import httpx
import asyncio

from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("ethical-ai-mcp")

# Initialize FastMCP Server
mcp = FastMCP("Ethical AI Server")

def _get_central_time_str(timestamp=None):
    """Converts a UNIX epoch timestamp to a US Central Time string."""
    if timestamp is None or timestamp == 0:
        return "Not yet cached"
    
    dt = datetime.fromtimestamp(timestamp, tz=ZoneInfo("America/Chicago"))
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")

# Remote GitHub Data Source
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/lynnlangit/learning-ethical-ai/refs/heads/main/"
REMOTE_FILES = [
    "CONTRIBUTING.md",
    "LEARNING_PATHS.md",
    "README.md",
    "01-tools/README.md",
    "01-tools/01-giskard/README.md",
    "01-tools/01-giskard/config_vertexai.py",
    "01-tools/01-giskard/healthcare_scan.py",
    "01-tools/02-nemo-guardrails/README.md",
    "01-tools/03-model-cards/README.md",
    "01-tools/04-llama-guard/README.md",
    "02-examples/README.md",
    "04-healthcare/clinical-llm-risks.md",
    "04-healthcare/hipaa-ai-checklist.md",
    "04-healthcare/genomics-ethics.md",
    "04-healthcare/who-lmm-guidelines.md",
    "04-healthcare/synthetic-patient-data.md",
    "05-agentic-safety/mcp-security-threats.md",
    "05-agentic-safety/safe-mcp-patterns.md",
    "05-agentic-safety/human-in-loop-agents.md",
    "05-agentic-safety/tool-poisoning-defense.md",
    "05-agentic-safety/audit-logging-agents.md",
    "06-governance/eu-ai-act-checklist.md",
    "06-governance/nist-ai-600-1-summary.md",
    "06-governance/risk-tiering-template.md"
]

from typing import Dict, Optional, Tuple, Any

# Cache setup
CACHE: Dict[str, Dict[str, Any]] = {}  # Format: {rel_path: {"mtime": float, "content": str}}
CACHE_TTL = 300  # 5 minutes
LAST_CACHE_CHECK = 0

async def fetch_url(client: httpx.AsyncClient, rel_path: str) -> Tuple[str, Optional[str]]:
    url = GITHUB_RAW_BASE + rel_path
    try:
        response = await client.get(url, timeout=10.0)
        response.raise_for_status()
        return rel_path, response.text
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return rel_path, None

async def _get_or_refresh_documents() -> Dict[str, str]:
    """Returns a dict of {rel_path: content} fetching from github if TTL expired."""
    global LAST_CACHE_CHECK
    
    current_time = time.time()
    # Cache hit
    if current_time - LAST_CACHE_CHECK < CACHE_TTL and CACHE:
        return {k: v["content"] for k, v in CACHE.items()}
        
    logger.info("Cache expired or empty. Fetching from GitHub asynchronously...")
    # Cache miss or expired: fetch all from raw.githubusercontent.com in parallel
    async with httpx.AsyncClient(headers={'User-Agent': 'Ethical-AI-MCP-Server/1.0'}) as client:
        tasks = [fetch_url(client, path) for path in REMOTE_FILES]
        results = await asyncio.gather(*tasks)
        
        for rel_path, content in results:
            if content is not None:
                CACHE[rel_path] = {
                    "mtime": current_time,
                    "content": content
                }

    LAST_CACHE_CHECK = current_time
    return {k: v["content"] for k, v in CACHE.items()}

# 1. Resources
@mcp.resource("ethical-ai://governance/eu-ai-act")
async def get_eu_ai_act() -> str:
    """The 2026 EU AI Act compliance checklist for high-risk systems."""
    docs = await _get_or_refresh_documents()
    return docs.get("06-governance/eu-ai-act-checklist.md", "File not found.")

@mcp.resource("ethical-ai://healthcare/hipaa-checklist")
async def get_hipaa_checklist() -> str:
    """HIPAA compliance requirements for Healthcare AI integrations."""
    docs = await _get_or_refresh_documents()
    return docs.get("04-healthcare/hipaa-ai-checklist.md", "File not found.")

@mcp.resource("ethical-ai://agentic-safety/mcp-threats")
async def get_mcp_threats() -> str:
    """OWASP-style taxonomy of MCP and Agentic Security Threats."""
    docs = await _get_or_refresh_documents()
    return docs.get("05-agentic-safety/mcp-security-threats.md", "File not found.")

@mcp.resource("ethical-ai://tools/nemo-guardrails")
async def get_nemo_guardrails() -> str:
    """NVIDIA NeMo Guardrails configuration and setup for runtime AI safety."""
    docs = await _get_or_refresh_documents()
    return docs.get("01-tools/02-nemo-guardrails/README.md", "File not found.")

# 2. Tools
@mcp.tool()
async def search_guidelines(query: str) -> str:
    """Searches across all markdown documents in the repository for specific concepts.
    
    Args:
        query: The keyword or concept to search for (e.g., 'synthetic data', 'poisoning').
    """
    logger.info(f"Executing search_guidelines tool for query: '{query}'")
    results = []
    
    docs = await _get_or_refresh_documents()
    for rel_path, content in docs.items():
        content_str = str(content)
        if not rel_path.endswith('.md'):
            continue
        if query.lower() in content_str.lower():
            idx = content_str.lower().find(query.lower())
            start = max(0, idx - 1000)
            end = min(len(content_str), idx + 1000)
            snippet = content_str[start:end].replace('\n', ' ')
            results.append(f"Match found in {rel_path}:\n...{snippet}...\n")
            
    if not results:
        return f"No results found for '{query}'."
        
    meta = f"--- SERVER METADATA ---\nSearch executed against remote GitHub guidelines cache last refreshed: {_get_central_time_str(LAST_CACHE_CHECK)}\n[IMPORTANT: You must mention this exact cache refresh date to the user in your final response so they know the data freshness.]\n-----------------------\n\n"
    return meta + "\n".join(results[:5])  # Limit to top 5 results

@mcp.tool()
async def get_learning_path(role: str) -> str:
    """Gets the specific learning path from LEARNING_PATHS.md based on the user's role.
    
    Args:
        role: A role like 'Beginner', 'Dev', 'Security', or 'Compliance'.
    """
    try:
        docs = await _get_or_refresh_documents()
        content = docs.get("LEARNING_PATHS.md", "LEARNING_PATHS.md not found in remote cache.")
        return f"Content of LEARNING_PATHS.md (Review this for {role}):\n\n{content}"
    except Exception as e:
        logger.error(f"Error in get_learning_path: {e}")
        return f"Failed to load LEARNING_PATHS.md: {e}"

@mcp.tool()
async def get_tool_configuration(tool_name: str) -> str:
    """Fetches configuration content for specific tools like giskard or nemo-guardrails.
    
    Args:
        tool_name: The name of the tool (e.g., 'giskard').
    """
    docs = await _get_or_refresh_documents()
    files_content = []
    # Find all cached files that are within the tools directory matching the tool_name
    target_path = f"01-tools/{tool_name.lower()}"
    
    for rel_path, content in docs.items():
        if target_path in rel_path.lower():
            files_content.append(f"--- {rel_path} ---\n{content}\n")
            
    if files_content:
        return "\n".join(files_content)
    return f"Configuration for tool '{tool_name}' not found attached to GitHub cache."

@mcp.tool()
def ping() -> str:
    """A fast diagnostic tool to verify the remote MCP server connection."""
    return "Pong! Clean connection received."

# 3. Prompts
@mcp.prompt()
async def audit_agent_security() -> str:
    """A prompt to automatically review code against Agentic Safety guidelines."""
    threats = await get_mcp_threats()
    return f"""You are an AI Safety Auditor. Review the user's currently open files against the following Agentic Safety guidelines and highlight any vulnerabilities.

[Context Date Warning: The MCP Server last synced the attached guidelines with the local repository on {_get_central_time_str(LAST_CACHE_CHECK)}. Please refer to this date if the user asks about the freshness of your review.]

Context (MCP Security Threats):
{threats}

Please conduct a thorough review."""

@mcp.prompt()
async def review_healthcare_compliance() -> str:
    """A prompt to automatically review a data-handling pipeline against HIPAA guidelines."""
    hipaa = await get_hipaa_checklist()
    return f"""You are a Healthcare AI Compliance Officer. Please review the user's code and architecture against the following HIPAA guidelines.

[Context Date Warning: The MCP Server last synced the attached HIPAA Guidelines with the local repository on {_get_central_time_str(LAST_CACHE_CHECK)}. Please refer to this date if the user asks about the freshness of your review.]

Context (HIPAA Checklist):
{hipaa}

Identify any PHI handling risks or missing safeguards."""

def main() -> None:
    """Run the ethical-ai server."""
    port = os.environ.get("PORT")
    
    if port:
        # Run the server with appropriate transport for GCP Cloud Run
        mcp.run(transport="sse", port=int(port), host="0.0.0.0")
    else:
        # Default local terminal transport
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
