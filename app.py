import streamlit as st
from src.vectorstore import load_vectorstore
from src.retriever import get_retriever
from src.rag_chain import run_rag

st.set_page_config("Legal RAG Assistant", layout="wide")
st.title("⚖️ AI Paralegal")

@st.cache_resource
def load_db():
    return load_vectorstore()

vectorstore = load_db()
retriever = get_retriever(vectorstore)

query = st.text_input("Ask a legal question:")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching legal documents of the firm..."):
            answer, citations = run_rag(query, retriever)

        st.subheader("📌 Answer")
        st.write(answer)

        st.subheader("📄 Citations")
        for c in citations:
            st.write("-", c)
    else:
        st.warning("Please enter a question")
