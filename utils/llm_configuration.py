"""
llm_configuration.py

Purpose:
    Centralized configuration for the LLM provider.
    Explicitly configures Ollama to avoid environment issues.
"""

from pydantic_ai.models.openai import OpenAIChatModel, OpenAIChatModelSettings
from pydantic_ai.providers.ollama import OllamaProvider


def get_llm_model(model_name: str = "llama3.2:latest") -> OpenAIChatModel:
    """
    Returns a configured Ollama model instance.

    Args:
        model_name: Name of the Ollama model to use (default: "llama3.2:latest")

    Returns:
        OpenAIChatModel: Model instance connected to local Ollama service
    """
    provider = OllamaProvider(base_url="http://localhost:11434/v1")
    # Configure model settings for better JSON output
    model_settings = OpenAIChatModelSettings(
        temperature=0.3,  # Lower temperature for more consistent output
        max_tokens=2000
    )
    return OpenAIChatModel(
        model_name=model_name,
        provider=provider,
        settings=model_settings
    )
