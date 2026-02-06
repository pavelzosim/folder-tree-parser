````md
```text
============================================================
   PAVEL ZOSIM
   CODE x ART x AUTOMATE
============================================================
````

# FolderTree.Parser v2.0

A lightweight CLI tool for analyzing and generating folder structures.

FolderTree.Parser is designed to:

* Parse existing directory structures
* Generate folders from human-readable templates
* Export results into common text-based formats
* Work fully offline with a clean ASCII terminal interface

Built for developers, technical artists, and structured workflows.

---

## Features

### Mode 1 — Folder Parsing

* Recursive folder scanning
* Optional file name inclusion
* Export formats:

  * JSON
  * CSV
  * TXT
* Semantic root folder preserved
* Timestamped output files
* Windows-friendly (`.bat` launchers)

### Mode 2 — Folder Creation from Template

* Create folder hierarchies from templates (`.fst` / `.txt`)
* Indentation-based, human-readable format
* Supports comments and inline instructions
* Safe output (folders are created only inside `output/`)

---

## Requirements

* Python 3.9+
* Windows 10 / 11
  *(Linux / macOS not officially tested)*

No external system dependencies.

---

## Quick Start

```bash
install.bat
RUN.bat
```

Follow the on-screen menu.

---

## Program Modes

After launch, select a mode:

```
1) Parse existing folder
2) Create folders from template (.fst / .txt)
3) Exit
```

---

## Parsing Mode (Export Folder Structure)

1. Select a folder to scan
2. Choose output format
3. Result is saved to `output/` as:

```
folder_<root_name>_YYYY-MM-DD.txt
folder_<root_name>_YYYY-MM-DD.json
folder_<root_name>_YYYY-MM-DD.csv
```

### Example TXT Output

```
- Scripts
  - Camera
  - Core
    - Systems
      - DarkSauce
      - Pressure
  - UI
  - VFX
```

---

## Template Mode (Create Folder Structure)

Templates are stored in the `templates/` folder and listed automatically.

Supported extensions:

* `.fst` (recommended)
* `.txt` (beginner-friendly)

Templates are sorted alphabetically and selected by number.

---

## Template Format (`.fst` / `.txt`)

### Indentation Rules

* 1 level = 1 TAB **OR** 2 spaces
* Do NOT mix TABs and spaces on the same line
* Use consistent indentation
* Spaces inside folder names are allowed

### Comments

* Lines starting with `#` are ignored
* Comments can be used as inline documentation

---

### Example Template

```
# Folder Structure Template
# 1 TAB or 2 spaces = 1 level

Scripts
  Camera
  Collectables
  Core
    Systems
      DarkSauce
      Pressure
  Game
    Enemies
      Core
      Data
  UI
  VFX
```

### Result

```
output/
└── template_example/
    └── Scripts/
        ├── Camera/
        ├── Core/
        │   └── Systems/
        │       ├── DarkSauce/
        │       └── Pressure/
        └── VFX/
```

---

## Project Structure

```
FolderTree.Parser/
├── src/
│   ├── main.py              # Entry point
│   ├── ui_ascii.py          # Terminal UI
│   ├── scanner.py           # Folder scanning logic
│   ├── exporters.py         # JSON / CSV / TXT exporters
│   ├── template_parser.py   # .fst / .txt parsing
│   ├── folder_creator.py    # Folder creation logic
│   └── utils.py             # Shared utilities
├── templates/
│   └── example.fst
├── output/
│   └── .gitkeep
├── install.bat
├── RUN.bat
├── requirements.txt
└── README.md
```

---

## Design Philosophy

* Predictable behavior over hidden magic
* Clear separation of data and metadata
* Safe file system operations
* No GUI dependencies
* Human-readable formats first

Built as a tool, not a script.

---

## Roadmap

* Export templates from parsed folders
* Dry-run mode for template creation
* Ignore rules (`.fstignore`)
* Depth limit
* Overwrite / conflict detection

---

**Like this post?** ( ´◔ ω◔`) ノシ

**Support:**
[Buy Me a Coffee](https://buymeacoffee.com/pavel.zosim) | [Patreon](https://www.patreon.com/c/pavel_zosim) | [GitHub](https://github.com/pavelzosim) | [Gumroad](https://pavelzosim.gumroad.com/) | [YouTube](https://www.youtube.com/@VFX_PavelZosim/videos)

```