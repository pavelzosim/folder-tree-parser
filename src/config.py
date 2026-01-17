from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AppConfig:
    root_path: str = ""
    include_files: bool = False
    include_subfolders: bool = False  # If True, scan nested subfolders. If False, only immediate children.
    output_format: str = "json"   # json | csv | txt

    # Subfolder filter settings:
    #   filter_mode: "none" | "include" | "exclude"
    #   subfolders: list of immediate subfolder names (relative to root_path)
    filter_mode: str = "none"
    subfolders: Optional[List[str]] = None
