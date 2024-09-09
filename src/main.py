from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from controllers import video_controller
from views.video_view import render_home

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/static/processed", StaticFiles(directory="static/processed"), name="processed")

app.include_router(video_controller.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return render_home(request)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)