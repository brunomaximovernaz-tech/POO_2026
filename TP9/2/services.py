from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas

class CotizacionService:
    def __init__(self, db: Session):
        self.db = db

    def cotizar(self, peticion: schemas.CotizacionRequest) -> schemas.CotizacionResponse:
        # Escenario 3: Validación de cantidad inválida
        if peticion.cantidad <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La cantidad de entradas solicitadas debe ser mayor a cero"
            )

        # Escenario 2: Cotización rechazada por falta de disponibilidad
        entradas_disponibles = self.db.query(models.Entrada).filter(
            models.Entrada.evento_id == peticion.evento_id,
            models.Entrada.sector_id == peticion.sector_id,
            models.Entrada.estado == models.EstadoEntrada.DISPONIBLE
        ).count()

        if entradas_disponibles < peticion.cantidad:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Capacidad insuficiente o entradas no disponibles"
            )

        # Escenario 1: Cotización exitosa (Camino Feliz)
        # Nota: Como en la Parte 1 no se definió 'precio' en Sector/Evento, fijamos los $12.000 de la HU.
        precio_fijo = 12000.0  
        subtotal_calculado = precio_fijo * peticion.cantidad

        return schemas.CotizacionResponse(
            subtotal=subtotal_calculado,
            mensaje="Cotización exitosa"
        )