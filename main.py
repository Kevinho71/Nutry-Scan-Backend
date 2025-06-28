from fastapi import FastAPI
from routes import scan_ocr, login, registro
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Escaner Productos AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplaza con la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#incluir las rutas
app.include_router(scan_ocr.router, prefix="/scan", tags=["OCR"] )
app.include_router(login.router, prefix="/login", tags=["Login"] )
app.include_router(registro.router, prefix="/register", tags=["Register"] )
