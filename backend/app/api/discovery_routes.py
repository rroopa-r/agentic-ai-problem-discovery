from fastapi import APIRouter, UploadFile, File
from app.tools.pdf_processor import extract_text_from_pdf
from app.services.graph_service import run_discovery_pipeline
import shutil
import os

router = APIRouter()

@router.post("/upload-pdf")
async def handle_pdf(file: UploadFile = File(...)):
    # Save file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 1. Extract text
    text_content = extract_text_from_pdf(temp_path)
    
    # 2. Run through LangGraph
    result = run_discovery_pipeline(text_content)
    
    # Cleanup
    os.remove(temp_path)
    
    return result