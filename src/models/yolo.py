"""Yolo model for detection"""
import io
from typing import List
from PIL import Image
from ultralytics import YOLO
from src.models.base import BaseSignDetector
from src.config import settings
from src.constants import YOLO_PATH


class YOLOSignDetector(BaseSignDetector):
    """Class for sign detection using YOLO"""

    def __init__(self):
        self.model = YOLO(YOLO_PATH)

    def recognize_signs(self, image: bytes) -> List[str]:
        """
        Generates id list with YOLO model
        """
        sign_id_list = []
        yolo_image = Image.open(io.BytesIO(image))
        found_signs = self.model.predict(yolo_image)[0]
        for box in found_signs.boxes:
            prob = round(box.conf[0].item(), 2)
            if prob > settings.prob_threshold:
                class_id = box.cls[0].item()
                sign_id = found_signs.names[class_id]
                sign_id_list.append(sign_id)
        return list(set(sign_id_list))
