"""
WHOIS Lookup Module
"""

import whois
from datetime import datetime
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validate_domain

logger = setup_logger(__name__)


class WhoisLookup:
    """WHOIS information retriever"""

    def __init__(self):
        self.logger = logger

    def lookup(self, domain: str) -> dict:
        """Retrieve WHOIS information for a domain"""
        if not validate_domain(domain):
            self.logger.error(f"Invalid domain format: {domain}")
            return {"error": "Invalid domain format"}

        try:
            self.logger.info(f"Looking up WHOIS information for {domain}")
            whois_data = whois.whois(domain)

            result = {
                "domain": domain,
                "registrar": whois_data.registrar,
                "creation_date": str(whois_data.creation_date),
                "expiration_date": str(whois_data.expiration_date),
                "updated_date": str(whois_data.updated_date),
                "nameservers": whois_data.nameservers if whois_data.nameservers else [],
                "status": whois_data.status if whois_data.status else [],
                "emails": whois_data.emails if whois_data.emails else [],
            }

            # Add optional fields
            if hasattr(whois_data, "registrant_name"):
                result["registrant_name"] = whois_data.registrant_name
            if hasattr(whois_data, "registrant_country"):
                result["registrant_country"] = whois_data.registrant_country
            if hasattr(whois_data, "admin_name"):
                result["admin_name"] = whois_data.admin_name

            self.logger.info(f"WHOIS lookup completed for {domain}")
            return result

        except Exception as e:
            self.logger.error(f"WHOIS lookup failed: {str(e)}")
            return {"error": str(e)}

    def is_expired(self, domain: str) -> bool:
        """Check if domain is expired"""
        try:
            whois_data = whois.whois(domain)
            expiration = whois_data.expiration_date
            if isinstance(expiration, list):
                expiration = expiration[0]
            return expiration < datetime.now()
        except Exception as e:
            self.logger.error(f"Error checking expiration: {str(e)}")
            return None

    def get_registrar(self, domain: str) -> str:
        """Get domain registrar"""
        try:
            whois_data = whois.whois(domain)
            return whois_data.registrar
        except Exception as e:
            self.logger.error(f"Error getting registrar: {str(e)}")
            return None
