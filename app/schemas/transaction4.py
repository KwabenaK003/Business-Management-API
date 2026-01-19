from pydantic import BaseModel

class TransactionCreate(BaseModel):
    description: str
    amount: float
    transaction_type: str

class TransactionOut(TransactionCreate):
    id: int

    class Config:
        # orm_mode = True
        from_attribute = True