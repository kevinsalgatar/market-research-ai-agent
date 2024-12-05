import pandas as pd
import numpy as np
from typing import Dict, List

class DataProcessor:
    @staticmethod
    def clean_text_data(text: str) -> str:
        """Clean and normalize text data"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = " ".join(text.split())
        
        # Basic text cleaning
        text = text.strip()
        
        return text
    
    @staticmethod
    def extract_key_metrics(data: Dict) -> Dict:
        """Extract key metrics from market data"""
        metrics = {
            'market_size': data.get('market_size', 0),
            'growth_rate': data.get('growth_rate', 0),
            'market_share': data.get('market_share', {}),
            'key_indicators': data.get('key_indicators', [])
        }
        return metrics
    
    @staticmethod
    def format_report_data(research_data: Dict, analysis_data: Dict, trends_data: List) -> str:
        """Format data for final report generation"""
        report = {
            'company_overview': research_data.get('overview', ''),
            'market_analysis': analysis_data,
            'trends': trends_data,
            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return str(report)