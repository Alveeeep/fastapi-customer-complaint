from app.dao.base import BaseDAO
from app.models.complaints import Complaint


class ComplaintsDAO(BaseDAO[Complaint]):
    model = Complaint