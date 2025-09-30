import os
from typing import Dict, Tuple
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não está definida no ambiente.")
openai.api_key = api_key


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
