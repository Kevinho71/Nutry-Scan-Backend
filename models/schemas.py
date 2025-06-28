# models/schemas.py
from datetime import date

from pydantic import BaseModel, EmailStr
from typing import List, Optional

class LoginData(BaseModel):
    email: EmailStr
    contrasena: str


class RegisterData(BaseModel):
    nombre: str
    fecha_nacimiento: date
    genero: str
    enfermedad: str
    email: EmailStr
    contrasena: str
    peso: float
    altura: float