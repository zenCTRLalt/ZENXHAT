"""
Search Aggregator Module
"""

import requests
from zenxhat.core.logger import setup_logger
from zenxhat.core.config import config

logger = setup_logger(__name__)


class SearchAggregator:
    """Aggregate search results from multiple sources"""

    def __init__(self):
        self.logger = logger
        self.timeout = config.REQUEST_TIMEOUT

    def duckduckgo_search(self, query: str, max_results: int = 10) -> list:
        """Search using DuckDuckGo (privacy-friendly)"""
        try:
            self.logger.info(f"Searching DuckDuckGo for: {query}")
            url = "https://html.duckduckgo.com"
            params = {"q": query}
            headers = {"User-Agent": "ZENXHAT-OSINT"}

            response = requests.get(
                url, params=params, headers=headers, timeout=self.timeout
            )
            response.raise_for_status()

            # Basic parsing (would need BeautifulSoup for production)
            results = [{"query": query, "source": "DuckDuckGo", "status": "partial"}]
            return results

        except Exception as e:
            self.logger.warning(f"DuckDuckGo search failed: {str(e)}")
            return []

    def aggregate_search(self, query: str, sources: list = None) -> dict:
        """Aggregate search results from multiple sources"""
        if sources is None:
            sources = ["duckduckgo"]

        self.logger.info(f"Aggregating search results for: {query}")
        all_results = {"query": query, "sources": {}, "total_results": 0}

        if "duckduckgo" in sources or "google" in sources:
            all_results["sources"]["duckduckgo"] = self.duckduckgo_search(query)

        return all_results
