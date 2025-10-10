"""API router that bundles all v1 endpoints."""

from fastapi import APIRouter

from app.api.v1.endpoints import background

api_router = APIRouter()
api_router.include_router(background.router, prefix="/background")
