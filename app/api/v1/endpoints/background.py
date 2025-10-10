"""API endpoints for background removal operations."""

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.background import BackgroundRemovalResponse
from app.utils.background import remove_background_from_image

router = APIRouter(tags=["background"])


@router.post(
    "/remove-bg",
    response_model=BackgroundRemovalResponse,
    summary="Remove the background from an uploaded image",
)
async def remove_background(file: UploadFile = File(...)) -> BackgroundRemovalResponse:
    """Remove the background from the provided image."""

    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="업로드된 파일이 이미지가 아닙니다.")

    try:
        contents = await file.read()
        encoded_image = remove_background_from_image(contents)
        return BackgroundRemovalResponse(result_image=encoded_image)
    except HTTPException:
        raise
    except Exception as exc:  # pylint: disable=broad-except
        raise HTTPException(status_code=500, detail=str(exc)) from exc
