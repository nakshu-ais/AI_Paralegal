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

##Demo
<img width="1373" height="745" alt="Screenshot 2025-12-28 192242" src="https://github.com/user-attachments/assets/918eae64-ad8c-48dd-8525-a72d673170a9" />
<img width="1373" height="745" alt="Screenshot 2025-12-28 192242" src="https://github.com/user-attachments/assets/c409edaa-3a39-49da-b56f-a20919553650" />
<img width="1066" height="893" alt="Screenshot 2025-12-28 192409" src="https://github.com/user-attachments/assets/31af1158-b11c-4a1f-8588-68a3b74443d7" />



