from crewai import Agent

class ReportWriterAgent:
    def create(self):
        return Agent(
            role='Report Writer',
            goal='Create comprehensive and well-structured market research reports',
            backstory='''
                You are a skilled business writer with expertise in creating clear, 
                concise, and insightful market research reports. You excel at 
                presenting complex information in an easily digestible format.
            ''',
            tools=[],  # Report writer primarily uses language abilities
            verbose=True,
            allow_delegation=False
        )