from utils import normalize_path
import os

from colorama import Fore, Style, init
init(autoreset=True)

TEMPLATE_DIR = "templates"


# ------------------------------------------------------------
# Color helpers (green terminal style)
# ------------------------------------------------------------

GREEN = Fore.GREEN
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL


def info(text):
    print(f"{GREEN}[INFO]{RESET} {text}")


def ok(text):
    print(f"{GREEN}[OK]{RESET} {text}")


def error(text):
    print(f"{GREEN}[ERROR]{RESET} {text}")


def line():
    print(GREEN + "-" * 60 + RESET)


# ------------------------------------------------------------
# UI
# ------------------------------------------------------------

def banner():
    """Print the program banner."""
    line()
    print(BRIGHT + GREEN + "FOLDER TREE PARSER v2.0" + RESET)
    print(GREEN + "Scan folders -> Export structure" + RESET)
    line()
    print(GREEN + "by Pavel Zosim ( ´◔ ω◔`) ノシ | pavelzosim.com | tools & tutorials" + RESET)



def ask_path():
    """Prompt for a folder path to scan."""
    return input("\nEnter folder path to scan:\n> ").strip()


def ask_include_files():
    """Ask if file names should be included in the scan."""
    return input("\nInclude file names? (y/n): ").lower().startswith("y")


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
        raw = input("\nEnter folder path to scan:\n> ").strip()
        path = normalize_path(raw)

        if os.path.isdir(path):
            return path

        error("Path does not exist:")
        print(path)
        print("\n1) Enter path again")
        print("2) Exit")

        if input("> ").strip() == "2":
            return None


def ask_continue():
    """Ask if the user wants to process another folder or exit."""
    print("\n1) Parse another folder")
    print("2) Exit")
    return input("> ").strip() == "1"


def ask_template_from_list():
    """Prompt user to select a template from the templates directory."""
    if not os.path.isdir(TEMPLATE_DIR):
        error(f"Templates folder not found: {TEMPLATE_DIR}")
        return None

    files = sorted(
        f for f in os.listdir(TEMPLATE_DIR)
        if f.lower().endswith((".fst", ".txt"))
    )

    if not files:
        error("No templates found.")
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

        error("Invalid selection. Try again.")


def ask_next_action():
    """
    Ask the user what to do next after completing an action.
    Returns:
        str: "1" for main menu, "2" to repeat, "3" to exit.
    """
    print("\nWhat next?")
    print("1) Back to main menu")
    print("2) Repeat this action")
    print("3) Exit")
    choice = input("> ").strip()
    return choice
