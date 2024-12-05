import os
from typing import Dict, Any

class Settings:
    # API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    SERP_API_KEY = os.getenv('SERP_API_KEY')
    BROWSERLESS_API_KEY = os.getenv('BROWSERLESS_API_KEY')
    
    # Agent Configuration
    AGENT_CONFIG = {
        'market_researcher': {
            'model': 'gpt-4',
            'temperature': 0.7,
            'max_iterations': 3
        },
        'data_analyst': {
            'model': 'gpt-4',
            'temperature': 0.3,
            'max_iterations': 2
        },
        'report_writer': {
            'model': 'gpt-4',
            'temperature': 0.5,
            'max_iterations': 1
        }
    }
    
    # Task Configuration
    TASK_CONFIG = {
        'research': {
            'max_results': 5,
            'search_depth': 2
        },
        'analysis': {
            'min_confidence': 0.8,
            'data_points': 100
        }
    }
    
    @classmethod
    def get_agent_config(cls, agent_type: str) -> Dict[str, Any]:
        return cls.AGENT_CONFIG.get(agent_type, {})
    
    @classmethod
    def get_task_config(cls, task_type: str) -> Dict[str, Any]:
        return cls.TASK_CONFIG.get(task_type, {})