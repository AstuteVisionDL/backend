"""Application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from src.api.router import router as api_router
from src.frontend.router import router as frontend_router
from src.models.dependencies import get_actual_sign_detector
from src.config import settings, ModeEnum
from src.constants import STATIC_PATH


@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Executes start actions
    """
    logger.info(f"Server has started in mode: {settings.mode}")
    application.state.sign_detector = get_actual_sign_detector()
    logger.info("Model loading was successful")
    yield


app = FastAPI(
    lifespan=lifespan if settings.mode == ModeEnum.PRODUCTION else None,
    title="Sign Detector Backend",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)
logger.add("logs.log")
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

app.include_router(api_router)
app.include_router(frontend_router)
