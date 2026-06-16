"""
IP Geolocation Module
"""

import requests
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validate_ip
from zenxhat.core.config import config

logger = setup_logger(__name__)


class IPGeolocation:
    """IP address geolocation and information lookup"""

    def __init__(self):
        self.logger = logger
        self.timeout = config.REQUEST_TIMEOUT
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def geoip_lookup(self, ip: str) -> dict:
        """Get geolocation information for IP using ip-api.com (free tier)"""
        if not validate_ip(ip):
            self.logger.error(f"Invalid IP: {ip}")
            return {"error": "Invalid IP format"}

        try:
            self.logger.info(f"Looking up geolocation for {ip}")
            url = f"http://ip-api.com/json/{ip}?fields=status,query,country,countryCode,city,region,regionName,timezone,isp,org,as,asname"

            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            if data["status"] == "success":
                return {
                    "ip": data.get("query"),
                    "country": data.get("country"),
                    "country_code": data.get("countryCode"),
                    "city": data.get("city"),
                    "region": data.get("region"),
                    "region_name": data.get("regionName"),
                    "timezone": data.get("timezone"),
                    "isp": data.get("isp"),
                    "organization": data.get("org"),
                    "asn": data.get("as"),
                    "asn_name": data.get("asname"),
                }
            else:
                self.logger.warning(f"Geolocation lookup failed for {ip}")
                return {"error": "Lookup failed"}

        except Exception as e:
            self.logger.error(f"IP geolocation error: {str(e)}")
            return {"error": str(e)}

    def get_asn_info(self, ip: str) -> dict:
        """Get ASN information"""
        geo_data = self.geoip_lookup(ip)
        return {
            "ip": ip,
            "asn": geo_data.get("asn"),
            "asn_name": geo_data.get("asn_name"),
            "organization": geo_data.get("organization"),
            "isp": geo_data.get("isp"),
        }

    def get_location(self, ip: str) -> dict:
        """Get location information only"""
        geo_data = self.geoip_lookup(ip)
        return {
            "ip": ip,
            "country": geo_data.get("country"),
            "city": geo_data.get("city"),
            "timezone": geo_data.get("timezone"),
            "coordinates": {
                "country_code": geo_data.get("country_code"),
                "region": geo_data.get("region"),
            },
        }
