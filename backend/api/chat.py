from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio

from backend.rag.analyzer import analyze_vulnerabilities  # this might need to be async

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        # If analyze_vulnerabilities is async:
        if asyncio.iscoroutinefunction(analyze_vulnerabilities):
            result = await analyze_vulnerabilities(request.question)
        else:
            result = analyze_vulnerabilities(request.question)
        return {"answer": result}
    except Exception as e:
        print(f"Error analyzing vulnerabilities: {e}")
        raise HTTPException(status_code=500, detail="Internal error analyzing vulnerabilities")
@router.post("/chat")
async def chat(request: ChatRequest):
    result = await analyze_vulnerabilities(request.question)
    return {"answer": result}
