# Agentic AI Financial Advisor - Project Report

## Objective of the Task

The primary objective of this project is to build an intelligent Agentic AI-based financial advisor system that analyzes current market scenarios and provides comprehensive investment recommendations. The system should:

- Analyze global and Indian financial market conditions including macroeconomic indicators, interest rates, inflation, and geopolitical factors
- Generate short-term investment recommendations (weeks to months horizon) focusing on market momentum and volatility
- Generate long-term investment recommendations (multiple years horizon) focusing on fundamental strength and compounding growth
- Produce a complete analysis report with market insights and investment suggestions
- Use Pydantic AI framework with Ollama LLM for reliable and structured outputs

## Market Data Source

### Current Implementation
The system currently uses **LLM-based market analysis** as its data source:
- **Source**: Llama 3.2 model via Ollama (local LLM)
- **Data Basis**: Model's training data with knowledge cutoff in December 2023
- **Method**: The Market Analyst Agent generates analysis based on the LLM's understanding of historical market patterns, economic indicators, and trends
- **Limitation**: No real-time market data integration

### Data Source Analysis
```python
# From market_analyst_agent.py
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
```

### Recommended Improvements for Production
For a production-ready system, consider integrating real-time data sources:

1. **Financial APIs**:
   - Alpha Vantage API
   - Yahoo Finance API
   - Bloomberg Terminal API
   - NSE/BSE APIs for Indian markets

2. **Economic Indicators**:
   - Federal Reserve Economic Data (FRED)
   - World Bank Open Data
   - RBI Economic Data

3. **News and Sentiment**:
   - Financial news APIs (NewsAPI, Alpha Vantage News)
   - Social media sentiment analysis

### Example Enhancement
```python
# Potential enhancement for real-time data
import yfinance as yf
import requests

def get_realtime_market_data():
    # Fetch current market indices
    nifty = yf.Ticker("^NSEI").history(period="1d")
    sensex = yf.Ticker("^BSESN").history(period="1d")
    
    # Fetch economic indicators
    # API calls to financial data providers
    
    return market_data
```

### Brief Introduction
Pydantic AI is a Python framework for building agentic AI systems that combines the power of Large Language Models (LLMs) with structured data validation through Pydantic models. It provides a clean, type-safe way to create AI agents that can perform complex tasks with reliable output formatting.

### Advantages
- **Type Safety**: Uses Pydantic models to ensure structured, validated outputs from LLMs
- **Agent Orchestration**: Built-in support for multi-agent systems and complex workflows
- **Error Handling**: Robust retry mechanisms and validation error handling
- **Integration**: Easy integration with various LLM providers including Ollama
- **Async Support**: Full asynchronous programming support for scalable applications

### Disadvantages
- **Learning Curve**: Requires understanding of both Pydantic and agent patterns
- **Dependency**: Adds complexity compared to direct LLM API calls
- **Performance**: Additional validation overhead may impact speed for simple tasks

## Solution Flow/Workflow

The system follows a sequential agentic workflow orchestrated through a central coordinator:

### 1. Market Analysis Phase
- **Agent**: Market Analyst Agent
- **Input**: "Analyze current financial market conditions"
- **Process**: Analyzes global and Indian market trends, inflation, interest rates, geopolitics, and sentiment
- **Output**: Comprehensive market overview text

### 2. Short-Term Investment Phase
- **Agent**: Short-Term Investment Agent
- **Input**: Market analysis context + "Provide short-term investment recommendation"
- **Process**: Focuses on tactical opportunities, market momentum, and volatility (weeks-months horizon)
- **Output**: Structured JSON with asset_name, rationale, risk_level, expected_return, time_horizon

### 3. Long-Term Investment Phase
- **Agent**: Long-Term Investment Agent
- **Input**: Market analysis context + "Provide long-term investment recommendation"
- **Process**: Focuses on fundamental strength, risk-adjusted returns, and compounding (years horizon)
- **Output**: Structured JSON with asset_name, rationale, risk_level, expected_return, time_horizon

### 4. Report Generation Phase
- **Orchestrator**: Financial Orchestrator
- **Process**: Aggregates all agent outputs into formatted final report
- **Output**: Complete financial advisory report with market analysis and recommendations

## Agent Details

### 1. Market Analyst Agent (`market_analyst_agent.py`)
**Purpose**: Analyzes current global and Indian financial market conditions
- **Framework**: Pydantic AI Agent with Ollama Llama 3.2 model
- **System Prompt Focus**: Professional financial market analyst role
- **Responsibilities**:
  - Global and Indian market trend analysis
  - Macroeconomic indicators (inflation, interest rates)
  - Geopolitical factors and market sentiment
  - Concise, factual market overview generation
