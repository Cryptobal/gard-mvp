#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn main:app --host 0.0.0.0 --port $PORT 