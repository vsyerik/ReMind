from textblob import TextBlob
import requests

def get_sentiment_textblob(text: str) -> str:
    """
    Get sentiment using TextBlob.

    Args:
        text: The text to analyze

    Returns:
        String indicating sentiment: "positive", "neutral", or "negative"
    """
    # Check for strongly negative phrases
    negative_phrases = ["terrible day", "worst day", "hate", "awful"]
    for phrase in negative_phrases:
        if phrase in text.lower():
            return "negative"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def get_sentiment(text: str) -> str:
    """
    Get sentiment using Ollama if available, falling back to TextBlob.

    Args:
        text: The text to analyze

    Returns:
        String indicating sentiment: "positive", "neutral", or "negative"
    """
    prompt = (
        "Analyze the emotional tone of the following journal entry. "
        "Reply with only one word: positive, neutral, or negative.\n\n"
        f"{text}"
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi4",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.5,
            },
            timeout=30
        )
        response.raise_for_status()
        answer = response.json()["response"].strip().lower()
        if answer not in {"positive", "neutral", "negative"}:
            return "neutral"
        return answer
    except Exception as e:
        print(f"[Ollama error] {e}")
        # Fall back to TextBlob-based sentiment analysis
        return get_sentiment_textblob(text)


def get_weekly_insight(text: str) -> str:
    prompt = (
        "These are my journal entries from the past week.\n\n"
        "Please analyze them and describe the emotional or psychological themes that show up. "
        "Write your response in first person, as if I am reflecting on myself. "
        "Use language like 'I noticed...', 'I felt...', or 'I seem to be...'. "
        "Speak gently and with emotional intelligence.\n\n"
        f"{text}"
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.7,
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        print(f"[Ollama insight error] {e}")
        return "(Insight unavailable)"
