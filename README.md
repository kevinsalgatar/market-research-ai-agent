# Market Research AI Agent

An advanced AI agent system for conducting comprehensive market research using CrewAI. This system employs multiple specialized agents to gather, analyze, and present market research data.

## Features

- **Comprehensive Market Research**: Industry analysis, competitor research, and trend identification
- **Data Analysis**: Statistical analysis and data visualization
- **Report Generation**: Automated creation of detailed market research reports
- **Multi-Agent System**: Specialized agents for different aspects of market research
- **Extensible Architecture**: Easy to add new capabilities and customize existing ones
- **Pre-built Scenarios**: Ready-to-use market research scenarios for common use cases

## Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key
- SERP API key (for web searches)
- Browserless API key (for web scraping)

### Installation

```bash
# Clone the repository
git clone https://github.com/kevinsalgatar/market-research-ai-agent.git
cd market-research-ai-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running Example Scenarios

```bash
# List available scenarios
python run_scenario.py --scenario list

# Run AI startup analysis scenario
python run_scenario.py --scenario ai_startup_analysis.json

# Run market entry analysis scenario
python run_scenario.py --scenario market_entry_fintech.json

# Run competitor benchmark scenario
python run_scenario.py --scenario competitor_benchmark_ecommerce.json
```

### Using the CLI

```bash
# Analyze a startup
python cli.py analyze-startup \
    --startup-name "TechCorp" \
    --target-market "AI Software"

# Benchmark competitors
python cli.py benchmark \
    --company "MainCorp" \
    --competitors "Competitor1,Competitor2,Competitor3" \
    --industry "Software"

# Analyze market entry
python cli.py market-entry \
    --company "GlobalCorp" \
    --target-market "Southeast Asia" \
    --strategy "Joint Venture"
```

## Architecture

### Agent System

The system uses three main types of agents:

1. **Market Researcher Agent**
   - Gathers information from various sources
   - Conducts competitor analysis
   - Identifies market opportunities

2. **Data Analyst Agent**
   - Processes and analyzes market data
   - Creates visualizations
   - Identifies trends and patterns

3. **Report Writer Agent**
   - Synthesizes information into coherent reports
   - Creates executive summaries
   - Generates recommendations

### Tools and Utilities

1. **Data Processing**
   - Market data processor
   - Competitor data processor
   - Trend data processor

2. **Visualization**
   - Market share charts
   - Trend analysis graphs
   - Competitive matrices

3. **Report Generation**
   - Template-based generation
   - Multiple format support (MD, HTML)
   - Custom styling options

## Example Scenarios

### 1. AI Startup Analysis
- Comprehensive analysis of AI/ML market
- Competitor analysis of major AI companies
- Market size and growth projections
- Customer segment analysis

### 2. Fintech Market Entry
- Regional market assessment
- Regulatory environment analysis
- Competitive landscape evaluation
- Entry strategy recommendations

### 3. E-commerce Platform Benchmark
- Feature comparison with major platforms
- Market share analysis
- Customer experience evaluation
- Growth metrics comparison

## Configuration

### Environment Variables
```env
OPENAI_API_KEY=your_openai_api_key
SERP_API_KEY=your_serp_api_key
BROWERLESS_API_KEY=your_browserless_api_key
```

### Configuration Files
- `config/settings.py`: Agent and task configuration
- `config/prompts.py`: Customizable prompts for agents
- `config/cli_config.yaml`: CLI behavior configuration

## Development

### Project Structure
```
market-research-ai-agent/
├── agents/              # Agent definitions
├── tools/              # Tool implementations
├── tasks/              # Task definitions
├── utils/              # Utility functions
├── config/             # Configuration files
├── examples/           # Example scenarios
├── tests/              # Test suite
└── reports/            # Generated reports
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_agents.py

# Run with coverage
python -m pytest --cov=. tests/
```

### Adding New Features

1. **Creating New Agents**
   ```python
   from crewai import Agent
   
   class NewAgent:
       def create(self):
           return Agent(
               role='New Role',
               goal='Specific goal',
               backstory='Agent backstory',
               tools=[...]
           )
   ```

2. **Adding New Tools**
   ```python
   from langchain.tools import Tool
   
   class NewTool:
       def some_function(self, input: str) -> str:
           # Implementation
           return result
       
       def get_tools(self):
           return [Tool.from_function(
               func=self.some_function,
               name="Tool Name",
               description="Tool description"
           )]
   ```

3. **Creating Custom Scenarios**
   ```json
   {
       "scenario": "Scenario Name",
       "target_company": {
           "name": "Company Name",
           "industry": "Industry"
       },
       "analysis_parameters": {
           "timeframe": "12months",
           "focus_areas": [...]
       }
   }
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- CrewAI for the multi-agent framework
- OpenAI for language models
- Various open-source tools and libraries