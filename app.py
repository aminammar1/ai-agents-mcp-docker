from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.tools.mcp import MCPTools
import asyncio
import os

load_dotenv()

MCP_SERVER_URL = {
    "SERVER_URL": "http://localhost:8080"
}

async def main():
    MCP_TOOLKIT = MCPTools(url=MCP_SERVER_URL["SERVER_URL"], transport="streamable-http")
    await MCP_TOOLKIT.connect()

    agent = Agent(
        name="Github Repo Summarizer",
        role="summarize the github repository using available toolkit",
        tools=[
            MCP_TOOLKIT
        ],
        model=OpenAIChat(
            id="openai/gpt-oss-20b:free",
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        ),
        show_tool_calls=True,
        debug_mode=True,
        add_datetime_to_instructions=True
    )

    while True:
        query = input("\nEnter your query (type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Exiting...")
            break
        
        await agent.aprint_response(query)
    MCP_TOOLKIT.close()

if __name__ == "__main__":
    asyncio.run(main())