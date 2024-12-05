from crewai import Agent
from anthropic import Anthropic
from typing import List
from config.settings import Settings

class BaseAgent:
    def __init__(self):
        self.settings = Settings()
        self.anthropic = Anthropic(api_key=self.settings.ANTHROPIC_API_KEY)
    
    def create_agent(self, role: str, goal: str, backstory: str, tools: List = None) -> Agent:
        """Create a CrewAI agent with Anthropic's Claude"""
        config = self.settings.AGENT_CONFIG.get(role.lower().replace(' ', '_'), {})
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            tools=tools or [],
            llm_config={
                'model': config.get('model', 'claude-3-opus-20240229'),
                'temperature': config.get('temperature', 0.7),
                'anthropic_api_key': self.settings.ANTHROPIC_API_KEY
            },
            verbose=True
        )