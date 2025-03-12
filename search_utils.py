import requests
from typing import List, Dict
from bs4 import BeautifulSoup
import time
import re

class WebSearch:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or ""  # Add your Google/Bing API key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def search(self, query: str, num_results: int = 3) -> List[Dict[str, str]]:
        """Perform web search and return relevant snippets"""
        try:
            # Basic DuckDuckGo-style search (can be replaced with Google/Bing API)
            url = f"https://html.duckduckgo.com/html/?q={query}"
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = []
            for result in soup.select('.result')[:num_results]:
                title = result.select_one('.result__title')
                snippet = result.select_one('.result__snippet')
                if title and snippet:
                    results.append({
                        'title': title.get_text().strip(),
                        'snippet': snippet.get_text().strip()
                    })
            
            time.sleep(1)  # Be nice to the search engine
            return results
        except Exception as e:
            print(f"Search error: {str(e)}")
            return []

    def extract_relevant_info(self, results: List[Dict[str, str]]) -> str:
        """Format search results for the model"""
        if not results:
            return ""
        
        context = "Here's some relevant information:\n\n"
        for idx, result in enumerate(results, 1):
            context += f"{idx}. {result['title']}\n{result['snippet']}\n\n"
        return context
