import unittest
from unittest.mock import Mock, patch
from tools.search_tools import SearchTools
from tools.web_scraping_tools import WebScrapingTools
from tools.analysis_tools import AnalysisTools

class TestTools(unittest.TestCase):
    def setUp(self):
        self.search_tools = SearchTools()
        self.web_tools = WebScrapingTools()
        self.analysis_tools = AnalysisTools()

    @patch('tools.search_tools.DDGS')
    def test_web_search(self, mock_ddgs):
        mock_results = [
            {'title': 'Test', 'link': 'http://test.com', 'body': 'Test content'}
        ]
        mock_ddgs.return_value.__enter__.return_value.text.return_value = mock_results
        
        result = self.search_tools.web_search('test query')
        self.assertIn('Test content', result)

    @patch('tools.web_scraping_tools.requests')
    def test_web_scraper(self, mock_requests):
        mock_requests.get.return_value.text = '<html><body>Test content</body></html>'
        
        result = self.web_tools.scrape_website('http://test.com')
        self.assertIn('Test content', result)

    def test_data_analysis(self):
        test_data = "[{'metric': 'value', 'count': 10}]"
        result = self.analysis_tools.analyze_data(test_data)
        self.assertIsInstance(result, str)