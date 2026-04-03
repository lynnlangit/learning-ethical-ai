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
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo
import logging
import sys

import httpx
import asyncio

from typing import Annotated, Dict, Optional, Tuple, Any
from fastmcp import FastMCP, Context
from pydantic import Field

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("ethical-ai-mcp")

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

CACHE_TTL = 300  # 5 minutes


@dataclass
class CacheState:
    """Server-scoped document cache, managed via FastMCP lifespan."""
    docs: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    last_check: float = 0.0


@asynccontextmanager
async def lifespan(server: FastMCP):
    """Initialize server-scoped cache state on startup and clean up on shutdown."""
    logger.info("Server starting — initializing cache state.")
    yield CacheState()
    logger.info("Server shutting down.")


# Initialize FastMCP Server with lifespan for state management
mcp = FastMCP("Ethical AI Server", lifespan=lifespan)


def _get_central_time_str(timestamp: float = 0) -> str:
    """Converts a UNIX epoch timestamp to a US Central Time string."""
    if timestamp == 0:
        return "Not yet cached"
    dt = datetime.fromtimestamp(timestamp, tz=ZoneInfo("America/Chicago"))
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")


async def fetch_url(client: httpx.AsyncClient, rel_path: str) -> Tuple[str, Optional[str]]:
    url = GITHUB_RAW_BASE + rel_path
    try:
        response = await client.get(url, timeout=10.0)
        response.raise_for_status()
        return rel_path, response.text
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return rel_path, None


async def _get_or_refresh_documents(state: CacheState) -> Dict[str, str]:
    """Returns a dict of {rel_path: content}, fetching from GitHub if TTL expired."""
    current_time = time.time()
    # Cache hit
    if current_time - state.last_check < CACHE_TTL and state.docs:
        return {k: v["content"] for k, v in state.docs.items()}

    logger.info("Cache expired or empty. Fetching from GitHub asynchronously...")
    async with httpx.AsyncClient(headers={"User-Agent": "Ethical-AI-MCP-Server/1.0"}) as client:
        tasks = [fetch_url(client, path) for path in REMOTE_FILES]
        results = await asyncio.gather(*tasks)
        for rel_path, content in results:
            if content is not None:
                state.docs[rel_path] = {"mtime": current_time, "content": content}

    state.last_check = current_time
    return {k: v["content"] for k, v in state.docs.items()}


# 1. Resources
@mcp.resource("ethical-ai://governance/eu-ai-act")
async def get_eu_ai_act(ctx: Context) -> str:
    """The 2026 EU AI Act compliance checklist for high-risk systems."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    return docs.get("06-governance/eu-ai-act-checklist.md", "File not found.")

@mcp.resource("ethical-ai://healthcare/hipaa-checklist")
async def get_hipaa_checklist(ctx: Context) -> str:
    """HIPAA compliance requirements for Healthcare AI integrations."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    return docs.get("04-healthcare/hipaa-ai-checklist.md", "File not found.")

@mcp.resource("ethical-ai://agentic-safety/mcp-threats")
async def get_mcp_threats(ctx: Context) -> str:
    """OWASP-style taxonomy of MCP and Agentic Security Threats."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    return docs.get("05-agentic-safety/mcp-security-threats.md", "File not found.")

@mcp.resource("ethical-ai://tools/nemo-guardrails")
async def get_nemo_guardrails(ctx: Context) -> str:
    """NVIDIA NeMo Guardrails configuration and setup for runtime AI safety."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    return docs.get("01-tools/02-nemo-guardrails/README.md", "File not found.")


# 2. Tools
@mcp.tool()
async def search_guidelines(
    query: Annotated[str, Field(min_length=1, max_length=200, description="The keyword or concept to search for (e.g., 'synthetic data', 'poisoning').")],
    ctx: Context,
) -> str:
    """Searches across all markdown documents in the repository for specific concepts."""
    logger.info(f"Executing search_guidelines tool for query: '{query}'")
    results = []

    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    for rel_path, content in docs.items():
        content_str = str(content)
        if not rel_path.endswith(".md"):
            continue
        if query.lower() in content_str.lower():
            idx = content_str.lower().find(query.lower())
            start = max(0, idx - 1000)
            end = min(len(content_str), idx + 1000)
            snippet = content_str[start:end].replace("\n", " ")
            results.append(f"Match found in {rel_path}:\n...{snippet}...\n")

    if not results:
        return f"No results found for '{query}'."

    meta = f"--- SERVER METADATA ---\nCache last refreshed: {_get_central_time_str(ctx.lifespan_context.last_check)}\n-----------------------\n\n"
    return meta + "\n".join(results[:5])  # Limit to top 5 results

