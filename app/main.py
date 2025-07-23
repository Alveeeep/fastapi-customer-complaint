from fastapi import FastAPI
from app.config import settings
from contextlib import asynccontextmanager
from app.routers.complaints import router as complaints_router
from app.database.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(settings.BASE_DIR)
    await create_tables()
    print("База готова к работе")
    yield
    print("Приложение завершает работу (данные сохранены)")


app = FastAPI(lifespan=lifespan)
app.include_router(complaints_router)
