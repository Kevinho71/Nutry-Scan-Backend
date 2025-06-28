from sqlalchemy import Column, Integer, ForeignKey, DateTime, JSON
from db.database import Base
import datetime

class Escaneo(Base):
    __tablename__ = "escaneos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    datos = Column(JSON, nullable=False)
    imagenes = Column(JSON, nullable=True)  # Nueva columna: array de URLs
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
