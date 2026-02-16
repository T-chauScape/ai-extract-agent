# app/controllers/translation_controller.py
from fastapi import APIRouter, HTTPException

from app.views.schema.response import ExtractRequest, ExtractResponse
from app.views.schema.schema import OutputSchema 
from app.service.extractor_service import extract_transactions

router = APIRouter()

@router.post("/extract", response_model=ExtractResponse)
async def handle_extraction(request: ExtractRequest):
    try:
        print("Starting extraction process...")
        result = extract_transactions(request.texto_completo)
        return ExtractResponse(message="Extraction completed successfully.", result=result)
    except Exception as e:
        print(f"Error during extraction: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during extraction.")
