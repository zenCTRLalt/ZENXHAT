"""
Configuration manager for ZENXHAT
"""

import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """Global configuration loader"""

    def __init__(self):
        # Load .env file
        env_path = Path(__file__).parent.parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        # API Keys
        self.SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "")
        self.CENSYS_API_ID = os.getenv("CENSYS_API_ID", "")
        self.CENSYS_API_SECRET = os.getenv("CENSYS_API_SECRET", "")
        self.VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "")
        self.HUNTER_API_KEY = os.getenv("HUNTER_API_KEY", "")
        self.ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "")
        self.EMAILREP_API_KEY = os.getenv("EMAILREP_API_KEY", "")

        # Settings
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.RATE_LIMIT = float(os.getenv("RATE_LIMIT", "2"))
        self.REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))

        # Directories
        self.BASE_DIR = Path(__file__).parent.parent.parent
        self.OUTPUT_DIR = self.BASE_DIR / "output"
        self.OUTPUT_DIR.mkdir(exist_ok=True)

    def has_api_key(self, api_name: str) -> bool:
        """Check if API key is configured"""
        key_attr = f"{api_name.upper()}_API_KEY"
        return bool(getattr(self, key_attr, ""))


# Global config instance
config = Config()
