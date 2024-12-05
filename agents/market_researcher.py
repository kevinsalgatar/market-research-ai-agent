from agents.base_agent import BaseAgent
from tools.search_tools import SearchTools
from tools.web_scraping_tools import WebScrapingTools

class MarketResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.search_tools = SearchTools()
        self.web_tools = WebScrapingTools()

    def create(self):
        return self.create_agent(
            role='Market Research Specialist',
            goal='Conduct comprehensive market research and gather detailed information about companies, products, and industry trends',
            backstory='''
                You are an experienced market research specialist with expertise in 
                gathering and analyzing market intelligence. You have a strong background 
                in competitive analysis and industry trend identification.
            ''',
            tools=[
                self.search_tools.web_search,
                self.web_tools.scrape_website
            ]
        )