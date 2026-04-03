# Use official Python lightweight image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv for fast, reliable python package management. Also install dependencies globally.
RUN pip install uv "fastmcp==2.13.0" mcp httpx

# Copy the server script
COPY server.py .

# Run the server directly using python
CMD ["python", "server.py"]
