# ⚖️ Legal Document Retrieval using RAG (HuggingFace)

A Retrieval-Augmented Generation system for querying legal documents using
FAISS + HuggingFace embeddings + FLAN-T5.

## Features
- PDF-based legal search
- Semantic chunk retrieval
- Citation-aware answers
- Fully local LLM (no OpenAI)
- Streamlit UI

## Tech Stack
- LangChain
- HuggingFace Transformers
- FAISS
- Streamlit

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
