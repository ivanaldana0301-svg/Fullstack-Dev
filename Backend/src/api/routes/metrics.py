from fastapi import APIRouter
from src.api.services.data_service import get_metrics

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.get("/")
def metrics():
    return get_metrics()