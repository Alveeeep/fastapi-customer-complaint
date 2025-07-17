from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ComplaintBaseResponse(BaseModel):
    status: str = 'open'
    sentiment: str


class ComplaintFullResponse(ComplaintBaseResponse):
    category: str


class ComplaintPost(BaseModel):
    text: str


class ComplaintCreate(ComplaintBaseResponse):
    category: str = "другое"


class ComplaintDTO(ComplaintCreate):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
