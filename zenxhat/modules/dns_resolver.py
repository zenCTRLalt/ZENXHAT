"""
DNS Resolution Module
"""

import dns.resolver
import dns.reversename
import dns.zone
import dns.query
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validate_domain, validate_ip

logger = setup_logger(__name__)


class DNSResolver:
    """DNS information resolver"""

    def __init__(self):
        self.logger = logger
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = 5
        self.resolver.lifetime = 10

    def resolve_a_record(self, domain: str) -> list:
        """Resolve A records (IPv4)"""
        if not validate_domain(domain):
            self.logger.error(f"Invalid domain: {domain}")
            return []

        try:
            answers = self.resolver.resolve(domain, "A")
            return [str(rdata) for rdata in answers]
        except Exception as e:
            self.logger.warning(f"A record lookup failed for {domain}: {str(e)}")
            return []

    def resolve_aaaa_record(self, domain: str) -> list:
        """Resolve AAAA records (IPv6)"""
        if not validate_domain(domain):
            return []

        try:
            answers = self.resolver.resolve(domain, "AAAA")
            return [str(rdata) for rdata in answers]
        except Exception as e:
            self.logger.warning(f"AAAA record lookup failed: {str(e)}")
            return []

    def resolve_mx_record(self, domain: str) -> list:
        """Resolve MX records (Mail exchange)"""
        if not validate_domain(domain):
            return []

        try:
            answers = self.resolver.resolve(domain, "MX")
            mx_records = []
            for rdata in answers:
                mx_records.append(
                    {"priority": rdata.preference, "mail_server": str(rdata.exchange)}
                )
            return sorted(mx_records, key=lambda x: x["priority"])
        except Exception as e:
            self.logger.warning(f"MX record lookup failed: {str(e)}")
            return []

    def resolve_ns_record(self, domain: str) -> list:
        """Resolve NS records (Nameservers)"""
        if not validate_domain(domain):
            return []

        try:
            answers = self.resolver.resolve(domain, "NS")
            return [str(rdata) for rdata in answers]
        except Exception as e:
            self.logger.warning(f"NS record lookup failed: {str(e)}")
            return []

    def resolve_txt_record(self, domain: str) -> list:
        """Resolve TXT records (SPF, DKIM, DMARC)"""
        if not validate_domain(domain):
            return []

        try:
            answers = self.resolver.resolve(domain, "TXT")
            return [str(rdata) for rdata in answers]
        except Exception as e:
            self.logger.warning(f"TXT record lookup failed: {str(e)}")
            return []

    def resolve_all_records(self, domain: str) -> dict:
        """Resolve all common DNS records"""
        return {
            "domain": domain,
            "A_records": self.resolve_a_record(domain),
            "AAAA_records": self.resolve_aaaa_record(domain),
            "MX_records": self.resolve_mx_record(domain),
            "NS_records": self.resolve_ns_record(domain),
            "TXT_records": self.resolve_txt_record(domain),
        }

    def reverse_lookup(self, ip: str) -> str:
        """Reverse DNS lookup"""
        if not validate_ip(ip):
            self.logger.error(f"Invalid IP: {ip}")
            return None

        try:
            reverse_name = dns.reversename.from_address(ip)
            answers = self.resolver.resolve(reverse_name, "PTR")
            return str(answers[0])
        except Exception as e:
            self.logger.warning(f"Reverse lookup failed for {ip}: {str(e)}")
            return None

    def get_spf_record(self, domain: str) -> list:
        """Extract SPF records from TXT records"""
        txt_records = self.resolve_txt_record(domain)
        return [record for record in txt_records if record.startswith('"v=spf1')]

    def get_dmarc_record(self, domain: str) -> str:
        """Get DMARC policy record"""
        try:
            dmarc_domain = f"_dmarc.{domain}"
            answers = self.resolver.resolve(dmarc_domain, "TXT")
            return str(answers[0])
        except Exception:
            return None
