from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import load_llm

def format_docs(docs):
    return "\n\n".join(
        f"Source: {doc.metadata.get('title', 'Unknown')} | "
        f"Page: {doc.metadata.get('page_label', 'N/A')}\n"
        f"{doc.page_content}"
        for doc in docs
    )

def run_rag(query, retriever):
    docs = retriever.invoke(query)
    context = format_docs(docs)

    prompt = ChatPromptTemplate.from_template("""
You are a legal assistant.
Answer the question strictly using the context below.
If the answer is not present, say "Not found in the documents".

Context:
{context}

Question:
{question}
""")

    chain = prompt | load_llm() | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": query
    })

    citations = {
        f"{doc.metadata.get('title')} - Page {doc.metadata.get('page_label')}"
        for doc in docs
    }

    return answer, citations
