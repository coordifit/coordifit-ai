from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.api import api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title="CoordiFit AI API", version="1.0.0")

origins = settings.allowed_origins_list or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
