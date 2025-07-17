from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base


class Complaint(Base):
    text: Mapped[str]
    status: Mapped[str] = mapped_column(default='open')
    sentiment: Mapped[str]
    category: Mapped[str] = mapped_column(default='другое')
