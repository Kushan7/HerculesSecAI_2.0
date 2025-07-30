from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os
# Load variables from .env
load_dotenv()
print("Credential path:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

# Now the GOOGLE_APPLICATION_CREDENTIALS will be available to google.auth




BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path to /backend/rag/
CORPUS_DIR = os.path.join(BASE_DIR, "..", "data", "corpus")
CORPUS_DIR = os.path.normpath(CORPUS_DIR)

CHROMA_DIR = "/chroma_db"

def embed_documents():
    print("📄 Loading documents...")
    all_docs = []
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(CORPUS_DIR, filename))
            docs = loader.load()
            all_docs.extend(docs)

    if not all_docs:
        print("❌ No .txt files found in corpus directory.")
        return

    print(f"✅ Loaded {len(all_docs)} document(s)")

    print("✂️ Splitting documents into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(all_docs)
    print(f"✅ Created {len(chunks)} chunks")

    print("🧠 Generating embeddings using Gemini...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    print("📦 Storing embeddings in ChromaDB...")
    db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_DIR)


    print("✅ Done! Embeddings saved to ChromaDB.")

if __name__ == "__main__":
    embed_documents()
