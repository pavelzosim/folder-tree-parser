"""
Folder creator module.

Creates directory structures from parsed template data.
"""

import os
from typing import List, Tuple


def create_folders(base_path: str, structure: List[Tuple[int, str]]) -> None:
    """
    Create nested folders from a structure definition.

    Args:
        base_path: Root directory where folders will be created.
        structure: List of (depth, folder_name) tuples from template parser.
    """
    stack: List[str] = []

    for depth, name in structure:
        stack = stack[:depth]
        stack.append(name)
        folder_path = os.path.join(base_path, *stack)
        os.makedirs(folder_path, exist_ok=True)
