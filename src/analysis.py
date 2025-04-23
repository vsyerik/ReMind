# analysis.py

import re
from collections import Counter
from typing import List, Dict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from src.models.sentiment import get_sentiment
from src.utils.cleaning import extract_journal_content
import yaml

from src.config import get

# Initialize NLTK resources
from src.utils.imports import nltk

STOPWORDS = set(stopwords.words('english'))
custom_stopwords = set(get("custom_stopwords", []))

def analyze_entries(entries: List[Dict]) -> Dict:
    word_counts = Counter()
    total_questions = 0
    tags = Counter()
    entry_lengths = []
    tone_counts = Counter()

    for entry in entries:
        content = entry['content']
        content = extract_journal_content(content)
        words = word_tokenize(content.lower())
        filtered_words = [w for w in words if w.isalpha() and w not in STOPWORDS and w not in custom_stopwords]
        word_counts.update(filtered_words)

        total_questions += content.count('?')
        tags.update(re.findall(r'#(\w+)', content))
        entry_lengths.append(len(words))

        sentiment = get_sentiment(content)
        tone_counts[sentiment] += 1

    most_common = word_counts.most_common(5)
    repeated_words = [word for word, count in word_counts.items() if count > 1]

    summary = {
        'most_common_words': most_common,
        'questions_count': total_questions,
        'tags': tags.most_common(),
        'average_length': sum(entry_lengths) / len(entry_lengths) if entry_lengths else 0,
        'repeated_words': repeated_words,
        'tone_summary': dict(tone_counts),
    }

    return summary
