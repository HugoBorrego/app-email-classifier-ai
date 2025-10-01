from datetime import datetime

def suggest_reply(category: str, raw_text: str, signals: dict) -> str:
    text_lower = raw_text.lower()

    if category == "Improdutivo":
        return (
            "Olá!\n\n"
            "Agradecemos sua mensagem. Não há ação necessária neste momento.\n"
            "Caso precise de suporte ou tenha alguma solicitação específica, "
            "responda este email e vamos ajudar.\n\n"
            "Atenciosamente,\nEquipe de Atendimento"
        )

    if any(word in text_lower for word in ["status", "andamento", "atualização"]):
        return (
            "Olá!\n\n"
            "Recebemos sua solicitação de status e estamos verificando o andamento junto ao time responsável. "
            "Retornaremos com uma atualização até o fim do dia útil.\n\n"
            "Se houver alguma informação adicional ou número de protocolo, por favor, compartilhe para agilizar.\n\n"
            "Atenciosamente,\nEquipe de Atendimento"
        )

    if any(word in text_lower for word in ["anexo", "segue"]):
        return (
            "Olá!\n\n"
            "Confirmamos o recebimento do(s) anexo(s). Vamos validar o conteúdo e dar sequência ao processamento. "
            "Caso seja necessário algum ajuste, entraremos em contato.\n\n"
            "Atenciosamente,\nEquipe de Atendimento"
        )

    if any(word in text_lower for word in ["erro", "falha", "problema"]):
        return (
            "Olá!\n\n"
            "Lamentamos pelo inconveniente. Para acelerar o diagnóstico, poderia nos enviar:\n"
            "- Print do erro\n"
            "- Horário aproximado do ocorrido\n"
            "- Número de protocolo (se houver)\n\n"
            "Estamos abrindo um chamado e retornaremos com uma solução o quanto antes.\n\n"
            "Atenciosamente,\nEquipe de Suporte"
        )

    return (
        "Olá!\n\n"
        "Obrigado pela mensagem. Já direcionamos seu pedido ao time responsável e retornaremos em breve.\n\n"
        "Se puder, inclua detalhes como número de protocolo, prazo desejado ou contexto adicional para agilizar.\n\n"
        "Atenciosamente,\nEquipe de Atendimento"
    )
