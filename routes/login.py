from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from db.db_session import get_db
from models.user_model import Usuario
from models.schemas import LoginData

router = APIRouter()


@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == data.email).first()
    if not usuario or not bcrypt.verify(data.contrasena, usuario.contrasena):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {"success": True, "user_id": usuario.id}