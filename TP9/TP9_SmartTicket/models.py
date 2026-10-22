from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Entrada(Base):
    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True, index=True)
    evento_id = Column(Integer, index=True)
    sector_id = Column(Integer, index=True)
    codigo_qr = Column(String, unique=True, index=True, nullable=False)
    estado = Column(String, nullable=False, default="Disponible") # "Disponible", "Reservada", "Emitida", "Utilizada"
    hora_ingreso = Column(DateTime, nullable=True)

    # GRASP: Experto en Información - La entidad gestiona su propio estado
    def registrar_ingreso(self):
        if self.estado == "Utilizada":
            raise ValueError("Entrada ya utilizada")
        
        if self.estado in ["Reservada", "Disponible"]:
            raise ValueError("Ticket no emitido / Falta de pago")
            
        if self.estado == "Emitida":
            self.estado = "Utilizada"
            self.hora_ingreso = datetime.now()
        else:
            raise ValueError("Estado de ticket desconocido")

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, nullable=False, default="Pendiente") # "Pendiente", "Pagada", "Cancelada"
    total = Column(Float, nullable=False)
    tarjeta = Column(String, nullable=False)

    # GRASP: Experto en Información
    def confirmar_pago(self, pasarela_aprobada: bool):
        if not pasarela_aprobada:
            self.estado = "Cancelada"
            raise ValueError("Pago denegado")
        self.estado = "Pagada"