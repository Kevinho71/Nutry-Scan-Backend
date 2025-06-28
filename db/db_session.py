from db.database import SessionLocal

# Dependencia para inyectar la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()