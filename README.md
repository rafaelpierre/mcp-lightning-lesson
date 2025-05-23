# Build Your First Agentic AI App with MCP
## Maven Lightning Lesson

A Python project demonstrating the use of OpenAI GPT models and MCP (Model Context Protocol) agents to fetch and process real-world data.

## Overview

This project provides an example of using a custom agent to retrieve weather forecasts for Hintertux, Austria, by fetching data from the meteoblue.com website. It leverages the `openai-agents` library and its capabilities to run and expose MCP Servers.

## Features

- Custom agent implementation using OpenAI GPT models
- Integration with MCP server for data fetching
- Example function tool (`get_time`) for current time retrieval
- Returns structured JSON output

## Requirements

- Python 3.13+
- OpenAI API key

## Installation

1. Clone the repository:
   ```sh
   git clone ...
   cd mcp-lightning-lesson
   ```
2. Create a venv using [uv](astral.sh/uv):
   ```sh
   uv venv
   ```
4. Copy the example environment file and add your OpenAI API key:
   ```sh
   cp .env.example .env
   # Edit .env and set your OPENAI_API_KEY
   ```

## Usage

Run the main script:

```sh
uv run python main.py
```

The agent will:
- Fetch the weather forecast for Hintertux, Austria
- Get the current time
- Return the results as a JSON payload

## Project Structure

- `main.py` – Main application logic
- `pyproject.toml` – Project dependencies and metadata
- `.env.example` – Example environment variable file

## Dependencies

- openai-agents >= 0.0.15
- python-dotenv >= 1.1.0

## Frontend

Coming soon!
