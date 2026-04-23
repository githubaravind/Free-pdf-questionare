# PDF RAG Chatbot 🤖📄

A **Retrieval-Augmented Generation (RAG)** application that allows users to query PDF documents using semantic search powered by **LangChain**, **HuggingFace embeddings**, and a **vector database**.

This project demonstrates end-to-end GenAI engineering: PDF ingestion, text chunking, embedding generation, vector indexing, and retrieval — all runnable **locally** on Windows.

---

## 🚀 Why this project matters

Recruiters and interviewers look for **hands-on GenAI experience**, not just theory. This project shows:

* Practical understanding of **RAG architectures**
* Experience with **LLM tooling (LangChain)**
* Knowledge of **vector embeddings & semantic search**
* Ability to debug real-world issues (PDF parsing, environments, dependencies)

---

## 🧠 Architecture Overview

1. Load and parse PDF documents
2. Split text into manageable chunks
3. Convert text chunks into vector embeddings
4. Store embeddings in a vector index
5. Retrieve relevant chunks for downstream Q&A

```
PDF → Text → Chunks → Embeddings → Vector Store → Query
```

---

## 🛠️ Tech Stack

* **Python 3.12**
* **LangChain**
* **HuggingFace Sentence Transformers** (`all-MiniLM-L6-v2`)
* **FAISS / Vector Index**
* **PyPDF**
* **VS Code (Windows)**

---

## 📂 Project Structure

```
pdf-rag-chatbot/
│── ingest.py           # PDF ingestion & vector creation
│── sample.pdf          # Input PDF document
│── .gitignore
│── README.md
│── venv/               # Virtual environment (ignored in Git)
```

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

---

### 2️⃣ Create & activate virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```powershell
pip install -r requirements.txt
```

(If `requirements.txt` is missing, install manually:)

```powershell
pip install langchain langchain-community sentence-transformers pypdf faiss-cpu
```

---

### 4️⃣ Add a PDF

Place any PDF file in the project root and rename it:

```
sample.pdf
```

---

### 5️⃣ Run PDF ingestion

```powershell
python ingest.py
```

✅ Expected output:

```
PDF ingested and vector index created
```

---

## 📸 Screenshots

Add screenshots to make recruiters engage with your repo:

1. Successful PDF ingestion
2. Vector creation output
3. Folder structure in VS Code

Create a folder:

```
screenshots/
```

Then reference them here:

```md
![Ingestion Output](screenshots/ingestion.png)
```

---

## 🧪 Future Enhancements

* Add conversational Q&A using LLMs
* Build Streamlit or FastAPI UI
* Support multiple PDFs
* Add metadata-based filtering
* Deploy on cloud (Azure / GCP)

---

## 👤 Author

**Sanjana Reddy**
AI / Data Engineer | GenAI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps others discover the work!
