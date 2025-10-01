import os
from typing import Dict, Tuple
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_email_with_transformers(text: str) -> Tuple[str, float, Dict]:
    try:
        result = classifier(text)[0]
        label = result["label"]
        score = result["score"]

        categoria = "Produtivo" if label == "POSITIVE" else "Improdutivo"

        keywords = ["status", "requisição", "prazo", "resposta", "ação", "anexo", "erro", "falha", "problema"]
        sinais = [word for word in text.lower().split() if word in keywords]

        return categoria, round(score, 2), {"sinais": sinais}
    except Exception as e:
        return "Indefinido", 0.0, {"erro": str(e)}
