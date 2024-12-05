import click
import json
from datetime import datetime
from pathlib import Path
from examples.use_cases.tech_startup_analysis import analyze_tech_startup
from examples.use_cases.competitor_benchmark import benchmark_competitors
from examples.use_cases.market_entry_analysis import analyze_market_entry
from utils.report_generator import ReportGenerator

@click.group()
def cli():
    """Market Research AI Agent CLI"""
    pass

@cli.command()
@click.option('--startup-name', required=True, help='Name of the startup to analyze')
@click.option('--target-market', required=True, help='Target market segment')
@click.option('--output', default='reports', help='Output directory for the report')
@click.option('--format', type=click.Choice(['md', 'html']), default='md', help='Output format')
def analyze_startup(startup_name, target_market, output, format):
    """Analyze a technology startup and its market potential"""
    click.echo(f"Analyzing startup: {startup_name} in market: {target_market}")
    
    # Run analysis
    result = analyze_tech_startup(startup_name, target_market)
    
    # Generate report
    report_gen = ReportGenerator()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{startup_name.lower().replace(' ', '_')}_{timestamp}.{format}"
    
    if format == 'html':
        result = report_gen.convert_to_html(result)
    
    # Save report
    output_path = Path(output)
    output_path.mkdir(exist_ok=True)
    report_path = output_path / filename
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Report generated: {report_path}")

@cli.command()
@click.option('--company', required=True, help='Main company to analyze')
@click.option('--competitors', required=True, help='Comma-separated list of competitors')
@click.option('--industry', required=True, help='Industry sector')
@click.option('--output', default='reports', help='Output directory for the report')
@click.option('--format', type=click.Choice(['md', 'html']), default='md', help='Output format')
def benchmark(company, competitors, industry, output, format):
    """Perform competitive benchmarking analysis"""
    competitor_list = [c.strip() for c in competitors.split(',')]
    click.echo(f"Benchmarking {company} against {', '.join(competitor_list)}")
    
    # Run analysis
    result = benchmark_competitors(company, competitor_list, industry)
    
    # Generate report
    report_gen = ReportGenerator()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{company.lower().replace(' ', '_')}_benchmark_{timestamp}.{format}"
    
    if format == 'html':
        result = report_gen.convert_to_html(result)
    
    # Save report
    output_path = Path(output)
    output_path.mkdir(exist_ok=True)
    report_path = output_path / filename
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Report generated: {report_path}")

@cli.command()
@click.option('--company', required=True, help='Company planning market entry')
@click.option('--target-market', required=True, help='Target market for entry')
@click.option('--strategy', required=True, help='Market entry strategy')
@click.option('--output', default='reports', help='Output directory for the report')
@click.option('--format', type=click.Choice(['md', 'html']), default='md', help='Output format')
def market_entry(company, target_market, strategy, output, format):
    """Analyze market entry potential and strategy"""
    click.echo(f"Analyzing market entry for {company} into {target_market}")
    
    # Run analysis
    result = analyze_market_entry(company, target_market, strategy)
    
    # Generate report
    report_gen = ReportGenerator()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{company.lower().replace(' ', '_')}_market_entry_{timestamp}.{format}"
    
    if format == 'html':
        result = report_gen.convert_to_html(result)
    
    # Save report
    output_path = Path(output)
    output_path.mkdir(exist_ok=True)
    report_path = output_path / filename
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Report generated: {report_path}")

if __name__ == '__main__':
    cli()