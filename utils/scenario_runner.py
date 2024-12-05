import json
import os
from pathlib import Path
from typing import Dict, Any
from examples.use_cases.tech_startup_analysis import analyze_tech_startup
from examples.use_cases.competitor_benchmark import benchmark_competitors
from examples.use_cases.market_entry_analysis import analyze_market_entry
from utils.report_generator import ReportGenerator

class ScenarioRunner:
    def __init__(self, scenarios_dir: str = 'examples/scenarios'):
        self.scenarios_dir = Path(scenarios_dir)
        self.report_generator = ReportGenerator()
    
    def load_scenario(self, scenario_file: str) -> Dict[str, Any]:
        """Load a scenario from a JSON file"""
        try:
            with open(self.scenarios_dir / scenario_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading scenario: {str(e)}")
    
    def run_scenario(self, scenario_file: str, output_dir: str = 'reports') -> str:
        """Run a specific scenario and generate report"""
        # Load scenario
        scenario = self.load_scenario(scenario_file)
        
        # Extract parameters
        scenario_type = self._get_scenario_type(scenario_file)
        params = self._extract_parameters(scenario)
        
        # Execute appropriate analysis
        if scenario_type == 'ai_startup':
            result = analyze_tech_startup(
                startup_name=params['company_name'],
                target_market=params['target_market']
            )
        elif scenario_type == 'market_entry':
            result = analyze_market_entry(
                company=params['company_name'],
                target_market=params['target_market'],
                strategy=params['strategy']
            )
        elif scenario_type == 'competitor_benchmark':
            result = benchmark_competitors(
                company=params['company_name'],
                competitors=params['competitors'],
                industry=params['industry']
            )
        else:
            raise ValueError(f"Unknown scenario type: {scenario_type}")
        
        # Generate and save report
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        report_file = output_path / f"{scenario_type}_{params['company_name'].lower()}.md"
        with open(report_file, 'w') as f:
            f.write(result)
        
        return str(report_file)
    
    def list_available_scenarios(self) -> list:
        """List all available scenario files"""
        return [f.name for f in self.scenarios_dir.glob('*.json')]
    
    def _get_scenario_type(self, scenario_file: str) -> str:
        """Extract scenario type from filename"""
        name = Path(scenario_file).stem
        if 'ai_startup' in name:
            return 'ai_startup'
        elif 'market_entry' in name:
            return 'market_entry'
        elif 'competitor_benchmark' in name:
            return 'competitor_benchmark'
        else:
            raise ValueError(f"Unknown scenario type in file: {scenario_file}")
    
    def _extract_parameters(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Extract necessary parameters from scenario"""
        params = {
            'company_name': scenario['target_company']['name'],
            'target_market': scenario['target_company']['target_market']
        }
        
        if 'key_competitors' in scenario.get('analysis_parameters', {}):
            params['competitors'] = scenario['analysis_parameters']['key_competitors']
        
        if 'industry' in scenario['target_company']:
            params['industry'] = scenario['target_company']['industry']
        
        if 'entry_strategy' in scenario.get('analysis_parameters', {}):
            params['strategy'] = scenario['analysis_parameters']['entry_strategy']
        
        return params