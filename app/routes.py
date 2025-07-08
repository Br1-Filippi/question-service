from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from .models import CodeRequest
from .runner import run_code

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Pudiste comunicarte con el servicio de generación de banco de preguntas :3 ¡Bienvenido!"}

@router.post("/run-code",)
def generate_question_bank(request: CodeRequest):
    result = run_code(request.code)
    if result.startswith("ERROR"):
        raise HTTPException(status_code=400, detail=result)
    return {"message": "El código se ejecutó correctamente"}