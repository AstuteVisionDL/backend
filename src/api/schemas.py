"""Schemas for requests and responses"""
from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    """
    Response scheme for checking the health of the service
    """

    status: str = "ok"


class ErrorMessage(BaseModel):
    """
    Error response scheme
    """

    message: str
