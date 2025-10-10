"""Schemas for background removal endpoints."""

from typing import Literal
from pydantic import BaseModel, Field

class BackgroundRemovalData(BaseModel):
    result_image: str = Field(..., alias="resultImage", description="Base64 encoded PNG image")

    class Config:
        allow_population_by_field_name = True


class BackgroundRemovalResponse(BaseModel):
    status: Literal["success"] = Field("success")
    data: BackgroundRemovalData

    class Config:
        allow_population_by_field_name = True
