from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# --- HU 1: Cotización ---
class CotizacionRequest(BaseModel):
    evento_id: int
    sector_id: int
    cantidad: int

class CotizacionResponse(BaseModel):
    subtotal: float
    mensaje: str


# --- HU 2: Procesamiento de Pago ---
class PagoRequest(BaseModel):
    entradas_ids: List[int]
    total_cotizado: float
    numero_tarjeta: str

class PagoResponse(BaseModel):
    mensaje: str
    venta_id: int
    estado_entradas: str


# --- HU 3: Control de Acceso ---
class EscanearRequest(BaseModel):
    codigo_qr: str

class AccesoResponse(BaseModel):
    mensaje: str
    estado_ticket: str
    hora_ingreso: Optional[datetime] = None