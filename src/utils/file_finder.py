from pathlib import Path
from typing import List

def get_all_markdown_files(root_path: Path) -> List[Path]:
    """
    Recursively find all Markdown (.md) files under the given root path.
    Prints each file found.
    Args:
        root_path (Path): The root directory to search.
    Returns:
        List[Path]: List of Markdown file paths.
    """
    files = list(root_path.rglob("*.md"))
    print("Files found for processing:")
    for f in files:
        print(f"- {f}")
    return files
