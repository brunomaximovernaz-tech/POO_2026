from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()

# ==========================================
# ENDPOINTS CRUD BÁSICOS (PARTE 1)
# ==========================================

@router.post("/lugares/", response_model=schemas.LugarOut, tags=["CRUD Base"])
def crear_lugar(lugar: schemas.LugarCreate, db: Session = Depends(get_db)):
    db_lugar = models.Lugar(nombre=lugar.nombre, direccion=lugar.direccion)
    db.add(db_lugar)
    db.commit()
    db.refresh(db_lugar)
    return db_lugar

@router.get("/lugares/", response_model=List[schemas.LugarOut], tags=["CRUD Base"])
def listar_lugares(db: Session = Depends(get_db)):
    return db.query(models.Lugar).all()
# ==========================================
# ENDPOINTS CRUD: SECTOR Y EVENTO
# ==========================================

@router.post("/sectores/", response_model=schemas.SectorOut, tags=["CRUD Base"])
def crear_sector(sector: schemas.SectorCreate, db: Session = Depends(get_db)):
    db_sector = models.Sector(
        nombre=sector.nombre, 
        capacidad_maxima=sector.capacidad_maxima, 
        lugar_id=sector.lugar_id
    )
    db.add(db_sector)
    db.commit()
    db.refresh(db_sector)
    return db_sector

@router.get("/sectores/", response_model=List[schemas.SectorOut], tags=["CRUD Base"])
def listar_sectores(db: Session = Depends(get_db)):
    return db.query(models.Sector).all()

@router.post("/eventos/", response_model=schemas.EventoOut, tags=["CRUD Base"])
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    db_evento = models.Evento(
        nombre=evento.nombre, 
        fecha=evento.fecha, 
        lugar_id=evento.lugar_id
    )
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

@router.get("/eventos/", response_model=List[schemas.EventoOut], tags=["CRUD Base"])
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(models.Evento).all()
# ==========================================
# CONTROLADORES PREPARADOS PARA LAS HUs
# (Lógica de negocio a implementar por el equipo)
# ==========================================

@router.post("/cotizar", tags=["HU 1 - Cotización"])
def cotizar_entradas():
    """
    Endpoint para cotizar la compra de entradas.
    A implementar en la Parte 2 por Compañero 2.
    """
    raise HTTPException(status_code=501, detail="Endpoint no implementado aún")

@router.post("/iniciar-pago", tags=["HU 2 - Pagos"])
def iniciar_pago():
    """
    Endpoint para procesar el pago con tarjeta.
    A implementar en la Parte 3 por Compañero 3.
    """
    raise HTTPException(status_code=501, detail="Endpoint no implementado aún")

@router.post("/webhook-pagos", tags=["HU 2 - Pagos"])
def webhook_pagos():
    """
    Webhook para confirmación/notificación de la pasarela de pagos.
    A implementar en la Parte 3 por Compañero 3.
    """
    raise HTTPException(status_code=501, detail="Endpoint no implementado aún")

@router.post("/escanear-acceso", tags=["HU 3 - Control de Acceso"])
def escanear_acceso():
    """
    Endpoint para validar el ingreso en puerta mediante QR.
    A implementar en la Parte 4 por Compañero 4.
    """
    raise HTTPException(status_code=501, detail="Endpoint no implementado aún")