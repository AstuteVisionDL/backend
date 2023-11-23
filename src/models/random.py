"""Random model for testing frontend"""
import random
from typing import List
from random import randint, sample
from src.models.base import BaseSignDetector
from src.constants import SIGN_ID_LIST


class RandomSignDetector(BaseSignDetector):
    """Class for random detection"""

    def __int__(self, random_seed=0):
        random.seed(random_seed)

    def recognize_signs(self, image: bytes) -> List[int]:
        """
        Generates randomly id list of signs on image
        """
        recognized_signs_count = randint(0, len(SIGN_ID_LIST))
        recognized_signs = sample(SIGN_ID_LIST, k=recognized_signs_count)
        return recognized_signs
