from fastapi import APIRouter, status
from pydantic import BaseModel

from app.core.settings import get_settings

router = APIRouter(tags=["Version"])
settings = get_settings()

class VersionResponse(BaseModel):
    name: str
    version: str
    environment: str

@router.get("/version", response_model=VersionResponse, status_code=status.HTTP_200_OK)
async def get_version():
    """
    Endpoint para obtener la versión de la API.
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    } 