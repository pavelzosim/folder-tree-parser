import json
import csv
import os
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from semantic_analyzer import FileTagResult
    from semantic_config import SemanticConfig

def export_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def export_txt(data, output_path, indent=0):
    with open(output_path, "w", encoding="utf-8") as f:
        _write_txt(data, f, indent)

def _write_txt(data, file, indent):
    for key, value in data.items():
        file.write("  " * indent + f"- {key}\n")
        if isinstance(value, dict):
            _write_txt(value, file, indent + 1)

def export_csv(data, output_path):
    rows = []

    def walk(node, path=""):
        for key, value in node.items():
            current = f"{path}/{key}" if path else key
            rows.append([current])
            if isinstance(value, dict):
                walk(value, current)

    walk(data)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Path"])
        writer.writerows(rows)


# ------------------------------------------------------------
# Semantic analysis exporters
# ------------------------------------------------------------

def export_semantic_json(results, output_path, corpus_stats=None):
    """Export semantic analysis results to JSON."""
    data = {
        "files": [],
        "corpus": None
    }

    for r in results:
        data["files"].append({
            "file": r.file_path,
            "tags": [{"token": token, "weight": weight} for token, weight in r.tags],
            "token_counts": r.token_counts
        })

    # Add corpus-level info
    if corpus_stats:
        data["corpus"] = {
            "root_folder": corpus_stats.root_folder,
            "file_count": corpus_stats.file_count,
            "total_count": corpus_stats.total_count
        }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def export_semantic_csv(results, output_path):
    """Export semantic analysis results to CSV."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Tags", "Weights"])
        for r in results:
            tags_str = "; ".join(r.tag_names)
            weights_str = "; ".join(f"{w:.1f}" for _, w in r.tags)
            writer.writerow([r.file_path, tags_str, weights_str])


def export_semantic_txt(results, output_path, corpus_stats=None):
    """Export semantic analysis results to human-readable TXT."""
    with open(output_path, "w", encoding="utf-8") as f:
        # Corpus summary header
        if corpus_stats:
            f.write("=" * 60 + "\n")
            f.write("CORPUS SUMMARY\n")
            f.write("=" * 60 + "\n")
            f.write(f"Root folder: {corpus_stats.root_folder}\n")
            f.write(f"Total unique tokens: {len(corpus_stats.file_count)}\n")

            # Top tokens by file count
            top_tokens = sorted(corpus_stats.file_count.items(), key=lambda x: x[1], reverse=True)[:20]
            f.write(f"Top tokens: {', '.join(t for t, _ in top_tokens)}\n")
            f.write("=" * 60 + "\n\n")

        # Per-file results
        for r in results:
            f.write(f"File: {r.file_path}\n")
            if r.tags:
                tags_formatted = ", ".join(f"{token}({weight:.1f})" for token, weight in r.tags)
                f.write(f"Tags: {tags_formatted}\n")
            else:
                f.write("Tags: (none)\n")
            f.write("-" * 60 + "\n")


def export_semantic_obsidian(results, output_path, config=None, root_path=None):
    """Export semantic analysis results to Obsidian-compatible Markdown.

    Supports:
    - content mode: [[path]] with #tags
    - yaml mode: YAML frontmatter with tags array
    - path_format: absolute or relative paths
    - file splitting: if file exceeds max_lines_per_file

    Args:
        results: List of FileTagResult
        output_path: Output file path
        config: SemanticConfig for export options
        root_path: Root path for relative path calculation
    """
    from semantic_config import DEFAULT_CONFIG

    if config is None:
        config = DEFAULT_CONFIG

    # Generate all lines first
    lines = []
    for r in results:
        # Determine path format
        file_path = r.file_path
        if config.path_format == "relative" and root_path:
            try:
                file_path = os.path.relpath(r.file_path, root_path)
            except ValueError:
                pass  # Keep absolute if relpath fails (different drives)

        # Tags - extensions without dot (e.g., "pdf" -> "#pdf")
        tag_names = [token for token, _ in r.tags]

        if config.output_mode == "yaml":
            # YAML frontmatter format
            lines.append("---")
            lines.append(f"file: \"{file_path}\"")
            if tag_names:
                lines.append("tags:")
                for tag in tag_names:
                    lines.append(f"  - {tag}")
            lines.append("---")
            lines.append("")
        else:
            # Content mode (default)
            lines.append(f"[[{file_path}]]")
            if tag_names:
                tags_str = " ".join(f"#{token}" for token in tag_names)
                lines.append(tags_str)
            lines.append("")

    # Check if splitting is needed
    max_lines = config.max_lines_per_file
    if len(lines) <= max_lines:
        # Single file output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    else:
        # Split into multiple files
        _write_split_files(lines, output_path, max_lines)


def _write_split_files(lines: List[str], base_path: str, max_lines: int):
    """Split lines into multiple files.

    Args:
        lines: All lines to write
        base_path: Base output path (e.g., output/semantic_foo_2024.md)
        max_lines: Maximum lines per file
    """
    # Parse base path to create part names
    base_dir = os.path.dirname(base_path)
    base_name = os.path.basename(base_path)
    name, ext = os.path.splitext(base_name)

    part_num = 1
    start_idx = 0
    output_files = []

    while start_idx < len(lines):
        end_idx = min(start_idx + max_lines, len(lines))

        # Try to end at a blank line (entry boundary)
        if end_idx < len(lines):
            # Look for blank line near the cut point
            for i in range(end_idx, max(start_idx, end_idx - 50), -1):
                if lines[i - 1] == "":
                    end_idx = i
                    break

        # Generate part filename
        part_filename = f"{name}_part_{part_num}{ext}"
        part_path = os.path.join(base_dir, part_filename) if base_dir else part_filename

        # Write this part
        with open(part_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines[start_idx:end_idx]))

        output_files.append(part_path)
        part_num += 1
        start_idx = end_idx

    print(f"[INFO] Output split into {len(output_files)} files:")
    for path in output_files:
        print(f"  - {path}")
