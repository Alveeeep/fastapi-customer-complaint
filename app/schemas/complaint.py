from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ComplaintCreate(BaseModel):
    text: str
    status: str = 'open'
    sentiment: str
    category: str = 'другое'


class ComplaintDTO(ComplaintCreate):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
