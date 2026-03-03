# Ethical AI MCP Server - Development Journey

This document records the phased development and debugging process for deploying the Model Context Protocol (MCP) server that connects the `learning-ethical-ai` repository to Claude Desktop.

## Architecture Overview
*   **Data Source:** GitHub Repository Markdown Files
*   **Server Framework:** [FastMCP](https://jlowin.github.io/fastmcp/) (Python)
*   **Client:** Claude Desktop

---

## Phase 1: Fully Local Execution
We began by building a prototype that ran entirely on the local filesystem.
*   **Data:** Local disk (`path/to/learning-ethical-ai`) using recursive `Path.rglob()` searches.
*   **Server:** Local `uv run server.py` using Standard IO (`stdio`) transport.
*   **Client:** Claude Desktop running locally on macOS.

*Success:* Claude Desktop successfully read the local markdown files and exposed them as tools and resources.

## Phase 2: Remote Data + Local Execution 
To prepare for a cloud deployment, we detached the server from the local filesystem.
*   **Data:** Remote GitHub (`raw.githubusercontent.com`) fetched over HTTPS.
*   **Server:** Local `uv run server.py` using Standard IO (`stdio`) transport.
*   **Client:** Claude Desktop running locally on macOS.

*Success:* The server fetched remote Markdown data into an in-memory cache with a 5-minute TTL, passing it to Claude flawlessly over the local `stdio` stream.

## Phase 3: Fully Remote Execution (GCP Cloud Run)
The final step was migrating the server to Google Cloud Run to serve as a public endpoint.
*   **Data:** Remote GitHub (`raw.githubusercontent.com`).
*   **Server:** GCP Cloud Run using Server-Sent Events (`SSE`) transport.
*   **Client:** Claude Desktop connecting over the public internet.

### Build and Debugging Challenges
Deploying the SSE transport to Google Cloud Run introduced severe network termination bugs ("Empty Error" / HTTP 421 Invalid Host Header) that required deep architectural changes:

1. **`mcp.server.fastmcp` vs `fastmcp` PyPI Package:**
   We initially used the FastMCP submodule bundled natively inside the `mcp` SDK. However, this version failed to negotiate HTTP Host headers correctly when behind GCP's reverse proxy. **Fix:** We downgraded explicitly to the standalone `fastmcp==2.13.0` PyPI package, which natively supported `MCP_BASE_URL` reverse proxy configurations.
2. **Synchronous Thread Blocking:** 
   Our initial GitHub fetching logic used synchronous `urllib.request` threads. When downloading 24 markdown files simultaneously, the Python event loop was completely blocked for up to 10 seconds. This block prevented the FastMCP web server from sending SSE "heartbeats", causing Claude Desktop to abruptly terminate the connection. **Fix:** We rewrote the fetching layer and all tool definitions to be fully asynchronous using `httpx.AsyncClient` and `asyncio`.
3. **Claude Desktop Proxy Translation:**
   We originally configured Claude Desktop to connect using the third-party `mcp-proxy` tool to translate SSE to `stdio`. This tool failed to parse the heavy payload efficiently. **Fix:** We replaced it with FastMCP's native proxy command (`uvx fastmcp run [URL]`), which securely wraps the remote URL directly for Claude.
