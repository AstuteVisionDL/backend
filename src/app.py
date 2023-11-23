"""Application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger

from src.api.router import router


@asynccontextmanager
async def start(application: FastAPI):  # pylint: disable=unused-argument
    """
    Executes start actions
    """
    logger.info("Start application")
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
