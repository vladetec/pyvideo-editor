from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

def render_home(request: Request, error: str = None):
    return templates.TemplateResponse("home.html", {"request": request, "error": error})
