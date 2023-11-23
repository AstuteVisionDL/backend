"""Application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger

from src.api.router import router
from src.models.dependencies import get_actual_sign_detector


@asynccontextmanager
async def start(application: FastAPI):
    """
    Executes start actions
    """
    application.state.sign_detector = get_actual_sign_detector()
    logger.info("Model loading was successful")
    yield


app = FastAPI(
    lifespan=start,
    title="Sign Detector Backend",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)
logger.add("logs.log")


app.include_router(router)
