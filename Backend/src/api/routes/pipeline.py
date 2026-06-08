from fastapi import APIRouter
from src.api.services.data_service import run_pipeline

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])

@router.post("/run")
def execute_pipeline():
    run_pipeline()
    return {"message": "Pipeline executed successfully"}