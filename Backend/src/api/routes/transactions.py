from fastapi import APIRouter
from src.api.schemas import Transaction
from src.api.services.data_service import get_transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=list[Transaction])
def transactions():
    return get_transactions()