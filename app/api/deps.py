"""Reusable dependencies for API routes."""

from app.core.config import Settings, get_settings


def get_app_settings() -> Settings:
    """Return application settings for dependency injection."""

    return get_settings()
