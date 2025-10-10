from fastapi import APIRouter

from app.api.v1.endpoints import remove

api_router = APIRouter()
api_router.include_router(remove.router, prefix="/background", tags=["background"])
