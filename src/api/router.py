"""Endpoints"""
from fastapi import APIRouter
from fastapi.websockets import WebSocket, WebSocketDisconnect
from loguru import logger

from src.models.base import BaseSignDetector
from src.models.preprocessing import from_text_image_url_to_bytes
from src.api.schemas import HealthCheckResponse

router = APIRouter()


@router.get("/health", tags=["Health"], response_model=HealthCheckResponse)
async def health_check():
    """
    Checks if the service is working
    """
    logger.info("Health checking")
    return HealthCheckResponse()


@router.websocket("/ws")
async def process_image(websocket: WebSocket):
    """
    Detects signs on image from client and return identifiers
    Gets model from application state (loading on startup)
    """
    sign_detector: BaseSignDetector = websocket.app.state.sign_detector
    await websocket.accept()
    logger.info(f"Websocket start with client ({websocket.client})")
    try:
        while True:
            text_image_url = await websocket.receive_text()
            image = from_text_image_url_to_bytes(text_image_url)
            sign_id_list = sign_detector.recognize_signs(image)
            await websocket.send_json({"items": sign_id_list})
    except WebSocketDisconnect:
        logger.warning(f"Client ({websocket.client}) has disconnected")
    except Exception as ex:
        logger.error(f"Unhandled error: {ex}")
        await websocket.close()
