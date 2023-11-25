"""Settings of application"""
from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings


class ModeEnum(str, Enum):
    """
    Mode of application
    """

    TEST = "test"
    PRODUCTION = "prod"


class ApplicationSettings(BaseSettings):
    """
    Settings for application
    """

    mode: ModeEnum = Field(default="test", alias="MODE")
    port: int = Field(default=5000, alias="PORT")


settings = ApplicationSettings()
