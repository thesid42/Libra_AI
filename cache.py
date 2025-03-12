from typing import Dict, Any
import time
from functools import lru_cache

class SearchCache:
    def __init__(self, size: int = 100, ttl: int = 3600):
        self.ttl = ttl
        self._get_results = lru_cache(maxsize=size)(self._fetch_results)
        self.timestamps: Dict[str, float] = {}

    def _fetch_results(self, query: str) -> list:
        self.timestamps[query] = time.time()
        return []  # Will be populated by actual results

    def get(self, query: str) -> list:
        if query in self.timestamps:
            if time.time() - self.timestamps[query] > self.ttl:
                self._get_results.cache_clear()
                return []
        return self._get_results(query)

    def set(self, query: str, results: list) -> None:
        self._get_results.__wrapped__.__defaults__ = (results,)
        self._get_results(query)
