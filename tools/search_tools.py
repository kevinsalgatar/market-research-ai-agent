from langchain.tools import Tool
from duckduckgo_search import DDGS

class SearchTools:
    def web_search(self, query: str) -> str:
        """Search the web for information about a company or market"""
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=5)]
            return '\n'.join([f"Title: {r['title']}\nLink: {r['link']}\nSnippet: {r['body']}\n" for r in results])

    def get_tools(self):
        return [
            Tool.from_function(
                func=self.web_search,
                name="Web Search",
                description="Search the web for market research information"
            )
        ]