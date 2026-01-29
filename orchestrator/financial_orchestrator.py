"""
Orchestrator: Financial Orchestrator

Purpose:
    This file defines the Financial Orchestrator.
    The orchestrator coordinates all intelligent agents,
    controls execution order, and compiles a unified
    financial advisory report.

Why this file is critical:
    In an agentic AI system, individual agents work in
    isolation. The orchestrator ensures these agents
    collaborate in a structured, controlled, and
    predictable manner—similar to how a team lead
    coordinates different specialists.
"""

# Import individual agents responsible for different tasks
from agents.market_analyst_agent import market_analyst_agent
from agents.short_term_investment_agent import short_term_investment_agent
from agents.long_term_investment_agent import long_term_investment_agent

# Import the Pydantic schema used to validate investment recommendations
from schemas.investment_schema import InvestmentRecommendation

# Import JSON library for parsing model outputs
import json


# -------------------------------------------------------------------
# Helper Function: Extract and Validate Investment Data
# -------------------------------------------------------------------
def extract_investment_data(result_output) -> InvestmentRecommendation:
    """
    Extracts and validates investment recommendation data
    returned by an investment agent.

    Why this function exists:
        LLM outputs may arrive either as a JSON string or
        as a Python dictionary. This function normalizes
        the output and ensures it strictly follows the
        InvestmentRecommendation schema.

    Args:
        result_output:
            Raw output returned by an investment agent
            (either JSON string or dictionary).

    Returns:
        InvestmentRecommendation:
            A validated Pydantic object containing
            structured investment recommendation data.

    Raises:
        ValueError:
            If the output cannot be parsed or does not
            match the expected schema.
    """
    try:
        # If the agent output is a string, parse it as JSON
        if isinstance(result_output, str):
            data = json.loads(result_output)
        else:
            # If already a dictionary, use it directly
            data = result_output

        # Validate and convert data into a Pydantic model
        return InvestmentRecommendation(**data)

    except (json.JSONDecodeError, TypeError) as e:
        # Raise a clear error if parsing or validation fails
        raise ValueError(f"Failed to parse investment data: {e}")


# -------------------------------------------------------------------
# Main Orchestration Function
# -------------------------------------------------------------------
def run_agentic_financial_advisor() -> dict:
    """
    Executes the complete agentic financial advisory workflow.

    Workflow Overview:
        1. Market Analyst Agent analyzes current market conditions
        2. Short-Term Investment Agent generates tactical recommendations
        3. Long-Term Investment Agent generates strategic recommendations
        4. Orchestrator aggregates all outputs into a final report

    Returns:
        dict:
            A dictionary containing:
            - Market analysis summary
            - Short-term investment recommendation
            - Long-term investment recommendation
    """

    # Print header to clearly indicate workflow start
    print("\n" + "=" * 70)
    print("🤖 AGENTIC AI FINANCIAL ADVISOR - WORKFLOW STARTED")
    print("=" * 70)

    # ---------------------------------------------------------------
    # Step 1: Market Analysis
    # ---------------------------------------------------------------
    print("\n[1/3] 📊 Running Market Analyst Agent (LLaMA 3.2)...")
    print("      Analyzing current financial market conditions...")

    # Execute market analysis agent synchronously
    market_analysis_result = market_analyst_agent.run_sync(
        "Analyze current financial market conditions."
    )

    print("      ✅ Market analysis completed!\n")

    # ---------------------------------------------------------------
    # Step 2: Short-Term Investment Recommendation
    # ---------------------------------------------------------------
    print("[2/3] 📈 Running Short-Term Investment Agent (LLaMA 3.2)...")
    print("      Generating short-term investment recommendations...")

    short_term_investment = None
    try:
        # Pass market analysis as context to the short-term agent
        short_term_result = short_term_investment_agent.run_sync(
            f"Market Context: {market_analysis_result.output}\n\n"
            "Provide a short-term investment recommendation. "
            "Return ONLY a JSON object with the required fields."
        )

        # Parse and validate the agent output
        short_term_investment = extract_investment_data(
            short_term_result.output
        )

        print("      ✅ Short-term recommendation completed!\n")

    except Exception as e:
        # Capture and surface any error clearly
        print(f"      ❌ Error in short-term agent: {e}")
        raise

    # ---------------------------------------------------------------
    # Step 3: Long-Term Investment Recommendation
    # ---------------------------------------------------------------
    print("[3/3] 🏛️  Running Long-Term Investment Agent (LLaMA 3.2)...")
    print("      Generating long-term investment recommendations...")

    long_term_investment = None
    try:
        # Pass the same market context to the long-term agent
        long_term_result = long_term_investment_agent.run_sync(
            f"Market Context: {market_analysis_result.output}\n\n"
            "Provide a long-term investment recommendation. "
            "Return ONLY a JSON object with the required fields."
        )

        # Parse and validate the agent output
        long_term_investment = extract_investment_data(
            long_term_result.output
        )

        print("      ✅ Long-term recommendation completed!\n")

    except Exception as e:
        print(f"      ❌ Error in long-term agent: {e}")
        raise

    # ---------------------------------------------------------------
    # Final Aggregation
    # ---------------------------------------------------------------
    print("=" * 70)
    print("✨ All agents completed successfully! Generating final report...")
    print("=" * 70 + "\n")

    # Return the aggregated results in a structured format
    return {
        "market_analysis": market_analysis_result.output,
        "short_term_investment": short_term_investment,
        "long_term_investment": long_term_investment
    }
