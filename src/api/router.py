"""Endpoints"""
from fastapi import APIRouter

from src.api.schemas import HealthCheckResponse

router = APIRouter()


@router.get("/health", tags=["Health"], response_model=HealthCheckResponse)
async def health_check():
    """
    Checks if the service is working
    """
    return HealthCheckResponse()
