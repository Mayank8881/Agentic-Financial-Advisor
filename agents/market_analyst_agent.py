"""
market_analyst_agent.py

Purpose:
    Analyzes current market conditions including
    macroeconomic indicators and general sentiment.
"""

from pydantic_ai import Agent
from utils.llm_configuration import get_llm_model

market_analyst_agent = Agent(
    model=get_llm_model("llama3.2:latest"),
    system_prompt="""
    You are a professional financial market analyst.

    Responsibilities:
    - Analyze current global and Indian market trends
    - Consider inflation, interest rates, geopolitics, and sentiment
    - Provide a concise, factual market overview
    """
)
