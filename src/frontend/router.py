"""Endpoints"""
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from src.constants import TEMPLATES_PATH, RECOGNIZABLE_SIGNS

router = APIRouter(prefix="")
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """
    Gets homepage
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "signs": RECOGNIZABLE_SIGNS}
    )
