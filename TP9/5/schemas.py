from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EscanearRequest(BaseModel):
    codigo_qr: str

class AccesoResponse(BaseModel):
    mensaje: str
    estado_ticket: str
    hora_ingreso: Optional[datetime] = None
