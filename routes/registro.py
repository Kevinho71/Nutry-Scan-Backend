from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from passlib.hash import bcrypt
from db.db_session import get_db
from models.user_model import Usuario
from models.schemas import RegisterData

router = APIRouter()

@router.post("/register")
def register(data: RegisterData, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.correo == data.email).first():
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    hashed_password = bcrypt.hash(data.contrasena)

    nuevo_usuario = Usuario(
        nombre=data.nombre,
        fecha_nacimiento=data.fecha_nacimiento,
        genero=data.genero,
        enfermedad=data.enfermedad,
        correo=data.email,
        contrasena=hashed_password,
        peso=data.peso,
        altura=data.altura,
        plan="gratuito",
        creado_en=datetime.utcnow().date()
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"msg": "Usuario registrado exitosamente", "user_id": nuevo_usuario.id}