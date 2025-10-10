from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Background Removal API"
    api_v1_str: str = "/api/v1"
    allowed_origins: List[str] = ["*"]


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""

    return Settings()
