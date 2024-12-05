import unittest
from unittest.mock import Mock
from tasks.market_research_tasks import MarketResearchTasks

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.research_agent = Mock()
        self.analyst_agent = Mock()
        self.writer_agent = Mock()
        self.tasks = MarketResearchTasks(
            self.research_agent,
            self.analyst_agent,
            self.writer_agent
        )

    def test_research_company_task(self):
        task = self.tasks.research_company('Test Company')
        self.assertEqual(task.agent, self.research_agent)
        self.assertIn('Test Company', task.description)

    def test_analyze_market_data_task(self):
        task = self.tasks.analyze_market_data('Tech')
        self.assertEqual(task.agent, self.analyst_agent)
        self.assertIn('Tech', task.description)

    def test_create_report_task(self):
        task = self.tasks.create_report('research', 'analysis', 'trends')
        self.assertEqual(task.agent, self.writer_agent)
        self.assertIn('research', task.description)