"""Domain logic for background removal operations (sharp mode)."""

from io import BytesIO
from PIL import Image
from rembg import remove


class BackgroundRemovalError(Exception):
    """Raised when a background removal operation fails."""


def remove_background(image_bytes: bytes) -> bytes:
    """Remove the background from the provided image and return PNG bytes (sharp preset)."""
    try:
        # ⚙️ sharp preset 적용 — 옷 상품 등록용, 경계가 또렷하게
        result_bytes = remove(
            image_bytes,
            alpha_matting=False,    # 경계 흐림 제거
            post_process_mask=True  # 잔여 픽셀/노이즈 제거
        )
    except Exception as exc:
        raise BackgroundRemovalError("Failed to remove background") from exc

    try:
        with Image.open(BytesIO(result_bytes)) as processed_image:
            buffered = BytesIO()
            processed_image.convert("RGBA").save(buffered, format="PNG")
    except Exception as exc:
        raise BackgroundRemovalError("Failed to process output image") from exc

    return buffered.getvalue()
