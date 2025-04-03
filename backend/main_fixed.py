from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn
import logging
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Configuración directa en lugar de usar pydantic_settings
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CORS_ORIGINS = ["http://localhost:3000"]
APP_NAME = "GARD MVP API"
APP_VERSION = "0.1.0"
ENVIRONMENT = "development"

# Creación de la aplicación FastAPI
app = FastAPI(
    title=APP_NAME,
    description="API para el MVP de GARD",
    version=APP_VERSION,
)

# Middlewares
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=ALLOWED_HOSTS
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints básicos
@app.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/version")
async def get_version():
    """
    Endpoint para obtener la versión de la API.
    """
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    }

if __name__ == "__main__":
    uvicorn.run("main_fixed:app", host="0.0.0.0", port=8000, reload=True) 