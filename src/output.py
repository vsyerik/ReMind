from datetime import datetime, timedelta

def render_summary(summary: dict):
    today = datetime.now()
    last_week = today - timedelta(days=7)
    header = f"🧠 ReMind Pulse — {last_week.strftime('%b %d')} to {today.strftime('%b %d')}\n"

    tone = ", ".join([f"{k}: {v}" for k, v in summary.get('tone_summary', {}).items()])
    words = ", ".join([word for word, _ in summary['most_common_words']])
    questions = summary['questions_count']
    tags = ", ".join([f"#{tag}" for tag, _ in summary['tags']])
    avg_len = f"{summary['average_length']:.0f}"
    repeated = summary['repeated_words']

    # Try to find a nice prompt word
    prompt_word = repeated[0] if repeated else "stillness"

    body = f"""
{header}
Tone: {tone}
Most used words: {words}
Questions asked: {questions}
Tags: {tags}
Average entry length: {avg_len} words

📌 Gentle prompt: What does \"{prompt_word}\" mean to you this week?
"""

    print(body)
    if 'ollama_insight' in summary:
        print("\n🧠 Emotional Insight (via Ollama):")
        print(summary['ollama_insight'])
