from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from .models import CodeRequest
from .runner import run_code

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Pudiste comunicarte con el servicio de generación de banco de preguntas :3 ¡Bienvenido!"}

@router.post("/generate-xml")
def generate_question_bank(request: CodeRequest):
    output_path = run_code(request.code)
    if output_path.startswith("ERROR"):
        raise HTTPException(status_code=400, detail=output_path)
    return FileResponse(
        output_path,
        filename="banco_moodle.xml",
        media_type="application/xml"
    )