from sqlalchemy.orm import Session
from app.models.transaction3 import Transaction
from app.schemas.transaction4 import TransactionCreate

def create_transaction(db: Session, data: TransactionCreate, user_id: int):
    tx = Transaction(**data.model_dump(), owner_id=user_id)
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.owner_id == user_id).all()