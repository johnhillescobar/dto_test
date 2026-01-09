LLM_CONFIG = {
    "provider": "openai",  # openai | anthropic | google
    "model": "gpt-5",  # gpt-4o | gpt-4o-mini | gpt-4.1 | claude-sonnet-4-5-20250929 | gemini-2.5-flash
    "temperature": 0.1,
    "temperature_text": 0.5,
    "max_tokens": 50000,  # gpt-4o-mini max is 16384
    "timeout": 30,
    "fallback_model": "gpt-4o-mini",
}

LLM_CONFIG_MIDDLEWARE = {
    "provider": "openai",  # openai | anthropic | google
    "model": "gpt-4.1",  # gpt-4o | gpt-4o-mini | gpt-4.1 | claude-sonnet-4-5-20250929 | gemini-2.5-flash
    "temperature": 0.1,
    "temperature_text": 0.5,
    "max_tokens": 4000,  # gpt-4o-mini max is 16384
    "max_retries": 5,
    "max_tokens_before_summary": 4000,
    "messages_to_keep": 20,
    "timeout": 30,
    "fallback_model": "gpt-4o-mini",
    "trigger": 2000,
    "keep": 4,
}


AGENT_PROMPT = """
You are a helpful assistant that has access to the following tools:
{tools}
You are to use the tools to answer the user's question OR convert text from one unit to another.
"""
