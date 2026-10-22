from fastapi import FastAPI 
import models
from database import engine
from routers import router

# Crear las tablas en la base de datos SQLite
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartTicket API - Backend",
    description="Plataforma de venta de entradas y control de accesos para eventos",
    version="1.0.0"
)

# Incluir las rutas
app.include_router(router) 