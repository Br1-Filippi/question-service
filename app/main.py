from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from runner import run_code

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

# Routes

@app.post("/")
def read_root():
    return {"message": "Welcome to the Question Bank Generator API"}


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