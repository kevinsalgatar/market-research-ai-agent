# Market Research AI Agent

An advanced AI agent system for conducting comprehensive market research using CrewAI. This system employs multiple specialized agents to gather, analyze, and present market research data.

## Features

- **Comprehensive Market Research**: Industry analysis, competitor research, and trend identification
- **Data Analysis**: Statistical analysis and data visualization
- **Report Generation**: Automated creation of detailed market research reports
- **Multi-Agent System**: Specialized agents for different aspects of market research
- **Extensible Architecture**: Easy to add new capabilities and customize existing ones

## Architecture

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

## Prerequisites

- Python 3.9+
- OpenAI API key
- SERP API key (for web searches)
- Browserless API key (for web scraping)

## Installation

### Using pip

```bash
# Clone the repository
git clone https://github.com/kevinsalgatar/market-research-ai-agent.git
cd market-research-ai-agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Using Docker

```bash
# Build the Docker image
docker build -t market-research-agent .

# Run the container
docker run -v $(pwd)/reports:/app/reports --env-file .env market-research-agent
```

## Usage

### Basic Usage

```bash
python main.py --industry "tech" --company "Example Corp" --timeframe "3months"
```

### Advanced Usage

```python
from crewai import Crew
from agents.market_researcher import MarketResearcherAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_writer import ReportWriterAgent
from tasks.market_research_tasks import MarketResearchTasks

# Initialize agents
researcher = MarketResearcherAgent().create()
analyst = DataAnalystAgent().create()
writer = ReportWriterAgent().create()

# Create tasks
tasks = MarketResearchTasks(researcher, analyst, writer)

# Define task list
task_list = [
    tasks.research_company("Example Corp"),
    tasks.analyze_market_data("tech"),
    tasks.identify_trends("3months"),
]

# Create and run the crew
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=task_list,
    verbose=True
)

result = crew.kickoff()
```

## Configuration

The system can be configured through several files:

- `.env`: API keys and environment variables
- `config/settings.py`: Agent and task configuration
- `config/prompts.py`: Customizable prompts for agents

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_agents.py
```

### Adding New Capabilities

1. Create new agent in `agents/`
2. Add corresponding tools in `tools/`
3. Define tasks in `tasks/`
4. Update configuration as needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- CrewAI for the multi-agent framework
- OpenAI for language models
- Various open-source tools and libraries