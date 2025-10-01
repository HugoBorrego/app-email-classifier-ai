from fastapi import UploadFile
from pdfminer.high_level import extract_text as pdf_extract_text
import chardet
import tempfile
import os

async def read_text_from_upload(file: UploadFile | None, text: str | None) -> str:
    if text and text.strip():
        return text.strip()

    if file is None:
        return ""

    if file.filename.lower().endswith(".pdf"):
        content = await file.read()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            return pdf_extract_text(tmp_path) or ""
        finally:
            os.remove(tmp_path)

    raw = await file.read()
    detected = chardet.detect(raw)
    encoding = detected.get("encoding", "utf-8") or "utf-8"
    try:
        return raw.decode(encoding, errors="ignore")
    except Exception:
        return raw.decode("utf-8", errors="ignore")

