from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/version")
async def get_version():
    return {
        "name": "GARD MVP API",
        "version": "0.1.0",
        "environment": "development"
    } 