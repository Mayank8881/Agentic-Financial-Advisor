"""

Main.py

Purpose:
    This file serves as the entry point of the Agentic AI
    Financial Advisor system.

Why this file exists:
    - Acts as the starting point for system execution
    - Invokes the orchestrator to run the complete workflow
    - Formats and displays the final financial advisory report
      in a clear, human-readable manner
"""

# Import the main orchestration function that coordinates
# all agents and generates the final report.
from orchestrator.financial_orchestrator import run_agentic_financial_advisor


def main():
    """
    Executes the Agentic AI Financial Advisor system.

    Responsibilities:
        - Measure total execution time
        - Trigger the agentic workflow via the orchestrator
        - Display market analysis and investment recommendations
          in a clean, client-friendly format
    """

    # Import time module locally to measure execution duration.
    # This helps evaluate system performance and responsiveness.
    import time

    # Record the start time before running the workflow
    start_time = time.time()

    # Execute the full agentic workflow.
    # This call triggers all agents and returns a structured report.
    final_report = run_agentic_financial_advisor()

    # Calculate total execution time
    elapsed_time = time.time() - start_time

    # -----------------------------------------------------------
    # Display Report Header and Execution Summary
    # -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("📋 FINAL FINANCIAL ADVISORY REPORT")
    print("=" * 70)
    print(f"⏱️  Total processing time: {elapsed_time:.2f} seconds")
    print("=" * 70 + "\n")

    # -----------------------------------------------------------
    # Display Market Analysis Section
    # -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("📊 MARKET ANALYSIS")
    print("=" * 70 + "\n")

    # Market analysis is presented as a textual summary
    print(final_report["market_analysis"])

    # -----------------------------------------------------------
    # Display Short-Term Investment Recommendation
    # -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("📈 SHORT-TERM INVESTMENT RECOMMENDATION")
    print("=" * 70 + "\n")

    # Extract short-term investment recommendation object
    investment = final_report["short_term_investment"]

    # Display each field in a user-friendly format
    print(f"💼 Asset Name: {investment.asset_name}")
    print(f"📝 Rationale: {investment.rationale}")
    print(f"⚠️  Risk Level: {investment.risk_level}")
    print(f"📊 Expected Return: {investment.expected_return}")
    print(f"⏰ Time Horizon: {investment.time_horizon}")

    # -----------------------------------------------------------
    # Display Long-Term Investment Recommendation
    # -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("🏛️  LONG-TERM INVESTMENT RECOMMENDATION")
    print("=" * 70 + "\n")

    # Extract long-term investment recommendation object
    investment = final_report["long_term_investment"]

    # Display long-term investment details
    print(f"💼 Asset Name: {investment.asset_name}")
    print(f"📝 Rationale: {investment.rationale}")
    print(f"⚠️  Risk Level: {investment.risk_level}")
    print(f"📊 Expected Return: {investment.expected_return}")
    print(f"⏰ Time Horizon: {investment.time_horizon}")

    # -----------------------------------------------------------
    # Completion Message
    # -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("✅ Report generation completed successfully!")
    print("=" * 70 + "\n")


# Standard Python entry-point check.
# Ensures that the main function runs only
# when this file is executed directly.
if __name__ == "__main__":
    main()
