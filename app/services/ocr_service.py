"""OCR service for text extraction from images using EasyOCR."""

import easyocr
import numpy as np
import cv2
from typing import List, Dict, Any


class OCRError(Exception):
    """Raised when an OCR operation fails."""

reader = easyocr.Reader(['ko', 'en'], gpu=False, download_enabled=False, model_storage_directory="/root/.EasyOCR")


def extract_text_from_image(image_bytes: bytes) -> List[Dict[str, Any]]:
    """이미지 바이트에서 텍스트 추출"""
    try:
        # 바이트를 numpy 배열로 변환
        np_image = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
        
        if image is None:
            raise OCRError("Failed to decode image")
        
        # EasyOCR로 텍스트 추출
        results = reader.readtext(image)
        
        # 결과를 구조화된 형태로 변환
        texts = []
        for (bbox, text, conf) in results:
            texts.append({
                "text": text,
                "confidence": float(conf)
            })
        
        return texts
        
    except Exception as exc:
        raise OCRError(f"Failed to extract text from image: {str(exc)}") from exc