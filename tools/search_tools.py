from langchain.tools import Tool
from typing import List, Dict, Any
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class SearchTools:
    def __init__(self):
        self.brave_api_key = os.getenv('BRAVE_API_KEY')
        self.api_endpoint = 'https://api.search.brave.com/res/v1/web/search'
        
    def web_search(self, query: str) -> str:
        """Search the web for information about a company or market"""
        try:
            headers = {
                'Accept': 'application/json',
                'X-Subscription-Token': self.brave_api_key
            }
            
            params = {
                'q': query,
                'count': 10  # Number of results
            }
            
            response = requests.get(
                self.api_endpoint,
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                results = response.json().get('web', {}).get('results', [])
                formatted_results = []
                
                for result in results:
                    formatted_results.append(
                        f"Title: {result.get('title', '')}"
                        f"\nLink: {result.get('url', '')}"
                        f"\nDescription: {result.get('description', '')}\n"
                    )
                
                return '\n\n'.join(formatted_results)
            else:
                return f"Error searching: Status code {response.status_code}"
                
        except Exception as e:
            return f"Error performing search: {str(e)}"
    
    def local_search(self, query: str) -> str:
        """Search for local business information"""
        try:
            headers = {
                'Accept': 'application/json',
                'X-Subscription-Token': self.brave_api_key
            }
            
            params = {
                'q': query + ' near me',  # Add local context
                'count': 5,
                'type': 'places'  # Focus on local places
            }
            
            response = requests.get(
                self.api_endpoint,
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                results = response.json().get('places', [])
                formatted_results = []
                
                for result in results:
                    formatted_results.append(
                        f"Business: {result.get('name', '')}"
                        f"\nAddress: {result.get('address', '')}"
                        f"\nRating: {result.get('rating', 'N/A')}"
                        f"\nWebsite: {result.get('website', 'N/A')}\n"
                    )
                
                return '\n\n'.join(formatted_results)
            else:
                return f"Error searching: Status code {response.status_code}"
                
        except Exception as e:
            return f"Error performing local search: {str(e)}"
    
    def news_search(self, query: str) -> str:
        """Search for news articles"""
        try:
            headers = {
                'Accept': 'application/json',
                'X-Subscription-Token': self.brave_api_key
            }
            
            params = {
                'q': query,
                'count': 5,
                'type': 'news'  # Focus on news articles
            }
            
            response = requests.get(
                self.api_endpoint,
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                results = response.json().get('news', [])
                formatted_results = []
                
                for result in results:
                    formatted_results.append(
                        f"Title: {result.get('title', '')}"
                        f"\nSource: {result.get('source', '')}"
                        f"\nPublished: {result.get('published', '')}"
                        f"\nLink: {result.get('url', '')}"
                        f"\nSummary: {result.get('description', '')}\n"
                    )
                
                return '\n\n'.join(formatted_results)
            else:
                return f"Error searching: Status code {response.status_code}"
                
        except Exception as e:
            return f"Error performing news search: {str(e)}"
    
    def get_tools(self) -> List[Tool]:
        """Return list of available tools"""
        return [
            Tool.from_function(
                func=self.web_search,
                name="Web Search",
                description="Search the web for market research information"
            ),
            Tool.from_function(
                func=self.local_search,
                name="Local Search",
                description="Search for local business information"
            ),
            Tool.from_function(
                func=self.news_search,
                name="News Search",
                description="Search for news articles"
            )
        ]