from ui_ascii import (
    banner,
    ask_path_safe,
    ask_include_files,
    ask_output_format,
    ask_continue,
    ask_template_from_list,
)
from scanner import scan_folder
from exporters import export_json, export_csv, export_txt
from utils import make_safe_filename, get_date_stamp
from template_parser import parse_fst
from folder_creator import create_folders
import os

OUTPUT_DIR = "output"
PREFIX = "folder_"

def ask_mode():
    """Prompt user to select the main program mode."""
    print("\nSelect mode:")
    print("1) Parse existing folder")
    print("2) Create folders from template (.fst)")
    print("3) Exit")
    return input("> ").strip()

def run_parse_mode():
    """Run folder parsing and export mode."""
    root_path = ask_path_safe()
    if not root_path:
        print("\n[INFO] Exiting program.")
        return

    include_files = ask_include_files()
    output_format = ask_output_format()

    root_name = os.path.basename(root_path.rstrip("\\/"))
    print("\n[INFO] Root directory:")
    print(root_path)
    print(f"[INFO] Root folder name: {root_name}")

    tree = scan_folder(root_path, include_files)

    safe_root = make_safe_filename(root_name)
    date_stamp = get_date_stamp()

    output_filename = f"{PREFIX}{safe_root}_{date_stamp}.{output_format}"
    output_file = os.path.join(OUTPUT_DIR, output_filename)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Export the folder structure in the selected format
    if output_format == "json":
        export_json({root_name: tree}, output_file)
    elif output_format == "csv":
        export_csv({root_name: tree}, output_file)
    else:
        export_txt({root_name: tree}, output_file)

    print("\n[OK] Parsing completed")
    print("[INFO] Output saved to:")
    print(output_file)

def run_template_mode():
    """Run folder creation from template mode."""
    template_path = ask_template_from_list()
    if not template_path:
        return

    template_name = os.path.splitext(os.path.basename(template_path))[0]
    output_root = os.path.join("output", f"template_{template_name}")

    try:
        structure = parse_fst(template_path)
    except Exception as e:
        print(f"\n[ERROR] Invalid .fst file:")
        print(e)
        return

    create_folders(output_root, structure)

    print("\n[OK] Folder structure created")
    print("[INFO] Output location:")
    print(output_root)

def main():
    """Main program loop."""
    while True:
        banner()
        mode = ask_mode()

        if mode == "1":
            run_parse_mode()
        elif mode == "2":
            run_template_mode()
        else:
            print("\n[INFO] Exiting program.")
            return

        if not ask_continue():
            print("\n[INFO] Program finished.")
            return

if __name__ == "__main__":
    main()
