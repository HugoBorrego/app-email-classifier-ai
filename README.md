# 📬 Classificador de Email com AI

Aplicação web simples que utiliza inteligência artificial para classificar emails como **Produtivos** ou **Improdutivos**, e sugerir respostas automáticas com base no conteúdo.  
Ideal para empresas que lidam com alto volume de mensagens e desejam automatizar triagem e atendimento.

---

## 🚀 Funcionalidades

- 📂 Upload de arquivos `.txt` ou `.pdf` com conteúdo de email.
- ✍️ Inserção direta de texto via formulário.
- 🧠 Classificação automática do email:
  - **Produtivo**: requer ação ou resposta (ex.: suporte, status, dúvidas).
  - **Improdutivo**: não exige ação imediata (ex.: felicitações, agradecimentos).
- 🤖 Geração de resposta automática contextualizada.
- 🌐 Interface web intuitiva e responsiva.
- ☁️ Pronto para deploy em nuvem (Render, Railway, etc.).

---

## 🧪 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/email-classifier-ai.git
cd email-classifier-ai

python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

# Baixe recursos do NLTK (apenas primeira vez)
import nltk
nltk.download("punkt")
nltk.download("stopwords")

uvicorn app:app --reload

http://localhost:8000
```

``` bash
email-classifier-ai/
├─ app.py                      # Backend principal com FastAPI
├─ templates/index.html        # Interface web
├─ static/styles.css           # Estilos da interface
├─ utils/file_reader.py        # Leitura de arquivos .txt/.pdf
├─ nlp/
│  ├─ preprocess.py            # Pré-processamento de texto (NLTK + TextBlob)
│  ├─ responder.py             # Geração de resposta automática
│  └─ classifier.py            # Classificação com IA (Hugging Face Transformers)
├─ requirements.txt            # Dependências do projeto
└─ README.md                   # Documentação do projeto


```