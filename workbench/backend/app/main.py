from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.artifacts import router as artifacts_router
from app.api.cases import router as cases_router
from app.api.execution import router as execution_router
from app.api.integrity import router as integrity_router
from app.api.routing import router as routing_router
from app.models.db import Base
from app.storage.database import engine

app = FastAPI(title="GosseOS Workbench v1 API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(cases_router)
app.include_router(routing_router)
app.include_router(execution_router)
app.include_router(integrity_router)
app.include_router(artifacts_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
