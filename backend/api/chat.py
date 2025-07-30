# backend/api/chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from backend.rag.analyzer import analyze_vulnerabilities

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: ChatRequest):
    result = analyze_vulnerabilities(request.question)
    return {"answer": result}
