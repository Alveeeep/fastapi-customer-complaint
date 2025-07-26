FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -d /home/app app && \
    mkdir -p /home/app/.cache/uv && \
    chown -R 1000:1000 /home/app

COPY --chown=1000:1000 pyproject.toml uv.lock ./
RUN uv venv
RUN uv sync --locked

RUN mkdir -p /app/database/data /app/logs && \
    chown -R 1000:1000 /app && \
    chmod -R 775 /app/database /app/logs

ENV PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/home/app/.cache/uv \
    PATH="/home/app/.local/bin:${PATH}"

COPY --chown=1000:1000 . /app

WORKDIR /app

RUN touch /app/logs/bot.log /app/database/data/clients.db && \
    chmod 664 /app/logs/bot.log /app/database/data/clients.db

USER 1000:1000

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]