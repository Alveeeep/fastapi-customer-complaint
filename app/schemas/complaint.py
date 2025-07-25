from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ComplaintBaseResponse(BaseModel):
    status: str = 'open'
    sentiment: str

    model_config = ConfigDict(from_attributes=True)


class ComplaintFullResponse(ComplaintBaseResponse):
    category: str


class ComplaintPost(BaseModel):
    text: str


class ComplaintCreate(ComplaintBaseResponse, ComplaintPost):
    category: str = "другое"


class ComplaintUpdateFilter(BaseModel):
    id: int


class ComplaintUpdateValue(BaseModel):
    category: str | None = None
    status: str | None = None


class ComplaintDTO(ComplaintCreate):
    id: int
    timestamp: datetime
