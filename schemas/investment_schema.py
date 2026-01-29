"""
Investment Schema

Purpose:
    This file defines the structured data model used for
    investment recommendations across the system.

Why this file exists:
    - Ensures all investment recommendations follow
      a consistent and predictable structure
    - Prevents malformed or ambiguous outputs from LLMs
    - Enables automatic validation using Pydantic
    - Makes outputs easier to read, debug, and integrate
      with other systems
"""

# Import BaseModel and Field from Pydantic.
# BaseModel is used to define structured data models,
# while Field allows additional metadata and validation.
from pydantic import BaseModel, Field


class InvestmentRecommendation(BaseModel):
    """
    Represents a single investment recommendation produced
    by the Short-Term or Long-Term Investment Agent.

    Why this model is important:
        Large Language Models can return unpredictable outputs.
        This schema enforces a strict format, ensuring that
        every recommendation contains all required fields
        in a clear and validated structure.

    Attributes:
        asset_name (str):
            Name of the recommended financial instrument
            (e.g., ETF, stock, mutual fund, index fund).

        rationale (str):
            Clear explanation describing why this
            investment is being recommended.

        risk_level (str):
            Indicates the risk associated with the investment.
            Allowed values typically include:
            - "Low"
            - "Medium"
            - "High"

        expected_return (str):
            Description or range of expected returns
            (e.g., "10-12% annually").

        time_horizon (str):
            Specifies whether the recommendation is intended
            for a short-term or long-term investment horizon.
    """

    # Name of the financial asset being recommended.
    # The example value helps documentation and readability.
    asset_name: str = Field(
        ...,
        example="NIFTY 50 ETF"
    )

    # Explanation justifying the investment recommendation.
    rationale: str

    # Risk classification of the investment.
    risk_level: str

    # Expected return description or range.
    expected_return: str

    # Investment time horizon (Short-term or Long-term).
    time_horizon: str
