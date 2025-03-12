import os
from typing import Dict, Any, Iterator
from llama_cpp import Llama
from config import MODEL_CONFIG, GENERATION_CONFIG, SEARCH_CONFIG
from search_utils import WebSearch
from cache import SearchCache

class ModelHandler:
    def __init__(self):
        self.model = None
        self.search = WebSearch()
        self.cache = SearchCache(SEARCH_CONFIG['cache_size'], SEARCH_CONFIG['cache_ttl'])
        self._initialize_model()

    def _initialize_model(self):
        try:
            self.model = Llama(**MODEL_CONFIG)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize model: {str(e)}")

    def generate_response(self, prompt: str) -> Iterator[str]:
        search_results = ""
        if SEARCH_CONFIG['enabled']:
            # Try cache first
            results = self.cache.get(prompt)
            if not results:
                results = self.search.search(prompt, SEARCH_CONFIG['results_count'])
                self.cache.set(prompt, results)
            search_results = self.search.extract_relevant_info(results)
        
        formatted_prompt = f"[INST] {search_results}\n\n{prompt} [/INST]"
        
        response = self.model(
            formatted_prompt,
            **GENERATION_CONFIG
        )
        
        for chunk in response:
            if chunk and 'choices' in chunk and chunk['choices']:
                yield chunk['choices'][0]['text']
