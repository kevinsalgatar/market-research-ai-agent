from crewai import Agent
from tools.analysis_tools import AnalysisTools

class DataAnalystAgent:
    def __init__(self):
        self.analysis_tools = AnalysisTools()

    def create(self):
        return Agent(
            role='Data Analyst',
            goal='Analyze market data and identify key trends, patterns, and insights',
            backstory='''
                You are a data analyst with expertise in market analysis and 
                statistical modeling. You excel at transforming raw data into 
                actionable insights and clear visualizations.
            ''',
            tools=[
                self.analysis_tools.analyze_data,
                self.analysis_tools.create_visualization
            ],
            verbose=True,
            allow_delegation=False
        )