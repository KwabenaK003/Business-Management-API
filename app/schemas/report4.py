from pydantic import BaseModel

class FinancialReport(BaseModel):
    total_income: float
    total_expense: float
    balance: float