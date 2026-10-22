from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from database import Base

# Definición de Estados de la Entrada
class EstadoEntrada(str, enum.Enum):
    DISPONIBLE = "Disponible"
    RESERVADA = "Reservada"
    EMITIDA = "Emitida"
    UTILIZADA = "Utilizada"

# Definición de Estados de la Venta
class EstadoVenta(str, enum.Enum):
    PENDIENTE = "Pendiente"
    PAGADA = "Pagada"
    CANCELADA = "Cancelada"

class Lugar(Base):
    __tablename__ = "lugares"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)

    sectores = relationship("Sector", back_populates="lugar")
    eventos = relationship("Evento", back_populates="lugar")

class Sector(Base):
    __tablename__ = "sectores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    lugar_id = Column(Integer, ForeignKey("lugares.id"))

    lugar = relationship("Lugar", back_populates="sectores")
    entradas = relationship("Entrada", back_populates="sector")

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha = Column(String, nullable=False)
    lugar_id = Column(Integer, ForeignKey("lugares.id"))

    lugar = relationship("Lugar", back_populates="eventos")
    entradas = relationship("Entrada", back_populates="evento")

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    ventas = relationship("Venta", back_populates="cliente")

class Entrada(Base):
    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True, index=True)
    codigo_qr = Column(String, unique=True, nullable=True)
    estado = Column(Enum(EstadoEntrada), default=EstadoEntrada.DISPONIBLE)
    hora_ingreso = Column(DateTime, nullable=True)
    
    sector_id = Column(Integer, ForeignKey("sectores.id"))
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=True)

    sector = relationship("Sector", back_populates="entradas")
    evento = relationship("Evento", back_populates="entradas")
    venta = relationship("Venta", back_populates="entradas")

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    monto_total = Column(Float, nullable=False)
    estado = Column(Enum(EstadoVenta), default=EstadoVenta.PENDIENTE)
    
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="ventas")
    entradas = relationship("Entrada", back_populates="venta")