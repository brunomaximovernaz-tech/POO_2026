from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Entrada(Base):
    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True, index=True)
    codigo_qr = Column(String, unique=True, index=True, nullable=False)
    estado = Column(String, nullable=False) # "Disponible", "Reservada", "Emitida", "Utilizada"
    hora_ingreso = Column(DateTime, nullable=True)

    # GRASP: Experto en Información - La entidad gestiona su propio estado
    def registrar_ingreso(self):
        # Escenario 2: Entrada ya utilizada
        if self.estado == "Utilizada":
            raise ValueError("Entrada ya utilizada")
        
        # Escenario 4: Entrada no pagada
        if self.estado in ["Reservada", "Disponible"]:
            raise ValueError("Ticket no emitido / Falta de pago")
            
        # Escenario 1: Ingreso exitoso
        if self.estado == "Emitida":
            self.estado = "Utilizada"
            self.hora_ingreso = datetime.now()
        else:
            raise ValueError("Estado de ticket desconocido")
