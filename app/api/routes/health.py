"""Health check endpoint."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.common import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return basic API health status."""
    return HealthResponse(
        status="healthy", app_name=get_settings().app_name, version="0.1.0"
    )
