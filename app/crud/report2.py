from sqlalchemy.orm import Session
from app.models.transaction3 import Transaction
from sqlalchemy import func

def generate_report(db: Session, user_id: int):
    income = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.transaction_type == "income", Transaction.owner_id == user_id)\
        .scalar() or 0

    expense = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.transaction_type == "expense", Transaction.owner_id == user_id)\
        .scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }