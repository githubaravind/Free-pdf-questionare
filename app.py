import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# ✅ NEW IMPORTS (local model)
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

load_dotenv()

st.set_page_config(page_title="PDF RAG Chatbot", layout="wide")
st.title("📄 Chat with your PDF (FREE - Local Model)")

# ✅ Load embeddings once
@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# ✅ Load LLM locally (NO API, NO ERRORS)
@st.cache_resource
def get_llm():
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=512
    )
    return HuggingFacePipeline(pipeline=pipe)

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    if st.button("Process PDF"):
        with st.spinner("Processing..."):
            loader = PyPDFLoader("temp.pdf")
            documents = loader.load()

            embeddings = get_embeddings()

            db = FAISS.from_documents(documents, embeddings)
            db.save_local("faiss_index")

            st.success("PDF processed successfully!")

# Ask question
query = st.text_input("Ask a question:")

if query:
    embeddings = get_embeddings()

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever()
    )

    answer = qa_chain.run(query)

    st.write("### 🤖 Answer:")
    st.write(answer)