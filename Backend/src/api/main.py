from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import transactions, metrics, pipeline, health

app = FastAPI(title="Data Pipeline API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router)
app.include_router(metrics.router)
app.include_router(pipeline.router)
app.include_router(health.router)