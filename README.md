# ⚖️ AI Paralegal

AI Paralegal is an intelligent legal research assistant designed to support lawyers and law firms in handling large volumes of cases efficiently. The system can be customized using a firm’s own historical and ongoing case documents, enabling context-aware and firm-specific legal assistance.

By leveraging advanced document retrieval and reasoning, AI Paralegal provides accurate, grounded responses to legal queries, significantly reducing research time and improving turnaround for clients. Every answer is accompanied by source citations, allowing lawyers to verify the origin of the information and make informed, defensible legal decisions.

The platform is built to scale with growing clientele, ensuring faster insights, improved consistency in legal research, and seamless access to firm-owned knowledge.
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
