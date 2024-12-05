from langchain.tools import Tool
import requests
from bs4 import BeautifulSoup

class WebScrapingTools:
    def scrape_website(self, url: str) -> str:
        """Scrape content from a given URL"""
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            return text[:8000]  # Limit text length
        except Exception as e:
            return f"Error scraping website: {str(e)}"

    def get_tools(self):
        return [
            Tool.from_function(
                func=self.scrape_website,
                name="Web Scraper",
                description="Scrape content from a specific URL"
            )
        ]