from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..core.database import Base


class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))

report = Reports
