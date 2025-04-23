from pathlib import Path
from datetime import datetime, timedelta
from src.journal_parser import load_recent_entries
from src.analysis import analyze_entries
from src.output import render_summary
from src.models.sentiment import get_weekly_insight
from src.config import get

# --- Configuration ---
# Get configuration from config module with fallbacks
JOURNAL_DIR = Path(get("journal_dir", str(Path.home() / "Documents" / "Journal")))
DAYS_BACK = get("days_back", 7)

# --- Main CLI ---
def main():
    print("🔍 Scanning journal for the past 7 days...")
    since_date = datetime.now() - timedelta(days=DAYS_BACK)
    entries = load_recent_entries(JOURNAL_DIR, since_date)

    if not entries:
        print("No recent journal entries found.")
        return

    print(f"Found {len(entries)} entries. Analyzing...")
    summary = analyze_entries(entries)

    weekly_text = "\n\n".join([e["content"] for e in entries])
    summary["ollama_insight"] = get_weekly_insight(weekly_text)
    render_summary(summary)

if __name__ == "__main__":
    main()
