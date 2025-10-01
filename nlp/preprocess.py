import re
import nltk
from nltk.corpus import stopwords
import string

try:
    stopwords.words("portuguese")
except LookupError:
    nltk.download("stopwords")
    nltk.download("punkt")

def preprocess_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)

    tokens = nltk.word_tokenize(text, language="portuguese")

    stop_words = set(stopwords.words("portuguese"))
    cleaned_tokens = [
        word for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]
    return " ".join(cleaned_tokens)
