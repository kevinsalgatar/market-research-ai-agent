# Market Research AI Agent

An AI agent system for market research and analysis using CrewAI.

## Features

- Market Trend Analysis
- Competitor Research
- Consumer Sentiment Analysis
- Industry Reports Generation
- Data Visualization

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your API keys
4. Run the main script: `python main.py`

## Usage

```python
python main.py --industry "tech" --company "example corp" --timeframe "3months"
```

## Architecture

The system uses multiple specialized agents:
- Market Researcher Agent
- Data Analyst Agent
- Report Writer Agent
- Trend Analyzer Agent

These agents work together in a crew to produce comprehensive market research reports.

## License

MIT