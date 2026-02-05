from typing import AsyncGenerator

from blaxel.pydantic import bl_model, bl_tools
from pydantic_ai import Agent, CallToolsNode, Tool
from pydantic_ai.messages import ToolCallPart


def weather(city: str) -> str:
    """Get the weather in a given city"""
    return f"The weather in {city} is sunny"


async def agent(input: str) -> AsyncGenerator[str, None]:
    prompt = (
        "You are a helpful assistant that can answer questions and help with tasks."
    )
    tools = await bl_tools(["blaxel-search"]) + [
        Tool(
            weather,
        )
    ]
    model = await bl_model("sandbox-openai")
    agent = Agent(
        model=model,
        tools=tools,
        system_prompt=prompt,
    )
    async with agent.iter(input) as agent_run:
        async for node in agent_run:
            if isinstance(node, CallToolsNode):
                for part in node.model_response.parts:
                    if isinstance(part, ToolCallPart):
                        yield (f"Tool call: {part.tool_name}\n")
                    else:
                        yield part.content + "\n"
