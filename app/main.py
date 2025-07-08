from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.runner import run_code

app = FastAPI()

#Cors
origins_raw = os.getenv("CORS_ORIGINS", "")
origins = [o.strip() for o in origins_raw.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class CodeRequest(BaseModel):
    code: str

# Routes

@app.get("/")
def read_root():
    return {"message": "Pudiste comunicarte con el servicio de generación de banco de preguntas :3 ¡Bienvenido!"}


@app.post("/generate-xml")
def generate_question_bank(request: CodeRequest):
    output_path = run_code(request.code)

    if output_path.startswith("ERROR"):
        raise HTTPException(status_code=400, detail=output_path)

    return FileResponse(
        output_path,
        filename="banco_moodle.xml",
        media_type="application/xml"
    )