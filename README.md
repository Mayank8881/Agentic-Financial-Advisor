# Agentic Financial Advisor

## Description

The Agentic AI Financial Advisor is an intelligent system built using the Pydantic AI framework and Ollama LLM. It analyzes current market scenarios and provides comprehensive investment recommendations for both short-term and long-term horizons. The system leverages AI agents to evaluate global and Indian financial markets, considering factors like macroeconomic indicators, interest rates, inflation, and geopolitical events.

## Features

- **Market Analysis Agent**: Provides concise market overviews based on current trends.
- **Short-Term Investment Agent**: Generates recommendations for weeks to months horizon, focusing on momentum and volatility.
- **Long-Term Investment Agent**: Offers recommendations for multi-year horizons, emphasizing fundamental strength and growth.
- **Financial Orchestrator**: Coordinates all agents to produce a complete analysis report.
- **Structured Outputs**: Uses Pydantic schemas for reliable and structured investment recommendations.

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Llama 3.2 model pulled in Ollama (`ollama pull llama3.2`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mayank8881/Agentic-Financial-Advisor.git
   cd agentic_financial_advisor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Ollama is running and the Llama 3.2 model is available:
   ```bash
   ollama serve
   ollama pull llama3.2
   ```

## Usage

Run the main script to generate a financial advisory report:

```bash
python main.py
```

The script will:
- Analyze current market conditions
- Generate short-term and long-term investment recommendations
- Display the results in a formatted report

Processing may take a few minutes due to LLM inference.

## Project Structure

```
agentic_financial_advisor/
├── main.py                          # Entry point
├── requirements.txt                 # Python dependencies
├── PROJECT_REPORT.md                # Detailed project report
├── agents/                          # AI agents
│   ├── market_analyst_agent.py      # Market analysis agent
│   ├── short_term_investment_agent.py # Short-term recommendations
│   └── long_term_investment_agent.py  # Long-term recommendations
├── orchestrator/                    # Coordination logic
│   └── financial_orchestrator.py    # Main orchestrator
├── schemas/                         # Data models
│   └── investment_schema.py         # Pydantic schemas
├── utils/                           # Utilities
│   └── llm_configuration.py         # LLM setup
└── test_*.py                        # Test files
```

## Testing

Run the test files to validate individual components:

```bash
python test_market_analyst_agent.py
python test_short_term_agent.py
python test_long_term_agent.py
```

## Contributing

Contributions are welcome! Please ensure to follow the project structure and add tests for new features.

## License

This project is for educational purposes. Check the repository for licensing details.
