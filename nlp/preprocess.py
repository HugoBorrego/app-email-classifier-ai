import re # Usado para limpeza de espaços
import spacy

_nlp = None

def _ensure_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("pt_core_news_sm")

def preprocess_text(text: str) -> str:
    if not text:
        return ""
    _ensure_nlp()
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)

    doc = _nlp(text)
    tokens = []
    for t in doc:
        if t.is_stop or t.is_punct or t.like_email or t.like_url:
            continue
        lemma = t.lemma_.strip()
        if lemma:
            tokens.append(lemma)
    return " ".join(tokens)


""" 
IA: Copilot

Prompt: Quais bibliotecas python são usadas para leitura de arquivos (.txt/.pdf) e pré-processamento de texto para NLP?

Resposta: 
1. spaCy
Para tokenização, lematização, remoção de stopwords, etc.
...

Prompt: Me mostre a documentação e exemplos de uso da biblioteca spaCy?
...
"""