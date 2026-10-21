from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Entrada
from schemas import EscanearRequest, AccesoResponse
# from database import get_db # Descomentar e importar la dependencia real de la DB

router = APIRouter(prefix="/api/v1/acceso", tags=["Control de Acceso"])

# Dummy get_db para que no tire error de importación (borrar en el proyecto real)
def get_db():
    pass

@router.post("/escanear", response_model=AccesoResponse)
def escanear_acceso(request: EscanearRequest, db: Session = Depends(get_db)):
    # Escenario 3: Ticket Inválido o Inexistente
    entrada = db.query(Entrada).filter(Entrada.codigo_qr == request.codigo_qr).first()
    if not entrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Ticket Inválido o Inexistente"
        )

    try:
        # GRASP: Delegamos la lógica a la entidad
        entrada.registrar_ingreso()
        
        db.commit()
        db.refresh(entrada)
        
        # Escenario 1: Éxito
        return AccesoResponse(
            mensaje="Acceso Permitido",
            estado_ticket=entrada.estado,
            hora_ingreso=entrada.hora_ingreso
        )

    except ValueError as e:
        error_msg = str(e)
        if error_msg == "Entrada ya utilizada":
            # Escenario 2
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_msg)
        elif error_msg == "Ticket no emitido / Falta de pago":
            # Escenario 4
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)
