import os
from typing import Dict, Tuple
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("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")

def classify_email_with_ai(text: str) -> Tuple[str, float, Dict]:
    prompt = (
        "Você é um assistente que classifica emails em duas categorias: "
        "'Produtivo' (requere ação ou resposta) e 'Improdutivo' (não requer ação imediata). "
        "Leia o email abaixo e responda com a categoria, grau de confiança (0 a 1), e palavras-chave relevantes.\n\n"
        f"Email:\n{text}\n\n"
        "Responda no formato JSON:\n"
        "{ \"categoria\": \"Produtivo\", \"confiança\": 0.85, \"sinais\": [\"status\", \"requisição\"] }"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" se disponível
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    import json
    try:
        content = response["choices"][0]["message"]["content"]
        result = json.loads(content)
        return result["categoria"], result["confiança"], {"sinais": result.get("sinais", [])}
    except Exception as e:
        return "Indefinido", 0.0, {"erro": str(e)}
