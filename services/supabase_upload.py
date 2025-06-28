import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def subir_imagen(nombre_archivo: str, contenido: bytes, bucket="escaneos") -> str:
    res = supabase.storage.from_(bucket).upload(
        path=nombre_archivo,
        file=contenido,
        file_options={"content-type": "image/png"}
    )

    if hasattr(res, "error") and res.error:
        raise Exception(f"Error al subir imagen: {res.error.message}")

    url = supabase.storage.from_(bucket).get_public_url(nombre_archivo)
    return url
