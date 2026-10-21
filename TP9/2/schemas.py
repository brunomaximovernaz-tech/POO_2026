class CotizacionRequest(BaseModel):
    evento_id: int
    sector_id: int
    cantidad: int

class CotizacionResponse(BaseModel):
    subtotal: float
    mensaje: str