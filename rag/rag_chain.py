"""
Load the saved vector database and connect it to a 
local LLM (via ollama) to create a quesion-answering chain
"""
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
import os

# 1. Load the FAISS vector store from disk.
# 2. Re-initialize the same embedding model.
# 3. Wrap the vector store in a Retriever.
# 4. Load the LLM using ChatOllama(model='llama3') or another model.
# 5. Create a RetrievalQA chain using langchain.

def get_rag_chain():
      
      embeddings = HuggungFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
      vectorstore = FAISS.load_local("faiss_index", embeddings)
      retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
      
      llm = ChatOllama(model="llama3")
      
      qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
      )
      
      return qa_chain