- **Output**: Text-based market analysis report
- **Key Features**: No structured output type (free-form analysis)

### 2. Short-Term Investment Agent (`short_term_investment_agent.py`)
**Purpose**: Provides tactical investment recommendations for weeks to months horizon
- **Framework**: Pydantic AI Agent with Ollama Llama 3.2 model
- **System Prompt Focus**: Short-term investment advisor role
- **Investment Focus**:
  - Market momentum and volatility
  - Tactical investment opportunities
  - Risk management for short timeframes
- **Output**: Structured JSON with InvestmentRecommendation schema
- **Key Features**:
  - Manual JSON parsing (no output_type validation)
  - 3 retry attempts for error handling
  - Explicit JSON format instructions

### 3. Long-Term Investment Agent (`long_term_investment_agent.py`)
**Purpose**: Provides strategic investment recommendations for multiple years horizon
- **Framework**: Pydantic AI Agent with Ollama Llama 3.2 model
- **System Prompt Focus**: Long-term investment advisor role
- **Investment Focus**:
  - Fundamental company strength
  - Risk-adjusted returns and compounding
  - Wealth creation and stability
- **Output**: Structured JSON with InvestmentRecommendation schema
- **Key Features**:
  - Manual JSON parsing (no output_type validation)
  - 3 retry attempts for error handling
  - Explicit JSON format instructions

### Common Agent Configuration
All agents share:
- **LLM Model**: Llama 3.2 via Ollama (localhost:11434)
- **Temperature**: 0.3 (balanced creativity vs consistency)
- **Max Tokens**: 2000 (sufficient for detailed responses)
- **Retry Logic**: 3 attempts with error handling
- **Base URL**: http://localhost:11434/v1 (Ollama API endpoint)

## File System Structure

```
agentic_financial_advisor/
├── main.py                          # Entry point script
├── requirements.txt                 # Python dependencies
├── test_*.py                        # Individual agent test scripts
├── agents/                          # Agent implementations
│   ├── __init__.py
│   ├── market_analyst_agent.py      # Market analysis agent
│   ├── short_term_investment_agent.py # Short-term investment agent
│   └── long_term_investment_agent.py  # Long-term investment agent
├── orchestrator/                    # Workflow coordination
│   ├── __init__.py
│   └── financial_orchestrator.py    # Main orchestrator logic
├── schemas/                         # Data models
│   ├── __init__.py
│   └── investment_schema.py         # Pydantic models for investments
├── utils/                           # Utilities
│   ├── __init__.py
│   └── llm_configuration.py         # LLM provider configuration
└── __pycache__/                     # Python bytecode cache
```

### Key Files Explanation

- **main.py**: Entry point that runs the complete workflow and displays the final report
- **agents/*.py**: Individual agent implementations with specialized prompts and logic
- **orchestrator/financial_orchestrator.py**: Coordinates agent execution and handles errors
- **schemas/investment_schema.py**: Defines structured output formats using Pydantic
- **utils/llm_configuration.py**: Configures Ollama LLM connection and settings

## How to Execute the Code

### Prerequisites
1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **Llama 3.2 model** downloaded: `ollama pull llama3.2:latest`

### Installation Steps
```bash
# Clone or navigate to project directory
cd agentic_financial_advisor

# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running
ollama serve
```

### Execution
```bash
# Run the complete system
python main.py

# Or test individual agents
python test_market_analyst_agent.py
python test_short_term_agent.py
python test_long_term_agent.py
```

### Expected Output
The system will display:
1. Workflow progress with agent execution status
2. Processing time
3. Complete financial advisory report including:
   - Market analysis summary
   - Short-term investment recommendation
   - Long-term investment recommendation

### Troubleshooting
- **Connection Error**: Ensure Ollama is running on localhost:11434
- **Model Not Found**: Run `ollama pull llama3.2:latest`
- **Import Errors**: Verify all dependencies are installed
- **Timeout**: Increase timeout in llm_configuration.py if needed

## Programming Standards Followed

### Code Quality
- **Well-structured**: Modular design with clear separation of concerns
- **Documented**: Comprehensive docstrings and inline comments
- **Named properly**: Descriptive variable/function names, no single/two character names
- **Error handling**: Try-catch blocks with specific error messages
- **Type hints**: Used where appropriate for clarity

### File Naming
- **snake_case**: All Python files use snake_case naming convention
- **Descriptive**: File names clearly indicate their purpose
- **Consistent**: Follows Python community standards

### Dependencies
- **Pinned versions**: All packages have specific versions in requirements.txt
- **Minimal**: Only necessary dependencies included
- **Compatible**: Tested with Python 3.8+ and current package versions

The system successfully demonstrates an agentic AI approach to financial advisory, providing structured, reliable investment recommendations based on comprehensive market analysis.