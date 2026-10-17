#Purpose: Clean text
#Remove stopwords

import re


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()

    # Normalize common technical terms before cleaning.
    text = re.sub(r"\bc\s*\+\s*\+", "cplusplus", text)
    text = re.sub(r"\bc\s*#", "csharp", text)
    text = re.sub(r"\.net\b", "dotnet", text)
    text = re.sub(r"\bnode\.js\b", "nodejs", text)

    # Keep letters, digits, whitespace and underscores.
    text = re.sub(r"[^\w\s]", " ", text)

    # Normalize repeated whitespace.
    text = re.sub(r"\s+", " ", text).strip()

    return text


def remove_stopwords(text):
    if not isinstance(text, str) or not text.strip():
        return ""

    # Lightweight English stopword list.
    stopwords = {
        "a", "an", "the", "is", "are", "was", "were",
        "and", "or", "but", "of", "to", "in", "on",
        "for", "with", "by", "from", "at", "as", "be",
        "been", "being", "this", "that", "these", "those",
        "it", "its", "i", "we", "you", "they", "he", "she",
        "have", "has", "had", "do", "does", "did"
    }

    words = text.split()
    filtered_words = [
        word for word in words if word not in stopwords
    ]

    return " ".join(filtered_words)


def preprocess_text(text, remove_common_words=False):
    cleaned_text = clean_text(text)

    if remove_common_words:
        cleaned_text = remove_stopwords(cleaned_text)

    return cleaned_text
