import re # Usado para limpeza de espaços
from typing import Tuple, Dict, List

PRODUCTIVE_KEYWORDS = [
    "status", "andamento", "atualização", "suporte", "pedido", "requisição",
    "anexo", "documento", "proposta", "prazo", "urgente", "problema",
    "erro", "falha", "chamado", "ticket", "login", "acesso", "fatura", "boleto",
]
UNPRODUCTIVE_KEYWORDS = [
    "feliz natal", "boas festas", "parabéns", "agradeço", "obrigado", "grato",
    "comunicado", "divulgação", "newsletter",
]

def _find_signals(text: str, keywords: List[str]) -> List[str]:
    signals = []
    for kw in keywords:
        if re.search(rf"\b{re.escape(kw)}\b", text, flags=re.IGNORECASE):
            signals.append(kw)
    return signals

def classify_email(cleaned: str, raw_text: str) -> Tuple[str, float, Dict]:
    prod_hits = _find_signals(raw_text, PRODUCTIVE_KEYWORDS)
    impr_hits = _find_signals(raw_text, UNPRODUCTIVE_KEYWORDS)

    score_prod = len(prod_hits)
    score_impr = len(impr_hits)

    if "?" in raw_text:
        score_prod += 0.5

    if re.search(r"\banexo(s)?\b|\bsegue(m)?\b|\banexei\b", raw_text, re.IGNORECASE):
        score_prod += 0.7

    if score_prod > score_impr:
        category = "Produtivo"
        confidence = min(0.5 + 0.1 * score_prod, 0.95)
    elif score_impr > score_prod:
        category = "Improdutivo"
        confidence = min(0.5 + 0.1 * score_impr, 0.95)
    else:

        category = "Produtivo" if "?" in raw_text or "status" in raw_text.lower() else "Improdutivo"
        confidence = 0.55

    signals = {
        "prod_hits": prod_hits,
        "impr_hits": impr_hits,
        "score_prod": score_prod,
        "score_impr": score_impr,
    }
    return category, confidence, signals