from app.dao.base import BaseDAO
from app.models.complaints import Complaint


class AppointmentsDAO(BaseDAO[Complaint]):
    model = Complaint