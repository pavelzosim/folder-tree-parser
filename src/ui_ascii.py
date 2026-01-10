from utils import normalize_path
import os

from colorama import Fore, Style, init
init(autoreset=True)

TEMPLATE_DIR = "templates"

def banner():
    """Print the program banner with color."""
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "   Folder Tree Parser")
    print(Fore.CYAN + "   Scan folders → Export structure")
    print(Fore.CYAN + "=" * 60)

def ask_path():
    """Prompt for a folder path to scan."""
    return input("📁 Enter folder path to scan:\n> ").strip()

def ask_include_files():
    """Ask if file names should be included in the scan."""
    return input("Include file names? (y/n): ").lower().startswith("y")

def ask_output_format():
    """Prompt for output format selection."""
    print("\nSelect output format:")
    print("1) JSON")
    print("2) CSV")
    print("3) TXT")
    choice = input("> ").strip()

    return {
        "1": "json",
        "2": "csv",
        "3": "txt"
    }.get(choice, "json")

def ask_path_safe():
    """Prompt for a valid folder path, with retry and exit options."""
    while True:
        raw = input("\n[INFO] Enter folder path to scan:\n> ").strip()
        path = normalize_path(raw)

        if os.path.isdir(path):
            return path

        print("\n[ERROR] Path does not exist:")
        print(path)
        print("\n1) Enter path again")
        print("2) Exit")

        choice = input("> ").strip()
        if choice == "2":
            return None

def ask_continue():
    """Ask if the user wants to process another folder or exit."""
    print("\n1) Parse another folder")
    print("2) Exit")
    choice = input("> ").strip()
    return choice == "1"

def ask_template_file():
    """Prompt for a .fst template file path, with validation and retry."""
    while True:
        raw = input("\n[INFO] Enter .fst template file path:\n> ").strip()
        path = normalize_path(raw)

        if os.path.isfile(path) and path.lower().endswith(".fst"):
            return path

        print("\n[ERROR] Invalid .fst file.")
        print("1) Try again")
        print("2) Exit")

        if input("> ").strip() == "2":
            return None

def ask_template_from_list():
    """Prompt user to select a .fst template from the templates directory."""
    if not os.path.isdir(TEMPLATE_DIR):
        print(f"[ERROR] Templates folder not found: {TEMPLATE_DIR}")
        return None

    files = sorted(
        f for f in os.listdir(TEMPLATE_DIR)
        if f.lower().endswith(".fst")
    )

    if not files:
        print("[ERROR] No .fst templates found.")
        return None

    print("\nAvailable templates:")
    for i, name in enumerate(files, start=1):
        print(f"{i}) {name}")

    print("0) Exit")

    while True:
        choice = input("> ").strip()
        if choice == "0":
            return None

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return os.path.join(TEMPLATE_DIR, files[idx])

        print("[!] Invalid selection. Try again.")
