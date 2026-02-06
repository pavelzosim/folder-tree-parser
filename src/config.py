"""
Application configuration dataclass.

Stores runtime settings for folder parsing operations.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AppConfig:
    """Configuration for folder parsing mode."""

    root_path: str = ""
    include_files: bool = False
    include_subfolders: bool = False
    output_format: str = "json"  # json | csv | txt

    # Subfolder filtering
    filter_mode: str = "none"  # none | include | exclude
    subfolders: Optional[List[str]] = None
