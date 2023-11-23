"""Base class for detection"""
from typing import List
from abc import ABC, abstractmethod


class BaseSignDetector(ABC):
    """
    Base class for detection
    """

    @abstractmethod
    def recognize_signs(self, image: bytes) -> List[int]:
        """
        Detects signs on image
        """
        raise NotImplementedError(
            "This method should be implemented in child class"
        )
