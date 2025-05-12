# 💊 MediGuide — AI Assistant for Drug Information

MediGuide is a lightweight, local **RAG (Retrieval-Augmented Generation)** app that lets users ask natural language questions about common medications and receive helpful answers based on trusted medical documents.

🚀 Built in one day to demonstrate applied NLP, LangChain, and LLM deployment skills.

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

---

## 🗂️ Project Structure

```
MediGuide/
├── app/
│   └── main.py                # FastAPI app
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
├── venv/                      # Virtual environment (should be ignored)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add drug PDFs to the `data/` folder

### 3. Build vector index
```bash
python rag/ingest.py
```

### 4. Start the app
Make sure Ollama is running (`ollama run mistral` or similar)

```bash
uvicorn app.main:app --reload
```

### 5. Ask questions (via cURL or Postman)
```bash
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the side effects of ibuprofen?"}'
```

---

## 🔍 Example Query

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

## 🎯 Why This Project

- ✅ Demonstrates real-world use of LangChain + LLMs
- ✅ Hands-on with embeddings, vector search, and local LLMs
- ✅ Production-friendly design (can easily be expanded or deployed)

---

## 🧠 Future Improvements

- Add user upload support (dynamic RAG)
- Switch FAISS to Chroma or Pinecone for scalability
- Add Streamlit UI
- Improve LLM summarization formatting
- Deploy with Docker or Hugging Face Spaces

---

## 👩‍💻 Author

**Salma Ouardi**  

---

## 📄 License

MIT License — free to use, adapt, or improve.
