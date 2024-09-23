from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime, String
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status = Column(String, default="in_process", nullable=False)
