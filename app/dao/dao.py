from app.dao.base import BaseDAO
from app.models.complaints import Complaint
from datetime import datetime, timedelta
from loguru import logger
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


class ComplaintsDAO(BaseDAO[Complaint]):
    model = Complaint

    async def find_last_hour_open(self):
        try:
            one_hour_ago = datetime.now() - timedelta(hours=1)
            logger.info(
                f"Поиск записей {self.model.__name__} за последний час (с {one_hour_ago})"
            )
            query = select(self.model).where((self.model.timestamp >= one_hour_ago) & (self.model.status == 'open'))
            result = await self._session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} записей за последний час.")
            return records
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записей за последний час: {e}")
            raise
