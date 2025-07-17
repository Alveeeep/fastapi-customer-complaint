from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.dao import ComplaintsDAO
from typing import Union
from app.dependencies.dao_dep import (
    get_session_with_commit,
)
from app.schemas.complaint import ComplaintCreate, ComplaintDTO, ComplaintPost, ComplaintFullResponse, \
    ComplaintBaseResponse

router = APIRouter(tags=["Customers complaints"])


@router.post("/complaint", response_model=Union[ComplaintFullResponse, ComplaintBaseResponse])
async def create_appointment(
        complaint: ComplaintPost,
        session: AsyncSession = Depends(get_session_with_commit),):
    pass
    # added_complaint = await ComplaintsDAO(session=session).add(complaint)
    # if added_complaint.category == 'другое':
    #    return ComplaintBaseResponse()
