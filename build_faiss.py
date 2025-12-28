# build_faiss.py

from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import create_vectorstore

# 1️⃣ Load PDFs
docs = load_documents("data/legal_pdfs")
print(f"Loaded {len(docs)} PDFs")

# 2️⃣ Split into chunks
chunks = split_documents(docs)
print(f"Created {len(chunks)} chunks")

# 3️⃣ Create FAISS index
vectorstore = create_vectorstore(chunks)
print("✅ FAISS index created in 'faiss_index/' folder")
