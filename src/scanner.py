import os

def scan_folder(root_path: str, include_files: bool):
    tree = {}

    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        node = tree

        if rel_path != ".":
            for part in rel_path.split(os.sep):
                node = node.setdefault(part, {})

        if include_files:
            node["_files"] = files

    return tree
