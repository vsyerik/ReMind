import subprocess
from typing import List
from datetime import date

def get_reminders():
    script = '''
    tell application "Reminders"
            set theReminders to name of every reminder in every list
            return theReminders
        end tell
    '''
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=10
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        if result.returncode != 0:
            print("AppleScript error:", result.stderr)
            return []
        return [result.stdout.strip()] if result.stdout.strip() else []
    except subprocess.TimeoutExpired:
        print("AppleScript timed out. Reminders AppleScript interface may be broken on this macOS version.")
        return []

if __name__ == "__main__":
    reminders = get_reminders()
    print("Reminders result:", reminders)
    events = get_reminders()
    for event in events:
        print(event)

