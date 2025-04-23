tell application "Reminders"
    set theReminders to name of every reminder in every list
    return theReminders
end tell