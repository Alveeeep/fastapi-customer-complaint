FROM python:3.13-slim AS base

FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

RUN useradd -m -u 1001 app && \
    mkdir -p /app/{sqlite_data,logs} && \
    chmod -R 777 /app/logs && \
    chown -R app:app /app

WORKDIR /app

COPY --chown=app:app pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/home/app/.cache/uv \
    uv venv && \
    uv sync --frozen --no-install-project --no-dev

COPY --chown=app:app . .

RUN --mount=type=cache,target=/home/app/.cache/uv \
    uv sync --frozen --no-dev

FROM base

RUN useradd -m -u 1001 app && \
    mkdir -p /app/{sqlite_data,logs} && \
    chmod -R 777 /app/logs && \
    chown -R app:app /app

WORKDIR /app

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    LOG_DIR="/app/logs"

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]