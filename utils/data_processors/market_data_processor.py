import pandas as pd
import numpy as np
from typing import Dict, List, Any

class MarketDataProcessor:
    @staticmethod
    def calculate_market_metrics(data: Dict[str, Any]) -> Dict[str, float]:
        """Calculate key market metrics from raw data"""
        metrics = {
            'market_size': data.get('market_size', 0),
            'growth_rate': data.get('growth_rate', 0),
            'market_penetration': data.get('market_penetration', 0),
            'customer_acquisition_cost': data.get('customer_acquisition_cost', 0),
            'lifetime_value': data.get('lifetime_value', 0)
        }
        
        # Calculate additional metrics
        if metrics['market_size'] and metrics['market_penetration']:
            metrics['addressable_market'] = metrics['market_size'] * (metrics['market_penetration'] / 100)
        
        if metrics['customer_acquisition_cost'] and metrics['lifetime_value']:
            metrics['ltv_cac_ratio'] = metrics['lifetime_value'] / metrics['customer_acquisition_cost']
        
        return metrics
    
    @staticmethod
    def segment_analysis(data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze market segments"""
        segments = data.get('segments', {})
        analysis = {
            'total_segments': len(segments),
            'segment_sizes': {},
            'segment_growth_rates': {},
            'major_segments': []
        }
        
        for segment, info in segments.items():
            analysis['segment_sizes'][segment] = info.get('size', 0)
            analysis['segment_growth_rates'][segment] = info.get('growth_rate', 0)
            
            # Identify major segments (>10% of total market)
            if info.get('size', 0) / data.get('market_size', 1) > 0.1:
                analysis['major_segments'].append(segment)
        
        return analysis
    
    @staticmethod
    def competitive_analysis(data: Dict[str, Any]) -> pd.DataFrame:
        """Analyze competitive landscape"""
        competitors = data.get('competitors', {})
        
        # Create comparison matrix
        metrics = [
            'market_share',
            'revenue',
            'growth_rate',
            'product_score',
            'customer_satisfaction'
        ]
        
        df = pd.DataFrame(index=competitors.keys(), columns=metrics)
        
        for competitor, info in competitors.items():
            for metric in metrics:
                df.loc[competitor, metric] = info.get(metric, np.nan)
        
        return df