from fastapi import APIRouter, status
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(tags=["Health"])

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime

@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now()
    } 