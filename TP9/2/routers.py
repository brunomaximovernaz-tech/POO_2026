from services import CotizacionService # Agregar arriba con los imports

@router.post("/cotizar", response_model=schemas.CotizacionResponse, tags=["HU 1 - Cotización"])
def cotizar_entradas(peticion: schemas.CotizacionRequest, db: Session = Depends(get_db)):
    """
    Endpoint para cotizar la compra de entradas.
    Implementación de la HU 1 por Compañero 2.
    """
    servicio = CotizacionService(db)
    return servicio.cotizar(peticion)