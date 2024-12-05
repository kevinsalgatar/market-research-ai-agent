import json
from typing import Dict, Any

class ReportFormatter:
    @staticmethod
    def format_markdown(data: Dict[str, Any]) -> str:
        """Convert report data to markdown format"""
        markdown = f"# Market Research Report\n\n"
        markdown += f"Generated on: {data.get('timestamp', '')}\n\n"
        
        # Executive Summary
        markdown += "## Executive Summary\n\n"
        markdown += f"{data.get('executive_summary', '')}\n\n"
        
        # Company Overview
        markdown += "## Company Overview\n\n"
        markdown += f"{data.get('company_overview', '')}\n\n"
        
        # Market Analysis
        markdown += "## Market Analysis\n\n"
        if 'market_analysis' in data:
            market_data = data['market_analysis']
            markdown += f"Market Size: {market_data.get('market_size', '')}\n"
            markdown += f"Growth Rate: {market_data.get('growth_rate', '')}\n\n"
        
        # Trends
        markdown += "## Market Trends\n\n"
        if 'trends' in data:
            for trend in data['trends']:
                markdown += f"- {trend}\n"
        
        # Recommendations
        markdown += "\n## Recommendations\n\n"
        if 'recommendations' in data:
            for rec in data['recommendations']:
                markdown += f"- {rec}\n"
        
        return markdown
    
    @staticmethod
    def save_report(content: str, filename: str) -> None:
        """Save report to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)