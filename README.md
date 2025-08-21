# GitHub Repo Question-Answering Agent with Docker MCP Toolkit

This project demonstrates an AI agent that can answer questions about a GitHub repository. It uses the Model-Context-Protocol (MCP) Toolkit to interact with a GitHub MCP server running in a Docker container.

## Overview

This setup connects a developer’s local agent to GitHub through a Dockerized MCP Gateway, with Docker Compose orchestrating the environment. Here’s how it works step-by-step:

### User Interaction

1.  The developer runs the agent from a CLI or terminal.
2.  They type a question about a GitHub repository — e.g., “Where is the authentication logic implemented?”

### Agent Processing

1.  The Agent (LLM + MCPTools) receives the question.
2.  The agent determines that it needs repository data and issues a tool call via MCPTools.

### MCPTools → MCP Gateway

1.  MCPTools sends the request using `streamable-http` to the MCP Gateway running in Docker.
2.  This gateway is defined in `docker-compose.yml` and configured for the GitHub server (`--servers=github --port=8080`).

### GitHub Integration

The MCP Gateway handles all GitHub API interactions — listing files, retrieving content, searching code — and returns structured results to the agent.

### LLM Reasoning

1.  The agent sends the retrieved GitHub context to an LLM (like OpenAI's GPT models) as part of a prompt.
2.  The LLM reasons over the data and generates a clear, context-rich answer.

### Response to User

The agent prints the final answer back to the CLI, often with file names and line references.

## Folder Structure

```
.
├── app.py                # Main application file for the agent
├── docker-compose.yml    # Docker Compose file for services
├── Dockerfile            # Dockerfile for the agent application
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.8+](https://www.python.org/downloads/)
- An API key from [OpenAI](https://platform.openai.com/api-keys) or [OpenRouter](https://openrouter.ai/keys)

## Quick Start

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/aminammar1/ai-agents-mcp-docker.git
    cd ai-agents-mcp-docker
    ```

2.  **Set up environment variables:**
    Create a file named `.env` in the project root and add your API key:

    ```
    OPENAI_API_KEY="your-api-key-here"
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the MCP Gateway:**
    Open a terminal and run the following command to start the GitHub MCP server in a Docker container:

    ```bash
    docker-compose up -d
    ```

5.  **Run the agent:**
    In another terminal, run the agent application:

    ```bash
    python app.py
    ```

6.  **Interact with the agent:**
    Once the agent is running, you can ask questions about any public GitHub repository. For example:
    ```
    Enter your query (type 'exit' to quit): repo="langchain-ai/langchain" "what is this repo about?"
    ```
