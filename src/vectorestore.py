from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)

def load_vectorstore(path="faiss_index"):
    embeddings = get_embeddings()
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
