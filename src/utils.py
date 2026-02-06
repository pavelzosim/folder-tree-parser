"""
Utility functions.

Common helpers for path handling and filename generation.
"""

import os
import re
from datetime import datetime


def normalize_path(path: str) -> str:
    """
    Normalize a filesystem path.

    Removes quotes, normalizes slashes, and resolves the path.

    Args:
        path: Raw path string (may include quotes).

    Returns:
        Cleaned, normalized path.
    """
    if not path:
        return ""
    path = path.strip().strip('"').strip("'")
    return os.path.normpath(path)


def make_safe_filename(name: str) -> str:
    """
    Convert a string to a safe filename.

    Lowercase, underscores for spaces, alphanumeric only.

    Args:
        name: Original name string.

    Returns:
        Safe filename string.
    """
    name = name.strip().lower()
    name = name.replace(" ", "_")
    return re.sub(r"[^a-z0-9_\-]", "", name)


def get_date_stamp() -> str:
    """Return current date as YYYY-MM-DD string."""
    return datetime.now().strftime("%Y-%m-%d")
