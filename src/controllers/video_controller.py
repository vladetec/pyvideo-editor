from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from views.video_view import render_home
import shutil
from pathlib import Path

router = APIRouter()
UPLOAD_DIR = Path("static")
PROCESSED_DIR = UPLOAD_DIR / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/")
async def upload_video(request: Request, file: UploadFile = File(...), start_time: str = Form(...), end_time: str = Form(...)):
    try:
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        start_time_seconds = int(start_time)
        end_time_seconds = int(end_time)
        
        # Simular edição de vídeo
        output_file_name = f"edited_{file.filename}"
        output_file = PROCESSED_DIR / output_file_name
        shutil.copy(file_path, output_file)  # Simule a cópia para o arquivo processado

        return {"filename": file.filename, "start_time": start_time, "end_time": end_time, "output_file_url": f"/static/processed/{output_file_name}"}
    except Exception as e:
        return render_home(request, error=str(e))
