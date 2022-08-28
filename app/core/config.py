from functools import lru_cache
from typing import Any, Dict, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Hold app's Settings

    Set environment variables with the same name to override the values.
    e.g: LOG_LEVEL=DEBUG will override log_level
    """

    app_name: str = "fastapipoc"
    app_version: str = "0.0.1"

    # logger
    loggers: List[str] = ["uvicorn.error", "uvicorn.access"]
    log_level: str = "INFO"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "version": self.app_version,
            "name": self.app_name,
        }


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Returns new Settings instance
    """
    return Settings()
