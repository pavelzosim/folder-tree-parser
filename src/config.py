from dataclasses import dataclass

@dataclass
class AppConfig:
    root_path: str = ""
    include_files: bool = False
    output_format: str = "json"   # json | csv | txt
