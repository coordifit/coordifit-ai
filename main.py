from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from rembg import remove
from PIL import Image
import base64
import io

app = FastAPI(title="Background Removal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="업로드된 파일이 이미지가 아닙니다.")

    try:
        contents = await file.read()
        input_image = Image.open(io.BytesIO(contents)).convert("RGBA")
        output_bytes = remove(input_image)

        if isinstance(output_bytes, Image.Image):
            output_buffer = io.BytesIO()
            output_bytes.save(output_buffer, format="PNG")
            result_data = output_buffer.getvalue()
        else:
            result_data = output_bytes

        encoded_image = base64.b64encode(result_data).decode("utf-8")

        return {
            "status": "success",
            "result_image": encoded_image,
        }
    except HTTPException:
        raise
    except Exception as exc:  # pylint: disable=broad-except
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(_, exc: Exception):  # pylint: disable=broad-except
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
        },
    )
