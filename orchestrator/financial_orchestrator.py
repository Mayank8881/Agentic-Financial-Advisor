"""
financial_orchestrator.py

Purpose:
    Coordinates multiple agents and compiles
    a unified financial advisory report.
"""

from agents.market_analyst_agent import market_analyst_agent
from agents.short_term_investment_agent import short_term_investment_agent
from agents.long_term_investment_agent import long_term_investment_agent
from schemas.investment_schema import InvestmentRecommendation
import json


def extract_investment_data(result_output) -> InvestmentRecommendation:
    """
    Extracts investment recommendation data from agent result.
    Handles both JSON string and dict formats.
    
    Args:
        result_output: The output string from the agent
        
    Returns:
        InvestmentRecommendation: Properly formatted investment recommendation
    """
    try:
        # If it's a string, parse as JSON
        if isinstance(result_output, str):
            data = json.loads(result_output)
        else:
            data = result_output
            
        # Create InvestmentRecommendation object
        return InvestmentRecommendation(**data)
    except (json.JSONDecodeError, TypeError) as e:
        raise ValueError(f"Failed to parse investment data: {e}")


def run_agentic_financial_advisor() -> dict:
    """
    Executes the complete agentic financial advisory workflow.

    Workflow:
        1. Market Analyst Agent analyzes market conditions
        2. Short-term agent generates tactical recommendations
        3. Long-term agent generates strategic recommendations
        4. Results are aggregated into a final report

    Returns:
        dict:
            Dictionary containing market analysis,
            short-term and long-term recommendations.
    """

    print("\n" + "="*70)
    print("🤖 AGENTIC AI FINANCIAL ADVISOR - WORKFLOW STARTED")
    print("="*70)
    
    # Step 1: Market Analysis
    print("\n[1/3] 📊 Running Market Analyst Agent (Llama 3.2)...")
    print("      Analyzing current financial market conditions...")
    market_analysis_result = market_analyst_agent.run_sync(
        "Analyze current financial market conditions."
    )
    print("      ✅ Market analysis completed!\n")

    # Step 2: Short-Term Recommendation
    print("[2/3] 📈 Running Short-Term Investment Agent (Llama 3.2)...")
    print("      Generating short-term investment recommendations...")
    short_term_investment = None
    try:
        short_term_result = short_term_investment_agent.run_sync(
            f"Market Context: {market_analysis_result.output}\n\nProvide a short-term investment recommendation. Return ONLY a JSON object with the required fields."
        )
        short_term_investment = extract_investment_data(short_term_result.output)
        print("      ✅ Short-term recommendation completed!\n")
    except Exception as e:
        print(f"      ❌ Error in short-term agent: {e}")
        raise

    # Step 3: Long-Term Recommendation
    print("[3/3] 🏛️  Running Long-Term Investment Agent (Llama 3.2)...")
    print("      Generating long-term investment recommendations...")
    long_term_investment = None
    try:
        long_term_result = long_term_investment_agent.run_sync(
            f"Market Context: {market_analysis_result.output}\n\nProvide a long-term investment recommendation. Return ONLY a JSON object with the required fields."
        )
        long_term_investment = extract_investment_data(long_term_result.output)
        print("      ✅ Long-term recommendation completed!\n")
    except Exception as e:
        print(f"      ❌ Error in long-term agent: {e}")
        raise

    print("="*70)
    print("✨ All agents completed successfully! Generating final report...")
    print("="*70 + "\n")

    return {
        "market_analysis": market_analysis_result.output,
        "short_term_investment": short_term_investment,
        "long_term_investment": long_term_investment
    }
