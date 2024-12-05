import pandas as pd
import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta

class TrendDataProcessor:
    @staticmethod
    def analyze_trends(data: List[Dict[str, Any]], timeframe: str) -> Dict[str, Any]:
        """Analyze trends over a given timeframe"""
        # Convert timeframe to datetime
        end_date = datetime.now()
        if timeframe.endswith('months'):
            start_date = end_date - timedelta(days=30 * int(timeframe.split('months')[0]))
        elif timeframe.endswith('years'):
            start_date = end_date - timedelta(days=365 * int(timeframe.split('years')[0]))
        else:
            start_date = end_date - timedelta(days=90)  # Default to 3 months
        
        # Filter data by timeframe
        filtered_data = [
            d for d in data 
            if datetime.fromisoformat(d['date']) between start_date and end_date
        ]
        
        # Analyze trends
        analysis = {
            'trends': [],
            'metrics': {},
            'patterns': [],
            'anomalies': []
        }
        
        # Process trends
        for item in filtered_data:
            # Add trend if confidence is high enough
            if item.get('confidence', 0) > 0.7:
                analysis['trends'].append({
                    'name': item['name'],
                    'strength': item['strength'],
                    'impact': item['impact'],
                    'category': item['category']
                })
        
        # Calculate metrics
        if filtered_data:
            df = pd.DataFrame(filtered_data)
            analysis['metrics'] = {
                'total_trends': len(analysis['trends']),
                'avg_confidence': df['confidence'].mean(),
                'top_categories': df['category'].value_counts().to_dict()
            }
        
        # Identify patterns
        if len(filtered_data) > 1:
            analysis['patterns'] = TrendDataProcessor._identify_patterns(filtered_data)
        
        # Detect anomalies
        if len(filtered_data) > 2:
            analysis['anomalies'] = TrendDataProcessor._detect_anomalies(filtered_data)
        
        return analysis
    
    @staticmethod
    def _identify_patterns(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify patterns in trend data"""
        patterns = []
        
        # Convert to DataFrame for easier analysis
        df = pd.DataFrame(data)
        
        # Look for recurring trends
        if 'category' in df.columns:
            category_counts = df['category'].value_counts()
            recurring_categories = category_counts[category_counts > 1].index
            
            for category in recurring_categories:
                patterns.append({
                    'type': 'recurring_category',
                    'category': category,
                    'frequency': int(category_counts[category]),
                    'description': f"Recurring trend in category: {category}"
                })
        
        # Look for strength patterns
        if 'strength' in df.columns:
            strength_trend = np.polyfit(range(len(df)), df['strength'], 1)[0]
            if abs(strength_trend) > 0.1:
                patterns.append({
                    'type': 'strength_trend',
                    'direction': 'increasing' if strength_trend > 0 else 'decreasing',
                    'magnitude': abs(strength_trend),
                    'description': f"{'Increasing' if strength_trend > 0 else 'Decreasing'} trend strength"
                })
        
        return patterns
    
    @staticmethod
    def _detect_anomalies(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect anomalies in trend data"""
        anomalies = []
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Simple anomaly detection using z-score
        if 'strength' in df.columns:
            mean_strength = df['strength'].mean()
            std_strength = df['strength'].std()
            
            for idx, row in df.iterrows():
                z_score = (row['strength'] - mean_strength) / std_strength
                if abs(z_score) > 2:  # More than 2 standard deviations
                    anomalies.append({
                        'date': row['date'],
                        'type': 'strength_anomaly',
                        'value': row['strength'],
                        'z_score': z_score,
                        'description': f"Unusual trend strength detected"
                    })
        
        return anomalies