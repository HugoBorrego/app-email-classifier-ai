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



""" 
IA: Copilot

Prompt: Quais bibliotecas python são usadas para leitura de arquivos (.txt/.pdf) e pré-processamento de texto para NLP?

Resposta: 
1. TextBlob: Para análise de sentimentos, tradução, correção gramatical, etc.
2. NLTK (Natural Language Toolkit): Para tokenização, remoção de stopwords, stemming, lemmatização, etc.
...

Prompt: Me mostre a documentação e exemplos de uso da biblioteca spaCy?
...
"""