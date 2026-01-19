from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.report4 import FinancialReport
from app.crud.report2 import generate_report

router = APIRouter(prefix="/reports", tags=["Reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=FinancialReport)
def financial_report(user_id: int, db: Session = Depends(get_db)):
    return generate_report(db, user_id)