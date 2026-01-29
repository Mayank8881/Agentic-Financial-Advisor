"""
Market Analyst Agent

Purpose:
    This file defines the Market Analyst Agent.
    The agent is responsible for analyzing the current
    financial market environment and producing a
    high-level market overview.

Why this agent exists:
    In real-world financial advisory systems, market analysis
    is the first and most critical step. This agent mimics the
    role of a professional market analyst who studies
    economic conditions before any investment decisions
    are made.
"""

# Import the Agent class from the PydanticAI framework.
# This class is used to define intelligent, role-based AI agents.
from pydantic_ai import Agent

# Import the LLM configuration utility.
# This function returns the configured language model
# (running locally via Ollama).
from utils.llm_configuration import get_llm_model


# -------------------------------------------------------------------
# Market Analyst Agent Definition
# -------------------------------------------------------------------
# This agent uses a locally running open-source LLM (via Ollama)
# and is initialized with a system prompt that defines its role,
# responsibilities, and expected behavior.
#
# The system_prompt acts as instructions for the LLM, ensuring
# that responses remain factual, structured, and finance-focused.
# -------------------------------------------------------------------
market_analyst_agent = Agent(
    # Specify the language model to be used by this agent.
    # "llama3.2:latest" refers to the latest version of the LLaMA model
    # running locally through Ollama.
    model=get_llm_model("llama3.2:latest"),

    # System prompt defines the role and scope of this agent.
    # It guides the LLM to behave like a professional financial analyst.
    system_prompt="""
    You are a professional financial market analyst.

    Responsibilities:
    - Analyze current global and Indian market trends
    - Evaluate macroeconomic factors such as inflation,
      interest rates, and geopolitical events
    - Assess overall market sentiment
    - Provide a concise, factual, and easy-to-understand
      market overview that can be used by other agents
      for investment decision-making
    """
)
