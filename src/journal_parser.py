import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pathlib import Path
from datetime import datetime, timedelta
import argparse

# Import the extract_journal_content function from utils.cleaning
from src.utils.cleaning import extract_journal_content
from src.config import get

def load_recent_entries(journal_dir: Path, since: datetime):
    """
    Load journal entries that have been modified since the specified date.

    Args:
        journal_dir: Directory containing journal entries
        since: Only include entries modified after this datetime

    Returns:
        List of dictionaries containing a path, content, and modified time
    """
    entries = []

    if not journal_dir.exists():
        print(f"Warning: Journal directory does not exist: {journal_dir}")
        return entries

    # Use the correct glob pattern for files like "/Users/vsyerik/Obsidian/Personal/Journal 📓/2025/04 Apr/Apr 17.md"
    glob_pattern = "**/[0-1][0-9] [A-Za-z][A-Za-z][A-Za-z]/[A-Za-z][A-Za-z][A-Za-z] [0-3][0-9].md"
    matching_files = list(journal_dir.glob(glob_pattern))

    # Filter by modification time
    for file in matching_files:
        modified_time = datetime.fromtimestamp(file.stat().st_mtime)
        if modified_time >= since:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            entries.append({
                "path": file,
                "content": content,
                "modified": modified_time
            })
    return entries

# Re-export extract_journal_content for backward compatibility
__all__ = ['load_recent_entries', 'extract_journal_content']

# Standalone execution for debugging
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load recent journal entries for debugging")
    default_journal_dir = get("journal_dir", str(Path.home() / "Documents" / "Journal"))
    parser.add_argument("--journal_dir", type=str, default=default_journal_dir,
                        help="Directory containing journal entries")
    parser.add_argument("--days", type=int, default=2,
                        help="Number of days to look back")
    args = parser.parse_args()

    journal_dir = Path(args.journal_dir)
    since_date = datetime.now() - timedelta(days=args.days)

    print(f"🔍 Scanning journal at {journal_dir} for the past {args.days} days...")
    entries = load_recent_entries(journal_dir, since_date)

    if not entries:
        print("No recent journal entries found.")
    else:
        print(f"Found {len(entries)} entries:")
        for entry in entries:
            print(f"- {entry['path']} (modified: {entry['modified']})")
            # print(f"  Content preview: {entry['content'][:100]}...")
            print()
