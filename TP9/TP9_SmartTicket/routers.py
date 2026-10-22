from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from services import CotizacionService, PagoService

router = APIRouter(prefix="/api/v1", tags=["SmartTicket TP9"])

@router.post("/cotizar", response_model=schemas.CotizacionResponse, tags=["HU 1 - Cotización"])
def cotizar_entradas(peticion: schemas.CotizacionRequest, db: Session = Depends(get_db)):
    servicio = CotizacionService(db)
    return servicio.cotizar(peticion)

@router.post("/iniciar-pago", response_model=schemas.PagoResponse, tags=["HU 2 - Pagos"])
def iniciar_pago(request: schemas.PagoRequest, db: Session = Depends(get_db)):
    servicio = PagoService(db)
    return servicio.procesar_pago(request)

@router.post("/escanear", response_model=schemas.AccesoResponse, tags=["HU 3 - Control de Acceso"])
def escanear_acceso(request: schemas.EscanearRequest, db: Session = Depends(get_db)):
    entrada = db.query(models.Entrada).filter(models.Entrada.codigo_qr == request.codigo_qr).first()
    
    if not entrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Ticket Inválido o Inexistente"
        )

    try:
        entrada.registrar_ingreso()
        
        db.commit()
        db.refresh(entrada)
        
        return schemas.AccesoResponse(
            mensaje="Acceso Permitido",
            estado_ticket=entrada.estado,
            hora_ingreso=entrada.hora_ingreso
        )

    except ValueError as e:
        error_msg = str(e)
        if error_msg == "Entrada ya utilizada":
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_msg)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)