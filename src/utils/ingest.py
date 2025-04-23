from pathlib import Path
import os
import re
from src.utils.cleaning import clean_content  # Import from the new src package
from src.config import get

# --- CONFIG ---
JOURNAL_ROOT = Path(get("journal_dir"))
OUTPUT_DIR = Path("data/cleaned")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_all_markdown_files(root_path: Path):
    return list(root_path.rglob("*.md"))


def extract_date_from_path(file_path: Path):
    """
    Extract date from a path like /root/04 Apr/17 Apr.md
    Returns date string in YYYY-MM-DD format (using current year if not found)
    """
    try:
        # Get folder and file name
        month_folder = file_path.parent.name  # e.g., '04 Apr'
        day_file = file_path.stem  # e.g., '17 Apr'
        # Extract month and day
        month_num, month_str = month_folder.split()
        day_num, _ = day_file.split()
        year = str(Path().cwd().year)  # fallback to current year if not specified
        # Use current year (or you can make this configurable)
        year = str(2025)  # hardcoded for now, can be dynamic
        month_num = int(month_num)
        day_num = int(day_num)
        return f"{year}-{month_num:02d}-{day_num:02d}"
    except Exception as e:
        print(f"Error parsing date from path: {file_path} – {e}")
        return "unknown-date"


def read_file_content(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_cleaned_file(date_str: str, cleaned_text: str, output_dir: Path):
    if date_str == "unknown-date":
        return
    out_path = output_dir / f"{date_str}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)


def process_file(file_path: Path):
    date_str = extract_date_from_path(file_path)
    raw_text = read_file_content(file_path)
    cleaned = clean_content(raw_text)  # Use the imported cleaning function
    write_cleaned_file(date_str, cleaned, Path(OUTPUT_DIR))


def main():
    all_files = get_all_markdown_files(JOURNAL_ROOT)
    print("Files to be analyzed:")
    for file_path in all_files:
        print(f"- {file_path}")
    for file_path in all_files:
        process_file(file_path)


if __name__ == "__main__":
    main()
