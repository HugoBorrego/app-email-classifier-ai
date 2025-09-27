import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

from utils.file_reader import read_text_from_upload
from nlp.preprocess import preprocess_text
from nlp.classifier import classify_email
from nlp.responder import suggest_reply

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
    raw_text = await read_text_from_upload(file, text)
    cleaned = preprocess_text(raw_text)

    category, confidence, signals = classify_email(cleaned, raw_text)
    reply = suggest_reply(category, raw_text, signals)

    return {
        "category": category,
        "confidence": confidence,
        "reply": reply,
        "signals": signals,
    }
