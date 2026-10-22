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
            models.Entrada.estado == "Disponible"
        ).count()

        if entradas_disponibles < peticion.cantidad:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Capacidad insuficiente o entradas no disponibles"
            )

        # Escenario 1: Cotización exitosa (Camino Feliz)
        precio_fijo = 12000.0  
        subtotal_calculado = precio_fijo * peticion.cantidad

        return schemas.CotizacionResponse(
            subtotal=subtotal_calculado,
            mensaje="Cotización exitosa"
        )


class PagoService:
    def __init__(self, db: Session):
        self.db = db

    def procesar_pago(self, request: schemas.PagoRequest) -> schemas.PagoResponse:
        entradas = self.db.query(models.Entrada).filter(models.Entrada.id.in_(request.entradas_ids)).all()

        # Escenario 3: Problema de Concurrencia
        for entrada in entradas:
            if entrada.estado != "Disponible":
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Los lugares seleccionados ya no se encuentran disponibles"
                )

        # Simulamos pasarela (Escenario 1 y 2): Si termina en "0000", rechaza.
        pasarela_aprobada = not request.numero_tarjeta.endswith("0000")

        nueva_venta = models.Venta(total=request.total_cotizado, tarjeta=request.numero_tarjeta[-4:])
        self.db.add(nueva_venta)

        try:
            # GRASP: Delegamos a la entidad Venta
            nueva_venta.confirmar_pago(pasarela_aprobada)
            
            # Cambiamos estado de entradas a Emitida
            for entrada in entradas:
                entrada.estado = "Emitida"
            
            self.db.commit()
            self.db.refresh(nueva_venta)
            
            return schemas.PagoResponse(
                mensaje="Pago aprobado y entradas emitidas",
                venta_id=nueva_venta.id,
                estado_entradas="Emitida"
            )

        except ValueError as e:
            self.db.rollback() 
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )