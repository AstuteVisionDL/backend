"""FastAPI dependency for getting actual sign detector model"""
from src.models.random import RandomSignDetector
from src.models.base import BaseSignDetector


def get_actual_sign_detector() -> BaseSignDetector:
    """Dependency for returning actual detector"""
    return RandomSignDetector()


def get_test_sign_detector() -> BaseSignDetector:
    """Dependency for returning detector for testing"""
    return RandomSignDetector()
