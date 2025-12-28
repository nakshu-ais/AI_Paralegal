from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings
import os
import json

FAISS_INDEX_PATH = "faiss_index"

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Create folder if it doesn't exist
    if not os.path.exists(FAISS_INDEX_PATH):
        os.makedirs(FAISS_INDEX_PATH)

    # Save FAISS index to disk
    vectorstore.save_local(FAISS_INDEX_PATH)

    # Save metadata for reference
    metadata = [doc.metadata for doc in chunks]
    with open(os.path.join(FAISS_INDEX_PATH, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ FAISS index saved in '{FAISS_INDEX_PATH}'")
    return vectorstore


def load_vectorstore(path=FAISS_INDEX_PATH):
    embeddings = get_embeddings()
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
