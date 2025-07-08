import subprocess
import uuid
import os
from app.config import settings

def run_code(code: str) -> str:
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    uid = uuid.uuid4().hex
    script_path = os.path.join(settings.UPLOAD_DIR, f"user_{uid}.py")
    output_path = os.path.join(settings.UPLOAD_DIR, "preguntas_cloze_moodle.xml")

    with open(script_path, "w") as f:
        f.write(code)

    try:
        subprocess.run(
            ["python3", script_path],
            cwd=settings.UPLOAD_DIR,
            check=True,
            timeout=10
        )
    except subprocess.CalledProcessError as e:
        return f"ERROR: Código falló — {e}"
    except subprocess.TimeoutExpired:
        return "ERROR: Tiempo de ejecución excedido"

    return output_path if os.path.exists(output_path) else "ERROR: No se generó archivo"
