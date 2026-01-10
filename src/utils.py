import os
import re
from datetime import datetime

def normalize_path(path: str) -> str:
    """
    Normalize and clean up a filesystem path.
    Removes quotes, normalizes slashes, and resolves the path.
    """
    if not path:
        return ""

    # Remove surrounding quotes
    path = path.strip().strip('"').strip("'")

    # Normalize slashes and resolve
    path = os.path.normpath(path)

    return path

def make_safe_filename(name: str) -> str:
    """
    Convert a string to a safe, lowercase filename using underscores.
    Removes unsafe characters.
    """
    name = name.strip().lower()
    name = name.replace(" ", "_")
    name = re.sub(r"[^a-z0-9_\-]", "", name)
    return name

def get_date_stamp() -> str:
    """Return current date as YYYY-MM-DD string."""
    return datetime.now().strftime("%Y-%m-%d")
