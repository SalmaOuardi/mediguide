"""
Load the saved vector database and connect it to a 
local LLM (via ollama) to create a quesion-answering chain
"""
import logging
from rich.logging import RichHandler

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
import os

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger("mediGuide") 

#here too and and her

# 1. Load the FAISS vector store from disk.
# 2. Re-initialize the same embedding model.
# 3. Wrap the vector store in a Retriever.
# 4. Load the LLM using ChatOllama(model='llama3') or another model.
# 5. Create a RetrievalQA chain using langchain.

def get_rag_chain():
    logger.info("📦 Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    logger.info("📚 Loading FAISS vector store...")
    vectorstore = FAISS.load_local("rag/faiss_index", embeddings, allow_dangerous_deserialization=True)

    logger.info("🔍 Building retriever...")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    logger.info("🧠 Loading LLM (Ollama)... This may take a few seconds ⏳")
    llm = ChatOllama(model="llama3")

    logger.info("🔗 Creating RAG QA chain...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    logger.info("✅ RAG chain is ready.")
    return qa_chain