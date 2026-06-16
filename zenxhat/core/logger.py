"""
Logging utilities for ZENXHAT
"""

import logging
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter with colored output"""

    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        record.levelname = f"{log_color}{record.levelname}{Style.RESET_ALL}"
        return super().format(record)


def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Setup and return a logger instance"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(getattr(logging, level))

    # Formatter
    formatter = ColoredFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ch.setFormatter(formatter)

    # Add handler if not exists
    if not logger.handlers:
        logger.addHandler(ch)

    return logger
