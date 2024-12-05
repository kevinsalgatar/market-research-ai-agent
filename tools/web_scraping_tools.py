from langchain.tools import Tool
import requests
from bs4 import BeautifulSoup
from typing import Optional
import time

class WebScrapingTools:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def scrape_website(self, url: str) -> str:
        """Scrape content from a given URL using requests and BeautifulSoup"""
        try:
            # Add delay to be respectful to websites
            time.sleep(2)
            
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for element in soup.find_all(['script', 'style', 'nav', 'footer']):
                element.decompose()
            
            # Extract main content
            main_content = ""
            
            # Try to find main content container
            main = soup.find('main') or soup.find('article') or soup.find('div', {'class': ['content', 'main', 'article']})
            if main:
                main_content = main.get_text(separator='\n', strip=True)
            else:
                # Fallback to body content
                main_content = soup.body.get_text(separator='\n', strip=True) if soup.body else soup.get_text(separator='\n', strip=True)
            
            # Clean up the text
            lines = [line.strip() for line in main_content.splitlines() if line.strip()]
            cleaned_text = '\n'.join(lines)
            
            # Limit text length
            return cleaned_text[:8000] if len(cleaned_text) > 8000 else cleaned_text
            
        except requests.RequestException as e:
            return f"Error accessing website: {str(e)}"
        except Exception as e:
            return f"Error scraping website: {str(e)}"
    
    def extract_specific_data(self, url: str, data_type: str) -> str:
        """Extract specific types of data from a webpage"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            result = ""
            
            if data_type == 'contact':
                # Look for contact information
                emails = [a.get('href') for a in soup.find_all('a', href=True) if 'mailto:' in a.get('href', '')]
                phones = [a.get('href') for a in soup.find_all('a', href=True) if 'tel:' in a.get('href', '')]
                result = f"Emails: {', '.join(emails)}\nPhones: {', '.join(phones)}"
                
            elif data_type == 'social':
                # Look for social media links
                social_links = []
                social_domains = ['linkedin.com', 'twitter.com', 'facebook.com', 'instagram.com']
                for a in soup.find_all('a', href=True):
                    if any(domain in a.get('href', '').lower() for domain in social_domains):
                        social_links.append(a.get('href'))
                result = f"Social Links: {', '.join(social_links)}"
                
            elif data_type == 'prices':
                # Look for price information
                prices = soup.find_all(['span', 'div', 'p'], text=lambda t: t and ('$' in t or '€' in t or '£' in t))
                result = f"Prices found: {', '.join(p.text.strip() for p in prices)}"
            
            return result if result else f"No {data_type} information found"
            
        except Exception as e:
            return f"Error extracting {data_type} data: {str(e)}"
    
    def get_tools(self) -> list:
        """Return list of available tools"""
        return [
            Tool.from_function(
                func=self.scrape_website,
                name="Web Scraper",
                description="Scrape content from a specific URL"
            ),
            Tool.from_function(
                func=self.extract_specific_data,
                name="Data Extractor",
                description="Extract specific types of data (contact, social, prices) from a webpage"
            )
        ]