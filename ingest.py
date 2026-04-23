from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading PDF...")
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
vectorstore = FAISS.from_documents(documents, embeddings)

vectorstore.save_local("faiss_index")
print("✅ PDF ingested and vector index created")
