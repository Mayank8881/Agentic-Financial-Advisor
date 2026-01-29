"""
Short-Term Investment Agent

Purpose:
    This file defines the Short-Term Investment Agent.
    The agent is responsible for generating investment
    recommendations with a short-term horizon, typically
    ranging from a few weeks to a few months.

Why this agent exists:
    Short-term investments require quick decision-making
    based on market momentum and volatility. This agent
    simulates the role of a tactical investment advisor
    who focuses on near-term opportunities.
"""

# Import the Agent class from the PydanticAI framework.
# This class is used to create role-based intelligent agents.
from pydantic_ai import Agent

# Import the Pydantic schema that defines the structure
# of an investment recommendation.
# This schema is used later for validation by the orchestrator.
from schemas.investment_schema import InvestmentRecommendation

# Import the LLM configuration utility.
# This function returns the configured open-source
# language model running locally via Ollama.
from utils.llm_configuration import get_llm_model


# -------------------------------------------------------------------
# Short-Term Investment Agent Definition
# -------------------------------------------------------------------
# This agent is designed to generate short-term investment
# recommendations based on current market conditions.
#
# Key design considerations:
# - Enforce strict JSON-only output for reliability
# - Avoid function calling to simplify response parsing
# - Use retry logic to handle occasional formatting issues
# -------------------------------------------------------------------
short_term_investment_agent = Agent(
    # Specify the local open-source LLM to be used.
    # "llama3.2:latest" refers to the latest LLaMA model
    # served locally using Ollama.
    model=get_llm_model("llama3.2:latest"),

    # Number of retry attempts if the LLM output
    # does not follow the expected JSON structure.
    # This improves robustness when working with LLMs.
    retries=3,

    # System prompt defines the role, scope,
    # and strict output requirements for this agent.
    system_prompt="""
    You are a short-term investment advisor.

    Focus:
    - Time horizon: weeks to months
    - Market momentum and short-term volatility
    - Tactical investment opportunities

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
        "time_horizon": "Short-term"
    }

    Example output:
    {
        "asset_name": "NIFTY 50 ETF",
        "rationale": "Broad market exposure with stable growth potential",
        "risk_level": "Medium",
        "expected_return": "10-12% annually",
        "time_horizon": "Short-term"
    }
    """
)
