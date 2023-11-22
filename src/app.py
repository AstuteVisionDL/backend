"""Application"""
from fastapi import FastAPI

from src.api.router import router

app = FastAPI(
    title="Sign Detector Backend",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
