"""
Folder scanner module.

Recursively or shallowly scans directory structures into a nested dict.
"""

import os
from typing import Dict, Any


def scan_folder(
    root_path: str,
    include_files: bool,
    include_subfolders: bool = False
) -> Dict[str, Any]:
    """
    Scan a folder into a nested dictionary structure.

    Args:
        root_path: Path to the root directory to scan.
        include_files: If True, include file names under "_files" key.
        include_subfolders: If True, scan recursively. If False, only immediate children.

    Returns:
        Nested dict representing the folder structure.
    """
    tree: Dict[str, Any] = {}

    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        node = tree

        if rel_path != ".":
            for part in rel_path.split(os.sep):
                node = node.setdefault(part, {})

        # Shallow scan: only root level
        if rel_path == "." and not include_subfolders:
            for d in dirs:
                node.setdefault(d, {})
            if include_files:
                node["_files"] = files
            dirs[:] = []  # Prevent deeper traversal
            continue

        if include_files:
            node["_files"] = files

    return tree
