# 💊 MediGuide — AI Assistant for Drug Information

MediGuide is a lightweight, local **RAG (Retrieval-Augmented Generation)** app that lets users ask natural language questions about common medications and receive helpful answers based on trusted medical documents.

🚀 Built in one day to demonstrate applied NLP, LangChain, and LLM deployment skills, now containerized using Docker for reproducibility and deployment. A Streamlit UI was added for a clean, accessible user experience with a professional medical theme.

---

## 📚 What It Does

> “Can I take ibuprofen while pregnant?”  
> “What are the side effects of amoxicillin?”  
> “Is paracetamol safe for children under 6?”

MediGuide uses a **local LLM (via Ollama)** + a **vector database (FAISS)** to:
- Load and chunk medical drug PDFs
- Search for the most relevant information
- Answer user queries using context-grounded responses

---

## 🛠️ Tech Stack

- **LangChain** — Framework for chaining LLMs + retrieval
- **Ollama** — Local LLMs (e.g., LLaMA 3, Mistral)
- **FAISS** — Fast vector similarity search
- **HuggingFace Sentence Transformers** — For embedding text
- **FastAPI** — Lightweight API for interaction
- **Streamlit** — UI for asking questions and receiving answers
- **Docker** — Portable app container

---

## 🗂️ Project Structure

```
MediGuide/
├── app/
│   ├── main.py                # FastAPI app
│   └── ui.py                  # Streamlit UI
├── data/
│   └── who_drug_data.pdf      # Source PDF
├── notebooks/                 # (Optional) Jupyter notebooks
├── rag/
│   ├── ingest.py              # PDF ingestion & indexing
│   ├── rag_chain.py           # RAG chain setup
│   └── faiss_index/
│       ├── index.faiss        # FAISS vector store
│       └── index.pkl
├── tests/                     # Future unit tests
├── .github/workflows/ci.yml  # GitHub Actions workflow
├── .streamlit/config.toml     # Custom dark mode theme
├── Dockerfile                 # For containerizing the app
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How to Run

### 🚀 Run with Docker (Recommended)
```bash
docker build -t mediguide .
docker run -p 8000:8000 mediguide
```

To mount your FAISS index:
```bash
docker run -p 8000:8000 -v $(pwd)/rag/faiss_index:/app/rag/faiss_index mediguide
```

### 🐍 Run Locally
```bash
pip install -r requirements.txt
python rag/ingest.py
uvicorn app.main:app --reload
```

---

### 🧪 Use the Streamlit UI

Make sure your FastAPI backend is running on port `8000`, then launch the UI:

```bash
streamlit run app/ui.py
```

You’ll get a clean healthcare-themed chatbot interface with:
- A query input
- A loading spinner
- A styled, dark-mode friendly response box
- A footer disclaimer

---

### 🔎 Query the API directly

```bash
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the side effects of ibuprofen?"}'
```

---

## 📬 Example Query

**Input:**
```json
{ "query": "Can I take ibuprofen if I have asthma?" }
```

**Output:**
```json
{
  "answer": "Ibuprofen should be used with caution in people with asthma..."
}
```

---

## 🔄 CI/CD Pipeline

A simple GitHub Actions workflow builds the Docker image and runs a smoke test to ensure the app starts cleanly.

---

## 🎯 Why This Project

- ✅ Demonstrates real-world use of LangChain + LLMs
- ✅ Dockerized for reproducibility and deployment
- ✅ Streamlit UI for friendly human interaction
- ✅ Ready for extension, deployment, and testing

---

## 👩‍💻 Author

**Salma Ouardi**

---

## 📄 License

MIT License — free to use, adapt, or improve.
