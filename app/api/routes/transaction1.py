from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.transaction4 import TransactionCreate, TransactionOut
from app.crud.transaction2 import create_transaction, get_transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}", response_model=TransactionOut)
def add_transaction(user_id: int, tx: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, tx, user_id)

@router.get("/{user_id}", response_model=list[TransactionOut])
def list_transactions(user_id: int, db: Session = Depends(get_db)):
    return get_transactions(db, user_id)