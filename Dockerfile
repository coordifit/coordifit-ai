FROM python:3.10-slim

# 시스템 패키지(필요 최소만)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache

COPY . .

# Uvicorn 1 worker (메모리 아끼기)
ENV UVICORN_WORKERS=1 \
    HOST=0.0.0.0 \
    PORT=8000

EXPOSE 8000
CMD ["sh", "-c", "uvicorn main:app --host ${HOST} --port ${PORT} --workers ${UVICORN_WORKERS}"]
