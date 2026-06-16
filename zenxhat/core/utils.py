"""
Utility functions for ZENXHAT
"""

import re
from typing import List, Dict, Any
import json


def sanitize_input(user_input: str) -> str:
    """Sanitize user input to prevent injection attacks"""
    # Remove shell metacharacters
    dangerous_chars = r"[;&|`$()\n\r]"
    sanitized = re.sub(dangerous_chars, "", user_input)
    return sanitized.strip()


def validate_domain(domain: str) -> bool:
    """Validate domain format"""
    domain_pattern = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$"
    return bool(re.match(domain_pattern, domain.lower()))


def validate_email(email: str) -> bool:
    """Validate email format"""
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_pattern, email))


def validate_ip(ip: str) -> str:
    """Validate IPv4 or IPv6 address
    Returns: 'ipv4', 'ipv6', or None
    """
    ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    ipv6_pattern = r"^(?:[a-f0-9]{1,4}:){7}[a-f0-9]{1,4}$"

    if re.match(ipv4_pattern, ip):
        return "ipv4"
    elif re.match(ipv6_pattern, ip.lower()):
        return "ipv6"
    return None


def format_json(data: Dict[str, Any]) -> str:
    """Format data as pretty JSON"""
    return json.dumps(data, indent=2, ensure_ascii=False)


def save_output(data: Dict[str, Any], filename: str, output_dir: str = "output") -> str:
    """Save output data to JSON file"""
    from pathlib import Path

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    file_path = output_path / f"{filename}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return str(file_path)


def print_header(title: str, width: int = 80) -> None:
    """Print formatted header"""
    from colorama import Fore, Style

    print(f"\n{Fore.CYAN}{'=' * width}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{title.center(width)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * width}{Style.RESET_ALL}\n")


def print_success(message: str) -> None:
    """Print success message"""
    from colorama import Fore, Style

    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print info message"""
    from colorama import Fore, Style

    print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print error message"""
    from colorama import Fore, Style

    print(f"{Fore.RED}[-] {message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """Print warning message"""
    from colorama import Fore, Style

    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")
