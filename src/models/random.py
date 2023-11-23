"""Random model for testing frontend"""
from typing import List
from random import randint, sample
from src.models.base import BaseSignDetector
from src.constants import SIGN_ID_LIST


# pylint: disable=too-few-public-methods
class RandomSignDetector(BaseSignDetector):
    """Class for random detection"""

    @staticmethod
    def recognize_signs(image: bytes) -> List[int]:
        """
        Generates randomly id list of signs on image
        """
        recognized_signs_count = randint(0, len(SIGN_ID_LIST))
        recognized_signs = sample(SIGN_ID_LIST, k=recognized_signs_count)
        return recognized_signs
