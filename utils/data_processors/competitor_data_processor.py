import pandas as pd
import numpy as np
from typing import Dict, List, Any

class CompetitorDataProcessor:
    @staticmethod
    def create_comparison_matrix(competitors: Dict[str, Any], metrics: List[str]) -> pd.DataFrame:
        """Create a comparison matrix for competitors"""
        df = pd.DataFrame(index=competitors.keys(), columns=metrics)
        
        for competitor, data in competitors.items():
            for metric in metrics:
                df.loc[competitor, metric] = data.get(metric, np.nan)
        
        return df
    
    @staticmethod
    def calculate_relative_strengths(comparison_matrix: pd.DataFrame) -> Dict[str, List[str]]:
        """Calculate relative strengths and weaknesses of competitors"""
        analysis = {}
        
        for competitor in comparison_matrix.index:
            strengths = []
            weaknesses = []
            
            for metric in comparison_matrix.columns:
                value = comparison_matrix.loc[competitor, metric]
                avg = comparison_matrix[metric].mean()
                
                if value > avg * 1.1:  # 10% above average
                    strengths.append(metric)
                elif value < avg * 0.9:  # 10% below average
                    weaknesses.append(metric)
            
            analysis[competitor] = {
                'strengths': strengths,
                'weaknesses': weaknesses
            }
        
        return analysis