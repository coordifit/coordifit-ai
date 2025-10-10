"""Domain logic for background removal operations."""

from io import BytesIO

from PIL import Image
from rembg import remove


class BackgroundRemovalError(Exception):
    """Raised when a background removal operation fails."""


def remove_background(image_bytes: bytes) -> bytes:
    """Remove the background from the provided image and return PNG bytes."""
    try:
        result_bytes = remove(image_bytes)
    except Exception as exc:
        raise BackgroundRemovalError("Failed to remove background") from exc

    try:
        with Image.open(BytesIO(result_bytes)) as processed_image:
            buffered = BytesIO()
            processed_image.convert("RGBA").save(buffered, format="PNG")
    except Exception as exc:
        raise BackgroundRemovalError("Failed to process output image") from exc

    return buffered.getvalue()
