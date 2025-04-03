# GARD MVP

Un proyecto fullstack optimizado para el desarrollo rápido de MVP (Producto Mínimo Viable) utilizando FastAPI para el backend y Next.js 14 con App Router para el frontend.

## 📁 Estructura del Proyecto

```
gard-mvp/
├── backend/             # Proyecto FastAPI
│   ├── app/
│   │   ├── core/        # Configuraciones, DB, settings
│   │   ├── middleware/  # Middlewares personalizados
│   │   ├── models/      # Modelos de SQLAlchemy
│   │   ├── routes/      # Endpoints API
│   │   ├── schemas/     # Esquemas Pydantic
│   │   └── services/    # Lógica de negocio
│   ├── main.py          # Punto de entrada FastAPI
│   └── requirements.txt # Dependencias Python
│
└── frontend/            # Proyecto Next.js 14
    ├── app/             # App Router de Next.js
    │   ├── components/  # Componentes React reutilizables
    │   ├── lib/         # Utilidades y helpers
    │   ├── login/       # Página de login
    │   └── styles/      # Estilos globales y CSS modules
    ├── public/          # Archivos estáticos
    └── package.json     # Dependencias NPM
```

## 🚀 Inicio Rápido

### Backend (FastAPI)

1. Navegar al directorio del backend:
   ```bash
   cd backend
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crear un archivo `.env` basado en `.env.example`

5. Ejecutar el servidor de desarrollo:
   ```bash
   uvicorn main:app --reload
   ```

6. Acceder a la documentación Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend (Next.js)

1. Navegar al directorio del frontend:
   ```bash
   cd frontend
   ```

2. Instalar dependencias:
   ```bash
   npm install
   ```

3. Crear un archivo `.env.local` basado en `.env.example`

4. Ejecutar el servidor de desarrollo:
   ```bash
   npm run dev
   ```

5. Acceder a la aplicación: [http://localhost:3000](http://localhost:3000)

## 🚢 Despliegue

### Backend (Railway)

El proyecto está configurado para desplegarse en Railway. Solo necesitas conectar tu repositorio y Railway detectará automáticamente la configuración.

### Frontend (Vercel)

El proyecto está configurado para desplegarse en Vercel. Conecta tu repositorio y Vercel detectará automáticamente la configuración de Next.js.

## 🛠️ Tecnologías Utilizadas

### Backend
- FastAPI: Framework web rápido
- SQLAlchemy: ORM para bases de datos
- Pydantic: Validación de datos
- Python-dotenv: Gestión de variables de entorno

### Frontend
- Next.js 14: Framework React con App Router
- TailwindCSS: Utilidad CSS para diseño
- next-themes: Soporte para modo oscuro/claro 