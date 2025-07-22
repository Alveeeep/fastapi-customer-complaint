from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.dao import ComplaintsDAO
from app.utils.external_api import analyze_sentiment
from app.utils.ai_api import get_chatgpt_response
from typing import Union, reveal_type
from app.dependencies.dao_dep import (
    get_session_with_commit,
)
from app.schemas.complaint import ComplaintCreate, ComplaintDTO, ComplaintPost, ComplaintFullResponse, \
    ComplaintBaseResponse, ComplaintUpdateFilter, ComplaintUpdateValue

router = APIRouter(tags=["Customers complaints"])


@router.post("/complaint", response_model=Union[ComplaintFullResponse, ComplaintBaseResponse])
async def create_appointment(
        complaint: ComplaintPost,
        session: AsyncSession = Depends(get_session_with_commit), ):
    sentiment = await analyze_sentiment(complaint.text)
    data = {'text': complaint.text, 'sentiment': sentiment}
    complaint_to_add = ComplaintCreate(**data)
    added_complaint = await ComplaintsDAO(session=session).add(complaint_to_add)
    category = await get_chatgpt_response(complaint.text)
    if category != 'другое':
        added_complaint = await ComplaintsDAO(session=session).update(ComplaintUpdateFilter(id=added_complaint.id),
                                                    ComplaintUpdateValue(category=category))
        return ComplaintFullResponse.model_validate(added_complaint)
    else:
        return ComplaintBaseResponse.model_validate(added_complaint)

