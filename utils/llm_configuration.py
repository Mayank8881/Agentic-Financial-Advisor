"""

LLM Configuration

Purpose:
    This file provides a centralized configuration for the
    Large Language Model (LLM) used across the entire system.

Why this file exists:
    - Keeps LLM configuration in one place
    - Avoids hardcoding model settings inside agent files
    - Makes it easy to switch models or providers in the future
    - Explicitly configures Ollama to avoid environment variable issues
"""

# Import the OpenAI-compatible chat model interface used by PydanticAI.
# Even though we are NOT using OpenAI, this abstraction allows
# Ollama models to be accessed in a standardized way.
from pydantic_ai.models.openai import (
    OpenAIChatModel,
    OpenAIChatModelSettings
)

# Import the Ollama provider.
# This provider enables communication with a locally running
# open-source LLM through the Ollama service.
from pydantic_ai.providers.ollama import OllamaProvider


def get_llm_model(model_name: str = "llama3.2:latest") -> OpenAIChatModel:
    """
    Creates and returns a configured LLM instance connected to Ollama.

    Why this function is important:
        All agents call this function to obtain the same
        consistently configured LLM. This ensures:
        - Uniform behavior across agents
        - Centralized tuning of model parameters
        - Easier maintenance and debugging

    Args:
        model_name (str):
            Name of the Ollama model to use.
            Default is "llama3.2:latest", which refers to the
            latest locally available LLaMA 3.2 model.

    Returns:
        OpenAIChatModel:
            A model instance that communicates with the local
            Ollama service using an OpenAI-compatible interface.
    """

    # ---------------------------------------------------------------
    # Configure Ollama Provider
    # ---------------------------------------------------------------
    # The base_url points to the locally running Ollama service.
    # Using an explicit URL avoids dependency on environment variables
    # and ensures predictable behavior across environments.
    provider = OllamaProvider(
        base_url="http://localhost:11434/v1"
    )

    # ---------------------------------------------------------------
    # Configure Model Settings
    # ---------------------------------------------------------------
    # These settings control how the LLM behaves.
    # A lower temperature makes responses more deterministic
    # and reduces hallucinations, which is important for finance.
    model_settings = OpenAIChatModelSettings(
        temperature=0.3,   # Lower value = more stable and consistent output
        max_tokens=2000    # Maximum length of the model response
    )

    # ---------------------------------------------------------------
    # Create and Return Model Instance
    # ---------------------------------------------------------------
    # The OpenAIChatModel wrapper is used here purely as an interface.
    # The actual inference is performed by the Ollama-hosted model.
    return OpenAIChatModel(
        model_name=model_name,
        provider=provider,
        settings=model_settings
    )
