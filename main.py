from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain.agents.middleware import (
    ToolRetryMiddleware,
    SummarizationMiddleware,
    ContextEditingMiddleware,
    ClearToolUsesEdit,
)

from tools.feet_meters import FeetToMetersTool
from tools.meters_feet import MetersToFeetTool
from tools.celsius_farenheit import CelsiusToFarenheitTool
from tools.fahreheit_celsius import FahrenheitToCelsiusTool
from utils.middlewere_funcs import log_messages, handle_errors
from config import AGENT_PROMPT, LLM_CONFIG, LLM_CONFIG_MIDDLEWARE

load_dotenv()


def get_agent_prompt(tools: list[BaseTool]) -> str:
    return AGENT_PROMPT.format(
        tools="\n".join([tool.name + ": " + tool.description for tool in tools])
    )


def main():
    print("Hello from agent-lanchain105!")

    tools = [
        FeetToMetersTool(),
        MetersToFeetTool(),
        CelsiusToFarenheitTool(),
        FahrenheitToCelsiusTool(),
    ]

    # Create LLM
    llm = ChatOpenAI(
        model=LLM_CONFIG["model"],
        temperature=LLM_CONFIG["temperature"],
        max_tokens=LLM_CONFIG["max_tokens"],
        timeout=LLM_CONFIG["timeout"],
    )

    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=get_agent_prompt(tools),
        middleware=[
            log_messages,
            ToolRetryMiddleware(max_retries=LLM_CONFIG_MIDDLEWARE["max_retries"]),
            SummarizationMiddleware(
                model=LLM_CONFIG_MIDDLEWARE["model"],
                trigger=("tokens", LLM_CONFIG_MIDDLEWARE["max_tokens_before_summary"]),
                keep=("messages", LLM_CONFIG_MIDDLEWARE["messages_to_keep"]),
            ),
            ContextEditingMiddleware(
                edits=[
                    ClearToolUsesEdit(
                        trigger=LLM_CONFIG_MIDDLEWARE["trigger"],
                        keep=LLM_CONFIG_MIDDLEWARE["keep"],
                    )
                ]
            ),
            handle_errors,
        ],
    )

    # Run agent
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "How many meters are in 10 feet?"}]}
    )
    # Extract the final message content
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
