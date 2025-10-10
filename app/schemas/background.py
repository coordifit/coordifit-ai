"""Pydantic schemas for background removal endpoints."""

from pydantic import BaseModel, Field


class BackgroundRemovalResponse(BaseModel):
    """Response payload for successful background removal."""

    status: str = Field(default="success", description="Processing status")
    result_image: str = Field(
        ..., description="Base64 encoded PNG image with transparent background"
    )
