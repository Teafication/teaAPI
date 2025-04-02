from fastapi import APIRouter
from app.api.v1.endpoints.civco import civco

router = APIRouter()

# Add versioned routers
router.include_router(civco.router, prefix="/civco", tags=["civco"])