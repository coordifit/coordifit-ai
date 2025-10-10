"""Utility helpers for background removal."""

from __future__ import annotations

import base64
import io
from typing import Union

from PIL import Image
from rembg import remove


def remove_background_from_image(data: bytes) -> str:
    """Remove the background from the provided image bytes.

    Returns:
        A base64 encoded PNG image with transparent background.
    """

    input_image = Image.open(io.BytesIO(data)).convert("RGBA")
    result: Union[bytes, Image.Image] = remove(input_image)

    if isinstance(result, Image.Image):
        buffer = io.BytesIO()
        result.save(buffer, format="PNG")
        result_bytes = buffer.getvalue()
    else:
        result_bytes = result

    return base64.b64encode(result_bytes).decode("utf-8")
