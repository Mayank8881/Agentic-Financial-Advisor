"""
investment_schema.py

Purpose:
    Defines structured output formats for investment recommendations.
    Pydantic ensures type safety, validation, and clarity.
"""

from pydantic import BaseModel, Field


class InvestmentRecommendation(BaseModel):
    """
    Represents a single investment recommendation.

    Attributes:
        asset_name (str):
            Name of the financial instrument or asset.

        rationale (str):
            Explanation of why the investment is recommended.

        risk_level (str):
            Risk classification (Low / Medium / High).

        expected_return (str):
            Expected return range or description.

        time_horizon (str):
            Investment duration (Short-term / Long-term).

    Example:
        InvestmentRecommendation(
            asset_name="NIFTY 50 ETF",
            rationale="Broad market exposure with stable growth",
            risk_level="Medium",
            expected_return="10-12% annually",
            time_horizon="Long-term"
        )
    """

    asset_name: str = Field(..., example="NIFTY 50 ETF")
    rationale: str
    risk_level: str
    expected_return: str
    time_horizon: str
