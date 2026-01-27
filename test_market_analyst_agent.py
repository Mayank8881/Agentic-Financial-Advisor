"""
test_market_analyst_agent.py

Simple test script for the market analyst agent.
"""

from agents.market_analyst_agent import market_analyst_agent

def test_market_analyst_agent():
    """Test the market analyst agent."""

    print("Testing Market Analyst Agent...")
    print("=" * 50)

    try:
        result = market_analyst_agent.run_sync(
            "Analyze current financial market conditions."
        )

        print("Market Analysis Output:")
        print(result.output)

        print("\n✅ Test completed successfully!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_market_analyst_agent()