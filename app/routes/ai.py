from fastapi import APIRouter
from app.schemas.request import PromptRequest
from app.services.ai_service import ask_ai

router = APIRouter()

@router.post("/ask")
def ask(request: PromptRequest):
    response = ask_ai(request.prompt)
    return {"response": response}