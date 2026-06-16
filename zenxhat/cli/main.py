"""
CLI Main Interface for ZENXHAT
"""

import click
from zenxhat.core.logger import setup_logger
from zenxhat.core.config import config
from zenxhat.modules import (
    WhoisLookup,
    DNSResolver,
    SubdomainFinder,
    IPGeolocation,
    MetadataExtractor,
    EmailOSINT,
    UsernameFinder,
    SearchAggregator,
)
from zenxhat.core.utils import print_header, print_success, print_error, format_json

logger = setup_logger(__name__, config.LOG_LEVEL)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """ZENXHAT - OSINT Reconnaissance Toolkit"""
    pass


@cli.command()
@click.argument("domain")
def whois(domain):
    """Perform WHOIS lookup on a domain"""
    print_header(f"WHOIS Lookup: {domain}")
    try:
        whois_tool = WhoisLookup()
        result = whois_tool.lookup(domain)
        print(format_json(result))
        print_success("WHOIS lookup completed")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("domain")
def dns(domain):
    """Resolve DNS records for a domain"""
    print_header(f"DNS Resolution: {domain}")
    try:
        dns_tool = DNSResolver()
        result = dns_tool.resolve_all_records(domain)
        print(format_json(result))
        print_success("DNS resolution completed")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("domain")
def subdomains(domain):
    """Find subdomains for a domain (passive)"""
    print_header(f"Subdomain Enumeration: {domain}")
    try:
        subdomain_tool = SubdomainFinder()
        subdomains = subdomain_tool.find_subdomains(domain)
        result = {"domain": domain, "subdomains": subdomains, "count": len(subdomains)}
        print(format_json(result))
        print_success(f"Found {len(subdomains)} subdomains")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("ip_address")
def ipinfo(ip_address):
    """Get IP geolocation information"""
    print_header(f"IP Information: {ip_address}")
    try:
        ip_tool = IPGeolocation()
        result = ip_tool.geoip_lookup(ip_address)
        print(format_json(result))
        print_success("IP lookup completed")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("file_path")
def metadata(file_path):
    """Extract metadata from a file"""
    print_header(f"Metadata Extraction: {file_path}")
    try:
        metadata_tool = MetadataExtractor()
        if file_path.lower().endswith(("jpg", "jpeg", "png", "gif")):
            result = metadata_tool.extract_image_metadata(file_path)
        elif file_path.lower().endswith("pdf"):
            result = metadata_tool.extract_pdf_metadata(file_path)
        else:
            result = metadata_tool.extract_file_metadata(file_path)
        print(format_json(result))
        print_success("Metadata extraction completed")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("email")
def breach(email):
    """Check if email has been breached"""
    print_header(f"Breach Check: {email}")
    try:
        email_tool = EmailOSINT()
        result = email_tool.check_breach(email)
        print(format_json(result))
        if result.get("breached"):
            print_error(f"⚠️  Email found in {result.get('breach_count')} breach(es)!")
        else:
            print_success("Email not found in known breaches")
    except Exception as e:
        print_error(f"Error: {str(e)}")


@cli.command()
@click.argument("username")
def username(username):
    """Search for username across platforms"""
    print_header(f"Username Search: {username}")
    try:
        username_tool = UsernameFinder()
        result = username_tool.search_username(username)
        print(format_json(result))
        print_success(f"Found on {len(result['found_on'])} platform(s)")
    except Exception as e:
        print_error(f"Error: {str(e)}")


if __name__ == "__main__":
    cli()
