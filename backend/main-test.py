from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Creación de la aplicación FastAPI
app = FastAPI(
    title="GARD MVP API",
    description="API para el MVP de GARD",
    version="0.1.0",
)

# Endpoints básicos para prueba
@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/version")
async def get_version():
    return {
        "name": "GARD MVP API",
        "version": "0.1.0",
        "environment": "development"
    }

if __name__ == "__main__":
    uvicorn.run("main-test:app", host="0.0.0.0", port=8000, reload=True) 