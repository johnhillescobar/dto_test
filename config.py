from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class LLMConfig(BaseModel):
    provider: str = Field(
        default="openai", description="The provider to use for the LLM"
    )
    model: str = Field(default="gpt-5.2", description="The model to use for the LLM")
    temperature: float = Field(
        default=0.1, description="The temperature to use for the LLM", ge=0.0, le=2.0
    )
    temperature_text: float = Field(
        default=0.5,
        description="The temperature to use for the text generation",
        ge=0.0,
        le=1.0,
    )
    max_tokens: int = Field(
        default=50000, description="The maximum number of tokens to generate", ge=0
    )
    timeout: int = Field(default=30, description="The timeout to use for the LLM", ge=0)
    fallback_model: str = Field(
        default="gpt-4o-mini", description="The fallback model to use for the LLM"
    )


class LLMConfigMiddleware(BaseModel):
    provider: str = Field(
        default="openai", description="The provider to use for the LLM"
    )
    model: str = Field(default="gpt-4.1", description="The model to use for the LLM")
    temperature: float = Field(
        default=0.1, description="The temperature to use for the LLM", ge=0.0, le=2.0
    )
    temperature_text: float = Field(
        default=0.5,
        description="The temperature to use for the text generation",
        ge=0.0,
        le=1.0,
    )
    max_tokens: int = Field(
        default=4000, description="The maximum number of tokens to generate", ge=0
    )
    max_retries: int = Field(
        default=5, description="The maximum number of retries to use for the LLM", ge=0
    )
    max_tokens_before_summary: int = Field(
        default=4000,
        description="The maximum number of tokens to generate before summarizing",
        ge=0,
    )
    messages_to_keep: int = Field(
        default=20, description="The number of messages to keep in the context", ge=0
    )
    timeout: int = Field(default=30, description="The timeout to use for the LLM", ge=0)
    fallback_model: str = Field(
        default="gpt-4o-mini", description="The fallback model to use for the LLM"
    )
    trigger: int = Field(
        default=2000, description="The trigger to use for the context editing", ge=0
    )
    keep: int = Field(
        default=4, description="The number of messages to keep in the context", ge=0
    )


LLM_CONFIG = LLMConfig()

LLM_CONFIG_MIDDLEWARE = LLMConfigMiddleware()


AGENT_PROMPT = """
You are a helpful assistant that has access to the following tools:
{tools}

Instructions:
1. When the user asks for a conversion, use the appropriate tool ONCE
2. After receiving the tool result, provide your final answer and STOP
3. Do NOT call the same tool multiple times
4. Format your response with the conversion result clearly stated

You are to use the tools to answer the user's question OR convert text from one unit to another.
"""
