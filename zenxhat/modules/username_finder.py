"""
Username OSINT Module
"""

import requests
from zenxhat.core.logger import setup_logger
from zenxhat.core.config import config

logger = setup_logger(__name__)


class UsernameFinder:
    """Find usernames across multiple platforms"""

    def __init__(self):
        self.logger = logger
        self.timeout = config.REQUEST_TIMEOUT
        self.platforms = {
            "GitHub": "https://github.com/{username}",
            "Twitter": "https://twitter.com/{username}",
            "LinkedIn": "https://linkedin.com/in/{username}",
            "Instagram": "https://instagram.com/{username}",
            "Facebook": "https://facebook.com/{username}",
            "Reddit": "https://reddit.com/u/{username}",
            "Twitch": "https://twitch.tv/{username}",
            "YouTube": "https://youtube.com/@{username}",
        }

    def search_username(self, username: str) -> dict:
        """Search username across platforms"""
        self.logger.info(f"Searching for username: {username}")
        results = {"username": username, "found_on": []}

        for platform, url in self.platforms.items():
            full_url = url.format(username=username)
            try:
                response = requests.head(
                    full_url, timeout=self.timeout, allow_redirects=True
                )
                if response.status_code == 200:
                    results["found_on"].append(
                        {"platform": platform, "url": full_url, "status": "found"}
                    )
                    self.logger.info(f"Found {username} on {platform}")
            except Exception as e:
                self.logger.debug(f"Error checking {platform}: {str(e)}")
                results["found_on"].append(
                    {"platform": platform, "url": full_url, "status": "unknown"}
                )

        return results