@mcp.tool()
async def get_learning_path(role: str, ctx: Context) -> str:
    """Gets the specific learning path from LEARNING_PATHS.md based on the user's role.

    Args:
        role: A role keyword such as 'Beginner', 'Healthcare', 'Security', 'Compliance', or 'Advanced'.
              Partial matches are supported (e.g. 'security' matches the Agentic Security path).
    """
    try:
        docs = await _get_or_refresh_documents(ctx.lifespan_context)
        content = docs.get("LEARNING_PATHS.md", "")
        if not content:
            return "LEARNING_PATHS.md not found in remote cache."

        # Split into sections on ## Path headers, keeping the header with each section
        sections = []
        current = []
        for line in content.splitlines(keepends=True):
            if line.startswith("## Path") and current:
                sections.append("".join(current))
                current = [line]
            else:
                current.append(line)
        if current:
            sections.append("".join(current))

        role_lower = role.lower()
        matched = [s for s in sections if role_lower in s.lower()]

        if matched:
            return f"Learning path(s) matching '{role}':\n\n" + "\n---\n".join(matched)

        # No match — list available paths by their first line
        titles = [s.splitlines()[0].strip() for s in sections if s.startswith("## Path")]
        return (
            f"No learning path found for role '{role}'.\n\n"
            f"Available paths:\n" + "\n".join(f"- {t}" for t in titles)
        )
    except Exception as e:
        logger.error(f"Error in get_learning_path: {e}")
        return f"Failed to load LEARNING_PATHS.md: {e}"

@mcp.tool()
async def get_tool_configuration(
    tool_name: Annotated[str, Field(min_length=1, max_length=100, description="The name of the tool (e.g., 'giskard', 'nemo-guardrails').")],
    ctx: Context,
) -> str:
    """Fetches configuration content for specific tools like giskard or nemo-guardrails."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    files_content = []
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
async def audit_agent_security(ctx: Context) -> str:
    """A prompt to automatically review code against Agentic Safety guidelines."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    threats = docs.get("05-agentic-safety/mcp-security-threats.md", "File not found.")
    return f"""You are an AI Safety Auditor. Review the user's currently open files against the following Agentic Safety guidelines and highlight any vulnerabilities.

[Context Date Warning: The MCP Server last synced the attached guidelines with the local repository on {_get_central_time_str(ctx.lifespan_context.last_check)}. Please refer to this date if the user asks about the freshness of your review.]

Context (MCP Security Threats):
{threats}

Please conduct a thorough review."""

@mcp.prompt()
async def review_healthcare_compliance(ctx: Context) -> str:
    """A prompt to automatically review a data-handling pipeline against HIPAA guidelines."""
    docs = await _get_or_refresh_documents(ctx.lifespan_context)
    hipaa = docs.get("04-healthcare/hipaa-ai-checklist.md", "File not found.")
    return f"""You are a Healthcare AI Compliance Officer. Please review the user's code and architecture against the following HIPAA guidelines.

[Context Date Warning: The MCP Server last synced the attached HIPAA Guidelines with the local repository on {_get_central_time_str(ctx.lifespan_context.last_check)}. Please refer to this date if the user asks about the freshness of your review.]

Context (HIPAA Checklist):
{hipaa}

Identify any PHI handling risks or missing safeguards."""


def main() -> None:
    """Run the ethical-ai server."""
    port = os.environ.get("PORT")

    if port:
        # Run the server with Streamable HTTP transport for GCP Cloud Run (SSE is deprecated in FastMCP 2.x)
        mcp.run(transport="http", port=int(port), host="0.0.0.0")
    else:
        # Default local terminal transport
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
