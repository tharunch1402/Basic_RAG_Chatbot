from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from rag.rag_chain import ask_question

app = FastAPI(title="Basic RAG Chatbot API")


class AskRequest(BaseModel):
    '''What the user sends'''
    question: str = Field(..., min_length=3, examples=["What is this paper about?"])


class AskResponse(BaseModel):
    '''What the API sends back'''
    answer: str
    pages: list[int]


@app.get("/health")
def health():
    '''Check the API is running'''
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    '''Answer a question about the ingested PDF'''
    try:
        result = ask_question(request.question)
    except FileNotFoundError as error:
        # Vector DB not built yet
        raise HTTPException(status_code=503, detail=str(error)) from error

    return AskResponse(answer=result["answer"], pages=result["pages"])