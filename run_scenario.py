import click
from utils.scenario_runner import ScenarioRunner

@click.command()
@click.option('--scenario', required=True, help='Scenario file to run')
@click.option('--output-dir', default='reports', help='Output directory for reports')
def run_scenario(scenario: str, output_dir: str):
    """Run a market research scenario"""
    runner = ScenarioRunner()
    
    # List available scenarios if requested
    if scenario.lower() == 'list':
        scenarios = runner.list_available_scenarios()
        click.echo("Available scenarios:")
        for s in scenarios:
            click.echo(f"  - {s}")
        return
    
    # Run the specified scenario
    try:
        click.echo(f"Running scenario: {scenario}")
        report_path = runner.run_scenario(scenario, output_dir)
        click.echo(f"Report generated: {report_path}")
    except Exception as e:
        click.echo(f"Error running scenario: {str(e)}", err=True)

if __name__ == '__main__':
    run_scenario()