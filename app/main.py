from fastapi import FastAPI
from app.config import settings
from contextlib import asynccontextmanager
from app.routers.complaints import router as complaints_router
from app.database.db import create_tables
from loguru import logger

logger.add(
    "logs/bot.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    logger.info("База готова к работе")
    yield
    logger.info("Приложение завершает работу (данные сохранены)")


app = FastAPI(lifespan=lifespan)
app.include_router(complaints_router)
