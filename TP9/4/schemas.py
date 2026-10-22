from pydantic import BaseModel
from typing import Optional, List

# Esquemas para Lugar
class LugarBase(BaseModel):
    nombre: str
    direccion: str

class LugarCreate(LugarBase):
    pass

class LugarOut(LugarBase):
    id: int
    class Config:
        from_attributes = True

# Esquemas para Sector
class SectorBase(BaseModel):
    nombre: str
    capacidad_maxima: int
    lugar_id: int

class SectorCreate(SectorBase):
    pass

class SectorOut(SectorBase):
    id: int
    class Config:
        from_attributes = True

# Esquemas para Evento
class EventoBase(BaseModel):
    nombre: str
    fecha: str
    lugar_id: int

class EventoCreate(EventoBase):
    pass

class EventoOut(EventoBase):
    id: int
    class Config:
        from_attributes = True