from agents.base_agent import BaseAgent

class ReportWriterAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def create(self):
        return self.create_agent(
            role='Report Writer',
            goal='Create comprehensive and well-structured market research reports',
            backstory='''
                You are a skilled business writer with expertise in creating clear, 
                concise, and insightful market research reports. You excel at 
                presenting complex information in an easily digestible format.
            ''',
            tools=[]
        )