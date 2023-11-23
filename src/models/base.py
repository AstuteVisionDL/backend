"""Base class for detection"""
from abc import ABC, abstractmethod
from typing import List


class BaseSignDetector(ABC):  # pylint: disable=too-few-public-methods
    """
    Base class for detection
    """

    @staticmethod
    @abstractmethod
    def recognize_signs(image: bytes) -> List[int]:
        """
        Detects signs on image
        """
        raise NotImplementedError(
            "This method should be implemented in child class"
        )
