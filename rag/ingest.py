""" 
What should be done:
1. Extract text from the PDFs
2. Split into chunks
3. Embed them
4. Store the embeddings in a vector db (Faiss)
"""

# 1. Import the required libraries.
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# 2. Load all PDFs from the data/ folder.
# 3. Extract the text usiing a PDF loader.

def load_docs(doc_path:str):
      docs = []
      for file in os.listdir(doc_path):
            if file.endswith(".pdf"):
                  loader = PyPDFLoader(os.path.join(doc_path, file))
                  docs.extend(loader.load())
      return docs

# 4. Split the text into small overlapping chunks (helps with recall).

def chunk_docs(docs:list):
      splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
      chunks = splitter.split_documents(docs)
      return chunks

# 5. Convert each chunk into an embedding using a sentence transformer.
# 6. Store the chunks + embeddings in FAISS and save the index to the disk.
def create_vectorstore(chunks, persist_dir="faiss_index"):
      embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
      vectorstore = FAISS.from_documents(chunks, embeddings)
      vectorstore.save_local(persist_dir)
      print(f"Saved index to {persist_dir}")
      
if __name__ == "__main__":
      docs = load_docs("../data")
      chunks = chunk_docs(docs)
      create_vectorstore(chunks)
      

