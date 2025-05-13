from fastapi import FastAPI, Request
from pydantic import BaseModel
from rag.rag_chain import get_rag_chain

app = FastAPI()
qa_chain = get_rag_chain()

class Question(BaseModel):
      query : str
      

@app.get("/")
def root():
    return {"status": "MediGuide is running 🚀"}

      
@app.post('/ask')
def ask_question(q: Question):
      result = qa_chain.invoke({"query": q.query})
      return {
            "answer": result["result"],
            "sources": [doc.page_content for doc in result["source_documents"]]
            }