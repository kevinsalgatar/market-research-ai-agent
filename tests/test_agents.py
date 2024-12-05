import unittest
from unittest.mock import Mock, patch
from agents.market_researcher import MarketResearcherAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_writer import ReportWriterAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.market_researcher = MarketResearcherAgent()
        self.data_analyst = DataAnalystAgent()
        self.report_writer = ReportWriterAgent()

    def test_market_researcher_creation(self):
        agent = self.market_researcher.create()
        self.assertEqual(agent.role, 'Market Research Specialist')
        self.assertTrue(len(agent.tools) >= 2)

    def test_data_analyst_creation(self):
        agent = self.data_analyst.create()
        self.assertEqual(agent.role, 'Data Analyst')
        self.assertTrue(len(agent.tools) >= 2)

    def test_report_writer_creation(self):
        agent = self.report_writer.create()
        self.assertEqual(agent.role, 'Report Writer')
        # Report writer doesn't need tools as it uses language abilities
        self.assertEqual(len(agent.tools), 0)