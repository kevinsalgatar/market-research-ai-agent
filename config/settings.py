import os
from typing import Dict, Any

class Settings:
    # API Configuration
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    BRAVE_API_KEY = os.getenv('BRAVE_API_KEY')
    BROWSERLESS_API_KEY = os.getenv('BROWSERLESS_API_KEY')
    
    # Agent Configuration
    AGENT_CONFIG = {
        'market_researcher': {
            'model': 'claude-3-opus-20240229',
            'temperature': 0.7,
            'max_iterations': 3
        },
        'data_analyst': {
            'model': 'claude-3-opus-20240229',
            'temperature': 0.3,
            'max_iterations': 2
        },
        'report_writer': {
            'model': 'claude-3-opus-20240229',
            'temperature': 0.5,
            'max_iterations': 1
        }
    }
