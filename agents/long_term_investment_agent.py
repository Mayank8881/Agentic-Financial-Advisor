"""
Long-Term Investment Agent

Purpose:
    This file defines the Long-Term Investment Agent.
    The agent is responsible for generating investment
    recommendations that focus on long-term wealth
    creation, financial stability, and compounding returns.

Why this agent exists:
    Long-term investments require a different mindset
    compared to short-term trading. This agent mimics
    the behavior of a professional long-term financial
    advisor who prioritizes fundamentals, stability,
    and sustainable growth.
"""

# Import the Agent class from the PydanticAI framework.
# This is used to define a role-based AI agent.
from pydantic_ai import Agent

# Import the Pydantic schema used to describe the expected
# structure of an investment recommendation.
# (Used by the orchestrator for validation, not for function calling.)
from schemas.investment_schema import InvestmentRecommendation

# Import the LLM configuration utility.
# This function returns the configured open-source LLM
# running locally through Ollama.
from utils.llm_configuration import get_llm_model


# -------------------------------------------------------------------
# Long-Term Investment Agent Definition
# -------------------------------------------------------------------
# This agent is designed to generate long-term investment
# recommendations using a locally running LLM.
#
# Special care is taken to ensure:
# - Output is structured as valid JSON
# - Responses are stable and retry-safe
# - No function calling is used (to avoid parsing issues)
# -------------------------------------------------------------------
long_term_investment_agent = Agent(
    # Specify the language model used by this agent.
    # "llama3.2:latest" refers to the latest LLaMA model
    # served locally via Ollama.
    model=get_llm_model("llama3.2:latest"),

    # Number of retry attempts if the model output
    # does not match the expected format.
    # This improves reliability when dealing with LLMs.
    retries=3,

    # System prompt defines the behavior, role,
    # and strict output requirements for this agent.
    system_prompt="""
    You are a long-term investment advisor.

    Focus:
    - Time horizon: multiple years
    - Strong fundamentals and financial stability
    - Risk-adjusted returns and long-term compounding

    CRITICAL INSTRUCTIONS:
    - You must return ONLY a valid JSON object
    - Do NOT use function call format
    - Do NOT wrap the response in any additional text
    - Return the JSON directly as your final answer

    Required JSON format:
    {
        "asset_name": "Name of the investment",
        "rationale": "Why this investment is recommended",
        "risk_level": "Low" or "Medium" or "High",
        "expected_return": "Expected return description",
        "time_horizon": "Long-term"
    }

    Example output:
    {
        "asset_name": "Index Fund",
        "rationale": "Diversified portfolio with long-term growth potential",
        "risk_level": "Medium",
        "expected_return": "12-15% annually",
        "time_horizon": "Long-term"
    }
    """
)
