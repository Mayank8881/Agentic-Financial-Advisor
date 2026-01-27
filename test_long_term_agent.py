"""
test_long_term_agent.py

Simple test script for the long-term investment agent.
"""

from agents.long_term_investment_agent import long_term_investment_agent
from orchestrator.financial_orchestrator import extract_investment_data

def test_long_term_agent():
    """Test the long-term investment agent with mock market context."""
    mock_market_context = """
    Current market conditions:
    - Global markets showing moderate volatility
    - Interest rates stable at 5-6%
    - Inflation concerns present but manageable
    - Technology sector showing resilience
    - Emerging markets offering opportunities
    - Long-term growth prospects remain positive
    """

    print("Testing Long-Term Investment Agent...")
    print("=" * 50)

    try:
        result = long_term_investment_agent.run_sync(
            f"Market Context: {mock_market_context}\n\nProvide a long-term investment recommendation. Return ONLY a JSON object with the required fields."
        )

        print(f"Raw output: {result.output}")
        print()

        # Parse the JSON
        investment = extract_investment_data(result.output)

        print("Parsed Investment Recommendation:")
        print(f"Asset Name: {investment.asset_name}")
        print(f"Rationale: {investment.rationale}")
        print(f"Risk Level: {investment.risk_level}")
        print(f"Expected Return: {investment.expected_return}")
        print(f"Time Horizon: {investment.time_horizon}")

        print("\n✅ Test completed successfully!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_long_term_agent()