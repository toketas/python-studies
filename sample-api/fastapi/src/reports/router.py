from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .use_cases import create_report
from ..core.dependencies import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def read_reports():
    return [{"title": "Rick"}, {"title": "Morty"}]


from pydantic import BaseModel

class Report(BaseModel):
    title: str

    class Config:
        orm_mode = True

@router.post("/create", response_model=Report)
def add_report(report_in: Report, db: Session = Depends(get_db)):
    report = create_report(db, report_in)
    print(report)
    return report
