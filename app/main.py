from fastapi import FastAPI
from app.routers.complaints import router as complaints_router


app = FastAPI()
app.include_router(complaints_router)
