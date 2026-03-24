from fastapi import FastAPI
from app.routes.ai import router as ai_router
from app.routes.pdf import router as pdf_router

app = FastAPI(title="AI Business Assistant")

app.include_router(ai_router, prefix="/ai")

app.include_router(pdf_router, prefix="/pdf")