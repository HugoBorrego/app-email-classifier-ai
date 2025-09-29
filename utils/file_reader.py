from fastapi import UploadFile # tipo de arquivo recebido via formulário
from pdfminer.high_level import extract_text as pdf_extract_text # extrai texto de PDFs
import chardet # detecta encoding de arquivos .txt

async def read_text_from_upload(file: UploadFile | None, text: str | None) -> str:
    if text and text.strip():
        return text.strip()

    if file is None:
        return ""

    if file.filename.lower().endswith(".pdf"):
        content = await file.read()
        with open("tmp_upload.pdf", "wb") as f:
            f.write(content)
        return pdf_extract_text("tmp_upload.pdf") or ""

    raw = await file.read()
    detected = chardet.detect(raw)
    encoding = detected.get("encoding", "utf-8") or "utf-8"
    try:
        return raw.decode(encoding, errors="ignore")
    except Exception:
        return raw.decode("utf-8", errors="ignore")



""" 
IA: Copilot

Prompt: Mostre um código de leitura de texto txt ou pdf em python usando bibliotecas e fastapi comuns para eu usar como base em meu projeto.

Resposta:
...
"""