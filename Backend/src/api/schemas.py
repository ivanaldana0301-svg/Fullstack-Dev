from pydantic import BaseModel

class Transaction(BaseModel):
    date: str
    transaction_id: int
    amount: float
    price: float
    transaction_value_usd: float
    category: str