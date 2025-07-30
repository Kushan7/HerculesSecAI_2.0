# backend/rag/retriever.py

from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_context_docs(query: str, k: int = 5):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma(
        persist_directory="backend/rag/chroma_db",
        embedding_function=embedding
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(query)
    return docs
