from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.services.ai_service import analyze_document

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()

    text = extract_text_from_pdf(contents)

    result = analyze_document(text)

    return {
        "filename": file.filename,
        "data": result
    }