"""
ZENXHAT - OSINT Reconnaissance Toolkit
Version: 1.0.0
Author: zenCTRLalt
"""

__version__ = "1.0.0"
__author__ = "zenCTRLalt"
__description__ = "Comprehensive OSINT toolkit for ethical intelligence gathering"
__license__ = "MIT"

from .core.config import Config
from .core.logger import setup_logger

__all__ = ["Config", "setup_logger"]
