"""
main.py

Entry point of the Agentic AI Financial Advisor system.
"""

from orchestrator.financial_orchestrator import run_agentic_financial_advisor


def main():
    """
    Executes the financial advisor system
    and prints the generated report.
    """
    import time
    start_time = time.time()

    final_report = run_agentic_financial_advisor()

    elapsed_time = time.time() - start_time
    
    print("\n" + "="*70)
    print("📋 FINAL FINANCIAL ADVISORY REPORT")
    print("="*70)
    print(f"⏱️  Total processing time: {elapsed_time:.2f} seconds")
    print("="*70 + "\n")

    print("\n" + "="*70)
    print("📊 MARKET ANALYSIS")
    print("="*70 + "\n")
    print(final_report["market_analysis"])

    print("\n" + "="*70)
    print("📈 SHORT-TERM INVESTMENT RECOMMENDATION")
    print("="*70 + "\n")
    investment = final_report["short_term_investment"]
    print(f"💼 Asset Name: {investment.asset_name}")
    print(f"📝 Rationale: {investment.rationale}")
    print(f"⚠️  Risk Level: {investment.risk_level}")
    print(f"📊 Expected Return: {investment.expected_return}")
    print(f"⏰ Time Horizon: {investment.time_horizon}")

    print("\n" + "="*70)
    print("🏛️  LONG-TERM INVESTMENT RECOMMENDATION")
    print("="*70 + "\n")
    investment = final_report["long_term_investment"]
    print(f"💼 Asset Name: {investment.asset_name}")
    print(f"📝 Rationale: {investment.rationale}")
    print(f"⚠️  Risk Level: {investment.risk_level}")
    print(f"📊 Expected Return: {investment.expected_return}")
    print(f"⏰ Time Horizon: {investment.time_horizon}")

    print("\n" + "="*70)
    print("✅ Report generation completed successfully!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
