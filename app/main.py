from fastapi import FastAPI
from app.api.v1.endpoints.civco.civco_api_router import router as api_router

app = FastAPI(title="FastAPI Teafication")

# Include all API routes under /api/v1
app.include_router(api_router, prefix="/api/v1")