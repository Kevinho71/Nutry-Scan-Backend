from sqlalchemy import Column, Integer, String, Date, Float
from db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String, nullable=False)  # Ej: "M", "F", "Otro"
    enfermedad = Column(String, nullable=True)  # Ej: "Diabetes", "Ninguna"
    correo = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)  # ¡Debe estar hasheada!
    peso = Column(Float, nullable=True)
    altura = Column(Float, nullable=True)
    plan = Column(String, default="gratuito")  # "mensual", "anual", etc.
    creado_en = Column(Date, nullable=False)