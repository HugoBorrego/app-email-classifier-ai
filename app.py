import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

from utils.file_reader import read_text_from_upload
from nlp.preprocess import preprocess_text
from nlp.responder import suggest_reply
from nlp.classifier import classify_email_with_ai

app = FastAPI(title="Email Classifier AI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/process")
async def process_email(file: UploadFile | None = None, text: str | None = Form(default=None)):
    # 1. Lê o conteúdo do email (arquivo ou texto)
    raw_text = await read_text_from_upload(file, text)

    # 2. Pré-processa o texto (limpeza, lematização)
    cleaned = preprocess_text(raw_text)

    # 3. Classifica com IA (OpenAI ou outro modelo)
    category, confidence, signals = classify_email_with_ai(raw_text)

    # 4. Gera resposta automática com base na categoria
    reply = suggest_reply(category, raw_text, signals)

    # 5. Retorna os resultados
    return {
        "category": category,
        "confidence": confidence,
        "reply": reply,
        "signals": signals,
    }
