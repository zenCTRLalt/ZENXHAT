"""
Email OSINT Module
"""

import requests
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validate_email
from zenxhat.core.config import config

logger = setup_logger(__name__)


class EmailOSINT:
    """Email-based Open Source Intelligence"""

    def __init__(self):
        self.logger = logger
        self.timeout = config.REQUEST_TIMEOUT

    def check_breach(self, email: str) -> dict:
        """Check if email appeared in known breaches (using Have I Been Pwned)"""
        if not validate_email(email):
            self.logger.error(f"Invalid email: {email}")
            return {"error": "Invalid email format"}

        try:
            self.logger.info(f"Checking if {email} has been breached")
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {"User-Agent": "ZENXHAT-OSINT"}

            response = requests.get(
                url, headers=headers, timeout=self.timeout, verify=False
            )

            if response.status_code == 200:
                breaches = response.json()
                return {"email": email, "breached": True, "breach_count": len(breaches)}
            elif response.status_code == 404:
                return {"email": email, "breached": False, "breach_count": 0}
            else:
                return {"email": email, "status": "unknown"}

        except Exception as e:
            self.logger.warning(f"Breach check failed: {str(e)}")
            return {"email": email, "error": str(e)}

    def verify_email_format(self, email: str) -> bool:
        """Verify email format is valid"""
        return validate_email(email)

    def extract_domain(self, email: str) -> str:
        """Extract domain from email"""
        if "@" in email:
            return email.split("@")[1]
        return None
