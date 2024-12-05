# Market Research AI Agent CLI Usage Guide

## Overview

The Market Research AI Agent CLI provides easy access to various market research and analysis capabilities. This guide covers the main commands and their usage.

## Installation

```bash
# Install the package
pip install -e .

# Verify installation
python cli.py --help
```

## Commands

### 1. Analyze Startup

Analyze a technology startup and its market potential.

```bash
# Basic usage
python cli.py analyze-startup \
    --startup-name "TechCorp" \
    --target-market "AI Software"

# With additional options
python cli.py analyze-startup \
    --startup-name "TechCorp" \
    --target-market "AI Software" \
    --output "custom_reports" \
    --format html
```

### 2. Benchmark Competitors

Perform competitive benchmarking analysis.

```bash
# Basic usage
python cli.py benchmark \
    --company "MainCorp" \
    --competitors "Competitor1,Competitor2,Competitor3" \
    --industry "Software"

# With additional options
python cli.py benchmark \
    --company "MainCorp" \
    --competitors "Competitor1,Competitor2,Competitor3" \
    --industry "Software" \
    --output "benchmarks" \
    --format html
```

### 3. Analyze Market Entry

Analyze market entry potential and strategy.

```bash
# Basic usage
python cli.py market-entry \
    --company "GlobalCorp" \
    --target-market "Southeast Asia" \
    --strategy "Joint Venture"

# With additional options
python cli.py market-entry \
    --company "GlobalCorp" \
    --target-market "Southeast Asia" \
    --strategy "Joint Venture" \
    --output "market_entry" \
    --format html
```

## Output Formats

### Markdown (Default)
- Clean, readable format
- Easy to version control
- Can be converted to other formats

### HTML
- Interactive charts and visualizations
- Responsive design
- Easy to share and view in browsers

## Configuration

The CLI behavior can be customized through the `config/cli_config.yaml` file:

- Output directory settings
- Report format preferences
- Visualization options
- API configuration

## Examples

### Generate a Complete Market Analysis

```bash
# Analyze startup
python cli.py analyze-startup \
    --startup-name "AI Solutions Inc" \
    --target-market "Enterprise AI" \
    --format html

# Analyze competitors
python cli.py benchmark \
    --company "AI Solutions Inc" \
    --competitors "OpenAI,Anthropic,Cohere" \
    --industry "AI Technology"

# Analyze market entry strategy
python cli.py market-entry \
    --company "AI Solutions Inc" \
    --target-market "European Market" \
    --strategy "Direct Entry"
```

## Best Practices

1. Always provide specific and accurate company/market names
2. Use HTML format for reports that need interactive visualizations
3. Regularly clean the reports directory to manage space
4. Keep competitor lists focused and relevant

## Troubleshooting

Common issues and solutions:

1. **API Rate Limits**
   - Increase retry delays in config
   - Use rate limiting features

2. **Memory Issues**
   - Reduce the scope of analysis
   - Clear report cache regularly

3. **Report Generation Errors**
   - Check input data format
   - Verify template compatibility

## Support

For issues and feature requests:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include CLI command and error messages