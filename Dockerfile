FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --chown=app:app pyproject.toml uv.lock ./

RUN uv venv
RUN uv sync --locked

RUN groupadd -r appgroup && useradd -r -g appgroup app && \
    mkdir -p /home/app/.cache/uv && \
    chown -R app:appgroup /home/app

RUN mkdir -p /app/database/data && \
    mkdir -p /app/logs && \
    chown -R app:appgroup /app

ENV PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/home/app/.cache/uv \
    PATH="/home/app/.local/bin:${PATH}"

COPY --chown=app:appgroup . /app

WORKDIR /app

USER app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]