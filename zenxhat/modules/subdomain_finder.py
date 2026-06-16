"""
Passive Subdomain Discovery Module
"""

import requests
from bs4 import BeautifulSoup
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validate_domain
from zenxhat.core.config import config

logger = setup_logger(__name__)


class SubdomainFinder:
    """Passive subdomain discovery using public sources"""

    def __init__(self):
        self.logger = logger
        self.timeout = config.REQUEST_TIMEOUT
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        self.subdomains = set()

    def crt_sh_lookup(self, domain: str) -> list:
        """Get subdomains from crt.sh (Certificate Transparency)"""
        if not validate_domain(domain):
            return []

        try:
            self.logger.info(f"Fetching subdomains from crt.sh for {domain}")
            url = f"https://crt.sh/?q=%25.{domain}&output=json"

            response = requests.get(
                url, headers=self.headers, timeout=self.timeout, verify=False
            )
            response.raise_for_status()

            results = response.json()
            subdomains = set()

            for result in results:
                name_value = result["name_value"]
                for name in name_value.split("\n"):
                    name = name.strip()
                    if name and name not in subdomains:
                        subdomains.add(name)

            self.logger.info(f"Found {len(subdomains)} subdomains from crt.sh")
            return list(subdomains)

        except Exception as e:
            self.logger.error(f"crt.sh lookup failed: {str(e)}")
            return []

    def hackertarget_lookup(self, domain: str) -> list:
        """Get subdomains from HackerTarget"""
        if not validate_domain(domain):
            return []

        try:
            self.logger.info(f"Fetching subdomains from HackerTarget for {domain}")
            url = f"https://api.hackertarget.com/hostsearch/?q={domain}"

            response = requests.get(
                url, headers=self.headers, timeout=self.timeout, verify=False
            )
            response.raise_for_status()

            subdomains = set()
            for line in response.text.split("\n"):
                if "," in line:
                    subdomain = line.split(",")[0].strip()
                    if subdomain:
                        subdomains.add(subdomain)

            self.logger.info(f"Found {len(subdomains)} subdomains from HackerTarget")
            return list(subdomains)

        except Exception as e:
            self.logger.warning(f"HackerTarget lookup failed: {str(e)}")
            return []

    def find_subdomains(self, domain: str) -> list:
        """Find subdomains from multiple sources"""
        self.logger.info(f"Starting subdomain enumeration for {domain}")

        self.subdomains.update(self.crt_sh_lookup(domain))
        self.subdomains.update(self.hackertarget_lookup(domain))

        # Remove wildcard subdomains and sort
        subdomains = sorted([s for s in self.subdomains if "*" not in s])

        self.logger.info(f"Total unique subdomains found: {len(subdomains)}")
        return subdomains

    def get_results(self) -> dict:
        """Get enumeration results"""
        return {"subdomains": sorted(list(self.subdomains)), "count": len(self.subdomains)}
