from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models


class Report(BaseModel):
    title: str

def create_report(db: Session, report: Report) -> Report:
    db_obj = models.report(
        title=report.title
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
